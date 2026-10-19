# Chapter 10: SIEM Detection Engineering — Splunk & Sigma

> **Seminar Module:** Technical Telemetry Correlation, Detection Engineering & Hunting Rules  
> **Target Audience:** Detection Engineers, SIEM Content Developers, SOC Analysts, Purple Teams  
> **Languages & Formats:** Splunk Search Processing Language (SPL) & Sigma Detection Format (YAML)

---

## 1. Detection Engineering Principles for Identity-Driven Ransomware

To catch attacks like the MGM Resorts compromise, detection rules must transition from static file hash matching to **behavioral event sequence correlation** across the identity and virtualization planes.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                     CROSS-PLANE DETECTION TIMELINE LOGIC                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   [LOG SOURCE 1: OKTA SYSTEMLOG]                                                │
│   Event: `user.mfa.factor.deactivate` (Actor = Help Desk Agent)                 │
│                                  │                                              │
│                                  ▼ [Window: < 15 Minutes]                       │
│   [LOG SOURCE 1: OKTA SYSTEMLOG]                                                │
│   Event: `user.mfa.factor.activate` (Target = High-Privilege Account)           │
│   Anomaly: Client IP ASN != Corporate Network AND Geo != Historical Baseline   │
│                                  │                                              │
│                                  ▼ [Window: < 60 Minutes]                       │
│   [LOG SOURCE 2: AZURE AD AUDIT]                                                │
│   Event: `Add service principal` OR `Add member to role: Global Administrator`  │
│                                  │                                              │
│                                  ▼ [Window: < 120 Minutes]                      │
│   [LOG SOURCE 3: ESXi SYSLOG]                                                   │
│   Event: Direct SSH Login to Host + Burst of `esxcli vm process kill`           │
│                                  │                                              │
│                                  ▼                                              │
│            [CORRELATED ALERT: FULL IDENTITY-TO-RANSOMWARE BREACH]               │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Production Splunk SPL Queries

### Rule 1: Okta Privileged Factor Reset and Rapid Activation Anomaly
Detects when an MFA factor is deactivated by support staff and a new factor is registered for the same user within 15 minutes from an untrusted or newly observed IP address.

```spl
index=okta sourcetype="Okta:SystemLog" (eventType="user.mfa.factor.deactivate" OR eventType="user.mfa.factor.activate")
| eval user=lower('target{}.alternateId')
| eval actor_user=lower('actor.alternateId')
| eval client_ip='client.ipAddress'
| eval event_time=_time
| stats earliest(eval(if(eventType=="user.mfa.factor.deactivate", event_time, null()))) as deactivate_time,
        earliest(eval(if(eventType=="user.mfa.factor.deactivate", actor_user, null()))) as deactivating_agent,
        latest(eval(if(eventType=="user.mfa.factor.activate", event_time, null()))) as activate_time,
        latest(eval(if(eventType=="user.mfa.factor.activate", client_ip, null()))) as activating_ip,
        latest(eval(if(eventType=="user.mfa.factor.activate", 'client.geographicalContext.city', null()))) as activating_city
        by user
| eval time_delta_sec = activate_time - deactivate_time
| where isnotnull(deactivate_time) AND isnotnull(activate_time) AND time_delta_sec > 0 AND time_delta_sec < 900
| lookup privileged_users_lookup user OUTPUT is_privileged, department
| where is_privileged=="true"
| table user, department, deactivating_agent, activating_ip, activating_city, time_delta_sec
```

---

### Rule 2: Okta Inbound SAML Identity Provider Creation
Alerts immediately whenever a new external Identity Provider trust is created or modified. Inbound federation changes should occur exclusively during scheduled maintenance windows.

```spl
index=okta sourcetype="Okta:SystemLog" eventType IN ("system.idp.lifecycle.create", "system.idp.lifecycle.update")
| eval admin_user='actor.alternateId'
| eval idp_name='target{}.displayName'
| eval idp_type='target{}.type'
| eval client_ip='client.ipAddress'
| eval user_agent='client.userAgent.rawUserAgent'
| table _time, admin_user, idp_name, idp_type, client_ip, user_agent
```

---

### Rule 3: Microsoft Entra ID (Azure AD) High-Privilege Application Credential Creation
Detects the addition of secret keys or certificates to high-privilege Azure AD Service Principals, a common Scattered Spider persistence vector.

```spl
index=azure sourcetype="azure:aad:audit" operationName="Add service principal credentials"
| eval initiated_by=coalesce('initiatedBy.user.userPrincipalName', 'initiatedBy.app.displayName')
| eval target_app='targetResources{}.displayName'
| eval key_type=spath(properties, "KeyDescription")
| search initiated_by!="*AutomationAccount*"
| table _time, initiated_by, target_app, result, key_type
```

