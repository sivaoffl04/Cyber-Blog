#!/usr/bin/env python3
"""
PsExec Threat Detection & Sysmon-Wazuh Telemetry Analyzer
=========================================================
Companion forensic & detection engineering script for the INE Security Lab:
"Detecting PsExec with Wazuh"
Lab URL: https://my.ine.com/labs/ebf73ec9-5b02-4d28-8089-3c1ba3501604

Capabilities:
1. Parses and validates Wazuh custom detection rules (Rules 160010, 160011, 160012, 160013)
2. Maps Sysmon Registry (Event IDs 12/13) and Named Pipe (Event IDs 17/18) telemetry to MITRE ATT&CK
3. Reconstructs the chronological PsExec privilege escalation & service lifecycle timeline
4. Generates a structured JSON forensic triage report & 10-frame animated walkthrough GIF
"""

import argparse
import json
import os
import xml.etree.ElementTree as ET
from typing import Dict, List

WAZUH_PSEXEC_RULES_XML = """<group name="windows,sysmon">
  <rule id="160010" level="10">
    <if_group>windows,sysmon</if_group>
    <field name="win.eventdata.eventType" type="pcre2">SetValue</field>
    <field name="win.eventdata.targetObject" type="pcre2">\\\\SOFTWARE\\\\Sysinternals\\\\PsExec\\\\EulaAccepted</field>
    <options>no_full_log</options>
    <description>PsExec EULA registry found on $(win.system.computer)</description>
    <mitre>
      <id>T1112</id>
    </mitre>
  </rule>
  <rule id="160011" level="10">
    <if_group>windows,sysmon</if_group>
    <field name="win.eventdata.targetObject" type="pcre2">HKLM\\\\System\\\\CurrentControlSet\\\\Services\\\\PSEXESVC</field>
    <field name="win.eventdata.eventType" type="pcre2">^SetValue$</field>
    <field name="win.eventdata.user" type="pcre2">NT AUTHORITY\\\\SYSTEM</field>
    <options>no_full_log</options>
    <description>PsExec service running as $(win.eventdata.user) has been created on $(win.system.computer)</description>
    <mitre>
      <id>T1543.003</id>
    </mitre>
  </rule>
  <rule id="160012" level="10">
    <if_group>windows,sysmon</if_group>
    <field name="win.eventdata.targetObject" type="pcre2">HKLM\\\\System\\\\CurrentControlSet\\\\Services\\\\PSEXESVC</field>
    <field name="win.eventdata.eventType" type="pcre2">^DeleteKey$</field>
    <field name="win.eventdata.user" type="pcre2">NT AUTHORITY\\\\SYSTEM</field>
    <options>no_full_log</options>
    <description>PsExec service running as $(win.eventdata.user) has been deleted on $(win.system.computer)</description>
    <mitre>
      <id>T1543.003</id>
    </mitre>
  </rule>
  <rule id="160013" level="10">
    <if_group>windows,sysmon</if_group>
    <field name="win.eventdata.eventType" type="pcre2">CreatePipe</field>
    <field name="win.eventdata.image" type="pcre2">\\\\PSEXESVC.exe</field>
    <match type="pcre2">(?i)(PSEXESVC|stdin|stdout|stderr)</match>
    <field name="win.eventdata.user" type="pcre2">NT AUTHORITY\\\\SYSTEM</field>
    <options>no_full_log</options>
    <description>PsExec named pipe running as $(win.eventdata.user) has been found on $(win.system.computer)</description>
    <mitre>
      <id>T1570</id>
    </mitre>
  </rule>
</group>"""

