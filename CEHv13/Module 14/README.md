<div align="center">

![CEH v13 Module 14 Banner](./images/banner.jpg)

# 🛡️ CEH v13 — Module 14: Hacking Web Applications
### Certified Ethical Hacker (CEH v13) Exam Notes • Phase 3: Web, Wireless & Emerging Tech • Technical Study Architecture

[![Certification](https://img.shields.io/badge/Certification-CEH%20v13%20(ANSI%2017024)-0078D4?style=for-the-badge&logo=shield)](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)
[![EC-Council](https://img.shields.io/badge/Exam%20Code-312--50-red?style=for-the-badge&logo=target)](https://www.eccouncil.org/)
[![Track](https://img.shields.io/badge/Module-14%20of%2020-success?style=for-the-badge&logo=git)](../README.md)
[![Phase](https://img.shields.io/badge/Phase-PHASE 3 • WEB APPLICATIONS-orange?style=for-the-badge)](../README.md)

<p align="center">
  <b>Authoritative, exam-oriented study guide and reference architecture for CEH v13 Module 14: Hacking Web Applications. Covers owasp top 10 vulnerabilities, cross-site scripting (xss), csrf, ssrf & api security, attack methodologies, automated tooling, MITRE ATT&CK alignment, and enterprise defensive engineering.</b>
</p>

[📖 Module Hub](../README.md) • [🗺️ Knowledge Base Index](../../README.md)

</div>

---

## 📋 Module Overview & Exam Objectives

In the **EC-Council Certified Ethical Hacker (CEH v13)** certification exam (Exam 312-50), **Module 14: Hacking Web Applications** represents a fundamental domain within **Phase 3: Web, Wireless & Emerging Tech**. Candidates are tested on both theoretical protocol knowledge and hands-on operational commands used to discover, analyze, exploit, and remediate vulnerabilities across modern networked environments.

### Core Learning Domains:
* **OWASP TOP 10 MASTERCLASS:** Broken Access Control, Cryptographic Failures, Insecure Design, and Security Misconfiguration.
* **CROSS-SITE SCRIPTING (XSS):** Stored, Reflected, and DOM-based XSS exploitation, cookie theft, and keylogger injection.
* **FORGERY & SSRF ATTACKS:** Cross-Site Request Forgery (CSRF) and Server-Side Request Forgery (SSRF) targeting cloud metadata.
* **API SECURITY & WAF DEFENSE:** REST/GraphQL vulnerabilities, Mass Assignment, BOLA/IDOR flaws, and Web Application Firewalls.

---

## 🔬 In-Depth Technical Breakdown

### 1. OWASP TOP 10 MASTERCLASS

Broken Access Control, Cryptographic Failures, Insecure Design, and Security Misconfiguration.

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.

### 2. CROSS-SITE SCRIPTING (XSS)

Stored, Reflected, and DOM-based XSS exploitation, cookie theft, and keylogger injection.

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.

### 3. FORGERY & SSRF ATTACKS

Cross-Site Request Forgery (CSRF) and Server-Side Request Forgery (SSRF) targeting cloud metadata.

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.

### 4. API SECURITY & WAF DEFENSE

REST/GraphQL vulnerabilities, Mass Assignment, BOLA/IDOR flaws, and Web Application Firewalls.

* **Core Operational Theory:** Candidates must understand both how threat actors leverage these techniques during offensive operations and how enterprise defenders monitor and detect anomalous behavior.
* **Key Attack Artifacts:** Exam scenarios frequently present command-line strings, configuration files, packet captures, and network connection parameters requiring precise identification of adversary behavior.
* **Exam Relevance:** Directly tested across multiple-choice questions on CEH Exam 312-50.



---

## 🛠️ Tooling & Command Reference Matrix

| Tool / Technology | Category | Primary Function | Exam Utility / Key Syntax |
| :--- | :--- | :--- | :--- |
| **OWASP ZAP** | Application Scanner | Automated dynamic vulnerability scanning (DAST) | `Active & passive vulnerability spidering` |
| **Burp Suite Pro** | Web Proxy / Scanner | Vulnerability interception, scanning, Intruder | `Automated payload fuzzing & API audits` |
| **XSStrike** | XSS Suite | Intelligent parameter analysis & payload creation | ``python xsstrike.py -u 'http://target.com/search?q='`` |
| **Commix** | Command Injection | Automated OS command injection testing | ``commix --url='http://target.com/vuln.php?id=1'`` |

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
