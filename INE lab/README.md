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
| **Kibana: DNS Log Analysis** | **CID 1191** | Network Telemetry & Threat Hunting | Zeek DNS Logs (`logstash-*`) | **T1590.002** (DNS Recon / AXFR)<br>**T1071.004** (DNS Tunneling / TXT)<br>**T1018** (Reverse DNS Discovery) | 🟢 **100% Solved**<br>(7/7 Flags) | [View Solution](./Kibana%20DNS%20log%20analysis/README.md) |
| **Log Anomaly Detection Basics** | **CID 141** | Web Forensics / Anomaly Detection | Web Access Telemetry (`logs.txt`) | **T1190** (Exploit Public-Facing App)<br>**T1595** (Active Scanning)<br>**T1059** (Command & Scripting Interpreter) | 🟢 **100% Solved**<br>(5/5 Anomalies) | [View Solution](./Log%20Anomaly%20Detection%20Basics/README.md) |
| **Compromised Credentials** | **Incident Response** | Windows Host Forensics / Brute Force | Security.evtx (EID 4625/4624) & Sysmon EID 3 | **T1110.001** (Password Guessing)<br>**T1110.003** (Password Spraying)<br>**T1078.003** (Local Accounts)<br>**T1021.002** (SMB) | 🟢 **100% Solved**<br>(Breach Confirmed) | [View Solution](./Compromised%20Credentials/README.md) |
| **Malicious User Behaviour Analysis** | **Insider Threat** | Linux Host Forensics / Insider Threat | `/etc/shadow`, ClamAV, `ss`, `/proc` | **T1078.003** (Local Accounts)<br>**T1204.002** (Malicious File)<br>**T1571** (Non-Standard Port) | 🟢 **100% Solved**<br>(3/3 Tasks) | [View Solution](./Malicious%20User%20Behaviour%20Analysis/README.md) |
| **Apache Error Log Analysis Basics** | **CID 140** | Web Forensics / Error Log Analysis | Apache `error.log` | **T1595.002** (Vulnerability Scanning)<br>**T1110.001** (Password Guessing)<br>**T1083** (File & Directory Discovery) | 🟢 **100% Solved**<br>(7/7 Questions) | [View Solution](./Apache%20Error%20Log%20Analysis%20Basics/README.md) |
| **Apache Log Analysis Basics** | **CID 103** | Web Forensics / Access Log Analysis | Apache `apache_access.log` (10k events) | **T1110.001** (Password Guessing)<br>**T1190** (Exploit Public-Facing App)<br>**T1595.002** (Vulnerability Scanning) | 🟢 **100% Solved**<br>(7/7 Questions) | [View Solution](./Apache%20Log%20Analysis%20Basics/README.md) |
| **False Positive Validation: Trusted Admin Brute-Force** | **SOC Lab** | SOC Triage / Case Management | Wazuh v4.x & TheHive (`10.0.0.11` / `10.0.0.100`) | **T1110** (Brute Force)<br>**T1078** (Valid Accounts)<br>**T1021.004** (SSH) | 🟢 **100% Solved**<br>(Escalated to L2) | [View Solution](./False%20Positive%20Validation%20Trusted%20Admin%20Brute-Force%20Detection/README.md) |
| **Account Creation & Privilege Escalation Attempt** | **SOC Lab** | SOC Triage / Privilege Escalation | Wazuh v4.x & TheHive (`ip-10-0-0-100` / `10.0.0.11`) | **T1136** (Create Account)<br>**T1078** (Valid Accounts)<br>**T1021.004** (SSH)<br>**T1548.003** (Sudoers) | 🟢 **100% Solved**<br>(Escalated to L2) | [View Solution](./Account%20Creation%20&%20Privilege%20Escalation%20Attempt%20Detection/README.md) |
| **PCAP Analysis With Zeek** | **Defender Lab** | Network Forensics / Malware PCAP | Zeek Logs (`conn`, `dns`, `http`, `ssl`, `dhcp`, `kerberos`) | **T1071.001** (Web Protocols)<br>**T1566.001** (Spearphishing Attachment)<br>**T1059.005** (Macros)<br>**T1078** (Valid Accounts) | 🟢 **100% Solved**<br>(15/15 Questions) | [View Solution](./PCAP%20Analysis%20With%20Zeek/README.md) |
| **Attack Emulation & Detection on ELK** | **Defender Lab** | Threat Hunting / Attack Emulation | HELK Stack (Elasticsearch · Kibana · Kafka) + Winlogbeat + Sysmon | **T1218.010** (Regsvr32 Proxy Exec)<br>**T1518.001** (Security Software Discovery)<br>**T1053.005** (Scheduled Task) | 🟢 **100% Solved**<br>(3/3 Attacks) | [View Solution](./Effectively%20Using%20the%20ELK%20Stack/README.md) |
| **Detecting Abnormal Network Connections With Wazuh** | **Defender Lab** | SIEM Detection / Port Anomaly | Sysmon EID 3 (Network Connections) | **T1021.002** (SMB Shares)<br>**T1059.001** (PowerShell)<br>**T1571** (Non-Standard Port) | 🟢 **100% Solved**<br>(Real-time Alerts) | [View Solution](./Detecting%20Abnormal%20Network%20Connections%20With%20Wazuh/README.md) |
| **SOC-1: Analyzing Unusual PowerShell Execution** | **Incident Response** | SOC Triage / PowerShell Deobfuscation | ELK Stack & TheHive (`syntrix` index) | **T1059.001** (PowerShell)<br>**T1027** (Obfuscated Command)<br>**T1071.001** (Web Protocols)<br>**T1105** (Ingress Tool Transfer) | 🟢 **100% Solved**<br>(Escalated to L2) | [View Solution](./SOC-1%20Analyzing%20Unusual%20PowerShell%20Execution/README.md) |
| **Detecting Mimikatz Threat Using Sysmon and Wazuh** | **Defender Lab** | Threat Hunting / Credential Dumping | Sysmon EID 1 (Process), EID 8 (RemoteThread), EID 10 (ProcessAccess) | **T1003.001** (LSASS Memory)<br>**T1078** (Valid Accounts)<br>**T1059.001** (PowerShell) | 🟢 **100% Solved**<br>(Level 12 Alerts) | [View Solution](./Detecting%20Mimikatz%20Threat%20Using%20Sysmon%20and%20Wazuh/README.md) |
| **Detecting PsExec with Wazuh** | **Defender Lab** | SIEM Detection / Lateral Movement | Sysmon EID 12/13 (Registry), EID 17/18 (Pipes) | **T1112** (Modify Registry)<br>**T1543.003** (Windows Service)<br>**T1570** (Lateral Tool Transfer) | 🟢 **100% Solved**<br>(Rules 160010-160013) | [View Solution](./Detecting%20PsExec%20with%20Wazuh/README.md) |
| **Malware Fundamentals: LockBit 2.0 Static Analysis** | **Malware Analysis** | Static Binary Triage & Dissection | HxD, BinText, PE-Tree, VirusTotal | **T1486** (Data Encrypted)<br>**T1484.001** (GPO Modification)<br>**T1562.001** (Disable Tools)<br>**T1070.004** (File Deletion) | 🟢 **100% Solved**<br>(100% Identified) | [View Solution](./Malware%20Fundamentals/README.md) |
| **SOC-1: Scanning for IOCs** | **Incident Response** | Host Forensics / IOC Triage | LOKI IOC Scanner, TheHive 5, VirusTotal | **T1059.001** (PowerShell)<br>**T1547.001** (Startup Folder)<br>**T1562.001** (Disable Tools)<br>**T1003.002** (SAM Dump)<br>**T1003** (Mimikatz) | 🟢 **100% Solved**<br>(Escalated to L2) | [View Solution](./SOC-1%20Scanning%20for%20IOCs/README.md) |
| **SOC-1: Detecting Malware** | **Incident Response** | Wazuh FIM & Sysmon / WannaCry | Wazuh syscheck & Sysmon EID 1 (Process Creation) | **T1204.002** (Malicious File)<br>**T1059.003** (Command Shell)<br>**T1547.001** (Registry Run)<br>**T1490** (Inhibit Recovery)<br>**T1486** (Data Encrypted) | 🟢 **100% Solved**<br>(Escalated to L2) | [View Solution](./SOC-1%20Detecting%20Malware/README.md) |
| **Malware Analysis: Trojan** | **Malware Analysis** | Disguised PDF Dropper / REMnux | `base64dump.py`, `scite`, `iconv`, VirusTotal | **T1036.008** (Masquerade File Type)<br>**T1027** (Obfuscated Command)<br>**T1059.001** (PowerShell)<br>**T1564.003** (Hidden Window)<br>**T1105** (Ingress Tool Transfer) | 🟢 **100% Solved**<br>(Payload Deobfuscated) | [View Solution](./Malware%20Analysis%20Trojan/README.md) |
| **ELK: SSH Logs** | **CID 1138** | Linux Host Telemetry / SSH Brute-Force | OpenSSH Daemon Logs (`ssh-log*`) | **T1110.001** (Password Guessing)<br>**T1110.003** (Password Spraying)<br>**T1078.003** (Local Accounts)<br>**T1021.004** (SSH)<br>**T1571** (Non-Standard Port) | 🟢 **100% Solved**<br>(10/10 Flags) | [View Solution](./ELK%20SSH%20Logs/README.md) |
| **Kibana: Squid Log Analysis** | **CID 1190** | Network Telemetry / Proxy Forensics | Squid Access Logs (`squid-logs*`) | **T1090.002** (Open Proxy)<br>**T1046** (Network Service Scanning)<br>**T1572** (Protocol Tunneling)<br>**T1110.001** (Password Guessing) | 🟢 **100% Solved**<br>(10/10 Flags) | [View Solution](./Kibana%20Squid%20Log%20Analysis/README.md) |
| **MongoDB: Basics** | **CID 230** | Infrastructure Attacks / NoSQL Injection | MongoDB 4.x (`admin`, `city`, `flag`, `users`) | **T1190** (Exploit Public App)<br>**T1087** (Account Discovery)<br>**T1083** (File & Directory Discovery)<br>**T1005** (Data from Local System) | 🟢 **100% Solved**<br>(12/12 Questions) | [View Solution](./MongoDB%20Basics/README.md) |
| **Threat Detection with Elasticsearch & Kibana** | **SOC Lab** | Red-to-Blue Telemetry / Threat Hunting | Sysmon + Winlogbeat → HELK Kafka (`10.0.21.29:9092`) | **T1190** (Rejetto HFS Exploit)<br>**T1059.005** (VBScript)<br>**T1547.001** (Persistence Run Key)<br>**T1003.001** (LSASS Memory Dump) | 🟢 **100% Solved**<br>(8/8 Tasks) | [View Solution](./Threat%20Detection%20With%20Elasticsearch%20And%20Kibana/README.md) |
| **Threat Detection with Wazuh and Sysmon** | **SOC Lab** | Red-to-Blue Telemetry / SIEM Detection | Sysmon (EIDs 1, 8, 10, 13) + Wazuh Manager (`10.0.26.67`) | **T1021.002** (SMB PsExec)<br>**T1078.003** (Pass-The-Hash)<br>**T1055.001** (Remote Injection)<br>**T1136.001** (Local Account) | 🟢 **100% Solved**<br>(7/7 Tasks) | [View Solution](./Threat%20Detection%20with%20Wazuh%20Sysmon/README.md) |

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