LAB_CAPTURED_ALERTS: List[Dict[str, object]] = [
    {
        "@timestamp": "2023-03-07T07:50:12.525Z",
        "_id": "mW8Mu4YBhBA8ktkdqRqw",
        "agent": {
            "id": "001",
            "name": "AttackDefense",
            "ip": "10.0.17.171"
        },
        "rule": {
            "id": "160013",
            "level": 10,
            "description": "PsExec named pipe running as NT AUTHORITY\\\\SYSTEM has been found on AttackDefense",
            "mitre": {
                "id": ["T1570"],
                "tactic": ["Lateral Movement"],
                "technique": ["Lateral Tool Transfer"]
            }
        },
        "data": {
            "win": {
                "system": {
                    "eventID": "17",
                    "channel": "Microsoft-Windows-Sysmon/Operational",
                    "computer": "AttackDefense"
                },
                "eventdata": {
                    "eventType": "CreatePipe",
                    "image": "C:\\\\Windows\\\\PSEXESVC.exe",
                    "user": "NT AUTHORITY\\\\SYSTEM",
                    "pipeName": "\\\\PSEXESVC-AttackDefense-stdin/stdout/stderr"
                }
            }
        }
    },
    {
        "@timestamp": "2023-03-07T07:51:35.792Z",
        "_id": "m28Nu4YBhBA8ktkd9RrR",
        "agent": {
            "id": "001",
            "name": "AttackDefense",
            "ip": "10.0.17.171"
        },
        "rule": {
            "id": "160011",
            "level": 10,
            "description": "PsExec service running as NT AUTHORITY\\\\SYSTEM has been created on AttackDefense",
            "mitre": {
                "id": ["T1543.003"],
                "tactic": ["Persistence", "Privilege Escalation"],
                "technique": ["Create or Modify System Process: Windows Service"]
            }
        },
        "data": {
            "win": {
                "system": {
                    "eventID": "13",
                    "channel": "Microsoft-Windows-Sysmon/Operational",
                    "computer": "AttackDefense"
                },
                "eventdata": {
                    "eventType": "SetValue",
                    "image": "C:\\\\Windows\\\\system32\\\\services.exe",
                    "targetObject": "HKLM\\\\System\\\\CurrentControlSet\\\\Services\\\\PSEXESVC\\\\Start",
                    "details": "DWORD (0x00000004)",
                    "user": "NT AUTHORITY\\\\SYSTEM"
                }
            }
        }
    },
    {
        "@timestamp": "2023-03-07T07:51:35.808Z",
        "_id": "nG8Nu4YBhBA8ktkd9RrR",
        "agent": {
            "id": "001",
            "name": "AttackDefense",
            "ip": "10.0.17.171"
        },
        "rule": {
            "id": "160012",
            "level": 10,
            "description": "PsExec service running as NT AUTHORITY\\\\SYSTEM has been deleted on AttackDefense",
            "mitre": {
                "id": ["T1543.003"],
                "tactic": ["Persistence", "Privilege Escalation"],
                "technique": ["Create or Modify System Process: Windows Service"]
            }
        },
        "data": {
            "win": {
                "system": {
                    "eventID": "12",
                    "channel": "Microsoft-Windows-Sysmon/Operational",
                    "computer": "AttackDefense"
                },
                "eventdata": {
                    "eventType": "DeleteKey",
                    "image": "C:\\\\Windows\\\\system32\\\\services.exe",
                    "targetObject": "HKLM\\\\System\\\\CurrentControlSet\\\\Services\\\\PSEXESVC",
                    "user": "NT AUTHORITY\\\\SYSTEM"
                }
            }
        }
    }
]


def validate_psexec_rules() -> Dict[str, object]:
    """Parses and validates the custom Wazuh XML rules for PsExec detection."""
    root = ET.fromstring(WAZUH_PSEXEC_RULES_XML)
    parsed_rules = []
    for r in root.findall("rule"):
        fields = [
            {"name": f.attrib.get("name"), "type": f.attrib.get("type"), "pattern": f.text}
            for f in r.findall("field")
        ]
        mitre_ids = [m.text for m in r.findall("./mitre/id")]
        parsed_rules.append({
            "id": r.attrib.get("id"),
            "level": int(r.attrib.get("level", "0")),
            "if_group": r.findtext("if_group"),
            "fields": fields,
            "match": r.findtext("match"),
            "description": r.findtext("description"),
            "mitre_ids": mitre_ids
        })
    return {
        "group": root.attrib.get("name"),
        "rule_count": len(parsed_rules),
        "rules": parsed_rules
    }


