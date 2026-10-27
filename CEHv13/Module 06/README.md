<div align="center">

![CEH v13 Module 06 Banner](./images/banner.jpg)

# 🛡️ CEH v13 — Module 06: System Hacking
### Certified Ethical Hacker (CEH v13) Exam Notes • Phase 2: Network & Host Hacking • Technical Study Architecture

[![Certification](https://img.shields.io/badge/Certification-CEH%20v13%20(ANSI%2017024)-0078D4?style=for-the-badge&logo=shield)](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)
[![EC-Council](https://img.shields.io/badge/Exam%20Code-312--50-red?style=for-the-badge&logo=target)](https://www.eccouncil.org/)
[![Track](https://img.shields.io/badge/Module-06%20of%2020-success?style=for-the-badge&logo=git)](../README.md)
[![Phase](https://img.shields.io/badge/Phase-PHASE 2 • SYSTEM EXPLOITATION-orange?style=for-the-badge)](../README.md)

<p align="center">
  <b>Authoritative, exam-oriented study guide and reference architecture for CEH v13 Module 06: System Hacking. Covers privilege escalation, password cracking, pivoting, rootkits & log wiping tradecraft, attack methodologies, automated tooling, MITRE ATT&CK alignment, and enterprise defensive engineering.</b>
</p>

[📖 Module Hub](../README.md) • [📋 PDF Part 1](./CEHv13%20-%20Module%2006%20-%20System%20Hacking%20Part%201.pdf) • [📋 PDF Part 2](./CEHv13%20-%20Module%2006%20-%20System%20Hacking%20Part%202.pdf) • [📋 PDF Part 3](./CEHv13%20-%20Module%2006%20-%20System%20Hacking%20Part%203.pdf) • [🗺️ Knowledge Base Index](../../README.md)

</div>

---

### 📖 Official Courseware Slide Deck

<div align="center">

[![Official CEH v13 Module 06 Slide Deck Cover](./images/pdf_cover.png)](./CEHv13%20-%20Module%2006%20-%20System%20Hacking%20Part%201.pdf)

*EC-Council Certified Ethical Hacker (CEH v13) Official Course Slide Deck Reference*

</div>

---

## 📋 Module Overview & Exam Objectives

In the **EC-Council Certified Ethical Hacker (CEH v13)** certification exam (Exam 312-50), **Module 06: System Hacking** represents a fundamental domain within **Phase 2: Network & Host Hacking**. Candidates are tested on both theoretical protocol knowledge and hands-on operational commands used to discover, analyze, exploit, and remediate vulnerabilities across modern networked environments.

### Core Learning Domains:
* **AUTHENTICATION BREAKING:** Offline hash cracking (Hashcat, John the Ripper), rainbow tables, and Pass-the-Hash (PtH).
* **PRIVILEGE ESCALATION:** Windows Token Manipulation, Unquoted Service Paths, Linux Sudoers abuse, SUID binaries, and kernel bugs.
* **PIVOTING & LATERAL MOVEMENT:** Port forwarding, SSH tunneling, proxychains, and Meterpreter routing across segmented subnets.
* **COVERING TRACKS & ROOTKITS:** Disabling Windows Event Logs, auditd tampering, Timestomping metadata, and kernel-mode rootkits.

---

## 🔬 In-Depth Technical Breakdown

### 1. AUTHENTICATION BREAKING

Offline hash cracking (Hashcat, John the Ripper), rainbow tables, and Pass-the-Hash (PtH).

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.

### 2. PRIVILEGE ESCALATION

Windows Token Manipulation, Unquoted Service Paths, Linux Sudoers abuse, SUID binaries, and kernel bugs.

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.

### 3. PIVOTING & LATERAL MOVEMENT

Port forwarding, SSH tunneling, proxychains, and Meterpreter routing across segmented subnets.

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.

### 4. COVERING TRACKS & ROOTKITS

Disabling Windows Event Logs, auditd tampering, Timestomping metadata, and kernel-mode rootkits.

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.



---

## 🛠️ Tooling & Command Reference Matrix

| Tool / Technology | Category | Primary Function | Exam Utility / Key Syntax |
| :--- | :--- | :--- | :--- |
| **Hashcat** | GPU Password Cracker | High-velocity rule-based hash cracking | ``hashcat -m 1000 -a 0 ntlm.hashes rockyou.txt`` |
| **John the Ripper** | Password Cracker | CPU/GPU hash & archive cracking | ``john --wordlist=rockyou.txt hashes.txt`` |
| **Mimikatz** | Credential Extraction | LSASS memory dumping & ticket creation | ``sekurlsa::logonpasswords`` |
| **Chisel** | Pivoting / Tunneling | Fast TCP/UDP reverse proxy via HTTP | ``chisel server --port 8000 --reverse`` |

---

## 🛡️ Enterprise Countermeasures & Hardening Guidelines

1. **Principle of Least Privilege:** Enforce strict role-based access control (RBAC) and minimize attack surfaces across network daemons.
2. **Defensive Telemetry & Logging:** Centralize event logging (SIEM) with real-time alerting on anomalous spikes, connection retries, and unauthorized protocol commands.
3. **Continuous Auditing & Patching:** Regularly scan infrastructure using automated vulnerability scanners and enforce strict SLA timelines for critical and high vulnerabilities.
4. **Network Segmentation & Zero Trust:** Isolate sensitive subnets, database tiers, and management interfaces behind stateful firewalls and intrusion prevention systems (IPS).

---

## 📚 Official References & Study Resources

* [EC-Council Official CEH v13 Program](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)
* [CEH v13 Master Curriculum Index](../README.md)
* [National Vulnerability Database (NVD)](https://nvd.nist.gov/)
* [MITRE ATT&CK Framework](https://attack.mitre.org/)
