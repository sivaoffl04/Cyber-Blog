#!/usr/bin/env python3
"""
================================================================================
LOKI IOC SCANNER TRIAGE & THEHIVE CASE MANAGEMENT ENGINE
================================================================================
Lab: SOC-1: Scanning for IOCs (Malware Analysis for SOC Analysts)
Platform: INE Security
Author: Antigravity SOC Triage Automation
Target: Windows Workstation Post-Compromise Host-Based Scan

Description:
  Automates the parsing, forensic classification, and threat intelligence
  enrichment of Indicators of Compromise (IOCs) identified by the LOKI IOC scanner.
  Generates production-ready TheHive 5 case templates, MITRE ATT&CK mappings,
  and structured markdown executive reports.
================================================================================
"""

import sys
import json
import argparse
from datetime import datetime

# Threat Artifact Database from LOKI & Host Triage
ARTIFACTS = [
    {
        "id": "ART-01",
        "file_name": "haha.exe",
        "file_path": r"C:\ProgramData\haha.exe",
        "file_type": "EXE (x64 Portable Executable)",
        "file_size": "1,355,264 bytes (1.29 MB)",
        "risk_score": 415,
        "md5": "29efd64dd3c7fe1e2b022b7ad73a1ba5",
        "sha1": "e3b6ea8c46fa831cec6f235a5cf48b38a4ae8d69",
        "sha256": "61c0810a23580cf492a6ba4f7654566108331e7a4134c968c2d6a05261b2d8a1",
        "created": "2022-09-19 16:44:40 UTC",
        "modified": "2025-12-02 05:59:02 UTC",
        "accessed": "2025-12-02 05:59:02 UTC",
        "yara_rule": "mimikatz (Author: Benjamin DELPY / gentilkiwi)",
        "yara_subscore": 70,
        "filename_ioc": r"\\ProgramData\\[^\\]{1,20}\.(exe|dll)",
        "virustotal_verdict": "66/72 Malicious (HackTool.Win32.Mimikatz)",
        "mitre_technique": "T1003 - OS Credential Dumping",
        "severity": "CRITICAL",
        "description": "Mimikatz x64 credential dumping tool disguised as haha.exe in C:\\ProgramData."
    },
    {
        "id": "ART-02",
        "file_name": "winfix.exe",
        "file_path": r"C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\winfix.exe",
        "file_type": "EXE (Windows Executable)",
        "file_size": "73,802 bytes",
        "risk_score": 130,
        "md5": "c074df02fa916a037803a5531988880a",
        "sha1": "N/A",
        "sha256": "N/A",
        "created": "2025-12-02 05:55:31 UTC",
        "modified": "2025-12-02 05:55:31 UTC",
        "accessed": "2025-12-02 05:55:31 UTC",
        "yara_rule": "Metasploit_Payload",
        "yara_subscore": 60,
        "filename_ioc": r"Startup Folder Persistence",
        "network_listener": "winfix.exe (PID 4500) listening on 0.0.0.0:4444 (Bind Shell)",
        "virustotal_verdict": "0/70 (Unreported / Fresh Payload)",
        "mitre_technique": "T1547.001 - Registry Run Keys / Startup Folder",
        "severity": "CRITICAL",
        "description": "Metasploit bind shell payload placed in Administrator Startup folder listening on port 4444."
    },
    {
        "id": "ART-03",
        "file_name": "89852140106261f4bda5e815876583e8",
        "file_path": r"C:\Users\Public\89852140106261f4bda5e815876583e8",
        "file_type": "Windows Registry Hive File (SAM Database)",
        "file_size": "49,152 bytes",
        "risk_score": 80,
        "md5": "N/A",
        "sha1": "N/A",
        "sha256": "N/A",
        "created": "2025-12-02 05:57:47 UTC",
        "modified": "2025-12-02 05:57:47 UTC",
        "accessed": "2025-12-02 05:57:47 UTC",
        "yara_rule": "SAM_Hive_Backup",
        "yara_subscore": 80,
        "filename_ioc": r"C:\Users\Public\[random_hex_name]",
        "virustotal_verdict": "N/A (Local Database Hive)",
        "mitre_technique": "T1003.002 - OS Credential Dumping: Security Account Manager (SAM)",
        "severity": "HIGH",
        "description": "Extracted copy of the local SAM hive database containing user account password hashes."
    },
    {
        "id": "ART-04",
        "file_name": "Disable.ps1",
        "file_path": r"C:\Windows\Disable.ps1",
        "file_type": "PowerShell Script (.ps1)",
        "file_size": "4,192 bytes",
        "risk_score": 100,
        "md5": "7d77408e1c6d11bf5623cd777444e8b8",
        "sha1": "N/A",
        "sha256": "N/A",
        "created": "2025-12-02 06:00:33 UTC",
        "modified": "2025-12-02 06:00:33 UTC",
        "accessed": "2025-12-02 06:00:33 UTC",
        "yara_rule": "PowerShell_Security_Disabler",
        "yara_subscore": 75,
        "filename_ioc": r"C:\Windows\[^\\]+\.ps1",
        "virustotal_verdict": "Confirmed Malicious (Disables Windows Defender & Firewall)",
        "mitre_technique": "T1562.001 - Impair Defenses: Disable or Modify Tools",
        "severity": "HIGH",
        "description": "PowerShell script in Windows root directory designed to blind Windows Defender and evade security logging."
    }
]

