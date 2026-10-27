import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Set UTF-8 stdout
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
PHASES_DIR = os.path.join(IMAGES_DIR, "phases")
MODULES_DIR = os.path.join(IMAGES_DIR, "modules")
BANNERS_DIR = os.path.join(IMAGES_DIR, "module_banners")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(PHASES_DIR, exist_ok=True)
os.makedirs(MODULES_DIR, exist_ok=True)
os.makedirs(BANNERS_DIR, exist_ok=True)

# Fonts
FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
if not os.path.exists(FONT_REG):
    FONT_REG = r"C:\Windows\Fonts\arial.ttf"
    FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

def get_font(size, bold=False):
    fpath = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(fpath, size)
    except:
        return ImageFont.load_default()

# 13 Modules Dataset (Strictly Modules with Official Courseware PDFs)
MODULES = [
    {
        "id": "01",
        "title": "Introduction to Ethical Hacking",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "phase_color": "#00d4ff",
        "concepts": [
            "CIA Triad, AAA Security Model & Non-Repudiation",
            "Adversary Kill Chains: Cyber Kill Chain & Diamond Model",
            "Information Warfare: Defensive vs Offensive Tactics",
            "AI-Powered Pentesting & Generative Security Tools"
        ],
        "tools": "PentestGPT · CyberChef · MISP · STIX/TAXII",
        "exam_focus": "CIA Triad, Hacker classes, Kill Chain phases, Legal/SLA boundaries"
    },
    {
        "id": "02",
        "title": "Footprinting & Reconnaissance",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "phase_color": "#00d4ff",
        "concepts": [
            "Passive & Active OSINT Gathering Frameworks",
            "Advanced Google Dorking & Search Operands",
            "DNS Reconnaissance, WHOIS Queries & BGP IP Blocks",
            "Subdomain Harvesting & Email Header Tracking"
        ],
        "tools": "Maltego · Recon-ng · theHarvester · Shodan · Amass",
        "exam_focus": "Google dorks, DNS record types (SOA, MX, TXT), Whois interrogation"
    },
    {
        "id": "03",
        "title": "Scanning Networks",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "phase_color": "#00d4ff",
        "concepts": [
            "TCP 3-Way Handshake & Flag States (SYN, ACK, FIN, RST)",
            "Stealth Scans: SYN Stealth (-sS), Xmas (-sX), FIN (-sF)",
            "Active Host Discovery & UDP Ping Sweeps",
            "TCP/IP Stack Fingerprinting & OS Detection"
        ],
        "tools": "Nmap · Hping3 · Masscan · ZMap · Angry IP",
        "exam_focus": "Nmap switches (-sS, -sT, -sU, -A), RFC 793 RST responses, Hping3 crafting"
    },
    {
        "id": "04",
        "title": "Enumeration",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "phase_color": "#00d4ff",
        "concepts": [
            "NetBIOS Name Service (137-139) & Name Suffixes",
            "SMB Null Sessions, IPC$ Shares & RID Cycling",
            "SNMP Community Strings (public/private) & MIB Traversal",
            "LDAP Queries, NTP Monlist Amplification, SMTP (VRFY/EXPN)"
        ],
        "tools": "Enum4linux · Nbtstat · Snmpwalk · Ldapsearch · Rpcclient",
        "exam_focus": "NetBIOS codes (<00>, <20>, <1B>), SNMPv1 vs v3 security, RID range calculation"
    },
    {
        "id": "05",
        "title": "Vulnerability Analysis",
        "phase": 1,
        "phase_name": "Reconnaissance & Assessment",
        "phase_color": "#00d4ff",
        "concepts": [
            "Vulnerability Assessment Lifecycle & Pre-Assessment Setup",
            "CVSS v3.1 & v4 Scoring Metrics (Base, Temporal, Env)",
            "CVE Identifiers & National Vulnerability Database (NVD)",
            "Vulnerability Classification: Design vs Config Flaws"
        ],
        "tools": "Nessus · OpenVAS · QualysGuard · Nikto · GFI LanGuard",
        "exam_focus": "CVSS calculation vectors (AV, AC, PR, UI, S, C, I, A), False positive handling"
    },

    # Phase 2: Host & Network Exploitation (Modules 06 - 12)
    {
        "id": "06",
        "title": "System Hacking",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "phase_color": "#ff385c",
        "concepts": [
            "Password Cracking: Pass-The-Hash, LLMNR/NBT-NS Poisoning",
            "Buffer Overflow Exploitation & Shellcode Injection",
            "Privilege Escalation (UAC Bypass, DLL Hijacking, Token Abuse)",
            "Covering Tracks: Clearing EVTX Logs, Auditpol, ADS"
        ],
        "tools": "Responder · Mimikatz · John the Ripper · Hashcat · Metasploit",
        "exam_focus": "SAM database structure, NTLM hash anatomy, Pass-The-Hash mechanics"
    },
    {
        "id": "07",
        "title": "Malware Threats",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "phase_color": "#ff385c",
        "concepts": [
            "Trojans, Viruses, Worms, Rootkits & Ransomware Lifecycles",
            "Crypters, Packers, Wrappers & Code Obfuscation",
            "Botnet Command & Control (C2) Architectures (IRC/HTTP/P2P)",
            "Static & Dynamic Malware Analysis in Isolated Sandboxes"
        ],
        "tools": "Ghidra · IDA Pro · Pestudio · Cuckoo Sandbox · Any.Run",
        "exam_focus": "Malware classification, Dropper vs Downloader, PE header analysis"
    },
    {
        "id": "08",
        "title": "Sniffing",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "phase_color": "#ff385c",
        "concepts": [
            "Passive vs Active Sniffing in Switched Networks",
            "MAC Flooding (CAM Table Exhaustion) & Switch Port Security",
            "ARP Poisoning & Man-in-the-Middle (MitM) Interception",
            "DHCP Starvation, Rogue DHCP Servers & DNS Spoofing"
        ],
        "tools": "Wireshark · Ettercap · Bettercap · Macof · Yersinia · TCPDump",
        "exam_focus": "CAM overflow mitigation (Port Security), Gratuitous ARP, Wireshark filters"
    },
    {
        "id": "09",
        "title": "Social Engineering",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "phase_color": "#ff385c",
        "concepts": [
            "Human-Based: Phishing, Spearphishing, Whaling, Vishing, Smishing",
            "Physical Vectors: Dumpster Diving, Tailgating, Shoulder Surfing",
            "Influence Tactics: Authority, Scarcity, Urgency, Social Proof",
            "Insider Threat Profiling & Enterprise Awareness Training"
        ],
        "tools": "Social-Engineer Toolkit (SET) · GoPhish · Evilginx2 · King Phisher",
        "exam_focus": "Psychological triggers, Reverse social engineering, MFA interception"
    },
    {
        "id": "10",
        "title": "Denial-of-Service",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "phase_color": "#ff385c",
        "concepts": [
            "Volumetric vs Protocol vs Application-Layer DoS",
            "SYN Floods, Smurf Attacks (ICMP Directed Broadcast), UDP Floods",
            "Amplification Attacks: NTP Monlist, DNS Open Resolvers, Memcached",
            "Slowloris & R-U-Dead-Yet (RUDY) HTTP Exhaustion"
        ],
        "tools": "LOIC · HOIC · Slowloris · Hping3 · GoldenEye",
        "exam_focus": "SYN cookies, TCP backlog queue, Bandwidth amplification factor, Botnets"
    },
    {
        "id": "11",
        "title": "Session Hijacking",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "phase_color": "#ff385c",
        "concepts": [
            "Network-Level: TCP Sequence Number Prediction & RST Attacks",
            "Application-Level: Session Token Sniffing, Fixation & Replay",
            "Man-in-the-Browser (MitB) & DOM-Based Session Theft",
            "Defenses: Strict Session Invalidation, SameSite & HttpOnly Cookies"
        ],
        "tools": "Burp Suite · Bettercap · OWASP ZAP · Hamster & Ferret",
        "exam_focus": "TCP initial sequence numbers (ISN), 3-way handshake spoofing, Session entropy"
    },
    {
        "id": "12",
        "title": "Evading IDS, Firewalls & Honeypots",
        "phase": 2,
        "phase_name": "Host & Network Hacking",
        "phase_color": "#ff385c",
        "concepts": [
            "Signature Evasion: Packet Fragmentation & Overlapping Fragments",
            "Source Routing, Decoy Scanning (-D), & IP Address Spoofing",
            "Protocol Tunneling: SSH Port Forwarding, DNS & ICMP Tunneling",
            "Honeypot Detection & High-Interaction vs Low-Interaction Traps"
        ],
        "tools": "Nmap · Snort · Suricata · Proxychains · Ptunnel · Iodine",
        "exam_focus": "Snort rule syntax, Fragmentation flags (-f, --mtu), Honeyd fingerprinting"
    },

    # Phase 3: Web Server Exploitation & AI Security (Module 13 + AI Framework)
    {
        "id": "13",
        "title": "Hacking Web Servers",
        "phase": 3,
        "phase_name": "Web Server Exploitation & AI",
        "phase_color": "#ffb300",
        "concepts": [
            "Web Server Architectures (Apache, Nginx, Microsoft IIS)",
            "Default Credentials, Directory Traversal & Source Code Leaks",
            "WebDAV Insecure Methods (PUT, MOVE, COPY) & Webshell Dropping",
            "HTTP Request Smuggling, Pipeline Desynchronization & Hardening"
        ],
        "tools": "Nikto · Metasploit · Wpscan · Burp Suite · Nmap HTTP Scripts",
        "exam_focus": "IIS metabase vulnerabilities, WebDAV permissions, Server banner hiding"
    }
]