### 7. [Apache Error Log Analysis Basics](./Apache%20Error%20Log%20Analysis%20Basics/README.md)
* **Dataset:** `error.log` (Apache 2.x HTTPD Error Telemetry).
* **Scenario:** Forensic analysis of web server errors to uncover automated scanning and directory traversal attempts.
* **Key Tasks:** Filtering 229,112 non-existent page requests from aggressive path bruteforcing, isolating 75 unique usernames from HTTP Basic Auth password spraying, detecting 15 Directory Traversal / LFI requests targeting critical operating system files (`passwd`, `shadow`, `boot.ini`, `sam`), extracting probed URL wordlists, and categorizing the 7-part super-set of web server error types.

### 8. [Apache Log Analysis Basics](./Apache%20Log%20Analysis%20Basics/README.md)
* **Dataset:** `apache_access.log` (10,000 Apache Access Telemetry Entries).
* **Scenario:** Investigation of web traffic volume, endpoint access patterns, client browser distributions, and identification of aggressive automated brute-force attacks.
* **Key Tasks:** Quantifying total access requests (`10,000`), ranking top 5 client IPs to isolate primary attacker `91.141.1.150` (2,842 requests), extracting top 5 User-Agent strings, profiling top URLs requested alongside HTTP methods, evaluating visited URLs, filtering non-200 OK HTTP response codes, and conducting detailed threat attribution into Joomla administrator credential stuffing.

