# 🛡️ 07: SOC Detection Engineering — Detecting Infostealers & Session Hijacking

![Genesis Architecture](./images/genesis_market_architecture.jpg)

> **Detection Philosophy:** Defense-in-Depth Across Two Orthogonal Telemetry Planes  
> **Plane 1 (Endpoint):** Catching the Infostealer During Credential Harvesting & Staging  
> **Plane 2 (Identity & Cloud):** Catching the Adversary Replaying Cloned Sessions in Cloud Tenants  
> **Target Frameworks:** MITRE ATT&CK, Sigma, YARA, Splunk ES, Microsoft Entra ID  

---

## 🧭 1. The Dual-Plane Detection Strategy

To successfully defend against Genesis-style threats, a modern Security Operations Center (SOC) must understand that **endpoint alerts and identity logs cannot be treated as separate silos**. 

The attacker's kill chain spans two distinct operational planes:
1. **The Endpoint Plane:** Where malware harvests the raw cookies and digital fingerprint.
2. **The Identity & Cloud Plane:** Where the criminal buyer replays the stolen session into corporate cloud services.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     THE TWO-PLANE DETECTION ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   [PLANE 1: ENDPOINT DETECTION]                                                 │
│   Target: Infostealer Execution (RedLine, Vidar, Raccoon)                       │
│   Telemetry: EDR Process Trees, Sysmon EID 1 & 11, DPAPI Audit Logs             │
│   Key Focus:                                                                    │
│   ├── Unsigned binary accessing %LOCALAPPDATA%\Google\Chrome\User Data          │
│   ├── Anomalous call to CryptUnprotectData() by non-browser process             │
│   └── Rapid creation of 'cookies.txt', 'passwords.txt', or ZIPs in %TEMP%       │
│                                                                                 │
├─────────────────────────────────────────┬───────────────────────────────────────┤
│                                         │                                       │
│                                         ▼ (Data exfiltrated to Genesis)         │
│                                                                                 │
│   [PLANE 2: CLOUD & IDENTITY DETECTION] │                                       │
│   Target: Session Replay / Token Hijacking via Genesis Plugin                   │
│   Telemetry: Okta System Log, Entra ID Sign-ins, Google Workspace Audit         │
│   Key Focus:                                                                    │
│   ├── Impossible Travel (Geographic velocity violation)                         │
│   ├── TLS JA3/JA4 fingerprint or User-Agent shift on existing session cookie    │
│   ├── Session connection from residential proxy or commercial VPN               │
│   └── Zero recent MFA challenge recorded for newly initiated administrative task│
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 2. Endpoint Detection Engineering

### A. Non-Browser Process Accessing Browser Vaults
This is the single most reliable, high-fidelity indicator of infostealer activity. Legitimate browser databases (`Network\Cookies`, `Login Data`, `key4.db`) should **only ever be accessed by certified browser binaries**.

#### Sigma Detection Rule:
```yaml
title: Non-Browser Process Accessing Browser Credential or Cookie Store
id: 5f9a8b1c-3d2e-4a7b-8f1e-9a2c3d4e5f6a
status: production
description: Detects an unauthorized non-browser executable accessing Chrome, Edge, or Firefox credential databases.
author: Syntrix SOC Defense Operations
date: 2026/10/18
logsource:
    category: file_access
    product: windows
detection:
    target_files:
        TargetFilename|contains:
            - '\Google\Chrome\User Data\Default\Network\Cookies'
            - '\Google\Chrome\User Data\Default\Login Data'
            - '\Microsoft\Edge\User Data\Default\Network\Cookies'
            - '\Microsoft\Edge\User Data\Default\Login Data'
            - '\Mozilla\Firefox\Profiles\'
        TargetFilename|endswith:
            - '\cookies.sqlite'
            - '\key4.db'
            - '\logins.json'
    filter_legitimate_browsers:
        Image|endswith:
            - '\chrome.exe'
            - '\msedge.exe'
            - '\firefox.exe'
            - '\brave.exe'
            - '\opera.exe'
    condition: target_files and not filter_legitimate_browsers
falsepositives:
    - Legitimate browser migration utilities or backup software (must be specifically whitelisted by hash)
level: critical
tags:
    - attack.credential_access
    - attack.t1539
    - attack.t1555.003
```

