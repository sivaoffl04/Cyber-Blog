# Chapter 13: Seminar Handbook, Tabletop Exercises & Curriculum

> **Seminar Module:** Educational Delivery, GenAI Voice Threat Horizons & Tabletop Exercise (TTX)  
> **Target Audience:** Seminar Leaders, Cybersecurity Instructors, Incident Commanders, Executive Trainers  
> **Includes:** 4-Phase Interactive Tabletop Exercise, GenAI Threat Horizons & Executive Debriefing Guide

---

## 1. The Threat Horizon: Social Engineering in the GenAI Era

While Scattered Spider executed their 2023 vishing campaigns using natural human conversational fluency, the rapid maturation of **Generative AI (GenAI) Audio Synthesis** has fundamentally altered the threat landscape.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                      THE EVOLUTION OF VOICE PHISHING (VISHING)                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   2021-2022: LEGACY VISHING                                                     │
│   • Heavy foreign accents, robotic text-to-speech, spoofed caller IDs.          │
│   • Easily recognized by trained help desk operators.                           │
│                                                                                 │
│   2023: NATIVE HUMAN VISHING (SCATTERED SPIDER)                                 │
│   • Native colloquial English, high conversational agility, ambient noise.      │
│   • Convinced help desk agents through charisma, urgency, and familiarity.      │
│                                                                                 │
│   2024-PRESENT: DEEPFAKE GENERATIVE AUDIO CLONING                               │
│   • High-fidelity voice cloning requiring as little as 3 seconds of reference   │
│     audio scraped from corporate YouTube videos, podcasts, or earnings calls.   │
│   • Real-time voice conversion (RVC) operating with zero latency over VoIP.     │
│   • Generates perfect acoustic clones of the CEO, CISO, or VP of Engineering.   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### The Inadequacy of Acoustic Trust
In the GenAI era:
* **Hearing a familiar voice over the telephone is zero proof of identity.**
* Even video calls can be compromised using real-time face-swapping software.
* **The Imperative:** Organizations must transition from sensory-based trust (hearing or seeing an employee) to **cryptographic mathematical trust** (FIDO2 WebAuthn challenges, hardware tokens, and verifiable digital credentials).

---

## 2. Tabletop Exercise (TTX): "Operation Desert Spider"

This complete, four-phase tabletop simulation is designed for executive leadership, SOC management, and incident response teams.

### Exercise Parameters:
* **Target Enterprise:** "Apex Gaming & Hospitality Corp" (50,000 employees, 25 resort destinations).
* **Time Duration:** 3 Hours (45 minutes per inject + 45 minute debrief).
* **Roles Represented:** Incident Commander, CISO, CIO, VP of Hospitality Operations, General Counsel, VP of Corporate Communications, Lead Threat Hunter.

---

### Inject 1: The Sunday Morning Help Desk Ticket (Sunday, 03:15 AM)

```text
[SITUATION REPORT - INJECT 1]
At 03:15 AM on a holiday weekend Sunday, a caller contacts the tier-1 IT Service Desk 
claiming to be David Vance, Principal Identity Architect. The caller states:
"My company laptop and phone were stolen from my rental car. I am on-call, and the 
Datacenter VMware cluster is alarming. I need you to reset my Okta Verify factor and 
bind it to my temporary loaner phone right now."

The caller provides David Vance's correct Employee ID, Date of Birth, and residential 
address. The help desk agent clears the factor and provides a one-time enrollment code. 
At 03:28 AM, a new device authenticates to Okta from a residential IP address in Chicago.
```

#### Facilitator Questions for the Room:
1. **To Help Desk Management:** What control should have stopped this ticket from proceeding without out-of-band verification?
2. **To the SOC Lead:** Does your SIEM correlate factor deactivations on privileged accounts with subsequent immediate logins from unmanaged IP ranges?
3. **To the CISO:** What is your policy for verifying an identity engineer whose phone and laptop have both been lost simultaneously?

---

### Inject 2: The Anomaly in Cloud Directory (Sunday, 14:30 PM)

```text
[SITUATION REPORT - INJECT 2]
At 14:30 PM, an automated alert fires in the SOC:
"High-Severity Alert: Inbound SAML Identity Provider Created in Okta."
The actor is the David Vance account. Simultaneously, Azure AD Audit logs show a new 
Enterprise Application registration with 'Directory.ReadWrite.All' Graph permissions.

When the on-call SOC analyst calls David Vance's personal phone number on file, 
David answers and says: "I've been on a flight with my family all day. My phone and 
laptop are in my backpack. I haven't called the help desk in six months!"
```

#### Facilitator Questions for the Room:
1. **To Incident Response:** You have confirmed an active adversary with Super Admin access in Okta. What is your immediate containment action?
2. **To Identity Engineering:** If you suspend David Vance's account, how do you sever the rogue Inbound Identity Provider without disrupting valid employee SSO?
3. **To General Counsel:** Does an unauthorized IdP creation constitute a confirmed data breach requiring notification to outside counsel or insurers?

