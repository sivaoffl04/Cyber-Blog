#!/usr/bin/env python3
"""
Stuxnet Case Study: S7comm Protocol & Industrial Control Audit Tool
==================================================================
This educational audit and simulation script analyzes industrial environments
for indicators of Stuxnet-style cyber-physical sabotage:
  1. S7comm Network Traffic Inspector (ISO-on-TCP Port 102 Block Injections)
  2. Siemens STEP 7 DLL Proxy Integrity Auditor (s7otbxdx.dll / s7otbxsx.dll)
  3. Variable Frequency Drive (VFD) Resonance & Rotor Stress Calculator

Usage:
  python stuxnet_s7comm_audit.py --mode all
  python stuxnet_s7comm_audit.py --mode s7comm-audit
  python stuxnet_s7comm_audit.py --mode dll-check
  python stuxnet_s7comm_audit.py --mode resonance-calc --freq 1410
"""

import sys
import os
import json
import time
from datetime import datetime, timedelta, timezone

# ANSI Color Codes for terminal formatting
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner():
    banner = f"""
{CYAN}{BOLD}===============================================================================
  STUXNET CASE STUDY: S7COMM PROTOCOL & INDUSTRIAL CONTROL AUDIT TOOL
  Simulating Cyber-Physical Sabotage, S7comm Hooking & Resonance Physics
==============================================================================={RESET}
"""
    print(banner)


def generate_sample_s7comm_packets():
    """Generates synthetic S7comm protocol packets simulating Stuxnet's injection activity."""
    base_time = datetime.now(timezone.utc) - timedelta(minutes=30)
    
    packets = [
        # Packet 1: Normal cyclic data read
        {
            "packet_id": 101,
            "timestamp": (base_time).isoformat() + "Z",
            "src_ip": "192.168.1.50",  # WinCC HMI
            "dst_ip": "192.168.1.10",  # Siemens S7-315 PLC
            "dst_port": 102,
            "s7_func": "0x04 (Read Var)",
            "block_target": "DB1 (Process Variables)",
            "length_bytes": 54,
            "status": "NORMAL"
        },
        # Packet 2: Unauthorized block download request (Function 0x1A)
        {
            "packet_id": 102,
            "timestamp": (base_time + timedelta(minutes=4)).isoformat() + "Z",
            "src_ip": "192.168.1.45",  # Compromised Engineering Workstation
            "dst_ip": "192.168.1.10",  # S7-315 PLC
            "dst_port": 102,
            "s7_func": "0x1A (Request Download Block)",
            "block_target": "OB1 (Main Execution Loop Splicing)",
            "length_bytes": 188,
            "status": "SUSPICIOUS"
        },
        # Packet 3: Injected interrupt routine (OB35 100ms timer)
        {
            "packet_id": 103,
            "timestamp": (base_time + timedelta(minutes=4, seconds=5)).isoformat() + "Z",
            "src_ip": "192.168.1.45",
            "dst_ip": "192.168.1.10",
            "dst_port": 102,
            "s7_func": "0x1A (Request Download Block)",
            "block_target": "OB35 (High-Precision 100ms Interrupt)",
            "length_bytes": 240,
            "status": "MALICIOUS"
        },
        # Packet 4: Creation of covert Data Block (DB89 for sensor replay buffer)
        {
            "packet_id": 104,
            "timestamp": (base_time + timedelta(minutes=4, seconds=12)).isoformat() + "Z",
            "src_ip": "192.168.1.45",
            "dst_ip": "192.168.1.10",
            "dst_port": 102,
            "s7_func": "0x1A (Request Download Block)",
            "block_target": "DB89 (Covert Telemetry Buffer Storage)",
            "length_bytes": 1024,
            "status": "MALICIOUS"
        },
        # Packet 5: Parameter write to Variable Frequency Drive
        {
            "packet_id": 105,
            "timestamp": (base_time + timedelta(minutes=15)).isoformat() + "Z",
            "src_ip": "192.168.1.10",  # S7-315 to Profibus Bus
            "dst_ip": "Profibus Node 4 (Fararo Paya VFD)",
            "dst_port": 102,
            "s7_func": "0x05 (Write Var - DP_SEND)",
            "block_target": "VFD Output Frequency: 1,410 Hz (84,600 RPM)",
            "length_bytes": 68,
            "status": "SABOTAGE_OVERSPEED"
        }
    ]
    return packets