### 9. [False Positive Validation: Trusted Admin Brute-Force Detection](./False%20Positive%20Validation%20Trusted%20Admin%20Brute-Force%20Detection/README.md)
* **Platform & Stack:** Wazuh SIEM v4.x & TheHive Incident Management Platform.
* **Scenario:** Tier 1 SOC triage of an SSH brute-force alert (MITRE T1110) targeting user `root` on internal Ubuntu server `10.0.0.100`.
* **Key Tasks:** Triaging Wazuh MITRE ATT&CK dashboard on date 7th December 2025, correlating source IP `10.0.0.11` to the trusted Syntrix administrator workstation, classifying the incident as a confirmed False Positive (`Severity: LOW`), creating and tagging the case in TheHive with `TLP:CLEAR` / `PAP:CLEAR`, binding sighted IP observables (`10.0.0.11`), and creating a mandatory cross-verification task escalated to SOC Level 2 (`soc2@syntrix.com`).

### 10. [Account Creation & Privilege Escalation Attempt Detection](./Account%20Creation%20&%20Privilege%20Escalation%20Attempt%20Detection/README.md)
* **Platform & Stack:** Wazuh SIEM v4.x & TheHive Incident Management Platform.
* **Scenario:** Tier 1 SOC triage of a multi-stage intrusion sequence involving unauthorized local user creation, remote SSH login, and privilege escalation targeting `/etc/sudoers` on Linux endpoint `ip-10-0-0-100`.
* **Key Tasks:** Reviewing Wazuh MITRE ATT&CK dashboard on date 24th December 2025, correlating unauthorized account creation `eviluser` (T1136 @ 07:41) with subsequent SSH access from `10.0.0.11` (T1021/T1078 @ 07:59) and first-time sudo execution on `/etc/sudoers` (T1548.003 @ 08:00), classifying as a True Positive (`Severity: HIGH`), registering 4 sighted observables (`eviluser`, `10.0.0.11`, `ip-10-0-0-100`, `/etc/sudoers`), defining a mandatory validation task, attaching MITRE TTPs, and reassigning the case to SOC Level 2 (`soc2@syntrix.com`).

