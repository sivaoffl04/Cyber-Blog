#!/usr/bin/env python3
"""
Generate High-Quality Visual Media Assets for Threat Detection with Wazuh Sysmon Walkthrough
- threat_detection_wazuh_banner.jpg (1376x768)
- threat_detection_wazuh_workflow_map.jpg (1376x768)
- threat_detection_wazuh_live_demo.gif (920x520, animated multi-frame GIF)
- images/task_images/ (Task 1 to Task 7 visual cards)
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
TASK_DIR = os.path.join(IMAGES_DIR, "task_images")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(TASK_DIR, exist_ok=True)

# Fonts
font_huge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
font_large = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 16)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)
font_small = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 14)
font_mono_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)

def draw_grid_background(draw, width, height, grid_size=44, line_color=(18, 28, 48)):
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=line_color, width=1)
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=line_color, width=1)

def generate_hero_banner():
    print("Generating Wazuh Sysmon Hero Banner...")
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 48, (18, 28, 48))

    # Top header bar
    draw.rounded_rectangle([(40, 28), (w - 40, 72)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 40), "INE SECURITY LABS • THREAT DETECTION, HOST FORENSICS & SIEM/EDR ENGINEERING", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 240, 40), "WAZUH v4.X & SYSMON", fill=(245, 158, 11), font=font_subtitle)

    # Title & Subtitle
    draw.text((40, 96), "Threat Detection with Wazuh & Sysmon", fill=(248, 250, 252), font=font_huge)
    draw.text((40, 150), "Agent Setup, Sysmon Forwarding, Custom Level 12 XML Rules, PsExec PTH & Process Migration", fill=(148, 163, 184), font=font_title)

    # Badges
    badges = [
        ("100% SOLVED (7/7 TASKS)", (16, 185, 129)),
        ("WAZUH MANAGER 10.0.26.67", (2, 132, 199)),
        ("SYSMON OPERATIONAL CHANNEL", (147, 51, 234)),
        ("METASPLOIT PSEXEC PTH", (239, 68, 68)),
        ("MIMIKATZ & INJECTION RULES", (245, 158, 11)),
    ]
    cur_x = 40
    for text, color in badges:
        bw = int(draw.textlength(text, font=font_badge)) + 22
        draw.rounded_rectangle([(cur_x, 192), (cur_x + bw, 222)], radius=6, fill=color)
        draw.text((cur_x + 11, 199), text, fill=(255, 255, 255), font=font_badge)
        cur_x += bw + 14

    # 4 Metric Cards
    cards = [
        {"label": "WAZUH MANAGER IP", "val": "10.0.26.67", "sub": "Ubuntu 20.04 SIEM Manager", "color": (56, 189, 248)},
        {"label": "TARGET ENDPOINT", "val": "10.0.18.168", "sub": "Windows Server 2019 (Target)", "color": (16, 185, 129)},
        {"label": "ATTACK TECHNIQUE", "val": "Pass-The-Hash", "sub": "PsExec SMB NTLM relay", "color": (239, 68, 68)},
        {"label": "SECURITY ALERTS", "val": "26+ Level 12+", "sub": "Sysmon EID 1, 8, 10, 13", "color": (245, 158, 11)},
    ]
    cx = 40
    card_w = (w - 80 - 3 * 20) // 4
    for c in cards:
        draw.rounded_rectangle([(cx, 242), (cx + card_w, 342)], radius=8, fill=(15, 23, 42), outline=c["color"], width=2)
        draw.text((cx + 16, 256), c["label"], fill=(148, 163, 184), font=font_small)
        draw.text((cx + 16, 276), c["val"], fill=(248, 250, 252), font=font_large)
        draw.text((cx + 16, 314), c["sub"], fill=(203, 213, 225), font=font_small)
        cx += card_w + 20

    # Lower Panel: 7-Stage Execution Architecture
    draw.rounded_rectangle([(40, 362), (w - 40, 720)], radius=10, fill=(15, 23, 42), outline=(30, 41, 59), width=2)
    draw.text((60, 380), "WAZUH & SYSMON DETECTION ENGINEERING PIPELINE", fill=(56, 189, 248), font=font_title)

    steps = [
        ("Task 1: Wazuh Agent Deployment", "Silent MSI install with WAZUH_MANAGER=10.0.26.67 and registration to default group; service started", (56, 189, 248)),
        ("Task 2: SwiftOnSecurity Sysmon", "Installing Sysmon service using sysmonconfig-export.xml for comprehensive kernel and socket event auditing", (16, 185, 129)),
        ("Task 3: Forwarding Sysmon Logs", "Configuring ossec.conf eventchannel for Microsoft-Windows-Sysmon/Operational and disabling client_buffer", (168, 85, 247)),
        ("Task 4: Custom Mimikatz Rules", "Authoring Level 12 XML rules in local_rules.xml (100000: EID 1 Image, 100001: EID 8 Thread, 100002: EID 10 Access)", (245, 158, 11)),
        ("Task 5: Global Sysmon Ingest Rule", "Deploying Rule 220000 (Level 12) in local_rules.xml to elevate all Sysmon events into Wazuh Security Events", (56, 189, 248)),
        ("Task 6: Metasploit PsExec PTH Attack", "Exploiting 10.0.18.168 via exploit/windows/smb/psexec using NTLM hash; migrating to explorer.exe; adding wazuh-hacker", (239, 68, 68)),
        ("Task 7: Incident Triage in Wazuh UI", "Analyzing 26+ alerts: PsExec service creation (T1543.003), EID 8 injection into explorer.exe, and net user creation (T1136)", (236, 72, 153)),
    ]

    sy = 420
    for title, desc, col in steps:
        draw.ellipse([(60, sy + 3), (72, sy + 15)], fill=col)
        draw.text((82, sy), title, fill=col, font=font_subtitle)
        draw.text((380, sy + 2), "— " + desc, fill=(203, 213, 225), font=font_small)
        sy += 40

    out_path = os.path.join(IMAGES_DIR, "threat_detection_wazuh_banner.jpg")
    img.save(out_path, quality=95)
    print(f"Saved hero banner to {out_path}")

def generate_workflow_map():
    print("Generating Wazuh Sysmon Workflow Architecture Map...")
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 44, (18, 28, 48))

    draw.rounded_rectangle([(40, 24), (w - 40, 68)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 36), "WAZUH SYSMON THREAT DETECTION • SYSTEM ARCHITECTURE & DETECTION BLUEPRINT", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 280, 36), "7-TASK LAB BLUEPRINT", fill=(16, 185, 129), font=font_subtitle)

    boxes = [
        {"title": "TASK 1: Agent MSI Installation", "cmd": "msiexec /i wazuh-agent.msi WAZUH_MANAGER=10.0.26.67", "detail": "Connects Windows Server (10.0.18.168) to Wazuh Manager", "col": (56, 189, 248), "x": 40, "y": 88, "w": 400, "h": 128},
        {"title": "TASK 2: Sysmon Deployment", "cmd": "Sysmon.exe -i sysmonconfig-export.xml", "detail": "SwiftOnSecurity modular driver & event configuration", "col": (16, 185, 129), "x": 480, "y": 88, "w": 400, "h": 128},
        {"title": "TASK 3: Forwarding Configuration", "cmd": "ossec.conf -> Microsoft-Windows-Sysmon/Operational", "detail": "Configures eventchannel log forwarding in agent", "col": (168, 85, 247), "x": 920, "y": 88, "w": 416, "h": 128},

        {"title": "TASK 4: Mimikatz Rules (100000-100002)", "cmd": "Rules for EID 1 (Image), EID 8 (Thread), EID 10 (Access)", "detail": "Level 12 alerts triggered upon running mimikatz.exe", "col": (245, 158, 11), "x": 40, "y": 236, "w": 400, "h": 128},
        {"title": "TASK 5: All Sysmon Ingestion Rule", "cmd": "Rule id 220000 level 12 (<if_group>sysmon</if_group>)", "detail": "Promotes all Sysmon event IDs to high priority in UI", "col": (56, 189, 248), "x": 480, "y": 236, "w": 400, "h": 128},
        {"title": "TASK 6: Metasploit PsExec Attack", "cmd": "exploit/windows/smb/psexec (Pass-the-Hash)", "detail": "Lateral movement, explorer.exe migration & net user add", "col": (239, 68, 68), "x": 920, "y": 236, "w": 416, "h": 128},

        {"title": "TASK 7: Wazuh Dashboard Triage", "cmd": "Wazuh -> Modules -> Security Events (26+ Alerts)", "detail": "EID 1 (Service & Powershell), EID 8 (Migration), EID 1 (User add)", "col": (16, 185, 129), "x": 40, "y": 384, "w": 1296, "h": 128},

        {"title": "MITRE ATT&CK FRAMEWORK MAPPING", "cmd": "T1075 (Pass-The-Hash), T1543.003 (Windows Service), T1055 (Process Injection), T1136 (Create Account)", "detail": "Complete offensive kill chain detected, categorized, and visualized in Wazuh Security Events UI", "col": (56, 189, 248), "x": 40, "y": 532, "w": 1296, "h": 136},
    ]

    for b in boxes:
        draw.rounded_rectangle([(b["x"], b["y"]), (b["x"] + b["w"], b["y"] + b["h"])], radius=8, fill=(15, 23, 42), outline=b["col"], width=2)
        draw.text((b["x"] + 14, b["y"] + 10), b["title"], fill=b["col"], font=font_subtitle)
        draw.text((b["x"] + 14, b["y"] + 34), "Command: " + b["cmd"][:44], fill=(148, 163, 184), font=font_mono_small)

        bw = int(draw.textlength(b["detail"][:40], font=font_small)) + 16
        draw.rounded_rectangle([(b["x"] + 14, b["y"] + 58), (min(b["x"] + b["w"] - 14, b["x"] + 14 + bw), b["y"] + 82)], radius=4, fill=(19, 29, 49), outline=b["col"], width=1)
        draw.text((b["x"] + 22, b["y"] + 63), b["detail"][:40], fill=(248, 250, 252), font=font_small)

        draw.text((b["x"] + 14, b["y"] + 96), b["detail"], fill=(203, 213, 225), font=font_small)

    out_path = os.path.join(IMAGES_DIR, "threat_detection_wazuh_workflow_map.jpg")
    img.save(out_path, quality=95)
    print(f"Saved workflow map to {out_path}")

def generate_live_demo_gif():
    print("Generating Wazuh Sysmon Animated Live Demo GIF...")
    w, h = 920, 520
    frames = []

    steps = [
        ("Task 1: Wazuh Agent Installation", "msiexec /i wazuh-agent.msi WAZUH_MANAGER=10.0.26.67", "Agent Connected", "Active Agent verified in Wazuh Dashboard (10.0.18.168)"),
        ("Task 2: Sysmon Deployment", "Sysmon.exe -accepteula -i sysmonconfig-export.xml", "Sysmon Running", "SwiftOnSecurity config auditing kernel processes & sockets"),
        ("Task 3: Sysmon Eventchannel Forwarding", "ossec.conf -> Microsoft-Windows-Sysmon/Operational", "Forwarding Active", "Restarted WazuhSvc service; Sysmon logs reaching manager"),
        ("Task 4: Custom Mimikatz Rules (100000-100002)", "local_rules.xml -> rule id 100000-100002 level 12", "Rules Activated", "Triggered mimikatz.exe on Windows -> Level 12 Alert in UI"),
        ("Task 5: Global Sysmon Rule (220000)", "local_rules.xml -> rule id 220000 level 12", "All Sysmon Ingested", "All Sysmon events (EID 1, 3, 8, 10, 13) elevated to high priority"),
        ("Task 6A: Metasploit PsExec PTH", "use exploit/windows/smb/psexec (Pass-the-Hash)", "Meterpreter Shell", "Lateral movement via SMB NTLM hash -> NT AUTHORITY\\SYSTEM"),
        ("Task 6B: Process Migration & Account Creation", "migrate -N explorer.exe & net user /add wazuh-hacker", "PrivEsc & Backdoor", "Migrated to user session and created administrative user"),
        ("Task 7A: Wazuh Triage — PsExec Service Creation", "Event ID 1 & 13 (T1543.003)", "PsExec Service Alert", "Wazuh detected new service creating PowerShell Meterpreter"),
        ("Task 7B: Wazuh Triage — Process Migration", "Event ID 8 (CreateRemoteThread)", "Injection Alert", "Detected thread injection from SYSTEM to explorer.exe"),
        ("Task 7C: Wazuh Triage — Backdoor Account", "Event ID 1 (net user /add wazuh-hacker)", "T1136 Account Alert", "Detected rogue user creation and addition to localgroup administrators"),
    ]

    for title, cmd, status, sub in steps:
        frame = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(frame)

        # Chrome Header
        draw.rectangle([(0, 0), (w, 42)], fill=(30, 41, 59))
        draw.ellipse([(14, 15), (24, 25)], fill=(239, 68, 68))
        draw.ellipse([(32, 15), (42, 25)], fill=(245, 158, 11))
        draw.ellipse([(50, 15), (60, 25)], fill=(16, 185, 129))
        draw.text((76, 12), "Wazuh v4.x Security Operations Center — Threat Detection Dashboard", fill=(203, 213, 225), font=font_subtitle)

        # Command / Filter Box
        draw.rounded_rectangle([(20, 56), (w - 20, 100)], radius=6, fill=(11, 17, 32), outline=(56, 189, 248), width=2)
        draw.text((34, 68), "CMD / RULE: " + cmd, fill=(56, 189, 248), font=font_mono_bold)

        # Main Box
        draw.rounded_rectangle([(20, 116), (w - 20, 460)], radius=8, fill=(11, 17, 32), outline=(30, 41, 59), width=1)
        draw.text((40, 136), title, fill=(248, 250, 252), font=font_large)

        # Status badge
        draw.rounded_rectangle([(40, 180), (w - 40, 270)], radius=6, fill=(19, 29, 49), outline=(16, 185, 129), width=2)
        draw.text((60, 196), "WAZUH DETECTION & SIEM ALERT STATE:", fill=(148, 163, 184), font=font_small)
        draw.text((60, 218), status, fill=(16, 185, 129), font=font_large)

        draw.text((40, 290), "OBSERVED ATTACK FOOTPRINT & FORENSIC EVENT:", fill=(148, 163, 184), font=font_small)
        draw.text((40, 316), sub, fill=(203, 213, 225), font=font_body)

        draw.rounded_rectangle([(40, 360), (w - 40, 440)], radius=4, fill=(15, 23, 42))
        draw.text((54, 372), f"Execution: {cmd}", fill=(148, 163, 184), font=font_mono_small)
        draw.text((54, 400), "Telemetry: Windows Server (10.0.18.168) -> Wazuh Manager (10.0.26.67)", fill=(56, 189, 248), font=font_mono_small)

        draw.text((20, 480), "INE Hands-on Lab: Threat Detection with Wazuh Sysmon — 100% Solved", fill=(100, 116, 139), font=font_small)
        draw.text((w - 220, 480), "Live Demo Simulation", fill=(245, 158, 11), font=font_small)

        frames.append(frame)

    out_path = os.path.join(IMAGES_DIR, "threat_detection_wazuh_live_demo.gif")
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=1400, loop=0)
    print(f"Saved live demo GIF to {out_path}")

def generate_task_images():
    print("Generating Wazuh Task Summary Visual Cards...")
    tasks = [
        ("Task1", "Wazuh Agent MSI Deployment", "msiexec /i wazuh-agent.msi WAZUH_MANAGER=10.0.26.67", "Agent registered and active in Wazuh Dashboard"),
        ("Task2", "Sysmon Driver & Service Setup", "Sysmon.exe -accepteula -i sysmonconfig-export.xml", "SwiftOnSecurity modular configuration loaded"),
        ("Task3", "Forwarding Sysmon Telemetry", "ossec.conf eventchannel Microsoft-Windows-Sysmon", "WazuhSvc restarted; logs streaming to manager"),
        ("Task4", "Custom Mimikatz XML Rules", "local_rules.xml -> Rules 100000, 100001, 100002", "Level 12 alert on mimikatz.exe execution"),
        ("Task5", "All Sysmon Logs Ingest Rule", "local_rules.xml -> Rule 220000 level 12", "Elevates all Sysmon event IDs in Security Events"),
        ("Task6", "Metasploit PsExec PTH Attack", "exploit/windows/smb/psexec SMBPass=...5c4d5939...", "PTH to SYSTEM, migrate explorer.exe, add user"),
        ("Task7", "Wazuh Dashboard Incident Triage", "Wazuh -> Modules -> Security Events (26+ Alerts)", "Correlated PsExec service, EID 8 injection & net user"),
    ]

    for tid, title, cmd, detail in tasks:
        w, h = 640, 220
        img = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle([(10, 10), (w - 10, h - 10)], radius=8, fill=(11, 17, 32), outline=(56, 189, 248), width=2)

        draw.text((26, 24), f"THREAT DETECTION WITH WAZUH SYSMON • {tid.upper()}", fill=(56, 189, 248), font=font_subtitle)
        draw.text((26, 50), title, fill=(148, 163, 184), font=font_small)
        draw.text((26, 74), f"Action: {cmd}", fill=(203, 213, 225), font=font_mono_small)

        bw = int(draw.textlength(detail[:34], font=font_mono_bold)) + 24
        draw.rounded_rectangle([(26, 110), (min(w - 26, 26 + bw), 160)], radius=6, fill=(16, 185, 129))
        draw.text((38, 125), detail[:34], fill=(11, 17, 32), font=font_mono_bold)

        draw.text((26, 180), detail, fill=(100, 116, 139), font=font_small)

        out_p = os.path.join(TASK_DIR, f"{tid}.png")
        img.save(out_p)
    print(f"Generated {len(tasks)} task images in {TASK_DIR}")

if __name__ == "__main__":
    generate_hero_banner()
    generate_workflow_map()
    generate_live_demo_gif()
    generate_task_images()
    print("All Wazuh Sysmon visual media assets completed successfully!")
