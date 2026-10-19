# Chapter 04: The Four Zero-Days & Windows Internals

> **Seminar Module:** Vulnerability Exploitation, Kernel Rootkits & Memory Evasion Techniques  
> **Target Audience:** Exploit Developers, Reverse Engineers, Forensic Analysts, Windows Internals Specialists  
> **Core Focus:** Deconstructing the 4 Zero-Day Vulnerabilities & Kernel Evasion Modules

---

## 1. The Weaponry of Stuxnet: An Unprecedented Zero-Day Arsenal

In the history of cybersecurity prior to 2010, encountering a piece of malware that utilized **one** functional zero-day vulnerability was rare. Stuxnet deployed **four distinct, previously unknown Windows zero-day vulnerabilities** simultaneously, alongside a patched remote code execution vulnerability (MS08-067).

In the commercial exploit broker market, assembling an arsenal of four zero-days across remote execution, shell rendering, and kernel privilege escalation represents millions of dollars in research and development capital.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       STUXNET'S FOUR ZERO-DAY EXPLOITS                          │
├───────────────────┬───────────────────────────┬─────────────────────────────────┤
│   CVE IDENTIFIER  │     VULNERABLE MODULE     │        EXPLOIT FUNCTION         │
├───────────────────┼───────────────────────────┼─────────────────────────────────┤
│ 1. CVE-2010-2568  │ Windows Shell (`shell32`) │ Zero-Click Remote Execution     │
│                   │ LNK Shortcut Parsing      │ via USB icon rendering          │
├───────────────────┼───────────────────────────┼─────────────────────────────────┤
│ 2. CVE-2010-2729  │ Windows Print Spooler     │ Remote Code Execution via RPC   │
│                   │ (`spoolsv.exe`)           │ for lateral propagation         │
├───────────────────┼───────────────────────────┼─────────────────────────────────┤
│ 3. CVE-2010-3338  │ Windows Task Scheduler    │ Local Privilege Escalation      │
│                   │ (`taskschd.dll`)          │ from standard user to SYSTEM    │
├───────────────────┼───────────────────────────┼─────────────────────────────────┤
│ 4. CVE-2010-2743  │ Windows Graphics Driver   │ Kernel-Level Memory Corruption  │
│                   │ (`win32k.sys` / User32)   │ Privilege Escalation to ring-0  │
└───────────────────┴───────────────────────────┴─────────────────────────────────┘
```

---

## 2. Technical Deconstruction of the Exploits

### 1. CVE-2010-2568: Windows Shell LNK Vulnerability
* **Vulnerable Component:** `shell32.dll`
* **Mechanism:** When Windows Explorer displays an icon for a shortcut file (`.lnk`), it parses the file format to locate the referenced icon resource. If the icon location is an arbitrary dynamic link library (`.dll`), Windows calls `LoadLibraryW()` on that file path.
* **Exploitation:** Stuxnet crafted `.lnk` files where the icon resource pointed directly to its own malicious export loader `~WTR4141.tmp`. The moment Explorer enumerated the drive directory, the operating system loaded and executed Stuxnet's code in the context of `explorer.exe` without any user interaction.

### 2. CVE-2010-2729: Windows Print Spooler Remote Code Execution
* **Vulnerable Component:** `spoolsv.exe` (Print Spooler Service)
* **Mechanism:** The Windows Print Spooler RPC interface (`MS-RPRN`) permitted remote clients to send print jobs to shared network printers. A boundary validation flaw in `spoolsv.exe` allowed an attacker to write arbitrary files into `%System32%`.
* **Exploitation:** Stuxnet connected to the remote target's Print Spooler service over RPC (port 445/139), sent a malformed print request containing its payload, and caused the remote system to drop and execute its driver directly with `NT AUTHORITY\SYSTEM` privileges.

### 3. CVE-2010-3338: Task Scheduler Privilege Escalation
* **Vulnerable Component:** `taskschd.dll` (Windows Task Scheduler 2.0 on Windows Vista/7)
* **Mechanism:** On Windows Vista and Windows 7, standard non-administrative users could create scheduled tasks, but the service failed to properly validate the memory structures associated with task security descriptors.
* **Exploitation:** Stuxnet injected a corrupt task definition file into `\Windows\System32\Tasks`, resulting in an integer overflow that overwrote function pointers in memory, elevating the process from a limited user token to `NT AUTHORITY\SYSTEM`.

### 4. CVE-2010-2743: Win32k.sys TrueType Keyboard Layout Escalation
* **Vulnerable Component:** `win32k.sys` (Kernel-Mode Graphics Driver)
* **Mechanism:** A kernel memory corruption flaw existed in the way `win32k.sys` handled window message parameters and keyboard layout conversions.
* **Exploitation:** Stuxnet triggered a NULL-dereference and index out-of-bounds write in kernel memory, flipping security tokens in the EPROCESS block to escalate code execution to ring-0 kernel mode.

---

## 3. In-Memory Injection and Process Hollowing

Stuxnet took extraordinary precautions to avoid creating suspicious processes that could alert system administrators viewing Windows Task Manager. It executed almost entirely inside legitimate, trusted system processes:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    STUXNET IN-MEMORY INJECTION PIPELINE                         │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   1. Initial Loader executes in `explorer.exe` via .LNK exploit.                │
│   2. Injects reflective loader into `services.exe` and `lsass.exe`.             │
│   3. Unhooks System DLLs: Stuxnet detects user-mode hooks placed by antivirus   │
│      products in `ntdll.dll` and restores clean original memory bytes.          │
│   4. Allocates virtual memory sections in `svchost.exe` using `VirtualAllocEx`. │
│   5. Copies decrypted payload modules and resolves imports dynamically.         │
│   6. Diverts thread execution to payload entry point using `SetThreadContext`.  │
│                                                                                 │
│   RESULT: No malicious .EXE appears in the process list. All malicious code     │
│   runs under the guise of legitimate Windows operating system daemons.          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Kernel-Mode Rootkits: Hiding Files and Drivers

To remain completely invisible to local disk scans and user queries, Stuxnet deployed two specialized kernel-mode filter drivers signed with the stolen Realtek and JMicron certificates:

```
                          WINDOWS KERNEL STORAGE STACK
                                        │
           ┌────────────────────────────┴────────────────────────────┐
           ▼                                                         ▼
    [mrxnet.sys Rootkit]                                      [mrxcls.sys Rootkit]
    Signed by: Realtek Semiconductor                          Signed by: JMicron Technology
    Hook: `\FileSystem\Fastfat` & `\FileSystem\Ntfs`         Hook: Windows Device / Class Filters
    ────────────────────────────────────────────              ────────────────────────────────────
    • Intercepts `IRP_MJ_DIRECTORY_CONTROL` queries.          • Injected during system startup.
    • Scans file enumeration buffers.                         • Handles encrypted payload loading
    • Hides all files matching:                                 and memory protection.
      - `~WTR4141.tmp`                                        • Neutralizes legacy forensic tools.
      - `~WTR4132.tmp`
      - `*.lnk`