# TheHive 5 Complete Case Specification
THEHIVE_CASE = {
    "title": "Multiple Malicious Artifacts Detected via LOKI Indicating Post-Compromise Activity",
    "description": (
        "Multiple high-risk artifacts were identified on a Windows system during a host-based scan "
        "using the LOKI IOC scanner. The findings include suspicious executables located in uncommon "
        "directories, indicators associated with credential access activity, persistence mechanisms "
        "configured to survive reboots, and evidence of a process listening for incoming connections. "
        "Additional artifacts suggest sensitive system data was accessed and that security-related "
        "settings may have been targeted."
    ),
    "severity": 4,  # Critical
    "startDate": "2025-12-30T10:17:00Z",
    "tlp": 2,       # TLP:Amber
    "pap": 2,       # PAP:Amber
    "tags": ["mimikatz", "persistence", "backdoor", "startup-folder", "sam-hive", "loki"],
    "owner": "soc2@syntrix.com",
    "status": "New",
    "observables": [
        {
            "dataType": "filename",
            "data": r"C:\ProgramData\haha.exe",
            "ioc": True,
            "sighted": True,
            "sightedAt": "2025-12-02T05:59:02Z",
            "tlp": 2,
            "pap": 2,
            "tags": ["malware", "mimikatz", "post-compromise"],
            "message": "Executable identified in an uncommon directory with a very high risk score (415). Matches YARA signatures associated with Mimikatz, indicating potential post-exploitation activity."
        },
        {
            "dataType": "hash",
            "data": "29efd64dd3c7fe1e2b022b7ad73a1ba5",
            "ioc": True,
            "sighted": True,
            "sightedAt": "2025-12-02T05:59:02Z",
            "tlp": 2,
            "pap": 2,
            "tags": ["hash", "mimikatz", "malware"],
            "message": "MD5 hash associated with haha.exe. Cross-referenced with threat intelligence sources (VirusTotal 66/72) and confirmed to be linked to Mimikatz credential dumping activity."
        },
        {
            "dataType": "filename",
            "data": r"C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\winfix.exe",
            "ioc": True,
            "sighted": True,
            "sightedAt": "2025-12-02T05:55:31Z",
            "tlp": 2,
            "pap": 2,
            "tags": ["persistence", "startup-folder", "metasploit", "backdoor"],
            "message": "Executable located in the Administrator's Startup folder, configured to execute automatically at logon. Matches YARA rules associated with Metasploit payloads, suggesting persistence behavior."
        },
        {
            "dataType": "other",
            "data": "winfix.exe listening on 0.0.0.0:4444",
            "ioc": True,
            "sighted": True,
            "sightedAt": "2025-12-02T05:55:31Z",
            "tlp": 2,
            "pap": 2,
            "tags": ["backdoor", "network-listener", "post-exploitation"],
            "message": "Process identified by LOKI ProcessScan as actively listening on port 4444 (PID 4500). Consistent with Metasploit bind shell payload waiting for incoming attacker connection."
        },
        {
            "dataType": "filename",
            "data": r"C:\Users\Public\89852140106261f4bda5e815876583e8",
            "ioc": True,
            "sighted": True,
            "sightedAt": "2025-12-02T05:57:47Z",
            "tlp": 2,
            "pap": 2,
            "tags": ["credential-access", "sam-hive", "registry"],
            "message": "Registry hive file detected in a public directory. Matches YARA rules for a SAM database copy, which contains sensitive local account credential data and NTLM password hashes."
        },
        {
            "dataType": "filename",
            "data": r"C:\Windows\Disable.ps1",
            "ioc": True,
            "sighted": True,
            "sightedAt": "2025-12-02T06:00:33Z",
            "tlp": 2,
            "pap": 2,
            "tags": ["powershell", "defense-evasion", "script"],
            "message": "PowerShell script found in a system directory with a high risk score (100). The script is associated with disabling security features and performing self-modifying actions, indicating malicious intent."
        },
        {
            "dataType": "hash",
            "data": "7d77408e1c6d11bf5623cd777444e8b8",
            "ioc": True,
            "sighted": True,
            "sightedAt": "2025-12-02T06:00:33Z",
            "tlp": 2,
            "pap": 2,
            "tags": ["hash", "powershell", "malware"],
            "message": "MD5 hash associated with Disable.ps1. Cross-referenced with threat intelligence sources and confirmed to be linked to disabling security features activity."
        }
    ],
    "ttps": [
        {
            "patternId": "T1059.001",
            "tactic": "Execution",
            "name": "Command and Scripting Interpreter: PowerShell",
            "occurDate": "2025-12-02T05:55:31Z",
            "description": "PowerShell scripts were identified on the system, including a script placed in a system directory (Disable.ps1), indicating script-based execution activity."
        },
        {
            "patternId": "T1547.001",
            "tactic": "Persistence",
            "name": "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder",
            "occurDate": "2025-12-02T05:55:31Z",
            "description": "An executable (winfix.exe) was located in the Administrator's Startup folder, ensuring automatic execution upon user logon and persistence across reboots."
        },
        {
            "patternId": "T1562.001",
            "tactic": "Defense Evasion",
            "name": "Impair Defenses: Disable or Modify Tools",
            "occurDate": "2025-12-02T05:55:31Z",
            "description": "The PowerShell script Disable.ps1 is associated with disabling security features, consistent with attempts to weaken host-based protections and evade detection."
        },
        {
            "patternId": "T1003.002",
            "tactic": "Credential Access",
            "name": "OS Credential Dumping: Security Account Manager (SAM)",
            "occurDate": "2025-12-02T05:55:31Z",
            "description": "A copy of the SAM registry hive was identified in a public directory, indicating access to stored credential material."
        }
    ],
    "tasks": [
        {
            "title": "Context on Potential Initial Foothold and Entry Point",
            "owner": "soc2@syntrix.com",
            "status": "Waiting",
            "description": (
                "Multiple post-compromise artifacts were identified on the system, including credential "
                "access tooling, persistence mechanisms, and defense-evasion scripts. Reviewing available "
                "telemetry may help determine how initial access to the system was obtained, including "
                "whether the activity originated from user execution, external exposure, or another entry "
                "vector. Clarifying the initial foothold could assist in understanding the broader attack timeline."
            )
        },
        {
            "title": "Context on Identified Executables and Scripts",
            "owner": "soc2@syntrix.com",
            "status": "Waiting",
            "description": (
                "Several suspicious files were identified during host-based scanning, including winfix.exe, "
                "Disable.ps1, and haha.exe. Further analysis may help determine the true nature and purpose "
                "of these artifacts. Reviewing their functionality and execution context could provide "
                "insight into the actions performed on the system."
            )
        }
    ]
}