def audit_s7comm_traffic(packets):
    """Inspects S7comm network packets for unauthorized PLC bytecode download commands."""
    print(f"\n{BOLD}{CYAN}=== 1. S7COMM INDUSTRIAL PROTOCOL DEEP PACKET INSPECTION ==={RESET}")
    print(f"[*] Ingested {len(packets)} S7comm packets over ISO-on-TCP (Port 102). Analyzing...\n")

    alerts = []
    for pkt in packets:
        func = pkt["s7_func"]
        target = pkt["block_target"]
        src = pkt["src_ip"]
        dst = pkt["dst_ip"]
        
        if "0x1A" in func:
            severity = "CRITICAL" if any(b in target for b in ("OB1", "OB35", "DB89")) else "HIGH"
            color = RED if severity == "CRITICAL" else YELLOW
            alerts.append({
                "severity": severity,
                "packet_id": pkt["packet_id"],
                "rule": "RULE-S7COMM-001: Unauthorized S7comm Block Download Command",
                "details": f"Workstation [{src}] executed '{func}' targeting block '{target}' on PLC [{dst}].",
                "target": target
            })
            print(f"[{color}{BOLD}ALERT: S7COMM INJECTION{RESET}] {target} written to PLC [{dst}] from [{src}]")

        elif "SABOTAGE_OVERSPEED" in pkt["status"]:
            alerts.append({
                "severity": "FATAL",
                "packet_id": pkt["packet_id"],
                "rule": "RULE-S7COMM-002: Abnormal Variable Frequency Drive Speed Command",
                "details": f"PLC command forced VFD output to 1,410 Hz! Exceeds maximum mechanical tolerance.",
                "target": target
            })
            print(f"[{RED}{BOLD}FATAL: VFD OVERSPEED{RESET}] Malicious frequency modification detected: {target}")
        else:
            print(f"[{GREEN}NORMAL TRAFFIC{RESET}] Packet #{pkt['packet_id']}: {func} -> {target}")

    print(f"\n{BOLD}S7comm DPI Findings Summary:{RESET}")
    for idx, a in enumerate(alerts, 1):
        c = RED if a["severity"] in ("CRITICAL", "FATAL") else YELLOW
        print(f"  {idx}. [{c}{a['severity']}{RESET}] {BOLD}{a['rule']}{RESET}")
        print(f"     Details: {a['details']}")
    return alerts


def audit_step7_dll_integrity():
    """Simulates Siemens STEP 7 DLL proxying detection (s7otbxdx.dll / s7otbxsx.dll)."""
    print(f"\n{BOLD}{CYAN}=== 2. SIEMENS SIMATIC STEP 7 DLL PROXY AUDITOR ==={RESET}")
    print("[*] Inspecting Siemens communication libraries in %CommonProgramFiles%\\Siemens\\S7Common\\...")

    # Simulated file system checks
    simulated_files = [
        {
            "filename": "s7otbxdx.dll",
            "size_bytes": 482912,
            "sha256": "4020a65cf23381e4b9f2eb430d41829e88419bcf819448102fcae1281489012a",
            "signed_by": "UNSIGNED / CORRUPT CHECKSUM",
            "hooked_exports": ["s7blk_read", "s7blk_write", "s7blk_delete"],
            "status": "MALICIOUS_STUXNET_WRAPPER"
        },
        {
            "filename": "s7otbxsx.dll",
            "size_bytes": 524288,
            "sha256": "12984afc498102ebba948123019842aef9120489128491024810928410294810",
            "signed_by": "Siemens AG (Valid WHQL)",
            "hooked_exports": [],
            "status": "LEGITIMATE_RENAMED_ORIGINAL"
        }
    ]

    print(f"\n{'Target Filename':<20} | {'Digital Signature':<25} | {'Hook Status':<20} | {'Finding'}")
    print("-" * 80)
    for f in simulated_files:
        if f["status"] == "MALICIOUS_STUXNET_WRAPPER":
            finding = f"{RED}{BOLD}STUXNET PROXY DLL{RESET}"
            hooks = f"{len(f['hooked_exports'])} Exports Hooked"
        else:
            finding = f"{YELLOW}RENAMED ORIGINAL{RESET}"
            hooks = "Clean"
        print(f"{f['filename']:<20} | {f['signed_by']:<25} | {hooks:<20} | {finding}")

    print("-" * 80)
    print(f"[{RED}{BOLD}CRITICAL MITM DETECTED{RESET}] Siemens communication library has been proxied!")
    print(f"  * Malicious file 's7otbxdx.dll' intercepts all 's7blk_read' and 's7blk_write' calls.")
    print(f"  * Legitimate library was renamed to 's7otbxsx.dll' to maintain proxy passthrough.")
    print(f"  * Action Required: Quarantine both DLLs and restore STEP 7 from vendor optical media.\n")


