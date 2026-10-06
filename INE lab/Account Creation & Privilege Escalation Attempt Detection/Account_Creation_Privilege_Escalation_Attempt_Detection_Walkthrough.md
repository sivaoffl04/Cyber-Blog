# ⚔️ Account Creation & Privilege Escalation Attempt Detection — Complete SOC Walkthrough

![Account Creation & Privilege Escalation Banner](./images/account_privesc_banner.jpg)

> **Lab Platform:** [INE Security](https://my.ine.com/course/soc-ticketing-reporting/7f70e83f-52fe-4234-a19d-e4acb30c5c43/lab/7ceb853d-64ab-47e9-8c41-187ba835bd32)  
> **Course:** SOC Ticketing & Reporting  
> **Role:** SOC Level 1 Incident Analyst (Organization: *Syntrix*)  
> **Investigation Date:** **24th December 2025**  
> **Target Endpoint (Agent 002):** `ip-10-0-0-100` (`10.0.0.100` - Internal Linux Production Host)  
> **Attacker Ingress / Source IP:** `10.0.0.11`  
> **Rogue Identity Created:** `eviluser` (Local Account)  
> **Critical File Targeted:** `/etc/sudoers` (System Sudo Privilege Table)  
> **Key Tools:** Mozilla Firefox, **Wazuh SIEM v4.x** (`https://wazuh.ine.local`), **TheHive Platform** (`http://localhost:9000`)  
> **Status:** 🟢 **100% Solved — True Positive Multi-Stage Compromise Verified, 4 Observables Registered, 4 MITRE TTPs Associated, & Formally Escalated to SOC L2**

---

## 📑 Table of Contents
1. [Executive Summary & Quick Triage Card](#-executive-summary--quick-triage-card)
2. [Attack Kill Chain & SOC Triage Architecture](#-attack-kill-chain--soc-triage-architecture)
3. [Live Incident Triage Demonstration (Animated GIF)](#-live-incident-triage-demonstration)
4. [Lab Environment & Analyst Credentials](#-lab-environment--analyst-credentials)
5. [Investigation Deep Dive: Step-by-Step Walkthrough](#-investigation-deep-dive-step-by-step-walkthrough)
   * [Phase 1: Wazuh SIEM Telemetry & Endpoint Identification](#phase-1-wazuh-siem-telemetry--endpoint-identification)
   * [Phase 2: MITRE ATT&CK Matrix Correlation (24th Dec 2025)](#phase-2-mitre-attck-matrix-correlation-24th-dec-2025)
   * [Phase 3: Deep Log Forensic Analysis & Kill Chain Reconstruction](#phase-3-deep-log-forensic-analysis--kill-chain-reconstruction)
   * [Phase 4: TheHive Case Creation & Incident Classification](#phase-4-thehive-case-creation--incident-classification)
   * [Phase 5: Observable Registration & Telemetry Binding](#phase-5-observable-registration--telemetry-binding)
   * [Phase 6: SOC Action Item & Mandatory Task Creation](#phase-6-soc-action-item--mandatory-task-creation)
   * [Phase 7: MITRE ATT&CK TTP Association](#phase-7-mitre-attck-ttp-association)
   * [Phase 8: Tier 2 Reassignment & Formal Escalation](#phase-8-tier-2-reassignment--formal-escalation)
6. [Complete Step-by-Step Official Screenshot Archive (35 Images)](#-complete-step-by-step-official-screenshot-archive)
7. [Threat Hunting, Incident Response & Containment Playbook](#-threat-hunting-incident-response--containment-playbook)
8. [Conclusion & Key Takeaways](#-conclusion--key-takeaways)

---

## 📌 Executive Summary & Quick Triage Card

| Parameter / Field | Triage Value | SOC Operational Rationale |
|---|---|---|
| **Incident Case Title** | `Suspicious Account Creation Followed by Privileged Access Attempt` | Standardized naming convention identifying the persistence mechanism and subsequent privilege escalation attempt. |
| **Investigation Date** | `24th December 2025` | Temporal scope specified in the incident report and event timeline. |
| **Monitored Endpoint** | `ip-10-0-0-100` (`Agent ID: 002`) | Target Linux server hosting business services for Syntrix. |
| **Adversary Source IP** | `10.0.0.11` | Source host initiating the unauthorized SSH remote connection. |
| **Rogue Identity Created** | `eviluser` | Unauthorized local Linux user provisioned without IT authorization. |
| **Sensitive Target Asset** | `/etc/sudoers` | Critical Linux permission catalog targeted for root privilege escalation. |
| **SIEM Detection Rules** | T1136 (Create Account), T1021/T1078 (SSH Login), T1548.003 (Sudo /etc/sudoers) | Correlated multi-stage alerts triggered sequentially across a 19-minute window. |
| **Incident Classification** | 🔴 **True Positive — Multi-Stage Intrusion & Persistence** | Verified unauthorized account addition followed by remote interactive logon and sudo manipulation. |
| **Assigned Severity** | **`HIGH`** | High-impact threat involving unauthorized account creation and attempts to modify system-level root configurations. |
| **TLP Marking** | **`TLP:AMBER`** | Internal security incident with active system compromise indicators; restricted to Syntrix SOC and incident response staff. |
| **PAP Marking** | **`PAP:AMBER`** | Active investigation requiring controlled response actions; must not trigger defensive actions visible outside authorized personnel. |
| **Case Tags** | `privilege-escalation`, `account-creation`, `persistence`, `sudo`, `ssh` | Facilitates rapid indexing, metric generation, and retrospective threat hunting. |
| **Registered Observables** | 4 Total: `eviluser` (other, IOC: Yes), `10.0.0.11` (ip, IOC: No), `ip-10-0-0-100` (hostname, IOC: No), `/etc/sudoers` (filename, IOC: Yes) | Complete forensic evidence package bound to the case. |
| **Mandatory Task** | `Validate legitimacy of privileged access attempt` | Tier 2 task to verify authorization, audit shadow changes, and confirm blast radius. |
| **Task & Case Assignee** | `SOC 2` (`soc2@syntrix.com`) | Formal operational handoff from Tier 1 triage to Tier 2 deep containment. |

---

## 🏗️ Attack Kill Chain & SOC Triage Architecture

The diagram below details the adversary's tactical progression across the monitored Syntrix Linux endpoint (`ip-10-0-0-100`) alongside the SOC triage lifecycle:

![Attack Kill Chain & SOC Triage Architecture](./images/attack_killchain_and_triage_architecture.jpg)

```mermaid
flowchart TD
    subgraph Adversary ["Adversary Tactical Progression (24 Dec 2025)"]
        A1["07:41 UTC - Account Creation<br/>Local command adds 'eviluser'"] --> A2["07:59 UTC - Remote Ingress<br/>SSH Logon from 10.0.0.11 via 'eviluser'"]
        A2 --> A3["08:00 UTC - Privilege Escalation<br/>First-time sudo execution accessing /etc/sudoers"]
    end

    subgraph SIEM ["Wazuh SIEM Detection Engine"]
        W1["Rule: User added to system<br/>Technique: T1136 (Persistence)"]
        W2["Rule: Successful SSH authentication<br/>Technique: T1021.004 / T1078 (Lateral Movement)"]
        W3["Rule: Sudoers file accessed via sudo<br/>Technique: T1548.003 (Privilege Escalation)"]
    end

    subgraph SOC ["Syntrix SOC Triage & Escalation (TheHive)"]
        T1["SOC L1 Analyst (soc1@syntrix.com)<br/>Drills into Agent 002 (ip-10-0-0-100)"]
        T2["Correlates 3 Events across 19-min window<br/>Classifies as TRUE POSITIVE - HIGH Severity"]
        T3["Creates Case in TheHive<br/>TLP:AMBER / PAP:AMBER"]
        T4["Registers 4 Observables + 4 MITRE TTPs<br/>Defines Mandatory Task for Tier 2"]
        T5["Reassigns Case to SOC 2 (soc2@syntrix.com)<br/>Triggers Emergency Host Containment"]
    end

    A1 -.->|Telemetry| W1
    A2 -.->|Telemetry| W2
    A3 -.->|Telemetry| W3

    W1 --> T1
    W2 --> T2
    W3 --> T2
    T2 --> T3
    T3 --> T4
    T4 --> T5
```

---

## 🎬 Live Incident Triage Demonstration

The animated forensic recording below captures the complete interactive workflow executed during this incident triage: reviewing the Wazuh MITRE ATT&CK framework on December 24th, drilling down into the three correlated alerts, authoring the case in TheHive, registering all four observables, assigning the mandatory task, and reassigning the incident to SOC Level 2:

![Live Incident Triage Demonstration](./images/account_privesc_live_demo.gif)

---

## 🖥️ Lab Environment & Analyst Credentials

The hands-on environment comprises a dedicated dual-node Ubuntu architecture simulating a corporate SOC workstation and centralized detection infrastructure:

| Node / Interface | URL / Access Path | Authentication | Primary Function |
|---|---|---|---|
| **Primary SOC Workstation** | Ubuntu Desktop GUI (Firefox) | Default Session | Analyst triage console for Wazuh and TheHive. |
| **Wazuh SIEM v4.x** | `https://wazuh.ine.local` | Stored Browser Credentials | Security telemetry aggregator, rule matching engine, and MITRE matrix visualization. |
| **TheHive Incident Platform** | `http://localhost:9000` | **Username:** `soc1@syntrix.com`<br/>**Password:** `pass123` | Security incident management, observable cataloging, and Tier 1 to Tier 2 escalation. |
| **Target Monitored Endpoint** | `ip-10-0-0-100` (`Agent ID: 002`) | Wazuh Agent Ingestion | Internal Linux host where rogue user creation and sudo access occurred. |
| **Adversary Source Machine** | `10.0.0.11` | Network Ingress | Host initiating unauthorized remote SSH connections to the target machine. |

---

## 🔍 Investigation Deep Dive: Step-by-Step Walkthrough

### Phase 1: Wazuh SIEM Telemetry & Endpoint Identification
1. **Launch Browser & Access Wazuh:** Open Firefox and navigate to `https://wazuh.ine.local`. Authenticate using the pre-configured analyst credentials.
2. **Review Agents Summary:** Navigate to **Wazuh** -> **Agents Summary**. The fleet status shows active and disconnected agents.
3. **Filter Disconnected Agents:** Click on the **Disconnected** status metric to inspect offline/isolated endpoints.
4. **Locate Target Host:** Select **Agent ID: 002** corresponding to hostname `ip-10-0-0-100` (`10.0.0.100`).

### Phase 2: MITRE ATT&CK Matrix Correlation (24th Dec 2025)
1. **Navigate to MITRE Dashboard:** Inside Agent 002's view, click on the **More** dropdown and select the **MITRE ATT&CK** dashboard.
2. **Apply Temporal Filter:** Set the date range strictly to **24th December 2025**.
3. **Filter Active Techniques:** Enable the toggle **"Hide techniques with no alerts"** to highlight only tactics triggered on this date.
4. **Identify Active Threat Vectors:** The filtered matrix reveals three prominent alert clusters:
   * **Persistence:** `Create Account` (T1136)
   * **Lateral Movement / Initial Access:** `Remote Services` (T1021) & `Valid Accounts` (T1078)
   * **Privilege Escalation:** `Sudo and Sudo Caching` (T1548.003)

### Phase 3: Deep Log Forensic Analysis & Kill Chain Reconstruction

#### Event 1: Unauthorized Account Creation (07:41 UTC)
* **Technique:** MITRE ATT&CK **T1136 (Create Account)**
* **Timestamp:** `2025-12-24 07:41:00`
* **Log Description:** `New user added to the system`
* **Forensic Evidence:** The syslog/authlog parser identified an account creation event on host `ip-10-0-0-100`. The account username is explicitly identified as **`eviluser`**.
* **Analyst Assessment:** There was no corresponding approved service ticket or employee onboarding request for `eviluser`. This represents unauthorized persistence.

#### Event 2: Remote Interactive SSH Login (07:59 UTC)
* **Technique:** MITRE ATT&CK **T1021.004 (SSH)** / **T1078 (Valid Accounts)**
* **Timestamp:** `2025-12-24 07:59:00`
* **Log Description:** `Successful SSH authentication for eviluser`
* **Source IP:** **`10.0.0.11`**
* **Target Host:** `ip-10-0-0-100` (port 22)
* **Analyst Assessment:** Exactly 18 minutes after account creation, the newly created account `eviluser` authenticated successfully via SSH from internal host `10.0.0.11`. This establishes that the credentials were valid and remotely weaponized.

#### Event 3: Privilege Escalation Attempt Targeting /etc/sudoers (08:00 UTC)
* **Technique:** MITRE ATT&CK **T1548.003 (Sudo and Sudo Caching)**
* **Timestamp:** `2025-12-24 08:00:00`
* **Log Description:** `First time sudo execution by user` & `/etc/sudoers file accessed`
* **User Identity:** `eviluser`
* **Target File:** **`/etc/sudoers`**
* **Analyst Assessment:** Merely one minute after gaining SSH access, `eviluser` executed a command using `sudo` targeting `/etc/sudoers`. Modifying `/etc/sudoers` grants permanent, unrestricted passwordless root access. This confirms active privilege escalation.

---

### Phase 4: TheHive Case Creation & Incident Classification

1. **Access TheHive:** Open a new tab or switch to the second machine and navigate to `http://localhost:9000`. Log in as `soc1@syntrix.com` with password `pass123`.
2. **Initiate Case Creation:** Click **Create case** -> Select **Empty case**.
3. **Configure Case Parameters:**
   * **Title:** `Suspicious Account Creation Followed by Privileged Access Attempt`
   * **Date:** `Current Date`
   * **Severity:** **`HIGH`** *(Justification: New local account created, authenticated remotely, and attempted to overwrite `/etc/sudoers`)*
   * **TLP:** **`TLP:AMBER`** *(Internal security incident involving critical system integrity; sensitive operational data)*
   * **PAP:** **`PAP:AMBER`** *(Controlled investigation; defensive handling must follow established SOC protocols)*
   * **Tags:** `privilege-escalation`, `account-creation`, `persistence`, `sudo`, `ssh`
   * **Description:**
     ```text
     Wazuh detected the creation of a new local user account eviluser on host ip-10-0-0-100. 
     Shortly after account creation, successful SSH authentication was observed for the same account originating from internal IP 10.0.0.11. 
     Subsequent logs indicate that the newly created user executed sudo for the first time and attempted to modify the /etc/sudoers file, suggesting a potential privilege escalation attempt. 
     The sequence of events indicates possible unauthorized persistence and privilege escalation activity. 
     Findings have been documented and escalated for further review.
     ```
4. **Confirm Creation:** Click **Confirm** to initialize the case.

---

### Phase 5: Observable Registration & Telemetry Binding

Navigate to the **Observables** tab of the newly created case and register all four key forensic artifacts:

#### Observable 1: Rogue User Account
* **Type:** `other`
* **Value:** `eviluser`
* **TLP / PAP:** `TLP:AMBER` / `PAP:AMBER`
* **Is IOC:** **`Yes`**
* **Has been sighted:** **`Yes`**
* **Sighted at:** `2025-12-24 07:41`
* **Tags:** `new-account`, `persistence`, `local-user`
* **Description:** `Newly created local user account observed prior to remote authentication and privileged command execution.`

#### Observable 2: Ingress Source IP
* **Type:** `ip`
* **Value:** `10.0.0.11`
* **TLP / PAP:** `TLP:AMBER` / `PAP:AMBER`
* **Is IOC:** `No` (Internal infrastructure host requiring pivot analysis)
* **Has been sighted:** **`Yes`**
* **Sighted at:** `2025-12-24 07:59`
* **Tags:** `ssh`, `remote-access`
* **Description:** `Source IP used for successful SSH authentication to the newly created account.`

#### Observable 3: Affected Production Endpoint
* **Type:** `hostname`
* **Value:** `ip-10-0-0-100`
* **TLP / PAP:** `TLP:AMBER` / `PAP:AMBER`
* **Is IOC:** `No` (Internal target asset)
* **Has been sighted:** **`Yes`**
* **Sighted at:** `2025-12-24 08:00`
* **Tags:** `linux`, `privilege-escalation`
* **Description:** `Target Linux host involved in account creation, SSH access, and privileged command execution.`

#### Observable 4: Critical File Target
* **Type:** `filename`
* **Value:** `/etc/sudoers`
* **TLP / PAP:** `TLP:AMBER` / `PAP:AMBER`
* **Is IOC:** **`Yes`**
* **Has been sighted:** **`Yes`**
* **Sighted at:** `2025-12-24 08:00`
* **Tags:** `sudo`, `privilege-escalation`, `configuration`
* **Description:** `The /etc/sudoers file was accessed via sudo by the newly created user eviluser, indicating an attempt to modify privileged configuration for potential privilege escalation.`

---

### Phase 6: SOC Action Item & Mandatory Task Creation

1. Navigate to the **Tasks** tab inside the case.
2. Click **+** (Add Task) and specify the following Tier 2 action item:
   * **Group:** `default`
   * **Title:** `Validate legitimacy of privileged access attempt`
   * **Mandatory:** **`Yes`**
   * **Description:** `Validate whether the account creation and modification attempt of /etc/sudoers was authorized. Confirm if privilege escalation was successful and assess potential impact.`
   * **Assignee:** `SOC 2`
3. Click **Confirm** to commit the task.

---

### Phase 7: MITRE ATT&CK TTP Association

1. Navigate to the **TTPs** tab and click **+** (Add TTP).
2. Attach the four techniques mapped during triage:
   * **Catalog:** `Enterprise Attack`
   * **Occur Date:** `2025-12-24 07:41`
   * **TTP 1:** **`T1136 – Create Account`** (*New user eviluser was created*)
   * **TTP 2:** **`T1078 – Valid Accounts`** (*Successful SSH login using the newly created account*)
   * **TTP 3:** **`T1021 – Remote Services`** (*Remote SSH access from 10.0.0.11*)
   * **TTP 4:** **`T1548.003 – Sudo and Sudo Caching`** (*Attempt to modify /etc/sudoers using sudo*)
3. Click **Confirm** to lock the TTP mappings.

---

### Phase 8: Tier 2 Reassignment & Formal Escalation

1. Return to the case summary header.
2. Locate the **Assignee** field currently set to `soc1@syntrix.com`.
3. Select and reassign ownership to **`SOC 2`** (`soc2@syntrix.com`).
4. Save the update. The case is now formally escalated with complete forensic context, high severity priority, and structured observables.

---

## 📸 Complete Step-by-Step Official Screenshot Archive

Below is the exhaustive, ordered sequence of all 35 official screenshots captured during the investigation, mapped directly to their operational checkpoints:

### Step 1: Lab Access & Desktop Initialization
![Step 1 - Desktop GUI Access](./image/image34.jpg)
*Figure 1: Analyst desktop environment showing Firefox and terminal shortcuts.*

---

### Step 2: Wazuh SIEM Access & Telemetry Analysis

![Step 2a - Firefox Wazuh Login](./image/image32.jpg)
*Figure 2: Navigating to `https://wazuh.ine.local` on the SOC workstation.*

![Step 2b - Agents Summary Overview](./image/image9.jpg)
*Figure 3: Reviewing the Wazuh Agents Summary and clicking Disconnected.*

![Step 2c - Selecting Agent ID 002](./image/image12.jpg)
*Figure 4: Inspecting Agent ID 002 (`ip-10-0-0-100`).*

![Step 2d - Navigating to MITRE ATT&CK Dashboard](./image/image17.jpg)
*Figure 5: Clicking "More" and selecting the MITRE ATT&CK dashboard.*

![Step 2e - Filtering by Date (24th Dec 2025)](./image/image23.jpg)
*Figure 6: Filtering the ATT&CK framework for December 24, 2025, and hiding inactive techniques.*

![Step 2f - Inspecting Create Account Alert](./image/image26.jpg)
*Figure 7: Opening the T1136 Create Account alert cluster.*

![Step 2g - Account Creation Log Details (eviluser)](./image/image1.jpg)
*Figure 8: Alert details showing new user `eviluser` added to host `ip-10-0-0-100` at 07:41.*

![Step 2h - Inspecting Remote Services Alert](./image/image30.jpg)
*Figure 9: Opening the T1021 Remote Services alert cluster.*

![Step 2i - Remote SSH Access Log Details](./image/image18.jpg)
*Figure 10: Alert details showing SSH logon by `eviluser` from `10.0.0.11` at 07:59.*

![Step 2j - Inspecting Sudo and Sudo Caching Alert](./image/image14.jpg)
*Figure 11: Opening the T1548.003 Sudo and Sudo Caching alert cluster.*

![Step 2k - Sudoers Access Alert Notification](./image/image4.jpg)
*Figure 12: Notification showing `/etc/sudoers` accessed via sudo at 08:00.*

![Step 2l - Full Log Record of Sudoers Modification Attempt](./image/image5.jpg)
*Figure 13: Full log inspection confirming `eviluser` executed privileged commands on `/etc/sudoers`.*

---

### Step 3: TheHive Case Management & Escalation

![Step 3a - TheHive Login Screen](./image/image8.jpg)
*Figure 14: Accessing TheHive at `http://localhost:9000` with credentials `soc1@syntrix.com`.*

![Step 3b - Initiating New Case Creation](./image/image13.jpg)
*Figure 15: Clicking "Create case" in TheHive dashboard.*

![Step 3c - Selecting Empty Case Template](./image/image7.jpg)
*Figure 16: Choosing the Empty case template for manual investigation setup.*

![Step 3d - Populating Case Metadata](./image/image6.jpg)
*Figure 17: Entering Title, HIGH severity, TLP:AMBER, PAP:AMBER, tags, and detailed description.*

![Step 3e - Confirming Case Creation](./image/image24.jpg)
*Figure 18: Clicking "Confirm" to create the incident ticket.*

![Step 3f - Newly Created Case View](./image/image33.jpg)
*Figure 19: Incident case dashboard showing initial status and summary details.*

![Step 3g - Navigating to Observables Tab](./image/image15.jpg)
*Figure 20: Accessing the Observables tab and clicking "+".*

![Step 3h - Adding Observable 1: eviluser](./image/image31.jpg)
*Figure 21: Registering `eviluser` (Type: other, Is IOC: Yes, Sighted: 2025-12-24 07:41).*

![Step 3i - Saving and Adding Another Observable](./image/image11.jpg)
*Figure 22: Selecting "Save and add another" to continue registering forensic artifacts.*

![Step 3j - Adding Observable 2: 10.0.0.11](./image/image20.jpg)
*Figure 23: Registering `10.0.0.11` (Type: ip, Is IOC: No, Sighted: 2025-12-24 07:59).*

![Step 3k - Saving and Continuing](./image/image0.jpg)
*Figure 24: Selecting "Save and add another".*

![Step 3l - Adding Observable 3: ip-10-0-0-100](./image/image10.jpg)
*Figure 25: Registering `ip-10-0-0-100` (Type: hostname, Is IOC: No, Sighted: 2025-12-24 08:00).*

![Step 3m - Saving and Continuing](./image/image25.jpg)
*Figure 26: Selecting "Save and add another".*

![Step 3n - Adding Observable 4: /etc/sudoers](./image/image16.jpg)
*Figure 27: Registering `/etc/sudoers` (Type: filename, Is IOC: Yes, Sighted: 2025-12-24 08:00).*

![Step 3o - Confirming All Observables Registered](./image/image22.jpg)
*Figure 28: Reviewing the complete list of 4 registered observables in TheHive.*

![Step 3p - Navigating to Tasks Tab](./image/image28.jpg)
*Figure 29: Accessing the Tasks tab and clicking "+".*

![Step 3q - Defining Mandatory Investigation Task](./image/image3.jpg)
*Figure 30: Adding task "Validate legitimacy of privileged access attempt" assigned to SOC 2.*

![Step 3r - Confirming Task Creation](./image/image19.jpg)
*Figure 31: Committing the task to the incident case.*

![Step 3s - Navigating to TTPs Tab](./image/image2.jpg)
*Figure 32: Accessing the TTPs tab and clicking "+".*

![Step 3t - Mapping MITRE ATT&CK TTPs](./image/image21.jpg)
*Figure 33: Associating T1136, T1078, T1021, and T1548.003 with descriptions and date.*

![Step 3u - Reassigning Case Ownership to SOC 2](./image/image29.jpg)
*Figure 34: Changing the incident assignee from `soc1` to `SOC 2`.*

![Step 3v - Final Escalated Incident Case](./image/image27.jpg)
*Figure 35: Fully documented, prioritized, and escalated incident case ready for Tier 2 containment.*

---

## 🛡️ Threat Hunting, Incident Response & Containment Playbook

Following formal escalation from SOC Level 1 to Level 2, the following emergency containment and remediation steps must be executed immediately:

### 1. Host Isolation & Account Disabling
```bash
# Immediately lock the malicious user account
sudo usermod -L -e 1 eviluser

# Terminate all active processes spawned by eviluser
sudo pkill -u eviluser

# Check active network sockets associated with eviluser
sudo lsof -u eviluser

# Remove the unauthorized account and home directory after collecting memory/forensics
sudo userdel -r eviluser
```

### 2. Sudoers File Integrity Verification
```bash
# Verify checksum and syntax of /etc/sudoers
sudo visudo -c

# Audit git/history or diff against backup
sudo diff -u /etc/sudoers /etc/sudoers.bak

# Inspect sudoers drop-in configuration directory
sudo ls -la /etc/sudoers.d/
```

### 3. Source Host (`10.0.0.11`) Pivot Analysis
* Check whether `10.0.0.11` is compromised or running automated lateral movement tools (e.g., CrackMapExec, Ansible, Cobalt Strike).
* Review network flow logs between `10.0.0.11` and all other subnet hosts for additional lateral movements.

---

## 🏆 Conclusion & Key Takeaways

1. **Multi-Stage Attack Visibility:** The combination of Wazuh's MITRE ATT&CK integration and endpoint file/auth monitoring allowed the SOC to correlate three distinct events across a 19-minute window into a unified attack narrative.
2. **True Positive Distinction:** Unlike the trusted administrator brute-force scenario (which was benign), this activity exhibited zero operational authorization, rogue account creation (`eviluser`), and unauthorized privilege escalation targeting `/etc/sudoers`.
3. **Structured Case Governance:** Documenting the case in TheHive with appropriate TLP:AMBER / PAP:AMBER labels, explicit observables, mapped TTPs, and mandatory verification tasks guarantees seamless Tier 2 containment without operational delay.

---
*Authored by the Syntrix SOC Team | Reference: [INE Security Learning Lab](https://my.ine.com/course/soc-ticketing-reporting/7f70e83f-52fe-4234-a19d-e4acb30c5c43/lab/7ceb853d-64ab-47e9-8c41-187ba835bd32)*
