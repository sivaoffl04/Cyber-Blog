<div align="center">

# 🛡️ Cyber-Blog — Contributor & Usage Guide

**The authoritative handbook for readers, researchers, and contributors**

[![Actively Maintained](https://img.shields.io/badge/Status-Actively%20Maintained-success?style=for-the-badge&logo=git)](https://github.com/sivaoffl04/Cyber-Blog)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge&logo=github)](https://github.com/sivaoffl04/Cyber-Blog/pulls)
[![License](https://img.shields.io/badge/License-Educational%20Use-blue?style=for-the-badge&logo=shield)](./LICENSE)

</div>

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [Repository Philosophy](#-repository-philosophy) |
| 2 | [Who This Is For](#-who-this-is-for) |
| 3 | [Repository Architecture](#-repository-architecture) |
| 4 | [How to Navigate the Knowledge Base](#-how-to-navigate-the-knowledge-base) |
| 5 | [Section Deep-Dives](#-section-deep-dives) |
| 6 | [Visual & Asset Standards](#-visual--asset-standards) |
| 7 | [Contributing a New Module](#-contributing-a-new-module) |
| 8 | [Git Workflow & Commit Conventions](#-git-workflow--commit-conventions) |
| 9 | [Audit & Quality Scripts](#-audit--quality-scripts) |
| 10 | [Ethical & Legal Framework](#-ethical--legal-framework) |

---

## 🧭 Repository Philosophy

Cyber-Blog is **not** a cheat-sheet dump or link aggregator. Every guide is built as a **production-grade operational reference** with:

- **Low-level protocol mechanics** — packet diagrams, hex breakdowns, RFC references
- **Realistic tradecraft** — offensive and defensive techniques used in real-world engagements
- **Detection engineering** — Sigma rules, MITRE ATT&CK technique IDs, and SIEM query patterns
- **Animated visual walkthroughs** — modern SaaS-style GIFs demonstrating tool usage step by step
- **Verified lab captures** — every flag, every answer, reproducibly documented

> [!IMPORTANT]
> All techniques are published for **education, defensive research, and authorized security assessments only**. Never execute offensive actions without explicit written permission from the resource owner.

---

## 👥 Who This Is For

| Audience | Primary Sections |
|----------|-----------------|
| **SOC Analysts (L1–L3)** | INE Labs, SOC, Security Teams (Blue) |
| **Penetration Testers** | Tools, Android Pentest, Security Teams (Red) |
| **OSINT Investigators** | OSINT Complete Framework |
| **CTI / Threat Hunters** | OSINT, INE Labs (Zeek, ELK), Security Teams (Purple) |
| **DevSecOps Engineers** | GitHub Security & Hardening Masterclass |
| **Students & Certification Candidates** | All sections — eJPT, eCPPT, OSCP, CySA+, BAP, CRTP, eCDFP |

---

## 🗂️ Repository Architecture

```
Cyber-Blog/
├── README.md                          ← Root hub — start here
├── CONTRIBUTING.md                    ← This guide
│
├── OSINT/                             ← Open Source Intelligence
│   ├── README.md                      ← OSINT portal with visuals
│   └── Over all OSINT/
│       ├── README.md                  ← Animated lifecycle + tool gallery
│       ├── OSINT_Complete_Framework_and_Investigation_Guide.md  ← 107-section masterclass
│       └── images/                    ← All GIFs and infographics
│
├── tools/                             ← Offensive & forensic tool courses
│   ├── Nmap/
│   ├── Hashcat/
│   ├── John the ripper/
│   └── Aircrack-ng/
│
├── INE lab/                           ← Hands-on SOC lab walkthroughs
│   ├── Kibana Windows Event Logs I/
│   ├── Kibana Windows Event Logs II/
│   ├── Kibana Windows Event Logs III/
│   ├── Log Anomaly Detection Basics/
│   ├── Compromised Credentials/
│   ├── Malicious User Behaviour Analysis/
│   ├── Apache Error Log Analysis Basics/
│   ├── Apache Log Analysis Basics/
│   ├── False Positive Validation .../
│   ├── Account Creation & Privilege Escalation .../
│   ├── PCAP Analysis With Zeek/
│   └── Effectively Using the ELK Stack/
│
├── GitHub_Security/                   ← DevSecOps hardening
├── Blog/                              ← Additional articles
├── Security_Team/                     ← Red / Blue / Purple team guides
│   ├── Red_Team/
│   ├── Blue_Team/
│   ├── Purple_Team/
│   └── Red_Team_vs_Blue_Team/
│
├── SOC/                               ← SOC workflow & IR playbooks
│   ├── EDR_SIEM_SOAR_YARA/
│   └── NIST 800-61/
│
└── Android_pentest/                   ← Mobile security
    ├── Introduction, APK Analysis, JADX & MobSF/
    └── Android Studio, ADB, Root & Non-Root Lab Setup/
```

---

## 🔍 How to Navigate the Knowledge Base

### Starting Points by Goal

| Goal | Where to Start |
|------|---------------|
| I want to investigate a person / domain / IP | [OSINT Complete Framework](./OSINT/Over%20all%20OSINT/OSINT_Complete_Framework_and_Investigation_Guide.md) → Sections 1–10 |
| I need a specific OSINT tool walkthrough | [OSINT Tool Gallery](./OSINT/Over%20all%20OSINT/README.md) → Tool Demo GIFs |
| I'm working a SOC alert right now | [INE Labs](./INE%20lab/README.md) → pick your alert type |
| I want to learn Nmap / Hashcat / John / Aircrack | [Tools Masterclasses](./tools/) |
| I'm hardening a GitHub organization | [GitHub Security](./GitHub_Security/GitHub_Security_and_Hardening_Masterclass.md) |
| I need MITRE ATT&CK technique context | [Root README ATT&CK Matrix](./README.md#mitre-attck-coverage-matrix) |
| I'm pentesting an Android app | [Android Pentest Part 1](./Android_pentest/Introduction,%20APK%20Analysis,%20JADX%20&%20MobSF/README.md) |
| I need to understand Red vs Blue team dynamics | [Security Teams](./Security_Team/Red_Team_vs_Blue_Team/README.md) |

### Quick Jump Architecture

The [root `README.md`](./README.md) contains:
1. **Interactive Mermaid flowchart** — visual map of every section
2. **Complete Knowledge Base Index table** — direct links with difficulty levels
3. **MITRE ATT&CK coverage matrix** — technique ID → module cross-reference
4. **Section summaries** — expanded descriptions for each major domain

---

## 📚 Section Deep-Dives

### 🔎 OSINT — Open Source Intelligence

The OSINT section is the most comprehensive module, structured as a 3-tier knowledge system:

```
OSINT/README.md
  └── Over all OSINT/README.md          ← Animated lifecycle GIF, tool gallery
        └── OSINT_Complete_Framework_and_Investigation_Guide.md
              ├── Sections 1–10:   Core Identity Recon (username, email, phone, person)
              ├── Sections 11–25:  Infrastructure (domains, IPs, Shodan, Censys, BGP)
              ├── Sections 26–45:  Social Media, Images, Video & Geolocation
              ├── Sections 46–60:  Corporate, Documents, Code Repos
              ├── Sections 61–75:  Dark Web, Breach Data, Crypto Tracing
              ├── Sections 76–90:  Threat Intelligence, CTI, MISP
              └── Sections 91–107: Automation, OPSEC, Legal & Reporting
```

**Key Tool GIF Walkthroughs available:**

| Tool | What It Demonstrates |
|------|---------------------|
| `sherlock_username_recon_demo.gif` | Username enumeration across 400+ platforms |
| `holehe_email_investigation_demo.gif` | Email → service account discovery (zero-alert method) |
| `subdomain_recon_pipeline_demo.gif` | Subfinder + HTTPX passive subdomain pipeline |
| `shodan_device_recon_demo.gif` | CVE banner analysis and IoT fingerprinting |
| `exiftool_metadata_analysis_demo.gif` | GPS + camera EXIF extraction with SunCalc chronolocation |
| `theharvester_recon_demo.gif` | Multi-source email and subdomain harvesting |

**Pivot Matrix:** The investigation always starts with what you have (email, username, domain, IP, image) and pivots outward. The [OSINT Pivot Matrix infographic](./OSINT/Over%20all%20OSINT/images/osint_pivot_matrix_infographic.jpg) maps 6 starting points × 6 destination domains.

---

### 🧰 Tools Masterclasses

Each tool guide follows the same deep-dive structure:

1. **Architecture** — how the tool works at the protocol / OS level
2. **Core commands** — annotated with what each flag actually does
3. **Advanced workflows** — chained pipelines, automation, scripting
4. **Detection signatures** — what SOC/EDR/SIEM sees when the tool runs
5. **Certification relevance** — which cert exam objectives are covered

| Module | Core Technologies | Certification Map |
|--------|------------------|--------------------|
| [Nmap](./tools/Nmap/README.md) | TCP/IP state machine, SYN scanning, NSE Lua | eJPT, eCPPT, OSCP |
| [Hashcat](./tools/Hashcat/README.md) | GPU CUDA/OpenCL, attack modes 0/1/3/6/7 | eCPPT, OSCP, CRTP |
| [John the Ripper](./tools/John%20the%20ripper/README.md) | `*2john` converters, rule mutation, sessions | eJPT, eCPPT |
| [Aircrack-ng](./tools/Aircrack-ng/README.md) | 802.11 frames, EAPOL, WPA2/WPA3, PMF | Wireless specializations |

---

### 🎯 INE Lab Walkthroughs

Every lab includes:
- **Challenge description** and learning objectives
- **Step-by-step methodology** — tools used, queries written, pivots made
- **All flags captured** with verification screenshots or output
- **Sigma detection rules** for the adversary techniques observed
- **Defensive takeaways** — what the blue team should have had in place

Labs are organized from beginner to advanced:

```
Beginner
  └── Apache Log Analysis Basics / Error Log Analysis Basics
Intermediate
  └── Log Anomaly Detection → Compromised Credentials → Malicious User Behaviour
Advanced
  └── Kibana Event Logs I/II/III → PCAP Analysis With Zeek → ELK Attack Emulation
SOC Workflow
  └── False Positive Validation → Account Creation & PrivEsc
```

---

### 🔒 GitHub Security & DevSecOps

Two-part curriculum covering both everyday developer hygiene and enterprise security engineering:

- **[Part 1](./GitHub_Security/How_to_Use_GitHub_Securely_Complete_Guide.md):** Git internals, Ed25519 SSH keys, signed commits, `gh` CLI, the 4-zone model
- **[Part 2](./GitHub_Security/GitHub_Security_and_Hardening_Masterclass.md):** Real breach case studies (Uber, Toyota, Codecov, CircleCI), 5-layer defense blueprint, OIDC passwordless auth, CodeQL, SBOM

---

### 👥 Security Team Operations

| Team | Focus |
|------|-------|
| [🔴 Red Team](./Security_Team/Red_Team/README.md) | C2 infrastructure, process injection, AD exploitation, evasion |
| [🔵 Blue Team](./Security_Team/Blue_Team/README.md) | EDR deployment, threat hunting hypotheses, hardening |
| [🟣 Purple Team](./Security_Team/Purple_Team/README.md) | Atomic Red Team emulation, ATT&CK coverage mapping, Sigma rule validation |
| [⚖️ Red vs Blue](./Security_Team/Red_Team_vs_Blue_Team/README.md) | Mental models, asymmetric defense, unified feedback loops |

---

### 🛡️ SOC & Incident Response

- **[Modern SOC Architecture](./SOC/EDR_SIEM_SOAR_YARA/README.md):** CrowdStrike → Splunk → Cortex XSOAR → YARA pipeline
- **[NIST SP 800-61](./SOC/NIST%20800-61/README.md):** Full IR lifecycle, severity matrices, containment/eradication, RCA reporting

---

### 📱 Android Penetration Testing

- **[Part 1](./Android_pentest/Introduction,%20APK%20Analysis,%20JADX%20&%20MobSF/README.md):** APK unpacking, DEX/Smali, JADX-GUI, MobSF static analysis, exported component auditing
- **[Part 2](./Android_pentest/Android%20Studio,%20ADB,%20Root%20&%20Non-Root%20Lab%20Setup/README.md):** AVD setup, ADB commands, Magisk rooting, Frida gadget injection for non-root testing

---

## 🎨 Visual & Asset Standards

> [!IMPORTANT]
> All visual assets in this repository follow the **Modern SaaS Card** design language. Do NOT use terminal-style monospace dark backgrounds.

### Design Language

| Element | Standard |
|---------|---------|
| **Background** | White or very light grey (`#f8fafc`) — NOT black |
| **Cards** | Rounded corners (`radius=12px`), subtle drop shadows |
| **Typography** | Segoe UI / SF Pro — large, readable sizes (min 18px body) |
| **Accent colors** | Per-section palette — blue/cyan for OSINT, red for alerts, green for success |
| **Tool pills** | Colored rounded pill badges for tool names |
| **Arrows** | Chevron-style (`→`) directional flow arrows |
| **GIF animation** | 5–9 frames, 800ms delay between frames, 920×520 minimum resolution |

### Image Generation Scripts

All images are generated via Python (Pillow). Scripts live in the artifacts directory:

| Script | Generates |
|--------|----------|
| `generate_interactive_lifecycle.py` | OSINT lifecycle pipeline JPG + animated GIF |
| `generate_tool_gifs.py` | 6 tool demonstration GIFs + 2 infographic JPGs |
| `update_docs_with_gifs.py` | Injects GIF walkthroughs into guide markdown |

**Font paths (Windows):**
```
C:/Windows/Fonts/seguisb.ttf    ← Segoe UI Semibold (headings)
C:/Windows/Fonts/segoeui.ttf    ← Segoe UI (body)
C:/Windows/Fonts/segoeuib.ttf   ← Segoe UI Bold (labels)
```

### Image Storage Convention

```
<section>/images/
  ├── <section>_banner.jpg            ← Hero banner (1200×500)
  ├── <section>_architecture.jpg      ← Architecture diagram (1600×1120)
  ├── <section>_architecture.gif      ← Animated version (same dimensions)
  ├── <tool>_demo.gif                 ← Tool walkthrough (920×520, 5 frames)
  └── <topic>_infographic.jpg         ← Reference infographic (1200×750–800)
```

---

## ✍️ Contributing a New Module

### Checklist Before Opening a PR

- [ ] **Directory** — create `<category>/<Module Name>/` with a `README.md`
- [ ] **Banner image** — create a section banner (`1200×500`, SaaS card style)
- [ ] **Structure** — follow the module template below
- [ ] **MITRE mapping** — identify all ATT&CK technique IDs covered
- [ ] **Legal review** — ensure all techniques are legal and ethically documented
- [ ] **Anchor validation** — run `audit_repo_links.py` — zero broken refs

### Module README Template

```markdown
<div align="center">

![Banner](./images/<module>_banner.jpg)

# 🛡️ Module Title
### Subtitle — Technology Scope

[![Badge](https://img.shields.io/badge/...)](link)

</div>

---

## 📋 Table of Contents
[TOC with jump links]

---

## Overview
[What this module covers and why it matters]

## Core Concepts
[Protocol-level, architecture-level explanation]

## Methodology
[Step-by-step operational approach]

## Tools & Commands
[Annotated commands with expected output]

## Detection & Defense
[What defenders see; Sigma rules; SIEM queries]

## MITRE ATT&CK Coverage
| Tactic | ID | Technique |
|--------|----|----|

## References
[Authoritative sources, RFCs, official docs]
```

### Content Quality Standards

| Standard | Requirement |
|---------|------------|
| **Depth** | Explain the "why" and "how" — not just command syntax |
| **Reproducibility** | Every command must be testable in a legal lab environment |
| **Attribution** | Cite sources; link to official documentation |
| **Neutrality** | Present offensive techniques alongside detection signatures |
| **Language** | Clear English; no filler, no excessive jargon without definition |

---

## 🔀 Git Workflow & Commit Conventions

### Branch Model

```
main  ← production branch (all pushes go here)
```

For new modules or large changes, work locally then push to `main` after self-review.

### Commit Message Format

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <short summary>

Types:
  feat      → new content module or major addition
  docs      → documentation additions or improvements
  fix       → broken links, typos, anchor errors
  style     → image regeneration, visual updates
  refactor  → restructuring without content change
  chore     → scripts, config, tooling updates

Examples:
  feat(osint): add cryptocurrency tracing and blockchain analysis module
  fix(ine-lab): resolve broken TOC anchor links in Zeek walkthrough
  style(osint): regenerate lifecycle pipeline with SaaS card design
  docs(android): add Frida gadget injection deep-dive to Part 2
```

### Pre-Push Checks

Run all three audit scripts before pushing:

```powershell
# From the repo root
python audit_repo_links.py    # 0 broken references required
python audit_mermaid.py       # 0 Mermaid fence issues
python audit_md_syntax.py     # 0 markdown syntax issues
```

---

## 🛠️ Audit & Quality Scripts

All scripts are stored in the artifacts directory. Copy them to the repo root to run.

### `audit_repo_links.py`
Walks every `.md` file and validates that all local image/file references resolve to existing files. Reports broken paths with line numbers.

```powershell
python audit_repo_links.py
# Expected: "0 broken references found"
```

### `audit_mermaid.py`
Validates Mermaid diagram fence blocks — checks for unclosed fences and basic syntax issues.

```powershell
python audit_mermaid.py
# Expected: "0 Mermaid issues found"
```

### `audit_md_syntax.py`
Checks for common markdown formatting problems — unclosed HTML tags, malformed tables, empty headings.

```powershell
python audit_md_syntax.py
# Expected: "0 markdown issues found"
```

### Anchor Slug Rule (Critical)

> [!WARNING]
> GitHub strips emojis from heading slugs. A heading `## 🔎 OSINT Tools` generates anchor `#osint-tools`, NOT `#-osint-tools`.

- **Wrong:** `[link](#-osint-tools)` ← broken on GitHub
- **Correct:** `[link](#osint-tools)` ← works on GitHub

Always test anchor links by clicking them on the rendered GitHub page after pushing.

---

## ⚖️ Ethical & Legal Framework

All content in this repository is governed by the following principles:

1. **Authorization First** — Offensive techniques are documented for use only on systems you own or have explicit written permission to test
2. **No Live Target Data** — No real credentials, PII, or actual breach data is published here
3. **Educational Intent** — The goal is to teach defenders how attacks work so they can build better detection
4. **Responsible Disclosure** — If you find real vulnerabilities while following techniques in this repo, follow responsible disclosure protocols
5. **Legal Compliance** — Techniques comply with CFAA (USA), Computer Misuse Act (UK), IT Act Section 43/66 (India), and equivalent international cybersecurity legislation

> [!CAUTION]
> Unauthorized use of offensive techniques described here is illegal. The repository maintainer assumes no liability for misuse. This content is published in the same spirit as academic security research and professional certifications like OSCP, CRTP, and CySA+.

---

<div align="center">

**Crafted with ❤️ by [Siva](https://github.com/sivaoffl04) | Continuously Updated**

⭐ **Star this repository if you find it valuable!** ⭐

[🔝 Back to Top](#-cyber-blog--contributor--usage-guide)

</div>
