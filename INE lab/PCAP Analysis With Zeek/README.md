# 🦈 PCAP Analysis With Zeek — Lab Documentation

![Zeek Banner](./images/zeek_pcap_analysis_banner.jpg)

This directory contains the complete network forensics, PCAP dissection, and threat hunting walkthrough for the **PCAP Analysis With Zeek** hands-on lab from INE Security.

---

## 📂 Directory Contents

* **[PCAP_Analysis_With_Zeek_Walkthrough.md](./PCAP_Analysis_With_Zeek_Walkthrough.md)**: Master in-depth walkthrough answering all 15 questions across both malware scenarios, featuring technical command explanations, log analyses, and detection engineering rules.
* **[images/](./images/)**: Custom visual assets including the hero banner, Zeek architecture and processing pipeline infographic, and animated terminal live demo GIF.
* **[image/](./image/)**: Full chronological archive of all 22 official lab screenshots (`1.png` through `5_6.png`).
* **[PCAP Analysis With Zeek solution.mp4](./PCAP%20Analysis%20With%20Zeek%20solution.mp4)**: Complete high-resolution walkthrough video demonstration.

---

## ⚡ Quick Incident Triage Summary

| Attribute | Details |
|---|---|
| **Platform / Course** | INE Security — Network Defense & Threat Hunting |
| **Target OS** | Ubuntu (Zeek Sensor) & Kali Linux |
| **Core Tools** | Zeek (Bro), `zeek-cut`, `jq`, `awk` |
| **Malware 1 Threats** | Bumblebee RAT (`139.177.146.137`), Cobalt Strike Beacon (`ceyuvigi.com` / `23.108.57.213`) |
| **Malware 2 Threat** | Emotet Phishing Campaign (Dropper: Word doc, Payload: `6169583.exe` - 429,056 bytes) |
| **Compromised Host** | `172.17.1.129` (`00:1e:67:4a:d7:5c` / `Nalyvaiko-PC` / `innochka.nalyvaiko`) |
| **Questions Solved** | 🟢 **15 of 15 Complete** |

---

👉 **Read the full walkthrough**: [PCAP Analysis With Zeek Walkthrough](./PCAP_Analysis_With_Zeek_Walkthrough.md)