PHASES_META = [
    {
        "phase": 1,
        "name": "Phase 1: Information Gathering & Vulnerability Assessment",
        "subtitle": "Modules 01 - 05 • Reconnaissance, OSINT, Scanning, Enumeration & Vulnerability Discovery",
        "color": "#00d4ff",
        "modules": [m for m in MODULES if m["phase"] == 1]
    },
    {
        "phase": 2,
        "name": "Phase 2: Host & Network Exploitation",
        "subtitle": "Modules 06 - 12 • System Hacking, Malware, Sniffing, Social Eng, DoS, Hijacking & Evasion",
        "color": "#ff385c",
        "modules": [m for m in MODULES if m["phase"] == 2]
    },
    {
        "phase": 3,
        "name": "Phase 3: Web Server Exploitation & AI-Powered Security",
        "subtitle": "Module 13 + CEH v13 AI Architecture • Web Architecture, Attack Surface & AI Framework",
        "color": "#ffb300",
        "modules": [m for m in MODULES if m["phase"] == 3]
    }
]

def draw_badge(draw, x, y, text, bg_color, text_color="#ffffff", font_size=16, pad_x=12, pad_y=6, radius=6):
    fnt = get_font(font_size, bold=True)
    bbox = fnt.getbbox(text)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    box = [x, y, x + w + pad_x * 2, y + h + pad_y * 2]
    draw.rounded_rectangle(box, radius=radius, fill=bg_color)
    draw.text((x + pad_x, y + pad_y - bbox[1]), text, fill=text_color, font=fnt)
    return box[2]

