# Chapter 09: Blue Team & SOC Detection Playbooks

> **Seminar Module:** Operational SOC Incident Handling & Identity Threat Detection (ITDR)  
> **Target Audience:** SOC Managers, Tier 2/3 Security Analysts, Incident Handlers, Threat Hunters  
> **Playbooks Included:** 1. Help Desk Impersonation | 2. Identity Provider Tampering | 3. ESXi Hypervisor Ransomware

---

## 1. The Modern Paradigm: Identity Threat Detection & Response (ITDR)

Traditional Security Operations Centers (SOCs) are heavily optimized to detect malicious executables on Windows endpoints. When an adversary operates entirely within legitimate administrative cloud portals using valid credentials, traditional EDR sensors remain silent.

To counter threat actors like Scattered Spider, modern Blue Teams must implement **Identity Threat Detection & Response (ITDR)**, treating identity lifecycle modifications with the same critical urgency historically reserved for kernel memory exploits.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      ITDR DETECTION CORRELATION ENGINE                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   [Help Desk Ticket: MFA Reset] ──► [Okta Factor Deactivated]                   │
│                                                │                                │
│                                                ▼                                │
│   [Time Delta < 10 Minutes] ──────► [New Device Enrolled from Residential IP]   │
│                                                │                                │
│                                                ▼                                │
│   [High-Privilege Role Check] ────► [User Has Super Admin / Global Admin Role]  │
│                                                │                                │
│                                                ▼                                │
│                           [AUTOMATED SEVERITY 1 CRITICAL ALERT]                 │
│                           • Automatically suspend account                       │
│                           • Terminate active Okta sessions                      │
│                           • Page On-Call Incident Commander                     │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. SOC Playbook 1: Detecting Help Desk Impersonation & Vishing

### Objective
Identify unauthorized MFA resets and account takeovers initiated through the IT service desk prior to adversary lateral movement.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│               PLAYBOOK 1: HELP DESK IMPERSONATION TRIAGE                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [TRIGGER]                                                                  │
│  • Okta event: `user.mfa.factor.deactivate` initiated by Service Desk agent.│
│  • Followed by `user.mfa.factor.activate` within 15 minutes.                │
│                                                                             │
│  [TRIAGE CHECKLIST]                                                         │
│  1. Check User Privilege Level:                                             │
│     Is the target user a member of "Okta Super Admins", "Domain Admins",    │
│     or "Cloud Infrastructure Leads"? If YES ➔ INSTANT ESCALATION.           │
│  2. Verify Ticket ID Cross-Reference:                                       │
│     Does the ServiceNow / Jira Service Desk ticket have an approved         │
│     manager signature attached?                                             │
│  3. Verify Authentication IP Context:                                       │
│     Compare newly registered device IP ASN with target user's 90-day        │
│     historical login baseline. Is the IP a known VPN or residential proxy?  │
│  4. Execute Out-of-Band (OOB) Voice/Video Verification:                     │
│     Immediately call the employee's pre-registered corporate cellular phone │
│     or initiate a live Microsoft Teams / Slack video call.                  │
│                                                                             │
│  [CONTAINMENT ACTIONS]                                                      │
│  • IF verification fails or cannot be confirmed within 5 minutes:           │
│    1. Execute API call: Suspend user account in Okta.                       │
│    2. Revoke all active Okta and Azure AD session tokens.                   │
│    3. Reset on-premises Active Directory password and disable Kerberos TGT. │
│    4. Notify enterprise Incident Response Team for host triage.             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. SOC Playbook 2: Detecting Identity Provider (Okta / Entra) Tampering

### Objective
Detect unauthorized modifications to identity federation trust relationships, rogue SAML Identity Providers, and rogue enterprise OAuth application registrations.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│               PLAYBOOK 2: IDENTITY FEDERATION TAMPERING                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [TRIGGER]                                                                  │
│  • Okta SystemLog: `system.idp.lifecycle.create` or `system.idp.update`     │
│  • Azure AD Audit: `Add service principal` or `Consent to application` with  │
│    high-risk scopes (`Directory.ReadWrite.All`, `RoleManagement.ReadWrite`) │
│                                                                             │
│  [TRIAGE CHECKLIST]                                                         │
│  1. Check Change Management Authorization:                                   │
│     Is there an approved, active Emergency Change Ticket (RFC) for adding   │
│     an external Identity Provider or enterprise application?                │
│  2. Inspect Inbound Federation Metadata:                                    │
│     What is the Issuer URL and Signing Certificate domain of the newly     │
│     added IdP? Does the domain resolve to an external, untrusted registrar? │
│  3. Analyze Actor Session History:                                          │
│     Trace the session ID of the administrator who executed the change.      │
│     Were there recent factor modifications on that admin account?           │
│                                                                             │
│  [CONTAINMENT ACTIONS]                                                      │
│  • IF unauthorized IdP creation is confirmed:                               │
│    1. IMMEDIATELY DELETE or DEACTIVATE the rogue Identity Provider in Okta. │
│    2. Revoke all application credentials and client secrets in Azure AD.    │
│    3. Invalidate all active SAML assertions and OAuth refresh tokens.       │
│    4. Place entire tenant in "High-Security Lockdown" (Enforce FIDO2-only). │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. SOC Playbook 3: Detecting ESXi Ransomware & Hypervisor Mass Termination

