#!/bin/bash

DESCRIPTION="Checking CPU C-state and P-state configuration"
SCRIPT_TYPE="parallel"

check_pstates() {
    pstates_output=$(cpupower frequency-info 2>/dev/null)
    if [[ $? -ne 0 ]]; then
        echo "Failed to run cpupower frequency-info"
        return 1
    fi

    if echo "$pstates_output" | grep -q 'Pstate-P1'; then
        echo "✅ Limited P-states (P0–P2) → Likely BIOS setting: P-state 1 & 2 Disabled"
    else
        echo "⚠️  P-states beyond P0–P2 detected or unsupported"
        return 254
    fi

    if echo "$pstates_output" | grep -q 'Boost States: 0'; then
        echo "✅ Boost state disabled"
    else
        echo "⚠️  Boost state is enabled"
        return 254
    fi
    return 0
}

check_cstates() {
    cstates_output=$(cpupower idle-info 2>/dev/null)
    if [[ $? -ne 0 ]]; then
        echo "Failed to run cpupower idle-info"
        return 1
    fi

    idle_states=$(echo "$cstates_output" | grep -E 'Available idle states:' | cut -d: -f2 | tr -d ' ')
    if [[ "$idle_states" == "POLLC1" ]]; then
        echo "✅ Only C1 state available → Likely BIOS setting: GlobalC_stateControl & DFCstates Disabled"
        return 0
    else
        echo "⚠️  Higher C-states detected: $idle_states"
        return 254
    fi
}

check_pstates || ret=$?
check_cstates || [[ $ret -eq 0 ]] || ret=$?

exit ${ret:-0}
