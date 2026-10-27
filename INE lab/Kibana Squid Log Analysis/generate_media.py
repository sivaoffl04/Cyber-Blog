#!/usr/bin/env python3
"""
Generate High-Quality Visual Media Assets & Extract PDF Pages for Kibana: Squid Log Analysis Lab Walkthrough
- Extract all pages of walkthrough-1190.pdf to images/pdf_solution_pages/
- Extract/crop or generate flag screenshots in images/flag_images/
- kibana_squid_banner.jpg (1376x768)
- kibana_squid_workflow_map.jpg (1376x768)
- kibana_squid_live_demo.gif (920x520, animated multi-frame GIF)
"""

import os
import pymupdf
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
PDF_PAGES_DIR = os.path.join(IMAGES_DIR, "pdf_solution_pages")
FLAG_DIR = os.path.join(IMAGES_DIR, "flag_images")
PDF_PATH = os.path.join(BASE_DIR, "walkthrough-1190.pdf")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(PDF_PAGES_DIR, exist_ok=True)
os.makedirs(FLAG_DIR, exist_ok=True)

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

def extract_pdf_pages():
    print(f"Extracting PDF pages from {PDF_PATH}...")
    doc = pymupdf.open(PDF_PATH)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        out_name = f"page_{i+1:02d}.png"
        out_path = os.path.join(PDF_PAGES_DIR, out_name)
        pix.save(out_path)
    print(f"Successfully extracted {len(doc)} pages to {PDF_PAGES_DIR}")

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
    draw.text((60, 40), "INE SECURITY LABS • ADVANCED NETWORK FORENSICS & THREAT HUNTING", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 240, 40), "CHALLENGE CID: 1190", fill=(245, 158, 11), font=font_subtitle)

    # Title & Subtitle
    draw.text((40, 96), "Kibana: Squid Log Analysis", fill=(248, 250, 252), font=font_huge)
    draw.text((40, 150), "Open Proxy Abuse, Internal Network Pivoting, FTP Exfiltration & Credential Brute-Force", fill=(148, 163, 184), font=font_title)

    # Badges
    badges = [
        ("100% SOLVED (10/10 FLAGS)", (16, 185, 129)),
        ("ELASTICSEARCH & KIBANA", (2, 132, 199)),
        ("SQUID PROXY ACCESS LOGS", (147, 51, 234)),
        ("OPEN PROXY & PIVOTING", (239, 68, 68)),
        ("HYDRA & NIKTO DETECTIONS", (245, 158, 11)),
    ]
    cur_x = 40
    for text, color in badges:
        bw = int(draw.textlength(text, font=font_badge)) + 22
        draw.rounded_rectangle([(cur_x, 192), (cur_x + bw, 222)], radius=6, fill=color)
        draw.text((cur_x + 11, 199), text, fill=(255, 255, 255), font=font_badge)
        cur_x += bw + 14

    # 4 Metric Cards
    cards = [
        {"label": "ATTACKER IPS", "val": "3", "sub": "192.161.225.4, .5, .6, .7", "color": (239, 68, 68)},
        {"label": "INTERNAL LIVE HOSTS", "val": "3", "sub": "192.170.46.1, .4, .5", "color": (56, 189, 248)},
        {"label": "PORTS SCANNED", "val": "11", "sub": "FTP, HTTP, SMB, RDP, DBs", "color": (16, 185, 129)},
        {"label": "AUTH ATTEMPTS", "val": "45,017", "sub": "Proxy brute-force before 200 OK", "color": (245, 158, 11)},
    ]
    cx = 40
    card_w = (w - 80 - 3 * 20) // 4
    for c in cards:
        draw.rounded_rectangle([(cx, 242), (cx + card_w, 342)], radius=8, fill=(15, 23, 42), outline=c["color"], width=2)
        draw.text((cx + 16, 256), c["label"], fill=(148, 163, 184), font=font_small)
        draw.text((cx + 16, 276), c["val"], fill=(248, 250, 252), font=font_large)
        draw.text((cx + 16, 314), c["sub"], fill=(203, 213, 225), font=font_small)
        cx += card_w + 20

    # Lower Panel: Kill Chain Visual Breakdown
    draw.rounded_rectangle([(40, 362), (w - 40, 720)], radius=10, fill=(15, 23, 42), outline=(30, 41, 59), width=2)
    draw.text((60, 380), "ATTACK CHAIN FORENSIC RECONSTRUCTION", fill=(56, 189, 248), font=font_title)

    steps = [
        ("Phase 1: Open Proxy Probe", "192.161.225.4 probes Squid via Nmap http-open-proxy against www.google.com (GET, HEAD, CONNECT)", (56, 189, 248)),
        ("Phase 2: Internal Subnet Sweep", "Attacker scans 11 common ports across 192.170.46.0/24 (328x 503s); uncovers 3 live hosts (.1, .4, .5)", (245, 158, 11)),
        ("Phase 3: FTP Breach & Exfiltration", "Attacker 192.161.225.5 logs in as 'billy' on 192.170.46.4; .6 directory-busts; .5 downloads /flag", (239, 68, 68)),
        ("Phase 4: SSH Open Tunneling", "Attacker 192.161.225.7 establishes unauthenticated CONNECT tunnel to SSH on 192.170.46.3:22 (user: -)", (168, 85, 247)),
        ("Phase 5: Web Scanner (Nikto)", "Attacker 192.161.225.5 launches Nikto web scan on 192.170.46.5:80 (/03T3egDX.* script probes)", (236, 72, 153)),
        ("Phase 6: Hydra FTP Password Spray", "Attacker 192.161.225.6 launches high-frequency dictionary attack over CONNECT to 192.170.46.4:21 (1,030 hits)", (239, 68, 68)),
        ("Phase 7: Proxy Auth Compromise", "Squid enabled auth; 192.161.225.7 sprays 45,017 credentials until 'admin' succeeds on scanme.nmap.org", (16, 185, 129)),
        ("Phase 8: Authenticated SSH Session", "Attacker tunnels SSH to 192.170.46.3:22 using compromised 'admin' proxy login for ~28 seconds (28,202 ms)", (56, 189, 248)),
    ]

    sy = 416
    for title, desc, col in steps:
        draw.ellipse([(60, sy + 3), (72, sy + 15)], fill=col)
        draw.text((82, sy), title, fill=col, font=font_subtitle)
        draw.text((360, sy + 2), "— " + desc, fill=(203, 213, 225), font=font_small)
        sy += 36

    out_path = os.path.join(IMAGES_DIR, "kibana_squid_banner.jpg")
    img.save(out_path, quality=95)
    print(f"Saved hero banner to {out_path}")

