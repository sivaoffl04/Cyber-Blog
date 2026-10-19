# Chapter 02: Threat Actor Landscape — Scattered Spider & ALPHV/BlackCat

> **Seminar Module:** Threat Actor Profiling & The Cybercrime Affiliate Dynamic  
> **Target Audience:** Threat Intelligence Analysts, Security Leadership, Incident Responders  
> **Key Adversaries:** Scattered Spider (UNC3944 / Octo Tempest) & ALPHV/BlackCat (RaaS)

---

## 1. The Adversary Landscape: A Symbiotic Cybercrime Convergence

The MGM Resorts cyberattack represented an unprecedented operational convergence between two distinct tiers of the global cybercrime ecosystem:
1. **Scattered Spider (UNC3944):** Highly agile, young, native English-speaking social engineers skilled in identity manipulation and cloud navigation.
2. **ALPHV/BlackCat:** A hardened, mature, Eastern European Ransomware-as-a-Service (RaaS) syndicate with advanced cryptographic payloads targeting virtualization infrastructure.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│               THE SCATTERED SPIDER + ALPHV OPERATIONAL CONVERGENCE               │
├────────────────────────────────────────┬─────────────────────────────────────────┤
│       SCATTERED SPIDER (UNC3944)       │          ALPHV / BLACKCAT RAAS          │
│        [Access & Identity Core]        │         [Payload & Extortion Core]      │
├────────────────────────────────────────┼─────────────────────────────────────────┤
│ • Native English conversational fluency│ • Advanced Rust-based multi-platform    │
│ • LinkedIn OSINT & corporate mapping   │   ransomware (Windows, Linux, ESXi)     │
│ • Help desk voice phishing (vishing)   │ • Tor-based negotiation portals & leaks │
│ • Okta & Microsoft Entra ID mastery    │ • Escrow, affiliate profit splits       │
│ • MFA bypass (push fatigue, reset)     │ • Corporate PR shaming & press attacks  │
│ • Cloud & SaaS tenant pivoting         │ • High-performance multithreaded crypto │
└────────────────────────────────────────┴─────────────────────────────────────────┘
                                         │
                                         ▼
                 JOINT ATTACK ON MGM RESORTS INTERNATIONAL (SEPT 2023)
                 ─────────────────────────────────────────────────────
                 1. Scattered Spider compromises Okta via IT Help Desk
                 2. Expands privileges across Azure AD & Active Directory
                 3. Locates 100+ VMware ESXi hypervisor hosts
                 4. Deploys ALPHV/BlackCat ESXi ELF ransomware lockers
                 5. ALPHV initiates multi-million dollar extortion demand
```

---

## 2. Deep Dive: Profiling Scattered Spider (UNC3944 / Octo Tempest)

### Aliases & Industry Tracking
Across cybersecurity vendors and intelligence agencies, this adversary group is tracked under multiple designations:
* **Mandiant / Google Cloud:** UNC3944
* **Microsoft Threat Intelligence:** Octo Tempest
* **CrowdStrike:** Scattered Spider / Scatter Swine
* **Palo Alto Networks Unit 42:** Muddled Libra
* **CISA / FBI:** Joint Advisory Alert AA23-320A ("Scattered Spider")

### Origins and Demographics: The Underground "Com"
Unlike traditional nation-state APTs (e.g., Russian FSB or Chinese MSS) or established Russian-speaking ransomware cartels, Scattered Spider originated from a loosely organized online collective colloquially known as **"The Com"** (The Community). 

Members are predominantly teenagers and young adults aged 16 to 22 residing primarily in the United States, United Kingdom, and Canada. Their background stems from:
* High-stakes SIM swapping and crypto theft (2019–2021).
* Swatting and harassment campaigns on Discord and Telegram.
* Advanced social engineering targeting telecommunications carriers (AT&T, Verizon, T-Mobile).

### Evolution into Enterprise Intruders (2022–2023)
Between 2022 and 2023, Scattered Spider pivoted from individual consumer crypto theft to targeting Fortune 500 enterprises, Business Process Outsourcers (BPOs), and SaaS identity providers. 

```
                               SCATTERED SPIDER EVOLUTION
  2019-2020                 2021-2022                 2022-2023                 2023-Present
