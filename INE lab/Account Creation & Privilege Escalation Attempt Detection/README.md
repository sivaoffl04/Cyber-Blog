# ⚔️ Account Creation & Privilege Escalation Attempt Detection — Lab Documentation

![Banner](./images/account_privesc_banner.jpg)

This directory contains the complete SOC Level 1 triage, analysis, and case documentation walkthrough for the **Account Creation & Privilege Escalation Attempt Detection** hands-on lab from INE Security.

---

## 📂 Directory Contents

* **[Account_Creation_Privilege_Escalation_Attempt_Detection_Walkthrough.md](./Account_Creation_Privilege_Escalation_Attempt_Detection_Walkthrough.md)**: Master in-depth walkthrough covering the complete incident investigation across Wazuh SIEM v4.x, MITRE ATT&CK framework, and TheHive incident management platform.
* **[images/](./images/)**: Custom visual assets including the hero banner, attack kill chain architecture infographic, and live animated demonstration GIF.
* **[image/](./image/)**: Full chronological archive of all 35 official lab screenshots (`image0.jpg` through `image34.jpg`).
* **[Account Creation and Privilege Escalation Attempt Detection solution.mp4](./Account%20Creation%20and%20Privilege%20Escalation%20Attempt%20Detection%20solution.mp4)**: Complete high-resolution walkthrough video demonstration.

---

## ⚡ Quick Incident Triage Summary

| Attribute | Details |
|---|---|
| **Platform / Course** | INE Security — SOC Ticketing & Reporting |
| **Role** | SOC Level 1 Incident Analyst (Syntrix) |
| **Incident Date** | 24th December 2025 |
| **Target Host** | `ip-10-0-0-100` (`Agent ID: 002`) |
| **Source Ingress IP** | `10.0.0.11` |
| **Malicious User** | `eviluser` |
| **Target Configuration** | `/etc/sudoers` |
| **Classification** | 🔴 **True Positive (Active Compromise)** |
| **Severity** | **`HIGH`** |
| **TLP / PAP** | `TLP:AMBER` / `PAP:AMBER` |
| **Case Title** | `Suspicious Account Creation Followed by Privileged Access Attempt` |
| **Case Assignee** | `SOC 2` (`soc2@syntrix.com`) |

---

👉 **Read the full walkthrough**: [Account Creation & Privilege Escalation Attempt Detection Walkthrough](./Account_Creation_Privilege_Escalation_Attempt_Detection_Walkthrough.md)