---

### Rule 4: VMware ESXi Mass Virtual Machine Process Termination
Identifies bursts of virtual machine termination commands across ESXi hypervisor hosts within a 2-minute sliding window.

```spl
index=esxi sourcetype="vmware:esxlog:syslog" ("esxcli vm process kill" OR "vim-cmd vmsvc/power.off" OR "Terminating virtual machine")
| rex field=_raw "WorldID=(?<world_id>\d+)"
| rex field=_raw "VM: (?<vm_name>[^\s,]+)"
| bin _time span=2m
| stats count as kill_count, values(vm_name) as terminated_vms by _time, host
| where kill_count >= 5
| eval alert_severity=if(kill_count >= 20, "CRITICAL", "HIGH")
| table _time, host, kill_count, alert_severity, terminated_vms
```

---

## 3. Production Sigma Rules (YAML)

### Sigma Rule 1: Suspicious Privileged Okta Factor Reset
```yaml
title: Okta Suspicious Privileged MFA Factor Reset and Re-Enrollment
id: 4b29a102-7c81-42e9-89a1-0d3f8472bfa0
status: production
description: Detects a rapid deactivation and re-activation of an authentication factor on a high-privilege account.
author: Cyber-Blog Detection Engineering Team
references:
    - https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
tags:
    - attack.initial_access
    - attack.t1566.004
    - attack.persistence
    - attack.t1556.006
logsource:
    product: okta
    service: okta
detection:
    selection_deactivate:
        eventType: 'user.mfa.factor.deactivate'
        outcome.result: 'SUCCESS'
    selection_activate:
        eventType: 'user.mfa.factor.activate'
        outcome.result: 'SUCCESS'
    privileged_accounts:
        target.alternateId|contains:
            - 'admin'
            - 'engineer'
            - 'architect'
            - 'director'
    timeframe: 15m
    condition: selection_deactivate and selection_activate and privileged_accounts
fields:
    - actor.alternateId
    - target.alternateId
    - client.ipAddress
    - client.geographicalContext.city
falsepositives:
    - Legitimate verified phone replacement executed with scheduled help desk ticket.
level: high
```

---

### Sigma Rule 2: Inbound Identity Provider Creation in Okta
```yaml
title: Creation of Inbound Identity Provider in Okta
id: 9a74c184-e35b-4328-879e-4b6819a8204e
status: production
description: Detects the creation of an inbound SAML or OIDC Identity Provider in Okta, which can be leveraged for persistence or Golden SAML attacks.
author: Cyber-Blog Detection Engineering Team
references:
    - https://sec.okta.com/articles/2023/08/cross-tenant-impersonation
tags:
    - attack.persistence
    - attack.t1484.002
logsource:
    product: okta
    service: okta
detection:
    selection:
        eventType:
            - 'system.idp.lifecycle.create'
            - 'system.idp.lifecycle.update'
    condition: selection
fields:
    - actor.alternateId
    - target.displayName
    - target.type
    - client.ipAddress
falsepositives:
    - Legitimate corporate M&A or business partner B2B federation change during planned change window.
level: critical
```

---

### Sigma Rule 3: ESXi Hypervisor Mass Virtual Machine Termination
```yaml
title: VMware ESXi Mass Virtual Machine Force Kill
id: c7189f21-0e42-4981-b472-88147d391f5a
status: production
description: Detects command-line invocation of esxcli or vim-cmd to forcibly terminate virtual machine processes, characteristic of ALPHV/BlackCat ransomware.
author: Cyber-Blog Detection Engineering Team
references:
    - https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware
tags:
    - attack.impact
    - attack.t1489
    - attack.t1486
logsource:
    product: vmware
    service: esxi
detection:
    selection:
        message|contains:
            - 'esxcli vm process kill'
            - 'vim-cmd vmsvc/power.off'
            - 'poweroff-force'
    condition: selection
fields:
    - host
    - message
falsepositives:
    - Emergency hypervisor maintenance script executed by authorized virtualization engineers.
level: critical
```

---

## 4. Testing and Validation Instructions

To validate these rules in a lab environment:
1. **Okta Telemetry Ingestion:** Ensure that the **Okta Add-on for Splunk** (`Splunk_TA_okta`) is installed and actively polling the Okta Events API (`/api/v1/logs`).
2. **ESXi Syslog Forwarding:** Ensure all ESXi hypervisors forward `/var/log/syslog.log` and `/var/log/shell.log` to the centralized SIEM forwarder over TLS port 6514.
3. **Lookup Tables:** Populate the `privileged_users_lookup.csv` table with all corporate executives, domain administrators, and cloud engineers to enable dynamic severity escalation.