```

If an engineer at Natanz inserted an infected USB drive into a workstation and opened a command prompt to run `dir E:\`, the `mrxnet.sys` rootkit intercepted the I/O Request Packet (IRP) in kernel space, stripped the malicious filenames from the returned data structure, and presented a clean directory. To the human user, the flash drive appeared completely empty.

---

## 5. Self-Imposed Kill Switches and Safeguards

A critical indicator of Stuxnet's military-grade lineage was its inclusion of strict programmatic **self-restraint mechanisms** designed to limit uncontrolled collateral damage:

1. **The Infection Cap (3 Infections per USB):** Stuxnet wrote a counter into the header of the flash drive. It would only replicate from a given USB drive to a maximum of **three machines**, after which it automatically deactivated USB propagation to avoid exponential wildfire spreading.
2. **The Hardcoded Expiration Kill-Switch:** Stuxnet was coded with a suicide date: **June 24, 2012**. After this timestamp, the worm completely ceased propagation and deactivated its operational modules.
3. **Antivirus Neutralization Protocols:** Stuxnet actively enumerated installed security software:
   * If **Kaspersky Antivirus** was detected, it utilized a specialized injection technique using memory sections.
   * If other AV engines were detected, it adjusted its memory allocation to avoid triggering heuristic behavioral scanners.

---

## 6. Seminar Discussion Questions

1. **The Lifetime of Zero-Days:** Why would the authors of Stuxnet "burn" four exceptionally valuable zero-day vulnerabilities in a single operation, and what does that reveal about the strategic priority of delaying Iran's nuclear enrichment?
2. **User-Mode vs. Kernel-Mode Evasion:** If modern EDR agents utilize kernel callbacks (`PsSetCreateProcessNotifyRoutine`), how did Stuxnet's signed drivers successfully evade detection in 2010?