# -------------------------------------------------------------
# 1. Master CEH v13 13-Module Architecture Roadmap (3 Columns)
# -------------------------------------------------------------
def generate_master_roadmap():
    print("Generating Master 13-Module Roadmap Infographic...")
    W, H = 3400, 2200
    img = Image.new("RGB", (W, H), "#070b14")
    draw = ImageDraw.Draw(img)

    # Background subtle grid pattern
    for gx in range(0, W, 80):
        draw.line([(gx, 0), (gx, H)], fill="#0c1322", width=1)
    for gy in range(0, H, 80):
        draw.line([(0, gy), (W, gy)], fill="#0c1322", width=1)

    # Top Header Panel
    draw.rounded_rectangle([40, 30, W - 40, 230], radius=16, fill="#0d1527", outline="#1e293b", width=2)
    draw.line([(60, 32), (W - 60, 32)], fill="#00d4ff", width=3)

    # Title & Subtitle
    title_font = get_font(44, bold=True)
    draw.text((80, 55), "CERTIFIED ETHICAL HACKER (CEH v13) — 13-MODULE MASTER ARCHITECTURE", fill="#ffffff", font=title_font)
    
    sub_font = get_font(22, bold=False)
    draw.text((80, 115), "Official Courseware Slide Decks • Adversary Tradecraft • Attack Lifecycles • AI-Powered Security Engineering", fill="#94a3b8", font=sub_font)

    # Badges
    bx = 80
    by = 160
    bx = draw_badge(draw, bx, by, "EC-COUNCIL 312-50", "#0078d4", "#ffffff", 16) + 15
    bx = draw_badge(draw, bx, by, "ANSI 17024 ACCREDITED", "#0284c7", "#ffffff", 16) + 15
    bx = draw_badge(draw, bx, by, "13 CORE DOMAINS WITH PDFS", "#10b981", "#ffffff", 16) + 15
    bx = draw_badge(draw, bx, by, "3 OPERATIONAL PHASES", "#f59e0b", "#ffffff", 16) + 15
    bx = draw_badge(draw, bx, by, "⚡ AI-POWERED ETHICAL HACKING", "#a855f7", "#ffffff", 16) + 15
    bx = draw_badge(draw, bx, by, "MITRE ATT&CK ALIGNED", "#ec4899", "#ffffff", 16) + 15

    # 3 Phase Columns
    col_w = (W - 80 - 40) // 3
    start_y = 250
    content_h = H - start_y - 140

    for i, phase in enumerate(PHASES_META):
        cx = 40 + i * (col_w + 20)
        cy = start_y

        # Phase Header Card
        draw.rounded_rectangle([cx, cy, cx + col_w, cy + 90], radius=12, fill="#0f172a", outline=phase["color"], width=2)
        draw_badge(draw, cx + 15, cy + 12, f"PHASE 0{phase['phase']}", phase["color"], "#000000", 14, pad_x=8, pad_y=3)
        
        p_name = phase["name"].split(": ")[1]
        draw.text((cx + 15, cy + 48), p_name[:36], fill="#ffffff", font=get_font(18, bold=True))

        mods = phase["modules"]
        mod_y = cy + 105

        if phase["phase"] == 1:
            # 5 modules in column 1
            card_h = (content_h - 105 - (5 - 1) * 12) // 5
            for m in mods:
                card_box = [cx, mod_y, cx + col_w, mod_y + card_h]
                draw.rounded_rectangle(card_box, radius=10, fill="#0b1120", outline="#1e293b", width=1)
                draw.rounded_rectangle([cx, mod_y, cx + 6, mod_y + card_h], radius=3, fill=phase["color"])

                draw_badge(draw, cx + 16, mod_y + 12, f"M{m['id']}", phase["color"], "#000000", 14, pad_x=7, pad_y=2)
                draw.text((cx + 72, mod_y + 13), m["title"][:32], fill="#f8fafc", font=get_font(17, bold=True))

                by = mod_y + 46
                for conc in m["concepts"][:3]:
                    draw.text((cx + 20, by), "•", fill=phase["color"], font=get_font(14, bold=True))
                    draw.text((cx + 34, by), conc[:45], fill="#cbd5e1", font=get_font(13, bold=False))
                    by += 22

                draw.text((cx + 20, mod_y + card_h - 52), "Tools:", fill="#64748b", font=get_font(12, bold=True))
                draw.text((cx + 65, mod_y + card_h - 52), m["tools"][:42], fill="#38bdf8", font=get_font(12, bold=False))

                draw.text((cx + 20, mod_y + card_h - 26), "Exam:", fill="#e2e8f0", font=get_font(12, bold=True))
                draw.text((cx + 65, mod_y + card_h - 26), m["exam_focus"][:42], fill="#f59e0b", font=get_font(12, bold=False))

                mod_y += card_h + 12

        elif phase["phase"] == 2:
            # 7 modules in column 2
            card_h = (content_h - 105 - (7 - 1) * 10) // 7
            for m in mods:
                card_box = [cx, mod_y, cx + col_w, mod_y + card_h]
                draw.rounded_rectangle(card_box, radius=10, fill="#0b1120", outline="#1e293b", width=1)
                draw.rounded_rectangle([cx, mod_y, cx + 6, mod_y + card_h], radius=3, fill=phase["color"])

                draw_badge(draw, cx + 16, mod_y + 10, f"M{m['id']}", phase["color"], "#000000", 13, pad_x=6, pad_y=2)
                draw.text((cx + 68, mod_y + 11), m["title"][:32], fill="#f8fafc", font=get_font(16, bold=True))

                by = mod_y + 38
                for conc in m["concepts"][:2]:
                    draw.text((cx + 20, by), "•", fill=phase["color"], font=get_font(13, bold=True))
                    draw.text((cx + 34, by), conc[:45], fill="#cbd5e1", font=get_font(12, bold=False))
                    by += 19

                draw.text((cx + 20, mod_y + card_h - 44), "Tools:", fill="#64748b", font=get_font(11, bold=True))
                draw.text((cx + 62, mod_y + card_h - 44), m["tools"][:42], fill="#38bdf8", font=get_font(11, bold=False))

                draw.text((cx + 20, mod_y + card_h - 22), "Exam:", fill="#e2e8f0", font=get_font(11, bold=True))
                draw.text((cx + 62, mod_y + card_h - 22), m["exam_focus"][:42], fill="#f59e0b", font=get_font(11, bold=False))

                mod_y += card_h + 10

        elif phase["phase"] == 3:
            # Module 13 card + Large AI-Powered Ethical Hacking Master Panel
            m13 = mods[0]
            card_h = 280
            card_box = [cx, mod_y, cx + col_w, mod_y + card_h]
            draw.rounded_rectangle(card_box, radius=10, fill="#0b1120", outline="#1e293b", width=1)
            draw.rounded_rectangle([cx, mod_y, cx + 6, mod_y + card_h], radius=3, fill=phase["color"])

            draw_badge(draw, cx + 16, mod_y + 14, f"M{m13['id']}", phase["color"], "#000000", 14, pad_x=7, pad_y=3)
            draw.text((cx + 72, mod_y + 15), m13["title"], fill="#f8fafc", font=get_font(18, bold=True))

            by = mod_y + 54
            for conc in m13["concepts"]:
                draw.text((cx + 20, by), "•", fill=phase["color"], font=get_font(14, bold=True))
                draw.text((cx + 34, by), conc[:45], fill="#cbd5e1", font=get_font(13, bold=False))
                by += 24

            draw.text((cx + 20, mod_y + card_h - 58), "Tools:", fill="#64748b", font=get_font(13, bold=True))
            draw.text((cx + 70, mod_y + card_h - 58), m13["tools"], fill="#38bdf8", font=get_font(13, bold=False))

            draw.text((cx + 20, mod_y + card_h - 30), "Exam:", fill="#e2e8f0", font=get_font(13, bold=True))
            draw.text((cx + 70, mod_y + card_h - 30), m13["exam_focus"], fill="#f59e0b", font=get_font(13, bold=False))

            # AI Master Panel
            mod_y += card_h + 16
            ai_box = [cx, mod_y, cx + col_w, cy + content_h]
            draw.rounded_rectangle(ai_box, radius=14, fill="#120c29", outline="#a855f7", width=2)
            
            draw_badge(draw, cx + 20, mod_y + 20, "⚡ WHAT'S NEW IN CEH v13", "#a855f7", "#ffffff", 14, pad_x=10, pad_y=4)
            draw.text((cx + 20, mod_y + 64), "AI-Driven Ethical Hacking Framework", fill="#ffffff", font=get_font(22, bold=True))
            draw.text((cx + 20, mod_y + 98), "EC-Council formal integration of Generative AI tradecraft", fill="#c084fc", font=get_font(14, bold=False))

            ai_points = [
                ("1. AI Reconnaissance & OSINT:", "LLM autonomous target profiling, automated search dorking, surface graphing."),
                ("2. AI Vulnerability Discovery:", "Semantic static code audits, automated payload synthesis, API logic fuzzing."),
                ("3. AI Exploit Crafting & Evasion:", "Polymorphic shellcode generation, adaptive C2 beaconing, evasion syntax."),
                ("4. AI Threat Hunting & SOC Ops:", "Real-time UEBA behavioral telemetry correlation and automated playbooks."),
                ("5. Defending AI Architectures:", "OWASP LLM Top 10: Prompt injection, model inversion, jailbreak defenses.")
            ]

            ai_y = mod_y + 140
            for h_txt, b_txt in ai_points:
                draw.text((cx + 22, ai_y), h_txt, fill="#ec4899", font=get_font(15, bold=True))
                draw.text((cx + 22, ai_y + 24), b_txt, fill="#e2e8f0", font=get_font(13, bold=False))
                ai_y += 68

    # Bottom Footer Status Bar
    draw.rounded_rectangle([40, H - 95, W - 40, H - 35], radius=10, fill="#0d1527", outline="#1e293b", width=1)
    
    foot_font = get_font(16, bold=False)
    draw.text((60, H - 75), "Cyber Kill Chain: Reconnaissance ➔ Weaponization ➔ Delivery ➔ Exploitation ➔ Installation ➔ Command & Control ➔ Actions on Objectives", fill="#94a3b8", font=foot_font)
    
    author_font = get_font(15, bold=True)
    draw.text((W - 550, H - 75), "Cyber-Blog • Production Engineering Knowledge Base", fill="#38bdf8", font=author_font)

    out_path = os.path.join(IMAGES_DIR, "ceh_v13_all_modules_roadmap.png")
    img.save(out_path, "PNG", quality=95)
    print(f"Master Roadmap saved to: {out_path}")
    return out_path

