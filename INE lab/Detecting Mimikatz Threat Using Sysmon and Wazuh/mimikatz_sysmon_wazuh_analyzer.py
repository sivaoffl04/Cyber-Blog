#!/usr/bin/env python3
"""
Mimikatz Threat Detection & Sysmon-Wazuh Telemetry Analyzer
===========================================================
Companion forensic & detection engineering script for the INE Security Lab:
"Detecting Mimikatz Threat Using Sysmon and Wazuh"
Lab URL: https://my.ine.com/labs/7a7d418e-9b1b-4154-9145-60b16ee6a128

Capabilities:
1. Validates the Sysmon XML configuration (Schema 4.10: Event IDs 1, 8, 10)
2. Validates Wazuh custom detection rules (Rules 100000, 100001, 100002)
3. Decodes Windows ProcessAccess GrantedAccess bitmasks (e.g., 0x1010 on lsass.exe)
4. Parses Sysmon Event ID 10 CallTrace stack frames from Mimikatz LSASS access
5. Generates a structured JSON forensic triage report & animated walkthrough GIF
"""

import argparse
import json
import os
import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple

# Windows Process Access Rights Bitmask Definitions
PROCESS_ACCESS_FLAGS: Dict[int, Tuple[str, str]] = {
    0x0001: ("PROCESS_TERMINATE", "Required to terminate a process using TerminateProcess."),
    0x0002: ("PROCESS_CREATE_THREAD", "Required to create a thread in the process (used in remote thread injection)."),
    0x0008: ("PROCESS_VM_OPERATION", "Required to perform an operation on the address space of a process."),
    0x0010: ("PROCESS_VM_READ", "Required to read memory in a process using ReadProcessMemory (core Mimikatz sekurlsa requirement)."),
    0x0020: ("PROCESS_VM_WRITE", "Required to write to memory in a process using WriteProcessMemory."),
    0x0040: ("PROCESS_DUP_HANDLE", "Required to duplicate a handle using DuplicateHandle."),
    0x0400: ("PROCESS_QUERY_INFORMATION", "Required to retrieve certain information about a process (token, exit code, priority)."),
    0x0800: ("PROCESS_SUSPEND_RESUME", "Required to suspend or resume a process."),
    0x1000: ("PROCESS_QUERY_LIMITED_INFORMATION", "Required to retrieve subset of process information (used by Mimikatz alongside PROCESS_VM_READ)."),
}

SYSMON_CONFIG_XML = """<Sysmon schemaversion="4.10">
  <HashAlgorithms>md5</HashAlgorithms>
  <EventFiltering>
    <!--SYSMON EVENT ID 1 : PROCESS CREATION-->
    <ProcessCreate onmatch="include">
      <Image condition="contains">mimikatz.exe</Image>
    </ProcessCreate>
    <!--SYSMON EVENT ID 2 : FILE CREATION TIME RETROACTIVELY CHANGED IN THE FILESYSTEM-->
    <FileCreateTime onmatch="include" />
    <!--SYSMON EVENT ID 3 : NETWORK CONNECTION INITIATED-->
    <NetworkConnect onmatch="include" />
    <!--SYSMON EVENT ID 4 : RESERVED FOR SYSMON STATUS MESSAGES, THIS LINE IS INCLUDED FOR DOCUMENTATION PURPOSES ONLY-->
    <!--SYSMON EVENT ID 5 : PROCESS ENDED-->
    <ProcessTerminate onmatch="include" />
    <!--SYSMON EVENT ID 6 : DRIVER LOADED INTO KERNEL-->
    <DriverLoad onmatch="include" />
    <!--SYSMON EVENT ID 7 : DLL (IMAGE) LOADED BY PROCESS-->
    <ImageLoad onmatch="include" />
    <!--SYSMON EVENT ID 8 : REMOTE THREAD CREATED-->
    <CreateRemoteThread onmatch="include">
      <SourceImage condition="contains">mimikatz.exe</SourceImage>
    </CreateRemoteThread>
    <!--SYSMON EVENT ID 9 : RAW DISK ACCESS-->
    <RawAccessRead onmatch="include" />
    <!--SYSMON EVENT ID 10 : INTER-PROCESS ACCESS-->
    <ProcessAccess onmatch="include">
      <SourceImage condition="contains">mimikatz.exe</SourceImage>
    </ProcessAccess>
    <!--SYSMON EVENT ID 11 : FILE CREATED-->
    <FileCreate onmatch="include" />
    <!--SYSMON EVENT ID 12 & 13 & 14 : REGISTRY MODIFICATION-->
    <RegistryEvent onmatch="include" />
    <!--SYSMON EVENT ID 15 : ALTERNATE DATA STREAM CREATED-->
    <FileCreateStreamHash onmatch="include" />
    <PipeEvent onmatch="include" />
  </EventFiltering>
</Sysmon>"""