def calculate_centrifuge_rotor_stress(frequency_hz=1410):
    """Calculates mechanical stress increase and harmonic resonance risks on IR-1 centrifuge rotors."""
    print(f"\n{BOLD}{CYAN}=== 3. CENTRIFUGE ROTOR RESONANCE & MECHANICAL STRESS CALCULATOR ==={RESET}")
    print(f"[*] Evaluating centrifuge rotational dynamics for VFD output: {BOLD}{frequency_hz} Hz{RESET}")

    normal_freq = 1064.0  # Normal steady-state speed
    normal_rpm = normal_freq * 60.0
    actual_rpm = frequency_hz * 60.0

    # Centrifugal stress is proportional to the square of angular velocity (omega^2)
    stress_ratio = (frequency_hz / normal_freq) ** 2
    percentage_change = (stress_ratio - 1.0) * 100.0

    print(f"\n  * Normal Operating Speed : {normal_freq:.0f} Hz ({normal_rpm:,.0f} RPM)")
  
    if frequency_hz > normal_freq:
        status_label = f"{RED}{BOLD}DANGEROUS OVERSPEED{RESET}"
        stress_desc = f"Radial tensile stress increases by +{percentage_change:.1f}%! Exceeds yield limit of Aluminum 7075-T6."
    elif frequency_hz < 100:
        status_label = f"{RED}{BOLD}CRITICAL HARMONIC RESONANCE CRASH{RESET}"
        stress_desc = f"Dwell time inside critical resonance band (~350 Hz to ~800 Hz) causes violent lateral rotor collision."
    else:
        status_label = f"{GREEN}NOMINAL OPERATING RANGE{RESET}"
        stress_desc = "Centrifuge rotor operating within safe hydrodynamic boundary limits."

    print(f"  * Current Command Speed  : {frequency_hz:.0f} Hz ({actual_rpm:,.0f} RPM) -> {status_label}")
    print(f"  * Calculated Stress Load : {stress_ratio:.2f}x Baseline")
    print(f"  * Physical Consequence   : {stress_desc}")

    # Resonance spectrum zones for IR-1 centrifuge
    print(f"\n{BOLD}IR-1 Centrifuge Harmonic Spectrum Matrix:{RESET}")
    spectrum = [
        {"range": "0 - 100 Hz", "zone": "Sub-Critical Run-up", "risk": "Low"},
        {"range": "300 - 450 Hz", "zone": "First Critical Resonance Node", "risk": "FATAL (Severe Vibration)"},
        {"range": "750 - 900 Hz", "zone": "Second Critical Resonance Node", "risk": "FATAL (Bellows Buckling)"},
        {"range": "1,000 - 1,100 Hz", "zone": "Supercritical Steady-State Cruise", "risk": "OPTIMAL (Normal)"},
        {"range": "> 1,350 Hz", "zone": "Centrifugal Tensile Burst Limit", "risk": "FATAL (Casing Rupture)"}
    ]
    for s in spectrum:
        color = RED if "FATAL" in s["risk"] else (GREEN if "OPTIMAL" in s["risk"] else YELLOW)
        print(f"  [{color}{s['risk']:<28}{RESET}] {s['range']:<18} | {s['zone']}")


def main():
    print_banner()
    mode = "all"
    freq = 1410

    if len(sys.argv) > 1 and sys.argv[1] == "--mode" and len(sys.argv) > 2:
        mode = sys.argv[2]
    if "--freq" in sys.argv:
        try:
            f_idx = sys.argv.index("--freq")
            freq = float(sys.argv[f_idx + 1])
        except (ValueError, IndexError):
            freq = 1410

    if mode in ("all", "s7comm-audit"):
        packets = generate_sample_s7comm_packets()
        audit_s7comm_traffic(packets)

    if mode in ("all", "dll-check"):
        audit_step7_dll_integrity()

    if mode in ("all", "resonance-calc"):
        calculate_centrifuge_rotor_stress(freq)

    print(f"\n{BOLD}{GREEN}*** Stuxnet ICS Diagnostic & Simulation Run Completed Successfully ***{RESET}\n")


if __name__ == "__main__":
    main()
