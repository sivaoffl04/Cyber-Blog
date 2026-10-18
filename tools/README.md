# 🧰 Cybersecurity Tool Masterclasses & Open-Source Ecosystem

Welcome to the **Cybersecurity Tool Masterclasses** repository section. Rather than basic command cheat sheets, each guide in this directory provides a comprehensive, production-grade operational reference covering underlying protocol architecture, hardware acceleration mechanics, real-world attack tradecraft, detection engineering (SIEM/Sigma), and enterprise defensive hardening.

Every tool featured below is paired with its **official project domain** and **official open-source GitHub repository** for source code auditing, compilation, and issue tracking.

---

## 📚 Masterclass & Open-Source Tool Ecosystem Index

| Tool | Category | 🌐 Official Domain | 🐙 Open-Source GitHub | Hardware / Protocols | 📖 Course Link |
| :--- | :--- | :---: | :---: | :--- | :---: |
| **Nmap** (Network Mapper) | Network Reconnaissance & Port Scanning | [nmap.org](https://nmap.org/) | [nmap/nmap](https://github.com/nmap/nmap) | TCP, UDP, SCTP, Raw IP Sockets, Lua NSE | [Nmap Masterclass](./Nmap/README.md) |
| **John the Ripper** (JtR) | Password Cracking & Cryptanalysis | [openwall.com/john](https://www.openwall.com/john/) | [openwall/john](https://github.com/openwall/john) | CPU (Multi-core), SIMD, AVX-512, OpenCL | [John the Ripper Masterclass](./John%20the%20ripper/README.md) |
| **Hashcat** | High-Performance Password Recovery | [hashcat.net](https://hashcat.net/hashcat/) | [hashcat/hashcat](https://github.com/hashcat/hashcat) | GPU (CUDA, ROCm, OpenCL), PCIe, Tensor Cores | [Hashcat Masterclass](./Hashcat/README.md) |
| **Aircrack-ng** | Wireless Security & 802.11 Auditing | [aircrack-ng.org](https://www.aircrack-ng.org/) | [aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) | 802.11 a/b/g/n/ac/ax, RF Channels, WPA2/WPA3 | [Aircrack-ng Masterclass](./Aircrack-ng/README.md) |
| **Kerberos** (AD Identity Suite) | Network Authentication & AD Security | [web.mit.edu/kerberos](https://web.mit.edu/kerberos/) & [Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview) | [GhostPack/Rubeus](https://github.com/GhostPack/Rubeus) & [fortra/impacket](https://github.com/fortra/impacket) | Kerberos V5 (RFC 4120), RC4 / AES, LDAP, Event 4769 | [Kerberos Masterclass](./Kerberos/README.md) |
| **Metasploit** (Exploit Framework) | Penetration Testing & Exploit Verification | [metasploit.com](https://www.metasploit.com/) & [docs](https://docs.metasploit.com/) | [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework) | Exploits, Auxiliary, Meterpreter, Post, msfvenom | [Metasploit Masterclass](./Metasploit/README.md) |


---

## 🛠️ Tool Masterclass Highlights & Official Source Portals

### 1. [Nmap — Complete Network Reconnaissance Masterclass](./Nmap/README.md)
* **🌐 Official Project Domain:** [https://nmap.org](https://nmap.org/)
* **🐙 Official Open-Source GitHub:** [https://github.com/nmap/nmap](https://github.com/nmap/nmap)
* **What You'll Learn:** Low-level TCP three-way handshakes, SYN vs Connect vs FIN/Xmas/Null scans, OS fingerprinting heuristics, writing custom Lua scripts for the Nmap Scripting Engine (NSE), and bypassing stateful firewalls with fragmentation and decoys.
* **Key Artifacts:** Detailed packet exchange sequence diagrams, live scan demonstration GIF, and port state decision matrix.

### 2. [John the Ripper — Advanced Password Cryptanalysis Masterclass](./John%20the%20ripper/README.md)
* **🌐 Official Project Domain:** [https://www.openwall.com/john/](https://www.openwall.com/john/)
* **🐙 Official Open-Source GitHub:** [https://github.com/openwall/john](https://github.com/openwall/john)
* **What You'll Learn:** Linux `/etc/shadow` and Windows NTLM auditing, Single Crack mode heuristics, wordlist mutation engines, hash identification, and leveraging the complete suite of `*2john` utilities to extract hashes from SSH keys, PDFs, ZIPs, Keepass, and BitLocker volumes.
* **Key Artifacts:** Cracking mode decision flowchart, live terminal cracking GIF, and cryptographic hash hierarchy breakdown.

### 3. [Hashcat — Advanced GPU Cracking & Cryptanalysis Masterclass](./Hashcat/README.md)
* **🌐 Official Project Domain:** [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/)
* **🐙 Official Open-Source GitHub:** [https://github.com/hashcat/hashcat](https://github.com/hashcat/hashcat)
* **What You'll Learn:** Unleashing maximum compute horsepower through CUDA/OpenCL, optimizing workload profiles, designing combinatorial and hybrid attacks, crafting complex rules (`best64.rule`), and cracking high-entropy hashes (NTLM, Kerberos, bcrypt, Argon2).
* **Key Artifacts:** GPU vs CPU benchmark analysis, attack mode visual diagrams, and real-time cracking animation.

### 4. [Aircrack-ng & Wi-Fi Security — Protocol Auditing Masterclass](./Aircrack-ng/README.md)
* **🌐 Official Project Domain:** [https://www.aircrack-ng.org/](https://www.aircrack-ng.org/)
* **🐙 Official Open-Source GitHub:** [https://github.com/aircrack-ng/aircrack-ng](https://github.com/aircrack-ng/aircrack-ng)
* **What You'll Learn:** 802.11 management, control, and data frames; RF monitor mode drivers; capturing the EAPOL 4-way handshake; targeted deauthentication mechanics; PMKID attacks without clients; and auditing modern WPA3-SAE networks with Protected Management Frames (PMF).
* **Key Artifacts:** 4-way handshake cryptographic derivation diagram, deauth vs PMF attack matrix, and live aircrack session GIF.

### 5. [Kerberos — Deep Explanation, Tools, Attack Research & Practical Lab Guide](./Kerberos/README.md)
* **🌐 Official Protocol Standard & Docs:** [MIT Kerberos (web.mit.edu/kerberos)](https://web.mit.edu/kerberos/) • [Microsoft Kerberos Architecture](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview) • [IETF RFC 4120](https://datatracker.ietf.org/doc/html/rfc4120)
* **🐙 Open-Source Ecosystem Repositories:**
  - **Impacket (Python AD Protocol Suite):** [https://github.com/fortra/impacket](https://github.com/fortra/impacket)
  - **Rubeus (C# Windows Kerberos Suite):** [https://github.com/GhostPack/Rubeus](https://github.com/GhostPack/Rubeus)
  - **Kerbrute (Go Pre-Auth Sprayer):** [https://github.com/ropnop/kerbrute](https://github.com/ropnop/kerbrute)
  - **NetExec (Network Execution Suite):** [https://github.com/Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec)
  - **Mimikatz (Credentials & Ticket Forging):** [https://github.com/gentilkiwi/mimikatz](https://github.com/gentilkiwi/mimikatz)
  - **MIT Kerberos V5 Core:** [https://github.com/krb5/krb5](https://github.com/krb5/krb5)
* **What You'll Learn:** RFC 4120 protocol mechanics; AS-REQ/REP, TGS-REQ/REP, and AP-REQ exchanges; Pre-Authentication; Service Principal Name (SPN) architecture; Kerberoasting (`T1558.003`) and AS-REP Roasting (`T1558.004`); Rubeus and Impacket GetUserSPNs tooling; offline GPU cracking with Hashcat Mode 13100; Windows Security Event Log analysis (4768, 4769, 4771); Splunk SPL detection engineering; and enterprise defense via gMSA and AES encryption.
* **Key Artifacts:** Authentication sequence flowchart, Kerberoasting attack and defense architecture diagram, live auditing and SIEM alert GIF, and Splunk detection queries.

### 6. [Metasploit Framework — Technical Tool Architecture & Systems Guide](./Metasploit/README.md)
* **🌐 Official Project Domain:** [https://www.metasploit.com](https://www.metasploit.com/) • **Official Docs:** [https://docs.metasploit.com](https://docs.metasploit.com/)
* **🐙 Official Open-Source GitHub:** [https://github.com/rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)
* **What You'll Learn:** Metasploit Framework internal architecture (Rex library, MSF Core, MSF Base); 7 module families (Exploits, Auxiliary, Payloads, Post, Encoders, NOPs, Evasion); `msfconsole` command engine & session management; PostgreSQL database services (`db_nmap`, hosts, services, creds); Staged vs. Stageless payload engineering; Meterpreter TLV protocol & in-memory Reflective DLL execution; `msfvenom` CLI binary generation; concrete tool applications across 12 cybersecurity domains (Network, Web, Windows, Linux, Active Directory, Wireless, Cloud, Containers/DevSecOps, IoT/Embedded, Mobile, Exploit Development, and SOC/EDR operations); Sysmon endpoint telemetry forensics (Event IDs 1, 3, 7, 10); and Splunk SPL correlation rules.
* **Key Artifacts:** Module architecture infographic, attack and defense timeline diagram, live terminal session walkthrough GIF, and companion technical architecture markdown reference.

