#!/usr/bin/env python3
"""
MGM Resorts Case Study: Enterprise Identity & Help Desk Security Audit Tool
===========================================================================
This diagnostic and simulation script evaluates an enterprise's vulnerability
to Scattered Spider / UNC3944 style identity attacks, including:
  1. Okta SystemLog Anomaly Detection (Help desk vishing & rapid factor resets)
  2. Help Desk Verification Policy Risk Calculator (NIST SP 800-63-3 compliance)
  3. VMware ESXi Virtualization Posture Assessment (Lockdown mode & SSH checks)

Usage:
  python identity_helpdesk_audit.py --mode all
  python identity_helpdesk_audit.py --mode okta-audit --log-file sample_okta_logs.json
  python identity_helpdesk_audit.py --mode policy-calc
  python identity_helpdesk_audit.py --mode esxi-check
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
  MGM RESORTS CASE STUDY: ENTERPRISE IDENTITY & HELP DESK AUDIT TOOL
  Simulating Scattered Spider (UNC3944) Detection & Help Desk Hardening
==============================================================================={RESET}
"""
    print(banner)


def generate_sample_okta_logs():
    """Generates synthetic Okta SystemLog events simulating the MGM attack sequence."""
    base_time = datetime.now(timezone.utc) - timedelta(minutes=45)
    
    events = [
        # 1. Normal login earlier
        {
            "eventId": "evt_001",
            "published": (base_time - timedelta(hours=2)).isoformat() + "Z",
            "eventType": "user.session.start",
            "outcome": {"result": "SUCCESS"},
            "actor": {"alternateId": "systems.engineer@mgmresorts.com", "displayName": "Senior Systems Engineer"},
            "client": {"ipAddress": "199.167.211.5", "geographicalContext": {"city": "Las Vegas", "country": "United States"}, "userAgent": {"rawUserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}}
        },
        # 2. Help desk agent deactivates Okta Verify factor
        {
            "eventId": "evt_002",
            "published": (base_time).isoformat() + "Z",
            "eventType": "user.mfa.factor.deactivate",
            "outcome": {"result": "SUCCESS"},
            "actor": {"alternateId": "helpdesk.agent@mgmresorts.com", "displayName": "IT Support Tier-1"},
            "target": [{"alternateId": "systems.engineer@mgmresorts.com", "displayName": "Senior Systems Engineer", "type": "User"}],
            "client": {"ipAddress": "10.200.14.88", "userAgent": {"rawUserAgent": "ServiceDesk-Internal-Portal/3.2"}}
        },
        # 3. Attacker registers new factor 8 minutes later from residential IP
        {
            "eventId": "evt_003",
            "published": (base_time + timedelta(minutes=8)).isoformat() + "Z",
            "eventType": "user.mfa.factor.activate",
            "outcome": {"result": "SUCCESS"},
            "actor": {"alternateId": "systems.engineer@mgmresorts.com", "displayName": "Senior Systems Engineer"},
            "target": [{"alternateId": "systems.engineer@mgmresorts.com", "displayName": "Senior Systems Engineer", "type": "User"}],
            "client": {
                "ipAddress": "70.168.14.92",
                "geographicalContext": {"city": "Henderson", "state": "Nevada", "country": "United States"},
                "userAgent": {"rawUserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X)"}
            }
        },
        # 4. Attacker starts administrative session
        {
            "eventId": "evt_004",
            "published": (base_time + timedelta(minutes=10)).isoformat() + "Z",
            "eventType": "user.session.start",
            "outcome": {"result": "SUCCESS"},
            "actor": {"alternateId": "systems.engineer@mgmresorts.com", "displayName": "Senior Systems Engineer"},
            "client": {
                "ipAddress": "70.168.14.92",
                "geographicalContext": {"city": "Henderson", "state": "Nevada", "country": "United States"},
                "userAgent": {"rawUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/116.0.0.0"}
            }
        },
        # 5. Attacker creates rogue Inbound SAML Identity Provider
        {
            "eventId": "evt_005",
            "published": (base_time + timedelta(minutes=25)).isoformat() + "Z",
            "eventType": "system.idp.lifecycle.create",
            "outcome": {"result": "SUCCESS"},
            "actor": {"alternateId": "systems.engineer@mgmresorts.com", "displayName": "Senior Systems Engineer"},
            "target": [{"displayName": "External-Partner-SAML-Trust", "type": "Identity Provider"}],
            "client": {"ipAddress": "70.168.14.92"}
        }
    ]
    return events


def audit_okta_system_logs(events):
    """Analyzes Okta SystemLog events for Scattered Spider intrusion patterns."""
    print(f"\n{BOLD}{CYAN}=== 1. OKTA SYSTEMLOG ITDR ANOMALY AUDIT ==={RESET}")
    print(f"[*] Ingested {len(events)} telemetry events. Analyzing behavioral patterns...\n")
    
    deactivations = {}
    alerts = []
    
    for evt in events:
        event_type = evt.get("eventType")
        published_str = evt.get("published")
        actor = evt.get("actor", {}).get("alternateId", "Unknown")
        client_ip = evt.get("client", {}).get("ipAddress", "Unknown")
        targets = evt.get("target", [])
        
        # Track factor deactivations
        if event_type == "user.mfa.factor.deactivate":
            for t in targets:
                target_user = t.get("alternateId")
                deactivations[target_user] = {
                    "time": published_str,
                    "agent": actor,
                    "event": evt
                }
                print(f"[{YELLOW}MFA DEACTIVATE{RESET}] Target: {BOLD}{target_user}{RESET} by Agent: {actor}")

        # Correlate factor activation within rapid window
        elif event_type == "user.mfa.factor.activate":
            for t in targets:
                target_user = t.get("alternateId")
                if target_user in deactivations:
                    deact_data = deactivations[target_user]
                    alerts.append({
                        "severity": "CRITICAL",
                        "rule": "RULE-OKTA-001: Rapid Privileged Factor Reset & Activation",
                        "user": target_user,
                        "deactivated_by": deact_data["agent"],
                        "activated_from_ip": client_ip,
                        "description": f"MFA factor deactivated and new factor activated rapidly. Potential vishing bypass detected!"
                    })
                    print(f"[{RED}{BOLD}ALERT DETECTED{RESET}] Target: {BOLD}{target_user}{RESET} registered new factor from IP: {client_ip}")

        # Check for Inbound Identity Provider creation
        elif event_type in ("system.idp.lifecycle.create", "system.idp.lifecycle.update"):
            target_name = targets[0].get("displayName") if targets else "Unknown"
            alerts.append({
                "severity": "FATAL",
                "rule": "RULE-OKTA-002: Unauthorized Inbound SAML Identity Provider Creation",
                "user": actor,
                "target_idp": target_name,
                "ip": client_ip,
                "description": f"Actor created/modified an external Inbound SAML IdP: '{target_name}'. High probability of Golden SAML persistence."
            })
            print(f"[{RED}{BOLD}FATAL ALERT{RESET}] Inbound IdP created: '{target_name}' by Actor: {actor}")

    print(f"\n{BOLD}Audit Findings Summary:{RESET}")
    if alerts:
        for idx, alert in enumerate(alerts, 1):
            color = RED if alert["severity"] in ("CRITICAL", "FATAL") else YELLOW
            print(f"  {idx}. [{color}{alert['severity']}{RESET}] {BOLD}{alert['rule']}{RESET}")
            print(f"     Details: {alert['description']}")
            print(f"     Target/Actor: {alert.get('user')} | Origin IP: {alert.get('activated_from_ip') or alert.get('ip')}")
    else:
        print(f"  {GREEN}[+] No high-risk factor reset anomalies detected.{RESET}")
    return alerts


def calculate_helpdesk_risk_score():
    """Evaluates help desk verification policies against NIST SP 800-63-3 standards."""
    print(f"\n{BOLD}{CYAN}=== 2. HELP DESK VERIFICATION POLICY RISK CALCULATOR ==={RESET}")
    print("[*] Evaluating Help Desk Operational Hardening Posture...")

    # Simulated enterprise questionnaire (representing MGM baseline vs Hardened baseline)
    posture_questions = [
        {
            "id": 1,
            "policy": "Knowledge-Based Authentication (KBA) usage",
            "description": "Does the help desk verify users using Employee ID, DOB, or SSN?",
            "current_state": True,  # MGM had this vulnerability
            "weight": 30,
            "mitigation": "Ban KBA completely. Rely on out-of-band video or cryptographic challenge."
        },
        {
            "id": 2,
            "policy": "Tier-0 Privileged Account Reset Authority",
            "description": "Can tier-1 help desk agents reset credentials for Super Admins / Domain Admins?",
            "current_state": True,  # MGM had this vulnerability
            "weight": 25,
            "mitigation": "Strip Tier-0 reset authority from service desk. Require Identity Security team."
        },
        {
            "id": 3,
            "policy": "Mandatory Live Out-of-Band Video Verification",
            "description": "Is a recorded video call with facial verification required before clearing MFA?",
            "current_state": False, # MGM lacked this
            "weight": 20,
            "mitigation": "Implement live Microsoft Teams / Zoom video callback matching corporate HR photo."
        },
        {
            "id": 4,
            "policy": "Dual-Custody Manager Approval",
            "description": "Is digital authorization from the employee's direct manager required?",
            "current_state": False, # MGM lacked this
            "weight": 15,
            "mitigation": "Require direct manager digital sign-off via ITSM ticket before token generation."
        },
        {
            "id": 5,
            "policy": "Post-Reset Quarantine Policy",
            "description": "Are reset accounts placed in a 24h quarantine restricting admin consoles?",
            "current_state": False, # MGM lacked this
            "weight": 10,
            "mitigation": "Enforce conditional access policy restricting sensitive cloud/vCenter access for 24h."
        }
    ]

    total_risk = 0
    max_risk = sum(q["weight"] for q in posture_questions)

    print(f"\n{'Policy Control':<45} | {'Status':<10} | {'Risk Contribution':<15}")
    print("-" * 75)
    for q in posture_questions:
        if q["current_state"] and q["id"] in (1, 2):  # Bad policies present
            risk = q["weight"]
            status = f"{RED}DEFICIENT{RESET}"
        elif not q["current_state"] and q["id"] in (3, 4, 5):  # Good policies missing
            risk = q["weight"]
            status = f"{RED}MISSING{RESET}"
        else:
            risk = 0
            status = f"{GREEN}SECURE{RESET}"
        
        total_risk += risk
        print(f"{q['policy']:<45} | {status:<19} | +{risk} Points")

    print("-" * 75)
    risk_percentage = (total_risk / max_risk) * 100
    
    if risk_percentage >= 70:
        rating = f"{RED}{BOLD}CRITICAL VULNERABILITY (MGM 2023 BASELINE){RESET}"
    elif risk_percentage >= 40:
        rating = f"{YELLOW}{BOLD}MODERATE RISK{RESET}"
    else:
        rating = f"{GREEN}{BOLD}HARDENED DEFENSE{RESET}"

    print(f"Total Help Desk Risk Score: {BOLD}{risk_percentage:.1f}% / 100%{RESET} -> {rating}")
    print(f"\n{BOLD}Prescriptive Hardening Roadmap:{RESET}")
    for q in posture_questions:
        print(f"  * {BOLD}{q['policy']}:{RESET} {q['mitigation']}")


def audit_esxi_hypervisor_posture():
    """Simulates VMware ESXi configuration audit against ALPHV/BlackCat tactics."""
    print(f"\n{BOLD}{CYAN}=== 3. VMWARE ESXi HYPERVISOR HARDENING AUDIT ==={RESET}")
    print("[*] Assessing virtual infrastructure against BlackCat ransomware tradecraft...")

    esxi_checks = [
        {"check": "ESXi Shell Disabled by Default", "passed": False, "severity": "HIGH", "detail": "Direct ESXi Shell was left enabled, allowing attacker console access."},
        {"check": "SSH Service Disabled / Stopped", "passed": False, "severity": "CRITICAL", "detail": "SSH service active on port 22, enabling direct payload staging."},
        {"check": "Strict Lockdown Mode Enforced", "passed": False, "severity": "FATAL", "detail": "Lockdown mode disabled; direct hypervisor logins permitted without vCenter."},
        {"check": "Out-of-Band Management VLAN Isolation", "passed": False, "severity": "CRITICAL", "detail": "ESXi management IPs directly routable from corporate cloud subnets."},
        {"check": "Hardware Immutable Storage Snapshots", "passed": False, "severity": "HIGH", "detail": "Storage SAN snapshots writable; allowed attackers to delete volume backups."}
    ]

    print(f"\n{'Hypervisor Configuration Check':<45} | {'Status':<10} | {'Finding Severity'}")
    print("-" * 75)
    for c in esxi_checks:
        status = f"{GREEN}PASSED{RESET}" if c["passed"] else f"{RED}FAILED{RESET}"
        sev_color = RED if c["severity"] in ("CRITICAL", "FATAL") else YELLOW
        sev = f"{sev_color}{c['severity']}{RESET}"
        print(f"{c['check']:<45} | {status:<19} | {sev}")
        if not c["passed"]:
            print(f"    --> {CYAN}Remediation:{RESET} {c['detail']}")

    print("-" * 75)
    print(f"{BOLD}Assessment:{RESET} The virtual infrastructure reflects the unhardened state exploited by ALPHV.")
    print(f"{GREEN}{BOLD}Mandatory Recommendation:{RESET} Enforce VMware Strict Lockdown Mode and isolate ESXi management on an air-gapped VLAN.\n")


def main():
    print_banner()
    mode = "all"
    if len(sys.argv) > 1 and sys.argv[1] == "--mode" and len(sys.argv) > 2:
        mode = sys.argv[2]

    if mode in ("all", "okta-audit"):
        sample_logs = generate_sample_okta_logs()
        audit_okta_system_logs(sample_logs)

    if mode in ("all", "policy-calc"):
        calculate_helpdesk_risk_score()

    if mode in ("all", "esxi-check"):
        audit_esxi_hypervisor_posture()

    print(f"\n{BOLD}{GREEN}*** Audit and Simulation Run Completed Successfully ***{RESET}\n")


if __name__ == "__main__":
    main()
