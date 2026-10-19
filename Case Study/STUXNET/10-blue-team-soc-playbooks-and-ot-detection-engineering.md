# Chapter 10: Blue Team SOC Playbooks & OT Detection Engineering

> **Seminar Module:** Network Telemetry Inspection, Industrial Protocol Rules & SIEM Detection Engineering  
> **Target Audience:** Detection Engineers, SOC Lead Analysts, OT Security Engineers, Incident Responders  
> **Rules & Signatures:** Suricata (S7comm), Zeek, Splunk SPL & YARA

---

## 1. Detection Engineering Principles for Industrial Control Systems

Building detection rules for an Operational Technology (OT) network requires a fundamentally different philosophy than enterprise IT:
* **Protocol Rigidity:** In industrial networks, communication is highly deterministic. A PLC communicates with the exact same engineering workstation every day, using the exact same function codes, at the exact same intervals.
* **Zero Normal Program Downloads:** In a production facility, PLC programming blocks are **almost never updated** outside of scheduled, annual maintenance shutdowns. Any unauthorized `s7blk_write` or block download command occurring on ISO-on-TCP port 102 during normal operations is a **Defcon 1 Critical Alert**.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    OT INDUSTRIAL TELEMETRY CORRELATION                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   [WINDOWS ENDPOINT / EDR]                                                      │
│   • Detection: File creation `s7otbxsx.dll` in Siemens directory                │
│   • Detection: Hash mismatch on `s7otbxdx.dll`                                  │
│                                  │                                              │
│                                  ▼                                              │
│   [INDUSTRIAL NETWORK TAP / SURICATA]                                           │
│   • Detection: S7comm Function 0x1A (Download Block) to PLC S7-315              │
│   • Detection: Block Type = OB1 / OB35 / DB89                                   │
│                                  │                                              │
│                                  ▼                                              │
│   [PHYSICAL SENSOR HISTORIAN]                                                   │
│   • Anomaly: Frequency Converter output deviates from 1,064 Hz steady state     │
│                                  │                                              │
│                                  ▼                                              │
│             [HIGH-FIDELITY CYBER-PHYSICAL ATTACK ALERT]                         │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Industrial Protocol Detection: Suricata S7comm Rules

The following Suricata network intrusion detection rules monitor ISO-on-TCP port 102 traffic for unauthorized Siemens S7 communication events:

```suricata
# Rule 1: Detect S7comm Unauthorized Block Download / Write to PLC
alert tcp any any -> any 102 (
    msg:"OT-ATTACK Stuxnet-Style S7comm Block Write / Download Command";
    flow:to_server,established;
    content:"|03 00|"; depth:2;                 # TPKT Header (ISO-on-TCP)
    content:"|02 f0 80|"; distance:2; within:3;  # ISO-COTP Connection
    content:"|32|"; distance:0; within:1;        # S7comm Protocol Identifier (0x32)
    content:"|1a|"; distance:8; within:2;        # Function Code 0x1A: Request Download Block
    classtype:industrial-control-compromise;
    sid:1000801;
    rev:1;
    metadata:mitre_ics T0843, Purdue_Level Level_1;
)

# Rule 2: Detect S7comm Unauthorized PLC CPU Stop Command
alert tcp any any -> any 102 (
    msg:"OT-ATTACK S7comm PLC CPU Stop Execution Command";
    flow:to_server,established;
    content:"|32 01|";                           # S7comm Header (Job Request)
    content:"|29|"; distance:8; within:2;        # Function Code 0x29: CPU Stop
    classtype:industrial-control-compromise;
    sid:1000802;
    rev:1;
    metadata:mitre_ics T0804, Purdue_Level Level_1;
)
```

---

## 3. Production Splunk SPL Queries

### Rule 1: Siemens STEP 7 DLL Replacement Anomaly
Detects the renaming of the legitimate Siemens communication library to `s7otbxsx.dll` or the replacement of `s7otbxdx.dll` with an untrusted binary.

```spl
index=endpoint sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=11
| eval file_name = lower(TargetFilename)
| where match(file_name, ".*\\\\siemens\\\\s7common\\\\s7otbx[d|s]x\.dll$")
| stats earliest(_time) as first_seen, latest(_time) as last_seen, count by host, Image, file_name
| eval alert_type=if(match(file_name, "s7otbxsx\.dll$"), "LEGITIMATE_DLL_RENAMED", "HOOKED_DLL_DROPPED")
| table host, Image, file_name, alert_type, first_seen, last_seen
```

---

### Rule 2: Windows Shell LNK Zero-Day Exploitation (CVE-2010-2568)
Detects Windows Explorer loading executable libraries (`.tmp` or `.dll`) directly from removable media root directories upon folder enumeration.

```spl
index=endpoint sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=7
| eval loaded_module = lower(ImageLoaded)
| eval process_name = lower(Image)
| where match(process_name, ".*\\\\explorer\.exe$")
| where match(loaded_module, "^[d-z]:\\\\~wtr\d+\.tmp$") OR match(loaded_module, "^[d-z]:\\\\.*\.dll$")
| table _time, host, process_name, loaded_module, Signed, SignatureStatus
```

---

### Rule 3: Print Spooler Lateral Code Execution (CVE-2010-2729)
Detects the Windows Print Spooler service (`spoolsv.exe`) writing executable files to system directories or spawning child processes.

