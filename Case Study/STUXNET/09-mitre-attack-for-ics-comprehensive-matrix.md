# Chapter 09: Comprehensive MITRE ATT&CK for ICS Matrix

> **Seminar Module:** Operational Technology Threat Taxonomy & MITRE ATT&CK for ICS Mapping  
> **Target Audience:** OT Security Architects, Detection Engineers, Threat Hunters, Purple Teams  
> **Framework:** MITRE ATT&CK for Industrial Control Systems (ICS) v14

---

## 1. Enterprise IT vs. Industrial ICS ATT&CK Matrices

Traditional cybersecurity teams are accustomed to the **MITRE ATT&CK for Enterprise** matrix, which tracks tactics like *Credential Access*, *Exfiltration*, and *Impact (Data Encrypted for Impact)*.

However, in operational technology and industrial control environments, the ultimate objective of an adversary is not stealing intellectual property or deploying ransomware. The objective is **impairing process control, inhibiting automated safety responses, and inflicting physical damage on machinery**.

To evaluate cyber-physical threats, MITRE developed the **ATT&CK for ICS Matrix**, specifically designed to categorize adversary behaviors across Levels 0, 1, 2, and 3 of the Purdue Model.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    MITRE ATT&CK FOR ICS PROGRESSION IN STUXNET                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   INITIAL ACCESS ──► EXECUTION ──► EVASION ──► DISCOVERY ──► LATERAL MOVEMENT   │
│   • T0847 (USB)      • T0843       • T0856     • T0846       • T0866 (RPC)      │
│   • T0886 (Remote)   • T0823       • T0851     • T0840       • T0867 (P2P)      │
│                                                                                 │
│          │                                                                      │
│          ▼                                                                      │
│                                                                                 │
│   INHIBIT RESPONSE ──────► IMPAIR PROCESS CONTROL ──────► IMPACT                │
│   • T0838 (Modify Alarms)  • T0836 (Modify Parameter)     • T0879 (Property)    │
│   • T0804 (Block Commands) • T0855 (Unauthorized Command) • T0826 (Control Loss)│
│                                                           • T0832 (View Spoof)  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Exhaustive MITRE ATT&CK for ICS Mapping Table

