#!/usr/bin/env python3
"""
Generate High-Quality Visual Media Assets for Threat Detection With Elasticsearch And Kibana Walkthrough
- threat_detection_elk_banner.jpg (1376x768)
- threat_detection_elk_workflow_map.jpg (1376x768)
- threat_detection_elk_live_demo.gif (920x520, animated multi-frame GIF)
- images/task_images/ (Task 1 to Task 8 visual cards)
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
    print("Generating Hero Banner...")
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 48, (18, 28, 48))

    # Top header bar
    draw.rounded_rectangle([(40, 28), (w - 40, 72)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 40), "INE SECURITY LABS • THREAT HUNTING, RED-TO-BLUE EMULATION & SIEM DETECTION", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 260, 40), "HELK / ELASTICSEARCH / KIBANA", fill=(245, 158, 11), font=font_subtitle)

    # Title & Subtitle
    draw.text((40, 96), "Threat Detection with Elasticsearch & Kibana", fill=(248, 250, 252), font=font_huge)
    draw.text((40, 150), "Advanced Auditing, Sysmon & Winlogbeat Pipeline, Rejetto HFS Exploit & Mimikatz Triage", fill=(148, 163, 184), font=font_title)

    # Badges
    badges = [
        ("100% COMPLETED (8/8 TASKS)", (16, 185, 129)),
        ("HELK / KAFKA (PORT 9092)", (2, 132, 199)),
        ("SYSMON & WINLOGBEAT", (147, 51, 234)),
        ("METASPLOIT REJETTO HFS", (239, 68, 68)),
        ("MIMIKATZ LSASS SCRAPING", (245, 158, 11)),
    ]
    cur_x = 40
    for text, color in badges:
        bw = int(draw.textlength(text, font=font_badge)) + 22
        draw.rounded_rectangle([(cur_x, 192), (cur_x + bw, 222)], radius=6, fill=color)
        draw.text((cur_x + 11, 199), text, fill=(255, 255, 255), font=font_badge)
        cur_x += bw + 14

    # 4 Metric Cards
    cards = [
        {"label": "SOC HELK BROKER", "val": "10.0.21.29:9092", "sub": "Kafka ingest to Elasticsearch", "color": (56, 189, 248)},
        {"label": "TARGET SERVER", "val": "demo2.ine.local", "sub": "Windows Server 2019 (Target)", "color": (16, 185, 129)},
        {"label": "EXPLOITED SERVICE", "val": "Rejetto HFS 2.3", "sub": "Port 80 RCE via Metasploit", "color": (239, 68, 68)},
        {"label": "CREDENTIAL DUMP", "val": "NTLM Hashes", "sub": "Mimikatz sekurlsa::logonPasswords", "color": (245, 158, 11)},
    ]
    cx = 40
    card_w = (w - 80 - 3 * 20) // 4
    for c in cards:
        draw.rounded_rectangle([(cx, 242), (cx + card_w, 342)], radius=8, fill=(15, 23, 42), outline=c["color"], width=2)
        draw.text((cx + 16, 256), c["label"], fill=(148, 163, 184), font=font_small)
        draw.text((cx + 16, 276), c["val"], fill=(248, 250, 252), font=font_large)
        draw.text((cx + 16, 314), c["sub"], fill=(203, 213, 225), font=font_small)
        cx += card_w + 20

    # Lower Panel: 8-Stage Execution Architecture
    draw.rounded_rectangle([(40, 362), (w - 40, 720)], radius=10, fill=(15, 23, 42), outline=(30, 41, 59), width=2)
    draw.text((60, 380), "END-TO-END DETECTION ENGINEERING & THREAT HUNTING PIPELINE", fill=(56, 189, 248), font=font_title)

    steps = [
        ("Task 1: HELK Stack Deployment", "Starting dockerized hunting stack via ./helk_install.sh (Kibana https://localhost helk:hunting)", (56, 189, 248)),
        ("Task 2: Detailed Windows Auditing", "Enabling Process Creation/Termination, Command-Line Arguments, PowerShell ScriptBlock, and Task Scheduler logs", (245, 158, 11)),
        ("Task 3: SwiftOnSecurity Sysmon", "Installing Sysmon service using sysmonconfig-export.xml for deep process and network connection telemetry", (16, 185, 129)),
        ("Task 4: Winlogbeat Shipper Setup", "Configuring Winlogbeat to ship Windows Event Logs to HELK Kafka broker (10.0.21.29:9092) as a Windows service", (168, 85, 247)),
        ("Task 5: Rejetto HFS Exploitation", "Attacking demo2.ine.local:80 with Metasploit rejetto_hfs_exec to obtain Meterpreter shell & getsystem", (239, 68, 68)),
        ("Task 6: Maintaining Persistence", "Executing Meterpreter 'run persistence' creating auto-starting VBS backdoor in %TEMP%", (236, 72, 153)),
        ("Task 7: Mimikatz Credential Dumping", "Running privilege::debug and sekurlsa::logonPasswords to dump plaintext credentials and NTLM hashes from LSASS", (239, 68, 68)),
        ("Task 8: Kibana SOC Threat Hunting", "Triage in Kibana Sysmon Dashboards & Discover (correlating hfs.exe, wscript.exe, .vbs dropper, and mimikatz.exe)", (56, 189, 248)),
    ]

    sy = 416
    for title, desc, col in steps:
        draw.ellipse([(60, sy + 3), (72, sy + 15)], fill=col)
        draw.text((82, sy), title, fill=col, font=font_subtitle)
        draw.text((380, sy + 2), "— " + desc, fill=(203, 213, 225), font=font_small)
        sy += 36

    out_path = os.path.join(IMAGES_DIR, "threat_detection_elk_banner.jpg")
    img.save(out_path, quality=95)
    print(f"Saved hero banner to {out_path}")

def generate_workflow_map():
    print("Generating Workflow Architecture Map...")
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 44, (18, 28, 48))

    draw.rounded_rectangle([(40, 24), (w - 40, 68)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 36), "THREAT DETECTION WITH ELASTICSEARCH & KIBANA • FULL RED-TO-BLUE ARCHITECTURE", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 280, 36), "8-STAGE LAB BLUEPRINT", fill=(16, 185, 129), font=font_subtitle)

    boxes = [
        {"title": "TASK 1: HELK SOC Machine", "cmd": "cd /opt/HELK/docker && ./helk_install.sh", "detail": "Ubuntu 20.04 (10.0.21.29) running Kafka 9092, ES, Kibana", "col": (56, 189, 248), "x": 40, "y": 88, "w": 400, "h": 128},
        {"title": "TASK 2: Windows Detailed Auditing", "cmd": "gpedit.msc & profile.ps1", "detail": "Process Creation + CmdLine, ScriptBlock, Task Scheduler Log", "col": (245, 158, 11), "x": 480, "y": 88, "w": 400, "h": 128},
        {"title": "TASK 3: Sysmon Deployment", "cmd": "Sysmon.exe -i sysmonconfig-export.xml", "detail": "SwiftOnSecurity high-quality kernel & network monitoring", "col": (16, 185, 129), "x": 920, "y": 88, "w": 416, "h": 128},

        {"title": "TASK 4: Winlogbeat Shipper", "cmd": "winlogbeat.yml -> 10.0.21.29:9092", "detail": "Kafka broker ingestion pipeline with auto-starting service", "col": (168, 85, 247), "x": 40, "y": 236, "w": 400, "h": 128},
        {"title": "TASK 5: Metasploit HFS RCE", "cmd": "exploit/windows/http/rejetto_hfs_exec", "detail": "Port 80 RCE -> Meterpreter shell -> getsystem (SYSTEM)", "col": (239, 68, 68), "x": 480, "y": 236, "w": 400, "h": 128},
        {"title": "TASK 6: Persistence Mechanism", "cmd": "run persistence (Meterpreter)", "detail": "Drops .vbs backdoor in %TEMP% and registers Run key", "col": (236, 72, 153), "x": 920, "y": 236, "w": 416, "h": 128},

        {"title": "TASK 7: Mimikatz LSASS Dump", "cmd": "privilege::debug; sekurlsa::logonPasswords", "detail": "Harvests NTLM hashes from Local Security Authority (LSASS)", "col": (239, 68, 68), "x": 40, "y": 384, "w": 400, "h": 128},
        {"title": "TASK 8A: Sysmon Dashboards", "cmd": "Sysmon & Sysmon Network Dashboards", "detail": "Correlates process executions, unknown binaries, SHA256 hashes", "col": (56, 189, 248), "x": 480, "y": 384, "w": 400, "h": 128},
        {"title": "TASK 8B: Discover Triage", "cmd": "Query 'hfs.exe' AND 'wscript.exe'", "detail": "Tracks tlqjxleo.vbs, douwxodqwof.vbs, and Mimikatz execution", "col": (16, 185, 129), "x": 920, "y": 384, "w": 416, "h": 128},

        {"title": "SOC VERIFICATION & MITRE MAPPING", "cmd": "T1190 (RCE), T1059.005 (VBS), T1547.001 (Run Key), T1003.001 (LSASS Memory), T1046 (Nmap)", "detail": "Full cyber kill chain observed, correlated, and alerted in Kibana 7.x SIEM Dashboard", "col": (56, 189, 248), "x": 40, "y": 532, "w": 1296, "h": 136},
    ]

    for b in boxes:
        draw.rounded_rectangle([(b["x"], b["y"]), (b["x"] + b["w"], b["y"] + b["h"])], radius=8, fill=(15, 23, 42), outline=b["col"], width=2)
        draw.text((b["x"] + 14, b["y"] + 10), b["title"], fill=b["col"], font=font_subtitle)
        draw.text((b["x"] + 14, b["y"] + 34), "Action: " + b["cmd"][:44], fill=(148, 163, 184), font=font_mono_small)
        
        bw = int(draw.textlength(b["detail"][:40], font=font_small)) + 16
        draw.rounded_rectangle([(b["x"] + 14, b["y"] + 58), (min(b["x"] + b["w"] - 14, b["x"] + 14 + bw), b["y"] + 82)], radius=4, fill=(19, 29, 49), outline=b["col"], width=1)
        draw.text((b["x"] + 22, b["y"] + 63), b["detail"][:40], fill=(248, 250, 252), font=font_small)

        draw.text((b["x"] + 14, b["y"] + 96), b["detail"], fill=(203, 213, 225), font=font_small)

    out_path = os.path.join(IMAGES_DIR, "threat_detection_elk_workflow_map.jpg")
    img.save(out_path, quality=95)
    print(f"Saved workflow map to {out_path}")

def generate_live_demo_gif():
    print("Generating Animated Live Demo GIF...")
    w, h = 920, 520
    frames = []

    steps = [
        ("Task 1: Starting HELK Hunting Stack", "cd /opt/HELK/docker && ./helk_install.sh", "HELK Stack Online", "Kibana up at https://localhost (helk / hunting)"),
        ("Task 2: Detailed Windows Auditing", "gpedit.msc & Audit Process Creation", "Command Line Auditing Enabled", "PowerShell ScriptBlock logging & Task Scheduler Operational log"),
        ("Task 3: Sysmon Deployment", "Sysmon.exe -i sysmonconfig-export.xml", "Sysmon Service Running", "SwiftOnSecurity config monitoring process, network, and registry"),
        ("Task 4: Winlogbeat Shipper", "hosts: ['10.0.21.29:9092']", "Kafka Shipper Active", "Winlogbeat streaming security and sysmon telemetry to HELK"),
        ("Task 5: Rejetto HFS Exploit", "msf > use exploit/windows/http/rejetto_hfs_exec", "Meterpreter Session 1 Opened", "Gained remote code execution & elevated to NT AUTHORITY\\SYSTEM"),
        ("Task 6: Maintaining Persistence", "meterpreter > run persistence", "VBS Script & Run Key Planted", "Backdoor deployed: douwxodqwof.vbs in Temp directory"),
        ("Task 7: Mimikatz LSASS Dump", "mimikatz # sekurlsa::logonPasswords", "NTLM Hashes Harvested", "Local Security Authority Subsystem Service memory dumped"),
        ("Task 8A: Kibana Sysmon Dashboard", "Sysmon Dashboard (HELK)", "116 Process Events Visualized", "Correlated wmiadap.exe, SHA256 hashes, and execution spikes"),
        ("Task 8B: Sysmon Network Dashboard", "Sysmon Network Dashboard (HELK)", "Outbound Connections Flagged", "38 socket events mapped to attacker Kali machine"),
        ("Task 8C: Kibana Discover Triage", "KQL: 'hfs.exe' AND 'wscript.exe'", "Attack Footprint Confirmed", "Detected hfs.exe spawning wscript.exe //B //NOLOGO tlqjxleo.vbs"),
        ("Task 8D: Persistence & Mimikatz Detection", "KQL: '.vbs' | KQL: 'mimikatz'", "T1547 & T1003 Confirmed", "Identified douwxodqwof.vbs backdoor and Mimikatz process logs"),
    ]

    for title, cmd, status, sub in steps:
        frame = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(frame)

        # Chrome Header
        draw.rectangle([(0, 0), (w, 42)], fill=(30, 41, 59))
        draw.ellipse([(14, 15), (24, 25)], fill=(239, 68, 68))
        draw.ellipse([(32, 15), (42, 25)], fill=(245, 158, 11))
        draw.ellipse([(50, 15), (60, 25)], fill=(16, 185, 129))
        draw.text((76, 12), "HELK / Kibana SIEM — Red-to-Blue Threat Hunting Console", fill=(203, 213, 225), font=font_subtitle)

        # Command / Filter Box
        draw.rounded_rectangle([(20, 56), (w - 20, 100)], radius=6, fill=(11, 17, 32), outline=(56, 189, 248), width=2)
        draw.text((34, 68), "EXEC: " + cmd, fill=(56, 189, 248), font=font_mono_bold)

        # Main Box
        draw.rounded_rectangle([(20, 116), (w - 20, 460)], radius=8, fill=(11, 17, 32), outline=(30, 41, 59), width=1)
        draw.text((40, 136), title, fill=(248, 250, 252), font=font_large)

        # Status badge
        draw.rounded_rectangle([(40, 180), (w - 40, 270)], radius=6, fill=(19, 29, 49), outline=(16, 185, 129), width=2)
        draw.text((60, 196), "TELEMETRY & ATTACK STATE:", fill=(148, 163, 184), font=font_small)
        draw.text((60, 218), status, fill=(16, 185, 129), font=font_large)

        draw.text((40, 290), "FORENSIC EVIDENCE & CORRELATION:", fill=(148, 163, 184), font=font_small)
        draw.text((40, 316), sub, fill=(203, 213, 225), font=font_body)

        draw.rounded_rectangle([(40, 360), (w - 40, 440)], radius=4, fill=(15, 23, 42))
        draw.text((54, 372), f"Command / Query: {cmd}", fill=(148, 163, 184), font=font_mono_small)
        draw.text((54, 400), "HELK Pipeline: Winlogbeat -> Kafka 9092 -> Elasticsearch -> Kibana 7.x", fill=(56, 189, 248), font=font_mono_small)

        draw.text((20, 480), "INE Hands-on Lab: Threat Detection with Elasticsearch and Kibana — 100% Solved", fill=(100, 116, 139), font=font_small)
        draw.text((w - 220, 480), "Live Demo Simulation", fill=(245, 158, 11), font=font_small)

        frames.append(frame)

    out_path = os.path.join(IMAGES_DIR, "threat_detection_elk_live_demo.gif")
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=1400, loop=0)
    print(f"Saved live demo GIF to {out_path}")

def generate_task_images():
    print("Generating Task Summary Visual Cards...")
    tasks = [
        ("Task1", "HELK Stack Initialization", "cd /opt/HELK/docker && ./helk_install.sh", "Kibana up at https://localhost:5601 (helk/hunting)"),
        ("Task2", "Windows Detailed Auditing (gpedit.msc)", "Audit Process Creation with CommandLine Arguments", "PowerShell ScriptBlock logging & Task Scheduler Operational"),
        ("Task3", "Sysmon Kernel Telemetry Service", "Sysmon.exe -accepteula -i sysmonconfig-export.xml", "SwiftOnSecurity high-fidelity process & socket monitoring"),
        ("Task4", "Winlogbeat Kafka Log Shipper", "hosts: ['10.0.21.29:9092']", "Shipping Windows Event Logs directly to HELK Kafka broker"),
        ("Task5", "Rejetto HFS 2.3 Remote Exploitation", "use exploit/windows/http/rejetto_hfs_exec", "Meterpreter session established & elevated to SYSTEM"),
        ("Task6", "Meterpreter Persistence Backdoor", "run persistence", "VBS dropper (douwxodqwof.vbs) planted with registry autorun"),
        ("Task7", "Mimikatz LSASS Credential Harvesting", "privilege::debug; sekurlsa::logonPasswords", "NTLM password hashes extracted from LSASS memory"),
        ("Task8", "Kibana SOC Incident Triage & Correlation", "Query 'hfs.exe' AND 'wscript.exe'", "Correlated initial exploit, persistence, and Mimikatz dump"),
    ]

    for tid, title, cmd, detail in tasks:
        w, h = 640, 220
        img = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle([(10, 10), (w - 10, h - 10)], radius=8, fill=(11, 17, 32), outline=(56, 189, 248), width=2)

        draw.text((26, 24), f"THREAT DETECTION WITH ELASTICSEARCH & KIBANA • {tid.upper()}", fill=(56, 189, 248), font=font_subtitle)
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
    print("All Threat Detection ELK visual media assets completed successfully!")
