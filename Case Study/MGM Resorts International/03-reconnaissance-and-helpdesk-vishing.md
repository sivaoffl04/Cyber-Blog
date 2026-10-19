# Chapter 03: Reconnaissance & Help Desk Voice Phishing (Vishing)

> **Seminar Module:** The Social Engineering Kill Chain & Identity Seeding  
> **Target Audience:** Red Teams, Social Engineering Researchers, Help Desk Managers, Security Awareness Trainers  
> **Core Vectors:** Open-Source Intelligence (OSINT), LinkedIn Mining, Caller ID Spoofing, Vishing Tradecraft

---

## 1. The High-Level Attack Flow Architecture

The MGM Resorts intrusion followed a precise, multi-phase trajectory that transitioned from open-source profiling to total virtualization compromise in less than 48 hours.

![MGM Attack Flow Vector Diagram](image/mgm_attack_flow_diagram.jpg)
*Figure 3.1: Complete forensic attack flow vector: OSINT reconnaissance on LinkedIn ➔ Help Desk vishing ➔ Okta admin takeover ➔ Azure AD pivot ➔ VMware ESXi hypervisor mass encryption.*

![ThriveDX Incident Timeline](image/mgm_thrivedx_attack_timeline.jpg)
*Figure 3.2: Chronological incident timeline and operational progression from initial reconnaissance through crisis response.*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   MGM RESORTS ATTACK CHAIN ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [PHASE 1: OSINT] ────────► LinkedIn employee search identifies Okta Admin. │
│         │                                                                   │
│  [PHASE 2: VISHING] ──────► Phone call to IT Help Desk spoofing employee.   │
│         │                   MFA token reset & attacker device registered.   │
│         │                                                                   │
│  [PHASE 3: IDENTITY] ─────► Attacker logs into Okta; claims Super Admin.    │
│         │                   Tamfers with Inbound SAML Identity Federation.  │
│         │                                                                   │
│  [PHASE 4: LATERAL] ──────► Pivots to Microsoft Entra ID (Azure AD) and     │
│         │                   on-premises Active Directory Domain Controllers.│
│         │                                                                   │
│  [PHASE 5: ESXi] ─────────► Discovers VMware vCenter and ESXi hypervisors.  │
│         │                   Terminates virtual machines; deploys BlackCat.  │
│         ▼                                                                   │
│  [PHASE 6: IMPACT] ───────► Over 100 ESXi servers encrypted; slots & keys   │
│                             offline; $100M operational disruption.          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Phase 1: OSINT and Target Employee Profiling

Before placing a single phone call, Scattered Spider conducted meticulous open-source reconnaissance to select the optimal identity vector. 

### Why Target Identity Administrators?
In a typical enterprise, compromising a standard receptionist or marketing coordinator gives an attacker initial access, but requires extensive, noisy internal reconnaissance, vulnerability exploitation, and privilege escalation to reach domain control.

By contrast, **compromising an identity administrator yields instant, enterprise-wide sovereignty** over every single application, cloud tenant, and user account connected to the Identity Provider (IdP).

```
Traditional Path:
User Account ──► Endpoint Compromise ──► EDR Bypass ──► Kerberoast ──► Domain Admin
(High noise, multiple detection gates, takes days/weeks)

Scattered Spider Path:
LinkedIn Search ──► Identity Admin Found ──► Help Desk Vishing ──► Okta Super Admin
(Zero malware, zero EDR gates, completed in 10 minutes)
```

### The LinkedIn Reconnaissance Methodology
The threat actors searched LinkedIn using targeted Boolean queries to identify MGM Resorts employees with administrative authority:

```text
("MGM Resorts" OR "MGM Grand") AND ("Okta" OR "Identity" OR "IAM" OR "Active Directory" OR "Systems Engineer")
```

Through this open-source reconnaissance, the attackers gathered:
1. **Full Legal Name** and professional headshot.
2. **Current Job Title:** Senior Systems Engineer / Identity & Access Management Specialist.
3. **Department & Management Structure:** Reporting lines to Director of Enterprise Infrastructure.
4. **Corporate Email Scheme:** Derived from company conventions (e.g., `firstname.lastname@mgmresorts.com`).
5. **Employment Tenure:** Confirming whether the individual had been with the company long enough to possess senior administrative rights.

### Data Enrichment & PII Aggregation
Once the individual target was identified on LinkedIn, the threat actors cross-referenced the employee's name against commercial data broker databases, people-search websites (e.g., LexisNexis, TrueCaller, Radaris), and historical breach records (e.g., DeHashed, HaveIBeenPwned). 

Within minutes, the attackers acquired the employee's:
* Personal mobile telephone number
* Residential home address
* Date of birth
* Last four digits of the Social Security Number (SSN)
* Names of immediate family members

Armed with this dossier, the attackers possessed all the knowledge required to bypass standard Knowledge-Based Authentication (KBA) questions typically posed by enterprise help desk agents.

---

## 3. Phase 2: Social Engineering and the IT Help Desk Call

On Sunday, September 10, 2023, during off-peak weekend hours when help desk staffing was thin and supervisory oversight was minimal, the attacker initiated the call to MGM's IT Service Desk.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      THE VISHING EXECUTION PIPELINE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  1. Caller ID Spoofing: Masking outbound call with employee's area code     │
│  2. Acoustic Engineering: Background office chatter, domestic ambient noise │
│  3. Psychological Framing: High urgency, mild embarrassment, time-crunch    │
│  4. Knowledge-Based Auth: Passing static KBA checks (DOB, Employee ID, Zip) │
│  5. The Ask: "My phone fell in the pool / cracked; I cannot get Okta push"  │
│  6. Device Swap: "Can you clear my MFA and bind this new device temporarily"│
│  7. Identity Handover: Help desk clears MFA token; registers attacker phone │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Forensic Reconstruction: The Help Desk Dialogue
The following script reconstructs the conversational dynamics utilized by Scattered Spider operators, based on threat intelligence disclosures from Mandiant and CISA:

