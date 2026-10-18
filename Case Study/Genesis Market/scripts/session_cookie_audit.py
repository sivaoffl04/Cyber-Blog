#!/usr/bin/env python3
"""
Session Cookie & Browser Profile Security Audit Tool
Case Study: Genesis Market (Operation Cookie Monster) - Defensive Tooling
Author: Syntrix Cyber Defense Operations / Threat Hunting Team

Description:
    Forensic auditing tool for SOC analysts and incident responders to detect
    browser credential/cookie exposure, identify infostealer staging artifacts,
    audit session cookie security postures, and correlate findings to MITRE ATT&CK.
"""

import os
import sys
import json
import argparse
import hashlib
from datetime import datetime
from pathlib import Path

# ANSI Color Codes for Terminal Output
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

BANNER = f"""{CYAN}{BOLD}
╔══════════════════════════════════════════════════════════════════════════════╗
║             BROWSER SESSION & CREDENTIAL FORENSIC AUDITING TOOL              ║
║         Genesis Market TTP Detection: Cookie Stores & Infostealer Triage     ║
╚══════════════════════════════════════════════════════════════════════════════╝{RESET}
"""

# Common browser artifact locations on Windows / Linux
BROWSER_PATHS_WINDOWS = {
    "Google Chrome": {
        "cookies": r"AppData\Local\Google\Chrome\User Data\Default\Network\Cookies",
        "login_data": r"AppData\Local\Google\Chrome\User Data\Default\Login Data",
        "web_data": r"AppData\Local\Google\Chrome\User Data\Default\Web Data",
        "local_state": r"AppData\Local\Google\Chrome\User Data\Local State",
    },
    "Microsoft Edge": {
        "cookies": r"AppData\Local\Microsoft\Edge\User Data\Default\Network\Cookies",
        "login_data": r"AppData\Local\Microsoft\Edge\User Data\Default\Login Data",
        "web_data": r"AppData\Local\Microsoft\Edge\User Data\Default\Web Data",
        "local_state": r"AppData\Local\Microsoft\Edge\User Data\Local State",
    },
    "Brave": {
        "cookies": r"AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Network\Cookies",
        "login_data": r"AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data",
        "web_data": r"AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Web Data",
        "local_state": r"AppData\Local\BraveSoftware\Brave-Browser\User Data\Local State",
    },
    "Mozilla Firefox": {
        "profiles": r"AppData\Roaming\Mozilla\Firefox\Profiles",
    }
}

INFOSTEALER_INDICATOR_FILES = [
    "cookies.txt", "passwords.txt", "autofill.txt", "cards.txt",
    "system_info.txt", "user_info.txt", "installed_software.txt",
    "desktop_screenshot.png", "screen.jpg", "screenshot.png",
    "wallet.dat", "wallets.txt", "discord_tokens.txt", "telegram_session"
]

SUSPICIOUS_STAGING_DIRS = [
    r"AppData\Local\Temp",
    r"AppData\Roaming",
    r"AppData\Local",
    r"C:\ProgramData",
    r"C:\Users\Public"
]

def get_file_metadata(filepath):
    """Retrieve file size, last modified time, and SHA-256 hash."""
    p = Path(filepath)
    if not p.exists() or not p.is_file():
        return None
    try:
        stat = p.stat()
        hasher = hashlib.sha256()
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hasher.update(chunk)
        return {
            "path": str(p.resolve()),
            "size_bytes": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "sha256": hasher.hexdigest()
        }
    except Exception as e:
        return {"path": str(p), "error": str(e)}

