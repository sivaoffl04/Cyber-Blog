#!/usr/bin/env python3
"""
Generate High-Quality Visual Media Assets for ELK: SSH Logs Lab Walkthrough
- elk_ssh_banner.jpg (1376x768)
- elk_ssh_workflow_map.jpg (1376x768)
- elk_ssh_live_demo.gif (920x520, 10 frames)
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
FLAG_DIR = os.path.join(IMAGES_DIR, "flag_images")
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(FLAG_DIR, exist_ok=True)

# Standard Windows Fonts
font_huge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 38)
font_large = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 16)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)
font_small = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)
font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)
font_mono_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 12)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)

def draw_grid_background(draw, width, height, grid_size=40, line_color=(20, 30, 55)):
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=line_color, width=1)
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=line_color, width=1)

def generate_hero_banner():
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32)) # #0B1120
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 48, (18, 28, 48))

    # Top header bar
    draw.rounded_rectangle([(40, 28), (w - 40, 72)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 40), "INE SECURITY LABS • ADVANCED THREAT HUNTING & FORENSICS", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 240, 40), "CHALLENGE CID: 1138", fill=(245, 158, 11), font=font_subtitle)

    # Title & Subtitle
    draw.text((40, 96), "ELK: SSH Log Analysis", fill=(248, 250, 252), font=font_huge)
    draw.text((40, 150), "Multi-Server Brute-Force Profiling, Credential Compromise & Breach Timeline Forensics", fill=(148, 163, 184), font=font_title)

    # Badge Pills
    badges = [
        ("100% SOLVED (10/10 FLAGS)", (16, 185, 129)),
        ("ELASTICSEARCH & KIBANA", (2, 132, 199)),
        ("OPENSSH TELEMETRY", (99, 102, 241)),
        ("BRUTE-FORCE & SPRAYING", (239, 68, 68)),
        ("TIMELION SPIKE ANALYSIS", (236, 72, 153)),
    ]
    cur_x = 40
    for text, color in badges:
        bw = int(draw.textlength(text, font=font_badge)) + 22
        draw.rounded_rectangle([(cur_x, 192), (cur_x + bw, 222)], radius=6, fill=color)
        draw.text((cur_x + 11, 199), text, fill=(255, 255, 255), font=font_badge)
        cur_x += bw + 14

    # Row 1: 4 Metric Cards
    cards_r1 = [
        {
            "accent": (6, 182, 212), # Cyan
            "label": "ATTACKING MACHINES",
            "val": "3 Adversary IPs",
            "desc": "192.148.107.6 (Max attempts), .7, .8",
            "sub": "High-rate SSH authentication failure events"
        },
        {
            "accent": (245, 158, 11), # Amber
            "label": "TARGETED SSH SERVERS",
            "val": "3 Servers Attacked",
            "desc": "192.148.107.4 (Most attacked), .5, .3",
            "sub": "Concentric multi-level attack share pie"
        },
        {
            "accent": (168, 85, 247), # Purple
            "label": "AUTHENTICATION MODES",
            "val": "2 Active Modes",
            "desc": "Password & Publickey Authentication",
            "sub": "Attacker 192.148.107.8 used unauthorized pubkey"
        },
        {
            "accent": (59, 130, 246), # Blue
            "label": "SERVICE CONFIGURATION",
            "val": "Port 3603",
            "desc": "Custom SSH daemon listening port",
            "sub": "Uniform non-standard service port on all hosts"
        }
    ]

    card_w = (w - 80 - 3 * 16) // 4
    for i, c in enumerate(cards_r1):
        cx = 40 + i * (card_w + 16)
        cy = 246
        ch = 220
        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + ch)], radius=10, fill=(15, 23, 42), outline=(30, 41, 59), width=1)
        # Accent bar
        draw.rounded_rectangle([(cx + 16, cy + 18), (cx + 56, cy + 22)], radius=2, fill=c["accent"])
        draw.text((cx + 16, cy + 34), c["label"], fill=(148, 163, 184), font=font_badge)
        draw.text((cx + 16, cy + 62), c["val"], fill=(255, 255, 255), font=font_title)
        draw.text((cx + 16, cy + 110), c["desc"], fill=c["accent"], font=font_body)
        draw.text((cx + 16, cy + 155), c["sub"], fill=(100, 116, 139), font=font_small)

    # Row 2: 2 Wide Metric Cards
    cards_r2 = [
        {
            "accent": (244, 63, 94), # Rose/Red
            "label": "COMPROMISED CREDENTIAL & FIRST BREACHED SERVER",
            "val": "User: administrator • First Breached: 192.148.107.3",
            "desc": "Accepted SSH status confirmed account compromise • Earliest breach traced to ssh-server-3",
            "sub": "Attacker gained full privileged interactive access • Earliest document chronologically isolated"
        },
        {
            "accent": (16, 185, 129), # Emerald
            "label": "PEAK TELEMETRY INGESTION SPIKE FORENSICS",
            "val": "16:17:58 (Timelion Peak Timestamp)",
            "desc": "Sub-minute interval zoom pinpointed maximum log push into Elasticsearch cluster",
            "sub": "Coincides with high-velocity automated brute-force spray burst across servers"
        }
    ]

    card2_w = (w - 80 - 16) // 2
    for i, c in enumerate(cards_r2):
        cx = 40 + i * (card2_w + 16)
        cy = 484
        ch = 250
        draw.rounded_rectangle([(cx, cy), (cx + card2_w, cy + ch)], radius=10, fill=(15, 23, 42), outline=c["accent"], width=1)
        draw.rounded_rectangle([(cx + 20, cy + 20), (cx + 60, cy + 24)], radius=2, fill=c["accent"])
        draw.text((cx + 20, cy + 36), c["label"], fill=c["accent"], font=font_badge)
        draw.text((cx + 20, cy + 68), c["val"], fill=(255, 255, 255), font=font_title)
        draw.text((cx + 20, cy + 124), c["desc"], fill=(226, 232, 240), font=font_body)
        draw.text((cx + 20, cy + 175), c["sub"], fill=(148, 163, 184), font=font_small)

    out_path = os.path.join(IMAGES_DIR, "elk_ssh_banner.jpg")
    img.save(out_path, "JPEG", quality=95)
    print(f"[+] Rendered Banner: {out_path}")

def generate_workflow_map():
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 48, (18, 28, 48))

    # Top header bar
    draw.rounded_rectangle([(40, 24), (w - 40, 78)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 34), "10-STAGE SSH TELEMETRY THREAT HUNTING & BREACH INVESTIGATION WORKFLOW", fill=(248, 250, 252), font=font_large)
    draw.text((60, 58), "Systematic Investigation Architecture: From Authentication Failure Profiling to First Breach Chronology", fill=(56, 189, 248), font=font_small)

    stages = [
        # Row 1 (Stages 1-5)
        {"stage": "STAGE 1: ATTACKERS", "title": "Attacker Cardinality", "filter": "sshd_conn_stat : \"auth failure\"", "desc": "Isolate failed login events", "flag": "Flag: 3 Hosts (.6-.8)", "accent": (6, 182, 212)},
        {"stage": "STAGE 2: MAX VOLUME", "title": "Aggressive Attacker", "filter": "Agg: Terms on client_ip", "desc": "Rank source IPs by login attempts", "flag": "Flag: 192.148.107.6", "accent": (245, 158, 11)},
        {"stage": "STAGE 3: TARGETS", "title": "Attacked SSH Servers", "filter": "Filter: sshd_listen_ip : *", "desc": "Audit listening daemon IPs", "flag": "Flag: 3 Servers (.3-.5)", "accent": (239, 68, 68)},
        {"stage": "STAGE 4: ATTACK SHARE", "title": "Concentric Pie Chart", "filter": "Split: listen_ip -> client_ip", "desc": "Two-level attack share breakdown", "flag": "Flag: Tgt .4 / Atk .6", "accent": (59, 130, 246)},
        {"stage": "STAGE 5: AUTH MODES", "title": "Authentication Types", "filter": "sshd_auth_type : * AND NOT none", "desc": "Profile attempted auth mechanisms", "flag": "Flag: 2 Modes (pwd, key)", "accent": (168, 85, 247)},
        # Row 2 (Stages 6-10)
        {"stage": "STAGE 6: PUBKEY ATTACK", "title": "Public Key Attribution", "filter": "sshd_auth_type : \"publickey\"", "desc": "Isolate key-based break-in", "flag": "Flag: IP 192.148.107.8", "accent": (244, 63, 94)},
        {"stage": "STAGE 7: PORT AUDIT", "title": "SSH Service Port", "filter": "Filter: sshd_listen_port : *", "desc": "Verify listening daemon port", "flag": "Flag: Port 3603", "accent": (16, 185, 129)},
        {"stage": "STAGE 8: BREACH USER", "title": "Compromised Account", "filter": "sshd_conn_stat : \"Accepted\"", "desc": "Inspect accepted login user", "flag": "Flag: administrator", "accent": (234, 179, 8)},
        {"stage": "STAGE 9: SPIKE TIME", "title": "Timelion Ingestion Peak", "filter": "Timelion: .es(index=ssh-log*)", "desc": "Zoom into peak volume point", "flag": "Flag: Time 16:17:58", "accent": (236, 72, 153)},
        {"stage": "STAGE 10: FIRST BREACH", "title": "Earliest Compromise", "filter": "Sort: Time Asc -> host.name", "desc": "Resolve first compromised server IP", "flag": "Flag: IP 192.148.107.3", "accent": (20, 184, 166)}
    ]

    card_w = (w - 80 - 4 * 14) // 5
    card_h = 280

    # Draw connection lines between cards
    # Row 1 connectors
    cy1 = 100 + card_h // 2
    draw.line([(40 + card_w, cy1), (w - 40 - card_w, cy1)], fill=(51, 65, 85), width=2)
    # Turn around connector
    draw.line([(w - 40 - card_w // 2, cy1), (w - 40 - card_w // 2, 430 + card_h // 2)], fill=(59, 130, 246), width=2)
    # Row 2 connectors
    cy2 = 430 + card_h // 2
    draw.line([(40 + card_w // 2, cy2), (w - 40 - card_w // 2, cy2)], fill=(51, 65, 85), width=2)

    for idx, s in enumerate(stages):
        row = idx // 5
        col = idx % 5
        cx = 40 + col * (card_w + 14)
        cy = 100 if row == 0 else 430

        # Card container
        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)], radius=10, fill=(15, 23, 42), outline=(30, 41, 59), width=1)

        # Stage Pill
        pw = int(draw.textlength(s["stage"], font=font_badge)) + 16
        draw.rounded_rectangle([(cx + 12, cy + 14), (cx + 12 + pw, cy + 34)], radius=4, fill=(30, 41, 59))
        draw.text((cx + 20, cy + 18), s["stage"], fill=s["accent"], font=font_badge)

        # Title
        draw.text((cx + 14, cy + 46), s["title"], fill=(248, 250, 252), font=font_title)

        # Filter box
        draw.rounded_rectangle([(cx + 12, cy + 82), (cx + card_w - 12, cy + 122)], radius=6, fill=(11, 17, 32), outline=(30, 41, 59), width=1)
        draw.text((cx + 18, cy + 94), s["filter"], fill=(56, 189, 248), font=font_mono_small)

        # Description
        draw.text((cx + 14, cy + 138), s["desc"], fill=(148, 163, 184), font=font_small)

        # Flag Box
        draw.rounded_rectangle([(cx + 12, cy + card_h - 66), (cx + card_w - 12, cy + card_h - 14)], radius=6, fill=(11, 17, 32), outline=s["accent"], width=1)
        draw.text((cx + 18, cy + card_h - 50), s["flag"], fill=(255, 255, 255), font=font_mono_bold)

    out_path = os.path.join(IMAGES_DIR, "elk_ssh_workflow_map.jpg")
    img.save(out_path, "JPEG", quality=95)
    print(f"[+] Rendered Workflow Map: {out_path}")

def generate_live_demo_gif():
    gw, gh = 920, 520
    frames = []

    steps_data = [
        {
            "step": "STEP 1 / 10: ATTACKER DISCOVERY",
            "filter": "SEARCH / FILTER: sshd_conn_stat : \"authentication failure\" | Index: ssh-log*",
            "flag_img": "Flag1.png",
            "status": "Attacking Machines: 3 Attacking IPs (192.148.107.6, 7, 8) [FLAG CAPTURED]",
            "accent": (6, 182, 212)
        },
        {
            "step": "STEP 2 / 10: LOGIN ATTEMPT VOLUME",
            "filter": "VISUALIZATION: Vertical Bar | X-Axis: Terms on sshd_client_ip.keyword",
            "flag_img": "Flag2.png",
            "status": "Top Login Attempt Machine: 192.148.107.6 (~1,300 attempts) [FLAG CAPTURED]",
            "accent": (245, 158, 11)
        },
        {
            "step": "STEP 3 / 10: TARGET SERVERS AUDIT",
            "filter": "SEARCH / FILTER: sshd_listen_ip : * | Target Daemons Exposure Analysis",
            "flag_img": "Flag3.png",
            "status": "Attacked SSH Servers: 3 Servers (192.148.107.3, .4, .5) [FLAG CAPTURED]",
            "accent": (239, 68, 68)
        },
        {
            "step": "STEP 4 / 10: CROSS-SERVER ATTACK SHARE",
            "filter": "VISUALIZATION: Two-Level Nested Pie Chart | Split: listen_ip -> client_ip",
            "flag_img": "Flag4.png",
            "status": "Most Attacked Server: 192.148.107.4 | Top Attacker: 192.148.107.6 [FLAG CAPTURED]",
            "accent": (59, 130, 246)
        },
        {
            "step": "STEP 5 / 10: AUTHENTICATION MODES",
            "filter": "SEARCH / FILTER: sshd_auth_type : * AND NOT sshd_auth_type : none",
            "flag_img": "Flag5.png",
            "status": "Authentication Modes Used: 2 (password, publickey) [FLAG CAPTURED]",
            "accent": (168, 85, 247)
        },
        {
            "step": "STEP 6 / 10: PUBLIC KEY ATTACK ATTRIBUTION",
            "filter": "SEARCH / FILTER: sshd_auth_type : \"publickey\" | Attacker Key Audit",
            "flag_img": "Flag6.png",
            "status": "Public Key Attacker IP: 192.148.107.8 [FLAG CAPTURED]",
            "accent": (244, 63, 94)
        },
        {
            "step": "STEP 7 / 10: SSH SERVICE PORT VERIFICATION",
            "filter": "SEARCH / FILTER: sshd_listen_port : * | Daemon Configuration Audit",
            "flag_img": "Flag7.png",
            "status": "SSH Service Daemon Port: 3603 (Non-standard port) [FLAG CAPTURED]",
            "accent": (16, 185, 129)
        },
        {
            "step": "STEP 8 / 10: COMPROMISED IDENTITY TRIAGE",
            "filter": "SEARCH / FILTER: sshd_conn_stat : \"Accepted\" | Accepted Sessions",
            "flag_img": "Flag8.png",
            "status": "Compromised User Account: administrator [FLAG CAPTURED]",
            "accent": (234, 179, 8)
        },
        {
            "step": "STEP 9 / 10: TIMELION PEAK SPIKE PINPOINTING",
            "filter": "VISUALIZATION: Timelion | .es(index=ssh-log*) | High-Resolution Temporal Zoom",
            "flag_img": "Flag9.png",
            "status": "Peak Telemetry Ingestion Timestamp: 16:17:58 [FLAG CAPTURED]",
            "accent": (236, 72, 153)
        },
        {
            "step": "STEP 10 / 10: FIRST BREACHED SERVER ISOLATION",
            "filter": "CHRONOLOGY: Earliest Accepted Log -> host.name : \"ssh-server-3\" -> listen_ip",
            "flag_img": "Flag10.png",
            "status": "First Compromised SSH Server IP: 192.148.107.3 [FLAG CAPTURED]",
            "accent": (20, 184, 166)
        }
    ]

    for s in steps_data:
        fimg = Image.new("RGB", (gw, gh), color=(11, 17, 32))
        fdraw = ImageDraw.Draw(fimg)
        draw_grid_background(fdraw, gw, gh, 40, (18, 28, 48))

        # macOS window bar
        fdraw.rectangle([(0, 0), (gw, 38)], fill=(15, 23, 42))
        fdraw.line([(0, 38), (gw, 38)], fill=(30, 41, 59), width=1)
        fdraw.ellipse([(14, 13), (24, 23)], fill=(239, 68, 68))
        fdraw.ellipse([(32, 13), (42, 23)], fill=(245, 158, 11))
        fdraw.ellipse([(50, 13), (60, 23)], fill=(16, 185, 129))
        fdraw.text((74, 11), "Kibana SIEM Threat Hunting Console — [SSH Telemetry Forensics CID 1138]", fill=(203, 213, 225), font=font_mono_small)

        # Step badge & filter bar
        pw = int(fdraw.textlength(s["step"], font=font_badge)) + 16
        fdraw.rounded_rectangle([(24, 48), (24 + pw, 70)], radius=4, fill=(30, 41, 59))
        fdraw.text((32, 52), s["step"], fill=s["accent"], font=font_badge)

        # Filter bar
        fdraw.rounded_rectangle([(24, 78), (gw - 24, 110)], radius=6, fill=(15, 23, 42), outline=(30, 41, 59), width=1)
        fdraw.text((34, 88), s["filter"], fill=(56, 189, 248), font=font_mono_small)

        # Center evidence display area (max w=872, max h=330)
        flag_path = os.path.join(FLAG_DIR, s["flag_img"])
        if os.path.exists(flag_path):
            src_im = Image.open(flag_path).convert("RGB")
            # Calculate resize keeping aspect ratio
            max_w, max_h = gw - 48, 326
            scale = min(max_w / src_im.width, max_h / src_im.height)
            rw = int(src_im.width * scale)
            rh = int(src_im.height * scale)
            resized_im = src_im.resize((rw, rh), Image.Resampling.LANCZOS)

            # Center position
            px = (gw - rw) // 2
            py = 120 + (max_h - rh) // 2
            # Outer frame
            fdraw.rounded_rectangle([(px - 2, py - 2), (px + rw + 2, py + rh + 2)], radius=6, fill=(15, 23, 42), outline=s["accent"], width=1)
            fimg.paste(resized_im, (px, py))

        # Bottom status pill
        fdraw.rounded_rectangle([(24, gh - 56), (gw - 24, gh - 16)], radius=6, fill=(15, 23, 42), outline=s["accent"], width=1)
        fdraw.text((36, gh - 46), s["status"], fill=(255, 255, 255), font=font_mono_bold)

        frames.append(fimg)

    out_gif = os.path.join(IMAGES_DIR, "elk_ssh_live_demo.gif")
    frames[0].save(
        out_gif,
        save_all=True,
        append_images=frames[1:],
        duration=2500,
        loop=0,
        optimize=True
    )
    print(f"[+] Rendered Animated Live Demo GIF: {out_gif} ({len(frames)} frames)")

def main():
    print("[*] Generating ELK SSH Logs media assets...")
    generate_hero_banner()
    generate_workflow_map()
    generate_live_demo_gif()
    print("[+] All media assets generated successfully.")

if __name__ == "__main__":
    main()