WAZUH_LOCAL_RULES_XML = """<group name="windows, sysmon, sysmon_process-anomalies,">
  <rule id="100000" level="12">
    <if_group>sysmon_event1</if_group>
    <field name="win.eventdata.image">mimikatz.exe</field>
    <description>Sysmon - Suspicious Process - mimikatz.exe</description>
  </rule>
  <rule id="100001" level="12">
    <if_group>sysmon_event8</if_group>
    <field name="win.eventdata.sourceImage">mimikatz.exe</field>
    <description>Sysmon - Suspicious Process mimikatz.exe created a remote thread</description>
  </rule>
  <rule id="100002" level="12">
    <if_group>sysmon_event_10</if_group>
    <field name="win.eventdata.sourceImage">mimikatz.exe</field>
    <description>Sysmon - Suspicious Process mimikatz.exe accessed $(win.eventdata.targetImage)</description>
  </rule>
</group>"""

LAB_ALERTS = [
    {
        "@timestamp": "2023-03-22T18:46:02.250Z",
        "_id": "eVekCocBy09XixQCg0Jc",
        "agent": {
            "id": "001",
            "name": "AttackDefense",
            "ip": "10.0.25.100"
        },
        "rule": {
            "id": "100000",
            "level": 12,
            "description": "Sysmon - Suspicious Process - mimikatz.exe",
            "groups": ["windows", "sysmon", "sysmon_process-anomalies"],
            "mitre": {
                "id": ["T1003", "T1003.001"],
                "tactic": ["Credential Access"],
                "technique": ["OS Credential Dumping: LSASS Memory"]
            }
        },
        "data": {
            "win": {
                "system": {
                    "eventID": "1",
                    "channel": "Microsoft-Windows-Sysmon/Operational"
                },
                "eventdata": {
                    "image": "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe",
                    "commandLine": "\\\"C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe\\\"",
                    "currentDirectory": "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\",
                    "company": "gentilkiwi (Benjamin DELPY)",
                    "description": "mimikatz for Windows",
                    "fileVersion": "2.2.0.0"
                }
            }
        }
    },
    {
        "@timestamp": "2023-03-22T18:46:29.977Z",
        "_id": "eIekCocBy09XixQC5UIR",
        "agent": {
            "id": "001",
            "name": "AttackDefense",
            "ip": "10.0.25.100"
        },
        "rule": {
            "id": "100002",
            "level": 12,
            "description": "Sysmon - Suspicious Process mimikatz.exe accessed C:\\\\Windows\\\\system32\\\\lsass.exe",
            "groups": ["windows", "sysmon", "sysmon_process-anomalies"],
            "mitre": {
                "id": ["T1003.001"],
                "tactic": ["Credential Access"],
                "technique": ["OS Credential Dumping: LSASS Memory"]
            }
        },
        "data": {
            "win": {
                "system": {
                    "eventID": "10",
                    "channel": "Microsoft-Windows-Sysmon/Operational"
                },
                "eventdata": {
                    "sourceImage": "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe",
                    "targetImage": "C:\\\\Windows\\\\system32\\\\lsass.exe",
                    "grantedAccess": "0x1010",
                    "callTrace": (
                        "C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+9fc24|"
                        "C:\\\\Windows\\\\System32\\\\KERNELBASE.dll+2126e|"
                        "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe+c291e|"
                        "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe+c2cf5|"
                        "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe+c285d|"
                        "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe+85a44|"
                        "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe+8587c|"
                        "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe+85647|"
                        "C:\\\\Users\\\\Administrator\\\\Desktop\\\\Investigation\\\\Mimikatz\\\\mimikatz_trunk\\\\x64\\\\mimikatz.exe+c97a5|"
                        "C:\\\\Windows\\\\System32\\\\KERNEL32.DLL+17974|"
                        "C:\\\\Windows\\\\SYSTEM32\\\\ntdll.dll+6a271"
                    )
                }
            }
        }
    }
]


def decode_granted_access(hex_mask: str) -> List[Dict[str, str]]:
    """Decodes a Windows ProcessAccess GrantedAccess hexadecimal bitmask."""
    mask_int = int(hex_mask, 16)
    decoded = []
    for bit, (name, desc) in PROCESS_ACCESS_FLAGS.items():
        if mask_int & bit:
            decoded.append({
                "hex": f"0x{bit:04x}",
                "flag": name,
                "description": desc
            })
    return decoded


