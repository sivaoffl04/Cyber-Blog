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
| **Log Anomaly Detection Basics** | **CID 141** | Web Forensics / Anomaly Detection | Web Access Telemetry (`logs.txt`) | **T1190** (Exploit Public-Facing App)<br>**T1595** (Active Scanning)<br>**T1059** (Command & Scripting Interpreter) | 🟢 **100% Solved**<br>(5/5 Anomalies) | [View Solution](./Log%20Anomaly%20Detection%20Basics/README.md) |
| **Compromised Credentials** | **Incident Response** | Windows Host Forensics / Brute Force | Security.evtx (EID 4625/4624) & Sysmon EID 3 | **T1110.001** (Password Guessing)<br>**T1110.003** (Password Spraying)<br>**T1078.003** (Local Accounts)<br>**T1021.002** (SMB) | 🟢 **100% Solved**<br>(Breach Confirmed) | [View Solution](./Compromised%20Credentials/README.md) |
| **Malicious User Behaviour Analysis** | **Insider Threat** | Linux Host Forensics / Insider Threat | `/etc/shadow`, ClamAV, `ss`, `/proc` | **T1078.003** (Local Accounts)<br>**T1204.002** (Malicious File)<br>**T1571** (Non-Standard Port) | 🟢 **100% Solved**<br>(3/3 Tasks) | [View Solution](./Malicious%20User%20Behaviour%20Analysis/README.md) |

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

### 4. [Log Anomaly Detection Basics](./Log%20Anomaly%20Detection%20Basics/README.md)
* **Dataset:** `logs.txt` (1,000,005 Web Access Log Records).
* **Scenario:** Web application telemetry analysis to isolate hidden malicious probes and syntax corruptions from baseline traffic.
* **Key Tasks:** Developing high-throughput streaming Python pipelines and AWK one-liners, auditing HTTP verb cardinality to detect non-standard method `HEADER`, evaluating temporal calendar semantics to identify impossible day `33` and corrupted month `XYZ`, statistical range modeling to flag numeric outlier `8119`, and enforcing lexical prefix patterns to detect word mutation `crachy`.

### 5. [Compromised Credentials](./Compromised%20Credentials/README.md)
* **Dataset:** Windows Security Event Log (`Security.evtx`) and Sysmon Operational Telemetry.
* **Scenario:** Triage of a Windows host following suspicious login notifications from an employee.
* **Key Tasks:** Enumerating local SAM accounts (`net user`), measuring 3,651 failed authentication attempts (Event ID 4625), isolating attacker IP `13.214.192.125`, confirming Administrator account takeover via Event ID 4624 (Logon Type 3 - Network), and correlating targeted SMB service (TCP Port 445) via Sysmon Event ID 3.

### 6. [Malicious User Behaviour Analysis](./Malicious%20User%20Behaviour%20Analysis/README.md)
* **Dataset:** Ubuntu Linux Host Environment (`/etc/passwd`, `/etc/shadow`, ClamAV, `ss`).
* **Scenario:** Internal hygiene audit of 5 employees to identify careless and negligent behavior following a branch breach.
* **Key Tasks:** Cracking weak user shadow hashes with John the Ripper (`usr1: 12345`), scanning user home directories with ClamAV to uncover trojan malware (`Unix.Ircbot` in `usr1`'s project tree), inspecting listening network sockets with `ss` to detect unauthenticated Netcat listeners on port 4444, and tracing process ownership to `usr1` via `/proc/<PID>/environ`.

---

## 🛠️ Defensive Engineering Value
Each lab solution goes beyond simply capturing flags by providing:
1. **Sigma Rules:** Production-ready detection rules ready to deploy into Splunk, Elastic SIEM, or Microsoft Sentinel.
2. **Hardening Recommendations:** Actionable endpoint and domain-hardening controls (ASR rules, GPO policies, RestrictRemoteSAM, and firewall filtering).
3. **Forensic Dissection:** Low-level explanations of Windows telemetry (Sysmon EID 1, EID 3, Windows Security EID 4688).