```spl
index=endpoint sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" (EventCode=1 OR EventCode=11)
| eval parent_proc = lower(ParentImage)
| eval process_img = lower(Image)
| where match(parent_proc, ".*\\\\spoolsv\.exe$")
| search process_img!="*\\printconfig.dll"
| table _time, host, EventCode, parent_proc, process_img, CommandLine
```

---

## 4. Production YARA Signatures

### Signature 1: Stuxnet S7 Hooking Library (`s7otbxdx.dll`)
```yara
rule Stuxnet_Siemens_S7_Hooking_DLL {
    meta:
        description = "Detects the malicious hooked s7otbxdx.dll used by Stuxnet"
        author = "Cyber-Blog Threat Intelligence Team"
        reference = "https://www.cisa.gov/uscert/ics/advisories/ICSA-10-272-01"
        date = "2026-10-19"
        hash = "4020a65cf23381e4b9f2eb430d41829e"
    strings:
        $export1 = "s7blk_read" fullword ascii
        $export2 = "s7blk_write" fullword ascii
        $export3 = "s7blk_delete" fullword ascii
        $renamed = "s7otbxsx.dll" fullword ascii wide
        $s7_code = { 8B 45 ?? 50 FF 15 ?? ?? ?? ?? 85 C0 74 ?? 8B 4D ?? E8 }
    condition:
        uint16(0) == 0x5A4D and
        pe.exports("s7blk_read") and
        pe.exports("s7blk_write") and
        $renamed and
        filesize < 1MB
}
```

---

### Signature 2: Realtek Stolen Code-Signing Certificate Driver
```yara
rule Stuxnet_Signed_Kernel_Driver_Realtek {
    meta:
        description = "Detects kernel drivers signed with the compromised Realtek Semiconductor certificate"
        author = "Cyber-Blog Threat Intelligence Team"
        date = "2026-10-19"
    strings:
        $driver_name = "mrxnet.sys" fullword ascii wide
        $magic_val   = { 8B 44 24 04 89 41 08 C7 01 00 00 00 00 33 C0 C2 04 00 }
        $cert_owner  = "Realtek Semiconductor Corp." ascii wide
    condition:
        uint16(0) == 0x5A4D and
        ($driver_name or $magic_val) and
        $cert_owner
}
```

---

## 5. SOC Playbook 1: Removable Media Incident in Air-Gapped Network

```
┌─────────────────────────────────────────────────────────────────────────────┐
│             SOC PLAYBOOK 1: AIR-GAPPED USB MALWARE INCIDENT                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [TRIGGER]                                                                  │
│  • Endpoint EDR or host log alerts on `.tmp` file creation on removable drive.│
│  • Sysmon Event ID 7: `explorer.exe` loads unsigned DLL from USB drive.     │
│                                                                             │
│  [TRIAGE CHECKLIST]                                                         │
│  1. Identify Physical Machine & Location:                                   │
│     Locate the specific engineering workstation, cabinet, and Purdue zone.  │
│  2. Identify the Human Operator:                                            │
│     Which contractor or technician plugged in the USB device?               │
│  3. Physical Media Quarantine:                                              │
│     Immediately unplug and bag the USB flash drive in a Faraday enclosure.  │
│  4. Inspect Connected PLCs:                                                 │
│     Query the connected Siemens S7-315 / S7-417 PLCs:                        │
│     Has `s7blk_write` occurred in the last 24 hours?                        │
│                                                                             │
│  [CONTAINMENT ACTIONS]                                                      │
│  • DO NOT REBOOT WORKSTATION: Capture live volatile memory (RAM).           │
│  • Sever local fieldbus / Profibus cable to PLCs if process is stable.      │
│  • Compare live PLC checksum against pristine offline baseline copy.        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. SOC Playbook 2: PLC Logic Anomaly & Unauthorized Firmware Hunt

```
┌─────────────────────────────────────────────────────────────────────────────┐
│             SOC PLAYBOOK 2: PLC LOGIC INTEGRITY ANOMALY HUNT                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [TRIGGER]                                                                  │
│  • Physical process measurement deviates from SCADA HMI displayed telemetry.│
│  • Network TAP identifies unexpected ISO-on-TCP (port 102) block download.  │
│                                                                             │
│  [TRIAGE CHECKLIST]                                                         │
│  1. Independent Physical Telemetry Validation:                              │
│     Dispatch technician with hand-held analog strobe tachometer to measure  │
│     actual motor shaft speed independently of SCADA.                        │
│  2. Hardware-Level Memory Dump:                                             │
│     Extract PLC memory using clean, air-gapped programming console          │
│     running a verified, hash-checked instance of STEP 7.                    │
│  3. Bytecode Diff Analysis:                                                 │
│     Execute MC7 bytecode disassembly diff:                                  │
│     Check for injected Organization Blocks: `OB1`, `OB35`, `DB89`.          │
│                                                                             │
│  [REMEDIATION & RECOVERY]                                                   │
│  • Execute PLC Cold Restart / Factory Memory Reset (MRES).                  │
│  • Re-flash validated clean firmware from vendor optical media.             │
│  • Re-upload authenticated program blocks from offline vault.               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Seminar Discussion Questions

1. **Protocol Limitations:** Why are traditional IT network intrusion detection systems (NIDS) blind to S7comm block injections unless specifically equipped with deep packet inspection (DPI) parsers for industrial fieldbuses?
2. **The Problem of In-Memory Malware:** If a PLC executes its logic entirely in volatile RAM without saving files to a file system, how can digital forensic investigators acquire a forensically sound memory dump of a running Siemens controller?
