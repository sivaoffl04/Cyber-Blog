<div align="center">

![Open Source Intelligence and Threat Reconnaissance Banner](./Over%20all%20OSINT/images/osint_masterclass_banner.jpg)

# 🔎 Open Source Intelligence (OSINT) & Threat Reconnaissance
### Enterprise Investigation Framework • Digital Footprinting • Attack Surface Mapping • SOCMINT • GEOINT • CTI

[![Framework](https://img.shields.io/badge/Architecture-Enterprise%20OSINT%20Framework-00e5ff?style=for-the-badge&logo=target)](https://osintframework.com/)
[![Standard](https://img.shields.io/badge/Standard-NIST%20SP%20800--61%20%7C%20DoD-blue?style=for-the-badge&logo=shield)](https://csrc.nist.gov/)
[![Playbook](https://img.shields.io/badge/Playbook-107%20Investigation%20Domains-success?style=for-the-badge&logo=git)](./Over%20all%20OSINT/OSINT_Complete_Framework_and_Investigation_Guide.md)

**A production-grade operational knowledge base covering all 107 specialized disciplines and tool suites of Open Source Intelligence (OSINT) and Cyber Threat Reconnaissance.**

</div>

---

## 📖 Operational Guide Navigation

👉 **[Launch Complete 107-Section Field Operations Manual: `OSINT_Complete_Framework_and_Investigation_Guide.md`](./Over%20all%20OSINT/OSINT_Complete_Framework_and_Investigation_Guide.md)**  
👉 **[View Master Tool & Domain Quick Index: `Over all OSINT/README.md`](./Over%20all%20OSINT/README.md)**

---

## 🗺️ Investigation Lifecycle & Pivot Architecture

<div align="center">

![OSINT Lifecycle and Pivot Architecture](./Over%20all%20OSINT/images/osint_investigation_lifecycle_pipeline.jpg)

*High-Resolution Operational Execution Flow: 5-Stage Investigation Lifecycle & Cross-Domain Entity Pivot Nexus.*

</div>

---

## ⚡ Terminal Workflow Simulation

<div align="center">

![OSINT Live Investigation Terminal Demo](./Over%20all%20OSINT/images/osint_recon_live_demo.gif)

*Live end-to-end command-line simulation demonstrating multi-hop reconnaissance and threat attribution.*

</div>

---

## 🎬 Interactive Tool Demonstrations & Animated CLI Walkthroughs

The operational playbook includes detailed, frame-by-frame animated command-line executions and analytical walkthroughs for every primary OSINT discipline:

| Demonstration | Target Discipline | Core Toolchain & Commands | Key Operational Capabilities |
| :--- | :--- | :--- | :--- |
| **[Username Recon Demo](./Over%20all%20OSINT/images/sherlock_username_recon_demo.gif)** | Section 04: Username Intelligence | `sherlock shadow_operative --timeout 15 --print-found --csv` | Scans 400+ platforms, detects active developer/gaming handles, exports CSV telemetry. |
| **[Email Intel Demo](./Over%20all%20OSINT/images/holehe_email_investigation_demo.gif)** | Section 05: Email Intelligence | `holehe target.dev@domain.com --only-used` | Zero-alert password-reset probing, recovers Google Gaia ID, unmasks phone numbers. |
| **[Subdomain Pipeline Demo](./Over%20all%20OSINT/images/subdomain_recon_pipeline_demo.gif)** | Section 10: Subdomain Reconnaissance | `subfinder -d target.com -silent \| httpx -title -tech-detect` | Combines 40+ passive feeds with active HTTP probes to unmask dev portals and Grafana metrics. |
| **[Shodan CLI Demo](./Over%20all%20OSINT/images/shodan_device_recon_demo.gif)** | Section 12: Device & Infrastructure | `shodan search 'org:"Target"' \| shodan host <ip>` | Indexes IPv4 banners, identifies unpatched perimeter CVEs (Pulse Secure, Ivanti CVSS 10.0). |
| **[ExifTool Forensics Demo](./Over%20all%20OSINT/images/exiftool_metadata_analysis_demo.gif)** | Section 32: Media & Metadata | `exiftool -GPS* -Make -Model target.jpg \| suncalc` | Extracts camera hardware, coordinates, reverse-geocodes address, validates solar shadows. |
| **[theHarvester Demo](./Over%20all%20OSINT/images/theharvester_recon_demo.gif)** | Section 52: Multi-Source Scraping | `theHarvester -d target.com -b all -l 500` | Aggregates employee emails, subdomains, and IP netblocks across search engines and threat feeds. |

---

## 🗺️ Cross-Pillar Pivot Blueprint & Methodological Framework

<div align="center">

![OSINT Cross-Pillar Pivot Matrix](./Over%20all%20OSINT/images/osint_pivot_matrix_infographic.jpg)

*Systematic lateral pivot matrix: Converting isolated indicators into comprehensive intelligence dossiers.*

</div>

<br>

<div align="center">

![Geospatial Intelligence Methodology](./Over%20all%20OSINT/images/geospatial_intelligence_methodology.jpg)

*Scientific 4-quadrant GEOINT framework: Solar chronolocation, infrastructure markers, and multispectral satellites.*

</div>

---

## 🛠️ The 10 Core Tools Every Cybersecurity Analyst Must Master

1. **Google / Advanced Dorking:** Rapid index querying, directory listings, and filetype mining.
2. **Shodan & Censys:** Passive discovery of exposed servers, IoT banners, industrial controls, and SSL certificates.
3. **Maltego:** Visual link analysis, graph generation, and automated entity transform chains.
4. **Subfinder & OWASP Amass:** High-speed passive subdomain enumeration across 40+ third-party APIs.
5. **Holehe & Epieos:** Cross-platform email account discovery and linked profile attribution.
6. **Sherlock & Maigret:** Multi-platform username hunting and digital identity footprinting.
7. **GitLeaks & TruffleHog:** SAST secrets detection across git commit histories and open repositories.
8. **ExifTool & SunCalc:** Hardware metadata extraction and solar shadow chronolocation.
9. **VirusTotal & AlienVault OTX:** Threat intelligence correlation, domain reputation, and malware pivoting.
10. **Recon-ng & theHarvester:** Multi-source modular OSINT automation pipelines.

---

<div align="center">

👉 **[Explore the Complete 107-Section OSINT Operations Manual & Playbook](./Over%20all%20OSINT/OSINT_Complete_Framework_and_Investigation_Guide.md)**

</div>
