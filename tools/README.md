# 🧰 Cybersecurity Tool Masterclasses & Deep Dives

Welcome to the **Cybersecurity Tool Masterclasses** repository section. Rather than basic command cheat sheets, each course in this directory provides a comprehensive, production-grade guide covering architecture, packet-level / hardware mechanics, real-world attack scenarios, detection engineering, and defensive hardening.

---

## 📚 Masterclass Index

| Tool | Category | Focus Areas | Hardware / Protocols | Course Link |
| :--- | :---: | :--- | :--- | :---: |
| **Nmap** (Network Mapper) | Network Reconnaissance & Port Scanning | TCP/UDP mechanics, SYN stealth scans, NSE scripting engine, firewall evasion, IDS evasion | TCP, UDP, SCTP, Raw IP Sockets, Lua NSE | [Nmap Masterclass](./Nmap/README.md) |
| **John the Ripper** (JtR) | Password Cracking & Cryptanalysis | Password cracking modes, wordlist mutation rules, `*2john` format converters, potfile management, incremental attacks | CPU (Multi-core), SIMD, AVX-512, OpenCL | [John the Ripper Masterclass](./John%20the%20ripper/README.md) |
| **Hashcat** | High-Performance Password Recovery | GPU-accelerated hashing, attack modes (0, 1, 3, 6, 7), rule-based cracking, mask attacks, Markov chains | GPU (CUDA, ROCm, OpenCL), PCIe, Tensor Cores | [Hashcat Masterclass](./Hashcat/README.md) |
| **Aircrack-ng** | Wireless Security & 802.11 Auditing | Wi-Fi 802.11 frames, monitor mode, WPA/WPA2 4-way handshake capture, controlled deauth, WPA3 SAE / PMF analysis | 802.11 a/b/g/n/ac/ax, RF Channels, WPA2-PSK, WPA3-SAE | [Aircrack-ng Masterclass](./Aircrack-ng/README.md) |

---

## 🛠️ Tool Masterclass Highlights

### 1. [Nmap — Complete Cybersecurity Course](./Nmap/README.md)
* **What You'll Learn:** Low-level TCP three-way handshakes, SYN vs Connect vs FIN/Xmas/Null scans, OS fingerprinting heuristics, writing custom Lua scripts for the Nmap Scripting Engine (NSE), and bypassing stateful firewalls with fragmentation and decoys.
* **Key Artifacts:** Detailed packet exchange sequence diagrams, live scan demonstration GIF, and port state decision matrix.

### 2. [John the Ripper — A–Z Complete Course](./John%20the%20ripper/README.md)
* **What You'll Learn:** Linux `/etc/shadow` and Windows NTLM auditing, Single Crack mode heuristics, wordlist mutation engines, hash identification, and leveraging the complete suite of `*2john` utilities to extract hashes from SSH keys, PDFs, ZIPs, Keepass, and BitLocker volumes.
* **Key Artifacts:** Cracking mode decision flowchart, live terminal cracking GIF, and cryptographic hash hierarchy breakdown.

### 3. [Hashcat — A–Z Complete Course](./Hashcat/README.md)
* **What You'll Learn:** Unleashing maximum compute horsepower through CUDA/OpenCL, optimizing workload profiles, designing combinatorial and hybrid attacks, crafting complex rules (`best64.rule`), and cracking high-entropy hashes (NTLM, Kerberos, bcrypt, Argon2).
* **Key Artifacts:** GPU vs CPU benchmark analysis, attack mode visual diagrams, and real-time cracking animation.

### 4. [Aircrack-ng & Wi-Fi Security — Complete Course](./Aircrack-ng/README.md)
* **What You'll Learn:** 802.11 management, control, and data frames; RF monitor mode drivers; capturing the EAPOL 4-way handshake; targeted deauthentication mechanics; PMKID attacks without clients; and auditing modern WPA3-SAE networks with Protected Management Frames (PMF).
* **Key Artifacts:** 4-way handshake cryptographic derivation diagram, deauth vs PMF attack matrix, and live aircrack session GIF.
