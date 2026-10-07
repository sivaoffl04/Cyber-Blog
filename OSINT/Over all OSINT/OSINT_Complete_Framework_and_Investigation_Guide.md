<div align="center">

![Open Source Intelligence and Threat Reconnaissance Banner](./images/osint_masterclass_banner.jpg)

# 🔎 Open Source Intelligence (OSINT) & Cyber Threat Reconnaissance
### Enterprise Investigation Framework • Attack Surface Mapping • SOCMINT • GEOINT • Blockchain Forensics • CTI Architecture

[![Framework](https://img.shields.io/badge/Framework-OSINT%20Framework-00e5ff?style=for-the-badge&logo=target)](https://osintframework.com/)
[![Standard](https://img.shields.io/badge/Standard-NIST%20SP%20800--61%20%7C%20DoD-blue?style=for-the-badge&logo=shield)](https://csrc.nist.gov/)
[![Intelligence](https://img.shields.io/badge/Intelligence-MISP%20%7C%20STIX%202.1-orange?style=for-the-badge&logo=apache)](https://www.misp-project.org/)
[![Playbook](https://img.shields.io/badge/Playbook-20%20Operational%20Domains-success?style=for-the-badge&logo=git)](.)

<p align="center">
  <b>A comprehensive, production-grade Open Source Intelligence (OSINT) operations manual designed for Cybersecurity Analysts, Threat Hunters, Purple Teams, Penetration Testers, and Incident Responders.</b>
</p>

[🏛️ Architecture & Lifecycle](#-osint-investigation-lifecycle--pivot-architecture) • [⚡ Animated Workflow Demo](#-live-investigation-workflow-demonstration) • [📚 Operational Domains Directory](#-operational-domains-directory-domain-01--20) • [⚖️ Legal & OPSEC](#module-01-foundations-intelligence-cycle--opsec-tradecraft)

</div>

---

## 🏛️ OSINT Investigation Lifecycle & Pivot Architecture

Modern intelligence operations do not rely on random Google queries. Professional OSINT is an **iterative, multi-stage engineering discipline** structured across the standardized Intelligence Cycle:

![OSINT Lifecycle and Pivot Architecture](./images/osint_investigation_lifecycle_pipeline.jpg)

```mermaid
flowchart LR
    P["🎯 1. Planning & OPSEC\n• Define PIRs\n• Burner / Sock Puppets\n• VPN/Tor Sandboxing"] 
    --> C["📥 2. Harvesting\n• People & Usernames\n• DNS & Certificates\n• Network Scanners"]
    --> PV["🔄 3. Multi-Hop Pivoting\n• Email ➔ Dev Handle\n• Handle ➔ GitHub Commit\n• Commit ➔ AWS Key / IP"]
    --> A["🧠 4. Correlation & Graph\n• Maltego Link Analysis\n• Neo4j Graph Models\n• MISP Threat Sharing"]
    --> D["📑 5. Dissemination\n• Actionable Dossier\n• Confidence Matrix\n• Blue Team Hardening"]

    style P fill:#0f172a,stroke:#00e5ff,stroke-width:2px,color:#fff
    style C fill:#0f172a,stroke:#ffab00,stroke-width:2px,color:#fff
    style PV fill:#0f172a,stroke:#00e676,stroke-width:2px,color:#fff
    style A fill:#0f172a,stroke:#b388ff,stroke-width:2px,color:#fff
    style D fill:#0f172a,stroke:#ff5252,stroke-width:2px,color:#fff
```

---

## ⚡ Live Investigation Workflow Demonstration

The terminal demonstration below simulates an end-to-end authorized threat reconnaissance engagement—progressing through environment isolation, passive subdomain harvesting, certificate transparency queries, Shodan port correlation, developer secret recovery via GitLeaks, EXIF chronolocation, breach correlation, and final intelligence dossier generation:

![OSINT Live Investigation Terminal Demo](./images/osint_recon_live_demo.gif)

---

## 📚 Operational Domains Directory: Domain 01 → 20

| Module | Domain | Key Tools & Technologies | Focus & Capabilities |
| :---: | :--- | :--- | :--- |
| [**01**](#module-01-foundations-intelligence-cycle--opsec-tradecraft) | **Foundations & OPSEC** | DoD Cycle, Sock Puppets, Tor, Whonix, CFAA/GDPR | Intelligence cycle, non-attributable environments, operational security |
| [**02**](#module-02-search-engines--advanced-google-dorking) | **Search Engines & Dorking** | Google Dorking, GHDB, SearXNG, Mojeek, Yandex | Boolean logic, advanced dork syntax, cache mining, search aggregators |
| [**03**](#module-03-people--identity-intelligence) | **People & Identity** | Sherlock, Maigret, WhatsMyName, Blackbird | Username enumeration across 500+ services, cross-platform aliases |
| [**04**](#module-04-email-intelligence--header-forensics) | **Email & Headers** | Holehe, Epieos, Hunter, EmailRep, SPF/DKIM/DMARC | Registered services discovery, routing hop analysis, spoof verification |
| [**05**](#module-05-phone-number--telecom-reconnaissance) | **Phone & Telecom** | PhoneInfoga, NumVerify, Truecaller, E.164 Specs | Carrier routing, line type, country numbering plans, fraud scoring |
| [**06**](#module-06-domain-dns--infrastructure-osint) | **Domain & DNS** | `dig`, `nslookup`, WHOIS/RDAP, DNSDumpster, DNSViz | Zone transfers, SOA/MX/TXT auditing, DNSSEC chain validation |
| [**07**](#module-07-subdomain-discovery--attack-surface-mapping) | **Subdomain Mapping** | Amass, Subfinder, Assetfinder, Findomain, crt.sh | Passive attack-surface discovery, Certificate Transparency log mining |
| [**08**](#module-08-network-scanners--internet-wide-telemetry) | **Internet Scanners** | Shodan, Censys, GreyNoise, ZoomEye, FOFA | Banner harvesting, IoT/SCADA mapping, scanner noise filtering |
| [**09**](#module-09-web-application--technology-profiling) | **Tech Stack Profiling** | Wappalyzer, BuiltWith, urlscan.io, SecurityHeaders | Framework fingerprinting, DOM analysis, historical CDN/WAF telemetry |
| [**10**](#module-10-social-media-intelligence-socmint) | **SOCMINT** | X/Twitter, LinkedIn, Telegram (TGStat), Reddit | Corporate hierarchy mapping, threat actor channel monitoring, bot filtering |
| [**11**](#module-11-code-repository--secret-exposure-osint) | **Code & Secret Hunting** | GitLeaks, TruffleHog, GitHub Dorking, Gitrob | Hardcoded credentials in Git trees, commit diffs, cloud IAM key harvesting |
| [**12**](#module-12-breach-intelligence--dark-web-monitoring) | **Breach & Dark Web** | HIBP, DeHashed, Hudson Rock, Ahmia, Ransomwatch | Leaked credential database parsing, `.onion` indexing, ransomware monitoring |
| [**13**](#module-13-cryptocurrency--blockchain-forensics) | **Cryptocurrency OSINT** | Mempool, Etherscan, Blockchair, Arkham, Breadcrumbs | UTXO tracing, smart contract decompilation, exchange wallet clustering |
| [**14**](#module-14-corporate-business--legal-osint) | **Business & Legal** | OpenCorporates, SEC EDGAR, Companies House, ImportYeti | Corporate subsidiaries, beneficial ownership, bill-of-lading shipments |
| [**15**](#module-15-geospatial-intelligence-geoint--satellite) | **GEOINT & Imagery** | Google Earth Pro, SunCalc, Overpass Turbo, Sentinel | Chronolocation via shadows, satellite multispectral bands, street landmarks |
| [**16**](#module-16-image-forensics--reverse-visual-search) | **Image Forensics** | ExifTool, FotoForensics, Google Lens, PimEyes | EXIF metadata extraction, Error Level Analysis (ELA), visual facial pivots |
| [**17**](#module-17-video--audio-osint-verification) | **Video & Audio** | InVID / WeVerify, `yt-dlp`, FFmpeg, Whisper | Keyframe extraction, reverse video framing, audio spectrum analysis |
| [**18**](#module-18-threat-intelligence--cti-frameworks) | **CTI & Threat Intel** | MISP, STIX 2.1, TAXII, AlienVault OTX, CISA KEV | Diamond Model, threat actor attribution, automated IOC exchange |
| [**19**](#module-19-link-analysis--visual-graph-correlation) | **Graph Correlation** | Maltego, Gephi, Neo4j, SpiderFoot | Transform engines, multi-hop entity graphs, centrality & clustering |
| [**20**](#module-20-automated-frameworks--intelligence-reporting) | **Automation & Reports** | Recon-ng, FinalRecon, theHarvester, CTI Reporting | Workflow pipelines, executive dossier writing, remediation playbooks |

---

## Module 01: Foundations, Intelligence Cycle & OPSEC Tradecraft

### 1.1 The Intelligence Cycle
Open Source Intelligence (OSINT) is intelligence produced from publicly available information that is collected, exploited, and disseminated in a timely manner to an appropriate audience for the purpose of addressing a specific intelligence requirement.

```mermaid
flowchart TD
    D["1. Direction & Planning\n(Define PIRs & Scoping)"] --> C["2. Collection\n(Harvesting Public Signals)"]
    C --> P["3. Processing\n(Normalization & Decryption)"]
    P --> A["4. Analysis & Production\n(Correlation, Attribution & Confidence)"]
    A --> DS["5. Dissemination\n(Actionable Report & Defense)"]
    DS --> F["6. Feedback & Evaluation"]
    F --> D

    style D fill:#1e293b,stroke:#00e5ff,color:#fff
    style C fill:#1e293b,stroke:#ffab00,color:#fff
    style P fill:#1e293b,stroke:#00e676,color:#fff
    style A fill:#1e293b,stroke:#b388ff,color:#fff
    style DS fill:#1e293b,stroke:#ff5252,color:#fff
    style F fill:#1e293b,stroke:#90caf9,color:#fff
```

### 1.2 Passive vs. Active Reconnaissance
* **Passive Reconnaissance:** The investigator communicates **exclusively with third-party aggregators, caches, and public registries** (e.g., querying DNS records from Google Public DNS, reviewing Shodan cache, pulling Certificate Transparency logs from `crt.sh`). **Zero network packets touch the target's perimeter.**
* **Semi-Passive Reconnaissance:** Queries that simulate normal user traffic (e.g., standard browser visit to the homepage, retrieving `robots.txt`) without triggering intrusion alerts.
* **Active Reconnaissance:** Packets directly interact with the target's infrastructure (e.g., SYN port scanning with Nmap, directory brute-forcing, SNMP walks). **Requires explicit written authorization.**

### 1.3 Operational Security (OPSEC) Architecture
Investigators must prevent target awareness and identity leakage:
1. **Dedicated Hardware / Virtual Sandbox:** Operate exclusively from dedicated virtual machines (Whonix, Tails, or ephemeral Kali containers). Never conduct research from your primary host workstation.
2. **Network Masking:** Route research traffic through multi-hop VPNs or Tor circuits. Rotate exit nodes when performing bulk queries to prevent rate-limiting and geo-location poisoning.
3. **Sock Puppets (Virtual Personas):**
   * Never tie research accounts to personal phone numbers, recovery emails, or payment cards.
   * Generate realistic, consistent persona backstories (age, occupation, location, interests).
   * Utilize burner SIMs or VoIP services (paid via privacy-centric methods) for two-factor verification.
   * Strip browser canvas fingerprints using privacy-hardened profiles (Brave, LibreWolf, Firefox with `privacy.resistFingerprinting = true`).

### 1.4 Legal Boundaries & Ethics
* **United States:** Adhere strictly to the Computer Fraud and Abuse Act (CFAA, 18 U.S.C. § 1030). Scraping public data is generally protected under *Van Buren v. United States* and *hiQ Labs v. LinkedIn*, but bypassing technical barriers (firewalls, CAPTCHAs, authenticated sessions) without authorization is illegal.
* **European Union:** General Data Protection Regulation (GDPR) mandates lawful processing of personal identifiable information (PII). Collecting, indexing, or redistributing EU citizens' personal data without a legitimate interest can result in administrative fines.
* **Ethics:** Never use exposed credentials found in breach databases to log into unauthorized systems. OSINT is observational; unauthorized access constitutes illegal intrusion.

---

## Module 02: Search Engines & Advanced Google Dorking

### 2.1 Boolean Search Heuristics
Search engines crawl and index trillions of documents. Advanced operators filter out 99.9% of irrelevant internet noise:

| Operator | Syntax | Function & Practical Use Case |
| :--- | :--- | :--- |
| `site:` | `site:target.com` | Restricts search strictly to a domain or top-level domain (e.g., `site:gov`) |
| `filetype:` | `filetype:pdf` | Limits results to specific document extensions (`pdf`, `docx`, `xlsx`, `env`, `sql`) |
| `inurl:` | `inurl:admin` | Locates strings embedded directly within the URL path or query parameters |
| `intitle:` | `intitle:"index of"` | Discovers web server directory listings and exposed file directories |
| `intext:` | `intext:"confidential"` | Searches for specific keywords within the visible body text of indexed pages |
| `cache:` | `cache:target.com` | Renders Google's cached snapshot of a page (useful for recently deleted pages) |
| `-` (NOT) | `site:target.com -www` | Excludes terms (e.g., excludes the primary website to surface subdomains) |
| `""` | `"internal use only"` | Enforces an exact verbatim phrase match |
| `OR` / `\|` | `ext:sql OR ext:bak` | Logical OR operation across multiple parameters |

### 2.2 High-Yield Cybersecurity Dorking Cheatsheet

```text
# 1. Exposed Directory Listings & Web Server Roots
site:target.com intitle:"index of /" OR intitle:"index of /admin"
site:target.com intitle:"index of" "parent directory"

# 2. Exposed Database Dumps & Configuration Files
site:target.com filetype:sql OR filetype:db OR filetype:sqlite OR filetype:mdb
site:target.com filetype:env "DB_PASSWORD" OR "AWS_SECRET_ACCESS_KEY"
site:target.com inurl:wp-config.php OR inurl:configuration.php OR inurl:settings.py

# 3. Sensitive Corporate Documents & PII
site:target.com filetype:xls OR filetype:xlsx "salary" OR "budget" OR "confidential"
site:target.com filetype:pdf "not for public distribution" OR "proprietary"

# 4. Exposed Log Files & Debug Telemetry
site:target.com filetype:log intext:"error" OR intext:"password" OR intext:"token"
site:target.com inurl:phpinfo.php OR inurl:info.php "PHP Version"

# 5. Cloud Storage Leaks (AWS S3, Azure Blob, Google Cloud Storage)
site:s3.amazonaws.com "target-company"
site:blob.core.windows.net "target-company"
site:storage.googleapis.com "target-company"
```

### 2.3 Alternative & Specialized Search Engines
* **Brave Search / Mojeek:** Independent search index engines that do not rely on Google or Bing crawl databases.
* **SearXNG:** Self-hosted, privacy-respecting metasearch engine combining results from 70+ search services without tracking queries.
* **Yandex:** Exceptional reverse image recognition capabilities and indexing of Eastern European/Russian networks.
* **Baidu:** Necessary for Asian/Chinese infrastructure, domains, and regional web platforms.

---

## Module 03: People & Identity Intelligence

### 3.1 Username Enumeration & Behavioral Profiling
Adversaries and targets frequently reuse usernames or handle variants (`johndoe`, `johndoe_sec`, `j_doe99`) across development, social, and gaming platforms.

### 3.2 Core Tools & Practical Execution

#### 1. Sherlock
Searches over 400 social platforms and sites via HTTP status checks and response signatures:

```bash
# Installation
sudo apt update && sudo apt install -y sherlock

# Scan target username across all platforms
sherlock target_alias --print-found

# Scan multiple candidate usernames and output to folder
sherlock user1 user2 user3 --folderoutput ./recon_results/
```

#### 2. Maigret
Maigret is an advanced fork of Sherlock that extracts user profile metadata (real names, bio, avatars, locations) and parses web pages for secondary links:

```bash
# Installation via pipx
pipx install maigret

# Deep search with parsing of profile metadata
maigret target_alias -a --parse-all

# Generate comprehensive HTML & JSON dossier report
maigret target_alias --html --json
```

#### 3. WhatsMyName
High-speed Python engine querying the WhatsMyName curated JSON signature database:

```bash
git clone https://github.com/WebBreacher/WhatsMyName.git
cd WhatsMyName
pip3 install -r requirements.txt
python3 whatsmyname.py -u target_alias
```

---

## Module 04: Email Intelligence & Header Forensics

### 4.1 Email Discovery & Account Binding
Given an email address (`analyst@target.com`), investigators determine:
1. Is the email address deliverable?
2. Which third-party online platforms (GitHub, Twitter, Spotify, Adobe) have an account registered with this address?
3. What is the associated Gravatar profile, avatar hash, or Google account ID?

### 4.2 Automated Email Reconnaissance Tools

#### 1. Holehe
Checks account registration status across 120+ platforms using password reset and signup endpoint side-channels without alerting the target:

```bash
# Installation
pipx install holehe

# Query email address
holehe target@example.com
```

#### 2. Epieos
Web service (`https://epieos.com/`) that queries Google account metadata, reveals linked Google Reviews, Google Maps edits, calendar availability, and profile photos from a simple email query.

#### 3. Hunter.io / Phonebook.cz
* **Hunter.io:** Identifies the corporate email formatting pattern (e.g., `{first}.{last}@company.com`) and lists all public indexed emails for an enterprise domain.
* **Phonebook.cz:** Free search interface indexing over 40 billion records from Intelligence X.

### 4.3 Email Header Forensic Analysis
During phishing and business email compromise (BEC) investigations, dissect the raw RFC 822 email header:

```text
Received: from mail-relay.attacker.com (mail-relay.attacker.com [198.51.100.45])
    by mx.google.com with ESMTPS id ...
    for <victim@target.com>; Mon, 14 Sep 2026 10:14:22 -0700 (PDT)
Authentication-Results: mx.google.com;
    dkim=pass header.i=@legitimate-partner.com;
    spf=fail (google.com: domain of sender@attacker.com does not designate 198.51.100.45 as permitted sender)
Return-Path: <spoofed@attacker.com>
Message-ID: <20260914171422.12345@attacker.com>
X-Originating-IP: [203.0.113.88]
```

#### Header Verification Checklist:
1. **Trace the `Received:` chain from bottom to top:** The bottom-most `Received:` line represents the original sending mail transfer agent (MTA) or mail client.
2. **SPF (Sender Policy Framework):** Verifies if the sending IP is authorized by the domain's DNS `v=spf1` TXT record.
3. **DKIM (DomainKeys Identified Mail):** Cryptographic signature verifying that the email content was not modified in transit.
4. **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** Specifies the receiving server's action (`none`, `quarantine`, `reject`) when SPF/DKIM fail.
5. **Inspect `X-Originating-IP`:** Captures the client IP behind webmail portals (Outlook Web App, roundcube).

---

## Module 05: Phone Number & Telecom Reconnaissance

### 5.1 Telecom Routing & E.164 Standards
International telecommunication numbers adhere to the ITU E.164 recommendation (e.g., `+[Country Code][Subscriber Number]`).

### 5.2 Investigative Vectors:
* **Carrier & Line Type:** Distinguish landline, cellular, and VoIP numbers (Google Voice, Skype, Twilio). VoIP numbers indicate burner accounts.
* **HLR (Home Location Register) Lookups:** Discloses the current Mobile Country Code (MCC), Mobile Network Code (MNC), and whether the SIM card is currently active or roaming.
* **Caller ID Aggregators:** Services like Truecaller, Whoscall, and Sync.ME crowdsource address books, revealing real names attached to unlisted numbers.

### 5.3 Automated Phone OSINT with PhoneInfoga

```bash
# Download and install PhoneInfoga binary
curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install | bash
sudo mv ./phoneinfoga /usr/local/bin/

# Scan single phone number
phoneinfoga scan -n "+14155552671"

# Launch local investigative web GUI
phoneinfoga serve -p 8080
```

---

## Module 06: Domain, DNS & Infrastructure OSINT

### 6.1 Domain Registration & RDAP
* **WHOIS:** Classical text-based protocol querying registrar databases on port 43. Frequently redacted due to GDPR.
* **RDAP (Registration Data Access Protocol):** RESTful, JSON-based replacement for WHOIS providing machine-readable registrar, registrant, and nameserver structures.

```bash
# Query RDAP via curl
curl -s "https://rdap.org/domain/example.com" | jq '{registrar: .entities[0].vcardArray[1][1][3], status: .status}'
```

### 6.2 DNS Anatomy & Command-Line Queries
The Domain Name System translates human-readable hostnames to IP addresses. It provides critical attack-surface intelligence:

```bash
# 1. Query IPv4 (A) and IPv6 (AAAA) records
dig +short A target.com
dig +short AAAA target.com

# 2. Query Mail Exchange (MX) records (Reveals email hosting: Office365, Google Workspace, on-prem)
dig +short MX target.com

# 3. Query Authoritative Nameservers (NS)
dig +short NS target.com

# 4. Query TXT records (Reveals SPF email routes, verification tokens, third-party SaaS bindings)
dig +short TXT target.com

# 5. Full Zone Transfer Attempt (AXFR - Test for misconfigured nameservers)
dig axfr @ns1.target.com target.com
```

```mermaid
flowchart TD
    D["target.com"]
    D -->|"A / AAAA"| IP["198.51.100.25 (Hosting Provider / CDN)"]
    D -->|"MX"| M["target-com.mail.protection.outlook.com (Office 365)"]
    D -->|"TXT"| S["v=spf1 include:sendgrid.net include:_spf.google.com ~all"]
    D -->|"NS"| NS["ns1.cloudflare.com (WAF / DDoS Shield)"]
    D -->|"SOA"| SOA["Admin Email: hostmaster.target.com"]

    style D fill:#1e293b,stroke:#00e5ff,color:#fff
    style IP fill:#0f172a,stroke:#ffab00,color:#fff
    style M fill:#0f172a,stroke:#00e676,color:#fff
    style S fill:#0f172a,stroke:#b388ff,color:#fff
    style NS fill:#0f172a,stroke:#ff5252,color:#fff
    style SOA fill:#0f172a,stroke:#90caf9,color:#fff
```

---

## Module 07: Subdomain Discovery & Attack Surface Mapping

### 7.1 Passive Subdomain Harvesting Mechanics
Attackers rarely breach well-guarded root domains (`target.com`). Instead, they target forgotten staging portals, developer testbeds, and legacy VPN appliances (`dev-api.target.com`, `vpn-legacy.target.com`).

### 7.2 Primary Toolchain

#### 1. Subfinder (ProjectDiscovery)
Blazing-fast passive subdomain discovery tool leveraging over 40 public APIs (AlienVault OTX, Chaos, Censys, VirusTotal):

```bash
# Installation
sudo apt install -y subfinder

# Passive scan across all passive sources
subfinder -d target.com -all -silent -o subdomains_subfinder.txt
```

#### 2. OWASP Amass
The industry benchmark in passive attack surface discovery and graph correlation:

```bash
# Installation
sudo apt install -y amass

# Passive enumeration without sending traffic to target
amass enum -passive -d target.com -o subdomains_amass.txt
```

#### 3. Certificate Transparency (CT) Log Mining
Whenever a Certificate Authority issues a TLS certificate, it must log the issuance to public Certificate Transparency logs. This allows analysts to discover newly created internal subdomains instantly:

```bash
# Query crt.sh API via curl and parse with jq
curl -s "https://crt.sh/?q=%.target.com&output=json" | \
  jq -r '.[].name_value' | \
  sed 's/\*\.//g' | \
  sort -u > subdomains_crtsh.txt
```

#### 4. Unified Discovery Pipeline

```bash
# High-Throughput Aggregation Bash Pipeline
subfinder -d target.com -silent | \
  assetfinder --subs-only | \
  anew subdomains_raw.txt

cat subdomains_raw.txt | sort -u | dnsx -silent -a -resp -o resolved_hosts.txt
```

---

## Module 08: Network Scanners & Internet-Wide Telemetry

### 8.1 Shodan: The Search Engine for Internet-Connected Devices
Shodan continuously crawls the entire IPv4 address space, sending service probes and indexing raw banner responses from ports 1 to 65535.

#### Master Shodan Filters & Syntax:

| Filter | Example | Description |
| :--- | :--- | :--- |
| `net:` | `net:198.51.100.0/24` | Scans an entire CIDR network block |
| `org:` | `org:"Target Corporation"` | Filters by registered organization name in BGP/WHOIS |
| `ssl:` | `ssl:"target.com"` | Matches certificates containing the target's domain name |
| `port:` | `port:3389,8080,445` | Filters specific exposed network ports |
| `has_vuln:true` | `has_vuln:true org:"Target"` | Surfaces hosts with known unpatched CVEs |
| `product:` | `product:"Apache httpd"` | Filters by specific software daemon |
| `http.title:` | `http.title:"Dashboard"` | Searches for specific title strings in HTML responses |

```bash
# Shodan CLI Setup
pip install shodan
shodan init YOUR_SHODAN_API_KEY

# Query host details and open ports
shodan host 198.51.100.14

# Search for exposed ElasticSearch clusters with no authentication
shodan search "port:9200 json:\"cluster_name\"" --fields ip_str,port,org
```

### 8.2 Censys
Censys monitors public certificates and hosts with deep protocol dissections (HTTP/2, SSH, SMB, TLS):

```bash
# Censys CLI search
censys search "services.tls.certificates.leaf_data.subject.common_name: target.com"
```

### 8.3 GreyNoise: Separating Targeted Attacks from Mass Scanners
GreyNoise categorizes Internet noise—differentiating benign crawlers (Shodan, Qualys, Censys), indiscriminate malicious worms (Mirai, mass exploiters), and stealthy targeted traffic.

```bash
# Query IP reputation
greynoise ip 198.51.100.14
```

---

## Module 09: Web Application & Technology Profiling

### 9.1 Framework & Header Fingerprinting
Understanding the target's software stack reveals known CVE attack vectors:
* **HTTP Response Headers:** `Server: nginx/1.18.0`, `X-Powered-By: PHP/7.4`, `Set-Cookie: PHPSESSID` (PHP), `csrftoken` (Django), `JSESSIONID` (Java/Spring).
* **HTML DOM Signatures:** Script source paths (`/wp-content/themes/` indicates WordPress, `_next/static/` indicates Next.js).

### 9.2 Tooling:
* **Wappalyzer CLI:** Analyzes HTML, headers, cookies, and scripts:
  ```bash
  wappalyzer https://target.com
  ```
* **urlscan.io:** Automated headless browser crawler executing JavaScript, capturing DOM snapshots, loaded external resources, outbound connections, and full page screenshots:
  ```bash
  curl -s -X POST "https://urlscan.io/api/v1/scan/" \
    -H "Content-Type: application/json" \
    -H "API-Key: $URLSCAN_API_KEY" \
    -d '{"url": "https://target.com", "visibility": "public"}'
  ```

---

## Module 10: Social Media Intelligence (SOCMINT)

### 10.1 Corporate Footprint & Employee Target Mapping
SOCMINT gathers operational intelligence from human assets:

```mermaid
flowchart TD
    LI["LinkedIn Corporate Page"] --> HR["Employee Directory & Roles"]
    HR --> ORG["Org Chart & Tech Stack Roles\n(e.g., 'AWS DevOps Engineer')"]
    ORG --> EX["Identify Key Admins & C-Level"]
    EX --> TW["Twitter / X Personal Profiles\n(Operational complaints, hobbies)"]
    EX --> GH["Personal GitHub Repositories\n(Accidental internal code uploads)"]
    EX --> TG["Telegram / Discord Participation"]

    style LI fill:#1e293b,stroke:#00e5ff,color:#fff
    style HR fill:#0f172a,stroke:#ffab00,color:#fff
    style ORG fill:#0f172a,stroke:#00e676,color:#fff
    style EX fill:#0f172a,stroke:#b388ff,color:#fff
    style TW fill:#0f172a,stroke:#ff5252,color:#fff
    style GH fill:#0f172a,stroke:#90caf9,color:#fff
    style TG fill:#0f172a,stroke:#f48fb1,color:#fff
```

### 10.2 Platform-Specific Techniques:
* **LinkedIn:** Search `site:linkedin.com/in/ "Target Company" "Software Engineer"` to bypass LinkedIn viewing limits.
* **X/Twitter Advanced Queries:**
  ```text
  from:TargetUser since:2025-01-01 until:2025-12-31
  to:TargetUser "vpn" OR "bug" OR "outage"
  ```
* **Telegram OSINT:** Threat actors communicate via public Telegram channels. Tools like **TGStat** (`https://tgstat.com/`) and **Telemetr** archive and index channel messages, forward chains, and user lists.
* **Reddit:** Utilize **PullPush** / **Pushshift** archives to review deleted posts and comments from corporate handles or developers discussing internal architecture problems.

---

## Module 11: Code Repository & Secret Exposure OSINT

### 11.1 The GitHub Attack Surface
Developers frequently upload sensitive enterprise keys, database passwords, and internal staging URLs to public personal GitHub repositories or commit histories.

### 11.2 High-Impact GitHub Search Dorks

```text
"target.com" filename:.env
"target.com" filename:wp-config.php
"target.com" extension:pem "PRIVATE KEY"
"target.com" "password =" OR "api_key ="
"target.com" "AWS_SECRET_ACCESS_KEY"
org:target-company "Authorization: Bearer"
```

### 11.3 Automated Secret Hunting Tools

#### 1. GitLeaks
Blazing-fast SAST engine for auditing git repositories for hardcoded secrets, API tokens, and private keys:

```bash
# Installation
sudo apt install -y gitleaks

# Audit remote public repository commit history
gitleaks detect --source https://github.com/developer/repo --verbose
```

#### 2. TruffleHog
Deep scanner that checks entropy and verifies if discovered API keys are **active and valid**:

```bash
# Run TruffleHog on a git repo
trufflehog git https://github.com/developer/repo --json
```

---

## Module 12: Breach Intelligence & Dark Web Monitoring

### 12.1 Credential Exposure Analysis
When third-party services suffer data breaches (LinkedIn, Dropbox, Canva), hashed and plaintext passwords circulate among cybercriminals. Threat actors test these credentials in **Credential Stuffing** attacks.

### 12.2 Breach Telemetry Platforms:
* **Have I Been Pwned (HIBP):** Industry standard maintaining records of billions of compromised accounts.
  ```bash
  # Query HIBP API v3
  curl -s "https://haveibeenpwned.com/api/v3/breachedaccount/target@corp.com" \
    -H "hibp-api-key: $HIBP_KEY" -H "user-agent: OSINT-App" | jq .
  ```
* **DeHashed / Hudson Rock:** Advanced platforms indexing parsed breaches, revealing partial hashes, associated usernames, IP addresses, and Infostealer malware logs (RedLine, Vidar, Lumma).

### 12.3 Dark Web (.onion) Reconnaissance
* **Tor Network:** Onion services provide anonymity for underground leak sites, ransomware extortion portals, and hacking forums.
* **Ahmia (`http://juhanurmih5wuprs5hxakybmamflzgapqbgystepehduw62crlobadjyd.onion/`):** Clearnet-accessible search engine for Tor services.
* **Ransomwatch / Ransomware.live:** Automated aggregators that monitor and archive ransomware gang leak sites, alerting organizations if their name appears on an extortion showcase.

---

## Module 13: Cryptocurrency & Blockchain Forensics

### 13.1 Blockchain Architecture & Ledger Openness
Unlike traditional banking systems, public blockchains (Bitcoin, Ethereum, Solana) are **immutable, decentralized public ledgers**. Every transaction, fee, timestamp, and wallet address is accessible to investigators.

### 13.2 Core Concepts:
* **UTXO Model (Bitcoin):** Unspent Transaction Outputs. Bitcoins exist as outputs from prior transactions. Transactions consume inputs and generate new outputs.
* **Account Model (Ethereum):** Global state where accounts maintain live balances and execute bytecode within smart contracts.
* **Clustering Heuristics:**
  1. *Common Input Ownership:* If Transaction A spends UTXOs from Address 1 and Address 2 together as inputs, both addresses belong to the same wallet entity.
  2. *Change Address Heuristic:* The remaining change output returns to an address controlled by the sender.

### 13.3 Blockchain Explorers & Analytical Platforms:
* **Mempool.space:** Real-time Bitcoin transaction explorer, fee tracker, and address visualizer.
* **Etherscan.io:** Comprehensive explorer for Ethereum transactions, ERC-20 token transfers, and verified Solidity source code.
* **Arkham Intelligence (`https://platform.arkhamintelligence.com/`):** Deanonymization platform linking public addresses to institutional entities, mixers, exchanges, and cybercrime syndicates.

---

## Module 14: Corporate, Business & Legal OSINT

### 14.1 Corporate Entity Structure
Enterprises operate complex corporate hierarchies: holding companies, shell corporations, joint ventures, and international subsidiaries.

### 14.2 Registry Portals:
* **OpenCorporates:** The largest open database of corporate entities globally (>220 million companies). Maps registered directors, active status, incorporation dates, and registered agent addresses.
* **SEC EDGAR (United States):** Public corporate disclosures:
  * **Form 10-K:** Annual comprehensive financial report detailing corporate structure, physical facilities, and risk disclosures.
  * **Form 8-K:** Material unscheduled events (e.g., disclosure of a cyber incident).
* **ImportYeti (`https://www.importyeti.com/`):** Visualizes ocean freight bill-of-lading shipment records, revealing a company's international supply chain, suppliers, logistics routes, and partners.
* **CourtListener / PACER:** United States Federal court dockets, pleadings, and civil/criminal litigation records.

---

## Module 15: Geospatial Intelligence (GEOINT) & Satellite Imagery

### 15.1 The Art of Geolocation
GEOINT determines the exact physical location where a photograph or video was captured by cross-referencing environmental features:

```mermaid
flowchart LR
    IMG["Photograph Target"] --> EX["1. Check EXIF GPS Data"]
    IMG --> BD["2. Built Environment\n(Architecture, signage, road markings)"]
    IMG --> NAT["3. Natural Environment\n(Mountain silhouettes, vegetation)"]
    IMG --> SUN["4. Chronolocation\n(Sun position, shadow angles)"]
    
    EX --> MAP["Plot Exact Coordinates\n(Google Earth / OpenStreetMap)"]
    BD --> MAP
    NAT --> MAP
    SUN --> MAP

    style IMG fill:#1e293b,stroke:#00e5ff,color:#fff
    style EX fill:#0f172a,stroke:#ffab00,color:#fff
    style BD fill:#0f172a,stroke:#00e676,color:#fff
    style NAT fill:#0f172a,stroke:#b388ff,color:#fff
    style SUN fill:#0f172a,stroke:#ff5252,color:#fff
    style MAP fill:#0f172a,stroke:#90caf9,color:#fff
```

### 15.2 Chronolocation with SunCalc
Shadow length and angle reveal the exact time and orientation of a photograph:
* **SunCalc (`https://www.suncalc.org/`):** Simulates sun position, sunrise/sunset times, azimuth, and shadow lengths for any coordinate on Earth at any historical date and time.
* By aligning a building's shadow angle in a photograph against SunCalc's azimuth overlay, you can pinpoint the hour and minute of capture.

### 15.3 Overpass Turbo (OpenStreetMap Query Language)
Query OpenStreetMap for specific physical combinations (e.g., "find all two-lane roads near a church and a cell tower in this region"):

```text
[out:json];
(
  node["amenity"="place_of_worship"](around:500, 37.7749, -122.4194);
  node["man_made"="tower"](around:500, 37.7749, -122.4194);
);
out body;
```

---

## Module 16: Image Forensics & Reverse Visual Search

### 16.1 EXIF Metadata Extraction
Exchangeable Image File Format (EXIF) stores camera settings, lens model, timestamps, software, and GPS coordinates inside image files.

```bash
# Install ExifTool
sudo apt install -y exiftool

# Extract all metadata tags including GPS
exiftool -GPS* -DateTimeOriginal -Make -Model target_image.jpg

# Export raw coordinates formatted for Google Maps
exiftool -c "%.6f" -p "$GPSLatitude, $GPSLongitude" target_image.jpg
```

> **Note:** Major social media networks (Twitter, Facebook, Instagram) strip EXIF metadata on upload to protect user privacy. Raw images shared via messaging apps (as uncompressed documents), cloud drives, or email attachments retain full EXIF data.

### 16.2 Error Level Analysis (ELA)
* **FotoForensics (`https://fotoforensics.com/`):** ELA highlights differences in compression levels across an image. Edited or spliced areas compress at different error rates than the original background, surfacing digital manipulation.

### 16.3 Reverse Image Engines
* **Google Lens:** General visual recognition (identifies consumer products, landmarks, street signs).
* **Yandex Visual Search:** The most powerful reverse image engine for faces, clothing, and background landmarks.
* **PimEyes / FaceCheck.ID:** Facial recognition engines matching faces against billions of indexed websites.

---

## Module 17: Video & Audio OSINT Verification

### 17.1 Video Verification Architecture
Videos are sequences of static frames accompanied by audio tracks. Video OSINT requires breaking media down into individual components:

1. **Extraction & Preservation:** Use `yt-dlp` to download media at maximum available quality:
   ```bash
   yt-dlp -f bestvideo+bestaudio --write-thumbnail --write-info-json "https://video-url"
   ```
2. **Keyframe Splitting with InVID / WeVerify:**
   * Browser extension developed for journalists to extract keyframes from web video streams.
   * Keyframes are subjected to reverse image searches to identify original upload dates and historical footage reuse.
3. **Frame-by-Frame Extraction via FFmpeg:**
   ```bash
   # Extract 1 frame per second as high-resolution PNG
   ffmpeg -i video.mp4 -r 1 -f image2 frame_%04d.png
   ```

### 17.2 Audio Analysis & Transcription
* **FFmpeg Audio Demuxing:**
  ```bash
  ffmpeg -i video.mp4 -vn -acodec copy audio_track.aac
  ```
* **Whisper AI:** Open-source automatic speech recognition (ASR) to transcribe and translate audio in foreign languages:
  ```bash
  pip install openai-whisper
  whisper audio_track.aac --model medium --language auto
  ```

---

## Module 18: Threat Intelligence & CTI Frameworks

### 18.1 Cyber Threat Intelligence (CTI) Mechanics
CTI converts raw data into actionable context regarding adversary intent, capabilities, and infrastructure.

```mermaid
flowchart TD
    T["Threat Actor / APT"] --> C["Campaign"]
    C --> TTP["MITRE ATT&CK Techniques\n(T1566 Phishing, T1059 Scripting)"]
    TTP --> IOC["Indicators of Compromise (IOCs)\n(IPs, Domains, Hashes, SSL Certs)"]
    IOC --> MISP["MISP / STIX 2.1 Threat Sharing"]
    MISP --> DEF["SOC & EDR Detection Rules\n(Sigma, YARA, Snort)"]

    style T fill:#1e293b,stroke:#ff5252,color:#fff
    style C fill:#1e293b,stroke:#ffab00,color:#fff
    style TTP fill:#1e293b,stroke:#00e5ff,color:#fff
    style IOC fill:#0f172a,stroke:#00e676,color:#fff
    style MISP fill:#0f172a,stroke:#b388ff,color:#fff
    style DEF fill:#0f172a,stroke:#90caf9,color:#fff
```

### 18.2 Industry CTI Standards & Sharing Platforms:
* **STIX 2.1 (Structured Threat Information Expression):** Standardized JSON schema for exchanging cyber threat intelligence.
* **TAXII 2.1 (Trusted Automated eXchange of Intelligence Information):** Application layer protocol over HTTPS to exchange STIX data.
* **MISP (Malware Information Sharing Platform):** Open-source platform for sharing indicators, malware telemetry, and threat actor profiles among trust circles.
* **AlienVault OTX (Open Threat Exchange):** Free community CTI platform crowdsourcing pulses of active IOCs.
* **CISA KEV (Known Exploited Vulnerabilities Catalog):** Authoritative database of vulnerabilities actively leveraged in the wild by threat actors.

---

## Module 19: Link Analysis & Visual Graph Correlation

### 19.1 Visual Graph Analysis Concepts
Humans struggle to identify patterns across thousands of disconnected rows in spreadsheets. Graph analysis connects nodes (entities) via directed edges (relationships):
```text
(Person: Jane Doe) --[REGISTERED]--> (Domain: dev-target.com)
(Domain: dev-target.com) --[RESOLVES_TO]--> (IP: 198.51.100.22)
(IP: 198.51.100.22) --[EXPOSES]--> (Port: 22 / OpenSSH)
```

### 19.2 Industry Link Analysis Software:
* **Maltego:** The industry gold standard for visual link analysis. Uses **Transforms** (API queries) to dynamically pivot from an IP to a Netblock, a Netblock to an Organization, or an Email to Social Profiles.
* **Gephi:** Open-source network visualization tool computing modularity, betweenness centrality, and graph clustering to identify key influencers or hub servers in massive datasets.
* **Neo4j:** Graph database utilizing the Cypher query language to query complex multi-hop relationships at enterprise scale:
  ```cypher
  MATCH (p:Person)-[:OWNS]->(d:Domain)-[:RESOLVES_TO]->(ip:IP)
  WHERE ip.country = 'RU'
  RETURN p, d, ip;
  ```

---

## Module 20: Automated Frameworks & Professional Intelligence Reporting

### 20.1 Reconnaissance Automation Frameworks

#### 1. Recon-ng
Modular, interactive reconnaissance framework mirroring the Metasploit interface:

```bash
# Launch Recon-ng
recon-ng

# Workflow commands inside recon-ng console
[recon-ng][default] > workspaces create TargetEngagement
[recon-ng][TargetEngagement] > modules load recon/domains-hosts/brute_hosts
[recon-ng][TargetEngagement] > options set SOURCE target.com
[recon-ng][TargetEngagement] > run
[recon-ng][TargetEngagement] > show hosts
```

#### 2. FinalRecon
Fast Python reconnaissance framework providing comprehensive domain, header, WHOIS, DNS, and SSL profiling in one pass:

```bash
finalrecon --full https://target.com
```

### 20.2 Professional OSINT Intelligence Dossier Template

When completing an engagement, document your findings using an executive-ready intelligence reporting format:

```markdown
# EXECUTIVE THREAT INTELLIGENCE DOSSIER

## 1. ENGAGEMENT METADATA
* Target Organization / Subject: [Organization Name]
* Investigation Scope: [Primary Domains, Infrastructure Ranges, Key Personas]
* Analyst Identifier: [Analyst Name / Call-Sign]
* Assessment Date: [YYYY-MM-DD]
* Classification: TLP:AMBER (Restricted to Authorized Stakeholders)

## 2. EXECUTIVE SUMMARY
[High-level summary of findings: Critical vulnerabilities discovered, exposed sensitive keys, compromised employee credentials, and executive exposure level.]

## 3. THREAT EXPOSURE MATRIX
| Finding | Asset Affected | Risk Level | Evidence / IOC | Remediation |
| :--- | :--- | :---: | :--- | :--- |
| Exposed AWS API Key | GitHub Repository | 🔴 Critical | AKIAIOSFODNN7EXAMPLE | Revoke IAM Key, Cycle Secrets |
| Pulse Secure SSL-VPN CVE | 198.51.100.14:443 | 🔴 Critical | CVE-2019-11510 | Patch Firmware Immediately |
| Breached C-Level Passwords | Active Directory | 🟠 High | 24 Cleartext Creds | Force Enterprise Password Reset |

## 4. INFRASTRUCTURE & ATTACK SURFACE TOPOLOGY
* Discovered Subdomains: [Count]
* Exposed Autonomous Systems (ASNs): [ASN List]
* Cloud Assets Identified: [S3 Buckets, Azure Blobs, GCP Instances]

## 5. IDENTITY & CREDENTIAL EXPOSURE
* Publicly Exposed Employee Emails: [List]
* Infostealer Logs Identified: [Malware Variants]

## 6. TIMELINE & PIVOT CHAIN
[Mermaid diagram or narrative documenting the step-by-step path taken from the initial indicator to the compromise finding.]

## 7. RECOMMENDED MITIGATION PLAYBOOK
1. Immediate Containment Controls (0-24 Hours)
2. Tactical Hardening Policies (1-7 Days)
3. Strategic Governance & Policy Enhancements (30 Days)
```

---

<div align="center">

**🎯 Open Source Intelligence (OSINT) Framework Complete — 20 Operational Domains**

*Ethical • Actionable • Enterprise-Grade Cyber Threat Intelligence*

</div>
