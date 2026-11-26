import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
PHASES_DIR = os.path.join(IMAGES_DIR, "phases")
MODULES_DIR = os.path.join(IMAGES_DIR, "modules")
BANNERS_DIR = os.path.join(IMAGES_DIR, "module_banners")
BG_DIR = os.path.join(IMAGES_DIR, "backgrounds")

for d in (IMAGES_DIR, PHASES_DIR, MODULES_DIR, BANNERS_DIR, BG_DIR):
    os.makedirs(d, exist_ok=True)

FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_MONO = r"C:\Windows\Fonts\consola.ttf"
FONT_MONO_BOLD = r"C:\Windows\Fonts\consolab.ttf"

if not os.path.exists(FONT_REG):
    FONT_REG = r"C:\Windows\Fonts\arial.ttf"
    FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
if not os.path.exists(FONT_MONO):
    FONT_MONO = FONT_REG
    FONT_MONO_BOLD = FONT_BOLD


def get_font(size, bold=False, mono=False):
    if mono:
        fpath = FONT_MONO_BOLD if bold else FONT_MONO
    else:
        fpath = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(fpath, size)
    except Exception:
        return ImageFont.load_default()


def hex_to_rgba(h, alpha=255):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), alpha)


def draw_badge(draw, x, y, text, bg_color, text_color="#ffffff", font_size=14, pad_x=11, pad_y=5, radius=6):
    fnt = get_font(font_size, bold=True)
    bbox = fnt.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    bw = tw + pad_x * 2
    bh = th + pad_y * 2
    box = [x, y, x + bw, y + bh]
    fill_val = hex_to_rgba(bg_color) if isinstance(bg_color, str) else bg_color
    t_fill = hex_to_rgba(text_color) if isinstance(text_color, str) else text_color
    draw.rounded_rectangle(box, radius=radius, fill=fill_val)
    draw.text((x + pad_x - bbox[0], y + pad_y - bbox[1]), text, fill=t_fill, font=fnt)
    return box[2], box[3]


def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    cur = []
    for w in words:
        trial = " ".join(cur + [w])
        bbox = font.getbbox(trial)
        if (bbox[2] - bbox[0]) <= max_width or not cur:
            cur.append(w)
        else:
            lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def draw_vector_bolt(draw, cx, cy, scale=1.0, fill="#38bdf8"):
    pts = [
        (cx + 3 * scale, cy - 8 * scale),
        (cx - 5 * scale, cy + 1 * scale),
        (cx + 0 * scale, cy + 1 * scale),
        (cx - 3 * scale, cy + 8 * scale),
        (cx + 5 * scale, cy - 1 * scale),
        (cx + 0 * scale, cy - 1 * scale),
    ]
    draw.polygon(pts, fill=fill)


