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
| **STUXNET: When Cybersecurity Crossed Into the Physical World** | **Cyber-Physical Sabotage / ICS / SCADA** | Siemens S7-315/417 PLCs, 4 Windows Zero-Days, STEP 7 DLL Proxying, 21s Sensor Replay | **Operation Olympic Games** (2007–2010)<br>~1,000 Centrifuges Destroyed | **Physical State $\neq$ Display State**<br>Hardware Keyswitch in RUN, Data Diodes, Out-of-Band Analog SIS | [Read Case Study](./STUXNET/README.md) |
---

## ⚖️ "The Problem" vs. "How They Solved It": Master Comparative Matrix

Every cybersecurity incident represents a collision between an innovative threat model (The Problem) and an evolving defensive response (How It Was Solved). The following comparative breakdown details the operational crisis and technical solutions across our three landmark case studies:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        INCIDENT MATRIX: THE PROBLEM VS. HOW THEY SOLVED IT                             │
├─────────────────────┬────────────────────────────────────────────┬─────────────────────────────────────┤
│ CASE STUDY          │ THE PROBLEM (ATTACK & FAILURE MODE)        │ HOW THEY SOLVED IT (CONTAIN & FIX)  │
├─────────────────────┼────────────────────────────────────────────┼─────────────────────────────────────┤
│ 1. GENESIS MARKET   │ • Infostealers (RedLine/Vidar) exfiltrated │ • Operation Cookie Monster: FBI,    │
│    (Identity-as-    │   full browser profiles (SQLite session    │   Dutch Politie, Europol seized 11  │
│    a-Service)       │   cookies, autofill, WebGL/canvas hashes). │   domains and 2 backend servers.    │
│                     │ • Custom Genesis Browser plugin replicated │ • 119 global arrests; seized 80M+   │
│                     │   victim fingerprint, bypassing MFA,       │   credentials and 1.5M bot records. │
│                     │   passwords, and IP/geo risk engines.      │ • Politie CheckYourHack released for│
│                     │ • EA Breach: $10 bot Slack cookie allowed  │   citizen victim remediation.       │
│                     │   corporate Slack takeover & 780 GB theft. │ • Architecture: FIDO2/WebAuthn, CAE │
│                     │ • Traditional password resets failed       │   Continuous Access Evaluation, and │
│                     │   because active session tokens persisted. │   DPoP cryptographic token binding. │
├─────────────────────┼────────────────────────────────────────────┼─────────────────────────────────────┤
│ 2. MGM RESORTS      │ • Scattered Spider used LinkedIn OSINT to  │ • High-Stakes Containment: Severed  │
│    INTERNATIONAL    │   vish IT Help Desk, impersonating staff.  │   internal networks, shut down core │
│    (Identity /      │ • Tricked help desk into resetting MFA     │   systems rather than pay ransom    │
│    Social Eng.)     │   token, escalating to Okta Super Admin.   │   ($0 paid, preserving databases).  │
│                     │ • Established rogue Inbound SAML IdP       │ • Mandiant & internal IR evicted    │
│                     │   backdoor to persist across admin resets. │   rogue federations, performed      │
│                     │ • Deployed ALPHV/BlackCat Rust ransomware  │   global Okta/Azure AD reset.       │
│                     │   across 100+ VMware ESXi hypervisors.     │ • Rebuilt ESXi from offline images. │
│                     │ • Disrupted 31 casino resort properties;   │ • Architecture: Banned KBA at help  │
│                     │   ~$100M EBITDAR operational loss.         │   desk; mandatory out-of-band video │
│                     │                                            │   verification; FIDO2 hardware keys.│
├─────────────────────┼────────────────────────────────────────────┼─────────────────────────────────────┤
│ 3. STUXNET          │ • Air-gapped nuclear uranium enrichment    │ • Forensic Discovery: VirusBlokAda  │
│    (Cyber-Physical  │   facility at Natanz crossed via USB.      │   identified zero-click .LNK & BSOD;│
│    Sabotage)        │ • 4 Windows Zero-Days + stolen Realtek and │   Ralph Langner decoded MC7 bytecode│
│                     │   JMicron certificates bypassed OS checks. │   targeting S7-315 and VFD drives.  │
│                     │ • Injected MC7 bytecode into Siemens S7-315│ • Symantec 1.4 Dossier mapped the   │
│                     │   and S7-417 PLCs via Step 7 DLL proxy.    │   complete 15,000-function payload. │
│                     │ • VFD speed manipulation: 1,410 Hz over-   │ • IAEA documented ~1,000 replaced   │
│                     │   speed (plastic rotor stretch) and 2 Hz   │   centrifuges; Natanz re-imaged     │
│                     │   sub-synchronous resonance destruction.   │   STEP 7 stations from clean media. │
│                     │ • 21-second sensor replay in DB89 blinded  │ • Architecture: Hardware keyswitches│
│                     │   SCADA WinCC operators for over a year.   │   locked to RUN; unidirectional data│
│                     │ • Destroyed ~1,000 IR-1 centrifuges.       │   diodes; independent analog SIS.   │
└─────────────────────┴────────────────────────────────────────────┴─────────────────────────────────────┘
```

---

## 🛡️ Master Defense Blueprint: How to Solve the Vulnerabilities & Protect Against Each Incident

The matrix below provides security leaders, enterprise architects, and incident responders with a unified cross-incident blueprint for **solving the underlying vulnerabilities** and **implementing resilient preventative protections**:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        MASTER BLUEPRINT: VULNERABILITY REMEDIATION & DEFENSE                           │
├─────────────────────┬────────────────────────────────────────────┬─────────────────────────────────────┤
│ INCIDENT            │ HOW TO SOLVE THE CORE VULNERABILITY        │ HOW TO PROTECT AGAINST THE INCIDENT │
├─────────────────────┼────────────────────────────────────────────┼─────────────────────────────────────┤
│ 1. GENESIS MARKET   │ • App-Bound Encryption (Chrome 127+):      │ • Continuous Access Evaluation (CAE)│
│    (Identity-as-    │   Encrypts DPAPI master key via SYSTEM     │   to revoke sessions within seconds │
│    a-Service &      │   elevation service, blocking user-mode    │   of anomalous ASN or IP drift.     │
│    Infostealers)    │   infostealers (RedLine/Vidar).            │ • Mandatory Session Revocation:     │
│                     │ • RFC 9449 DPoP & W3C DBSC:                │   Invoke IdP APIs (Entra ID/Okta)   │
│                     │   Binds session tokens to hardware TPM keys│   to invalidate all active cookies; │
│                     │   so stolen cookies cannot be replayed.    │   never rely on password resets.    │
│                     │ • Disable unmanaged binary execution in    │ • Phishing-Resistant FIDO2 keys     │
│                     │   %TEMP% and %APPDATA% via WDAC.           │   and device compliance gateways.   │
├─────────────────────┼────────────────────────────────────────────┼─────────────────────────────────────┤
│ 2. MGM RESORTS      │ • Abolish KBA (NIST SP 800-63B Rev 4):     │ • Phishing-Resistant FIDO2/WebAuthn │
│    INTERNATIONAL    │   Ban static biographical questions at     │   hardware tokens (YubiKeys) for all│
│    (Identity /      │   IT Help Desk; require live video checks  │   administrative personnel.         │
│    Vishing & ESXi   │   with corporate badge photo matching.     │ • Just-in-Time (JIT) PAM: Zero      │
│    Ransomware)      │ • IdP Federation Hardening:                │   standing Super Admin privileges.  │
│                     │   Require break-glass dual-custodian       │ • Virtualization Isolation: Put     │
│                     │   sign-off on Inbound SAML additions.      │   vCenter & ESXi on dedicated out-  │
│                     │ • ESXi Strict Lockdown Mode:               │   of-band management subnets.       │
│                     │   Disable SSH & DCUI; enforce UEFI Secure  │ • Immutable Backups & Extortion     │
│                     │   Boot to reject unapproved ELF lockers.   │   Governance: $0 ransom policy.     │
├─────────────────────┼────────────────────────────────────────────┼─────────────────────────────────────┤
│ 3. STUXNET          │ • Apply MS10-046 & Revoke Certs:           │ • Hardware Optical Data Diodes:     │
│    (Cyber-Physical  │   Neutralize CVE-2010-2568 (.LNK) and push │   Unidirectional physical fiber     │
│    Sabotage &       │   Realtek/JMicron certs to untrusted store.│   prevents reverse OT infiltration. │
│    Industrial ICS)  │ • PLC Hardware Keyswitch to "RUN":         │ • Out-of-Band Analog SIS: Indepen-  │
│                     │   Physically disconnect programming bus    │   dent analog relays & vibration    │
│                     │   write lines, blocking MC7 code injection.│   trips physically scram power.     │
│                     │ • S7comm-Plus & Step 7 DLL Integrity:      │ • Air-Gap Transit Kiosks (Sheep-    │
│                     │   Migrate to S7-1500; enforce Authenticode │   Dip) to scan all contractor USBs. │
│                     │   signatures on communication libraries.   │ • S7comm Deep Packet Inspection.    │
└─────────────────────┴────────────────────────────────────────────┴─────────────────────────────────────┘
```

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

