# 🛡️ Security Operations Center (SOC) Architecture & Incident Response

Welcome to the **Security Operations Center (SOC)** knowledge base. This section provides enterprise-grade architectures, frameworks, and playbooks designed for SOC analysts, incident responders, detection engineers, and blue teamers.

---

<div align="center">

![Modern SOC Detection and Response Operations](./images/soc_workflow_banner.jpg)

</div>

---

## 📑 SOC Knowledge Base Index

| Guide Title | Core Focus | Technologies & Standards | Level | Direct Link |
| :--- | :--- | :--- | :---: | :---: |
| **Modern SOC Detection & Response Workflow** | End-to-end alert lifecycle, threat hunting, telemetry aggregation, and automated containment playbooks. | **EDR** (CrowdStrike Falcon), **SIEM** (Splunk), **SOAR** (Cortex XSOAR), **YARA** | Intermediate | [Read Guide](./EDR_SIEM_SOAR_YARA/README.md) |
| **NIST SP 800-61 Incident Response Playbook** | Comprehensive incident handling guide aligned with NIST CSF 2.0, state machines, severity matrices, and post-mortem procedures. | **NIST SP 800-61 Rev. 3**, **NIST CSF 2.0**, Containment Strategies, Eradication | Intermediate | [Read Guide](./NIST%20800-61/README.md) |

---

## 🔍 Module Summaries

### 1. [EDR, SIEM, SOAR & YARA: Modern SOC Workflow](./EDR_SIEM_SOAR_YARA/README.md)
* **Tier 1 (Endpoint Depth):** CrowdStrike Falcon EDR kernel-level sensor telemetry, process ancestry trees, and real-time host network isolation.
* **Tier 2 (Enterprise Breadth):** Splunk SIEM log indexing, Common Information Model (CIM) normalization, and Search Processing Language (SPL) correlation rules.
* **Tier 3 (Automated Containment):** Palo Alto Cortex XSOAR playbook automation, indicator enrichment via VirusTotal / AlienVault OTX, and dynamic ticket triage.
* **Threat Hunting with YARA:** Writing custom byte-sequence and regular expression rules to hunt malware artifacts across enterprise disk volumes.

### 2. [NIST SP 800-61 Incident Response Guide](./NIST%20800-61/README.md)
* **Phase 1 (Preparation):** Establishing CSIRT teams, telemetry pipelines, pre-approved playbook authority, and out-of-band communication channels.
* **Phase 2 (Detection & Analysis):** Triaging alerts, establishing the 4Ws timeline (Who, What, When, Where), scoping the blast radius, and prioritizing severity.
* **Phase 3 (Containment, Eradication & Recovery):** Short-term network isolation, subverting attacker persistence, rotating compromised credentials, restoring clean golden images, and validating network hygiene.
* **Phase 4 (Post-Incident Activity):** Root cause analysis (RCA), executive debriefing, calculating MTTR/MTTD metrics, and feeding lessons learned into SIEM detection engineering.
