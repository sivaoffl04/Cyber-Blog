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

![OSINT Lifecycle and Pivot Architecture Interactive Flow](./Over all OSINT/images/osint_investigation_lifecycle_pipeline.gif)

*Figure 1.1: Interactive Animated Lifecycle & Entity Pivot Flow — Dynamically cycling through all 5 phases & pivot transformations.*

</div>

<br>

<details open>
<summary><b>🔍 Click to view High-Resolution Static Architecture Blueprint & Breakdown</b></summary>

<div align="center">

![OSINT Lifecycle and Pivot Architecture High-Res Blueprint](./Over all OSINT/images/osint_investigation_lifecycle_pipeline.jpg)

</div>

#### ⚡ Interactive Operational Phase Breakdown:

<details>
<summary><b>Phase 01: Planning, Direction & OPSEC (Click to expand)</b></summary>

* **Objective:** Define Priority Intelligence Requirements (PIRs) and establish legal Rules of Engagement (RoE).
* **OPSEC Protocol:** Provision aged, decoupled sock puppets, isolate hardware inside Whonix/Tails VMs, route traffic over Tor circuits and non-attributable VPN tunnels, and randomize browser canvas fingerprints.
* **Core Toolchain:** `Whonix`, `Tails OS`, `Tor`, `ProtonVPN`, `User-Agent Switcher`.

</details>

<details>
<summary><b>Phase 02: Multi-Vector Signal Harvesting (Click to expand)</b></summary>

* **Objective:** Conduct exhaustive passive collection without sending active probe packets to the target.
* **Collection Vectors:** Identity footprints (`Sherlock`, `Maigret`), Certificate Transparency (`crt.sh`), passive subdomain enumeration (`Subfinder`, `Amass`), device scanners (`Shodan`, `Censys`), and secrets detection (`GitLeaks`, `TruffleHog`).
* **Core Toolchain:** `Subfinder`, `Amass`, `Shodan`, `Holehe`, `Censys`, `GitLeaks`.

</details>

<details>
<summary><b>Phase 03: Multi-Hop Lateral Pivoting (Click to expand)</b></summary>

* **Objective:** Traverse from single isolated artifacts into multi-domain entity graphs.
* **Pivot Chains:** Email $\to$ GitHub Commits $\to$ Internal Dev Domains $\to$ Origin IP Addresses $\to$ SSL Certificate SANs $\to$ Exposed Administration Portals.
* **Core Toolchain:** `Holehe`, `Epieos`, `SecurityTrails`, `ExifTool`, `SunCalc`.

</details>

<details>
<summary><b>Phase 04: Correlation, Processing & CTI Enrichment (Click to expand)</b></summary>

* **Objective:** Synthesize raw observables into structured intelligence graphs and map adversary TTPs.
* **Analytical Engines:** Automated transform discovery in Maltego, graph database modeling in Neo4j/Gephi, threat indicator correlation via MISP & AlienVault OTX, and MITRE ATT&CK Reconnaissance (TA0043) alignment.
* **Core Toolchain:** `Maltego`, `Neo4j`, `MISP`, `AlienVault OTX`, `MITRE ATT&CK Navigator`.

</details>

<details>
<summary><b>Phase 05: Dissemination, Reporting & Defensive Action (Click to expand)</b></summary>

* **Objective:** Deliver actionable intelligence dossiers with cryptographic proof and mitigation playbooks.
* **Actionable Outputs:** Assign Admiralty Code reliability ratings, generate Blue Team containment playbooks (Sigma rules, firewall drop lists), and guide immediate CVE remediation.
* **Core Toolchain:** `Sigma Rules`, `YARA`, `CISA KEV`, `Executive Threat Dossier`.

</details>

</details>

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