### 11. [PCAP Analysis With Zeek](./PCAP%20Analysis%20With%20Zeek/README.md)
* **Platform & Stack:** Zeek (Bro Network Security Monitor), `zeek-cut`, `jq`, `awk` on Ubuntu Target Sensor.
* **Scenario:** Network packet dissection and threat attribution across two complex malware PCAP captures (`Malware1` & `Malware2`).
* **Key Tasks:** Splitting raw PCAPs into Zeek transaction logs (`conn.log`, `http.log`, `dns.log`, `ssl.log`, `dhcp.log`, `kerberos.log`, `files.log`), exporting JSON logs via `LogAscii::use_json=T`, parsing HTTP OCSP transactions with `jq`, extracting destination IP cardinality, uncovering Cobalt Strike TLS C2 (`ceyuvigi.com` / `23.108.57.213:443`) and Bumblebee RAT sessions (`139.177.146.137:443`), fingerprinting Windows client MAC (`00:1e:67:4a:d7:5c`) and hostname (`Nalyvaiko-PC`) via DHCP, extracting Kerberos domain account (`innochka.nalyvaiko`), tracing malicious Word document phishing download (`2018_11Details_zur_Transaktion.doc`), isolating binary payload executable (`6169583.exe` - 429,056 bytes), and identifying the Emotet Trojan campaign.

---

### 12. [Attack Emulation & Detection on ELK Stack](./Effectively%20Using%20the%20ELK%20Stack/README.md)
* **Platform & Stack:** HELK (Hunting ELK) — Elasticsearch · Logstash · Kibana · Kafka · Winlogbeat.
* **Scenario:** Full red-to-blue adversary emulation pipeline using the Atomic Red Team framework on a HELK-backed threat hunting platform.
* **Key Tasks:** Configuring Winlogbeat to ship Windows events to HELK Kafka broker (`hosts: ["10.0.21.29:9092"]`), installing Winlogbeat as a Windows service; importing `Invoke-AtomicRedTeam` PowerShell module; executing three Atomic Red Team tests — `T1218.010-1` (Regsvr32 LOLBAS proxy execution launching `calc.exe` via remote `.sct` scriptlet), `T1518.001-5` (Sysmon filter altitude enumeration via `fltmc.exe | findstr.exe 385201`), and `T1053.005-2` (scheduled task persistence creating `spawn` task → `cmd.exe` at 20:10); detecting all 3 attacks in Kibana Discover with queries `Invoke-Process`, `sysmon`, and `scheduled`; validating full payload capture in Sysmon `payload` field; and correlating the complete attack kill chain.


---

