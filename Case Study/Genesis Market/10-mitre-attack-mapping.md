# 🗺️ 10: Comprehensive MITRE ATT&CK Matrix Mapping

![Genesis Architecture](./images/genesis_market_architecture.jpg)

> **Framework:** MITRE ATT&CK® Enterprise Matrix (v14)  
> **Threat Model:** Infostealer Infection ➔ Genesis Market Brokerage ➔ Downstream Enterprise Compromise  
> **Covered Tactics:** 11 Tactics, 24 Techniques and Sub-techniques  

---

## 🧭 1. Enterprise Matrix Navigation

The Genesis Market attack chain does not exist in isolation. It spans three interconnected operational domains:
1. **The Infostealer Endpoint Infection** (Pre-Market)
2. **The Genesis Marketplace Identity Packaging** (Market Brokerage)
3. **The Downstream Enterprise Intrusion** (Post-Market Adversary Action)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    GENESIS COMPROMISE ATT&CK KILL CHAIN                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   [INITIAL ACCESS]      T1189 (Drive-by Malvertising) / T1566 (Phishing)        │
│          │                                                                      │
│          ▼                                                                      │
│   [EXECUTION]           T1204.002 (Malicious File) / T1059 (Scripting)          │
│          │                                                                      │
│          ▼                                                                      │
│   [DEFENSE EVASION]     T1027 (Obfuscation) / T1562.001 (Disable Antivirus)     │
│          │                                                                      │
│          ▼                                                                      │
│   [CREDENTIAL ACCESS]   T1539 (Steal Web Session Cookie)                        │
│                         T1555.003 (Credentials from Web Browsers)               │
│          │                                                                      │
│          ▼                                                                      │
│   [COLLECTION]          T1005 (Data from Local System) / T1113 (Screen Capture) │
│          │                                                                      │
│          ▼                                                                      │
│   [EXFILTRATION / C2]   T1071.001 (Web Protocols) ➔ Upload to Genesis C2       │
│          │                                                                      │
│          ▼                                                                      │
│   [DOWNSTREAM INTRUSION]T1078.004 (Valid Accounts: Cloud Replay via Genesis OS) │
│                         T1105 (Ingress Tool Transfer / Ransomware Deployment)   │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 2. Detailed Technique Breakdown

| Tactic | Technique ID | Technique Name | Operational Evidence & Tradecraft in Genesis Chain |
|---|---|---|---|
| **Initial Access** | **T1189** | Drive-by Compromise | Malvertising campaigns abusing Google Ads to deliver infostealers disguised as OBS Studio, Notepad++, or game cracks. |
| **Initial Access** | **T1566.001** | Spearphishing Attachment | Delivery of ISO, LNK, or weaponized ZIP attachments containing stealer loaders. |
| **Execution** | **T1204.002** | User Execution: Malicious File | Victim duped into running malicious executable disguised as installer. |
| **Execution** | **T1059.001** | PowerShell | Infostealer stagers invoking PowerShell download cradles with `-ExecutionPolicy bypass`. |
| **Persistence** | **T1547.001** | Registry Run Keys / Startup Folder | Adding persistence entries under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`. |
| **Persistence** | **T1053.005** | Scheduled Task | Creating hidden tasks in `TaskScheduler` to maintain periodic cookie harvesting. |
| **Defense Evasion** | **T1036.005** | Masquerading: Match Legitimate Name | Naming stealer processes `svchost.exe`, `RuntimeBroker.exe`, or `chrome_update.exe`. |
| **Defense Evasion** | **T1027** | Obfuscated Files or Information | Packing payload with Themida, VMProtect, or multi-stage XOR loaders to evade static AV. |
| **Defense Evasion** | **T1562.001** | Impair Defenses: Disable Tools | Adding folder exclusions in Windows Defender via `Add-MpPreference -ExclusionPath`. |
| **Credential Access** | **T1539** | Steal Web Session Cookie | Decrypting `Network\Cookies` SQLite database to harvest authenticated session cookies. |
| **Credential Access** | **T1555.003** | Credentials from Web Browsers | Calling `CryptUnprotectData` to decrypt passwords stored in Chromium `Login Data`. |
| **Credential Access** | **T1552.001** | Credentials in Files | Searching `%USERPROFILE%` for `wallet.dat`, `*.ovpn`, `recentservers.xml`, `.aws/credentials`. |
| **Discovery** | **T1082** | System Information Discovery | Querying WMI and registry for OS version, CPU, GPU, installed RAM, and screen resolution. |
| **Discovery** | **T1083** | File and Directory Discovery | Enumerating installed browser profiles in `%LOCALAPPDATA%` and `%APPDATA%`. |
| **Discovery** | **T1057** | Process Discovery | Enumerating running processes to detect analysis sandboxes, Wireshark, Process Hacker. |
| **Collection** | **T1005** | Data from Local System | Staging collected credentials, autofill, and tokens into `%TEMP%\<random_dir>\`. |
| **Collection** | **T1113** | Screen Capture | Executing GDI API calls (`BitBlt`) to capture full desktop screenshot at infection. |
| **Collection** | **T1115** | Clipboard Data | Monitoring clipboard for cryptocurrency wallet addresses (clipper trojan behavior). |
| **Command & Control** | **T1071.001** | Web Protocols: HTTP/HTTPS | Exfiltrating compressed stolen logs to C2 server via standard HTTP POST requests. |
| **Command & Control** | **T1573.001** | Symmetric Encryption | Encrypting exfiltrated archives using hardcoded AES or RC4 keys before upload. |
| **Initial Access (Buyer)** | **T1078.004** | Valid Accounts: Cloud Accounts | Criminal buyer importing bot cookies into Genesis OS to access corporate cloud apps without MFA. |
| **Lateral Movement** | **T1021.002** | Remote Services: SMB/Windows Admin Shares | Replaying recovered credentials across internal enterprise network shares. |
| **Impact** | **T1486** | Data Encrypted for Impact | Downstream ransomware affiliates encrypting enterprise storage systems after gaining access via bot. |
| **Impact** | **T1657** | Financial Theft | Draining cryptocurrency wallets and executing wire fraud using stolen banking sessions. |

---

## ⏭️ Next Chapter
Proceed to [**11: Lessons Learned — Strategic & Tactical Recommendations**](./11-lessons-learned.md) for CISO-level architectural takeaways and defensive engineering recommendations.
