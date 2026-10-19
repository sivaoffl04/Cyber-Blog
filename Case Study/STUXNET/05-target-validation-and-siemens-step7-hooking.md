# Chapter 05: Target Validation & Siemens STEP 7 Hooking

> **Seminar Module:** Industrial Man-in-the-Middle (MitM) Attacks, DLL Proxying & PLC Firmware Hooking  
> **Target Audience:** ICS Engineers, Protocol Analysts, Reverse Engineers, Forensic Investigators  
> **Core Architecture:** Siemens S7 Communication (`s7otbxdx.dll`), MC7 Bytecode Injection, Environmental Fingerprinting

---

## 1. The Selectivity Engine: Why Stuxnet Remained Dormant

The most dangerous misconception about Stuxnet was that it was an indiscriminate cyber weapon designed to destroy any industrial facility it entered.

In reality, **Stuxnet was the most selective malware in human history**. Although it infected over 100,000 corporate endpoints across Iran, Indonesia, India, and the United States, its destructive industrial payload executed in **only one location on Earth: the Natanz Fuel Enrichment Plant.**

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    STUXNET'S MULTI-GATE TARGET VALIDATION                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   GATE 1: OPERATING SYSTEM CHECK                                                │
│   • Is the system running a 32-bit Windows NT platform (2000, XP, 2003)?        │
│     NO ──► Exit / Sleep.                                                        │
│     YES ──► Proceed to Gate 2.                                                  │
│                                                                                 │
│   GATE 2: SIEMENS INDUSTRIAL SOFTWARE ENUMERATION                               │
│   • Is Siemens SIMATIC STEP 7 or SIMATIC WinCC installed?                       │
│     NO ──► Sleep / Spread only.                                                 │
│     YES ──► Proceed to Gate 3.                                                  │
│                                                                                 │
│   GATE 3: PLC HARDWARE PROFILE RECONNAISSANCE                                   │
│   • Does the connected PLC match CPU: 6ES7-315-2AG10-0AB0 or 6ES7-417-4HL01?   │
│     NO ──► Stand down. Do not inject PLC.                                       │
│     YES ──► Proceed to Gate 4.                                                  │
│                                                                                 │
│   GATE 4: FIELDBUS COMMUNICATIONS PROCESSOR VALIDATION                          │
│   • Is the PLC connected to a Siemens CP 342-5 Profibus communications module?  │
│     NO ──► Stand down.                                                          │
│     YES ──► Proceed to Gate 5.                                                  │
│                                                                                 │
│   GATE 5: VARIABLE FREQUENCY DRIVE (VFD) HARDWARE ID MATCH                      │
│   • Are exactly 33 frequency converters responding with vendor IDs:             │
│     0x7050 (Fararo Paya, Iran) or 0x0100 (Vacon, Finland)?                      │
│     NO ──► Stand down. Remain 100% dormant.                                     │
│     YES ──► [TARGET CONFIRMED: NATANZ CASCADE DETECTED]                         │
│             UNLEASH PLC SABOTAGE PAYLOAD.                                       │
└─────────────────────────────────────────────────────────────────────────────────┘
```

If even a single check in this chain failed, Stuxnet refrained from touching the PLC. It operated purely as an invisible reconnaissance agent, ensuring it would not accidentally disrupt water filtration plants, chemical refineries, or pharmaceutical factories.

---

## 2. The Man-in-the-Middle (MitM) DLL Proxy Attack

To interact with Siemens PLCs, an automation engineer runs **SIMATIC STEP 7** on an engineering workstation. STEP 7 communicates with PLCs over the network using Siemens' proprietary industrial protocol: **S7comm** (running over ISO-on-TCP port 102).

In standard installations, all reading, writing, and compilation of PLC code is handled by a core Siemens dynamic link library:
`%CommonProgramFiles%\Siemens\S7Common\s7otbxdx.dll`

Stuxnet executed a flawless, classic **DLL Proxying / Search Order Hijacking** attack to position itself as a stealthy man-in-the-middle broker between the engineer and the controller:

![Step 7 DLL Proxy Architecture](image/stuxnet_step7_dll_proxy_architecture.jpg)
*Figure 5.1: The Stuxnet DLL proxying architecture: replacing s7otbxdx.dll and hooking block read/write functions to hide malicious PLC code.*

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│               SIEMENS STEP 7 S7OTBXDX.DLL HIJACKING MECHANICS                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   1. Stuxnet locates original Siemens communication library: `s7otbxdx.dll`.    │
│   2. Stuxnet renames original file to: `s7otbxsx.dll` ("s" replaces "d").       │
│   3. Stuxnet drops its malicious wrapper DLL and names it: `s7otbxdx.dll`.      │
│   4. Stuxnet exports all 109 original Siemens API function calls:               │
│      • 93 benign functions pass through untouched to `s7otbxsx.dll`.            │
│      • 16 critical block read/write functions are intercepted by Stuxnet!       │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Hooking the S7comm Protocol: Intercepting Block Operations

By hooking the 16 critical functions inside `s7otbxdx.dll`, Stuxnet gained absolute control over every block of code transmitted between the engineering software and the physical PLC:

| Hooked Function | Normal Function Purpose | Stuxnet Malicious Interception |
| :--- | :--- | :--- |
| **`s7blk_write`** | Writes user logic blocks from STEP 7 into PLC memory. | Intercepts block write; injects malicious Organization Blocks (`OB1`, `OB35`) and Data Blocks (`DB89`). |
| **`s7blk_read`** | Reads code blocks from PLC back to engineer's screen. | Intercepts block read; strips malicious code blocks in memory and returns pristine original code! |
| **`s7blk_delete`** | Deletes a specified block from PLC memory. | Prevents user from deleting injected malicious blocks. |
| **`s7blk_findfirst`** | Enumerates blocks installed on the PLC. | Alters block enumeration results to hide injected Stuxnet blocks. |
| **`s7blk_findnext`** | Continues block enumeration. | Continues hiding malicious blocks from the catalog list. |

---

## 4. Deceiving the Human Engineer: Complete Code Cloaking

The genius of this architecture was its psychological and forensic perfection.

Imagine an Iranian automation engineer at Natanz suspecting that something is wrong with a centrifuge cascade:
1. The engineer opens **SIMATIC STEP 7** on the engineering laptop.
2. The engineer clicks **"Upload Station to PG"** to fetch the live running code directly from the Siemens S7-315 controller.
3. STEP 7 calls `s7blk_read` to retrieve the bytecode from the PLC.
4. **Stuxnet's hooked DLL intercepts the response.** It inspects the incoming MC7 bytecode blocks, removes its own malicious subroutines, reconstructs the original checksums, and feeds the clean original code to the STEP 7 GUI.
5. The engineer looks at the screen, sees standard, legitimate Ladder Logic, and concludes: *"The controller program is 100% clean. The centrifuges must be failing due to bad aluminum metallurgy or mechanical friction!"*

```
REALITY:             [Malicious Stuxnet Bytecode Running Inside PLC Memory]
                                       │
                                       ▼ (Intercepted by Hooked DLL)
DISPLAYED TO USER:   [Clean Original Logic Displayed in Siemens STEP 7 GUI]
```

Stuxnet was not merely a malware program; it was a **two-way perceptual filter** that manipulated physical reality while maintaining an illusion of perfection in the software domain.

---

## 5. Seminar Discussion Questions

1. **Protocol Integrity:** Why did the S7comm protocol lack cryptographic message authentication codes (HMACs), and how do modern protocols like S7comm-Plus or secure CIP protect against DLL proxying?
2. **Offline PLC Verification:** If the engineering software running on Windows cannot be trusted to report the true state of a controller, how can an incident responder extract and verify the authentic firmware and logic of an industrial PLC?