def audit_browser_datastores(base_user_dir=None):
    """Audit installed browser stores to determine exposure to infostealers."""
    user_home = Path(base_user_dir) if base_user_dir else Path.home()
    findings = []

    for browser_name, artifacts in BROWSER_PATHS_WINDOWS.items():
        browser_report = {
            "browser": browser_name,
            "installed": False,
            "artifacts_found": [],
            "risk_assessment": "Safe / Not Found"
        }

        if browser_name == "Mozilla Firefox":
            ff_prof_dir = user_home / artifacts["profiles"]
            if ff_prof_dir.exists() and ff_prof_dir.is_dir():
                browser_report["installed"] = True
                for prof in ff_prof_dir.iterdir():
                    if prof.is_dir():
                        cookie_db = prof / "cookies.sqlite"
                        key_db = prof / "key4.db"
                        logins_json = prof / "logins.json"
                        for target in [cookie_db, key_db, logins_json]:
                            if target.exists():
                                meta = get_file_metadata(target)
                                if meta:
                                    browser_report["artifacts_found"].append(meta)
        else:
            for art_name, rel_path in artifacts.items():
                target_path = user_home / rel_path
                if target_path.exists():
                    browser_report["installed"] = True
                    meta = get_file_metadata(target_path)
                    if meta:
                        meta["artifact_type"] = art_name
                        browser_report["artifacts_found"].append(meta)

        if browser_report["installed"]:
            if len(browser_report["artifacts_found"]) > 0:
                browser_report["risk_assessment"] = (
                    "High Exposure: Active cookie & credential stores present on disk. "
                    "Vulnerable to DPAPI-based infostealer extraction (RedLine, Vidar, Raccoon)."
                )
            findings.append(browser_report)

    return findings

def scan_infostealer_staging_artifacts(base_user_dir=None):
    """Scan common infostealer staging paths for dumped text files and archive bundles."""
    user_home = Path(base_user_dir) if base_user_dir else Path.home()
    suspicious_findings = []

    for rel_dir in SUSPICIOUS_STAGING_DIRS:
        target_dir = Path(rel_dir) if rel_dir.startswith("C:") else user_home / rel_dir
        if not target_dir.exists() or not target_dir.is_dir():
            continue

        try:
            # Check shallow top-level items in staging directories
            for entry in target_dir.iterdir():
                # Check for known filenames
                if entry.name.lower() in [f.lower() for f in INFOSTEALER_INDICATOR_FILES]:
                    meta = get_file_metadata(entry)
                    if meta:
                        meta["detection_reason"] = f"Known infostealer artifact signature: {entry.name}"
                        suspicious_findings.append(meta)

                # Check for suspicious zip bundles recently created
                if entry.suffix.lower() in [".zip", ".rar", ".7z"]:
                    if any(kw in entry.name.lower() for kw in ["log", "stealer", "bot", "grab", "pass", "cookie"]):
                        meta = get_file_metadata(entry)
                        if meta:
                            meta["detection_reason"] = f"Suspicious exfiltration archive candidate: {entry.name}"
                            suspicious_findings.append(meta)
        except PermissionError:
            continue
        except Exception:
            continue

    return suspicious_findings

def map_mitre_ttps(browser_findings, staging_findings):
    """Map detected conditions to MITRE ATT&CK techniques."""
    ttps = [
        {
            "technique_id": "T1539",
            "technique_name": "Steal Web Session Cookie",
            "tactic": "Credential Access",
            "status": "Monitored / At Risk" if browser_findings else "Unobserved",
            "description": "Adversaries extract authentication cookies from browser disk stores to hijack active sessions."
        },
        {
            "technique_id": "T1555.003",
            "technique_name": "Credentials from Web Browsers",
            "tactic": "Credential Access",
            "status": "Monitored / At Risk" if browser_findings else "Unobserved",
            "description": "Infostealers decrypt Windows DPAPI-protected Login Data vaults to recover stored passwords."
        },
        {
            "technique_id": "T1005",
            "technique_name": "Data from Local System",
            "tactic": "Collection",
            "status": "Elevated Alert" if staging_findings else "Normal",
            "description": "Staging harvested credentials, autofill, and browser profiles into local temp directories."
        },
        {
            "technique_id": "T1078.004",
            "technique_name": "Valid Accounts: Cloud Accounts",
            "tactic": "Defense Evasion / Initial Access",
            "status": "Downstream Risk",
            "description": "Compromised session cookies replay authentication state into cloud SSO, bypassing MFA."
        }
    ]
    return ttps

