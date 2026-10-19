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
| **Inside the MGM Resorts Cyberattack: How Social Engineering Became an Enterprise Incident** | **Identity Compromise / Vishing / Ransomware** | Scattered Spider (UNC3944), ALPHV/BlackCat, Okta Super Admin, Azure AD, VMware ESXi Locker | **The 2023 Las Vegas Campaign** (Sept 2023)<br>~$100M EBITDAR Loss | **Identity is the Perimeter**<br>Ban KBA at Help Desk, Strict ESXi Lockdown, OOB Video Verification | [Read Case Study](./MGM%20Resorts%20International/README.md) |

---

## 📂 Case Study Deep-Dives

### 1. [Genesis Market: A Full Cybersecurity Case Study (Operation Cookie Monster)](./Genesis%20Market/README.md)
* **Status:** 🟢 **100% Complete — 15 Technical Chapters + Master Report + Interactive Demo Site + Python Audit Script**
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
  * [14: Industry Reports Synthesis & Comparative Landmark Case Studies](./Genesis%20Market/14-industry-reports-synthesis-and-comparative-case-studies.md)
  * [15: Authentic Web Infrastructure, Source Code Dissection & Portal Cloning](./Genesis%20Market/15-authentic-web-infrastructure-source-code-and-portal-cloning.md)
* **Interactive Web Lab:** [**Interactive Genesis Market & Zero Trust Simulation**](./Genesis%20Market/demo-site/index.html) (Live catalog search, bot profile inspector, authentic portal clone with CIS safe-harbor terms, Politie CheckYourHack verification engine, and Zero Trust lab).
* **Custom Tooling:** [`session_cookie_audit.py`](./Genesis%20Market/scripts/session_cookie_audit.py) (Local browser datastore and infostealer staging audit tool).

---

### 2. [Inside the MGM Resorts Cyberattack: How Social Engineering Became an Enterprise-Wide Cyber Incident](./MGM%20Resorts%20International/README.md)
* **Status:** 🟢 **100% Complete — 13 Technical Chapters + Master Landing Portal + Interactive Demo Lab + Python Audit Script**
* **Featured Incident:** The September 2023 MGM Resorts International Cyberattack (31 properties disrupted, ~$100M EBITDAR impact, $0 ransom paid).
* **Key Mechanics:** How Scattered Spider (UNC3944) leveraged LinkedIn OSINT to vish the IT help desk, reset Okta Super Admin MFA, tampered with Inbound SAML Federation, and partnered with ALPHV/BlackCat to deploy Rust ransomware across 100+ VMware ESXi hypervisors.
* **Chapters Included:**
  * [01: Executive Summary & Incident Overview](./MGM%20Resorts%20International/01-executive-summary-and-incident-overview.md)
  * [02: Threat Actor Landscape — Scattered Spider & ALPHV/BlackCat](./MGM%20Resorts%20International/02-threat-actor-landscape-scattered-spider-alphv.md)
  * [03: Reconnaissance & Help Desk Voice Phishing (Vishing)](./MGM%20Resorts%20International/03-reconnaissance-and-helpdesk-vishing.md)
  * [04: Identity Compromise & Okta Administration](./MGM%20Resorts%20International/04-identity-compromise-and-okta-administration.md)
  * [05: Lateral Movement & ESXi Mass Encryption](./MGM%20Resorts%20International/05-lateral-movement-and-esxi-mass-encryption.md)
  * [06: Incident Response, Containment Dilemma & Impact](./MGM%20Resorts%20International/06-incident-response-containment-dilemma-and-impact.md)
  * [07: Control Breakdowns & Defensive Resilience](./MGM%20Resorts%20International/07-control-breakdowns-and-defensive-resilience.md)
  * [08: Comprehensive MITRE ATT&CK Matrix Mapping](./MGM%20Resorts%20International/08-comprehensive-mitre-attack-matrix.md)
  * [09: Blue Team & SOC Detection Playbooks](./MGM%20Resorts%20International/09-blue-team-and-soc-detection-playbooks.md)
  * [10: SIEM Detection Engineering — Splunk & Sigma](./MGM%20Resorts%20International/10-siem-detection-engineering-splunk-and-sigma.md)
  * [11: Identity Architecture & Help Desk Hardening](./MGM%20Resorts%20International/11-identity-architecture-and-helpdesk-hardening.md)
  * [12: Comparative Case Study — MGM Resorts vs. Caesars Entertainment](./MGM%20Resorts%20International/12-comparative-case-study-mgm-vs-caesars.md)
  * [13: Seminar Handbook, Tabletop Exercises & Curriculum](./MGM%20Resorts%20International/13-seminar-handbook-tabletop-exercises-and-curriculum.md)
* **Interactive Web Lab:** [**Interactive MGM Resorts Identity Attack Path & Seminar Lab**](./MGM%20Resorts%20International/demo-site/index.html) (Live help desk vishing simulator, 6-stage interactive attack path explorer, SOC SIEM telemetry console, and verification risk calculator).
* **Custom Tooling:** [`identity_helpdesk_audit.py`](./MGM%20Resorts%20International/scripts/identity_helpdesk_audit.py) (Okta SystemLog anomaly hunt, help desk verification policy scoring, and ESXi hardening audit tool).