┌──────────────┐          ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│  SIM Swap &  │  ────►   │ Telecom BPO  │  ────►   │ Identity &   │  ────►   │ Enterprise   │
│ Crypto Theft │          │ Compromise   │          │ SaaS Tenants │          │ Ransomware   │
└──────────────┘          └──────────────┘          └──────────────┘          └──────────────┘
  Targeting individual     Targeting call centers     Compromising Okta,        Partnering with
  crypto holders and       to swap SIMs and bypass    Azure, Slack, Twilio,     ALPHV to encrypt
  gamertag accounts.       SMS verification.          and VPN gateways.         ESXi datastores.
```

### Signature Tactical Capabilities
1. **Flawless Native Conversational Vishing:** Because threat actors are native English speakers, they possess innate cultural context, colloquial speech patterns, and professional demeanor, allowing them to convince enterprise support desk analysts that they are legitimate employees experiencing technical difficulties.
2. **Aggressive Multi-Factor Exhaustion (MFA Fatigue):** Flooding targets with dozens of push notifications during late-night hours, often followed by direct phone calls or WhatsApp messages impersonating corporate security saying: *"Please approve the notification to clear the security hold."*
3. **Identity Federation Tampering:** Configuring new Inbound SAML Identity Providers (IdP) or unauthorized Azure Active Directory cross-tenant access relationships to maintain stealthy persistence.
4. **Cloud Infrastructure Harvesting:** Rapid enumeration of Amazon Web Services (AWS), Microsoft Azure, and VMware environments to target virtual disk stores (`.vmdk`) and database snapshots.

---

## 3. Deep Dive: Profiling ALPHV / BlackCat

### Origins & Architecture: The Rust Pioneer
ALPHV (first identified in November 2021) was the first major Ransomware-as-a-Service family authored entirely in the **Rust** programming language. The core developers are widely assessed to have emerged from the remnants of **DarkSide** (infamous for the May 2021 Colonial Pipeline attack) and **BlackMatter**.

### Why Rust?
* **Cross-Platform Compilation:** A single codebase compiles seamlessly to Windows PE, Linux ELF, and VMware ESXi without requiring platform-specific rewrites.
* **Memory Safety & Performance:** Highly optimized multithreading allows asynchronous parallel file encryption across massive enterprise storage arrays (NFS/SAN).
* **AV/EDR Evasion:** Binary payloads compiled in Rust present novel instruction flows and metadata signatures that bypass legacy heuristics designed for C/C++ binaries.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   ALPHV / BLACKCAT RANSOMWARE TECHNICAL STACK                    │
├──────────────────────────────────────────────────────────────────────────────────┤
│ • Language: Rust (Highly optimized, multithreaded)                               │
│ • Cryptography: ChaCha20 / AES-256 with RSA-4096 / Curve25519 key encapsulation  │
│ • Encryption Modes: Full, Interstitial (header/blocks), or Fast Partial Encrypt  │
│ • Platform Targets: Windows (x86/x64), Linux (x86_64, ARM), VMware ESXi          │
│ • Privilege Escalation: Exploits and built-in process termination routines       │
│ • ESXi Capabilities: Direct `esxcli` execution, VM shutdown, .vmdk file locking  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### The RaaS Business Model & Affiliate Terms
ALPHV operated on a tiered affiliate model:
* **Affiliate Revenue Split:** 80% to 90% of the ransom went to the affiliate who executed the breach (e.g., Scattered Spider), while 10% to 20% was retained by core ALPHV developers for infrastructure and payload updates.
* **Extortion Infrastructure:** Affiliates received automated access to:
  * Private Tor-based chat portals for victim negotiations.
  * Leak sites (clear-web mirrors and `.onion` domains) with automated public data posting.
  * Administrative dashboards to generate customized locker payloads with victim-specific configuration flags.

---

## 4. The ALPHV Public Press Release: Psychological Warfare

On September 13, 2023—two days after MGM took down its systems—ALPHV published an unprecedented, lengthy public statement on their dark web leak site. This communication offered an extraordinary window into the psychological warfare, operational frustrations, and adversary perspective during the incident.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│              EXCERPT FROM ALPHV/BLACKCAT PUBLIC PRESS STATEMENT                 │
│                              (SEPTEMBER 13, 2023)                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│ "MGM Resorts International has spent the last few days lying to their           │
│  shareholders, customers, and the media.                                        │
│                                                                                 │
│  We did not tamper with the slot machines. The slot machines were taken down    │
│  by MGM themselves because their own network engineers panicked and severed     │
│  their internal networks.                                                       │
│                                                                                 │
│  We had full administrative access to their Okta environment and their Azure    │
│  tenant. When they realized we were inside, they attempted to evict us by       │
│  disconnecting Okta Sync, which broke their own Active Directory.               │
│                                                                                 │
│  In response to their refusal to negotiate, we deployed ransomware across their │
│  ESXi hypervisors and encrypted over 100 servers.                               │
│                                                                                 │
│  MGM: You can lie to the public, but you cannot lie to the SEC. We still have   │
│  your data, and we will continue our operations until you come to the table."   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Analytical Deconstruction of the Adversary Statement
Threat intelligence analysts must look past the bluster to extract objective facts:
1. **Adversary Frustration Over Failed Communications:** Threat actors rely on structured extortion channels. MGM's aggressive "scorched earth" disconnection strategy cut off the attackers' communications, prompting them to resort to public shaming.
2. **Validation of Identity Mechanics:** The statement corroborated that the attackers maintained administrative control across both Okta and Azure, and that MGM's defensive severance of Okta Sync caused cascading internal identity failures.
3. **Weaponizing SEC Regulations:** ALPHV explicitly referenced the SEC's newly instituted 4-day material cybersecurity incident reporting rules (Form 8-K), using federal regulatory pressure as an extortion lever against the board of directors.

---

## 5. Strategic Comparison: Traditional Ransomware vs. Identity-Driven RaaS

| Attribute | Legacy Ransomware Operations (2017–2021) | Modern Identity-Driven RaaS (MGM / 2023) |
| :--- | :--- | :--- |
| **Initial Intrusion** | Phishing email with weaponized macro/EXE; exploit on unpatched VPN (Fortinet, Pulse). | Conversational voice phishing (vishing) targeting internal IT Help Desk. |
| **Credential Access** | Mimikatz, Kerberoasting, LSASS dumping on domain-joined endpoints. | Help desk MFA reset, self-registration of attacker MFA hardware/software tokens. |
| **Privilege Escalation** | Active Directory privilege escalation (CVEs, misconfigured GPOs). | Inherent assignment of Okta Super Admin and Azure Global Admin roles. |
| **Persistence** | Scheduled tasks, service creation, webshells, registry run keys. | Inbound SAML Identity Federation, rogue OAuth applications, cross-tenant sync. |
| **Target of Impact** | Windows file servers and corporate endpoints. | Centralized VMware ESXi hypervisor clusters hosting virtual machines and SAN storage. |
| **Adversary Profile** | Eastern European groups communicating via Russian-language forums. | Distributed English-speaking youth affiliates collaborating with established RaaS syndicates. |

---

## 6. Seminar Discussion Questions

1. **The Affiliate Boundary:** How does an enterprise defend against a threat model where the initial intruder (Scattered Spider) speaks native colloquial English, understands corporate org charts, and outsources the destruction to a foreign ransomware payload (ALPHV)?
2. **Extortion Disruption:** Did MGM's refusal to engage in negotiations diminish the ransomware syndicate's leverage, or did it increase the collateral financial damage to operations?