### 13. [Detecting Abnormal Network Connections With Wazuh](./Detecting%20Abnormal%20Network%20Connections%20With%20Wazuh/README.md)
* **Platform & Stack:** Wazuh SIEM v4.x (Ubuntu SOC `10.0.18.204`), Microsoft Sysmon v14.x (Windows Server 2019 `10.0.23.132`), Kali Linux (`10.10.21.2`).
* **Scenario:** Host-based anomaly detection against unauthorized outbound C2 channels and lateral movement using CDB list port whitelisting.
* **Key Tasks:** Deploying Wazuh Agent v4.3.10 silently on Windows Server 2019; installing Microsoft Sysmon with modular XML schema; binding `Microsoft-Windows-Sysmon/Operational` eventchannel to agent `ossec.conf`; authoring CDB constant database list `/var/ossec/etc/lists/common-ports` with standard baseline ports; authoring custom Wazuh Rule `115001` (Level 10) evaluating `win.eventdata.destinationPort` with `lookup="not_match_key"`; simulating Pass-the-Hash via Metasploit SMB PsExec (`exploit/windows/smb/psexec`) triggering an alert on default port 4444; and launching an in-memory PowerShell reverse shell download cradle triggering an alert on non-standard port 1234.

---

### 14. [SOC-1: Analyzing Unusual PowerShell Execution](./SOC-1%20Analyzing%20Unusual%20PowerShell%20Execution/README.md)
* **Platform & Stack:** ELK Stack (Elasticsearch · Kibana `http://localhost:5601`) & TheHive Case Management (`http://localhost:9000`), Target Workstation `FIN-WS-02`.
* **Scenario:** Tier 1 SOC investigation of heavily obfuscated, multi-stage PowerShell payload execution detected in Windows Event Logs during November 2025.
* **Key Tasks:** Investigating `syntrix` index in Kibana Discover; identifying child process spawning of `powershell.exe` from `WINWORD.EXE` (PID `4812`); analyzing 6-layer obfuscation pipeline (Base64 encoding, environment variable concatenation, character array manipulation, and memory decompression); extracting C2 download cradle staging malicious Cobalt Strike beacon from `http://198.51.100.25/beacon.bin`; creating incident case `CAS-2025-11-PS01` in TheHive tagged `TLP:AMBER` / `PAP:AMBER`; and escalating containment playbook to SOC Level 2 (`soc2@syntrix.com`).

---

### 15. [Detecting Mimikatz Threat Using Sysmon and Wazuh](./Detecting%20Mimikatz%20Threat%20Using%20Sysmon%20and%20Wazuh/README.md)
* **Platform & Stack:** Wazuh SIEM v4.x (Ubuntu SOC Manager `10.0.31.41`), Microsoft Sysmon v14.x (Windows Server 2019 `10.0.30.222`).
* **Scenario:** End-to-end simulation and detection of in-memory LSASS credential dumping using Mimikatz (`sekurlsa::logonpasswords` and `privilege::debug`).
* **Key Tasks:** Deploying Wazuh agent silently on Windows Server 2019; configuring Sysmon with modular XML rules monitoring Event ID 1 (`ProcessCreate`), Event ID 8 (`CreateRemoteThread`), and Event ID 10 (`ProcessAccess`); binding Sysmon eventchannel to agent `ossec.conf`; authoring custom high-severity Wazuh Rules `100000`, `100001`, and `100002` (Level 12); executing Mimikatz credential theft; and verifying real-time alerts in the Wazuh Security Events dashboard.

---

### 16. [Detecting PsExec with Wazuh](./Detecting%20PsExec%20with%20Wazuh/README.md)
* **Platform & Stack:** Wazuh SIEM v4.x (Ubuntu SOC Manager `10.0.28.182`), Microsoft Sysmon v14.x (Windows Server 2019 `10.0.19.121`).
* **Scenario:** Forensic detection of administrative and adversary lateral movement via Sysinternals PsExec service creation, named pipes, and registry modifications.
* **Key Tasks:** Integrating Wazuh agent and Sysmon on Windows endpoint; monitoring Registry Event IDs 12/13 and Named Pipe Event IDs 17/18; authoring custom detection rules `160010` (EULA acceptance - MITRE T1112), `160011` (PSEXESVC service creation - MITRE T1543.003), `160012` (service teardown - MITRE T1543.003), and `160013` (named pipe IPC `\PSEXESVC-stdin/stdout/stderr` - MITRE T1570); executing interactive privileged PsExec session; and validating real-time MITRE ATT&CK alerts.

---

### 17. [Malware Fundamentals: LockBit 2.0 Static Analysis](./Malware%20Fundamentals/README.md)
* **Platform & Stack:** Windows Analysis Workstation, HxD Hex Editor, BinText, PE-Tree, VirusTotal, Python (`lockbit_pe_triage.py`).
* **Scenario:** Comprehensive static malware analysis and IOC extraction of captured LockBit 2.0 ransomware payload (`0545f842...`) without executing the binary.
* **Key Tasks:** Verifying DOS magic bytes (`4D 5A`) and compiler-embedded DOS stub in HxD; extracting MSVC Visual Studio 2017 linker telemetry from the Rich Header at offset `0xD8`; extracting 14 categories of high-fidelity strings in BinText (Tor `.onion` leak site, Tox ID, Active Directory GPO weaponization commands, Windows Defender suppression registry keys, and 512KB zero-wipe self-deletion); parsing PE headers, section geometry, and Shannon entropy in PE-Tree (confirming native unpacked binary); identifying minimal static imports (5 DLLs / 9 APIs) as evidence of runtime dynamic API resolution; and generating a complete MITRE ATT&CK mapping.

