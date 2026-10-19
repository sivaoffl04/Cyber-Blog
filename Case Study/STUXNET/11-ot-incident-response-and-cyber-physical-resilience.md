# Chapter 11: OT Incident Response & Cyber-Physical Resilience

> **Seminar Module:** Crisis Incident Response in Operational Technology & Safety-Critical Engineering  
> **Target Audience:** Incident Commanders, Plant Managers, Safety Officers, OT Security Responders  
> **Frameworks:** NIST SP 800-82 Rev. 3 (Guide to OT Security) & IEC 62443 Security Standards

---

## 1. The Core Dilemma: Why IT Incident Response Kills in OT

In enterprise Information Technology (IT), the golden rule of incident response is simple:
> *"When a server is compromised, pull the network cable, isolate the host, and power it down immediately to stop data exfiltration."*

In Operational Technology (OT), applying this IT mindset can be **catastrophic or lethal**:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    THE IT VS. OT INCIDENT RESPONSE CONFLICT                     │
├────────────────────────────────────────┬─────────────────────────────────────────┤
│        ENTERPRISE IT RESPONSE          │         INDUSTRIAL OT RESPONSE          │
├────────────────────────────────────────┼─────────────────────────────────────────┤
│ • Primary Metric: Confidentiality      │ • Primary Metric: Human & Process Safety│
│ • Isolation Action: Pull network cable │ • Isolation Action: Halts cooling pumps │
│ • System Action: Power down server     │ • System Action: Valves fail open/closed│
│ • Consequence: Temporary email outage  │ • Consequence: Chemical explosion, toxic│
│                                        │   gas release, structural metal failure │
└────────────────────────────────────────┴─────────────────────────────────────────┘
```

At Natanz, abruptly cutting power to spinning centrifuges would have dropped them through critical resonance without deceleration control, destroying the cascades anyway. **OT incident response must balance cybersecurity containment with physical safety and thermodynamic stability.**

---

## 2. The 10-Step Modern OT Incident Response Lifecycle

To safely navigate this dilemma, industrial organizations must follow a structured, multi-disciplinary incident lifecycle:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    THE 10-STEP OT INCIDENT RESPONSE MODEL                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   STEP 1: DETECT               Correlate endpoint alerts, network DPI, and      │
│                                physical measurement discrepancies.              │
│                                                                                 │
│   STEP 2: ASSESS SAFETY        Mandatory consultation between Incident          │
│                                Commander, Plant Engineers, and Safety Directors.│
│                                                                                 │
│   STEP 3: SAFE CONTAINMENT     Isolate supervisory networks without terminating │
│                                deterministic Level 1 PLC control loops.         │
│                                                                                 │
│   STEP 4: EVIDENCE PRESERVE    Capture volatile RAM, network PCAPs, and raw     │
│                                PLC controller memory blocks before rebooting.   │
│                                                                                 │
│   STEP 5: VALIDATE TOOLS       Inspect engineering workstations, verify DLL     │
│                                hashes, and inspect `.s7p` project archives.     │
│                                                                                 │
│   STEP 6: VERIFY PHYSICS       Execute independent out-of-band physical checks  │
│                                using analog gauges, strobe tachs, and thermals. │
│                                                                                 │
│   STEP 7: SANITIZE ASSETS      Format and re-image compromised engineering PCs; │
│                                execute PLC memory reset (MRES).                 │
│                                                                                 │
│   STEP 8: TRUSTED RESTORE      Re-flash validated firmware and restore logic    │
│                                from offline, write-protected physical media.    │
│                                                                                 │
│   STEP 9: STAGED STARTUP       Re-commission equipment in controlled stages     │
│                                under continuous, manual engineer supervision.   │
│                                                                                 │
│   STEP 10: ARCHITECT HARDENING Implement data diodes, keyswitch controls, and   │
│                                strict ISA-95 zone and conduit boundaries.       │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Engineering Workstation & PLC Hardening Framework

To ensure that an industrial facility is resilient against Stuxnet-style malware, security teams must enforce four foundational engineering controls:

### 1. The Physical Keyswitch: Hardware-Enforced Write Protection
Siemens S7 PLCs feature a physical, key-operated mode selector switch on the front panel:
* **`RUN-P` (Run-Program):** Allows remote code modification and block downloads over the network.
* **`RUN`:** Executes running logic, but **physically disables all remote program modifications and block downloads** over the backplane and fieldbus!
* **The Rule:** In production, the physical key must be turned to `RUN`, physically removed from the PLC chassis, and locked in a secure key cabinet. No malware can write code to a PLC when the hardware keyswitch is in `RUN`.

```
                    SIEMENS S7 FRONT PANEL KEYSWITCH
                          ┌─────────────────┐
                          │   RUN-P   RUN   │  ◄── Turn key to RUN
                          │    ( )    (*)   │      and remove key!
                          │      STOP       │
                          │       ( )       │
                          └─────────────────┘
```

### 2. Removable Media Scanning Kiosks (Sheep Dip Stations)
All USB flash drives and maintenance laptops must be quarantined at a physical security kiosk before entering the plant:
* Dedicated air-gapped kiosk running multiple independent antivirus and YARA engines.
* Automatic stripping of dangerous file extensions (`.lnk`, `.inf`, `.pif`, `.tmp`, `.scr`).
* Cryptographic conversion: transferring project files to specialized, read-only hardware-encrypted drives.

### 3. Unidirectional Security Gateways (Data Diodes)
To extract SCADA historian data from Level 3 to corporate Level 4 networks without permitting inbound traffic, facilities should deploy **optical data diodes**:
* Data diodes use physical fiber-optic cables with the transmit (TX) LED connected, but the receive (RX) photodiode physically removed.
* Physics guarantees that data can flow outward to corporate servers, but **zero packets, exploits, or commands can physically travel in reverse into the industrial network.**

---

## 4. Establishing Out-of-Band Physical Measurement Verification

To neutralize sensor replay attacks, modern critical infrastructure must maintain an **Independent Safety Instrumented System (SIS)** operating on a completely separate physical layer:

| Dimension | Primary Control System (BPCS) | Independent Safety System (SIS) |
| :--- | :--- | :--- |
| **Purdue Layer** | Level 1 Basic Process Control (S7-315) | Level 1 Safety System (HIMA / Triconex) |
| **Logic Solver** | Standard industrial PLC | Triple Modular Redundant (TMR) Safety PLC |
| **Sensors Used** | Networked Profibus digital transmitters | Hardwired 4-20mA analog current loops |
| **Network Protocol** | S7comm over Ethernet / Profibus | Isolated, non-routable safety bus |
| **Trip Mechanism** | Software ladder logic command | Hardwired electro-mechanical relay trip |
| **Operator Visibility** | WinCC HMI Computer Monitor | Physical backlit annunciator light panel |

If an attacker compromises the primary PLC and attempts to overspeed a motor while replaying false sensor data, the independent safety system detects the true analog current spike and **physically cuts electrical power to the motor**, bypassing the compromised software entirely.

---

## 5. Seminar Discussion Questions

1. **The Human-in-the-Loop:** During an industrial anomaly, if the SCADA screen indicates everything is normal, but a field technician hears an abnormal mechanical whining noise, what standard operating procedure (SOP) governs who has the authority to press the physical Emergency Stop (E-Stop)?
2. **Data Diodes vs. Firewalls:** Why are traditional next-generation firewalls fundamentally inferior to physical data diodes when isolating safety-critical OT enclaves from business networks?
