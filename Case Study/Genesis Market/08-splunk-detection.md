# 📊 08: Splunk SIEM Detection Engineering — Practical SPL Queries

![Genesis Detection Blueprint](./images/genesis_market_banner.jpg)

> **SIEM Platform:** Splunk Enterprise / Splunk Cloud / Splunk Enterprise Security (ES)  
> **Target Data Models:** Authentication, Endpoint.Processes, Endpoint.Filesystem, Change_Analysis  
> **Key Protocols:** Sysmon EID 1 & 11, Okta SystemLog, Microsoft Entra ID Sign-in Logs  
> **Methodology:** Risk-Based Alerting (RBA) & Multi-Source Cross-Telemetry Correlation  

---

## 🎯 1. Engineering Real-World Splunk Detections

Detecting Genesis-style identity theft in a SIEM cannot rely on simple, static keyword alerts. Adversaries using Genesis bot profiles deliberately present valid authentication cookies, correct usernames, and replicated browser fingerprints.

Defenders must use **behavioral baselining, stateful correlation, and velocity calculations** in Search Processing Language (SPL).

The following production-ready queries provide detection engineering teams with battle-tested search logic.

---

## 🔍 Query 1: Impossible Travel & Geolocation Velocity Anomaly
**Objective:** Detect instances where a user account initiates cloud logins from two distant geographic locations within a time window that makes physical travel impossible.

```spl
index=azure_ad_signin OR index=okta sourcetype IN ("azure:aad:signin", "OktaIM2:log")
| eval user=lower(coalesce(userPrincipalName, actor.alternateId))
| eval ip=coalesce(ipAddress, client.ipAddress)
| iplocation ip
| search Country!="" City!=""
| sort 0 user _time
| streamstats current=f window=1 
    last(lat) as prev_lat 
    last(lon) as prev_lon 
    last(_time) as prev_time 
    last(City) as prev_city 
    last(Country) as prev_country 
    last(ip) as prev_ip 
    by user
| eval time_diff_hours = (_time - prev_time) / 3600
| where time_diff_hours > 0 AND time_diff_hours < 4
| eval distance_km = round(2 * 6371 * asin(sqrt(
    pow(sin((lat - prev_lat) * pi() / 360), 2) +
    cos(prev_lat * pi() / 180) * cos(lat * pi() / 180) *
    pow(sin((lon - prev_lon) * pi() / 360), 2)
  )), 2)
| eval velocity_kmh = round(distance_km / time_diff_hours, 2)
| where velocity_kmh > 800 AND distance_km > 300
| table _time user prev_ip prev_city prev_country ip City Country distance_km time_diff_hours velocity_kmh
| sort - velocity_kmh
```

**Analyst Triage Tip:**
A velocity exceeding 800 km/h with different source IP blocks strongly indicates either an active session token replay via a commercial proxy or concurrent use of a compromised account.

---

## 🔍 Query 2: Non-Browser Process Accessing Browser Vaults
**Objective:** Detect any non-browser executable querying or copying Google Chrome, Microsoft Edge, or Mozilla Firefox cookie/password SQLite databases on Windows endpoints.

```spl
index=windows sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=11
| eval TargetFile=lower(TargetFilename)
| eval Process=lower(Image)
| search TargetFile IN (
    "*\\google\\chrome\\user data\\default\\network\\cookies*",
    "*\\google\\chrome\\user data\\default\\login data*",
    "*\\microsoft\\edge\\user data\\default\\network\\cookies*",
    "*\\microsoft\\edge\\user data\\default\\login data*",
    "*\\mozilla\\firefox\\profiles\\*\\cookies.sqlite*",
    "*\\mozilla\\firefox\\profiles\\*\\key4.db*"
  )
| search NOT Process IN (
    "*\\chrome.exe",
    "*\\msedge.exe",
    "*\\firefox.exe",
    "*\\brave.exe",
    "*\\opera.exe"
  )
| stats count earliest(_time) as first_seen latest(_time) as last_seen 
    by host user Process TargetFile CommandLine
| convert ctime(first_seen) ctime(last_seen)
| sort - count
```

**Severity:** `CRITICAL` — High-fidelity indicator of infostealer execution (RedLine, Vidar, Raccoon). Immediate endpoint isolation recommended.