---

### Inject 3: The Hypervisor Lockout & Casino Chaos (Monday, 02:45 AM)

```text
[SITUATION REPORT - INJECT 3]
At 02:45 AM, monitoring alarms trigger across the Las Vegas flagship casino:
• 40 VMware ESXi hosts have dropped offline in vCenter.
• Over 400 virtual machines powering the Casino Management System (CMS) and 
  Property Management System (PMS) have terminated.
• Slot machines display tilt error code 0x88F1; players cannot cash out vouchers.
• Hotel keyless door locks fail; hundreds of guests are locked out of rooms.
• An unencrypted text file appears on remaining storage shares:
  "YOUR HYPERVISORS ARE ENCRYPTED. CONTACT US ON TOR. YOU HAVE 72 HOURS: $25M USD."
```

#### Facilitator Questions for the Room:
1. **To Executive Leadership:** Do you proactively sever all internet connectivity to all 25 properties, knowing it will halt all food, beverage, and gaming transactions?
2. **To the Incident Commander:** What is the status of your hypervisor backups? Are your storage snapshots air-gapped and immutable?
3. **To VP of Hospitality Operations:** What is your manual contingency plan for 15,000 hotel guests who cannot enter their rooms?

---

### Inject 4: The Extortion Press Leak & SEC Clock (Tuesday, 08:30 AM)

```text
[SITUATION REPORT - INJECT 4]
At 08:30 AM, the threat actor group posts on social media:
"Apex Corp's board is incompetent. We have 500GB of customer databases including 
SSNs, player loss records, and VIP high-roller dossiers. If they do not pay by 
tomorrow, we will publish the full archive and report them to the SEC."

A Wall Street Journal reporter emails Corporate Communications requesting comment, 
citing leaked screenshots of internal employee Slack channels. The company's stock 
is down 6.5% in pre-market trading.
```

#### Facilitator Questions for the Room:
1. **To General Counsel & CFO:** Has a "materiality determination" occurred under SEC Item 1.05 Form 8-K rules? When does the 4-business-day clock expire?
2. **To Corporate Communications:** How do you balance transparency with customer reassurance while investigations are active?
3. **To the Board of Directors:** Do you negotiate to suppress the public release of customer VIP data, or do you stand on principle and refuse extortion?

---

## 3. Seminar Master Curriculum & Syllabus

| Module | Core Topic | Duration | Key Learning Outcome |
| :---: | :--- | :---: | :--- |
| **01** | **Executive Briefing & Fact Sheet** | 30 Mins | Comprehend the macro-scale financial, legal, and operational impact of the breach. |
| **02** | **Threat Actor Profiling (Scattered Spider + ALPHV)** | 45 Mins | Analyze the symbiotic division of labor between access brokers and RaaS cartels. |
| **03** | **OSINT & Help Desk Vishing Tradecraft** | 45 Mins | Identify psychological vulnerabilities in service desk verification workflows. |
| **04** | **Okta & Cloud Identity Mechanics** | 60 Mins | Deconstruct factor enrollment bypasses, Inbound SAML federation, and IdP persistence. |
| **05** | **Hypervisor Exploitation (ESXi & vCenter)** | 60 Mins | Understand why virtualization layers are prime targets for high-density ransomware. |
| **06** | **Incident Response & The Isolation Dilemma** | 45 Mins | Evaluate the systemic consequences of defensive network severance. |
| **07** | **Detection Engineering (Splunk & Sigma)** | 60 Mins | Deploy and tune production SPL and Sigma correlation rules for identity telemetry. |
| **08** | **Zero Trust & Help Desk Hardening** | 45 Mins | Implement out-of-band video verification, FIDO2 WebAuthn, and strict ESXi lockdown. |
| **09** | **Comparative Analysis: MGM vs. Caesars** | 45 Mins | Debate the ethics, fiduciary duty, and long-term risk of paying cyber ransoms. |
| **10** | **Executive Tabletop Simulation (TTX)** | 90 Mins | Execute high-pressure crisis decision-making under active cyber incident injects. |

---

## 4. Key Takeaways: The Principles of Modern Identity Resilience

1. **Identity is the Root of Enterprise Trust:** Firewalls and endpoint sensors are ineffective if an attacker possesses authenticated administrative tokens in your cloud identity directory.
2. **The Help Desk is a High-Value Cyber Gateway:** Any organization that allows tier-1 support technicians to reset credentials using static biographical PII has zero meaningful perimeter defense.
3. **Isolate the Virtualization Management Tier:** VMware ESXi hypervisors must never share identity federations or network routing with corporate enterprise workstations.
4. **Resilience Requires Manual Fallback Preparation:** When digital systems collapse, an organization's ultimate survival depends on the preparedness of its human workforce to execute manual business continuity procedures.