---

### 18. [SOC-1: Scanning for IOCs](./SOC-1%20Scanning%20for%20IOCs/README.md)
* **Platform & Stack:** Windows Victim Workstation (Syntrix Enterprise), LOKI Simple IOC Scanner, VirusTotal, TheHive 5 Platform (Ubuntu `http://localhost:9000`), Python (`loki_ioc_triage.py`).
* **Scenario:** Host-based forensic triage of a flagged Windows endpoint following user reports of performance degradation and pop-up activity, identifying multi-stage compromise artifacts.
* **Key Tasks:** Executing LOKI full storage volume scan (`.\loki.exe --allhds`); identifying renamed Mimikatz x64 binary in `C:\ProgramData\haha.exe` (Risk Score: 415, VT: 66/72); uncovering Metasploit persistence backdoor `winfix.exe` in the Administrator Startup folder listening on port 4444 (PID 4500 bind shell); identifying unauthorized SAM registry hive backup in `C:\Users\Public`; isolating malicious defense evasion PowerShell script `C:\Windows\Disable.ps1`; initializing incident Case #1 in TheHive (`Severity: Critical`, `TLP:Amber`); registering 7 observables, 4 MITRE ATT&CK TTPs, and 2 investigation tasks; and formally escalating case ownership to SOC Level 2 (`soc2@syntrix.com`).

---

### 19. [SOC-1: Detecting Malware](./SOC-1%20Detecting%20Malware/README.md)
* **Platform & Stack:** Wazuh SIEM v4.x (`http://localhost`), Microsoft Sysmon v14.x, TheHive 5 Platform (`http://localhost:9000`), VirusTotal, Python (`wannacry_wazuh_triage.py`).
* **Scenario:** Incident triage of corporate Windows endpoint `Syntrix-PC04` (`10.0.0.67`) exhibiting high-velocity file modifications and anomalous process spawning following execution under user `daisy`.
* **Key Tasks:** Filtering Wazuh FIM `syscheck` events for December 2025; tracking mass deletion and `.wncry` encrypted file recreation across user directories; isolating initial dropper `C:\Users\daisy\Downloads\CleanXpro.exe`; analyzing Sysmon Event ID 1 process creation events to uncover startup persistence via `tasksche.exe` in the `Run` registry key (MITRE T1547.001); identifying execution of `@WanaDecryptor@.exe` (MD5: `7BF2B57F2A205768755C07F238FB32CC`, confirmed WannaCry on VirusTotal 69/72); analyzing anti-recovery command sequences deleting Volume Shadow Copies (`vssadmin delete shadows /all /quiet`), purging backup catalogs (`wbadmin delete catalog`), and disabling recovery boot options (`bcdedit recoveryenabled no`); creating a Critical Severity incident case in TheHive with `TLP:Amber` / `PAP:Amber`; registering 7 observables and 5 MITRE ATT&CK TTPs; configuring investigation tasks; and escalating case ownership to SOC Level 2 (`soc2@syntrix.com`).

---

### 20. [Malware Analysis: Trojan](./Malware%20Analysis%20Trojan/README.md)
* **Platform & Stack:** REMnux v7.x Forensic Workstation (`https://remnux.ine.local:6901`), Debian Staging Bridge (`172.17.0.1:8000`), `base64dump.py`, SciTE, `iconv`, VirusTotal, Python (`trojan_static_triage.py`).
* **Scenario:** Rigorous static malware triage of weaponized document `info.pdf` masquerading as a benign PDF to uncover embedded droppers and download cradles without detonating malware.
* **Key Tasks:** Staging and hosting `info.zip` via Python HTTP server on port 8000; ingesting and extracting `info.pdf` into REMnux; calculating MD5 hash `e98b04a9d7092c424ae151e3c83ee302` and correlating across VirusTotal (confirmed Trojan.Downloader); parsing Base64 object streams with `base64dump.py` to isolate high-density Object ID 2 (280 bytes); inspecting raw PDF object structure in SciTE editor to isolate `-EncodedCommand` Unicode parameter; deobfuscating UTF-16LE payload via `base64 -d | iconv -f utf-16 -t utf-8`; extracting C2 endpoint `http://ncdbuganda.org/.css/awori.exe` and drop location `%APPDATA%\awori.exe`; and formulating automated triage scripts and Sigma/YARA detection rules.