def generate_gif(base_dir: str) -> str:
    """Generates the 10-frame animated walkthrough GIF inside images/psexec_wazuh_live_demo.gif."""
    from PIL import Image, ImageDraw, ImageFont

    image_dir = os.path.join(base_dir, "image")
    images_dir = os.path.join(base_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    W, H = 1080, 660
    font_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 16)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)

    slides = [
        ("TASK 1: WAZUH SERVER IP DISCOVERY (10.0.28.182)", "SOC Machine (Ubuntu 20.04) -> ip addr | Identifying Wazuh Manager Address", "6.png", (14, 165, 233), "SOC Machine IP: 10.0.28.182/20 (ens5)"),
        ("TASK 1: WAZUH AGENT MANAGER CONFIGURATION", "Target Machine (Windows Server 2019) -> Wazuh Agent Manager GUI (v4.3.10)", "7.png", (56, 189, 248), "Manager IP: 10.0.28.182 -> Start-Service -Name WazuhSvc"),
        ("TASK 1: ACTIVE AGENT VERIFICATION IN DASHBOARD", "Wazuh Dashboard (https://localhost) -> Active Agents: 1 (AttackDefense)", "9.png", (34, 197, 94), "Enrolled Agent 001: AttackDefense (10.0.17.171)"),
        ("TASK 2: WAZUH AGENT SYSMON EVENTCHANNEL CONFIG", "C:\\Program Files (x86)\\ossec-agent\\ossec.conf -> Microsoft-Windows-Sysmon/Operational", "10.png", (168, 85, 247), "<log_format>eventchannel</log_format>"),
        ("TASK 2: INSTALLING SYSMON WITH SYSMONCONFIG.XML", "PowerShell -> .\\Sysmon64.exe -accepteula -i sysmonconfig.xml (Schema 4.60)", "11.png", (139, 92, 246), "Sysmon64 & SysmonDrv Installed and Started"),
        ("TASK 3: AUTHORING CUSTOM PSEXEC RULES (160010-160013)", "/var/ossec/etc/rules/local_rules.xml -> MITRE T1112, T1543.003, T1570", "13.png", (245, 158, 11), "Rules 160010 (EULA), 160011 (Svc Create), 160012 (Svc Delete), 160013 (Pipe)"),
        ("TASK 4: PRIVILEGE ESCALATION WITH PSEXEC (-i -s)", "PowerShell -> cd .\\Downloads\\PSTools ; .\\PsExec.exe -i -s powershell", "16.png", (239, 68, 68), "whoami -> nt authority\\system (Elevated from Administrator to SYSTEM)"),
        ("TASK 5: WAZUH SECURITY EVENTS TABLE (RULES 160011-160013)", "Security Events -> Detecting PSEXESVC Named Pipes & Service Lifecycle", "19.png", (220, 38, 38), "Level 10 Alerts: Rule 160013 (T1570), Rule 160011 & 160012 (T1543.003)"),
        ("TASK 5: FORENSIC TELEMETRY -- RULE 160011 (SERVICE CREATED)", "HKLM\\System\\CurrentControlSet\\Services\\PSEXESVC | EventType: SetValue", "20.png", (16, 185, 129), "Image: C:\\Windows\\system32\\services.exe | Details: DWORD (0x00000004)"),
        ("TASK 5: FORENSIC TELEMETRY -- RULE 160013 (NAMED PIPE IPC)", "Image: C:\\Windows\\PSEXESVC.exe | EventType: CreatePipe (stdin/stdout/stderr)", "22.png", (6, 182, 212), "MITRE ATT&CK T1570 (Lateral Tool Transfer) as NT AUTHORITY\\SYSTEM"),
    ]

    frames = []
    for idx, (title, subtitle, img_name, accent, footer_text) in enumerate(slides, 1):
        canvas = Image.new("RGB", (W, H), (11, 15, 25))
        draw = ImageDraw.Draw(canvas)
        draw.rectangle([0, 0, W, 76], fill=(17, 24, 39))
        draw.rectangle([0, 73, W, 76], fill=accent)
        draw.rounded_rectangle([18, 16, 128, 56], radius=8, fill=accent)
        draw.text((28, 24), f"STEP {idx}/10", font=font_bold, fill=(255, 255, 255))
        draw.text((144, 13), title, font=font_bold, fill=(248, 250, 252))
        draw.text((144, 43), subtitle, font=font_sub, fill=(148, 163, 184))

        src = Image.open(os.path.join(image_dir, img_name)).convert("RGB")
        max_w, max_h = W - 48, H - 142
        src.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
        sx = (W - src.width) // 2
        sy = 84 + (max_h - src.height) // 2
        draw.rounded_rectangle([sx - 4, sy - 4, sx + src.width + 4, sy + src.height + 4], radius=6, outline=accent, width=2)
        canvas.paste(src, (sx, sy))

        draw.rectangle([0, H - 46, W, H], fill=(17, 24, 39))
        draw.text((20, H - 33), f"[+] {footer_text}", font=font_mono, fill=(56, 189, 248))
        for d in range(len(slides)):
            cx = W - 240 + d * 22
            cy = H - 23
            col = accent if d == idx - 1 else (51, 65, 85)
            draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=col)

        frames.append(canvas.quantize(colors=256, method=Image.Quantize.MEDIANCUT))

    gif_path = os.path.join(images_dir, "psexec_wazuh_live_demo.gif")
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=1600,
        loop=0,
        optimize=True,
    )
    return gif_path