### B. Infostealer Staging Artifact Creation
Infostealers almost universally assemble structured text files or zip archives in user-writable directories.

#### Sysmon Event ID 11 (FileCreate) Pattern:
* Target Directory: `C:\Users\*\AppData\Local\Temp\*` or `C:\ProgramData\*`
* Filename matching: `*cookies.txt`, `*passwords.txt`, `*autofill.txt`, `*system_info.txt`, `*wallets.txt`
* An alert should trigger immediately when a non-standard script or executable creates files matching these exact names.

---

## ☁️ 3. Identity & Cloud Detection Engineering

When an adversary imports a Genesis bot into their custom browser and accesses your cloud environment (e.g., Okta, Microsoft Entra ID, AWS Console, Google Workspace), they produce subtle anomalies in identity audit logs.

### A. Impossible Travel (Geographic Velocity Violation)
Because the legitimate employee is working from one location (e.g., London, UK) and the Genesis buyer is connecting from another (e.g., Bucharest, Romania or a US residential proxy), the employee's active session will suddenly appear from two vastly separated geographic coordinates within minutes:
$$\text{Velocity} = \frac{\Delta \text{Distance (km)}}{\Delta \text{Time (hours)}}$$
If $\text{Velocity} > 800\text{ km/h}$, the connection physically exceeds commercial airliner travel speeds, indicating token theft or unauthorized proxying.

### B. JA3 / JA4 & TLS Fingerprint Mismatch
Even though the Genesis browser plugins effectively spoof client-side JavaScript attributes (like `navigator.userAgent` and screen resolution), **spoofing the underlying TLS cipher suites negotiated at the TCP/TLS handshake level is significantly harder**.
* A legitimate employee's browser on Windows 11 negotiates a specific **JA4 TLS fingerprint**.
* When the adversary runs the Genesis plugin on Linux or through an interception proxy, the client's TLS handshake exhibits a divergent JA4 signature despite presenting the exact same HTTP `User-Agent`.
* Identifying a **JA4 fingerprint shift mid-session on the same active session cookie** is an undeniable indicator of session hijacking.

### C. Residential Proxy & Anonymization Telemetry
Sophisticated Genesis buyers use residential proxy networks (such as Bright Data, Oxylabs, or Smartproxy) to route their traffic through an IP address geographically adjacent to the victim's city.
* Cloud identity providers must integrate threat intelligence feeds that flag **Autonomous System Numbers (ASNs) associated with known proxy exit nodes, VPN hosting providers, or bulletproof datacenters**.

---

## 🔗 4. The Multi-Telemetry Correlation Rule

The failure of many security operations centers during Genesis-related compromises lies in isolated alert handling:
* An analyst sees a low-level EDR alert for an unsigned file in `%TEMP%` and closes it as "adware."
* Two hours later, a cloud identity alert fires for a login from a new ASN and is closed because "the user possesses a valid session cookie."

**Modern SOCs must automate cross-plane correlation:**

```
TRIGGER INCIDENT ESCALATION WHEN:
    [Endpoint Alert]
        Anomalous file read of Chrome 'Cookies' or 'Login Data'
    IS FOLLOWED WITHIN 24 HOURS BY:
    [Identity Alert]
        The same user account initiates a cloud session from a new IP/ASN
        OR
        Presents a new browser fingerprint
    ACTION:
        1. Auto-quarantine the endpoint via EDR API.
        2. Force-revoke all active cloud session tokens via IdP API.
        3. Trigger critical ticket in SOAR / SIEM.
```

---

## ⏭️ Next Chapter
Proceed to [**08: Splunk SIEM Detection Engineering — Practical SPL Queries**](./08-splunk-detection.md) to inspect production-ready Splunk queries for hunting infostealer and session hijacking artifacts.