def parse_call_trace(call_trace: str) -> List[Dict[str, str]]:
    """Splits a Sysmon Event ID 10 CallTrace string into ordered stack frames."""
    frames = []
    for idx, raw_frame in enumerate(call_trace.split("|"), start=1):
        clean_frame = raw_frame.replace("\\\\", "\\")
        if "+" in clean_frame:
            module_path, offset = clean_frame.rsplit("+", 1)
        else:
            module_path, offset = clean_frame, "0x0"
        frames.append({
            "frame": idx,
            "module": module_path,
            "offset": f"+0x{offset}",
            "role": (
                "Windows Native API Syscall (NtOpenProcess)" if idx == 1 else
                "Win32 KernelBase Wrapper (OpenProcess)" if "KERNELBASE" in module_path.upper() else
                "Mimikatz Sekurlsa LSASS Memory Reader" if "mimikatz.exe" in module_path.lower() else
                "Process Thread Entry Wrapper"
            )
        })
    return frames


def validate_xml_configs() -> Dict[str, object]:
    """Validates both the Sysmon XML schema and Wazuh custom rule XML."""
    sysmon_root = ET.fromstring(SYSMON_CONFIG_XML)
    wazuh_root = ET.fromstring(WAZUH_LOCAL_RULES_XML)

    rules = []
    for r in wazuh_root.findall("rule"):
        rules.append({
            "id": r.attrib.get("id"),
            "level": int(r.attrib.get("level", "0")),
            "if_group": r.findtext("if_group"),
            "field_name": r.find("field").attrib.get("name") if r.find("field") is not None else "",
            "field_value": r.findtext("field"),
            "description": r.findtext("description")
        })

    return {
        "sysmon_schema_version": sysmon_root.attrib.get("schemaversion"),
        "sysmon_hash_algorithms": sysmon_root.findtext("HashAlgorithms"),
        "wazuh_rule_group": wazuh_root.attrib.get("name"),
        "wazuh_rules": rules
    }