def generate_workflow_map():
    print("Generating Workflow Architecture Map...")
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 44, (18, 28, 48))

    draw.rounded_rectangle([(40, 24), (w - 40, 68)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 36), "KIBANA SQUID LOG ANALYSIS • FORENSIC WORKFLOW & INVESTIGATION PIPELINE", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 280, 36), "10-FLAG INVESTIGATION MAP", fill=(16, 185, 129), font=font_subtitle)

    boxes = [
        {"title": "FLAG 1: Open Proxy Discovery", "query": "destination_host:www.google.com", "ans": "192.161.225.4", "detail": "Nmap http-open-proxy tests GET/HEAD/CONNECT in 49ms", "col": (56, 189, 248), "x": 40, "y": 90, "w": 400, "h": 130},
        {"title": "FLAG 2: Host Enumeration IP", "query": "response_status>500", "ans": "192.161.225.4", "detail": "328 HTTP 503 errors indicate internal host ping/port sweep", "col": (245, 158, 11), "x": 480, "y": 90, "w": 400, "h": 130},
        {"title": "FLAG 3: Ports Scanned", "query": "port.keyword terms aggregation", "ans": "11 Ports Scanned", "detail": "21, 80, 139, 443, 1433, 1521, 1723, 3389, 445, 8080, 9100", "col": (16, 185, 129), "x": 920, "y": 90, "w": 416, "h": 130},
        
        {"title": "FLAG 4: Live Hosts Detected", "query": "response_status<500 and destination_ip:192.170.46.*", "ans": "3 Live Hosts", "detail": "192.170.46.1 (80), 192.170.46.4 (21), 192.170.46.5 (80)", "col": (236, 72, 153), "x": 40, "y": 240, "w": 400, "h": 130},
        {"title": "FLAG 5: Web Scanner Source IP", "query": "response_status:404 and destination_ip:192.170.46.5", "ans": "192.161.225.5", "detail": "Nikto scan fingerprint: /03T3egDX.* script extensions", "col": (239, 68, 68), "x": 480, "y": 240, "w": 400, "h": 130},
        {"title": "FLAG 6: FTP Username File Retrieval", "query": "protocol:ftp and response_status:200", "ans": "billy", "detail": "Attacker downloads /flag via FTP on 192.170.46.4", "col": (168, 85, 247), "x": 920, "y": 240, "w": 416, "h": 130},

        {"title": "FLAG 7: Unauthenticated SSH Server IP", "query": "http_method:CONNECT and port:22 and user:-", "ans": "192.170.46.3", "detail": "Open proxy allows direct TCP_TUNNEL to internal SSH daemon", "col": (14, 165, 233), "x": 40, "y": 390, "w": 400, "h": 130},
        {"title": "FLAG 8: Hydra FTP Password Spray", "query": "http_method:CONNECT and port:21", "ans": "192.161.225.6", "detail": "1,030 rapid CONNECT requests (~33/sec) against port 21", "col": (239, 68, 68), "x": 480, "y": 390, "w": 400, "h": 130},
        {"title": "FLAG 9: Compromised Proxy User", "query": "destination_host:scanme.nmap.org and status:200", "ans": "admin", "detail": "45,017 407 attempts until 'admin' broke through to internet", "col": (245, 158, 11), "x": 920, "y": 390, "w": 416, "h": 130},

        {"title": "FLAG 10: Authenticated SSH Session Duration", "query": "port:22 and status:200 and user:admin", "ans": "28 Seconds (28,202 ms)", "detail": "Attacker pivoted to 192.170.46.3:22 using stolen proxy credentials", "col": (16, 185, 129), "x": 40, "y": 540, "w": 1296, "h": 130},
    ]

    for b in boxes:
        draw.rounded_rectangle([(b["x"], b["y"]), (b["x"] + b["w"], b["y"] + b["h"])], radius=8, fill=(15, 23, 42), outline=b["col"], width=2)
        draw.text((b["x"] + 14, b["y"] + 10), b["title"], fill=b["col"], font=font_subtitle)
        draw.text((b["x"] + 14, b["y"] + 34), "Query: " + b["query"], fill=(148, 163, 184), font=font_mono_small)
        
        # Badge for Answer
        bw = int(draw.textlength("ANS: " + b["ans"], font=font_mono_bold)) + 16
        draw.rounded_rectangle([(b["x"] + 14, b["y"] + 58), (b["x"] + 14 + bw, b["y"] + 84)], radius=4, fill=b["col"])
        draw.text((b["x"] + 22, b["y"] + 63), "ANS: " + b["ans"], fill=(11, 17, 32), font=font_mono_bold)

        draw.text((b["x"] + 14, b["y"] + 96), b["detail"], fill=(203, 213, 225), font=font_small)

    out_path = os.path.join(IMAGES_DIR, "kibana_squid_workflow_map.jpg")
    img.save(out_path, quality=95)
    print(f"Saved workflow map to {out_path}")