def run_audit(target_dir=None):
    """Execute complete browser and infostealer audit."""
    print(BANNER)
    print(f"{BOLD}[+] Commencing Host Browser Profile & Session Cookie Security Audit...{RESET}")
    start_time = datetime.utcnow().isoformat() + "Z"

    browser_findings = audit_browser_datastores(target_dir)
    staging_findings = scan_infostealer_staging_artifacts(target_dir)
    ttps = map_mitre_ttps(browser_findings, staging_findings)

    # Print Browser Audit Summary
    print(f"\n{BOLD}[+] BROWSER DATASTORE INVENTORY & RISK AUDIT{RESET}")
    for b in browser_findings:
        print(f"  {CYAN}● {b['browser']}{RESET}")
        print(f"    Status: {GREEN}Installed{RESET} | Artifacts Located: {len(b['artifacts_found'])}")
        print(f"    Assessment: {YELLOW}{b['risk_assessment']}{RESET}")
        for art in b['artifacts_found']:
            art_type = art.get('artifact_type', Path(art['path']).name)
            print(f"      - {DIM}{art_type:12}{RESET}: {art['path']} ({art['size_bytes']} bytes)")

    # Print Infostealer Staging Artifacts
    print(f"\n{BOLD}[+] SUSPICIOUS INFOSTEALER STAGING & EXFILTRATION ARTIFACTS{RESET}")
    if staging_findings:
        print(f"  {RED}[!] WARNING: {len(staging_findings)} suspicious artifact(s) identified in local directories:{RESET}")
        for s in staging_findings:
            print(f"    {RED}✖{RESET} {s['path']}")
            print(f"      Reason: {s['detection_reason']}")
            print(f"      SHA256: {s['sha256']}")
    else:
        print(f"  {GREEN}[✓] Clean: No unencrypted infostealer staging files (cookies.txt, passwords.txt) found.{RESET}")

    # Print MITRE ATT&CK Matrix Correlation
    print(f"\n{BOLD}[+] MITRE ATT&CK ENTERPRISE MAPPING{RESET}")
    print(f"  {'TECHNIQUE ID':<14} | {'TACTIC':<20} | {'TECHNIQUE NAME'}")
    print(f"  {'-'*14}-+-{'-'*20}-+-{'-'*35}")
    for t in ttps:
        color = RED if "Elevated" in t['status'] else (YELLOW if "At Risk" in t['status'] else CYAN)
        print(f"  {color}{t['technique_id']:<14}{RESET} | {t['tactic']:<20} | {BOLD}{t['technique_name']}{RESET}")
        print(f"  {DIM}  ↳ Status: {t['status']} - {t['description']}{RESET}")

    # Actionable Recommendations
    print(f"\n{BOLD}[+] STRATEGIC BLUE TEAM & SOC RECOMMENDATIONS{RESET}")
    print("  1. Enforce Phishing-Resistant MFA (FIDO2 / WebAuthn / Passkeys) to neutralize session replay.")
    print("  2. Implement Conditional Access with Device Health Attestation (Intune / CrowdStrike Falcon ZTA).")
    print("  3. Block browser credential saving via GPO / InTune administrative templates.")
    print("  4. Enable continuous token evaluation (CAE) to revoke active OAuth/SAML tokens upon credential change.")
    print("  5. Monitor EDR telemetry for non-browser processes accessing '%LOCALAPPDATA%\\Google\\Chrome\\User Data'.")
    print(f"\n{GREEN}[✓] Forensic audit complete.{RESET}\n")

    return {
        "timestamp": start_time,
        "browser_audit": browser_findings,
        "staging_scan": staging_findings,
        "mitre_ttps": ttps
    }

def main():
    parser = argparse.ArgumentParser(description="Audit browser session cookie stores and infostealer staging indicators.")
    parser.add_argument("--user-dir", help="Audit specific user home directory (default: current user)")
    parser.add_argument("--json", dest="json_out", action="store_true", help="Output audit findings in JSON format")
    parser.add_argument("--export", dest="export_path", help="Export audit report to target JSON file path")
    args = parser.parse_args()

    report = run_audit(args.user_dir)

    if args.json_out:
        print(json.dumps(report, indent=2))

    if args.export_path:
        with open(args.export_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"{GREEN}[+] Report exported to: {args.export_path}{RESET}")

if __name__ == "__main__":
    main()