def draw_vector_chevron(draw, x, y, size=6, fill="#00d4ff"):
    pts = [
        (x, y),
        (x + size, y + size // 2),
        (x, y + size),
        (x + size // 3, y + size // 2),
    ]
    draw.polygon(pts, fill=fill)


MODULES = [
    {
        "id": "01",
        "title": "Introduction to Ethical Hacking",
        "banner_title": "Module 01: Introduction to Ethical Hacking",
        "banner_sub": "InfoSec Fundamentals, CIA/AAA Security Models, Cyber Warfare & AI-Driven Pentesting",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "pill_label": "PHASE 1 • FOUNDATIONS",
        "phase_color": "#00d4ff",
        "banner_accent": "#00d4ff",
        "concepts": [
            "CIA Triad, AAA Security Model & Non-Repudiation",
            "Adversary Kill Chains: Cyber Kill Chain & Diamond Model",
            "Information Warfare: Defensive vs Offensive Tactics",
            "AI-Powered Pentesting & Generative Security Tools",
        ],
        "tools": "PentestGPT · CyberChef · MISP · STIX/TAXII",
        "exam_focus": "CIA Triad, Hacker classes, Kill Chain phases, Legal/SLA boundaries",
        "banner_cards": [
            ("CIA & AAA SECURITY PILLARS", "Confidentiality, Integrity, Availability, Authentication, Authorization, Auditing, and Non-Repudiation formulas."),
            ("CYBER KILL CHAIN MODELS", "Lockheed Martin 7-stage Kill Chain, Unified Kill Chain (UKC), and MITRE ATT&CK integration."),
            ("THREAT INTEL & DIAMOND MODEL", "Adversary, Capability, Infrastructure, Victim correlations, IOC taxonomy, and strategic CTI feeds."),
            ("AI IN ETHICAL HACKING", "Generative AI security toolchains, PentestGPT, automated attack surface discovery, and LLM defenses."),
        ],
    },
    {
        "id": "02",
        "title": "Footprinting and Reconnaissance",
        "banner_title": "Module 02: Footprinting and Reconnaissance",
        "banner_sub": "Passive & Active OSINT, Domain Enumeration, Search Engine Dorking & Threat Recon",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "pill_label": "PHASE 1 • RECONNAISSANCE",
        "phase_color": "#00d4ff",
        "banner_accent": "#00d4ff",
        "concepts": [
            "Passive & Active OSINT Gathering Frameworks",
            "Advanced Google Dorking & Search Operators",
            "DNS Reconnaissance, WHOIS Queries & BGP IP Blocks",
            "Subdomain Harvesting & Email Header Tracking",
        ],
        "tools": "Maltego · Recon-ng · theHarvester · Shodan · Amass",
        "exam_focus": "Google dorks, DNS record types (SOA, MX, TXT), Whois interrogation",
        "banner_cards": [
            ("SEARCH ENGINE DORKING", "Advanced Google operators, cache mining, directory index hunting, and filetype leaks."),
            ("CYBER SEARCH ENGINES", "Shodan, Censys, FOFA, and ZoomEye telemetry queries for exposed infrastructure."),
            ("DOMAIN & DNS OSINT", "WHOIS registrars, DNS record interrogation, sub-domain brute forcing, and Certificate Transparency."),
            ("ORGANIZATIONAL FOOTPRINTING", "Employee profiling via LinkedIn, email harvesting (theHarvester), and social engineering vectors."),
        ],
    },
    {
        "id": "03",
        "title": "Scanning Networks",
        "banner_title": "Module 03: Scanning Networks",
        "banner_sub": "TCP 3-Way Handshake, Packet Crafting, Port Scanning, Nmap Timing & OS Fingerprinting",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "pill_label": "PHASE 1 • NETWORK SCANNING",
        "phase_color": "#00d4ff",
        "banner_accent": "#3b82f6",
        "concepts": [
            "TCP 3-Way Handshake & Flag States (SYN, ACK, FIN, RST)",
            "Stealth Scans: SYN Stealth (-sS), Xmas (-sX), FIN (-sF)",
            "Active Host Discovery & UDP Ping Sweeps",
            "TCP/IP Stack Fingerprinting & OS Detection",
        ],
        "tools": "Nmap · Hping3 · Masscan · ZMap · Angry IP",
        "exam_focus": "Nmap switches (-sS, -sT, -sU, -A), RFC 793 RST responses, Hping3 crafting",
        "banner_cards": [
            ("TCP/IP PACKET MECHANICS", "Header dissection, TCP flags (SYN, ACK, FIN, RST, PSH, URG), and 3-way handshake states."),
            ("PORT SCANNING TAXONOMY", "TCP Connect, SYN Stealth (-sS), FIN, XMAS, NULL, Idle/Zombie scans, and SCTP probes."),
            ("NMAP ENGINE & SCRIPTING (NSE)", "Service banner grabbing (-sV), OS fingerprinting (-O), NSE vulnerability scripts, and timing (-T0 to -T5)."),
            ("PACKET CRAFTING & EVASION", "Custom packet generation using Hping3, Scapy, MTU fragmentation, and source IP spoofing."),
        ],
    },
    {
        "id": "04",
        "title": "Enumeration",
        "banner_title": "Module 04: Enumeration",
        "banner_sub": "Service Interrogation, NetBIOS, SMB, SNMP, LDAP, SMTP, DNS & RPC Protocol Probing",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "pill_label": "PHASE 1 • ENUMERATION",
        "phase_color": "#00d4ff",
        "banner_accent": "#6366f1",
        "concepts": [
            "NetBIOS Name Service (137-139) & Name Suffixes",
            "SMB Null Sessions, IPC$ Shares & RID Cycling",
            "SNMP Community Strings (public/private) & MIB Traversal",
            "LDAP Queries, NTP Monlist Amplification, SMTP (VRFY/EXPN)",
        ],
        "tools": "Enum4linux · Nbtstat · Snmpwalk · Ldapsearch · Rpcclient",
        "exam_focus": "NetBIOS codes (<00>, <20>, <1B>), SNMPv1 vs v3 security, RID range calculation",
        "banner_cards": [
            ("NETBIOS & SMB ENUMERATION", "Null session exploitation, share harvesting, Nbtstat, enum4linux-ng, and CrackMapExec."),
            ("SNMP INFRASTRUCTURE MINING", "Management Information Base (MIB), community strings (public/private), snmpwalk, and OID queries."),
            ("LDAP & ACTIVE DIRECTORY", "Querying Directory Service endpoints, user accounts, groups, and domain architecture via LDAP."),
            ("SMTP, DNS & RPC PROBING", "VRFY/EXPN email verification, unauthenticated DNS zone transfers (AXFR), and rpcclient RPC binding."),
        ],
    },
    {
        "id": "05",
        "title": "Vulnerability Analysis",
        "banner_title": "Module 05: Vulnerability Analysis",
        "banner_sub": "Vulnerability Assessment Lifecycle, CVE/NVD Scoring, CVSS v3/v4 & Scanner Operations",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "pill_label": "PHASE 1 • VULN ASSESSMENT",
        "phase_color": "#00d4ff",
        "banner_accent": "#8b5cf6",
        "concepts": [
            "Vulnerability Assessment Lifecycle & Pre-Assessment Setup",
            "CVSS v3.1 & v4 Scoring Metrics (Base, Temporal, Env)",
            "CVE Identifiers & National Vulnerability Database (NVD)",
            "Vulnerability Classification: Design vs Config Flaws",
        ],
        "tools": "Nessus · OpenVAS · QualysGuard · Nikto · GFI LanGuard",
        "exam_focus": "CVSS calculation vectors (AV, AC, PR, UI, S, C, I, A), False positive handling",
        "banner_cards": [
            ("VULNERABILITY LIFECYCLE", "Pre-assessment scoping, automated scanning, vulnerability verification, analysis, and reporting."),
            ("CVE & CVSS METRIC ENGINE", "Base, Temporal, Environmental metrics, vector strings, and Common Vulnerability Scoring System (v3/v4)."),
            ("ENTERPRISE SCANNER AUDIT", "Credentialed vs. non-credentialed scans in Tenable Nessus, OpenVAS, Qualys, and Rapid7 Nexpose."),
            ("TRIAGE & REMEDIATION SLAS", "Remediating critical exposures, mitigating false positives, and patch management prioritization."),
        ],
    },
    {
        "id": "06",
        "title": "System Hacking",
        "banner_title": "Module 06: System Hacking",
        "banner_sub": "Privilege Escalation, Password Cracking, Pivoting, Rootkits & Log Wiping Tradecraft",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "pill_label": "PHASE 2 • SYSTEM EXPLOITATION",
        "phase_color": "#ff385c",
        "banner_accent": "#ef4444",
        "concepts": [
            "Password Cracking: Pass-The-Hash, LLMNR/NBT-NS Poisoning",
            "Buffer Overflow Exploitation & Shellcode Injection",
            "Privilege Escalation (UAC Bypass, DLL Hijacking, Token Abuse)",
            "Covering Tracks: Clearing EVTX Logs, Auditpol, ADS",
        ],
        "tools": "Responder · Mimikatz · John the Ripper · Hashcat · Metasploit",
        "exam_focus": "SAM database structure, NTLM hash anatomy, Pass-The-Hash mechanics",
        "banner_cards": [
            ("AUTHENTICATION BREAKING", "Offline hash cracking (Hashcat, John the Ripper), rainbow tables, and Pass-the-Hash (PtH)."),
            ("PRIVILEGE ESCALATION", "Windows Token Manipulation, Unquoted Service Paths, Linux Sudoers abuse, SUID binaries, and kernel bugs."),
            ("PIVOTING & LATERAL MOVEMENT", "Port forwarding, SSH tunneling, proxychains, and Meterpreter routing across segmented subnets."),
            ("COVERING TRACKS & ROOTKITS", "Disabling Windows Event Logs, auditd tampering, Timestomping metadata, and kernel-mode rootkits."),
        ],
    },
    {
        "id": "07",
        "title": "Malware Threats",
        "banner_title": "Module 07: Malware Threats",
        "banner_sub": "Trojans, Ransomware, Worms, Polymorphic Crypters & Dynamic Sandboxing Analysis",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "pill_label": "PHASE 2 • MALWARE ANALYSIS",
        "phase_color": "#ff385c",
        "banner_accent": "#dc2626",
        "concepts": [
            "Trojans, Viruses, Worms, Rootkits & Ransomware Lifecycles",
            "Crypters, Packers, Wrappers & Code Obfuscation",
            "Botnet Command & Control (C2) Architectures (IRC/HTTP/P2P)",
            "Static & Dynamic Malware Analysis in Isolated Sandboxes",
        ],
        "tools": "Ghidra · IDA Pro · PEStudio · Cuckoo Sandbox · Any.Run",
        "exam_focus": "Malware classification, Dropper vs Downloader, PE header analysis",
        "banner_cards": [
            ("MALWARE TAXONOMY & ANATOMY", "Droppers, loaders, banking trojans, RATs, worms, botnets, and Command-and-Control architectures."),
            ("RANSOMWARE OPERATIONS", "Asymmetric file encryption, Volume Shadow Copy destruction, payment portals, and double extortion."),
            ("EVASION & CODE OBFUSCATION", "Packers, polymorphic crypters, in-memory execution, anti-VM checks, and anti-debugging tricks."),
            ("STATIC & DYNAMIC TRIAGE", "PE header analysis, section entropy, string harvesting, and automated Cuckoo/REMnux sandboxing."),
        ],
    },
    {
        "id": "08",
        "title": "Sniffing",
        "banner_title": "Module 08: Sniffing",
        "banner_sub": "Packet Capture, MAC Flooding, ARP Poisoning, DHCP Starvation & Wireshark Forensics",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "pill_label": "PHASE 2 • PACKET SNIFFING",
        "phase_color": "#ff385c",
        "banner_accent": "#f97316",
        "concepts": [
            "Passive vs Active Sniffing in Switched Networks",
            "MAC Flooding (CAM Table Exhaustion) & Switch Port Security",
            "ARP Poisoning & Man-in-the-Middle (MitM) Interception",
            "DHCP Starvation, Rogue DHCP Servers & DNS Spoofing",
        ],
        "tools": "Wireshark · Ettercap · Bettercap · Macof · Yersinia · TCPDump",
        "exam_focus": "CAM overflow mitigation (Port Security), Gratuitous ARP, Wireshark filters",
        "banner_cards": [
            ("LAYER 2 SWITCH ATTACKS", "CAM table exhaustion, MAC flooding (macof), switch port stealing, and VLAN hopping."),
            ("ARP CACHE POISONING (MITM)", "Gratuitous ARP spoofing, bidirectional traffic redirection using arpspoof and Ettercap."),
            ("DHCP ATTACK VECTORS", "DHCP pool starvation, rogue DHCP server & gateway injection, and WPAD proxy hijacking."),
            ("TRAFFIC ANALYSIS & FORENSICS", "Wireshark display filters, cleartext credential extraction, and stream reconstruction with tcpdump."),
        ],
    },
    {
        "id": "09",
        "title": "Social Engineering",
        "banner_title": "Module 09: Social Engineering",
        "banner_sub": "Human Vulnerabilities, Phishing Campaign Architecture, Vishing, Pretexting & Defense",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "pill_label": "PHASE 2 • SOCIAL ENGINEERING",
        "phase_color": "#ff385c",
        "banner_accent": "#ea580c",
        "concepts": [
            "Human-Based: Phishing, Spearphishing, Whaling, Vishing, Smishing",
            "Physical Vectors: Dumpster Diving, Tailgating, Shoulder Surfing",
            "Influence Tactics: Authority, Scarcity, Urgency, Social Proof",
            "Insider Threat Profiling & Enterprise Awareness Training",
        ],
        "tools": "Social-Engineer Toolkit (SET) · GoPhish · Evilginx2 · King Phisher",
        "exam_focus": "Psychological triggers, Reverse social engineering, MFA interception",
        "banner_cards": [
            ("PHISHING & EMAIL ATTACKS", "Spearphishing, whaling, spoofed sender headers, and credential harvesting clones via SET."),
            ("VOICE & MOBILE DECEPTION", "Vishing (voice phishing), caller ID spoofing, deepfake audio lures, and smishing vectors."),
            ("PHYSICAL SOCIAL ATTACKS", "Tailgating, badge cloning, dumpster diving, shoulder surfing, and weaponized USB drops."),
            ("ORGANIZATIONAL HARDENING", "User awareness programs, phishing simulations, DMARC/SPF/DKIM validation, and FIDO2 MFA."),
        ],
    },
    {
        "id": "10",
        "title": "Denial-of-Service",
        "banner_title": "Module 10: Denial-of-Service",
        "banner_sub": "L3/L4 Flood Vectors, UDP Amplification, Slowloris, Botnet C2 & Mitigation Architectures",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "pill_label": "PHASE 2 • DOS / DDOS",
        "phase_color": "#ff385c",
        "banner_accent": "#e11d48",
        "concepts": [
            "Volumetric vs Protocol vs Application-Layer DoS",
            "SYN Floods, Smurf Attacks (ICMP Directed Broadcast), UDP Floods",
            "Amplification Attacks: NTP Monlist, DNS Open Resolvers, Memcached",
            "Slowloris & R-U-Dead-Yet (RUDY) HTTP Exhaustion",
        ],
        "tools": "LOIC · HOIC · Slowloris · Hping3 · GoldenEye",
        "exam_focus": "SYN cookies, TCP backlog queue, Bandwidth amplification factor, Botnets",
        "banner_cards": [
            ("VOLUMETRIC AMPLIFICATION", "DNS, NTP (monlist), SNMP, and Memcached reflection attacks delivering massive terabit floods."),
            ("STATE EXHAUSTION ATTACKS", "TCP SYN flooding, LAND attacks, Smurf ICMP floods, and connection pool depletion."),
            ("APPLICATION LAYER DOS", "Slowloris slow-header exhaustion, HTTP POST body starvation, and algorithmic XML entity bombs."),
            ("DDOS DEFENSE & SCRUBBING", "BGP Anycast routing, cloud scrubbing centers (Cloudflare, Akamai), SYN cookies, and rate limiting."),
        ],
    },
    {
        "id": "11",
        "title": "Session Hijacking",
        "banner_title": "Module 11: Session Hijacking",
        "banner_sub": "TCP Sequence Prediction, Session Token Theft, Man-in-the-Browser & Cookie Hijacking",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "pill_label": "PHASE 2 • SESSION HIJACKING",
        "phase_color": "#ff385c",
        "banner_accent": "#9333ea",
        "concepts": [
            "Network-Level: TCP Sequence Number Prediction & RST Attacks",
            "Application-Level: Session Token Sniffing, Fixation & Replay",
            "Man-in-the-Browser (MitB) & DOM-Based Session Theft",
            "Defenses: Strict Session Invalidation, SameSite & HttpOnly Cookies",
        ],
        "tools": "Burp Suite · Bettercap · OWASP ZAP · Hamster & Ferret",
        "exam_focus": "TCP initial sequence numbers (ISN), 3-way handshake spoofing, Session entropy",
        "banner_cards": [
            ("NETWORK-LEVEL HIJACKING", "TCP Sequence Number prediction, ACK storms, RST packet injection, and IP address spoofing."),
            ("APPLICATION SESSION THEFT", "Cookie theft via Cross-Site Scripting (XSS), session fixation, and session token prediction."),
            ("MAN-IN-THE-BROWSER (MITB)", "Trojan browser extensions, DOM manipulation, and transaction interceptors prior to SSL encryption."),
            ("SESSION PROTECTION POLICIES", "Cryptographically secure tokens, HttpOnly/SameSite/Secure cookie flags, and session timeout SLAs."),
        ],
    },
    {
        "id": "12",
        "title": "Evading IDS, Firewalls & Honeypots",
        "banner_title": "Module 12: Evading IDS, Firewalls, and Honeypots",
        "banner_sub": "Packet Fragmentation, Decoy Routing, Source Port Manipulation & Honeypot Detection",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "pill_label": "PHASE 2 • EVASION TECHNIQUES",
        "phase_color": "#ff385c",
        "banner_accent": "#7c3aed",
        "concepts": [
            "Signature Evasion: Packet Fragmentation & Overlapping Fragments",
            "Source Routing, Decoy Scanning (-D) & IP Address Spoofing",
            "Protocol Tunneling: SSH Port Forwarding, DNS & ICMP Tunneling",
            "Honeypot Detection & High-Interaction vs Low-Interaction Traps",
        ],
        "tools": "Nmap · Snort · Suricata · Proxychains · Ptunnel · Iodine",
        "exam_focus": "Snort rule syntax, Fragmentation flags (-f, --mtu), Honeyd fingerprinting",
        "banner_cards": [
            ("IDS / IPS BYPASS TACTICS", "Session splicing, overlapping TCP fragments, polymorphic payload encoding, and Unicode mutations."),
            ("FIREWALL EVASION STRATEGIES", "Source port spoofing (port 53/80), decoy scanning (-D), HTTP/DNS tunneling, and IP encapsulation."),
            ("HONEYPOT DETECTION", "Analyzing system response latencies, fake service emulation quirks, and virtual MAC addresses."),
            ("NEXT-GEN DEFENSIVE CONTROLS", "Stateful deep packet inspection (DPI), heuristic behavior analysis, and protocol normalization."),
        ],
    },
    {
        "id": "13",
        "title": "Hacking Web Servers",
        "banner_title": "Module 13: Hacking Web Servers",
        "banner_sub": "Web Architecture Attacks, Directory Traversal, WebDAV Abuse, Misconfigurations & Hardening",
        "phase": 3,
        "phase_name": "Web, Wireless & Emerging Tech",
        "pill_label": "PHASE 3 • WEB SERVERS",
        "phase_color": "#ffb300",
        "banner_accent": "#10b981",
        "concepts": [
            "Web Server Architectures (Apache, Nginx, Microsoft IIS)",
            "Default Credentials, Directory Traversal & Source Code Leaks",
            "WebDAV Insecure Methods (PUT, MOVE, COPY) & Webshell Dropping",
            "HTTP Request Smuggling, Pipeline Desynchronization & Hardening",
        ],
        "tools": "Nikto · Metasploit · WPScan · Burp Suite · Nmap HTTP Scripts",
        "exam_focus": "IIS metabase vulnerabilities, WebDAV permissions, Server banner hiding",
        "banner_cards": [
            ("WEB SERVER THREAT SURFACE", "Apache HTTPD, Nginx, Microsoft IIS, and lighttpd architecture, modules, and process identities."),
            ("SERVER MISCONFIGURATIONS", "Directory listings, default credentials, exposed diagnostic consoles, and information disclosure."),
            ("WEBDAV & FILE MANAGEMENT", "Arbitrary file upload via misconfigured PUT/MOVE methods and staging webshell backdoors."),
            ("SERVER HARDENING BLUEPRINTS", "Disabling unused HTTP verbs, enforcing least privilege, chroot jails, and TLS cipher tuning."),
        ],
    },
    {
        "id": "14",
        "title": "Hacking Web Applications",
        "banner_title": "Module 14: Hacking Web Applications",
        "banner_sub": "OWASP Top 10 Vulnerabilities, Cross-Site Scripting (XSS), CSRF, SSRF & API Security",
        "phase": 3,
        "phase_name": "Web, Wireless & Emerging Tech",
        "pill_label": "PHASE 3 • WEB APPLICATIONS",
        "phase_color": "#ffb300",
        "banner_accent": "#0d9488",
        "concepts": [
            "OWASP Top 10: Broken Access Control & Cryptographic Failures",
            "Cross-Site Scripting (Reflected, Stored, DOM-Based XSS)",
            "Cross-Site Request Forgery (CSRF) & Server-Side Request Forgery (SSRF)",
            "Insecure Direct Object References (IDOR) & Broken Object Level Auth",
        ],
        "tools": "Burp Suite Pro · OWASP ZAP · Postman · ffuf · Gobuster",
        "exam_focus": "XSS filter evasion, Same-Origin Policy (SOP), CORS headers, CSRF tokens",
        "banner_cards": [
            ("OWASP TOP 10 MASTERCLASS", "Broken Access Control, Cryptographic Failures, Insecure Design, and Security Misconfiguration."),
            ("CROSS-SITE SCRIPTING (XSS)", "Stored, Reflected, and DOM-based XSS exploitation, cookie theft, and keylogger injection."),
            ("FORGERY & SSRF ATTACKS", "Cross-Site Request Forgery (CSRF) and Server-Side Request Forgery (SSRF) targeting cloud metadata."),
            ("API SECURITY & WAF DEFENSE", "REST/GraphQL vulnerabilities, Mass Assignment, BOLA/IDOR flaws, and Web Application Firewalls."),
        ],
    },
    {
        "id": "15",
        "title": "SQL Injection",
        "banner_title": "Module 15: SQL Injection",
        "banner_sub": "In-Band UNION Exploitation, Blind Boolean/Time-Based SQLi, SQLMap & Prepared Statements",
        "phase": 3,
        "phase_name": "Web, Wireless & Emerging Tech",
        "pill_label": "PHASE 3 • SQL INJECTION",
        "phase_color": "#ffb300",
        "banner_accent": "#f59e0b",
        "concepts": [
            "In-Band SQLi: UNION-Based Data Extraction & Error-Based Payloads",
            "Blind SQLi: Boolean-Based Probing & Heavy Query Time Delays",
            "Out-of-Band (OOB) DNS Exfiltration (xp_dirtree, UTL_HTTP)",
            "Defense: Parameterized Prepared Statements & Stored Procedures",
        ],
        "tools": "SQLMap · Havij · Burp Suite · jSQL Injection · DSSS",
        "exam_focus": "SQL comment syntax (-- vs #), UNION column alignment, Prepared Statements",
        "banner_cards": [
            ("IN-BAND UNION INJECTION", "Determining column count (ORDER BY), mapping data types, and dumping databases via UNION SELECT."),
            ("BLIND SQL INJECTION", "Inferring data via Boolean-based binary evaluation and time-delay inference (SLEEP / WAITFOR DELAY)."),
            ("OUT-OF-BAND & ADVANCED SQLI", "DNS exfiltration, stacked queries, and executing operating system commands via xp_cmdshell."),
            ("SQLMAP & MITIGATION", "Automated injection testing with SQLMap, parameterized queries (Prepared Statements), and ORM security."),
        ],
    },
    {
        "id": "16",
        "title": "Hacking Wireless Networks",
        "banner_title": "Module 16: Hacking Wireless Networks",
        "banner_sub": "802.11 Protocols, WPA/WPA2 4-Way Handshake, WPA3 SAE, Rogue APs & Aircrack-ng",
        "phase": 3,
        "phase_name": "Web, Wireless & Emerging Tech",
        "pill_label": "PHASE 3 • WIRELESS SECURITY",
        "phase_color": "#ffb300",
        "banner_accent": "#0284c7",
        "concepts": [
            "802.11 Encryption Evolution: WEP (RC4), WPA (TKIP), WPA2 (AES-CCMP)",
            "WPA/WPA2 4-Way Handshake Capture (EAPOL) & Offline Cracking",
            "WPA3 SAE (Simultaneous Authentication of Equals) Dragonfly Handshake",
            "Rogue Access Points, Evil Twin Attacks & Karma Beacon Response",
        ],
        "tools": "Aircrack-ng · Airodump-ng · Aireplay-ng · Wifite · Kismet",
        "exam_focus": "4-Way Handshake frames (M1-M4), Deauth injection (--deauth 0), Protected Management Frames",
        "banner_cards": [
            ("802.11 PROTOCOL ANATOMY", "Management, Control, and Data frames, beacon intervals, SSID broadcasting, and monitor mode."),
            ("WPA/WPA2 HANDSHAKE ATTACKS", "Deauthentication frame injection, capturing EAPOL 4-way handshakes, and cracking PMK with Aircrack-ng."),
            ("WPA3 & MODERN ADVANCES", "Simultaneous Authentication of Equals (SAE), Dragonfly handshake mechanics, and PMKID harvesting."),
            ("ROGUE AP & EVIL TWINS", "Deploying Evil Twin access points, KARMA attacks, captive portal harvesting, and WIPS monitoring."),
        ],
    },
    {
        "id": "17",
        "title": "Hacking Mobile Platforms",
        "banner_title": "Module 17: Hacking Mobile Platforms",
        "banner_sub": "Android APK Reverse Engineering, DEX/Smali, JADX, MobSF, iOS Sandboxing & MDM Security",
        "phase": 3,
        "phase_name": "Web, Wireless & Emerging Tech",
        "pill_label": "PHASE 3 • MOBILE SECURITY",
        "phase_color": "#ffb300",
        "banner_accent": "#2563eb",
        "concepts": [
            "Android OS Sandboxing, APK Structure, DEX & Smali Bytecode",
            "Insecure Logging, Hardcoded Secrets & Exported Android Components",
            "iOS Sandbox Architecture, Jailbreaking & Mach-O Binaries",
            "Dynamic Instrumentation & SSL Pinning Bypass with Frida & Objection",
        ],
        "tools": "JADX-GUI · MobSF · APKTool · Frida · Objection · ADB",
        "exam_focus": "Android permissions model, AndroidManifest.xml auditing, App signing (v1-v4)",
        "banner_cards": [
            ("ANDROID ARCHITECTURE & APK", "Linux kernel, ART runtime, permissions, manifest analysis, and APK decompilation via JADX/Apktool."),
            ("AUTOMATED & STATIC AUDITS", "Static code auditing, hardcoded secrets, insecure broadcast receivers, and MobSF frameworks."),
            ("DYNAMIC FRIDA HOOKING", "Runtime instrumentation, modifying memory logic, method hooking, and SSL certificate pinning bypass."),
            ("IOS SANDBOX & MDM DEFENSE", "iOS security architecture, Keychain encryption, jailbreak detection evasion, and MDM policies."),
        ],
    },
    {
        "id": "18",
        "title": "IoT and OT Hacking",
        "banner_title": "Module 18: IoT and OT Hacking",
        "banner_sub": "Embedded Systems, MQTT, Zigbee, Modbus, SCADA/ICS Protocols & Hardware Interfacing",
        "phase": 3,
        "phase_name": "Web, Wireless & Emerging Tech",
        "pill_label": "PHASE 3 • IOT & OT HACKING",
        "phase_color": "#ffb300",
        "banner_accent": "#7c3aed",
        "concepts": [
            "IoT Architecture (Perception, Network, Edge, Cloud)",
            "Lightweight Protocols: MQTT Broker Security, CoAP, Zigbee, BLE",
            "Operational Technology (OT) & ICS/SCADA (Modbus, DNP3, Profibus)",
            "Hardware Hacking Interfaces: UART Serial, JTAG Debugging, SPI Flash",
        ],
        "tools": "Firmwalker · Binwalk · Shodan IoT · Wireshark · Radamsa",
        "exam_focus": "Purdue Enterprise Model, Modbus function codes, Hardware firmware extraction",
        "banner_cards": [
            ("IOT ARCHITECTURE & THREATS", "Edge devices, embedded Linux firmware extraction, Binwalk analysis, and cleartext MQTT brokers."),
            ("SCADA & INDUSTRIAL PROTOCOLS", "ICS architectures, PLCs, RTUs, and unauthenticated command injection into Modbus and DNP3."),
            ("HARDWARE INTERFACING", "UART serial console root access, JTAG boundary scan debugging, and bus snooping with logic analyzers."),
            ("DEFENSIVE ARCHITECTURES", "Purdue Model network segmentation, industrial firewalls, air-gapping, and ICS anomaly monitors."),
        ],
    },
    {
        "id": "19",
        "title": "Cloud Computing",
        "banner_title": "Module 19: Cloud Computing",
        "banner_sub": "AWS, Azure, GCP Architectures, IAM Privilege Escalation, S3 Bucket Audits & Containers",
        "phase": 4,
        "phase_name": "Cloud Security & Cryptography",
        "pill_label": "PHASE 4 • CLOUD SECURITY",
        "phase_color": "#10b981",
        "banner_accent": "#06b6d4",
        "concepts": [
            "Cloud Service Models (IaaS, PaaS, SaaS) & Shared Responsibility",
            "AWS, Azure, GCP IAM Role Misconfigurations & PrivEsc Vectors",
            "Public Cloud Storage Leakage (AWS S3 Buckets, Azure Blobs)",
            "Container Security: Docker Escapes, Namespaces & Kubernetes RBAC",
        ],
        "tools": "ScoutSuite · Pacu · CloudSploit · Prowler · Trivy · Docker Bench",
        "exam_focus": "Shared Responsibility Matrix, Cloud storage access control, Container isolation",
        "banner_cards": [
            ("SHARED RESPONSIBILITY MODEL", "IaaS, PaaS, SaaS security boundaries, cloud threat matrix, and compliance frameworks."),
            ("IAM MISCONFIGURATIONS", "Overprivileged IAM roles, AssumeRole lateral movement, policy evaluation, and credential leakage."),
            ("STORAGE & METADATA EXPLOITS", "Exposed S3 buckets/blobs, and SSRF targeting Instance Metadata Service (IMDSv1 vs IMDSv2)."),
            ("CONTAINER & K8S SECURITY", "Docker daemon socket escapes, container capabilities, Kubernetes RBAC misconfigurations, and Trivy."),
        ],
    },
    {
        "id": "20",
        "title": "Cryptography",
        "banner_title": "Module 20: Cryptography",
        "banner_sub": "Symmetric & Asymmetric Ciphers, Hashing, Public Key Infrastructure (PKI) & Cryptanalysis",
        "phase": 4,
        "phase_name": "Cloud Security & Cryptography",
        "pill_label": "PHASE 4 • CRYPTOGRAPHY",
        "phase_color": "#10b981",
        "banner_accent": "#eab308",
        "concepts": [
            "Symmetric Ciphers (AES-256, DES, 3DES, RC4, ChaCha20)",
            "Asymmetric Cryptography: RSA, Elliptic Curve Cryptography (ECC)",
            "Cryptographic Hashing (SHA-2, SHA-3) & Collision Attacks (MD5)",
            "Public Key Infrastructure (PKI), Digital Signatures & Cryptanalysis",
        ],
        "tools": "OpenSSL · Hashcat · John the Ripper · CrypTool · VeraCrypt",
        "exam_focus": "Symmetric vs Asymmetric trade-offs, RSA key sizes, Birthday attack, X.509 PKI",
        "banner_cards": [
            ("SYMMETRIC ENCRYPTION", "Block vs stream ciphers, AES (128/256-bit), DES/3DES, and block cipher modes (ECB, CBC, GCM)."),
            ("ASYMMETRIC CRYPTOGRAPHY", "Prime factorization (RSA), Diffie-Hellman key exchange, Discrete Logarithm, and Elliptic Curve (ECC)."),
            ("HASHING & DIGITAL SIGNATURES", "SHA-256, SHA-3, MD5 collision weaknesses, HMAC authentication, and non-repudiation signing."),
            ("PKI & CRYPTANALYSIS", "X.509 certificate hierarchy, CRL/OCSP revocation, Padding Oracle attacks, and quantum-resistant algorithms."),
        ],
    },
]

PHASES_META = [
    {
        "phase": 1,
        "short_name": "Information Gathering & Vulnerability Assessment",
        "name": "Phase 1: Information Gathering & Vulnerability Assessment",
        "subtitle": "Modules 01 - 05 • Foundations, OSINT Reconnaissance, Network Scanning, Enumeration & Vuln Analysis",
        "color": "#00d4ff",
    },
    {
        "phase": 2,
        "short_name": "Network, Endpoint & System Exploitation",
        "name": "Phase 2: Network, Endpoint & System Exploitation",
        "subtitle": "Modules 06 - 12 • System Hacking, Malware, Sniffing, Social Eng, DoS, Session Hijacking & Evasion",
        "color": "#ff385c",
    },
    {
        "phase": 3,
        "short_name": "Web, Wireless, Mobile & Modern Tech",
        "name": "Phase 3: Web, Wireless, Mobile & Modern Tech Exploitation",
        "subtitle": "Modules 13 - 18 • Web Servers, Web Apps, SQL Injection, Wireless, Mobile Platforms & IoT/OT",
        "color": "#ffb300",
    },
    {
        "phase": 4,
        "short_name": "Cloud Security & Cryptography",
        "name": "Phase 4: Cloud Security, Containers & Cryptography",
        "subtitle": "Modules 19 - 20 + AI Framework • Cloud IAM, IMDS, Kubernetes, Ciphers, PKI & AI Ethical Hacking",
        "color": "#10b981",
    },
]


def load_phase_bg(phase_num, size=(1376, 768)):
    bg_path = os.path.join(BG_DIR, f"phase_{phase_num}_bg.jpg")
    im = Image.open(bg_path).convert("RGBA")
    if im.size != size:
        im = im.resize(size, Image.Resampling.LANCZOS)
    return im


def generate_module_banners():
    print("Generating 20 clean module banners (zero pill collision)...")
    W, H = 1376, 768
    for m in MODULES:
        base_img = load_phase_bg(m["phase"], (W, H))
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(overlay)

        accent = m["banner_accent"]
        accent_rgba = hex_to_rgba(accent)

        # Top Metadata Bar
        d.rounded_rectangle([38, 18, W - 38, 68], radius=8, fill=(8, 13, 26, 215), outline=hex_to_rgba(accent, 90), width=1)
        d.text((54, 34), "EC-COUNCIL CERTIFIED ETHICAL HACKER (CEH v13)  •  OFFENSIVE SECURITY TRACK", fill=hex_to_rgba(accent, 235), font=get_font(15, mono=True))
        exam_str = f"EXAM 312-50  •  MODULE {m['id']} / 20"
        eb = get_font(15, bold=True, mono=True).getbbox(exam_str)
        d.text((W - 54 - (eb[2] - eb[0]), 34), exam_str, fill=(245, 158, 11, 255), font=get_font(15, bold=True, mono=True))

        # Hero Title Box
        d.rounded_rectangle([38, 84, W - 38, 206], radius=12, fill=(7, 11, 22, 225), outline=hex_to_rgba(accent, 180), width=2)
        d.text((58, 102), m["banner_title"], fill=(255, 255, 255, 255), font=get_font(36, bold=True))
        d.text((58, 156), m["banner_sub"], fill=(203, 213, 225, 255), font=get_font(18, bold=False))

        # Dynamic Non-Overlapping Pill Badges Row
        px = 38
        py = 220
        pills = [
            (m["pill_label"], accent, "#ffffff"),
            ("ANSI 17024 ACCREDITED", "#1e3a5f", "#ffffff"),
            ("AI-DRIVEN TRADECRAFT", "#047857", "#ffffff"),
            ("OFFICIAL STUDY GUIDE", "#7e22ce", "#ffffff"),
        ]
        for ptxt, pbg, ptc in pills:
            end_x, _ = draw_badge(d, px, py, ptxt, pbg, ptc, font_size=13, pad_x=13, pad_y=6, radius=6)
            px = end_x + 12

        # 4 Bottom Glass Cards (2x2)
        card_top = 406
        gap_x = 22
        gap_y = 18
        card_w = (W - 76 - gap_x) // 2
        card_h = 156
        f_title = get_font(19, bold=True)
        f_body = get_font(14, bold=False)

        for idx, (ctitle, cdesc) in enumerate(m["banner_cards"]):
            r = idx // 2
            c = idx % 2
            cx = 38 + c * (card_w + gap_x)
            cy = card_top + r * (card_h + gap_y)

            d.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=12, fill=(10, 16, 30, 228), outline=hex_to_rgba("#334155", 190), width=1)
            # Accent top bar indicator inside card
            d.rounded_rectangle([cx + 18, cy + 16, cx + 40, cy + 21], radius=2, fill=accent_rgba)
            d.text((cx + 18, cy + 32), ctitle, fill=(248, 250, 252, 255), font=f_title)

            wrapped = wrap_text(cdesc, f_body, card_w - 36)
            ty = cy + 68
            for line in wrapped[:3]:
                d.text((cx + 18, ty), line, fill=(186, 200, 220, 255), font=f_body)
                ty += 22

        combined = Image.alpha_composite(base_img, overlay).convert("RGB")
        b_path = os.path.join(BANNERS_DIR, f"module_{m['id']}_banner.jpg")
        combined.save(b_path, "JPEG", quality=95, subsampling=0)

        mod_img_dir = os.path.join(BASE_DIR, f"Module {m['id']}", "images")
        os.makedirs(mod_img_dir, exist_ok=True)
        combined.save(os.path.join(mod_img_dir, "banner.jpg"), "JPEG", quality=95, subsampling=0)
    print("All 20 module banners saved cleanly.")


def generate_animated_gif():
    print("Rebuilding cehv13_modules_overview.gif (20 frames, 960x540)...")
    frames = []
    for m in MODULES:
        b_path = os.path.join(BANNERS_DIR, f"module_{m['id']}_banner.jpg")
        im = Image.open(b_path).convert("RGB").resize((960, 540), Image.Resampling.LANCZOS)
        # Convert cleanly per frame to high quality 256-color palette
        im_p = im.quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG)
        frames.append(im_p)

    gif_out = os.path.join(IMAGES_DIR, "cehv13_modules_overview.gif")
    frames[0].save(
        gif_out,
        save_all=True,
        append_images=frames[1:],
        duration=1800,
        loop=0,
        optimize=True,
    )
    print(f"Animated GIF saved: {gif_out} ({os.path.getsize(gif_out)/1024:.1f} KB)")