```text
[RING... RING... CALL CONNECTED]

HELP DESK AGENT:
"MGM Resorts Global IT Service Desk, this is Marcus. How may I assist you today?"

ATTACKER (Posing as Senior Identity Engineer):
"Hey Marcus, good morning. Listen, I am having a massive headache here. This is 
[Employee Name] from Enterprise Identity Engineering. My family and I are out 
for the weekend, and my iPhone fell into the pool and is completely water-damaged. 
It won't turn on at all."

HELP DESK AGENT:
"Oh wow, that's terrible! I'm sorry to hear that."

ATTACKER (Establishing Urgency & Authority):
"Yeah, total nightmare. But worse, the director just called me because there's an 
escalated ticket on the vCenter single-sign-on sync, and I need to log into the 
admin portal immediately from my backup laptop. But every time I try to authenticate, 
Okta sends a push notification to my dead phone."

HELP DESK AGENT:
"I understand. Before I can reset your MFA, I need to verify your identity. 
Can you provide your employee ID number, date of birth, and your department?"

ATTACKER (Rapid, Confident Delivery of OSINT Data):
"Sure thing. Employee ID is 482910, date of birth is September 14, 1982, and 
department is Enterprise IAM and Directory Services under Infrastructure."

HELP DESK AGENT (Looking up static HR record):
"Thank you, that matches what I have on screen. And your zip code?"

ATTACKER:
"89117, Las Vegas."

HELP DESK AGENT:
"Perfect, identity verified. I can generate a temporary bypass code or reset your 
registered MFA device. Which do you need?"

ATTACKER:
"Can you please clear the existing Okta Verify enrollment on my profile? I have 
my new personal device right here and I can scan the QR code right now to re-enroll 
so I don't have to keep bothering you guys."

HELP DESK AGENT:
"No problem at all. I have cleared your registered MFA devices. I am sending an 
activation link to your mobile number... wait, do you have access to your mobile?"

ATTACKER:
"No, remember the phone is dead. Can you read me the one-time activation token or 
send it to my secondary contact number: 702-555-0194?"

HELP DESK AGENT:
"Understood. Your one-time Okta enrollment code is: 849-204."

ATTACKER:
"Awesome, Marcus! You just saved my life and saved the director's weekend. 
Really appreciate the fast help. Have a great day!"

[CALL TERMINATED - DURATION: 8 MINUTES 42 SECONDS]
```

---

## 4. Analytical Breakdown: Why the Help Desk Failed

The help desk failure at MGM Resorts was not an individual failure by "Marcus"; it was an **architectural failure of the enterprise verification model**.

### 1. The Fallacy of Knowledge-Based Authentication (KBA)
Static biographical data—birthdays, zip codes, employee IDs, mother's maiden names, and phone numbers—**is public information**. In 2023, data breaches, social media, and data broker aggregators have made personal information universally accessible. Using static data to authenticate high-privilege administrators provides zero cryptographic assurance.

### 2. Lack of Out-of-Band (OOB) Manager Authorization
In a mature security posture, resetting the authentication credentials of an employee with **Super Admin** or domain administrative privileges must require secondary out-of-band signoff:
* A video call verification with a known supervisor.
* An approval ticket authorized by the employee's direct manager.
* A cryptographic physical credential presented at a corporate badging office.

At MGM, tier-1 help desk operators had the technical authority to reset credentials for senior engineers and system administrators without supervisory intervention.

### 3. Asymmetric Information & Pressure
Help desk agents are measured on **Average Handle Time (AHT)** and **First-Call Resolution (FCR)**. Their job performance is evaluated based on customer service and speed, not adversarial resistance. When confronted by a confident, articulate colleague invoking senior executive names and urgent operational outages, the psychological incentive is to resolve the issue as quickly as possible.

---

## 5. Tactical Red Team Playbook: Help Desk Vishing Assessment

To test organizational resilience against Scattered Spider tradecraft, enterprise Red Teams must execute structured vishing simulations:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    RED TEAM VISHING ASSESSMENT FRAMEWORK                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  STEP 1: Target Scoping                                                     │
│  Identify 10 high-privilege users (Okta Admins, Cloud Engineers, SecOps).   │
│                                                                             │
│  STEP 2: OSINT Aggregation                                                  │
│  Harvest LinkedIn, corporate blogs, and public records for target dossiers. │
│                                                                             │
│  STEP 3: Telephony Setup                                                    │
│  Configure VoIP trunk (e.g., Twilio, Telnyx) with Caller ID spoofing.       │
│                                                                             │
│  STEP 4: Execution Simulation                                               │
│  Place recorded test calls during off-hours requesting password/MFA resets. │
│                                                                             │
│  STEP 5: Metric Evaluation                                                  │
│  • Did the agent request out-of-band verification?                          │
│  • Did the agent escalate privileged account resets to a manager?           │
│  • Was a security incident ticket generated immediately?                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Seminar Discussion Questions

1. **The Friction vs. Support Paradox:** If an organization mandates that any MFA reset requires a video call with a manager, what happens when a critical production server is down at 2:00 AM on a Sunday and the manager is unavailable?
2. **Caller ID Spoofing Countermeasures:** Why do legacy corporate PBX and VoIP telephone networks still allow incoming callers to present arbitrary caller ID numbers, and how can protocols like STIR/SHAKEN mitigate this risk?
