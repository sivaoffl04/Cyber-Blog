# Chapter 08: Comprehensive MITRE ATT&CK Matrix Mapping

> **Seminar Module:** Threat Tactic Taxonomy & ATT&CK Framework Deconstruction  
> **Target Audience:** Threat Intelligence Analysts, SOC Engineers, Detection Engineers, Red/Purple Teams  
> **Framework:** MITRE ATT&CK Enterprise Framework (v14)

---

## 1. Enterprise Matrix Overview: The Identity-to-Hypervisor Path

The intrusion into MGM Resorts International spans 12 distinct MITRE ATT&CK tactics, demonstrating how an initial non-technical voice phishing lure seamlessly converted into cloud identity manipulation and low-level virtualization destruction.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                      MGM RESORTS MITRE ATT&CK PROGRESSION                        │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│   RECONNAISSANCE ──► INITIAL ACCESS ──► PERSISTENCE ──► PRIVILEGE ESCALATION     │
│   • T1593.001        • T1566.004        • T1484.002     • T1078.004              │
│   • T1589.001        • T1078.004        • T1098.001     • T1098                  │
│                                                                                  │
│           │                                                      │               │
│           ▼                                                      ▼               │
│                                                                                  │
│   DEFENSE EVASION ──► CREDENTIAL ACCESS ──► DISCOVERY ──► LATERAL MOVEMENT       │
│   • T1562.001         • T1556.006           • T1087.004   • T1021.004            │
│   • T1535             • T1528               • T1046       • T1021.001            │
│                                                                                  │
│           │                                                      │               │
│           ▼                                                      ▼               │
│                                                                                  │
│   COLLECTION ───────► EXFILTRATION ───────► IMPACT                               │
│   • T1530             • T1567.002           • T1486 (ESXi Encryption)            │
│   • T1005             • T1048               • T1489 (Service Stop)               │
│                                             • T1490 (Inhibit Recovery)           │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Exhaustive MITRE ATT&CK Mapping Table