# -------------------------------------------------------------
# 2. Generate 3 Phase-Specific In-Depth Infographics
# -------------------------------------------------------------
def generate_phase_infographics():
    for p_info in PHASES_META:
        p_num = p_info["phase"]
        print(f"Generating Phase {p_num} Infographic...")
        W, H = 2400, 1500
        img = Image.new("RGB", (W, H), "#080d1a")
        draw = ImageDraw.Draw(img)

        # Subtle Grid
        for gx in range(0, W, 60):
            draw.line([(gx, 0), (gx, H)], fill="#0d1527", width=1)
        for gy in range(0, H, 60):
            draw.line([(0, gy), (W, gy)], fill="#0d1527", width=1)

        # Header Box
        draw.rounded_rectangle([40, 30, W - 40, 200], radius=16, fill="#0d1527", outline=p_info["color"], width=2)
        draw.line([(60, 32), (W - 60, 32)], fill=p_info["color"], width=3)

        draw_badge(draw, 70, 50, f"CEH v13 MASTER TRACK — PHASE 0{p_num}", p_info["color"], "#000000", 16)
        draw.text((70, 95), p_info["name"], fill="#ffffff", font=get_font(38, bold=True))
        draw.text((70, 148), p_info["subtitle"], fill="#94a3b8", font=get_font(18, bold=False))

        mods = p_info["modules"]
        
        if p_num == 1:
            cols = 3
            rows = 2
        elif p_num == 2:
            cols = 4
            rows = 2
        else: # Phase 3: Module 13 + AI Panel
            cols = 2
            rows = 1

        grid_x = 40
        grid_y = 230
        grid_w = W - 80
        grid_h = H - grid_y - 60

        card_w = (grid_w - (cols - 1) * 20) // cols
        card_h = (grid_h - (rows - 1) * 20) // rows

        for idx, m in enumerate(mods):
            r = idx // cols
            c = idx % cols
            mx = grid_x + c * (card_w + 20)
            my = grid_y + r * (card_h + 20)

            draw.rounded_rectangle([mx, my, mx + card_w, my + card_h], radius=14, fill="#0e172a", outline="#1e293b", width=1)
            draw.rounded_rectangle([mx, my, mx + card_w, my + 60], radius=14, fill="#131e36")
            draw.rectangle([mx, my + 45, mx + card_w, my + 60], fill="#131e36")
            
            draw_badge(draw, mx + 16, my + 14, f"MODULE {m['id']}", p_info["color"], "#000000", 14, pad_x=8, pad_y=4)
            draw.text((mx + 130, my + 18), m["title"][:28], fill="#ffffff", font=get_font(18, bold=True))

            draw.text((mx + 20, my + 75), "CORE CONCEPTS & VECTORS", fill=p_info["color"], font=get_font(14, bold=True))
            
            by = my + 105
            for conc in m["concepts"]:
                draw.text((mx + 20, by), "▶", fill=p_info["color"], font=get_font(11, bold=False))
                draw.text((mx + 36, by), conc, fill="#e2e8f0", font=get_font(13, bold=False))
                by += 26

            t_box_y = my + card_h - 110
            draw.rounded_rectangle([mx + 16, t_box_y, mx + card_w - 16, t_box_y + 40], radius=8, fill="#0a0f1d", outline="#1e293b")
            draw.text((mx + 26, t_box_y + 10), "TOOLS:", fill="#64748b", font=get_font(12, bold=True))
            draw.text((mx + 80, t_box_y + 10), m["tools"], fill="#38bdf8", font=get_font(12, bold=False))

            e_box_y = my + card_h - 60
            draw.rounded_rectangle([mx + 16, e_box_y, mx + card_w - 16, e_box_y + 45], radius=8, fill="#1c1917", outline="#44403c")
            draw.text((mx + 26, e_box_y + 12), "EXAM FOCUS:", fill="#f59e0b", font=get_font(12, bold=True))
            draw.text((mx + 115, e_box_y + 12), m["exam_focus"][:55], fill="#fde68a", font=get_font(12, bold=False))

        # For Phase 3, add AI Companion Card in the 2nd slot
        if p_num == 3:
            mx = grid_x + (card_w + 20)
            my = grid_y
            draw.rounded_rectangle([mx, my, mx + card_w, my + card_h], radius=14, fill="#120c29", outline="#a855f7", width=2)
            draw.rounded_rectangle([mx, my, mx + card_w, my + 60], radius=14, fill="#1e1342")
            draw.rectangle([mx, my + 45, mx + card_w, my + 60], fill="#1e1342")

            draw_badge(draw, mx + 16, my + 14, "AI HACKING", "#a855f7", "#ffffff", 14, pad_x=8, pad_y=4)
            draw.text((mx + 130, my + 18), "AI-Driven Ethical Hacking Architecture", fill="#ffffff", font=get_font(18, bold=True))

            ai_items = [
                ("1. AI Reconnaissance:", "Automated surface mapping & LLM OSINT correlation"),
                ("2. AI Vulnerability Mining:", "Context-aware code analysis & logic flaw discovery"),
                ("3. AI Exploit Synthesis:", "Polymorphic shellcode & adaptive bypass payloads"),
                ("4. AI Threat Hunting:", "Real-time SIEM UEBA behavioral anomaly tracking"),
                ("5. Defending AI Infrastructure:", "OWASP LLM Top 10 prompt injection & jailbreak defense")
            ]
            
            by = my + 80
            for h_txt, b_txt in ai_items:
                draw.text((mx + 20, by), h_txt, fill="#ec4899", font=get_font(14, bold=True))
                draw.text((mx + 20, by + 20), b_txt, fill="#e2e8f0", font=get_font(13, bold=False))
                by += 52

            t_box_y = my + card_h - 110
            draw.rounded_rectangle([mx + 16, t_box_y, mx + card_w - 16, t_box_y + 40], radius=8, fill="#080714", outline="#2e2154")
            draw.text((mx + 26, t_box_y + 10), "AI TOOLS:", fill="#a855f7", font=get_font(12, bold=True))
            draw.text((mx + 95, t_box_y + 10), "PentestGPT · Semgrep AI · ShellGPT · Garak · Promptfoo", fill="#f8fafc", font=get_font(12, bold=False))

            e_box_y = my + card_h - 60
            draw.rounded_rectangle([mx + 16, e_box_y, mx + card_w - 16, e_box_y + 45], radius=8, fill="#1c1917", outline="#44403c")
            draw.text((mx + 26, e_box_y + 12), "EXAM FOCUS:", fill="#f59e0b", font=get_font(12, bold=True))
            draw.text((mx + 115, e_box_y + 12), "AI Prompt Injection, Model Poisoning, Jailbreaking, Automated Exploits", fill="#fde68a", font=get_font(12, bold=False))

        out_name = f"ceh_v13_phase_{p_num}_overview.png"
        out_path = os.path.join(PHASES_DIR, out_name)
        img.save(out_path, "PNG", quality=95)
        print(f"Phase {p_num} image saved to: {out_path}")

