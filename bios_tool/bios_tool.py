import argparse
import logging
import sys
import traceback
import redfish
import yaml

from wekapyutils.wekalogging import configure_logging, register_module
from RedFishBMC import RedFishBMC, trim_supermicro_dict
from BMCsetup import bmc_setup
from tabulate import tabulate

log = logging.getLogger()

def csv_load(f):
    import csv
    reader = csv.DictReader(f)
    return {"hosts": list(reader)}

def _load_config(inputfile):
    with open(inputfile) as f:
        if inputfile.endswith(".csv"):
            return csv_load(f)
        return yaml.load(f, Loader=yaml.FullLoader)

def _generate_config(bmc_ips, bmc_username, bmc_password):
    return {
        "hosts": [
            {"name": ip, "user": bmc_username[0], "password": bmc_password[0]}
            for ip in bmc_ips
        ]
    }

def main():
    parser = argparse.ArgumentParser(description="View/Change BIOS Settings on servers")
    parser.add_argument("-c", "--hostconfigfile", type=str, default="host_config.csv")
    parser.add_argument("-b", "--bios", type=str, default="bios_settings.yml")
    parser.add_argument("--arch", choices=["Intel", "AMD"], help="Override CPU architecture detection")
    parser.add_argument("--bmc_config", action="store_true")
    parser.add_argument("--fix", action="store_true")
    parser.add_argument("--reboot", action="store_true")
    parser.add_argument("--dump", action="store_true")
    parser.add_argument("--reset_bios", action="store_true")
    parser.add_argument("--diff", nargs=2, default=False)
    parser.add_argument("--bmc_ips", type=str, nargs="*", default=None)
    parser.add_argument("--bmc_username", type=str, nargs=1, default=None)
    parser.add_argument("--bmc_password", type=str, nargs=1, default=None)
    parser.add_argument("-v", "--verbose", dest='verbosity', action='store_true')
    parser.add_argument("--version", action='store_true')

    args = parser.parse_args()

    if args.version:
        print("bios_tool.py version 2024.08.15")
        sys.exit(0)

    register_module("RedFishBMC", logging.INFO)
    configure_logging(log, args.verbosity)

    if args.bmc_ips:
        if args.bmc_username is None or args.bmc_password is None:
            log.error("You must provide a username and password when using --bmc_ips")
            sys.exit(1)
        conf = _generate_config(args.bmc_ips, args.bmc_username, args.bmc_password)
    else:
        try:
            conf = _load_config(args.hostconfigfile)
        except Exception as exc:
            log.error(f"Unable to open host configuration file: {exc}")
            sys.exit(1)

    try:
        desired_bios_settings = _load_config(args.bios)
    except Exception as exc:
        log.error(f"Unable to parse bios settings configuration file: {exc}")
        sys.exit(1)

    hostlist = conf["hosts"] if not args.diff else [x for x in conf["hosts"] if x["name"] in args.diff]
    redfish_list = []

    for host in hostlist:
        try:
            redfish_list.append(RedFishBMC(host["name"], username=host["user"], password=host["password"], arch_override=args.arch))
        except Exception as exc:
            log.error(f"Error opening connections to {host['name']}: {exc}")
            print(traceback.format_exc())

    for bmc in redfish_list:
        if args.dump:
            bmc.print_settings()
            continue
        elif args.reset_bios:
            bmc.reset_settings_to_default()
            if args.reboot:
                bmc.reboot()
        else:
            count = bmc.check_settings(desired_bios_settings[bmc.vendor][bmc.arch])
            if count > 0 and args.fix:
                bmc.change_settings(desired_bios_settings[bmc.vendor][bmc.arch])
                if args.reboot:
                    bmc.reboot()

    for bmc in redfish_list:
        bmc.redfish.logout()

if __name__ == "__main__":
    main()