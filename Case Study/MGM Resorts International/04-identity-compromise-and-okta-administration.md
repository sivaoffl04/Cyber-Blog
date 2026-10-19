# Chapter 04: Identity Compromise & Okta Administration

> **Seminar Module:** Cloud Identity Hijacking, MFA Re-Enrollment & Federation Tampering  
> **Target Audience:** Identity Architects, Okta Administrators, Cloud Security Engineers, Threat Hunters  
> **Core Concepts:** Okta Super Admin, Inbound SAML Federation, Factor Re-Enrollment, Golden SAML Concepts

---

## 1. Phase 3: Identity Compromise and Factor Re-Enrollment

Following the successful help desk vishing call, the threat actor held the one-time activation token provided by the support agent. Within seconds, the attacker executed the factor registration workflow.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   MFA RE-ENROLLMENT & COMPROMISE SEQUENCE                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. Attacker navigates to: https://mgmresorts.okta.com/signin/register      │
│  2. Inputs compromised employee username and one-time enrollment token      │
│  3. Registers attacker hardware: Apple iPhone (Okta Verify Push / OTP)      │
│  4. Residential Proxy Routing: Traffic tunneled via Las Vegas ISP IP        │
│  5. Bypassing Impossible Travel heuristics & conditional access rules       │
│  6. Session Established: Active session authenticated with Super Admin role │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Evading Geolocation & Device Posture Checks
Modern Identity Providers utilize **Conditional Access Policies** and **Risk-Based Authentication** to detect anomalies, such as an employee logging in from an unfamiliar country or an untrusted operating system.

Scattered Spider routinely circumvents these detections using **Residential SOCKS5 Proxy Networks** (e.g., BrightData, IPRoyal, Oxylabs):
* The threat actor identified that the targeted systems engineer lived in the Las Vegas metropolitan area.
* The attacker configured their browser to route through a residential IP address assigned to a residential ISP (e.g., Cox Communications / CenturyLink) located in the same geographic radius.
* To the Okta Risk Engine, the login appeared as a legitimate local residential connection, scoring low on the anomaly risk scale.

```json
{
  "actor": {
    "id": "00u4x92m8aBCDEF12345",
    "type": "User",
    "alternateId": "systems.engineer@mgmresorts.com",
    "displayName": "Senior Systems Engineer"
  },
  "client": {
    "userAgent": {
      "rawUserAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
      "os": "Mac OS X",
      "browser": "CHROME"
    },
    "ipAddress": "70.168.14.92",
    "geographicalContext": {
      "city": "Las Vegas",
      "state": "Nevada",
      "country": "United States"
    }
  },
  "eventType": "user.mfa.factor.activate",
  "outcome": {
    "result": "SUCCESS"
  }
}
```

---

## 2. Phase 4: Okta Administration and SSO Enumeration

Once authenticated, the attacker did not land in a limited end-user dashboard; they landed in the **Okta Administrative Console** with **Super Administrator** privileges.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      OKTA SUPER ADMINISTRATOR PRIVILEGES                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│ • Full CRUD access across all user accounts, groups, and directory sync rules   │
│ • Complete visibility into all configured Single Sign-On (SSO) applications     │
│ • Ability to issue SAML assertions and OAuth bearer tokens for any service      │
│ • Ability to disable or bypass MFA requirements across entire security policies │
│ • Authority to modify identity provider trust relationships & certificates     │
│ • Direct administrative API token generation with unlimited tenant scope        │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Enumerating the Enterprise Application Catalog
In an integrated enterprise, Okta acts as the central authentication clearinghouse. By inspecting the Okta Application Catalog, the threat actors instantly enumerated the entire enterprise IT ecosystem without sending a single network packet to the internal corporate LAN:

```
                          OKTA SINGLE SIGN-ON ECOSYSTEM
                                        │
             ┌──────────────────────────┼──────────────────────────┐
             ▼                          ▼                          ▼
   [Cloud Infrastructure]       [Directory Services]      [Enterprise SaaS]
   • Microsoft Azure / Entra    • On-Prem Active Directory • ServiceNow ITSM
   • Amazon Web Services (AWS)  • LDAP / Kerberos Realms   • Workday HR Management
   • VMware vCenter Server      • Google Workspace Cloud   • Slack / Microsoft Teams
```

The attackers observed SAML integrations directly into:
1. **Microsoft Entra ID (Azure AD):** The primary identity directory governing corporate Office 365, SharePoint, and Azure cloud subscriptions.
2. **VMware vCenter SSO:** The administrative management platform governing hypervisor clusters and virtual machine datastores.
3. **Internal Ticketing & Knowledge Bases (ServiceNow / Confluence):** Providing architectural network diagrams, IP allocation sheets, and disaster recovery procedures.

