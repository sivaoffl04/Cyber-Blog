# 🛡️ False Positive Validation: Trusted Admin Brute-Force Detection — Complete SOC Walkthrough

![False Positive Validation Hero Banner](./images/false_positive_validation_banner.jpg)

> **Lab Platform:** [INE Security](https://my.ine.com/course/soc-ticketing-reporting/7f70e83f-52fe-4234-a19d-e4acb30c5c43/lab/b0e70f5c-530f-494d-af7b-a6a2ff05631d)  
> **Course:** SOC Ticketing & Reporting  
> **Role:** SOC Level 1 Incident Analyst (Organization: *Syntrix*)  
> **Investigation Date:** **7th December 2025**  
> **Target Endpoint (Agent 001):** `10.0.0.100` (Syntrix Internal Ubuntu Server)  
> **Source Host:** `10.0.0.11` (Syntrix Administrator Workstation)  
> **Targeted Account & Service:** User `root` via OpenSSH (`sshd`)  
> **Key Tools:** Mozilla Firefox, **Wazuh SIEM v4.x**, **TheHive Incident Management Platform**  
> **Status:** 🟢 **100% Solved — Validated False Positive, Case Documented, Observables Attached, & Escalated to SOC L2**

---

## 📑 Table of Contents
1. [Executive Summary & Quick Triage Card](#executive-summary--quick-triage-card)
2. [SOC Triage & Escalation Workflow Architecture](#soc-triage--escalation-workflow-architecture)
3. [Live Case Management Demonstration (Animated GIF)](#live-case-management-demonstration)
4. [Lab Environment & Analyst Credentials](#lab-environment--analyst-credentials)
5. [Investigation Deep Dive: Step-by-Step Walkthrough](#investigation-deep-dive-step-by-step-walkthrough)
   * [Phase 1: Wazuh SIEM Telemetry & MITRE ATT&CK Triage](#phase-1-wazuh-siem-telemetry--mitre-attck-triage)
   * [Phase 2: Log Drill-Down & False Positive Validation](#phase-2-log-drill-down--false-positive-validation)
   * [Phase 3: TheHive Case Creation & Incident Classification](#phase-3-thehive-case-creation--incident-classification)
   * [Phase 4: Observable Registration & Telemetry Binding](#phase-4-observable-registration--telemetry-binding)
   * [Phase 5: Mandatory Task Assignment & SOC L2 Escalation](#phase-5-mandatory-task-assignment--soc-l2-escalation)
6. [Complete Step-by-Step Official Screenshot Archive](#complete-step-by-step-official-screenshot-archive)
7. [SOC Engineering: TLP, PAP & Detection Tuning](#soc-engineering-tlp-pap--detection-tuning)
8. [Conclusion & Key Takeaways](#conclusion--key-takeaways)

---

## 📌 Executive Summary & Quick Triage Card

| Parameter / Field | Triage Value | SOC Operational Rationale |
|---|---|---|
| **Incident Title** | `Failed SSH Brute-Force Login Attempt from Internal Admin Host (False Positive)` | Clear, standardized naming convention identifying vector, origin, and preliminary verdict. |
| **Investigation Date** | `7th December 2025` | Baseline timestamp established in the lab scenario. |
| **Target Host / Agent** | `10.0.0.100` (`Agent ID: 001`) | Internal server monitored by Wazuh agent. |
| **Source IP Address** | `10.0.0.11` | **Syntrix Administrator Workstation** (Trusted internal asset). |
| **Targeted Account** | `root` | System administrator account targeted during maintenance. |
| **SIEM Detection Rule** | `SSH Brute Force (T1110)` | Wazuh rule triggered due to consecutive failed authentications. |
| **Triage Verdict** | 🟢 **False Positive (Benign Administrative Activity)** | Activity originated from approved administrator workstation during scheduled system maintenance. |
| **Assigned Severity** | **`LOW`** | No compromise, trusted source, no indicators of unauthorized lateral movement. |
| **TLP Marking** | **`TLP:CLEAR`** | Internal operational telemetry, non-sensitive, permissible to share within Syntrix. |
| **PAP Marking** | **`PAP:CLEAR`** | No defensive restrictions, purely informational documentation. |
| **Case Tags** | `brute-force`, `false-positive`, `ssh`, `internal-activity` | Categorizes case for future query indexing and metric generation. |
| **Attached Observable** | Type: `ip` \| Value: `10.0.0.11` \| Sighted: `07/12/2025 18:13` | Enables historical threat correlation and tracking across TheHive/MISP. |
| **Mandatory Task** | `Cross-verify False Positive SSH Brute-Force Login Attempt from internal admin host` | Mandates second-tier verification against IT change management records. |
| **Task Assignee** | `SOC 2` (`soc2@syntrix.com`) | Assigns formal verification to SOC Tier 2 analyst. |
| **Case Escalation** | Ownership reassigned from `soc1@syntrix.com` to `soc2@syntrix.com` | Finalizes Level 1 handoff for formal review and ticket closure. |

---

## 🏗️ SOC Triage & Escalation Workflow Architecture

The diagram below maps the complete end-to-end incident lifecycle from raw telemetry ingestion in Wazuh to contextual triage, case documentation in TheHive, and formal Tier 2 escalation:

![SOC Triage & Escalation Workflow](./images/soc_triage_escalation_workflow.jpg)

### Triage Stages Dissected:
1. **Detection & Ingestion:** Wazuh agent detects repeated `sshd` authentication failures and flags MITRE ATT&CK technique **T1110 (Brute Force)**.
2. **Contextual Correlation:** The Level 1 analyst queries asset inventory and discovers source IP `10.0.0.11` belongs to the enterprise network administrator.
3. **Hypothesis Testing:** Are there secondary payloads, webshells, or anomalous outbound connections? None found. Root cause: Admin mistyped credentials or ran an automated maintenance script.
4. **Standardized Documentation:** Record findings in TheHive with appropriate Traffic Light Protocol (TLP) and Permissible Actions Protocol (PAP) markings.
5. **Separation of Duties:** Escalate case to SOC Tier 2 to verify against change tickets before permanent closure.

---

## 🎬 Live Case Management Demonstration

The animated demonstration below showcases the interactive SOC workflow: reviewing the Wazuh alert, creating the case in TheHive, registering the sighted IP observable, assigning the mandatory task, and executing the L2 escalation:

![TheHive Case Management Live Demo](./images/thehive_case_management_live_demo.gif)

---

## 🖥️ Lab Environment & Analyst Credentials

* **Wazuh SIEM Dashboard URL:** `https://wazuh.ine.local` (Pre-authenticated via stored browser session)
* **TheHive Case Management URL:** `http://localhost:9000`
* **Analyst Credentials:**
  * **Username:** `soc1@syntrix.com`
  * **Password:** `pass123`
* **Enterprise Host Assets:**
  * **Administrator Workstation:** `10.0.0.11`
  * **Target Ubuntu Host (Agent 001):** `10.0.0.100`

---

## 🔬 Investigation Deep Dive: Step-by-Step Walkthrough

### Phase 1: Wazuh SIEM Telemetry & MITRE ATT&CK Triage

1. **Accessing the Wazuh Dashboard:** Open Firefox on the primary Ubuntu analyst workstation and navigate to `https://wazuh.ine.local`.
2. **Reviewing Monitored Agents:** In the Wazuh Overview, inspect the **Agents Summary**. The environment features 1 agent (`Agent ID: 001`, status disconnected). Click on the agent to view its historical telemetry.
3. **Navigating to MITRE ATT&CK Framework View:** Click **More** $\rightarrow$ **MITRE ATT&CK** $\rightarrow$ **Framework**.
4. **Setting the Temporal Baseline:** Set the investigation timeframe filter to **7th December 2025**. Enable the filter to **Hide techniques with no alerts** to spotlight active detections.
5. **Identifying the Alert:** Under Credential Access, technique **T1110 (Brute Force)** shows active triggers.

---

### Phase 2: Log Drill-Down & False Positive Validation

1. **Expanding the Alert Details:** Click on the **Brute Force** event to inspect the raw log data and rule metadata.
2. **Analyzing the Description:**
   * Rule description: *"sshd: brute force trying to get access to the system"*
   * User target: `root`
   * Target endpoint: `10.0.0.100`
   * Source IP: `10.0.0.11`
   * Event Timestamp: `07/12/2025 18:13`
3. **Contextual Evaluation:**
   * In an external attack scenario, source IPs are untrusted public addresses, and failed passwords reflect common dictionaries (`admin`, `123456`, `toor`).
   * Here, source IP `10.0.0.11` is explicitly documented as the **Syntrix Administrator's Workstation**.
   * The failed SSH attempts for `root` indicate an administrator attempting system maintenance, misconfiguring an SSH key/password, or running a routine administration script.
4. **Triage Verdict:** **False Positive**. The alert does not represent an external threat actor or unauthorized intrusion. However, in enterprise SOC standard operating procedures (SOP), false positives involving administrative credentials must still be formally documented and escalated for change-management cross-verification.

---

### Phase 3: TheHive Case Creation & Incident Classification

1. **Accessing TheHive:** Switch to the second Ubuntu machine, open Firefox, and browse to `http://localhost:9000`. Log in using `soc1@syntrix.com` / `pass123`.
2. **Creating the Case:** Click **Create case** $\rightarrow$ Select **Empty case**.
3. **Configuring Incident Metadata:**
   * **Title:** `Failed SSH Brute-Force Login Attempt from Internal Admin Host (False Positive)`
   * **Date:** Current system date and time.
   * **Severity:** **`LOW`** *(Rationale: No active compromise; originating from trusted internal administrative host; validated as benign).*
   * **TLP:** **`TLP:CLEAR`** *(Information carries no sensitivity and can be shared freely across enterprise departments).*
   * **PAP:** **`PAP:CLEAR`** *(Recipients may freely use information for defensive purposes without operational restrictions).*
   * **Tags:** `brute-force`, `false-positive`, `ssh`, `internal-activity`
   * **Description:**
     ```text
     Investigation confirmed the source IP 10.0.0.11 is a trusted internal administrative workstation. The failed login attempt was associated with legitimate system maintenance activities.
     ```
4. **Confirming Case Creation:** Click **Confirm** to initialize the case.

---

### Phase 4: Observable Registration & Telemetry Binding

Observables link raw indicators of compromise (IoCs) or operational artifacts to an incident, allowing SIEM/SOAR platforms and threat intelligence platforms (MISP) to correlate future sightings.

1. **Navigating to Observables:** Inside the newly created case, click the **Observables** tab.
2. **Adding New Observable:** Click the **`+`** button and provide:
   * **Type:** `ip`
   * **Value:** `10.0.0.11`
   * **TLP:** `TLP:CLEAR`
   * **PAP:** `PAP:CLEAR`
   * **Has been sighted:** `Yes`
   * **Sighted at:** `07/12/2025 18:13` *(Timestamp captured from Wazuh raw alert)*
   * **Tags:** `internal`, `admin-workstation`, `false-positive`, `brute-force`
   * **Description:**
     ```text
     Source IP associated with failed authentication attempt. Validated as a trusted internal administrative workstation performing legitimate maintenance.
     ```
3. **Confirming Observable:** Click **Confirm** to bind the observable to the case.

---

### Phase 5: Mandatory Task Assignment & SOC L2 Escalation

In a mature Security Operations Center, a Level 1 analyst cannot unilaterally close an alert involving administrative credentials without a secondary review from Tier 2 / Incident Response.

1. **Creating Verification Task:** Navigate to the **Tasks** tab and click **`+`**.
2. **Task Configuration:**
   * **Group:** `default`
   * **Title:** `Cross-verify False Positive SSH Brute-Force Login Attempt from internal admin host`
   * **Mandatory:** **`YES`**
   * **Assignee:** `SOC2` (`soc2@syntrix.com`)
   * **Description:**
     ```text
     Cross-verify failed SSH authentication attempts originating from internal administrative workstation 10.0.0.11. Validate that the activity aligns with approved maintenance activity and confirm no indicators of compromise are present. If findings confirm legitimate behavior, close the case as a false positive.
     ```
3. **Confirming Task:** Click **Confirm**.
4. **Reassigning Case Ownership (Escalation):**
   * Navigate back to the case details view.
   * Under the **Owner** field, change the assignee from `soc1@syntrix.com` to **`soc2@syntrix.com`**.
   * Case status updates to escalated state, completing the Tier 1 incident response lifecycle.

---

## 📑 Complete Step-by-Step Official Screenshot Archive

Below is the complete sequence of 25 official screenshots capturing every UI step in Wazuh and TheHive:

### Step 1: Accessing the Analyst Workstation
![Step 1 - Accessing Ubuntu Machine](./image/image13.jpg)

### Step 2: Accessing Wazuh SIEM Dashboard
![Step 2 - Wazuh Dashboard Login](./image/image11.jpg)

### Step 3: Inspecting Agents Summary
![Step 3 - Agents Summary](./image/image20.jpg)

### Step 4: Selecting Agent 001
![Step 4 - Agent 001 Details](./image/image5.jpg)

### Step 5: Expanding Agent Navigation
![Step 5 - Agent Navigation Menu](./image/image10.jpg)

### Step 6: Opening MITRE ATT&CK Dashboard
![Step 6 - MITRE ATT&CK Dashboard](./image/image3.jpg)

### Step 7: Filtering by Date: 7th December 2025
![Step 7 - MITRE ATT&CK Framework Date Filter](./image/image6.jpg)

### Step 8: Identifying Brute-Force (T1110) Alert
![Step 8 - Brute Force Alert Triggered](./image/image2.jpg)

### Step 9: Expanding Brute-Force Event Details
![Step 9 - Brute Force Description and Metrics](./image/image7.jpg)

### Step 10: Correlating Source IP 10.0.0.11 & Target 10.0.0.100
![Step 10 - Source IP 10.0.0.11 Verification](./image/image8.jpg)

### Step 11: Recording Event Timestamp (07/12/2025 18:13)
![Step 11 - Event Timestamp Captured](./image/image15.jpg)

### Step 12: Logging into TheHive as soc1@syntrix.com
![Step 12 - TheHive Login Screen](./image/image12.jpg)

### Step 13: Initializing New Incident Case
![Step 13 - TheHive Create Case Button](./image/image16.jpg)

### Step 14: Selecting Empty Case Template
![Step 14 - Empty Case Template Selection](./image/image1.jpg)

### Step 15: Entering Case Title, Low Severity, Tags & Description
![Step 15 - Case Details Form Entry](./image/image4.jpg)

### Step 16: Confirming Case Creation
![Step 16 - Case Confirmation Dialog](./image/image0.jpg)

### Step 17: Case Successfully Initialized
![Step 17 - Created Case Dashboard](./image/image23.jpg)

### Step 18: Navigating to Observables Tab
![Step 18 - Observables Tab Navigation](./image/image9.jpg)

### Step 19: Adding IP Observable: 10.0.0.11 with Sighting
![Step 19 - New Observable Configuration](./image/image17.jpg)

### Step 20: Confirming Observable Creation
![Step 20 - Observable Confirmed](./image/image18.jpg)

### Step 21: Navigating to Tasks Tab
![Step 21 - Tasks Tab Navigation](./image/image21.jpg)

### Step 22: Assigning Mandatory Verification Task to SOC2
![Step 22 - Mandatory Task Form Entry](./image/image14.jpg)

### Step 23: Confirming Task Assignment
![Step 23 - Task Created Successfully](./image/image19.jpg)

### Step 24: Reassigning Case Owner to soc2@syntrix.com
![Step 24 - Case Owner Reassignment](./image/image22.jpg)

### Step 25: Case Formally Escalated to Level 2
![Step 25 - Escalation Completed](./image/image24.png)

---

## 🛡️ SOC Engineering: TLP, PAP & Detection Tuning

### 1. Traffic Light Protocol (TLP 2.0) Matrix
* **`TLP:RED`:** Strictly for the recipient's eyes only; cannot be shared further.
* **`TLP:AMBER`:** Limited disclosure within the recipient's organization on a need-to-know basis.
* **`TLP:AMBER+STRICT`:** Restricted strictly to the recipient's direct team.
* **`TLP:GREEN`:** Dissemination allowed within the organization and authorized external peers.
* **`TLP:CLEAR`:** **(Selected in this lab)** Open intelligence with no disclosure restrictions.

### 2. Permissible Actions Protocol (PAP)
* **`PAP:RED`:** Passive defensive observation only. Active probing or scanning is strictly forbidden.
* **`PAP:AMBER`:** Actions permissible within private organizational boundaries.
* **`PAP:GREEN`:** Active scanning and threat hunting permissible across organizational systems.
* **`PAP:CLEAR`:** **(Selected in this lab)** Free operational usage without restrictions.

### 3. Wazuh Detection Tuning & Rule Whitelisting
To prevent future false-positive alert fatigue while maintaining detection sensitivity for actual threats, detection engineers implement conditional rule overrides:

```xml
<!-- /var/ossec/etc/rules/local_rules.xml -->
<group name="syslog,sshd,">
  <!-- Rule 100110: Suppress SSH brute-force alert for approved admin workstation -->
  <rule id="100110" level="3">
    <if_sid>5712</if_sid>
    <srcip>10.0.0.11</srcip>
    <description>SSH brute-force from trusted administrator workstation (maintenance exception)</description>
    <group>trusted_admin_activity,</group>
  </rule>
</group>
```

> [!TIP]
> **Defensive Best Practice:** Never disable brute-force detection rules globally! Instead, use narrow source IP conditional matching (`<srcip>10.0.0.11</srcip>`) and log the event at informational level (`level="3"`) so audit trails remain intact.

---

## 🎯 Conclusion & Key Takeaways

1. **Context is King:** A brute-force alert is only malicious if the source, frequency, and intent are unverified. Checking internal asset databases prevented an unnecessary high-severity incident escalation.
2. **False Positives Require Documentation:** A confirmed false positive must never be ignored or deleted without a record. Documenting cases in TheHive preserves institutional memory and audit compliance.
3. **Structured Escalation Protects the SOC:** Assigning mandatory tasks and reassigning case ownership ensures accountability and follows enterprise SOC Tier 1 $\rightarrow$ Tier 2 escalation standards.