---

### 21. [Kibana: DNS Log Analysis](./Kibana%20DNS%20log%20analysis/README.md)
* **Platform & Stack:** Elasticsearch & Kibana (`http://localhost:5601`), Zeek DNS Telemetry (`logstash-*`), SecRepo MACCDC 2012 Dataset.
* **Scenario:** Comprehensive SOC threat hunting and network forensics across 280,000+ DNS events to uncover covert channels, protocol abuse, and reconnaissance activities.
* **Key Tasks:** Identifying the top queried domain (`teredo.ipv6.microsoft.com` - 17,219 requests); profiling scanner anomalies with empty DNS questions to isolate host `192.168.202.78` (13,016 requests); diagnosing root cause of DNS server failure returning 99.2% NXDOMAIN responses (`192.168.207.4`) and isolating max NXDOMAIN client `192.168.202.103`; building vertical bar charts to identify top sender `10.10.117.210` (212,277 requests); tracking internal network topology sweeps via reverse DNS PTR lookups (`192.168.202.83` with 11,540 `*in-addr.arpa` queries); auditing 440 unauthorized AXFR DNS zone transfers; and extracting a covert DNS C2 payload (`You’ve been pwned`) in an Apple subdomain TXT record alongside its Zeek connection identifier (`CmjiklOm3bnHgctw`).

---

### 22. [ELK: SSH Log Analysis](./ELK%20SSH%20Logs/README.md)
* **Platform & Stack:** Elasticsearch & Kibana (`http://localhost:5601`), OpenSSH Server Telemetry (`ssh-log*`).
* **Scenario:** Multi-server SSH brute-force campaign forensics, authentication mechanism profiling, credential compromise verification, and breach timeline reconstruction.
* **Key Tasks:** Identifying 3 distinct attacking machines (`192.148.107.6`, `192.148.107.7`, `192.148.107.8`); constructing vertical bar charts to isolate primary attacker `192.148.107.6` (~1,300 attempts); verifying attack exposure across all 3 SSH servers (`192.148.107.3`, `192.148.107.4`, `192.148.107.5`); building two-level nested concentric pie charts to correlate most targeted host (`192.148.107.4`) with top attacker (`192.148.107.6`); profiling 2 active authentication mechanisms (`password` & `publickey`); attributing unauthorized public key break-in to adversary `192.148.107.8`; verifying non-standard SSH daemon port (`3603`); confirming compromised user account (`administrator`); isolating peak log push timestamp (`16:17:58`) via Timelion time-series analysis; and identifying Patient Zero server (`192.148.107.3` / `ssh-server-3`).

---

### 23. [Kibana: Squid Log Analysis](./Kibana%20Squid%20Log%20Analysis/README.md)
* **Platform & Stack:** Elasticsearch & Kibana (`http://localhost:5601`), Squid Access Logs (`squid-logs*`), Nmap, Nikto, Hydra.
* **Scenario:** Open proxy exploitation, internal subnet discovery sweep, FTP directory-busting and credential brute-force, web vulnerability scanning, and authenticated SSH tunneling.
* **Key Tasks:** Identifying initial open proxy verification probe from `192.161.225.4` using Nmap `http-open-proxy`; tracking internal host enumeration across `192.170.46.0/24` generating 328 HTTP 503 errors; constructing Terms aggregations to identify 11 scanned ports; identifying 3 live internal hosts (`192.170.46.1`, `192.170.46.4`, `192.170.46.5`); detecting Nikto web vulnerability scanner from `192.161.225.5` on web server port 80; extracting retrieved `/flag` file and FTP username `billy`; isolating unauthenticated open proxy SSH tunnel to `192.170.46.3:22`; attributing Hydra FTP dictionary attack to `192.161.225.6` (1,030 hits); tracking 45,017 failed proxy authentication attempts (HTTP 407) until user `admin` is compromised by `192.161.225.7`; and measuring authenticated SSH session duration (`28` seconds / 28,202 ms).

---