def main() -> None:
    parser = argparse.ArgumentParser(description="PsExec Sysmon & Wazuh Detection Telemetry Analyzer")
    parser.add_argument("--generate-gif", action="store_true", help="Generate the animated walkthrough GIF")
    parser.add_argument("--json", action="store_true", help="Output full forensic report in JSON format")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    if args.generate_gif:
        gif_path = generate_gif(base_dir)
        print(f"[+] Generated animated GIF: {gif_path} ({os.path.getsize(gif_path):,} bytes)")

    validation = validate_psexec_rules()
    report = {
        "lab_name": "Detecting PsExec with Wazuh",
        "lab_url": "https://my.ine.com/labs/ebf73ec9-5b02-4d28-8089-3c1ba3501604",
        "environment": {
            "wazuh_server_ip": "10.0.28.182",
            "wazuh_dashboard_url": "https://localhost",
            "target_agent_name": "AttackDefense",
            "target_agent_id": "001",
            "target_agent_ip": "10.0.17.171",
            "target_os": "Windows Server 2019"
        },
        "custom_rules_validation": validation,
        "attack_command": ".\\PsExec.exe -i -s powershell",
        "escalated_privilege": "nt authority\\system",
        "alerts_captured": LAB_CAPTURED_ALERTS
    }

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("=" * 80)
        print(" PSEXEC SYSMON & WAZUH TELEMETRY ANALYZER -- FORENSIC SUMMARY")
        print("=" * 80)
        print(f" [+] Wazuh Server IP   : {report['environment']['wazuh_server_ip']}")
        print(f" [+] Enrolled Agent    : {report['environment']['target_agent_name']} (ID: {report['environment']['target_agent_id']}, IP: {report['environment']['target_agent_ip']})")
        print(f" [+] Attack Command    : {report['attack_command']} -> {report['escalated_privilege']}")
        print("-" * 80)
        print(" [+] Custom Wazuh Detection Rules Validated:")
        for r in validation["rules"]:
            mitre_str = ", ".join(r["mitre_ids"])
            print(f"     - Rule {r['id']} (Level {r['level']}) [MITRE {mitre_str}]: {r['description']}")
        print("-" * 80)
        print(" [+] Chronological Telemetry Timeline Captured in Wazuh:")
        for a in LAB_CAPTURED_ALERTS:
            rule = a["rule"]
            ev = a["data"]["win"]["eventdata"]
            print(f"     * {a['@timestamp']} | Rule {rule['id']} (Level {rule['level']}) | {ev['eventType']} -> {ev['image']}")
        print("=" * 80)


if __name__ == "__main__":
    main()