def generate_gif(base_dir: str) -> str:
    """Generates the animated walkthrough GIF inside images/mimikatz_wazuh_live_demo.gif."""
    from PIL import Image, ImageDraw, ImageFont

    image_dir = os.path.join(base_dir, "image")
    images_dir = os.path.join(base_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    W, H = 1080, 660
    font_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 16)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)

    slides = [
        ("TASK 1: WAZUH SERVER IP DISCOVERY (10.0.31.41)", "SOC Machine (Ubuntu 20.04) -> ip addr | Identifying Wazuh Manager Address", "6.png", (14, 165, 233), "SOC Machine IP: 10.0.31.41/20 (ens5)"),
        ("TASK 1: AGENT ENROLLMENT & SERVICE START", "Target Machine (Windows Server 2019) -> ossec.conf & Start-Service -Name WazuhSvc", "9.png", (34, 197, 94), "Active Agent 001: AttackDefense (10.0.25.100) Connected"),
        ("TASK 2: WAZUH AGENT SYSMON EVENTCHANNEL CONFIG", "C:\\Program Files (x86)\\ossec-agent\\ossec.conf -> Microsoft-Windows-Sysmon/Operational", "10.png", (56, 189, 248), "<log_format>eventchannel</log_format>"),
        ("TASK 2: SYSMON SCHEMA 4.10 CONFIGURATION LOAD", "Monitoring ProcessCreate (EID 1), CreateRemoteThread (EID 8), ProcessAccess (EID 10)", "12.png", (168, 85, 247), ".\\Sysmon64.exe -c ..\\sysconfig.xml -> Validated & Updated"),
        ("TASK 3: WAZUH CUSTOM DETECTION RULES (100000-100002)", "/var/ossec/etc/rules/local_rules.xml -> Level 12 High-Severity Alert Rules", "14.png", (245, 158, 11), "Rules 100000 (EID 1), 100001 (EID 8), 100002 (EID 10)"),
        ("TASK 4: LAUNCHING MIMIKATZ.EXE ON TARGET ENDPOINT", "PowerShell -> cd .\\Desktop\\Investigation\\Mimikatz\\mimikatz_trunk\\x64\\ ; .\\mimikatz.exe", "16.png", (239, 68, 68), "Triggers Sysmon Event ID 1 (ProcessCreate: mimikatz.exe)"),
        ("TASK 4: CREDENTIAL DUMPING (SEKURLSA::LOGONPASSWORDS)", "mimikatz # privilege::debug -> log -> sekurlsa::logonpasswords (LSASS Memory Read)", "17.png", (220, 38, 38), "SeDebugPrivilege (20) OK -> Accessing C:\\Windows\\system32\\lsass.exe"),
        ("TASK 5: WAZUH DASHBOARD LEVEL 12+ ALERT FILTERING", "Security Events -> Filtering Level 12 or above alerts (2 Critical Detections)", "20.png", (239, 68, 68), "Alert 100000 (ProcessCreate) & Alert 100002 (LSASS ProcessAccess)"),
        ("TASK 5: FORENSIC TELEMETRY — RULE 100002 (LSASS ACCESS)", "Source: mimikatz.exe -> Target: C:\\Windows\\system32\\lsass.exe | GrantedAccess: 0x1010", "22.png", (16, 185, 129), "MITRE ATT&CK T1003.001 (OS Credential Dumping: LSASS Memory)"),
    ]

    frames = []
    for idx, (title, subtitle, img_name, accent, footer_text) in enumerate(slides, 1):
        canvas = Image.new("RGB", (W, H), (11, 15, 25))
        draw = ImageDraw.Draw(canvas)
        draw.rectangle([0, 0, W, 76], fill=(17, 24, 39))
        draw.rectangle([0, 73, W, 76], fill=accent)
        draw.rounded_rectangle([18, 16, 118, 56], radius=8, fill=accent)
        draw.text((32, 24), f"STEP {idx}/9", font=font_bold, fill=(255, 255, 255))
        draw.text((134, 13), title, font=font_bold, fill=(248, 250, 252))
        draw.text((134, 43), subtitle, font=font_sub, fill=(148, 163, 184))

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
            cx = W - 220 + d * 22
            cy = H - 23
            col = accent if d == idx - 1 else (51, 65, 85)
            draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=col)

        frames.append(canvas.quantize(colors=256, method=Image.Quantize.MEDIANCUT))

    gif_path = os.path.join(images_dir, "mimikatz_wazuh_live_demo.gif")
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
    parser = argparse.ArgumentParser(description="Mimikatz Sysmon & Wazuh Detection Telemetry Analyzer")
    parser.add_argument("--generate-gif", action="store_true", help="Generate the animated walkthrough GIF")
    parser.add_argument("--json", action="store_true", help="Output full forensic report in JSON format")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    if args.generate_gif:
        gif_path = generate_gif(base_dir)
        print(f"[+] Generated animated GIF: {gif_path} ({os.path.getsize(gif_path):,} bytes)")

    validation = validate_xml_configs()
    access_flags = decode_granted_access("0x1010")
    call_trace = parse_call_trace(LAB_ALERTS[1]["data"]["win"]["eventdata"]["callTrace"])

    report = {
        "lab_name": "Detecting Mimikatz Threat Using Sysmon and Wazuh",
        "lab_url": "https://my.ine.com/labs/7a7d418e-9b1b-4154-9145-60b16ee6a128",
        "environment": {
            "wazuh_server_ip": "10.0.31.41",
            "wazuh_dashboard_url": "https://localhost",
            "target_agent_name": "AttackDefense",
            "target_agent_id": "001",
            "target_agent_ip": "10.0.25.100",
            "target_os": "Windows Server 2019 Datacenter Evaluation"
        },
        "configuration_validation": validation,
        "granted_access_0x1010_decoded": access_flags,
        "lsass_call_trace_analysis": call_trace,
        "alerts_captured": LAB_ALERTS
    }

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("=" * 78)
        print(" MIMIKATZ SYSMON & WAZUH TELEMETRY ANALYZER -- FORENSIC SUMMARY")
        print("=" * 78)
        print(f" [+] Wazuh Server IP   : {report['environment']['wazuh_server_ip']}")
        print(f" [+] Enrolled Agent    : {report['environment']['target_agent_name']} (ID: {report['environment']['target_agent_id']}, IP: {report['environment']['target_agent_ip']})")
        print(f" [+] Sysmon Schema     : v{validation['sysmon_schema_version']} (HashAlgorithms: {validation['sysmon_hash_algorithms']})")
        print("-" * 78)
        print(" [+] Custom Wazuh Detection Rules Validated:")
        for r in validation["wazuh_rules"]:
            print(f"     - Rule {r['id']} (Level {r['level']}): [{r['if_group']}] {r['description']}")
        print("-" * 78)
        print(" [+] Decoded LSASS ProcessAccess Mask (0x1010):")
        for flag in access_flags:
            print(f"     - {flag['hex']} ({flag['flag']}): {flag['description']}")
        print("-" * 78)
        print(" [+] Sysmon Event ID 10 CallTrace Stack (Top 4 Frames):")
        for frame in call_trace[:4]:
            print(f"     #{frame['frame']:02d} {frame['module']}{frame['offset']} -> {frame['role']}")
        print("=" * 78)


if __name__ == "__main__":
    main()