# -------------------------------------------------------------
# 3. Generate 13 Individual Module Cards
# -------------------------------------------------------------
def generate_individual_module_cards():
    print("Generating 13 Individual Module Cards...")
    for m in MODULES:
        W, H = 1400, 900
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
        draw.line([(40, 32), (W - 40, 32)], fill=color, width=3)

        draw_badge(draw, 60, 50, f"CEH v13 — MODULE {m['id']}", color, "#000000", 16, pad_x=12, pad_y=5)
        draw_badge(draw, 320, 50, f"PHASE 0{m['phase']}: {m['phase_name'].upper()}", "#334155", "#ffffff", 14, pad_x=10, pad_y=5)
        
        draw.text((60, 105), m["title"], fill="#ffffff", font=get_font(34, bold=True))

        draw.rounded_rectangle([60, 200, W - 60, 530], radius=14, fill="#090f1d", outline="#1e293b", width=1)
        draw.text((90, 225), "KEY ATTACK VECTORS & METHODOLOGY DOMAINS", fill=color, font=get_font(18, bold=True))

        cy = 275
        for idx, conc in enumerate(m["concepts"]):
            draw_badge(draw, 90, cy, f"0{idx+1}", color, "#000000", 12, pad_x=6, pad_y=2)
            draw.text((140, cy + 2), conc, fill="#f1f5f9", font=get_font(18, bold=False))
            cy += 58

        box_w = (W - 120 - 30) // 2
        
        # Tools Box
        draw.rounded_rectangle([60, 560, 60 + box_w, H - 60], radius=14, fill="#090f1d", outline="#1e293b", width=1)
        draw.text((85, 585), "INDUSTRY TOOLS & FRAMEWORKS", fill="#38bdf8", font=get_font(16, bold=True))
        
        tool_list = [t.strip() for t in m["tools"].split("·")]
        ty = 630
        for tool in tool_list:
            draw.text((90, ty), "⚡", fill="#38bdf8", font=get_font(15, bold=False))
            draw.text((115, ty), tool, fill="#e2e8f0", font=get_font(16, bold=False))
            ty += 38

        # Exam Focus Box
        draw.rounded_rectangle([60 + box_w + 30, 560, W - 60, H - 60], radius=14, fill="#1c1917", outline="#f59e0b", width=1)
        draw.text((60 + box_w + 55, 585), "EXAM FOCUS & TRADECRAFT OBJECTIVES", fill="#f59e0b", font=get_font(16, bold=True))
        draw.text((60 + box_w + 55, 630), "Core Tested Scenarios:", fill="#fde68a", font=get_font(15, bold=True))
        draw.text((60 + box_w + 55, 665), m["exam_focus"], fill="#f8fafc", font=get_font(16, bold=False))
        draw.text((60 + box_w + 55, 740), "Standard: ANSI 17024 Accredited • EC-Council Exam 312-50", fill="#78716c", font=get_font(13, bold=False))

        out_name = f"Module_{m['id']}.png"
        out_path = os.path.join(MODULES_DIR, out_name)
        img.save(out_path, "PNG", quality=95)

        # Also copy to Module folder
        target_mod_dir = os.path.join(BASE_DIR, f"Module {m['id']}", "images")
        if os.path.exists(target_mod_dir):
            mod_card_path = os.path.join(target_mod_dir, "module_card.png")
            img.save(mod_card_path, "PNG", quality=95)

    print("All 13 individual module cards generated successfully!")

# -------------------------------------------------------------
# 4. Generate 13-Module Animated GIF Showcase
# -------------------------------------------------------------
def generate_animated_gif():
    print("Generating 13-Module Animated GIF Showcase...")
    frames = []
    for m in MODULES:
        banner_path = os.path.join(BANNERS_DIR, f"module_{m['id']}_banner.jpg")
        if not os.path.exists(banner_path):
            banner_path = os.path.join(BASE_DIR, f"Module {m['id']}", "images", "banner.jpg")
        if os.path.exists(banner_path):
            img = Image.open(banner_path).convert("RGB")
            img = img.resize((960, 540), Image.Resampling.LANCZOS)
            frames.append(img)
    
    if frames:
        gif_out = os.path.join(IMAGES_DIR, "cehv13_modules_overview.gif")
        frames[0].save(
            gif_out,
            save_all=True,
            append_images=frames[1:],
            duration=1200,
            loop=0,
            optimize=True
        )
        print(f"Animated GIF saved to: {gif_out}")

if __name__ == "__main__":
    generate_master_roadmap()
    generate_phase_infographics()
    generate_individual_module_cards()
    generate_animated_gif()
    print("ALL CEH v13 (13 MODULES) GENERATION COMPLETE!")