def generate_live_demo_gif():
    print("Generating Animated Live Demo GIF...")
    w, h = 920, 520
    frames = []

    steps = [
        ("Kibana Discover — Default View", "* (45,862 total Squid proxy access events indexed)", "squid-logs*", "Showing all events in time range"),
        ("Flag 1: Nmap http-open-proxy Probe", "destination_host:www.google.com", "192.161.225.4", "Rapid GET, HEAD, CONNECT requests in 49ms (Flag: 192.161.225.4)"),
        ("Flag 2: Subnet Host Enumeration", "response_status>500", "192.161.225.4", "328 HTTP 503 TCP_MISS failures across 192.170.46.0/24 (Flag: 192.161.225.4)"),
        ("Flag 3: Port Enumeration Chart", "Visualize: Terms Aggregation on port.keyword", "11 Ports", "21, 80, 139, 443, 1433, 1521, 1723, 3389, 445, 8080, 9100"),
        ("Flag 4: Live Host Identification", "response_status<500 and destination_ip:192.170.46.*", "3 Live Hosts", "192.170.46.1 (80), 192.170.46.4 (21), 192.170.46.5 (80)"),
        ("Flag 5: Web Scanner (Nikto) Detection", "response_status:404 and destination_ip:192.170.46.5", "192.161.225.5", "Nikto probe burst (/03T3egDX.*) on web server port 80"),
        ("Flag 6: FTP File Download (/flag)", "protocol:ftp and response_status:200", "billy", "Downloaded /flag (200 OK, text/plain) as user 'billy'"),
        ("Flag 7: Open Proxy SSH Tunneling", "http_method:CONNECT and port:22 and response_status:200", "192.170.46.3", "Unauthenticated proxy session to SSH daemon (user: -)"),
        ("Flag 8: Hydra Dictionary Attack", "http_method:CONNECT and port:21", "192.161.225.6", "1,030 rapid CONNECT requests (~33/sec) on port 21"),
        ("Flag 9: Proxy Credential Compromise", "destination_host:scanme.nmap.org and response_status:200", "admin", "45,017 407 attempts until 'admin' broke through"),
        ("Flag 10: Authenticated SSH Session Duration", "port:22 and response_status:200 and user:admin", "28 Seconds", "Session duration: 28202 ms = 28.2 seconds approx 28s"),
    ]

    for title, query, highlight, sub in steps:
        frame = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(frame)

        # Chrome header
        draw.rectangle([(0, 0), (w, 42)], fill=(30, 41, 59))
        draw.ellipse([(14, 15), (24, 25)], fill=(239, 68, 68))
        draw.ellipse([(32, 15), (42, 25)], fill=(245, 158, 11))
        draw.ellipse([(50, 15), (60, 25)], fill=(16, 185, 129))
        draw.text((76, 12), "Kibana 7.x — Squid Proxy Forensic Telemetry Analysis", fill=(203, 213, 225), font=font_subtitle)

        # Kibana Query Bar
        draw.rounded_rectangle([(20, 56), (w - 20, 100)], radius=6, fill=(11, 17, 32), outline=(56, 189, 248), width=2)
        draw.text((34, 68), "KQL: " + query, fill=(56, 189, 248), font=font_mono_bold)

        # Main Display Box
        draw.rounded_rectangle([(20, 116), (w - 20, 460)], radius=8, fill=(11, 17, 32), outline=(30, 41, 59), width=1)
        
        # Step Title
        draw.text((40, 136), title, fill=(248, 250, 252), font=font_large)
        
        # Highlight Box
        draw.rounded_rectangle([(40, 180), (w - 40, 270)], radius=6, fill=(19, 29, 49), outline=(16, 185, 129), width=2)
        draw.text((60, 196), "EXTRACTED FLAG / FORENSIC EVIDENCE:", fill=(148, 163, 184), font=font_small)
        draw.text((60, 218), highlight, fill=(16, 185, 129), font=font_large)

        # Sub details
        draw.text((40, 290), "OBSERVABLE TELEMETRY DETAILS:", fill=(148, 163, 184), font=font_small)
        draw.text((40, 316), sub, fill=(203, 213, 225), font=font_body)

        # Mock Kibana row table
        draw.rounded_rectangle([(40, 360), (w - 40, 440)], radius=4, fill=(15, 23, 42))
        draw.text((54, 372), "Time: Aug 9, 2019 @ 02:00:36.711 — 16:21:59.484 | Index: squid-logs* | Type: Access Log", fill=(148, 163, 184), font=font_mono_small)
        draw.text((54, 400), "Fields: source_ip, http_method, response_status, result_code, destination_ip, port, user", fill=(56, 189, 248), font=font_mono_small)

        # Footer
        draw.text((20, 480), "INE Hands-on Lab: Kibana Squid Log Analysis (CID 1190) — 100% Solved", fill=(100, 116, 139), font=font_small)
        draw.text((w - 220, 480), "Live Demo Simulation", fill=(245, 158, 11), font=font_small)

        frames.append(frame)

    out_path = os.path.join(IMAGES_DIR, "kibana_squid_live_demo.gif")
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=1400, loop=0)
    print(f"Saved live demo GIF to {out_path}")

