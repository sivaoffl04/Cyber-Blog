# 🔎 Cybersecurity Incident & Threat Case Studies

Welcome to the **Case Studies** repository of **Cyber-Blog**. This section contains exhaustive, production-grade post-mortems, forensic dissections, and architectural analyses of landmark cyber incidents, global law enforcement takedowns, advanced threat actor campaigns, and cybercrime marketplace disruptions.

Each case study breaks down:
* **Strategic & Geopolitical Context:** Background, motivation, threat actor attribution, and economic models.
* **Low-Level Technical Mechanics:** Deep-dive dissection of exploited protocols, malware code paths, authentication bypasses, and reverse engineering.
* **Law Enforcement & Takedown Operations:** Multi-jurisdictional task force actions, domain seizures, crypto tracking, and intelligence exploitation.
* **SOC Detection Engineering & SIEM Rules:** Production Sigma, YARA, and Splunk SPL queries to detect and hunt the tradecraft.
* **Incident Response & Defense Playbooks:** Step-by-step containment, eradication, and architectural zero-trust hardening.

---

## 🏆 Featured Case Studies

| Case Study Title | Category | Primary Focus & Threat Actor | Operation / Takedown | Key Takeaway / Defense | Link |
| :--- | :---: | :--- | :---: | :--- | :---: |
| **Genesis Market: From Stolen Credentials to "Identity-as-a-Service"** | **Cybercrime / IAB / Credential Theft** | Genesis "Bots", RedLine/Vidar/Raccoon Infostealers, Session Cookie Hijacking, EA Breach | **Operation Cookie Monster** (4 April 2023)<br>17 Nations, 119 Arrests | **Password Reset ≠ Attack Stopped**<br>Mandatory Session Revocation, FIDO2 MFA, DPoP Token Binding | [Read Case Study](./Genesis%20Market/README.md) |

---

## 📂 Case Study Deep-Dives

### 1. [Genesis Market: A Full Cybersecurity Case Study (Operation Cookie Monster)](./Genesis%20Market/README.md)
* **Status:** 🟢 **100% Complete — 13 Technical Chapters + Master Report + Interactive Demo Site + Python Audit Script**
* **Featured Incident:** The 2021 Electronic Arts (EA) $10 Slack Bot Breach (FIFA 21 & Frostbite Engine source code theft).
* **Key Mechanics:** How Genesis Market combined session cookies, browser fingerprints (WebGL, Canvas, AudioContext), and hardware specs into custom Chromium plugins to bypass MFA without passwords.
* **Chapters Included:**
  * [01: Genesis Market Overview — The Paradigm Shift to "Identity-as-a-Service"](./Genesis%20Market/01-genesis-market-overview.md)
  * [02: Technical Architecture — How Genesis Replicated Digital Identities](./Genesis%20Market/02-technical-architecture.md)
  * [03: The Infostealer Ecosystem — The Malware Engine Behind Genesis](./Genesis%20Market/03-infostealer-ecosystem.md)
  * [04: Initial Access Brokerage (IAB) & The Cybercrime Division of Labor](./Genesis%20Market/04-initial-access-broker.md)
  * [05: Operation Cookie Monster — The Global Law Enforcement Takedown](./Genesis%20Market/05-operation-cookie-monster.md)
  * [06: Digital Forensics & Law Enforcement Intelligence Exploitation](./Genesis%20Market/06-investigation-and-forensics.md)
  * [07: SOC Detection Engineering — Detecting Infostealers & Session Hijacking](./Genesis%20Market/07-soc-detection.md)
  * [08: Splunk SIEM Detection Engineering — Practical SPL Queries](./Genesis%20Market/08-splunk-detection.md)
  * [09: Incident Response Playbook — Infostealer Infection & Session Revocation](./Genesis%20Market/09-incident-response.md)
  * [10: Comprehensive MITRE ATT&CK Matrix Mapping](./Genesis%20Market/10-mitre-attack-mapping.md)
  * [11: Lessons Learned — Strategic & Tactical Recommendations](./Genesis%20Market/11-lessons-learned.md)
  * [12: Deep R&D — Reverse Engineering, Cryptographic Dissection & Forensic Deconstruction](./Genesis%20Market/12-deep-rnd-reverse-engineering-and-forensics.md)
  * [13: Primary Source Forensic R&D — Unsealed FBI Seizure Affidavit & Internet Archive OSINT Dissection](./Genesis%20Market/13-fbi-affidavit-forensic-dissection.md)
* **Interactive Web Lab:** [**Interactive Genesis Market & Zero Trust Simulation**](./Genesis%20Market/demo-site/index.html) (Live catalog search, bot profile inspector, and Zero Trust vs. session replay lab).
* **Custom Tooling:** [`session_cookie_audit.py`](./Genesis%20Market/scripts/session_cookie_audit.py) (Local browser datastore and infostealer staging audit tool).
