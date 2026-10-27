# INE / PentesterAcademy — Kibana: Squid Log Analysis (Challenge 1190)
## Complete Lab Investigation Report & DFIR Solution Guide

- **Course:** Advanced Network Forensics / SOC Analysis
- **Lab Title:** Kibana: Squid Log Analysis
- **Target URL:** `https://my.ine.com/labs/fad72959-09d1-3078-9e10-8ba9b3d2ce22`
- **AttackDefense Challenge ID:** `1190` (`https://attackdefense.com/challengedetails?cid=1190`)
- **Primary Ground Truth Manual:** [walkthrough-1190.pdf](file:///c:/Users/putin/Downloads/Cyber-Blog/INE%20lab/Kibana%20Squid%20Log%20Analysis/walkthrough-1190.pdf)
- **Target Environment:** Elasticsearch & Kibana 7.x indexing `squid-logs*`

---

## 📊 Master Answer Key (All 10 Challenge Flags)

| # | Lab Target Question | Verified Answer | Input Variants / Permissible Submissions | Kibana Query / Filter |
|---|---------------------|-----------------|------------------------------------------|-----------------------|
| **1** | Attacker IP testing open proxy via Nmap `http-open-proxy` | `192.161.225.4` | `192.161.225.4` | `destination_host:www.google.com` |
| **2** | Attacker IP enumerating live network hosts | `192.161.225.4` | `192.161.225.4` | `response_status>500` |
| **3** | Number of ports scanned & list of scanned ports | **Count:** `11`<br>**List:** `21, 80, 139, 443, 1433, 1521, 1723, 3389, 445, 8080, 9100` | **Primary field:** `11`<br>**If list required:** `21, 80, 139, 443, 1433, 1521, 1723, 3389, 445, 8080, 9100` *(or sorted: `21, 80, 139, 443, 445, 1433, 1521, 1723, 3389, 8080, 9100`)* | Visualize Terms Aggregation on `port.keyword` with filter `response_status:[500 TO 599] AND source_ip:192.161.225.4` |
| **4** | Number of live hosts detected in attacker scan | `3` | `3` *(Hosts: `192.170.46.1`, `192.170.46.4`, `192.170.46.5`)* | `response_status<500 and destination_ip:192.170.46.* and source_ip:192.161.225.4` |
| **5** | Attacker IP running web vulnerability scanner | `192.161.225.5` | `192.161.225.5` | `response_status:404 and destination_ip:192.170.46.5` |
| **6** | FTP username used to retrieve file (`/flag`) | `billy` | `billy` | `protocol:ftp and response_status:200` |
| **7** | IP address of SSH server tunneled via open proxy | `192.170.46.3` | `192.170.46.3` | `http_method:CONNECT and port:22 and response_status:200` *(unauthenticated proxy entry has `user: -`)* |
| **8** | Attacker IP conducting Hydra FTP dictionary attack | `192.161.225.6` | `192.161.225.6` | `http_method:CONNECT and port:21` |
| **9** | Username whose proxy credentials were compromised | `admin` | `admin` | `destination_host:scanme.nmap.org and response_status:200` |
| **10** | Approximate duration (in seconds) of authenticated SSH session | `28` | `28` *(Exact duration: `28202` ms $\approx 28.2$ s)* | `http_method:CONNECT and port:22 and response_status:200 and user:admin` |

---

## 🔍 Detailed Forensic Investigation & Walkthrough

### Question 1: Attacker IP testing open proxy via `http-open-proxy`
- **Objective:** Identify the attacker host that evaluated if the Squid proxy was open without authentication using Nmap's script `http-open-proxy`.
- **KQL Query:** `destination_host:www.google.com`
- **Forensic Findings:**
  - At `Aug 9, 2019 @ 02:00:36.711`: `source_ip: 192.161.225.4`, `http_method: GET`, `response_status: 200`, `result_code: TCP_MISS_ABORTED`
  - At `Aug 9, 2019 @ 02:00:36.757`: `source_ip: 192.161.225.4`, `http_method: HEAD`, `response_status: 200`, `result_code: TCP_MISS`
  - At `Aug 9, 2019 @ 02:00:36.760`: `source_ip: 192.161.225.4`, `http_method: CONNECT`, `port: 80`, `response_status: 200`, `result_code: TCP_TUNNEL`
- **Conclusion:** Nmap's `http-open-proxy.nse` sends rapid `GET`, `HEAD`, and `CONNECT` requests to `www.google.com`. All 3 requests occurred within 49 ms from `192.161.225.4`.
- **Answer:** `192.161.225.4`

---

### Question 2: Attacker IP enumerating live network hosts
- **Objective:** Find the attacker IP scanning the internal network through the open proxy.
- **KQL Query:** `response_status>500`
- **Forensic Findings:**
  - Filtering for HTTP server errors (`>500`) returns 328 hits.
  - The proxy generated HTTP 503 (`TCP_MISS/503`) whenever attempting to connect to non-responsive internal endpoints on `192.170.46.0/24`.
  - Every single scanning probe originated from `192.161.225.4`.
- **Answer:** `192.161.225.4`

---

### Question 3: Number of ports scanned & list of all scanned ports
- **Objective:** Determine the number of unique ports targeted during the internal host discovery sweep and list them.
- **Kibana Visualization:**
  - Chart Type: Vertical Bar chart on index `squid-logs*`
  - X-Axis: Aggregation = `Terms`, Field = `port.keyword`, Size = `20`
  - Split Series: Sub-aggregation = `Filters`, Query = `response_status:[500 TO 599] AND source_ip:192.161.225.4`
- **Scanned Ports Breakdown:**
  1. `21` — FTP
  2. `80` — HTTP
  3. `139` — NetBIOS Session Service
  4. `443` — HTTPS
  5. `445` — Microsoft-DS / SMB
  6. `1433` — Microsoft SQL Server
  7. `1521` — Oracle Database Listener
  8. `1723` — PPTP VPN
  9. `3389` — Microsoft Remote Desktop (RDP)
  10. `8080` — Alternative HTTP / Web Proxy
  11. `9100` — PDL / HP JetDirect Printing
- **Answers:**
  - **Count:** `11`
  - **List:** `21, 80, 139, 443, 1433, 1521, 1723, 3389, 445, 8080, 9100` *(or sorted: `21, 80, 139, 443, 445, 1433, 1521, 1723, 3389, 8080, 9100`)*

---

### Question 4: Live hosts detected by attacker scan
- **Objective:** Count how many live internal hosts responded successfully during the scan by `192.161.225.4`.
- **KQL Query:** `response_status<500 and destination_ip:192.170.46.* and source_ip:192.161.225.4`
- **Forensic Findings:**
  - Exactly 3 successful connections are recorded:
    1. `192.170.46.1` — Port `80` (HTTP active gateway)
    2. `192.170.46.4` — Port `21` (FTP service, returned HTTP 200)
    3. `192.170.46.5` — Port `80` (Web server, returned HTTP 200)
- **Manual Errata Warning:** Page 9 of the official manual prints an errant filter containing `destination_ip:192.170.46.5` instead of `destination_ip:192.170.46.*`. Only the wildcard query exposes all 3 hosts.
- **Answer:** `3`

---

### Question 5: Attacker IP using popular web vulnerability scanner
- **Objective:** Identify the attacker machine running a web vulnerability scanning tool against the internal web server (`192.170.46.5`).
- **KQL Query:** `response_status:404 and destination_ip:192.170.46.5`
- **Forensic Findings:**
  - At `03:13:39`, an attacker sent rapid requests testing for script handlers and non-existent files: `/03T3egDX.ashx`, `/03T3egDX.dtd`, `/03T3egDX.printer`, `/03T3egDX.dbe`, `/03T3egDX.vts`.
  - This 8-character randomized probe is the fingerprint of the **Nikto** web scanner.
  - All scanning traffic originated from source IP `192.161.225.5`.
- **Answer:** `192.161.225.5`

---

### Question 6: FTP username used to retrieve file
- **Objective:** Find the FTP username used by the attacker to log into the FTP server (`192.170.46.4`) and download the flag.
- **KQL Query:** `protocol:ftp and response_status:200`
- **Forensic Findings:**
  - Record at `Aug 9, 2019 @ 03:07:38.412`:
    - `source_ip: 192.161.225.5`
    - `destination_ip: 192.170.46.4:21`
    - `request_path: /flag`
    - `response_status: 200`
    - `content_type: text/plain`
    - `username: billy`
- **Answer:** `billy`

---

### Question 7: IP address of SSH server tunneled via open proxy
- **Objective:** Find the IP address of the SSH server accessed via an unauthenticated `CONNECT` tunnel.
- **KQL Query:** `http_method:CONNECT and port:22 and response_status:200`
- **Forensic Findings:**
  - Record at `Aug 9, 2019 @ 03:11:25.035`:
    - `source_ip: 192.161.225.7`
    - `destination_ip: 192.170.46.3:22`
    - `user: -` (indicates open proxy access without proxy authentication)
    - `result_code: TCP_TUNNEL`
- **Answer:** `192.170.46.3`

---

### Question 8: Attacker IP conducting Hydra FTP dictionary attack
- **Objective:** Identify the attacker machine performing an automated password guessing attack against the FTP service.
- **KQL Query:** `http_method:CONNECT and port:21`
- **Forensic Findings:**
  - Over 1,030 rapid `CONNECT` tunnel requests targeted port 21 on `192.170.46.4`.
  - At `15:34:05.736` to `15:34:06.281`, 33 connections were opened in less than 1 second, typical of THC-Hydra concurrent threads.
  - Source IP: `192.161.225.6`.
- **Answer:** `192.161.225.6`

---

### Question 9: Username whose proxy credentials were compromised
- **Objective:** Find the proxy user whose credentials were brute-forced after Squid was reconfigured to require authentication.
- **KQL Query:** `destination_host:scanme.nmap.org and response_status:200`
- **Forensic Findings:**
  - After authentication was enforced, `192.161.225.7` generated 45,017 `TCP_DENIED/407` proxy authentication failure events spraying common usernames (`root`, `administrator`, `webadmin`, `guest`, `admin`).
  - At `15:51:58.182`, authentication succeeded (`response_status: 200`) accessing `scanme.nmap.org` with user `admin`.
- **Answer:** `admin`

---

### Question 10: Duration of authenticated SSH session (in seconds)
- **Objective:** Calculate the approximate duration in seconds of the SSH session established using the compromised `admin` credentials.
- **KQL Query:** `http_method:CONNECT and port:22 and response_status:200 and user:admin`
- **Forensic Findings:**
  - Record at `Aug 9, 2019 @ 16:21:59.484`:
    - `source_ip: 192.161.225.7`
    - `destination_ip: 192.170.46.3:22`
    - `user: admin`
    - `duration: 28202` ms
  - Millisecond to second calculation: $\frac{28202}{1000} = 28.202 \text{ seconds} \approx \mathbf{28} \text{ seconds}$.
- **Answer:** `28`

---

## 🛡️ Squid Proxy Hardening & Prevention Measures

1. **Disable Open Relay / Tunneling:**
   - Enforce strict `http_access deny !Safe_ports` and `http_access deny CONNECT !SSL_ports`.
   - Never allow generic port `CONNECT` requests (e.g. ports 21, 22) through a corporate HTTP forward proxy.
2. **Enforce Strong Proxy Authentication:**
   - Enforce mandatory strong password policies and rate limiting (`fail2ban` or iptables `recent` module) to block dictionary attacks on port 3128.
3. **Internal Subnet ACLs:**
   - Restrict forward proxy ACLs so that clients cannot route traffic into private management subnets (`192.170.46.0/24`).
