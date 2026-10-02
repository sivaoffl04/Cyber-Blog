# 🎯 INE Security & AttackDefense Hands-on Labs Walkthroughs

Welcome to the **Hands-on Lab Walkthroughs & Cyber Threat Hunting Portfolio**. This directory contains in-depth, production-grade solutions, forensic dissections, and detection engineering playbooks for cybersecurity challenges from **[INE Security](https://my.ine.com/)** and **[AttackDefense](https://attackdefense.com/)**.

Each walkthrough includes real-world MITRE ATT&CK technique mappings, raw telemetry analysis, animated live demonstration GIFs, architecture infographics, step-by-step query guides, and custom Sigma detection rules.

---

## 🏆 Lab Solutions Directory

| Lab Title | Challenge ID | Category | Primary Telemetry | MITRE ATT&CK Techniques | Status | Direct Walkthrough |
| :--- | :---: | :--- | :--- | :--- | :---: | :---: |
| **Kibana : Windows Event Logs I** | **CID 1182** | Threat Hunting / LOLBAS | Sysmon EID 1 (Process Creation) | **T1053.005** (Schtasks)<br>**T1070.004** (SDelete)<br>**T1021.002** (SMB Shares)<br>**T1018** (Remote Discovery)<br>**T1197** (BITS Jobs) | 🟢 **100% Solved**<br>(5/5 Flags) | [View Solution](./Kibana%20Windows%20Event%20Logs%20I/README.md) |
| **Kibana : Windows Event Logs II** | **CID 1185** | Active Directory Recon | Sysmon EID 3 (Network Connections) | **T1087.002** (Domain Account Discovery)<br>**T1018** (Remote System Discovery)<br>**T1069.002** (Permission Groups) | 🟢 **100% Solved**<br>(3/3 Flags) | [View Solution](./Kibana%20Windows%20Event%20Logs%20II/README.md) |
| **Kibana : Windows Event Logs III** | **CID 1186** | Web Shell & Memory Decryption | Sysmon EID 1 (Process Creation) | **T1505.003** (Web Shell)<br>**T1027** (Obfuscation)<br>**T1059.001** (PowerShell)<br>**T1003** / **T1082** (LOLBAS `appcmd.exe`) | 🟢 **100% Solved**<br>(3/3 Flags) | [View Solution](./Kibana%20Windows%20Event%20Logs%20III/README.md) |

---

## 🔬 Lab Overviews & Investigation Focus

### 1. [Kibana : Windows Event Logs I](./Kibana%20Windows%20Event%20Logs%20I/README.md)
* **Dataset:** [`PanacheSysmon_vs_AtomicRedTeam01.evtx`](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/AutomatedTestingTools/PanacheSysmon_vs_AtomicRedTeam01.evtx)
* **Scenario:** Red Canary Atomic Red Team test execution emulating adversary actions on Windows endpoints.
* **Key Tasks:** Identifying plaintext passwords in scheduled tasks (`schtasks /RP`), tracking secure file deletion via Sysinternals `sdelete`, detecting remote SMB administrative mounts (`net use`), analyzing CIDR subnets from CMD ping sweep loops, and locating files transferred via Background Intelligent Transfer Service (`bitsadmin`).

### 2. [Kibana : Windows Event Logs II](./Kibana%20Windows%20Event%20Logs%20II/README.md)
* **Dataset:** [`discovery_sysmon_3_Invoke_UserHunter_SourceMachine.evtx`](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/Discovery/discovery_sysmon_3_Invoke_UserHunter_SourceMachine.evtx)
* **Scenario:** Active Directory post-exploitation reconnaissance executed using PowerView's `Invoke-UserHunter`.
* **Key Tasks:** Isolating dual-service domain controllers running both LDAP (port 389) and SMB (port 445), quantifying unique file-sharing target servers using Elasticsearch Dev Tools cardinality aggregations, and correlating target hostnames (`DEV_SERVER`) to destination IP addresses.

### 3. [Kibana : Windows Event Logs III](./Kibana%20Windows%20Event%20Logs%20III/README.md)
* **Dataset:** Samir Bousseaden EVTX Attack Samples (IIS Web Shell & Post-Exploitation Execution).
* **Scenario:** Compromise of an Internet Information Services (IIS) web server with in-memory obfuscated payload execution.
* **Key Tasks:** Identifying the compromised application pool from `w3wp.exe` execution, deobfuscating Base64/UTF-16LE encoded PowerShell scripts to extract the XOR decryption key, and tracing child process spawning of Microsoft's `appcmd.exe` utility used for credential and virtual directory harvesting.

---

## 🛠️ Defensive Engineering Value
Each lab solution goes beyond simply capturing flags by providing:
1. **Sigma Rules:** Production-ready detection rules ready to deploy into Splunk, Elastic SIEM, or Microsoft Sentinel.
2. **Hardening Recommendations:** Actionable endpoint and domain-hardening controls (ASR rules, GPO policies, RestrictRemoteSAM, and firewall filtering).
3. **Forensic Dissection:** Low-level explanations of Windows telemetry (Sysmon EID 1, EID 3, Windows Security EID 4688).
