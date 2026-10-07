# 🛡️ Detecting Abnormal Network Connections With Wazuh — Lab Documentation

![Wazuh Abnormal Network Connections Banner](./images/wazuh_abnormal_network_banner.jpg)

This directory contains the complete hands-on detection engineering, telemetry collection, and adversary simulation walkthrough for the **Detecting Abnormal Network Connections With Wazuh** lab from **INE Security**.

---

## 📂 Directory Contents

* **[Detecting_Abnormal_Network_Connections_With_Wazuh_Walkthrough.md](./Detecting_Abnormal_Network_Connections_With_Wazuh_Walkthrough.md)**: Master in-depth walkthrough covering all 5 tasks and 16 steps, architectural breakdowns, CDB list performance mechanics, live terminal screenshots, Sigma rules, and SOC triage playbooks.
* **[images/](./images/)**: Custom visual assets including the hero banner, detection pipeline architecture infographic, CDB list evaluation flowchart, and live animated terminal demonstration GIF.
* **[image/](./image/)**: Full chronological archive of all 16 step-by-step terminal execution cards (`1.png` through `16.png`).

---

## ⚡ Quick Incident Triage Summary

| Attribute | Details |
| :--- | :--- |
| **Lab Platform** | [INE Security (Defender Labs)](https://my.ine.com/labs/89688258-d373-40a5-a885-9ef8dd7b60a9) |
| **SOC Manager Host** | Ubuntu 20.04 (`10.0.18.204`) — Wazuh Server v4.3.10 & Web Dashboard |
| **Monitored Endpoint** | Windows Server 2019 (`10.0.23.132`) — Wazuh Agent & Microsoft Sysmon v14.x |
| **Attacker Machine** | Kali Linux (`10.10.21.2`) — Metasploit, Netcat, Python SimpleHTTP |
| **Core Telemetry** | Sysmon Event ID 3 (Network Connection) via `Microsoft-Windows-Sysmon/Operational` |
| **Detection Technique** | Constant Database (CDB) list lookup (`not_match_key`) in Wazuh Ruleset |
| **Custom Rule ID** | `115001` (Severity Level 10 - High) |
| **Attacks Simulated** | 1. Metasploit SMB PsExec (`4444/TCP`)<br>2. In-Memory PowerShell Reverse Shell (`1234/TCP`) |
| **Verification Status** | 🟢 **100% Solved — Both Abnormal Connections Caught in Real Time** |

---

## 🎯 Key Tasks Completed

1. **Wazuh Agent Deployment:** Deployed `wazuh-agent-4.3.10-1.msi` silently on Windows Server 2019, bound to manager `10.0.18.204`, and verified active status in the web console.
2. **Sysmon Integration:** Installed Microsoft Sysmon64 with `sysmonconfig.xml` and configured `ossec.conf` with `<localfile>` eventchannel parsing.
3. **CDB Port Whitelist:** Authored `/var/ossec/etc/lists/common-ports` containing standard enterprise ports (`21`, `22`, `80`, `443`, `445`, etc.) with `660` permissions.
4. **Custom Detection Rule 115001:** Crafted a Level 10 rule matching parent `sid: 61605` and performing `lookup="not_match_key"` against the compiled CDB list.
5. **Adversary Simulation & SIEM Validation:** Simulated Pass-the-Hash with Metasploit (`exploit/windows/smb/psexec`) and executed a custom PowerShell reverse shell to port `1234`, successfully verifying immediate Level 10 alerts in the Wazuh Dashboard.

---

👉 **Read the complete guide**: [Detecting Abnormal Network Connections With Wazuh Walkthrough](./Detecting_Abnormal_Network_Connections_With_Wazuh_Walkthrough.md)