---

### 3. [STUXNET: When Cybersecurity Crossed Into the Physical World](./STUXNET/README.md)
* **Status:** 🟢 **100% Complete — 13 Technical Chapters + Master Landing Portal + Interactive Telemetry Lab + Python Audit Script**
* **Featured Incident:** The 2007–2010 Natanz Nuclear Enrichment Sabotage Operation (~1,000 IR-1 centrifuges decommissioned, 18-month nuclear delay).
* **Key Mechanics:** How Stuxnet bridged an air-gapped facility via weaponized USB media (CVE-2010-2568), subverted 64-bit Windows kernel driver signing with stolen Realtek/JMicron certificates, executed a man-in-the-middle DLL proxy attack on Siemens STEP 7 (`s7otbxdx.dll`), manipulated S7-315/S7-417 PLC microcode (OB1/OB35), and drove centrifuges into 1,410 Hz overspeed and 2 Hz resonant crash while replaying a 21-second loop of pristine sensor data to operators.
* **Chapters Included:**
  * [01: Executive Summary & The Cyber-Physical Paradigm Shift](./STUXNET/01-executive-summary-and-cyber-physical-paradigm.md)
  * [02: Industrial Architecture & The Purdue Model](./STUXNET/02-industrial-architecture-and-purdue-model.md)
  * [03: Air-Gap Traversal & Weaponized Propagation](./STUXNET/03-air-gap-traversal-and-weaponized-propagation.md)
  * [04: The Four Zero-Days & Windows Internals](./STUXNET/04-the-four-zero-days-and-windows-internals.md)
  * [05: Target Validation & Siemens STEP 7 Hooking](./STUXNET/05-target-validation-and-siemens-step7-hooking.md)
  * [06: The PLC Payload & Centrifuge Sabotage Mechanics](./STUXNET/06-the-plc-payload-and-centrifuge-sabotage-mechanics.md)
  * [07: The Deception Engine & Sensor Replay Attacks](./STUXNET/07-the-deception-engine-and-sensor-replay-attacks.md)
  * [08: Discovery, Investigation & Forensic Reverse Engineering](./STUXNET/08-discovery-investigation-and-forensic-reverse-engineering.md)
  * [09: Comprehensive MITRE ATT&CK for ICS Matrix](./STUXNET/09-mitre-attack-for-ics-comprehensive-matrix.md)
  * [10: Blue Team SOC Playbooks & OT Detection Engineering](./STUXNET/10-blue-team-soc-playbooks-and-ot-detection-engineering.md)
  * [11: OT Incident Response & Cyber-Physical Resilience](./STUXNET/11-ot-incident-response-and-cyber-physical-resilience.md)
  * [12: Comparative Analysis — ICS Malware Evolution](./STUXNET/12-comparative-analysis-ics-malware-evolution.md)
  * [13: Seminar Handbook, Tabletop Exercise & Curriculum](./STUXNET/13-seminar-handbook-tabletop-exercise-and-curriculum.md)
* **Interactive Web Lab:** [**Interactive Cyber-Physical Attack Simulator & Centrifuge Telemetry Lab**](./STUXNET/demo-site/index.html) (Live rotor frequency wave canvas, SCADA operator deception split-view, Siemens S7 MC7 bytecode inspector, and MITRE ICS explorer).
* **Custom Tooling:** [`stuxnet_s7comm_audit.py`](./STUXNET/scripts/stuxnet_s7comm_audit.py) (S7comm protocol packet inspector, STEP 7 DLL proxy integrity auditor, and centrifuge rotor resonance stress calculator).