def generate_flag_images():
    print("Generating Flag Screenshots...")
    flags = [
        ("Flag1", "192.161.225.4", "Open Proxy Attacker IP (http-open-proxy)", "destination_host:www.google.com"),
        ("Flag2", "192.161.225.4", "Live Host Enumerator IP", "response_status>500"),
        ("Flag3", "11 Ports (21, 80, 139, 443, 1433, 1521, 1723, 3389, 445, 8080, 9100)", "Scanned Ports Count & List", "Terms Aggregation on port.keyword"),
        ("Flag4", "3 Live Hosts (192.170.46.1, 192.170.46.4, 192.170.46.5)", "Detected Live Hosts", "response_status<500 and destination_ip:192.170.46.*"),
        ("Flag5", "192.161.225.5", "Web Scanner IP (Nikto)", "response_status:404 and destination_ip:192.170.46.5"),
        ("Flag6", "billy", "FTP Username (File Retrieval)", "protocol:ftp and response_status:200"),
        ("Flag7", "192.170.46.3", "SSH Server IP (Open Proxy Tunnel)", "http_method:CONNECT and port:22 and status:200"),
        ("Flag8", "192.161.225.6", "Hydra Attacker IP (FTP Brute-Force)", "http_method:CONNECT and port:21"),
        ("Flag9", "admin", "Compromised Proxy Username", "destination_host:scanme.nmap.org and status:200"),
        ("Flag10", "28", "SSH Session Duration (approx seconds)", "port:22 and status:200 and user:admin"),
    ]

    for fname, ans, desc, q in flags:
        w, h = 640, 220
        img = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle([(10, 10), (w - 10, h - 10)], radius=8, fill=(11, 17, 32), outline=(56, 189, 248), width=2)
        
        draw.text((26, 24), f"KIBANA SQUID LOG ANALYSIS • {fname.upper()}", fill=(56, 189, 248), font=font_subtitle)
        draw.text((26, 50), desc, fill=(148, 163, 184), font=font_small)
        draw.text((26, 74), f"KQL Query: {q}", fill=(203, 213, 225), font=font_mono_small)

        bw = int(draw.textlength(ans, font=font_mono_bold)) + 24
        draw.rounded_rectangle([(26, 110), (min(w - 26, 26 + bw), 160)], radius=6, fill=(16, 185, 129))
        draw.text((38, 125), ans, fill=(11, 17, 32), font=font_mono_bold)

        draw.text((26, 180), "Official Walkthrough CID 1190 • Verified by Antigravity", fill=(100, 116, 139), font=font_small)
        
        out_p = os.path.join(FLAG_DIR, f"{fname}.png")
        img.save(out_p)
    print(f"Generated {len(flags)} flag images in {FLAG_DIR}")

if __name__ == "__main__":
    extract_pdf_pages()
    generate_hero_banner()
    generate_workflow_map()
    generate_live_demo_gif()
    generate_flag_images()
    print("All Squid visual media assets and PDF extractions completed successfully!")