| Tactic | Technique ID | Technique Name | Specific Stuxnet Implementation / Action | Detection Data Sources |
| :--- | :--- | :--- | :--- | :--- |
| **Initial Access** | **T0847** | Replication Through Removable Media | Weaponized USB flash drives using `.lnk` (CVE-2010-2568) and autorun components. | Endpoint USB Device Logs / Sysmon Event ID 1 |
| **Initial Access** | **T0886** | Remote Services | Leveraged SMB and RPC connections across local internal subnets. | Network Flow / Zeek SMB Protocol Logs |
| **Execution** | **T0843** | Program Download | Uploaded injected MC7 bytecode blocks (`OB1`, `OB35`, `DB89`, `FC1865`) into S7-315 PLCs. | S7comm Protocol Telemetry / `s7blk_write` Events |
| **Execution** | **T0823** | Execution through API | Called `LoadLibraryW()` via Windows Shell icon rendering vulnerability. | Windows API Call Monitoring / EDR Process Tree |
| **Persistence** | **T0839** | Module Firmware / Controller Logic | Stored malicious assembly blocks directly in battery-backed PLC RAM/EEPROM memory. | PLC Integrity Hashing / Firmware Dumps |
| **Persistence** | **T0859** | Valid Accounts | Authenticated to local WinCC database using hardcoded vendor password (`21001977`). | Microsoft SQL Server / WinCC Security Logs |
| **Privilege Escalation**| **T0890** | Exploit for Privilege Escalation | Exploited Task Scheduler (CVE-2010-3338) and `win32k.sys` (CVE-2010-2743) to reach SYSTEM. | Windows Event ID 4688 / Kernel Crash Dumps |
| **Evasion** | **T0856** | Spoof Reporting Message | Replayed 21-second recorded baseline telemetry buffer from DB89 to the SCADA HMI. | Inconsistent Analog Sensor Cross-Checks |
| **Evasion** | **T0851** | Rootkit | Deployed signed kernel-mode filter drivers (`mrxnet.sys` & `mrxcls.sys`) to hide files. | Kernel Module Listings / Driver Whitelisting Logs |
| **Evasion** | **T0820** | Exploit OS Vulnerability | Bypassed Windows 64-bit Driver Signature Enforcement using stolen certificates. | Certificate Revocation Lists (CRL) / OCSP Logs |
| **Discovery** | **T0846** | Remote System Discovery | Scanned local networks for listening S7comm services on ISO-on-TCP port 102. | Network IDS / Suricata Port 102 Scan Alerts |
| **Discovery** | **T0840** | Network Connection Enumeration | Identified Siemens CP 342-5 Profibus communication modules on the backplane bus. | PLC Hardware Catalog / STEP 7 Station Data |
| **Lateral Movement** | **T0866** | Exploitation of Remote Services | Exploited Windows Server Service RPC flaw (MS08-067) and Print Spooler (CVE-2010-2729). | Snort / Suricata RPC Overflow Signatures |
| **Lateral Movement** | **T0867** | Lateral Tool Transfer | Synchronized newer malware versions between infected nodes using peer-to-peer RPC. | Internal Host-to-Host RPC Session Spikes |
| **Collection** | **T0811** | Data from Information Repositories | Captured operational sensor baselines and Profibus communication parameters into DB89. | S7 Data Block Monitoring / Memory Read Buffers |
| **Inhibit Response** | **T0838** | Modify Alarm Settings | Intercepted and cleared internal PLC alarm generation registers during overspeed runs. | WinCC Alarm Event Audit Logs |
| **Inhibit Response** | **T0804** | Block Command Message | Suppressed operator-initiated shutdown commands and safety interlock trip relays. | Safety Instrumented System (SIS) Disconnect Logs |
| **Impair Control** | **T0836** | Modify Parameter | Altered Variable Frequency Drive output parameters to 1,410 Hz (overspeed) and 2 Hz (slowdown). | Profibus `DP_SEND` Packet Inspection |
| **Impair Control** | **T0855** | Unauthorized Command Message | Hooked Siemens `s7otbxdx.dll` to transmit forged control packets over the fieldbus. | Industrial Network TAP / S7comm Deep Packet Inspection |
| **Impact** | **T0879** | Damage to Property | Physical disintegration and shattering of aluminum centrifuge rotors and casing structures. | Physical Vibration Sensors / Acoustic Sensors |
| **Impact** | **T0826** | Loss of Control | Complete loss of administrative operational control over centrifuge cascade speeds. | Cascade Flow Rate & Enrichment Metrics |
| **Impact** | **T0832** | Manipulation of View | Displayed falsified normal operating parameters on human-machine interface (HMI) screens. | Plant Historian vs. Independent Analog Gauges |

---

## 3. High-Value Detection Takeaways from the Matrix

Reviewing the MITRE ATT&CK for ICS mapping reveals two critical architectural lessons:

### 1. Dual-Plane Exploitation
Notice that the attack existed across two completely different operational planes:
* **The IT / Windows Plane (T0847, T0886, T0890, T0866):** Handled propagation, credential abuse, privilege escalation, and lateral movement.
* **The OT / Physical Plane (T0843, T0856, T0836, T0879):** Handled protocol hooking, PLC bytecode injection, sensor replay, and mechanical sabotage.

Defenders who monitor only the Windows environment can catch the propagation, but cannot detect the sabotage. Defenders who monitor only the physical process notice the damage, but cannot identify the root digital cause. **Complete defense requires continuous correlation across both planes.**

### 2. The Dominance of "Manipulation of View" (T0832)
In the physical domain, an attacker who pairs process disruption with view manipulation effectively paralyzes the human response loop. Operators will spend hours re-calibrating physical equipment or checking electrical breakers before realizing their digital control system has been weaponized.

---

## 4. Seminar Discussion Questions

1. **Mapping ICS TTPs:** Reviewing technique **T0856 (Spoof Reporting Message)**, how does a modern SOC analyst detect when telemetry received by a SCADA historian is being replayed from a pre-recorded buffer?
2. **Safety System Independence:** In the Purdue hierarchy, why must Safety Instrumented Systems (SIS / Level 1) be engineered with completely separate hardware, power supplies, and logic solvers from the Basic Process Control System (BPCS)?
