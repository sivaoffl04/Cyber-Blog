<div align="center">

![Open Source Intelligence and Threat Reconnaissance Banner](./images/osint_masterclass_banner.jpg)

# 🔎 Open Source Intelligence (OSINT) & Threat Reconnaissance
### Enterprise Investigation Framework • Digital Footprinting • Attack Surface Mapping • SOCMINT • GEOINT • CTI

[![Framework](https://img.shields.io/badge/Architecture-Enterprise%20OSINT%20Framework-00e5ff?style=for-the-badge&logo=target)](https://osintframework.com/)
[![Standard](https://img.shields.io/badge/Standard-NIST%20SP%20800--61%20%7C%20DoD-blue?style=for-the-badge&logo=shield)](https://csrc.nist.gov/)
[![Playbook](https://img.shields.io/badge/Playbook-107%20Investigation%20Domains-success?style=for-the-badge&logo=git)](./OSINT_Complete_Framework_and_Investigation_Guide.md)

**An enterprise-grade operational playbook covering all 107 specialized disciplines and tool suites of Open Source Intelligence (OSINT) and Cyber Threat Reconnaissance.**

</div>

---

## 📖 Operational Guide Navigation

👉 **[Launch Complete 107-Section Field Operations Manual: `OSINT_Complete_Framework_and_Investigation_Guide.md`](./OSINT_Complete_Framework_and_Investigation_Guide.md)**

---

## 🗺️ Investigation Lifecycle & Pivot Architecture

<div align="center">

![OSINT Lifecycle and Pivot Architecture Interactive Flow](./images/osint_investigation_lifecycle_pipeline.gif)

*Figure 1.1: Interactive Animated Lifecycle & Entity Pivot Flow — Dynamically cycling through all 5 phases & pivot transformations.*

</div>

<br>

<details open>
<summary><b>🔍 Click to view High-Resolution Static Architecture Blueprint & Breakdown</b></summary>

<div align="center">

![OSINT Lifecycle and Pivot Architecture High-Res Blueprint](./images/osint_investigation_lifecycle_pipeline.jpg)

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

## ⚡ Operational Reconnaissance Pipeline Simulation

<div align="center">

![OSINT Multi-Stage Investigation Pipeline Demo](./images/osint_recon_live_demo.gif)

*Figure 1.2: Modern SaaS Multi-Stage Reconnaissance Pipeline — Cycling dynamically through all 5 phases from alias discovery to executive threat dossier.*

</div>

---

## 🎬 Interactive Tool Demonstrations & Animated CLI Walkthroughs

The operational playbook includes detailed, frame-by-frame animated command-line executions and analytical walkthroughs for every primary OSINT discipline:

| Demonstration | Target Discipline | Core Toolchain & Commands | Key Operational Capabilities |
| :--- | :--- | :--- | :--- |
| **[Username Recon Demo](./images/sherlock_username_recon_demo.gif)** | Section 04: Username Intelligence | `sherlock shadow_operative --timeout 15 --print-found --csv` | Scans 400+ platforms, detects active developer/gaming handles, exports CSV telemetry. |
| **[Maigret Deep Social Demo](./images/maigret_deep_social_recon_demo.gif)** | Section 04: Social Archaeology | `maigret target_user -a --parse-all --html --json` | Recursive scraping across 3,000+ sites, unmasks real names, bios, and avatar pHash clusters. |
| **[Email Intel Demo](./images/holehe_email_investigation_demo.gif)** | Section 05: Email Intelligence | `holehe target.dev@domain.com --only-used` | Zero-alert password-reset probing, recovers Google Gaia ID, unmasks phone numbers. |
| **[GHDB Web Dorking Demo](./images/ghdb_dorking_workflow_demo.gif)** | Section 03: Google Dorking | `site:target.com filetype:env "DB_PASSWORD"` | Advanced search operator chaining, unmasks exposed databases, API keys, and cloud buckets. |
| **[Subdomain Pipeline Demo](./images/subdomain_recon_pipeline_demo.gif)** | Section 10: Subdomain Reconnaissance | `subfinder -d target.com -silent \| httpx -title -tech-detect` | Combines 40+ passive feeds with active HTTP probes to unmask dev portals and Grafana metrics. |
| **[Shodan Device Demo](./images/shodan_device_recon_demo.gif)** | Section 12: Device & Infrastructure | `shodan search 'org:"Target"' \| shodan host <ip>` | Indexes IPv4 banners, identifies unpatched perimeter CVEs (Pulse Secure, Ivanti CVSS 10.0). |
| **[Censys Search Demo](./images/censys_certificate_recon_demo.gif)** | Section 13: Attack Surface | `services.tls.certificates.leaf_data.names: target.com` | Unmasks hidden origin web servers bypassing CDN WAFs using TLS SHA-256 and JARM hashes. |
| **[ExifTool Forensics Demo](./images/exiftool_metadata_analysis_demo.gif)** | Section 32: Media & Metadata | `exiftool -GPS* -Make -Model target.jpg \| suncalc` | Extracts camera hardware, coordinates, reverse-geocodes address, validates solar shadows. |
| **[theHarvester Demo](./images/theharvester_recon_demo.gif)** | Section 52: Multi-Source Scraping | `theHarvester -d target.com -b all -l 500` | Aggregates employee emails, subdomains, and IP netblocks across search engines and threat feeds. |
| **[Maltego Graph Demo](./images/maltego_link_analysis_demo.gif)** | Section 49: Visual Link Analysis | Multi-hop transforms across DNS, emails, IPs & CVEs | Maps multi-hop entity graphs, calculates node betweenness centrality, exports to STIX 2.1. |
| **[Crypto Forensics Demo](./images/blockchain_crypto_tracing_demo.gif)** | Section 27: Cryptocurrency | UTXO ledger tracking & Common Input Clustering | De-anonymizes ransomware extortion wallets, flags peeling chains, and targets KYC off-ramps. |

---

## 🗺️ Cross-Pillar Pivot Blueprint & Methodological Framework

<div align="center">

![OSINT Cross-Pillar Pivot Matrix](./images/osint_pivot_matrix_infographic.jpg)

*Systematic lateral pivot matrix: Converting isolated indicators into comprehensive intelligence dossiers.*

</div>

<br>

<div align="center">

![Geospatial Intelligence Methodology](./images/geospatial_intelligence_methodology.jpg)

*Scientific 4-quadrant GEOINT framework: Solar chronolocation, infrastructure markers, and multispectral satellites.*

</div>

---

## 📂 Primary Investigation Pillars

| Pillar | Focus Area | Core Capabilities & Toolchain | Direct Link |
| :---: | :--- | :--- | :---: |
| **01** | **Frameworks & Toolkits** | OSINT Framework, Bellingcat, OSINT Dojo, IntelTechniques, Trace Labs | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#1-osint-frameworks--master-toolkits) |
| **02** | **Search Engines & Aggregators** | Google, Bing, Brave, Yandex, SearXNG, Mojeek, Million Short | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#2-search-engines) |
| **03** | **Google Dorking & GHDB** | Advanced Boolean Operators, GHDB, DorkSearch, Sensitive File Dorks | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#3-google-dorking) |
| **04** | **Username OSINT** | Sherlock, Maigret, WhatsMyName, Blackbird, Cross-Platform Profiling | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#4-username-osint) |
| **05** | **Email OSINT** | Holehe, Epieos, Hunter.io, EmailRep, Gravatar, Service Binding | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#5-email-osint) |
| **06** | **Email Header Forensics** | RFC Headers, Hop Routing, SPF, DKIM, DMARC, X-Originating-IP | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#6-email-header-analysis) |
| **07** | **Phone Number OSINT** | PhoneInfoga, Truecaller, NumVerify, E.164 Specs, Carrier Metadata | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#7-phone-number-osint) |
| **08** | **Domain & WHOIS OSINT** | WHOIS, RDAP, SecurityTrails, ViewDNS, DNSDumpster | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#8-domain-osint) |
| **09** | **DNS OSINT** | Dig, Nslookup, SOA, MX, TXT SPF, DNSViz, Zone Transfers | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#9-dns-osint) |
| **10** | **Subdomain Enumeration** | OWASP Amass, Subfinder, Assetfinder, Findomain, Chaos | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#10-subdomain-enumeration) |
| **11** | **IP & ASN Telemetry** | BGPView, Hurricane Electric, IPinfo, AbuseIPDB, RIR Registries | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#11-ip-address-osint) |
| **12** | **Shodan Internet Scanner** | Banner Mining, Filters, Exposed Daemons, Unpatched CVEs | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#12-shodan) |
| **13** | **Censys Attack Surface** | Protocol Dissections, TLS Certificate Fingerprints, Asset Tracking | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#13-censys) |
| **14** | **Certificate Transparency** | crt.sh, CertSpotter, Wildcard SANs, Internal Staging Trails | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#14-certificate-transparency) |
| **15** | **Website Tech Profiling** | Wappalyzer, BuiltWith, WhatRuns, SecurityHeaders, WhatCMS | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#15-website-technology-osint) |
| **16** | **URL Analysis & Sandboxes** | urlscan.io, VirusTotal, Google Safe Browsing, Hybrid Analysis | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#16-url-analysis) |
| **17** | **Malware CTI Platforms** | Abuse.ch, ThreatFox, MalwareBazaar, URLhaus, AlienVault OTX | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#17-malware--cyber-threat-intelligence-osint) |
| **18** | **Cryptographic Hash OSINT** | MD5, SHA1, SHA256 Search, PE Headers, Outbound C2 Forensics | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#18-hash-osint) |
| **19** | **SOCMINT & Social Media** | Multi-Platform Monitoring, X/Twitter, Social Searcher, Botometer | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#19-social-media-intelligence-socmint) |
| **20** | **Code Repositories & Secrets** | GitHub Dorks, GitLeaks, TruffleHog, Commit History Mining | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#22-github-osint) |
| **21** | **Breach & Dark Web Intel** | Have I Been Pwned, DeHashed, Hudson Rock, Tor (.onion), Ransomwatch | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#25-breach--credential-exposure-intelligence) |
| **22** | **Cryptocurrency Forensics** | Bitcoin UTXO, Ethereum Accounts, Mempool, Etherscan, Arkham | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#27-cryptocurrency--blockchain-forensics) |
| **23** | **Corporate & Legal OSINT** | OpenCorporates, SEC EDGAR 10-K, Companies House, ImportYeti | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#28-corporate--business-entity-osint) |
| **24** | **Image Forensics & EXIF** | ExifTool, FotoForensics (ELA), Forensically, Aperi'Solve | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#32-exif--metadata) |
| **25** | **GEOINT & Satellite** | Google Earth Pro, SunCalc Chronolocation, Sentinel Hub, Overpass Turbo | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#33-image-geolocation) |
| **26** | **Transportation OSINT** | FlightRadar24, ADS-B Exchange, MarineTraffic AIS, VesselFinder | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#38-flight-osint) |
| **27** | **Digital Archives** | Wayback Machine CDX API, Archive.today, Common Crawl WARC | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#41-historical-web--archives) |
| **28** | **Visual Link Analysis** | Maltego Transforms, Gephi Modularity, Neo4j Graph Models | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#49-maltego) |
| **29** | **Threat Intel & Standards** | MITRE ATT&CK, MISP, STIX 2.1 / TAXII 2.1, CISA KEV Catalog | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#56-threat-actor-osint) |
| **30** | **Automation & Reporting** | SpiderFoot, Recon-ng, theHarvester, FinalRecon, Executive Dossier | [Read](./OSINT_Complete_Framework_and_Investigation_Guide.md#102-osint-automation-frameworks) |

---

<div align="center">

[👉 Explore the Full 107-Section Field Operations Manual & Playbook](./OSINT_Complete_Framework_and_Investigation_Guide.md)

</div>