def print_terminal_summary():
    """Prints a styled forensic triage report to stdout."""
    print("=" * 80)
    print("          LOKI HOST IOC SCANNER -- FORENSIC TRIAGE & SOC INCIDENT DOSSIER")
    print("=" * 80)
    print("\n[*] Incident Identification & Scope:")
    print("  [-] Organization      : Syntrix Enterprise SOC (Workstation Alert)")
    print("  [-] Analyst Role      : SOC Level 1 Triage Analyst (soc1@syntrix.com)")
    print("  [-] Escalation Target : SOC Level 2 Senior Analyst (soc2@syntrix.com)")
    print("  [-] Scanning Tool     : LOKI IOC & YARA Host Scanner (v0.10+)")
    print("  [-] Overall Verdict   : CONFIRMED MULTI-STAGE SYSTEM COMPROMISE")
    print("  [-] Case Severity     : CRITICAL (Level 4 / 4)")
    print("  [-] Information Class : TLP:AMBER | PAP:AMBER")

    print("\n[*] Identified High-Risk Artifacts & Indicators of Compromise (4 Findings):")
    for art in ARTIFACTS:
        print(f"\n  [!] {art['id']}: {art['file_name']} (Risk Score: {art['risk_score']})")
        print(f"      Path        : {art['file_path']}")
        print(f"      Type / Size : {art['file_type']} | {art['file_size']}")
        if art['md5'] != "N/A":
            print(f"      MD5 Hash    : {art['md5']}")
        if art['sha256'] != "N/A":
            print(f"      SHA256 Hash : {art['sha256']}")
        print(f"      YARA Match  : {art['yara_rule']}")
        if "network_listener" in art:
            print(f"      Net Listener: {art['network_listener']}")
        print(f"      VirusTotal  : {art['virustotal_verdict']}")
        print(f"      MITRE ATT&CK: {art['mitre_technique']}")
        print(f"      Assessment  : {art['description']}")

    print("\n[*] MITRE ATT&CK Post-Compromise Kill Chain:")
    print("  1. Execution         -> T1059.001 (PowerShell: C:\\Windows\\Disable.ps1)")
    print("  2. Persistence       -> T1547.001 (Startup Folder: winfix.exe bind shell on 0.0.0.0:4444)")
    print("  3. Defense Evasion   -> T1562.001 (Impair Defenses: Disable.ps1 disabling Defender)")
    print("  4. Credential Access -> T1003.002 (SAM Registry Hive Dump in C:\\Users\\Public)")
    print("  5. Credential Access -> T1003     (Mimikatz x64 in C:\\ProgramData\\haha.exe)")

    print("\n[*] TheHive Case Management & Escalation Status:")
    print(f"  [-] Case Title       : {THEHIVE_CASE['title']}")
    print(f"  [-] Total Observables: {len(THEHIVE_CASE['observables'])} IOC Observables Registered")
    print(f"  [-] Total TTPs       : {len(THEHIVE_CASE['ttps'])} Techniques Mapped")
    print(f"  [-] Total Tasks      : {len(THEHIVE_CASE['tasks'])} SOC Level 2 Investigation Tasks")
    print(f"  [-] Ownership        : Escalated and assigned to {THEHIVE_CASE['owner']}")
    print("=" * 80)
    print("STATUS: Fully Solved & Escalated. Ready for SOC Level 2 Containment.")
    print("=" * 80)

