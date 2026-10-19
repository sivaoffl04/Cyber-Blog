# Chapter 02: Industrial Architecture & The Purdue Model

> **Seminar Module:** Operational Technology (OT) Architectures, Industrial Networking & SCADA Fundamentals  
> **Target Audience:** Control Systems Engineers, Security Architects, SOC Analysts Transitioning to OT  
> **Key Frameworks:** ISA-95 / Purdue Enterprise Reference Architecture (PERA), Siemens S7 Architecture

---

## 1. Deconstructing the Purdue Enterprise Reference Architecture (PERA)

To understand how malware operating inside a standard Microsoft Windows environment can manipulate heavy physical machinery, cybersecurity professionals must master the **Purdue Model (ISA-95)**.

The Purdue Model segments industrial manufacturing environments into hierarchical logical zones, separating corporate enterprise business networks from physical plant floor processes.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│              PURDUE ENTERPRISE REFERENCE ARCHITECTURE (ISA-95)                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LEVEL 5: Enterprise Corporate Network (ERP, Business Email, Internet Gateway)   │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LEVEL 4: Site Business Logistics (Plant Scheduling, MES, Work Orders)           │
├═════════════════════════════════════════════════════════════════════════════════┤
│                    INDUSTRIAL DEMILITARIZED ZONE (IDMZ)                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LEVEL 3: Plant Operations & Supervisory Control                                 │
│          • SCADA Servers (Siemens SIMATIC WinCC Central Servers)                │
│          • Engineering Workstations (Siemens SIMATIC STEP 7 IDE)                │
│          • Plant Historian (Process Log Databases)                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LEVEL 2: Area Supervisory Control & Operator Terminals                          │
│          • Local Human-Machine Interfaces (WinCC HMI Panels)                    │
│          • Operator Control Desks & Alarm Consoles                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LEVEL 1: Basic Process Control Layer (THE PROGRAMMABLE LOGIC CONTROLLER)        │
│          • Siemens SIMATIC S7-315-2AG10-0AB0 PLCs (Centrifuge Speed Logic)      │
│          • Siemens SIMATIC S7-417-4HL01-0AB0 PLCs (Cascade Pressure & Valves)   │
│          • Profibus DP / MPI Industrial Fieldbus Networks                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│ LEVEL 0: Physical Process & Field Devices                                       │
│          • Variable Frequency Drives (Fararo Paya & Vacon Inverters)            │
│          • Centrifuge 3-Phase Electric Motors & Rotating Aluminum Cylinders     │
│          • Uranium Hexafluoride (UF6) Gas Isolation Valves & Vacuum Gauges      │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Hardware Architecture: Mapping the Natanz Plant Network

Stuxnet's authors possessed an extraordinarily intimate, blueprint-level understanding of the physical and network topology inside the Natanz Fuel Enrichment Plant.

![Stuxnet SCADA PLC Network Architecture](image/stuxnet_scada_plc_network_architecture.jpg)
*Figure 2.1: The multi-tiered industrial network architecture at Natanz: from SCADA WinCC operator terminals down to Siemens S7-300 and S7-400 PLCs and centrifuge cascades.*

```
                       NATANZ ENRICHMENT NETWORK TOPOLOGY
                       
     [Infected USB]
           │
           ▼
  ┌─────────────────┐       ┌─────────────────┐
  │ WinCC Terminal  │       │ WinCC Terminal  │       [LEVEL 2: SCADA HMI]
  │   (Operator 1)  │       │   (Operator 2)  │
  └────────┬────────┘       └────────┬────────┘
           │                         │
           └────────────┬────────────┘
                        │ Ethernet / Industrial TCP/IP
                        ▼
           ┌────────────────────────┐
           │ Industrial Core Switch │
           └────────────┬───────────┘
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
  ┌──────────────┐              ┌──────────────┐
  │ WinCC Server │◄────(MPI)───►│ WinCC Server │      [LEVEL 3: SUPERVISORY]
  │   (Active)   │              │   (Standby)  │
  └──────┬───────┘              └──────┬───────┘
         │                             │
         └──────────────┬──────────────┘
                        │ Profibus DP (RS-485 Fieldbus)
                        ▼
         ┌─────────────────────────────┐
         │ Siemens CP 342-5 Comm Card  │
         └──────────────┬──────────────┘
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
  ┌──────────────┐              ┌──────────────┐
  │ Siemens S7-  │              │ Siemens S7-  │      [LEVEL 1: CONTROLLERS]
  │ 315-2AG10    │              │ 417-4HL01    │
  │ (VFD Speed)  │              │ (Gas Valves) │
  └──────┬───────┘              └──────┬───────┘
         │                             │
         ▼                             ▼
  ┌──────────────┐              ┌──────────────┐
  │ Fararo Paya/ │              │ Fast-Acting  │      [LEVEL 0: FIELD DEVICES]
  │ Vacon VFDs   │              │ Valves &     │
  └──────┬───────┘              │ Manifolds    │
         │                             │
         ▼                             ▼
  ┌────────────────────────────────────────────┐
  │  164 IR-1 Centrifuges in 18-Stage Cascade  │      [LEVEL 0: PHYSICAL PROCESS]
  └────────────────────────────────────────────┘
```

