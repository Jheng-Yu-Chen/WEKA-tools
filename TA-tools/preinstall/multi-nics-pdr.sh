#!/bin/bash

### Examples ###
#[root@weka01 ~]# yum install NetworkManager-config-routing-rules iproute -y
#[root@weka01 ~]# systemctl enable NetworkManager-dispatcher.service --now
#
#[root@weka01 ~]# ip -br addr show enp1s15
#enp1s15          UP             172.21.102.163/22
#[root@weka01 ~]# grep enp1s15 /etc/iproute2/rt_tables
#1018 enp1s15
#[root@weka01 ~]# cat /etc/sysconfig/network-scripts/route-enp1s15
#172.21.102.0/22 dev enp1s15 src 172.21.102.163 table enp1s15
#default via 172.21.102.163 dev enp1s15 table enp1s15
#[root@weka01 ~]# cat /etc/sysconfig/network-scripts/rule-enp1s15
#table enp1s15 from 172.21.102.163
###

set -e

# Define the starting table ID for custom tables
BASE_TABLE_ID=100

# Paths
RT_TABLES_FILE="/etc/iproute2/rt_tables"
NETWORK_SCRIPTS_DIR="/etc/sysconfig/network-scripts"

# Check if at least one NIC is provided
if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <nic1> [nic2 ... nicN]"
  exit 1
fi

# Function to add a route table if it doesn't exist
add_route_table() {
  local table_name="$1"
  local table_id="$2"

  if ! grep -q " $table_name$" "$RT_TABLES_FILE"; then
    echo "$table_id $table_name" >> "$RT_TABLES_FILE"
    echo "Added route table $table_name with ID $table_id to $RT_TABLES_FILE"
  fi
}

# Main loop for each NIC
for idx in "$@"; do
  nic="$idx"
  ip_info=$(ip -4 addr show "$nic" 2>/dev/null | grep -oP '(?<=inet\s)\d+\.\d+\.\d+\.\d+/\d+')

  if [ -z "$ip_info" ]; then
    echo "Skipping $nic: No IP address assigned."
    continue
  fi

  ip_address=$(echo "$ip_info" | cut -d'/' -f1)
  subnet=$(echo "$ip_info" | cut -d'/' -f2)

  table_name="$nic"
  table_id=$BASE_TABLE_ID

  # Increment table ID for the next NIC
  BASE_TABLE_ID=$((BASE_TABLE_ID + 1))

  # Ensure the route table is added
  add_route_table "$table_name" "$table_id"


  # Configure route file
  route_file="$NETWORK_SCRIPTS_DIR/route-$nic"
  cat > "$route_file" << EOF
${ip_address%.*}.0/$subnet dev $nic src $ip_address table $table_name
default via $ip_address dev $nic table $table_name
EOF
  echo "Configured $route_file"


  # Configure rule file
  rule_file="$NETWORK_SCRIPTS_DIR/rule-$nic"
  cat > "$rule_file" << EOF
table $table_name from $ip_address
EOF
  echo "Configured $rule_file"

done

# Apply the changes using NetworkManager
for idx in "$@"; do
  nic="$idx"
  ip_info=$(ip -4 addr show "$nic" 2>/dev/null | grep -oP '(?<=inet\s)\d+\.\d+\.\d+\.\d+/\d+')

  if [ -z "$ip_info" ]; then
    continue
  fi

  echo "Applying configuration for $nic..."
  nmcli con reload
  nmcli con down "$nic"
  nmcli con up "$nic"
done

echo "Policy-based routing configuration completed."