---

## 3. Phase 5: Persistence and Identity Federation Tampering

An advanced adversary possessing administrative control over an identity provider does not rely solely on maintaining the single compromised account. If the legitimate engineer wakes up and notices unauthorized logins, the account will be locked. 

To guarantee permanent, resilient access, Scattered Spider executed **Identity Federation Tampering**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 INBOUND IDENTITY FEDERATION TAMPERING FLOW                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [MGM Okta Tenant] ◄──(Trusts SAML)──► [Attacker-Controlled IdP]           │
│         │                                        │                          │
│         ▼                                        ▼                          │
│  Issues token for:                     Generates arbitrary SAML             │
│  admin@mgmresorts.com                  assertions with spoofed claims       │
│         │                                        │                          │
│         └──────────────────┬─────────────────────┘                          │
│                            │                                                │
│                            ▼                                                │
│         [Unfettered Cloud & Directory Access]                               │
│         Bypasses local MFA, password resets, and account suspension         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Mechanism 1: Rogue Inbound SAML Identity Provider
In Okta, administrators can configure **Inbound SAML / OIDC Identity Providers**. This feature is designed to allow external partners or subsidiaries to authenticate using their own identity systems.

The threat actors configured a new, rogue Inbound Identity Provider linked to an external domain under their control:
* **The Vulnerability:** Any user authenticating through this rogue IdP could present SAML assertions claiming to be any user within the `@mgmresorts.com` domain.
* **The Consequence:** Even if MGM's SOC reset the original systems engineer's password, revoked their sessions, and cleared their MFA devices, the attackers could continue generating valid assertions from their external IdP.

### Mechanism 2: Azure AD Cross-Tenant Synchronization
Simultaneously, the threat actors leveraged their access to configure **Cross-Tenant Access Settings** and rogue OAuth enterprise applications inside Microsoft Entra ID (Azure AD):
* They registered a multi-tenant Azure application with high-privilege Microsoft Graph API permissions: `Directory.ReadWrite.All`, `RoleManagement.ReadWrite.Directory`.
* This enabled the attackers to query directory contents, create secondary Global Administrator accounts, and generate long-lived application client secrets.

---

## 4. Okta SystemLog Forensic Analysis: Critical Event Indicators

During post-incident forensic triage, the following telemetry markers in the Okta SystemLog revealed the unauthorized administrative hijacking:

| Event Type (`eventType`) | Target / Context | Forensic Significance | Severity |
| :--- | :--- | :--- | :--- |
| `user.mfa.factor.deactivate` | IT Help Desk agent deactivates Okta Verify for Systems Engineer | Initial factor clearing resulting from the successful vishing call. | **High** |
| `user.mfa.factor.activate` | Attacker registers new iPhone from residential proxy IP | New authenticator device enrolled; IP location mismatch. | **Critical** |
| `user.session.start` | New administrative session initiated | Session authenticated with newly registered factor. | **High** |
| `user.account.privilege.grant` | Super Admin role assigned or verified | Administrative validation within console. | **Critical** |
| `system.idp.lifecycle.create` | New Inbound SAML Identity Provider created | **Persistence Mechanism:** Creation of rogue external federation trust. | **Fatal** |
| `application.lifecycle.create` | New SAML application or API token generated | Backdoor API token created with unlimited validity. | **Critical** |

---

## 5. Architectural Failure: Lack of Blast-Radius Containment

The compromise of MGM's Okta tenant illustrated a dangerous design flaw common across modern enterprises: **Identity Monoliths**.

```
                HIGH RISK: SINGLE IDENTITY MONOLITH
                ┌──────────────────────────────────┐
                │        Single Okta Tenant        │
                │     (Super Admin Controls All)   │
                └─────────────────┬────────────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
  [Corporate Office]      [Cloud Workloads]        [Critical Operations]
  • Email & Slack         • Azure / AWS Subnets    • Casino Slot Systems
  • HR & Payroll          • Production Databases   • Hotel Key Locks & PMS
```

When a single identity provider governs both mundane corporate communications (Slack, Workday) and mission-critical physical operations (casino floors, hotel door locks, hypervisors), a single identity compromise guarantees complete operational catastrophe.

---

## 6. Seminar Discussion Questions

1. **The Golden SAML Threat:** How does an identity architect detect when a federated SAML assertion contains forged claims if the underlying signing certificate has been compromised or untrusted IdPs are authorized?
2. **Privileged Identity Separation:** Why should production hypervisors (ESXi/vCenter) and physical access control systems NEVER be federated to the same identity provider used for corporate email and employee laptops?