---

## 3. Deep Dive: Key Operational Technology Components

### 1. The Engineering Workstation (Level 3)
* **Operating System:** Microsoft Windows XP Professional SP2 / SP3 or Windows 2000.
* **Engineering IDE:** **Siemens SIMATIC STEP 7** (versions 5.4 through 5.5).
* **Role:** The engineering workstation is the central development environment where automation engineers write, compile, and upload logic to PLCs. STEP 7 uses **Statement List (STL)**, **Ladder Logic (LAD)**, or **Function Block Diagram (FBD)** programming languages, compiling user logic into proprietary **MC7 bytecode**.

### 2. The Supervisory Control and Data Acquisition System (SCADA / HMI - Level 2 & 3)
* **Software:** **Siemens SIMATIC WinCC** (Windows Control Center).
* **Role:** WinCC aggregates sensor readings (rotational RPM, casing temperatures, cascade inlet/outlet gas pressures) into graphical human-machine interface (HMI) dashboards. Control room operators sit in front of WinCC monitors to monitor alarms and supervise enrichment operations.

### 3. The Programmable Logic Controller (PLC - Level 1)
A PLC is a ruggedized, microprocessor-based industrial computer designed for deterministic, real-time control of mechanical equipment under harsh physical conditions.
* **Siemens SIMATIC S7-315:** A compact, modular controller utilizing the **6ES7-315-2AG10-0AB0** CPU. In Natanz, these PLCs were assigned to regulate the frequency converter drives that controlled centrifuge rotational speed.
* **Siemens SIMATIC S7-417:** A high-performance, fault-tolerant industrial controller utilizing the **6ES7-417-4HL01-0AB0** CPU. In Natanz, these PLCs controlled the gas valves, isolation manifolds, and pressure sensor arrays across 18 cascade stages.

### 4. Variable Frequency Drives (VFDs) / Frequency Converters (Level 0)
An electric motor's rotational speed is directly proportional to the frequency of the alternating current (AC) electricity supplied to it:
$$\text{Speed (RPM)} = \frac{120 \times \text{Frequency (Hz)}}{\text{Number of Motor Poles}}$$
For a 2-pole centrifuge motor operating at $1,064\text{ Hz}$:
$$\text{Speed} = \frac{120 \times 1,064}{2} = 63,840\text{ RPM}$$
The frequency converters utilized at Natanz were manufactured by two specific vendors:
1. **Fararo Paya** (Tehran, Iran)
2. **Vacon** (Vaasa, Finland)

Stuxnet specifically monitored the communications bus for the vendor-specific hardware IDs of Fararo Paya and Vacon drives before unleashing its attack sequences.

---

## 4. Architectural Analysis: Why Traditional Firewalls Failed

Security planners at Natanz believed their facility was immune to cyberattack because they enforced a **physical air gap** between the plant and the external world. No network cables connected the centrifuge cascades to the internet.

However, the Purdue Model reveals the fatal flaw in static perimeter defense:
* Software on Level 3 Engineering Workstations does not update itself; engineers must plug in diagnostic laptops or USB storage drives to install patches, project updates, and firmware.
* Third-party contractors responsible for installing, calibrating, and servicing Siemens equipment carried laptops and USB drives between their home offices and the centrifuge halls.
* **The air gap was a physical barrier to network packets, but it was completely transparent to physical media.**

---

## 5. Seminar Discussion Questions

1. **The Purdue Model Boundary:** Where does the boundary between "IT security" and "OT safety" sit in the Purdue hierarchy, and why do IT security tools like traditional antivirus struggle at Level 1 and Level 0?
2. **Fieldbus Vulnerabilities:** Protocols like Profibus, Modbus, and standard S7comm lack built-in cryptographic authentication and encryption. How did Stuxnet exploit the trust relationship between Level 3 workstations and Level 1 PLCs?
