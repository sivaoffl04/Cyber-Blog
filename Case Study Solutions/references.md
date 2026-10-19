# 📚 Consolidated Research Sources, Forensic Evidence & Technical References

> **Primary Source Reference Library**  
> **Repository Base:** [`Cyber-Blog/Case Study Solutions/`](file:///c:/Users/putin/Downloads/Cyber-Blog/Case%20Study%20Solutions/README.md)  
> **Incidents Covered:** Genesis Market (IDaaS), MGM Resorts International (Identity/Vishing/Ransomware), STUXNET (ICS/SCADA Cyber-Physical Sabotage)

---

## 1. Genesis Market & The Infostealer Ecosystem

### Primary Court Documents & Law Enforcement Disclosures
1. **United States District Court for the Eastern District of Wisconsin:**
   * *In the Matter of the Seizure of Services and Domains Associated with Genesis Market*, Unsealed Seizure Warrant & Affidavit, Case No. 2:23-mj-00365-SCD, Signed by U.S. Magistrate Judge Stephen C. Dries, April 2023. [Archived on Internet Archive](https://archive.org/details/genesis-market-affidavit).
   * *Forensic Evidence Documented:* 115 undercover bot purchases by the FBI Milwaukee Cyber Task Force; cryptocurrency clustering tracking merchant Bitcoin wallet `1...J43QW` to Russian payment services YooMoney and WebMoney; physical server seizure in Limburg, Germany, and Helsinki, Finland.
2. **Europol Official Press Release:**
   * *Takedown of Notorious Hacker Marketplace Selling Your Identity to Criminals (Operation Cookie Monster)*, Press Release, The Hague, Netherlands, 5 April 2023.
   * *Key Metrics:* 119 arrests, 208 physical searches, 97 knock-and-talk preventive visits across 17 partner nations.
3. **Dutch National Police (Politie):**
   * *Operation Cookie Monster & CheckYourHack.nl Citizen Remediation Portal*, National High Tech Crime Unit (NHTCU), April 2023.
   * *Key Findings:* Recovery of over 80 million credential and cookie records; release of public citizen verification engine.
4. **United States Department of Justice (DOJ):**
   * *Criminal Marketplace Disrupted in International Cyber Operation*, Office of Public Affairs, Washington, D.C., 5 April 2023.

### Technical Standards & Engineering Publications
5. **Internet Engineering Task Force (IETF):**
   * *RFC 9449: OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP)*, Standards Track, D. Fett, K. Campbell, J. Bradley, September 2023. [IETF Datatracker](https://datatracker.ietf.org/doc/html/rfc9449).
6. **Google Chromium Core Security Architecture:**
   * *App-Bound Encryption in Google Chrome for Windows*, Chromium Security Blog & Engineering Documentation, July 2024.
   * *Technical Mechanism:* Migration of DPAPI AES master key decryption to `elevation_service.exe` running under `NT AUTHORITY\SYSTEM` with Authenticode verification.
7. **W3C Web Incubator Community Group (WICG):**
   * *Device Bound Session Credentials (DBSC) Specification*, Google Chrome Security Architecture, 2024. [GitHub WICG/dbsc](https://github.com/WICG/dbsc).
8. **Electronic Arts (EA) Security Advisory:**
   * *Statement on Cybersecurity Incident and Exfiltration of Proprietary Frostbite Engine Source Code*, Electronic Arts Corporate Communications, June 2021.

---

## 2. MGM Resorts International Cyberattack

### Official Corporate Filings & Disclosures
1. **United States Securities and Exchange Commission (SEC):**
   * *MGM Resorts International Form 8-K Current Report*, Commission File Number 001-10362, Disclosing Unauthorized Cyber Activity, Proactive Network Severance, and Financial Impact, Filed 5 October 2023. [SEC EDGAR Filing](https://www.sec.gov/Archives/edgar/data/789570/000119312523251667/d461062d8k.htm).
   * *Financial Impact Documented:* Approximately $100 million negative impact to Adjusted Property EBITDAR for Q3 2023; less than $10 million in one-time advisory and technical fees.
2. **MGM Resorts International Investor Relations:**
   * *MGM Resorts Update on Recent Cybersecurity Issue*, Official Press Release, Las Vegas, Nevada, 5 October 2023. [MGM Investor Relations](https://investors.mgmresorts.com/2023-10-05-MGM-RESORTS-UPDATE-ON-RECENT-CYBERSECURITY-ISSUE).

### Government Cybersecurity Advisories
3. **Cybersecurity and Infrastructure Security Agency (CISA) & Federal Bureau of Investigation (FBI):**
   * *Joint Cybersecurity Advisory: Scattered Spider (UNC3944 / Octo Tempest / Muddled Libra)*, Advisory AA23-320A, Released 16 November 2023.
   * *Adversary Tradecraft:* Voice phishing (vishing) targeting IT help desks, SIM-swapping, multi-factor authentication (MFA) fatigue, Inbound SAML federation tampering, and ALPHV ransomware deployment.
4. **National Institute of Standards and Technology (NIST):**
   * *NIST Special Publication 800-63B Rev. 4: Digital Identity Guidelines — Authentication and Lifecycle Management*, U.S. Department of Commerce, 2023.
   * *Key Guidance:* Explicit prohibition of Knowledge-Based Authentication (KBA) for identity proofing and credential recovery.

### Industry Threat Intelligence & Technical Postmortems
5. **Mandiant / Google Cloud Threat Intelligence:**
   * *M-Trends 2024: Inside Advanced Social Engineering and Cloud Identity Exploitation*, Mandiant Threat Research, April 2024.
6. **VMware Security Configuration Guidelines:**
   * *Securing VMware ESXi and vCenter Server: Lockdown Mode and Hypervisor Hardening*, VMware vSphere Documentation, Version 8.0, 2023.

---

## 3. STUXNET Industrial Control System (ICS) Sabotage

### Primary Forensic Research & Reverse Engineering
1. **Symantec Security Response:**
   * *W32.Stuxnet Dossier: Comprehensive Analysis of the First Cyber-Physical Weapon*, Nicolas Falliere, Liam O'Murchu, and Eric Chien, Version 1.4, February 2011.
   * *Forensic Breakthroughs Documented:* Deconstruction of 15,000 functions; disassembly of Siemens STEP 7 DLL proxy (`s7otbxdx.dll`); discovery of S7-315 and S7-417 MC7 bytecode; identification of Fararo Paya and Vacon frequency drive setpoints; analysis of the 21-second DB89 telemetry replay buffer.
2. **The Langner Group:**
   * *To Kill a Centrifuge: A Technical Analysis of What Stuxnet's Creators Tried to Achieve*, Ralph Langner, Langner Communications, November 2013.
   * *Key Engineering Insights:* Detailed mechanical resonance analysis ($2\text{ Hz}$ harmonic crash and $1,410\text{ Hz}$ overspeed hoop stress); separation of Stuxnet 0.5 (valve overpressurization) from Stuxnet 1.x (frequency drive manipulation).
3. **VirusBlokAda (Minsk, Belarus):**
   * *Rootkit.TmpHider: Discovery of the First Stuxnet Samples*, Sergey Ulasen and Oleg Kupreev, June 2010.
   * *Historical Milestone:* First isolation of the `.lnk` zero-day (CVE-2010-2568) and stolen Realtek Semiconductor digital certificates on crashing industrial machines in Iran.

### International Regulatory & Government ICS Advisories
4. **International Atomic Energy Agency (IAEA):**
   * *Implementation of the NPT Safeguards Agreement and Relevant Provisions of Security Council Resolutions in the Islamic Republic of Iran*, Report by the Director General, Board of Governors Document GOV/2010/62, Vienna, Austria, 23 November 2010.
   * *Physical Ground Truth:* Documented drop in operating centrifuges at the Natanz Fuel Enrichment Plant (FEP) from ~4,700 to ~3,900 between late 2009 and early 2010, confirming the physical destruction of roughly 1,000 IR-1 centrifuges.
5. **Cybersecurity and Infrastructure Security Agency (CISA) / US-CERT:**
   * *ICS-CERT Advisory ICSA-10-272-01: Siemens SIMATIC WinCC and STEP 7 Vulnerabilities Associated with Stuxnet*, October 2010.
6. **Microsoft Security Bulletins:**
   * *Microsoft Security Bulletin MS10-046 — Critical: Vulnerability in Windows Shell Could Allow Remote Code Execution (CVE-2010-2568)*, August 2010.
   * *Microsoft Security Bulletin MS10-061 — Critical: Vulnerability in Print Spooler Service Could Allow Remote Code Execution (CVE-2010-2729)*, September 2010.

---

## 4. Common Vulnerabilities and Exposures (CVE) & Weakness (CWE) Index

| Identifier | Class | Title / Formal Description | Target Environment |
| :--- | :---: | :--- | :--- |
| **CVE-2010-2568** | **CVE** | Windows Shell Shortcut Parsing Arbitrary DLL Loading | Microsoft Windows (`shell32.dll` / Stuxnet) |
| **CVE-2010-2729** | **CVE** | Windows Print Spooler Service Remote Code Execution | Microsoft Windows (`spoolsv.exe` / Stuxnet) |
| **CVE-2010-3338** | **CVE** | Windows Task Scheduler Privilege Escalation | Microsoft Windows (Stuxnet) |
| **CVE-2010-2743** | **CVE** | Windows Keyboard Layout Driver Elevation of Privilege | Microsoft Windows (`win32k.sys` / Stuxnet) |
| **CWE-312** | **CWE** | Cleartext Storage of Sensitive Information | Chromium `Local State` (Genesis Market) |
| **CWE-522** | **CWE** | Insufficiently Protected Credentials | Windows DPAPI User-Mode Key Decryption |
| **CWE-287** | **CWE** | Improper Authentication | Unbound HTTP Bearer Session Cookies |
| **CWE-384** | **CWE** | Session Fixation / Session Replay | Genesis Browser Plugin Emulation |
| **CWE-303** | **CWE** | Incorrect Implementation of Authentication Algorithm | Help Desk Knowledge-Based Auth (MGM) |
| **CWE-290** | **CWE** | Authentication Bypass by Spoofing | Okta Inbound SAML Federation Backdoor |
| **CWE-284** | **CWE** | Improper Access Control | VMware ESXi Management Subnet Access |
| **CWE-427** | **CWE** | Uncontrolled Search Path Element (DLL Hijacking) | Siemens STEP 7 `s7otbxdx.dll` Proxying |
| **CWE-306** | **CWE** | Missing Authentication for Critical Function | Siemens S7comm Protocol (TCP Port 102) |
| **CWE-294** | **CWE** | Authentication Bypass by Capture-Replay | 21-Second SCADA Sensor Replay (`DB89`) |

---

*Part of the **Cyber-Blog** Technical Incident Investigation & Architectural Security Suite.*