| Tactic | Technique ID | Technique Name | Adversary Specific Action at MGM Resorts | Detection Data Sources |
| :--- | :--- | :--- | :--- | :--- |
| **Reconnaissance** | **T1593.001** | Search Open Websites: Social Media | Mined LinkedIn to profile identity engineers, systems administrators, and IT directors. | External Threat Intelligence / Brand Monitoring |
| **Reconnaissance** | **T1589.001** | Gather Victim Identity: Credentials / PII | Aggregated employee DOB, mobile numbers, and addresses via people-search databases. | Dark Web Monitoring / Commercial Data Brokers |
| **Initial Access** | **T1566.004** | Phishing: Voice Phishing (Vishing) | Impersonated internal employee over telephone to MGM IT Help Desk to request MFA reset. | PBX / Call Center Recordings / Telephony Audio |
| **Initial Access** | **T1078.004** | Valid Accounts: Cloud Accounts | Authenticated to Okta portal using legitimate username and newly enrolled factor. | Okta SystemLog: `user.session.start` |
| **Execution** | **T1059.001** | Command & Scripting: PowerShell | Executed Microsoft Graph PowerShell modules to query Azure AD directory assets. | Windows Event ID 4104 (ScriptBlock Logging) |
| **Execution** | **T1204.002** | User Execution: Malicious File | Manually executed ALPHV Linux ELF ransomware locker on target ESXi hypervisors. | ESXi Syslog / Host Audit Logs (`/var/log/shell.log`) |
| **Persistence** | **T1484.002** | Domain Trust Modification: SAML IdP | Created rogue Inbound SAML Identity Provider inside Okta to bypass future authentications. | Okta SystemLog: `system.idp.lifecycle.create` |
| **Persistence** | **T1098.001** | Account Manipulation: Additional Credentials | Registered rogue Azure AD enterprise applications and generated long-lived client secrets. | Azure AD Audit: `Add service principal credentials` |
| **Persistence** | **T1556.006** | Modify Auth Process: Multi-Factor Auth | Re-registered Okta Verify token to attacker-controlled iPhone via help desk bypass code. | Okta SystemLog: `user.mfa.factor.activate` |
| **Privilege Escalation** | **T1078.004** | Valid Accounts: Cloud Accounts | Inherited Okta Super Administrator and Azure AD Global Administrator privileges. | Okta SystemLog / Azure AD Audit Logs |
| **Defense Evasion** | **T1562.001** | Impair Defenses: Disable / Modify Tools | Terminated internal monitoring agents and attempted to disable audit log feeds. | Sysmon EID 1 / Auditd Logs |
| **Defense Evasion** | **T1535** | Unused / Unsupported Cloud Regions | Tunneled authentication requests through residential SOCKS5 proxies matching Las Vegas IP space. | Okta Risk Engine / ASN & Geo-IP Telemetry |
| **Credential Access** | **T1556** | Modify Authentication Process | Manipulated Okta factor enrollment policies to allow untrusted mobile authenticator apps. | Okta Policy Changes: `policy.rule.update` |
| **Credential Access** | **T1528** | Steal Application Access Token | Extracted OAuth 2.0 bearer tokens to interact directly with cloud infrastructure APIs. | Azure AD Sign-in Logs: `InteractiveUser` |
| **Discovery** | **T1087.004** | Account Discovery: Cloud Accounts | Enumerated all federated applications in Okta (vCenter, Azure, AWS, Workday). | Okta SystemLog: `app.generic.config.read` |
| **Discovery** | **T1046** | Network Service Discovery | Scanned internal management VLANs for listening vCenter (443) and ESXi SSH (22/902) ports. | Zeek / Bro Network Flow / Firewall Session Logs |
| **Lateral Movement** | **T1021.004** | Remote Services: SSH | Established direct SSH connections to VMware ESXi hypervisor hosts from compromised jump hosts. | ESXi `/var/log/auth.log` (sshd connections) |
| **Lateral Movement** | **T1021.001** | Remote Services: RDP | Moved laterally to on-premises Windows servers and Domain Controllers via RDP. | Windows Event ID 4624 (Type 10 RemoteInteractive) |
| **Collection** | **T1530** | Data from Cloud Storage Object | Harvested corporate documentation, architectural blueprints, and customer data from cloud storage. | AWS S3 / Azure Blob Storage Access Logs |
| **Exfiltration** | **T1567.002** | Exfiltration Over Web Service | Exfiltrated staging archives to external cloud hosting services (e.g., Mega, Rclone). | Network Flow / Next-Gen Firewall (Palo Alto / Fortinet) |
| **Impact** | **T1486** | Data Encrypted for Impact | Executed ALPHV Rust binary, encrypting `.vmdk`, `.vmx`, and `.vmsn` files across 100+ ESXi hosts. | ESXi VMkernel Logs / Storage SAN IOPS Spikes |
| **Impact** | **T1489** | Service Stop | Forcibly terminated virtual machine processes via `esxcli vm process kill` to release file locks. | ESXi `/var/log/hostd.log` & `/var/log/vmkernel.log` |
| **Impact** | **T1490** | Inhibit System Recovery | Deleted hypervisor snapshots and purged local datastore backup volumes. | ESXi Shell Logs (`rm -rf` execution on snapshots) |

---

## 3. Threat Actor Tradecraft Synthesis

The mapping above highlights three distinctive signatures of the **Scattered Spider / ALPHV campaign**:

### 1. Zero Traditional Exploit Binaries in Initial Phases
Notice that from Reconnaissance through Lateral Movement, **not a single CVE exploit or malware dropper was utilized**. The adversaries operated entirely "Living off the Identity" (LotI), executing legitimate administrative actions within vendor-provided user interfaces and management APIs.

### 2. Dual-Layer Identity Exploitation
The threat actors did not stop at Active Directory. They exploited the modern multi-cloud identity plane—specifically the trust relationships between Okta (Workforce Identity Cloud) and Azure AD (Microsoft Entra ID)—bypassing years of traditional on-premises perimeter defenses.

### 3. Hypervisor Extinction Event
By moving down to the hypervisor level (VMware ESXi), the attackers achieved maximum destructive impact with minimum operational effort. Rather than needing to fight 1,000 distinct endpoint EDR sensors across Windows and Linux VMs, they struck at the container that hosted them all.

---

## 4. Seminar Discussion Questions

1. **Mapping Living off the Identity:** How does your SOC currently track MITRE technique **T1078.004 (Valid Accounts)**, and why do traditional anomaly rules often generate excessive false positives when applied to system administrators?
2. **Detection Gaps on Hypervisors:** Reviewing techniques **T1486** and **T1489** on ESXi hosts, what automated mechanisms does your organization possess to detect when an ESXi host receives mass `esxcli vm process kill` commands?