---

## 🔍 Query 3: Infostealer Staging Artifacts in User Directories
**Objective:** Identify the moment an infostealer writes harvested credentials, autofill dumps, or exfiltration archives to temporary file paths.

```spl
index=windows sourcetype="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=11
| eval Target=lower(TargetFilename)
| search Target IN (
    "c:\\users\\*\\appdata\\local\\temp\\*cookies.txt",
    "c:\\users\\*\\appdata\\local\\temp\\*passwords.txt",
    "c:\\users\\*\\appdata\\local\\temp\\*autofill.txt",
    "c:\\users\\*\\appdata\\local\\temp\\*system_info.txt",
    "c:\\users\\*\\appdata\\local\\temp\\*wallets.txt",
    "c:\\users\\*\\appdata\\roaming\\*cookies.txt",
    "c:\\programdata\\*passwords.txt"
  )
  OR (Target LIKE "c:\\users\\%\\appdata\\local\\temp\\%.zip" AND Target LIKE "%log%")
| stats values(TargetFilename) as created_files count by host user Image CommandLine
```

---

## 🔍 Query 4: Session Hijacking Detection via User-Agent & JA4 Shift
**Objective:** Detect an existing, authenticated cloud session where the client User-Agent or TLS JA4 fingerprint suddenly changes while retaining the same session identifier.

```spl
index=cloud_auth (sourcetype="aws:cloudtrail" OR sourcetype="okta:log")
| eval session_id = coalesce(sessionId, authenticationContext.externalSessionId)
| search session_id!=""
| stats dc(userAgent) as distinct_ua 
        values(userAgent) as observed_uas 
        dc(src_ip) as distinct_ips 
        values(src_ip) as observed_ips 
        earliest(_time) as session_start 
        latest(_time) as session_end 
        by user session_id
| where distinct_ua > 1 OR distinct_ips > 2
| eval duration_minutes = round((session_end - session_start) / 60, 2)
| table session_id user distinct_ua distinct_ips duration_minutes observed_uas observed_ips
| sort - distinct_ua
```

---

## 🔍 Query 5: High-Privilege Action in Un-Challenged Session
**Objective:** Identify high-risk corporate actions (e.g., adding a new MFA device, creating an OAuth app, creating an admin account) executed in a session that was authenticated solely via session cookie without a recent MFA prompt.

```spl
index=okta sourcetype="OktaIM2:log"
| search eventType IN (
    "user.mfa.factor.update", 
    "user.account.privilege.grant", 
    "app.oauth2.as.client.create", 
    "policy.rule.modify"
  )
| eval actor_user = lower(actor.alternateId)
| eval event_time = _time
| join type=left actor_user [
    search index=okta sourcetype="OktaIM2:log" eventType="user.authentication.verify"
    | eval actor_user = lower(actor.alternateId)
    | stats latest(_time) as last_mfa_time by actor_user
]
| eval mfa_lag_hours = (event_time - last_mfa_time) / 3600
| where isnull(last_mfa_time) OR mfa_lag_hours > 8
| table _time actor_user eventType client.ipAddress client.geographicalContext.city mfa_lag_hours
| sort - mfa_lag_hours
```

---

## 🏗️ 2. Splunk Risk-Based Alerting (RBA) Framework

Rather than generating noisy standalone alerts that cause alert fatigue, configure these SPL queries to increment a composite **Risk Score** assigned to both the user and the endpoint:

```
[Infostealer Process Accessing Cookie SQLite]  --> +60 Risk Score on Host
[Temp Folder Staging cookies.txt]              --> +40 Risk Score on Host
                                              ─────────────────────────
                                              = 100 Risk Score ➔ Automated EDR Containment

[Session Access from New ASN/Proxy]            --> +30 Risk Score on Identity
[Impossible Travel (>800 km/h)]                --> +50 Risk Score on Identity
[Mid-Session User-Agent Shift]                 --> +40 Risk Score on Identity
                                              ─────────────────────────
                                              = 120 Risk Score ➔ Automated Session Token Revocation
```

---

## ⏭️ Next Chapter
Proceed to [**09: Incident Response Playbook — Infostealer Infection & Session Revocation**](./09-incident-response.md) to review step-by-step containment procedures.