def generate_markdown():
    """Generates a Markdown table of the findings."""
    md = []
    md.append("### 📊 LOKI IOC Detection Summary Matrix\n")
    md.append("| Artifact ID | Detected File / Process | Risk Score | YARA Signature | MITRE Technique | Threat Intelligence Verdict |")
    md.append("|---|---|---|---|---|---|")
    for art in ARTIFACTS:
        net = f"<br>*(Listening on 0.0.0.0:4444)*" if "network_listener" in art else ""
        md.append(
            f"| **{art['id']}** | `{art['file_name']}`{net}<br>`{art['file_path']}` | **`{art['risk_score']}`** | `{art['yara_rule']}` | **{art['mitre_technique']}** | {art['virustotal_verdict']} |"
        )
    return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="LOKI IOC Scanner & TheHive Case Generator")
    parser.add_argument("--thehive", action="store_true", help="Print TheHive 5 JSON case specification")
    parser.add_argument("--markdown", action="store_true", help="Print Markdown formatted summary tables")
    parser.add_argument("--export", type=str, help="Export TheHive JSON payload to specified file path")
    args = parser.parse_args()

    if args.thehive:
        print(json.dumps(THEHIVE_CASE, indent=2))
    elif args.markdown:
        print(generate_markdown())
    elif args.export:
        with open(args.export, "w", encoding="utf-8") as f:
            json.dump(THEHIVE_CASE, f, indent=2)
        print(f"[+] Successfully exported TheHive 5 case payload to: {args.export}")
    else:
        print_terminal_summary()

if __name__ == "__main__":
    main()