### 24. [MongoDB: Basics](./MongoDB%20Basics/README.md)
* **Platform & Stack:** MongoDB 4.x Database Shell (`localhost:27017`), US Census Bureau `zips.json` dataset (29,353 records).
* **Scenario:** Database cluster reconnaissance, NoSQL document filtering, relational comparison operations, logical query conjunction/disjunction, regular expression indexing, cursor pagination, and server-side aggregation pipelines.
* **Key Tasks:** Enumerating 7 cluster databases (`show dbs`); auditing collection namespaces to identify 3 collections in database `users`; extracting hidden CTF flag (`fl4g_f0r_m0ng0_db`) from isolated `flag` collection; querying user profile documents to extract email address for user `Heather` (`mauris.sapien@eueratsemper.ca`); calculating collection cardinality for archived users (`179`); filtering US Census records for Massachusetts (`MA` - 474 cities); applying relational comparison operator `$gt` for population > 15,000 (5,785 cities); executing compound logical `$and` queries (Indiana pop > 15,000 = 130 cities) and `$or` queries (pop < 100 or Indiana = 1,376 cities); regex prefix matching (`^AN.*` = 154 cities); offset pagination via `.sort({"city":1}).skip(100).limit(1)` to extract 101st city (`ADDY`); and constructing an aggregation pipeline with `$group` and `$avg` to calculate average population (`8462.79`).

---

### 25. [Threat Detection with Elasticsearch and Kibana](./Threat%20Detection%20With%20Elasticsearch%20And%20Kibana/README.md)
* **Platform & Stack:** Hunting ELK (HELK) on Ubuntu 20.04 (`10.0.21.29:9092` Kafka), Windows Server 2019 (`demo2.ine.local`), Kali Linux, Metasploit, Sysmon, Winlogbeat.
* **Scenario:** End-to-end detection engineering and red-to-blue emulation. Configuring Windows detailed process auditing, deploying SwiftOnSecurity Sysmon, establishing an enterprise Kafka-to-Elasticsearch telemetry pipeline, executing Rejetto HFS 2.3 RCE, planting Meterpreter VBS persistence, dumping LSASS credentials via Mimikatz, and triaging all attacks in Kibana.
* **Key Tasks:** Starting containerized HELK stack (`./helk_install.sh`); enabling Group Policy Detailed Tracking, Process Creation with command line, and Task Scheduler operational logs; deploying Sysmon service (`Sysmon.exe -i sysmonconfig-export.xml`); configuring Winlogbeat to point to Kafka broker `10.0.21.29:9092`; exploiting Rejetto HFS 2.3 via Metasploit (`rejetto_hfs_exec`) and elevating to `SYSTEM`; deploying persistence backdoor (`douwxodqwof.vbs`); dumping NTLM hashes with Mimikatz (`sekurlsa::logonPasswords`); and correlating the entire breach footprint across Kibana Sysmon Dashboards and Discover queries.

---

### 26. [Threat Detection with Wazuh and Sysmon](./Threat%20Detection%20with%20Wazuh%20Sysmon/README.md)
* **Platform & Stack:** Wazuh Manager & Agent v4.x on Ubuntu 20.04 (`10.0.26.67`), Windows Server 2019 (`10.0.18.168`), Microsoft Sysmon v14.x (SwiftOnSecurity), Kali Linux, Metasploit Framework.
* **Scenario:** Enterprise host telemetry forwarding, custom SIEM XML rule authoring, adversary attack emulation via Pass-The-Hash lateral movement, in-memory thread injection, and rogue account provisioning with full Wazuh Security Events UI validation.
* **Key Tasks:** Installing Wazuh Agent MSI silently with manager registration flags; installing SwiftOnSecurity Sysmon configuration; binding `Microsoft-Windows-Sysmon/Operational` eventchannel with client buffering in `ossec.conf`; crafting custom Level 12 XML detection rules (`100000`, `100001`, `100002`) targeting Mimikatz execution, remote thread injection, and LSASS handle access; creating high-level group rule `220000` to promote all Sysmon alerts to the Wazuh Security Events UI; emulating lateral movement via Metasploit `windows/smb/psexec` using captured NTLM hashes (`00000000000000000000000000000000:5c4d59391f656d5958dab124ffeabc20`); executing thread injection and migrating Meterpreter into `explorer.exe`; provisioning backdoor administrator `wazuh-hacker`; and triaging 26+ correlated alerts across the Wazuh Manager dashboard.

---

## 🛠️ Defensive Engineering Value
Each lab solution goes beyond simply capturing flags by providing:
1. **Sigma Rules:** Production-ready detection rules ready to deploy into Splunk, Elastic SIEM, or Microsoft Sentinel.
2. **Hardening Recommendations:** Actionable endpoint and domain-hardening controls (ASR rules, GPO policies, RestrictRemoteSAM, and firewall filtering).
3. **Forensic Dissection:** Low-level explanations of Windows telemetry (Sysmon EID 1, EID 3, Windows Security EID 4688).