def generate_module_cards():
    print("Generating 20 crisp individual module cards (zero tofu glyphs, wrapped text)...")
    W, H = 1400, 900
    for m in MODULES:
        img = Image.new("RGB", (W, H), "#080d1a")
        draw = ImageDraw.Draw(img)

        for gx in range(0, W, 50):
            draw.line([(gx, 0), (gx, H)], fill="#0d1527", width=1)
        for gy in range(0, H, 50):
            draw.line([(0, gy), (W, gy)], fill="#0d1527", width=1)

        color = m["phase_color"]
        draw.rounded_rectangle([30, 30, W - 30, H - 30], radius=18, fill="#0e172a", outline=color, width=2)
        draw.rounded_rectangle([30, 30, W - 30, 170], radius=18, fill="#131e36")
        draw.rectangle([30, 140, W - 30, 170], fill="#131e36")
        draw.line([(45, 32), (W - 45, 32)], fill=color, width=3)

        p1_end, _ = draw_badge(draw, 60, 48, f"CEH v13 — MODULE {m['id']}", color, "#000000", 16, pad_x=14, pad_y=6)
        draw_badge(draw, p1_end + 18, 48, f"PHASE 0{m['phase']}: {m['phase_name'].upper()}", "#334155", "#ffffff", 14, pad_x=12, pad_y=6)
        draw.text((60, 102), m["title"], fill="#ffffff", font=get_font(34, bold=True))

        # Concepts container
        draw.rounded_rectangle([60, 198, W - 60, 526], radius=14, fill="#090f1d", outline="#1e293b", width=1)
        draw.text((90, 222), "KEY ATTACK VECTORS & METHODOLOGY DOMAINS", fill=color, font=get_font(18, bold=True))

        f_conc = get_font(18, bold=False)
        cy = 272
        for idx, conc in enumerate(m["concepts"]):
            draw_badge(draw, 90, cy, f"0{idx+1}", color, "#000000", 12, pad_x=7, pad_y=3)
            lines = wrap_text(conc, f_conc, W - 240)
            for lidx, ln in enumerate(lines[:2]):
                draw.text((144, cy + 1 + lidx * 24), ln, fill="#f1f5f9", font=f_conc)
            cy += 58

        box_w = (W - 120 - 30) // 2
        box_top = 554
        box_bot = H - 56

        # Tools Box (handles 4-6+ tools cleanly without touching border)
        draw.rounded_rectangle([60, box_top, 60 + box_w, box_bot], radius=14, fill="#090f1d", outline="#1e293b", width=1)
        draw.text((86, box_top + 24), "INDUSTRY TOOLS & FRAMEWORKS", fill="#38bdf8", font=get_font(16, bold=True))

        tool_list = [t.strip() for t in m["tools"].split("·")]
        f_tool = get_font(16, bold=False)
        if len(tool_list) <= 5:
            ty = box_top + 68
            step_y = 36
            for tool in tool_list:
                draw_vector_bolt(draw, 98, ty + 11, scale=0.85, fill="#38bdf8")
                draw.text((118, ty), tool, fill="#e2e8f0", font=f_tool)
                ty += step_y
        else:
            # 2-column grid for 6+ tools so zero collision with bottom border
            col_offsets = [90, 90 + (box_w - 60) // 2]
            for tidx, tool in enumerate(tool_list):
                col = tidx % 2
                row = tidx // 2
                tx = col_offsets[col]
                ty = box_top + 74 + row * 48
                draw_vector_bolt(draw, tx + 8, ty + 11, scale=0.85, fill="#38bdf8")
                draw.text((tx + 28, ty), tool, fill="#e2e8f0", font=f_tool)

        # Exam Focus Box (properly wrapped text!)
        ex_x = 60 + box_w + 30
        draw.rounded_rectangle([ex_x, box_top, W - 60, box_bot], radius=14, fill="#1c1917", outline="#f59e0b", width=1)
        draw.text((ex_x + 26, box_top + 24), "EXAM FOCUS & TRADECRAFT OBJECTIVES", fill="#f59e0b", font=get_font(16, bold=True))
        draw.text((ex_x + 26, box_top + 68), "Core Tested Scenarios:", fill="#fde68a", font=get_font(15, bold=True))

        f_exam = get_font(16, bold=False)
        exam_lines = wrap_text(m["exam_focus"], f_exam, box_w - 52)
        ey = box_top + 102
        for el in exam_lines[:4]:
            draw.text((ex_x + 26, ey), el, fill="#f8fafc", font=f_exam)
            ey += 26

        draw.text((ex_x + 26, box_bot - 42), "Standard: ANSI 17024 Accredited • EC-Council Exam 312-50", fill="#94a3b8", font=get_font(13, bold=False))

        out_path = os.path.join(MODULES_DIR, f"Module_{m['id']}.png")
        img.save(out_path, "PNG")
        mod_card_path = os.path.join(BASE_DIR, f"Module {m['id']}", "images", "module_card.png")
        img.save(mod_card_path, "PNG")
    print("All 20 individual module cards generated.")


def generate_ai_matrix():
    print("Generating ceh_v13_ai_ethical_hacking_matrix.png (zero pill collisions)...")
    W, H = 2400, 1400
    img = Image.new("RGB", (W, H), "#070b14")
    draw = ImageDraw.Draw(img)

    for gx in range(0, W, 60):
        draw.line([(gx, 0), (gx, H)], fill="#0d1424", width=1)
    for gy in range(0, H, 60):
        draw.line([(0, gy), (W, gy)], fill="#0d1424", width=1)

    # Top Header Panel
    draw.rounded_rectangle([40, 30, W - 40, 200], radius=16, fill="#0d1527", outline="#a855f7", width=2)
    draw_badge(draw, 70, 52, "CEH v13 EXCLUSIVE PARADIGM", "#9333ea", "#ffffff", 14, pad_x=12, pad_y=5)
    draw.text((70, 96), "AI-POWERED ETHICAL HACKING & ADVERSARY TRADECRAFT", fill="#ffffff", font=get_font(38, bold=True))
    draw.text((70, 150), "Integrating Generative AI, Neural Payload Synthesis, Automated Surface Discovery, and LLM Defense", fill="#cbd5e1", font=get_font(18))

    quads = [
        {
            "badge": "MODULES 01 - 04",
            "title": "1. AI in Threat Reconnaissance & OSINT",
            "color": "#00d4ff",
            "items": [
                ("Automated Target Profiling:", "Autonomous agent crawlers mapping employee dossiers and social graphs."),
                ("Natural Language Dorking:", "Converting conversational queries into complex Google & Shodan dorks."),
                ("Autonomous Surface Mapping:", "Predicting unlinked API endpoints and cloud assets using neural heuristics."),
                ("Threat Feed Synthesis:", "Real-time automated parsing of CTI feeds and IOC extraction."),
            ],
            "tools": "PentestGPT · Recon-AI · theHarvester-LLM · Shodan API",
        },
        {
            "badge": "MODULES 05, 13, 14, 15",
            "title": "2. AI-Driven Vulnerability Discovery",
            "color": "#f59e0b",
            "items": [
                ("Static Code Audit with LLMs:", "Scanning millions of lines of source code for subtle logic and access control bugs."),
                ("AI-Synthesized Fuzzing:", "Generating context-aware input payloads for zero-day memory corruption hunting."),
                ("Semantic Web Vulnerability Hunting:", "Uncovering SSRF, IDOR, and authorization bypasses beyond regex ASTs."),
                ("Smart Contract Auditing:", "Auditing EVM bytecode for reentrancy, integer overflow, and logic flaws."),
            ],
            "tools": "Semgrep AI · PentestGPT · Snyk DeepCode · Burp AI Assist",
        },
        {
            "badge": "MODULES 06, 07, 10, 12",
            "title": "3. AI-Crafted Exploitation & Evasion",
            "color": "#ef4444",
            "items": [
                ("Polymorphic Shellcode Synthesis:", "Dynamically mutating binary payloads to evade static AV / EDR signatures."),
                ("AI Spearphishing Generation:", "Hyper-personalized email and voice clones (Vishing) mimicking executives."),
                ("Adaptive C2 Traffic Mimicry:", "Masking Command & Control communications as benign Zoom or Teams traffic."),
                ("Automated Exploit Chaining:", "Synthesizing multi-stage privilege escalation chains automatically."),
            ],
            "tools": "WormGPT · FraudGPT · DeepPhish · ShellGPT · Custom LLMs",
        },
        {
            "badge": "MODULES 01, 19, 20  •  OWASP LLM TOP 10",
            "title": "4. Defending the AI Attack Surface",
            "color": "#10b981",
            "items": [
                ("Prompt Injection & Jailbreaks:", "Direct and indirect prompt hijacking bypassing system alignment."),
                ("Model Inversion & Data Poisoning:", "Extracting proprietary training weights and poisoning fine-tuning sets."),
                ("Insecure Output Handling:", "Preventing downstream XSS or RCE when applications execute LLM responses."),
                ("Guardrails & Boundary Enforcement:", "Deploying NeMo Guardrails, Llama Guard, and robust LLM firewalls."),
            ],
            "tools": "Garak · Promptfoo · NeMo Guardrails · OWASP LLM Top 10",
        },
    ]

    gx, gy = 40, 235
    gap_x, gap_y = 32, 32
    qw = (W - 80 - gap_x) // 2
    qh = (H - gy - 40 - gap_y) // 2

    for idx, q in enumerate(quads):
        r = idx // 2
        c = idx % 2
        qx = gx + c * (qw + gap_x)
        qy = gy + r * (qh + gap_y)
        col = q["color"]

        draw.rounded_rectangle([qx, qy, qx + qw, qy + qh], radius=16, fill="#0b1222", outline=col, width=2)
        # Clean Non-Overlapping Header Strip inside each quadrant: Badge LEFT, Title BELOW Badge or clean split
        end_px, _ = draw_badge(draw, qx + 24, qy + 20, q["badge"], col, "#000000", 14, pad_x=12, pad_y=4)
        # Put Title cleanly on the next row inside the card header, NEVER colliding!
        draw.text((qx + 24, qy + 56), q["title"], fill="#ffffff", font=get_font(24, bold=True))
        draw.line([(qx + 24, qy + 94), (qx + qw - 24, qy + 94)], fill="#1e293b", width=1)

        iy = qy + 114
        f_ih = get_font(17, bold=True)
        f_ib = get_font(15, bold=False)
        for h_txt, b_txt in q["items"]:
            draw.text((qx + 26, iy), h_txt, fill=col, font=f_ih)
            lines = wrap_text(b_txt, f_ib, qw - 56)
            for lidx, ln in enumerate(lines[:2]):
                draw.text((qx + 26, iy + 25 + lidx * 22), ln, fill="#cbd5e1", font=f_ib)
            iy += 80

        # Footer tools strip inside card
        t_y = qy + qh - 52
        draw.line([(qx + 24, t_y - 10), (qx + qw - 24, t_y - 10)], fill="#1e293b", width=1)
        draw.text((qx + 26, t_y), "TOOLCHAINS:", fill="#64748b", font=get_font(14, bold=True))
        draw.text((qx + 148, t_y), q["tools"], fill="#e2e8f0", font=get_font(14, bold=False))

    out_path = os.path.join(IMAGES_DIR, "ceh_v13_ai_ethical_hacking_matrix.png")
    img.save(out_path, "PNG")
    print(f"AI Matrix saved cleanly: {out_path}")


def generate_master_roadmap():
    print("Generating ceh_v13_all_modules_roadmap.png (all 20 modules, zero truncation, zero clipping)...")
    W, H = 3840, 2600
    img = Image.new("RGB", (W, H), "#070b14")
    draw = ImageDraw.Draw(img)

    for gx in range(0, W, 80):
        draw.line([(gx, 0), (gx, H)], fill="#0c1322", width=1)
    for gy in range(0, H, 80):
        draw.line([(0, gy), (W, gy)], fill="#0c1322", width=1)

    # Top Header Panel
    draw.rounded_rectangle([40, 30, W - 40, 224], radius=16, fill="#0d1527", outline="#1e293b", width=2)
    draw.line([(60, 32), (W - 60, 32)], fill="#00d4ff", width=3)

    draw.text((76, 54), "CERTIFIED ETHICAL HACKER (CEH v13) — COMPLETE 20-MODULE ARCHITECTURE", fill="#ffffff", font=get_font(46, bold=True))
    draw.text((76, 114), "Comprehensive Blueprint • All 20 Study Guides & Courseware PDFs • Adversary Tradecraft • AI-Powered Security Engineering", fill="#94a3b8", font=get_font(22))

    bx = 76
    by = 160
    top_pills = [
        ("EC-COUNCIL 312-50", "#0078d4", "#ffffff"),
        ("ANSI 17024 ACCREDITED", "#0284c7", "#ffffff"),
        ("20 CORE DOMAINS • 30 PDFS", "#10b981", "#ffffff"),
        ("4 OPERATIONAL PHASES", "#f59e0b", "#000000"),
        ("AI-POWERED ETHICAL HACKING", "#9333ea", "#ffffff"),
        ("MITRE ATT&CK ALIGNED", "#ec4899", "#ffffff"),
    ]
    for txt, bg, fg in top_pills:
        ex, _ = draw_badge(draw, bx, by, txt, bg, fg, 15, pad_x=13, pad_y=6)
        bx = ex + 14

    start_y = 248
    content_h = H - start_y - 120
    col_w = (W - 80 - 60) // 4

    def draw_wrapped_conc(d, x, y, text, font, max_w, fill, max_lines=2, line_h=20):
        lines = wrap_text(text, font, max_w)
        for li, ln in enumerate(lines[:max_lines]):
            d.text((x, y + li * line_h), ln, fill=fill, font=font)
        return min(len(lines), max_lines) * line_h

    for i, phase in enumerate(PHASES_META):
        pnum = phase["phase"]
        pcolor = phase["color"]
        cx = 40 + i * (col_w + 20)
        cy = start_y

        draw.rounded_rectangle([cx, cy, cx + col_w, cy + 96], radius=12, fill="#0f172a", outline=pcolor, width=2)
        draw_badge(draw, cx + 16, cy + 12, f"PHASE 0{pnum}", pcolor, "#000000", 14, pad_x=10, pad_y=3)
        draw.text((cx + 16, cy + 50), phase["short_name"], fill="#ffffff", font=get_font(21, bold=True))

        mods = [m for m in MODULES if m["phase"] == pnum]
        mod_y = cy + 112
        avail_h = content_h - 112

        if pnum in (1, 3):
            n_cards = len(mods)
            gap = 12
            card_h = (avail_h - gap * (n_cards - 1)) // n_cards
            for m in mods:
                draw.rounded_rectangle([cx, mod_y, cx + col_w, mod_y + card_h], radius=10, fill="#0b1120", outline="#1e293b", width=1)
                draw.rounded_rectangle([cx, mod_y, cx + 6, mod_y + card_h], radius=3, fill=pcolor)

                badge_end, _ = draw_badge(draw, cx + 16, mod_y + 12, f"M{m['id']}", pcolor, "#000000", 14, pad_x=8, pad_y=3)
                draw.text((badge_end + 12, mod_y + 13), m["title"], fill="#f8fafc", font=get_font(19, bold=True))

                f_conc = get_font(15)
                b_y = mod_y + 52
                for conc in m["concepts"][:3]:
                    draw.ellipse([cx + 20, b_y + 7, cx + 26, b_y + 13], fill=pcolor)
                    used_h = draw_wrapped_conc(draw, cx + 36, b_y, conc, f_conc, col_w - 50, "#cbd5e1", max_lines=2, line_h=20)
                    b_y += max(26, used_h + 6)

                draw.text((cx + 20, mod_y + card_h - 60), "Tools:", fill="#64748b", font=get_font(13, bold=True))
                draw_wrapped_conc(draw, cx + 76, mod_y + card_h - 60, m["tools"], get_font(13), col_w - 94, "#38bdf8", max_lines=1, line_h=18)

                draw.text((cx + 20, mod_y + card_h - 34), "Exam:", fill="#e2e8f0", font=get_font(13, bold=True))
                draw_wrapped_conc(draw, cx + 76, mod_y + card_h - 34, m["exam_focus"], get_font(13), col_w - 94, "#f59e0b", max_lines=1, line_h=18)

                mod_y += card_h + gap

        elif pnum == 2:
            n_cards = len(mods)
            gap = 10
            card_h = (avail_h - gap * (n_cards - 1)) // n_cards
            for m in mods:
                draw.rounded_rectangle([cx, mod_y, cx + col_w, mod_y + card_h], radius=10, fill="#0b1120", outline="#1e293b", width=1)
                draw.rounded_rectangle([cx, mod_y, cx + 6, mod_y + card_h], radius=3, fill=pcolor)

                badge_end, _ = draw_badge(draw, cx + 16, mod_y + 10, f"M{m['id']}", pcolor, "#000000", 13, pad_x=8, pad_y=2)
                draw.text((badge_end + 12, mod_y + 10), m["title"], fill="#f8fafc", font=get_font(18, bold=True))

                f_conc = get_font(14)
                b_y = mod_y + 44
                for conc in m["concepts"][:3]:
                    draw.ellipse([cx + 20, b_y + 6, cx + 26, b_y + 12], fill=pcolor)
                    used_h = draw_wrapped_conc(draw, cx + 36, b_y, conc, f_conc, col_w - 50, "#cbd5e1", max_lines=2, line_h=18)
                    b_y += max(22, used_h + 4)

                draw.text((cx + 20, mod_y + card_h - 50), "Tools:", fill="#64748b", font=get_font(12, bold=True))
                draw_wrapped_conc(draw, cx + 70, mod_y + card_h - 50, m["tools"], get_font(12), col_w - 88, "#38bdf8", max_lines=1, line_h=16)

                draw.text((cx + 20, mod_y + card_h - 27), "Exam:", fill="#e2e8f0", font=get_font(12, bold=True))
                draw_wrapped_conc(draw, cx + 70, mod_y + card_h - 27, m["exam_focus"], get_font(12), col_w - 88, "#f59e0b", max_lines=1, line_h=16)

                mod_y += card_h + gap

        elif pnum == 4:
            card_h = 350
            gap = 14
            for m in mods:
                draw.rounded_rectangle([cx, mod_y, cx + col_w, mod_y + card_h], radius=10, fill="#0b1120", outline="#1e293b", width=1)
                draw.rounded_rectangle([cx, mod_y, cx + 6, mod_y + card_h], radius=3, fill=pcolor)

                badge_end, _ = draw_badge(draw, cx + 16, mod_y + 14, f"M{m['id']}", pcolor, "#000000", 14, pad_x=8, pad_y=3)
                draw.text((badge_end + 12, mod_y + 14), m["title"], fill="#f8fafc", font=get_font(20, bold=True))

                f_conc = get_font(15)
                b_y = mod_y + 58
                for conc in m["concepts"][:4]:
                    draw.ellipse([cx + 20, b_y + 7, cx + 26, b_y + 13], fill=pcolor)
                    used_h = draw_wrapped_conc(draw, cx + 36, b_y, conc, f_conc, col_w - 50, "#cbd5e1", max_lines=2, line_h=20)
                    b_y += max(28, used_h + 6)

                draw.text((cx + 20, mod_y + card_h - 62), "Tools:", fill="#64748b", font=get_font(13, bold=True))
                draw_wrapped_conc(draw, cx + 76, mod_y + card_h - 62, m["tools"], get_font(13), col_w - 94, "#38bdf8", max_lines=1, line_h=18)

                draw.text((cx + 20, mod_y + card_h - 34), "Exam:", fill="#e2e8f0", font=get_font(13, bold=True))
                draw_wrapped_conc(draw, cx + 76, mod_y + card_h - 34, m["exam_focus"], get_font(13), col_w - 94, "#f59e0b", max_lines=1, line_h=18)

                mod_y += card_h + gap

            ai_bot = cy + content_h
            draw.rounded_rectangle([cx, mod_y, cx + col_w, ai_bot], radius=14, fill="#120c29", outline="#a855f7", width=2)
            draw_badge(draw, cx + 22, mod_y + 20, "WHAT'S NEW IN CEH v13", "#a855f7", "#ffffff", 14, pad_x=12, pad_y=4)
            draw.text((cx + 22, mod_y + 62), "AI-Driven Ethical Hacking Framework", fill="#ffffff", font=get_font(24, bold=True))
            draw.text((cx + 22, mod_y + 98), "Generative AI integration across offense & defense", fill="#c084fc", font=get_font(16))

            ai_points = [
                ("1. AI Reconnaissance & OSINT:", "LLM autonomous target profiling, automated Google/Shodan dorking, and surface graphing."),
                ("2. AI Vulnerability Discovery:", "Semantic static code auditing, context-aware fuzzing payloads, and API logic hunting."),
                ("3. AI Exploit Crafting & Evasion:", "Polymorphic shellcode generation, adaptive C2 mimicry, and automated exploit chaining."),
                ("4. AI Threat Hunting & SOC Ops:", "Real-time UEBA behavioral telemetry correlation, SIEM triage, and automated IR playbooks."),
                ("5. Defending AI (OWASP LLM Top 10):", "Prompt injection, jailbreak hardening, data poisoning defense, and NeMo Guardrails."),
            ]
            ai_y = mod_y + 148
            f_ah = get_font(17, bold=True)
            f_ab = get_font(15)
            for h_txt, b_txt in ai_points:
                draw.text((cx + 24, ai_y), h_txt, fill="#ec4899", font=f_ah)
                draw_wrapped_conc(draw, cx + 24, ai_y + 26, b_txt, f_ab, col_w - 48, "#e2e8f0", max_lines=2, line_h=22)
                ai_y += 98

    # Bottom Footer Status Bar
    draw.rounded_rectangle([40, H - 88, W - 40, H - 30], radius=10, fill="#0d1527", outline="#1e293b", width=1)
    kc_stages = ["Reconnaissance", "Weaponization", "Delivery", "Exploitation", "Installation", "Command & Control", "Actions on Objectives"]
    fx = 60
    fy = H - 68
    f_foot = get_font(16)
    draw.text((fx, fy), "Cyber Kill Chain: ", fill="#38bdf8", font=get_font(16, bold=True))
    fx += get_font(16, bold=True).getbbox("Cyber Kill Chain: ")[2] + 6
    for sidx, stg in enumerate(kc_stages):
        draw.text((fx, fy), stg, fill="#cbd5e1", font=f_foot)
        fx += f_foot.getbbox(stg)[2] + 10
        if sidx < len(kc_stages) - 1:
            draw_vector_chevron(draw, fx, fy + 6, size=8, fill="#00d4ff")
            fx += 18

    auth_str = "Cyber-Blog • Verified 20-Module Knowledge Base"
    ab = get_font(16, bold=True).getbbox(auth_str)
    draw.text((W - 60 - (ab[2] - ab[0]), fy), auth_str, fill="#38bdf8", font=get_font(16, bold=True))

    out_path = os.path.join(IMAGES_DIR, "ceh_v13_all_modules_roadmap.png")
    img.save(out_path, "PNG")
    print(f"Master 20-Module Roadmap saved: {out_path}")


def generate_curriculum_map():
    print("Polishing cehv13_curriculum_map.jpg (non-overlapping badges)...")
    W, H = 1376, 880
    img = Image.new("RGB", (W, H), "#070b14")
    draw = ImageDraw.Draw(img)

    for gx in range(0, W, 50):
        draw.line([(gx, 0), (gx, H)], fill="#0d1527", width=1)
    for gy in range(0, H, 50):
        draw.line([(0, gy), (W, gy)], fill="#0d1527", width=1)

    draw.rounded_rectangle([32, 22, W - 32, 82], radius=10, fill="#0d1527", outline="#1e293b", width=1)
    draw.text((52, 40), "CEH v13 MASTER ARCHITECTURE • 20-MODULE CERTIFICATION BLUEPRINT", fill="#ffffff", font=get_font(22, bold=True))
    eb_str = "EC-COUNCIL EXAM 312-50"
    eb = get_font(14, bold=True, mono=True).getbbox(eb_str)
    draw.text((W - 52 - (eb[2] - eb[0]), 44), eb_str, fill="#00d4ff", font=get_font(14, bold=True, mono=True))

    cols = [
        ("PHASE 1: FOUNDATIONS", "#00d4ff", [
            ("M01", "Intro to Ethical Hacking", "InfoSec, CIA/AAA, Kill Chains, AI"),
            ("M02", "Footprinting & Recon", "OSINT, Shodan, Dorking, DNS"),
            ("M03", "Scanning Networks", "TCP Flags, SYN/Connect, Nmap"),
            ("M04", "Enumeration", "NetBIOS, SMB, SNMP, LDAP, SMTP"),
            ("M05", "Vulnerability Analysis", "CVE, CVSS v3/v4, Nessus, OpenVAS"),
        ]),
        ("PHASE 2: NETWORK & HOST", "#ff385c", [
            ("M06", "System Hacking", "Password Cracking, PrivEsc, Pivoting"),
            ("M07", "Malware Threats", "Trojans, Ransomware, Crypters"),
            ("M08", "Sniffing", "ARP Poisoning, MAC Flood, Wireshark"),
            ("M09", "Social Engineering", "Phishing, Vishing, SET, Defense"),
            ("M10", "Denial-of-Service", "SYN Flood, UDP Amp, Slowloris"),
            ("M11", "Session Hijacking", "TCP Hijacking, MitB, Cookies"),
            ("M12", "Evading IDS & Firewalls", "Fragmentation, Decoys, Honeypots"),
        ]),
        ("PHASE 3: WEB & WIRELESS", "#f59e0b", [
            ("M13", "Hacking Web Servers", "Apache/IIS, WebDAV, Misconfigs"),
            ("M14", "Hacking Web Apps", "OWASP Top 10, XSS, CSRF, SSRF"),
            ("M15", "SQL Injection", "UNION, Blind, SQLMap, Defense"),
            ("M16", "Hacking Wireless", "802.11, WPA2/WPA3, Evil Twin"),
            ("M17", "Hacking Mobile", "Android APK, JADX, MobSF, Frida"),
            ("M18", "IoT and OT Hacking", "MQTT, Modbus, SCADA, Hardware"),
        ]),
        ("PHASE 4: CLOUD & CRYPTO", "#10b981", [
            ("M19", "Cloud Computing", "AWS/Azure/GCP, IAM, S3, Docker"),
            ("M20", "Cryptography", "AES, RSA, ECC, PKI, Signatures"),
            ("LABS", "Hands-on Exercises", "Break & Defend Practical Labs"),
            ("EXAM", "312-50 Preparation", "125 Questions • 4 Hours • 70%+"),
            ("AI-SEC", "AI Red Teaming", "LLM Prompt Injection & Defenses"),
        ]),
    ]

    gap = 16
    cw = (W - 64 - 3 * gap) // 4
    top_y = 100
    col_h = H - top_y - 24

    for cidx, (cname, ccol, items) in enumerate(cols):
        cx = 32 + cidx * (cw + gap)
        draw.rounded_rectangle([cx, top_y, cx + cw, top_y + col_h], radius=12, fill="#0b1120", outline="#1e293b", width=1)
        draw.text((cx + 16, top_y + 14), cname, fill=ccol, font=get_font(15, bold=True))

        n = len(items)
        card_gap = 10
        inner_top = top_y + 44
        inner_h = col_h - 58
        ih = (inner_h - card_gap * (n - 1)) // n

        for ridx, (tag, title, sub) in enumerate(items):
            iy = inner_top + ridx * (ih + card_gap)
            draw.rounded_rectangle([cx + 12, iy, cx + cw - 12, iy + ih], radius=8, fill="#0f172a", outline="#1e293b", width=1)
            end_bx, _ = draw_badge(draw, cx + 22, iy + 12, tag, ccol, "#000000", 12, pad_x=8, pad_y=3, radius=4)
            # Dynamic gap so EXAM / AI-SEC NEVER touches title!
            draw.text((end_bx + 10, iy + 12), title, fill="#ffffff", font=get_font(15, bold=True))
            sub_lines = wrap_text(sub, get_font(13), cw - 48)
            draw.text((cx + 22, iy + 42), sub_lines[0], fill="#94a3b8", font=get_font(13))

    out_path = os.path.join(IMAGES_DIR, "cehv13_curriculum_map.jpg")
    img.save(out_path, "JPEG", quality=95, subsampling=0)
    print(f"Curriculum Map saved cleanly: {out_path}")


def generate_phase_infographics():
    print("Generating 4 high-res cinematic phase overview infographics (2400x1350, zero clipping)...")
    W, H = 2400, 1350
    for phase in PHASES_META:
        pnum = phase["phase"]
        pcolor = phase["color"]
        bg = load_phase_bg(pnum, (W, H))
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(ov)

        d.rectangle([0, 0, W, H], fill=(5, 9, 18, 130))

        # Top Phase Header Banner
        d.rounded_rectangle([48, 32, W - 48, 192], radius=16, fill=(8, 13, 26, 232), outline=hex_to_rgba(pcolor, 210), width=2)
        d.line([(68, 34), (W - 68, 34)], fill=hex_to_rgba(pcolor, 255), width=3)
        draw_badge(d, 80, 52, f"CEH v13 OPERATIONAL PHASE 0{pnum}", pcolor, "#000000", 16, pad_x=14, pad_y=5)
        d.text((80, 96), phase["name"], fill=(255, 255, 255, 255), font=get_font(40, bold=True))
        d.text((80, 150), phase["subtitle"], fill=(203, 213, 225, 255), font=get_font(20))

        mods = [m for m in MODULES if m["phase"] == pnum]
        grid_x, grid_y = 48, 216
        grid_w, grid_h = W - 96, H - grid_y - 40

        if pnum == 1:
            cols, rows = 3, 2
            cards_data = [("mod", m) for m in mods] + [("summary", {
                "tag": "PHASE 1 SUMMARY",
                "title": "Recon-to-Assessment Pipeline",
                "bullets": [
                    "1. Legal Scope & RoE Authorization before any scan",
                    "2. Passive OSINT (Zero Packets) -> Active Footprinting",
                    "3. Port & Service Fingerprinting (Nmap, Hping3)",
                    "4. Protocol Enumeration (NetBIOS, SMB, SNMP, LDAP)",
                    "5. Risk Scoring & Prioritization (CVE + CVSS v3/v4)",
                ],
                "tools": "Maltego · Shodan · Nmap · enum4linux-ng · Nessus",
            })]
        elif pnum == 2:
            cols, rows = 4, 2
            cards_data = [("mod", m) for m in mods] + [("summary", {
                "tag": "PHASE 2 SUMMARY",
                "title": "System & Network Attack Matrix",
                "bullets": [
                    "1. Compromise Hosts (Hash Cracking, BoF, PrivEsc)",
                    "2. Deploy Persistence & Evade AV/EDR Sandboxes",
                    "3. Intercept Traffic (ARP MitM, Wireshark Forensics)",
                    "4. Exploit Human Trust (Phishing, Pretexting, Quishing)",
                    "5. Bypass Firewalls/IDS & Disrupt Availability",
                ],
                "tools": "Mimikatz · Hashcat · Wireshark · Bettercap · SET",
            })]
        elif pnum == 3:
            cols, rows = 3, 2
            cards_data = [("mod", m) for m in mods]
        else:
            cols, rows = 3, 1
            cards_data = [("mod", m) for m in mods] + [("summary", {
                "tag": "AI & EXAM FINALE",
                "title": "AI Ethical Hacking & 312-50 Prep",
                "bullets": [
                    "1. AI Recon & Code Auditing (PentestGPT, Semgrep AI)",
                    "2. OWASP LLM Top 10 (Prompt Injection, Jailbreaks)",
                    "3. Exam Focus: Shared Responsibility, IMDSv2, PKI",
                    "4. Cryptanalysis: Birthday (2^n/2) & Meet-in-the-Middle",
                    "5. 125 Questions • 4 Hours • ANSI 17024 Accredited",
                ],
                "tools": "ScoutSuite · Pacu · Trivy · OpenSSL · Promptfoo",
            })]

        gap_x, gap_y = 22, 22
        cw = (grid_w - (cols - 1) * gap_x) // cols
        ch = (grid_h - (rows - 1) * gap_y) // rows

        for idx, (ctype, item) in enumerate(cards_data):
            r = idx // cols
            c = idx % cols
            mx = grid_x + c * (cw + gap_x)
            my = grid_y + r * (ch + gap_y)

            if ctype == "mod":
                d.rounded_rectangle([mx, my, mx + cw, my + ch], radius=12, fill=(10, 16, 30, 234), outline=hex_to_rgba(pcolor, 180), width=1)
                d.rounded_rectangle([mx, my, mx + cw, my + 60], radius=12, fill=(16, 26, 48, 240))
                d.rectangle([mx, my + 44, mx + cw, my + 60], fill=(16, 26, 48, 240))
                end_bx, _ = draw_badge(d, mx + 16, my + 14, f"M{item['id']}", pcolor, "#000000", 14, pad_x=10, pad_y=3)
                t_font = get_font(20 if cols <= 3 else 18, bold=True)
                d.text((end_bx + 12, my + 15), item["title"], fill=(255, 255, 255, 255), font=t_font)

                by = my + 78
                f_b = get_font(16 if cols <= 3 else 14)
                line_step = 22 if cols <= 3 else 19
                for conc in item["concepts"]:
                    draw_vector_chevron(d, mx + 18, by + 6, size=6, fill=hex_to_rgba(pcolor))
                    lines = wrap_text(conc, f_b, cw - 48)
                    for lidx, ln in enumerate(lines[:2]):
                        d.text((mx + 34, by + lidx * line_step), ln, fill=(226, 232, 240, 255), font=f_b)
                    by += max(28 if cols == 4 else 36, len(lines[:2]) * line_step + 10)

                # Tools & Exam footer inside card (2 lines max for exam so NEVER clipped!)
                ty = my + ch - 96
                d.rounded_rectangle([mx + 14, ty, mx + cw - 14, ty + 34], radius=6, fill=(7, 11, 20, 238), outline=(30, 41, 59, 255))
                d.text((mx + 22, ty + 8), "TOOLS:", fill=(100, 116, 139, 255), font=get_font(12, bold=True))
                t_ln = wrap_text(item["tools"], get_font(13), cw - 105)[0]
                d.text((mx + 76, ty + 8), t_ln, fill=(56, 189, 248, 255), font=get_font(13))

                ey = my + ch - 54
                d.rounded_rectangle([mx + 14, ey, mx + cw - 14, ey + 44], radius=6, fill=(28, 25, 23, 238), outline=(68, 64, 60, 255))
                d.text((mx + 22, ey + 6), "EXAM:", fill=(245, 158, 11, 255), font=get_font(12, bold=True))
                e_lines = wrap_text(item["exam_focus"], get_font(12 if cols == 4 else 13), cw - 100)
                for lidx, el in enumerate(e_lines[:2]):
                    d.text((mx + 74, ey + 5 + lidx * 17), el, fill=(253, 230, 138, 255), font=get_font(12 if cols == 4 else 13))

            else:
                d.rounded_rectangle([mx, my, mx + cw, my + ch], radius=12, fill=(18, 12, 41, 236), outline=(168, 85, 247, 220), width=2)
                d.rounded_rectangle([mx, my, mx + cw, my + 60], radius=12, fill=(30, 19, 66, 240))
                d.rectangle([mx, my + 44, mx + cw, my + 60], fill=(30, 19, 66, 240))
                end_bx, _ = draw_badge(d, mx + 16, my + 14, item["tag"], "#a855f7", "#ffffff", 13, pad_x=10, pad_y=3)
                d.text((end_bx + 12, my + 15), item["title"], fill=(255, 255, 255, 255), font=get_font(18, bold=True))

                by = my + 82
                f_b = get_font(16 if rows == 2 else 18)
                for b in item["bullets"]:
                    lines = wrap_text(b, f_b, cw - 40)
                    for lidx, ln in enumerate(lines[:2]):
                        d.text((mx + 20, by + lidx * 24), ln, fill=(233, 213, 255, 255), font=f_b)
                    by += max(42 if rows == 2 else 60, len(lines[:2]) * 24 + 14)

                ty = my + ch - 48
                d.rounded_rectangle([mx + 14, ty, mx + cw - 14, ty + 36], radius=6, fill=(8, 7, 20, 238), outline=(76, 29, 149, 255))
                d.text((mx + 22, ty + 9), "STACK:", fill=(192, 132, 252, 255), font=get_font(12, bold=True))
                t_ln = wrap_text(item["tools"], get_font(13), cw - 100)[0]
                d.text((mx + 80, ty + 9), t_ln, fill=(248, 250, 252, 255), font=get_font(13))

        final_img = Image.alpha_composite(bg, ov).convert("RGB")
        out_path = os.path.join(PHASES_DIR, f"ceh_v13_phase_{pnum}_overview.png")
        final_img.save(out_path, "PNG")
        print(f"Phase {pnum} overview saved: {out_path}")


if __name__ == "__main__":
    generate_module_banners()
    generate_animated_gif()
    generate_module_cards()
    generate_ai_matrix()
    generate_master_roadmap()
    generate_curriculum_map()
    generate_phase_infographics()
    print("ALL 20 CEH v13 VISUAL ASSETS REGENERATED CLEANLY!")