### Objective
Identify mass virtual machine process termination, unauthorized SSH logins, and cryptographic file system modification across VMware ESXi hypervisor clusters.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│               PLAYBOOK 3: ESXi HYPERVISOR RANSOMWARE HUNT                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [TRIGGER]                                                                  │
│  • Burst of VM shutdown events (>5 VMs powered off within 60 seconds).      │
│  • ESXi host syslog: SSH service enabled or root SSH login from non-jump IP.│
│  • Storage SAN/NFS Alert: Massive spike in write IOPS accompanied by        │
│    abnormal metadata renaming across `/vmfs/volumes/`.                      │
│                                                                             │
│  [TRIAGE CHECKLIST]                                                         │
│  1. Check vCenter Task Console:                                             │
│     Were VMs terminated via legitimate vCenter UI or direct host commands   │
│     (`esxcli vm process kill` / `power.off`)?                               │
│  2. Inspect Active SSH Sessions on ESXi Hosts:                              │
│     Execute command via console: `# esxcli network ip connection list`      │
│     Check for remote connections on port 22.                                │
│  3. Check Datastore Directory Contents:                                     │
│     Check for files matching: `README.txt`, `*.lockbit`, `*.alphv`, `*.crypted`│
│                                                                             │
│  [EMERGENCY CONTAINMENT ACTIONS]                                            │
│  • IF malicious hypervisor activity is detected:                            │
│    1. EMERGENCY ISOLATION: Sever the ESXi Management VLAN at the core switch│
│       to stop lateral SSH propagation across the cluster.                   │
│    2. FREEZE STORAGE ARRAYS: Issue immediate API commands to NetApp/SAN     │
│       storage arrays to convert all datastore volumes to READ-ONLY.         │
│    3. SNAPSHOT PRESERVATION: Lock existing hardware-level SAN snapshots.    │
│    4. DO NOT REBOOT HOSTS: Preserve volatile RAM for forensic key recovery. │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Threat Hunting Matrix: High-Value Telemetry Sources

| Environment | Telemetry Source | Hunting Query / Indicator | Target Artifact |
| :--- | :--- | :--- | :--- |
| **Okta Cloud** | Okta SystemLog | `eventType eq "user.mfa.factor.deactivate"` AND `outcome.result eq "SUCCESS"` | Help desk agent clearing MFA factor |
| **Okta Cloud** | Okta SystemLog | `eventType eq "system.idp.lifecycle.create"` | Rogue SAML IdP persistence |
| **Microsoft Entra** | Azure AD Audit | `OperationName eq "Add service principal credentials"` | Backdoored OAuth service principal |
| **Microsoft Entra** | Azure AD Sign-in | `RiskState eq "atRisk"` AND `AppDisplayName eq "Azure Portal"` | Risky sign-in by global administrator |
| **VMware ESXi** | `/var/log/shell.log` | `esxcli vm process kill` OR `kill -9` | Forcible termination of VM processes |
| **VMware ESXi** | `/var/log/auth.log` | `Accepted keyboard-interactive/pam for root` | Direct root SSH login to hypervisor |
| **Storage Area Net** | SAN Syslog | `IOPS > 50000` AND `Write_Ratio > 95%` | High-throughput ransomware encryption |

---

## 6. Seminar Discussion Questions

1. **Automation vs. Human Review:** If an automated SOC playbook detects an Okta Super Admin re-enrolling MFA from a residential proxy, should the SOAR platform immediately lock the account automatically, even if it risks interrupting an active executive?
2. **Hypervisor Isolation Speed:** In an attack where 100 ESXi hosts are being encrypted simultaneously by an automated script, why is manual analyst intervention always too late, and what automated containment gates are necessary?
