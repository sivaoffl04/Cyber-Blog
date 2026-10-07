#!/usr/bin/env python3
"""
Wazuh Constant Database (CDB) Port List Manager
===============================================
Lab: Detecting Abnormal Network Connections With Wazuh
Platform: INE Security

This script allows SOC engineers to:
1. Validate the syntax of /var/ossec/etc/lists/common-ports
2. Export a clean, sorted CDB key-only format ('<port>:')
3. Add or remove baseline allowed ports
4. Test candidate Sysmon DestinationPort telemetry events
"""

import sys
import os
import argparse

DEFAULT_LAB_PORTS = [
    21, 22, 25, 53, 80, 135, 389, 443, 445, 993, 995,
    1514, 1515, 3389, 3306, 5000, 5223, 8000, 8002, 8080, 8083, 8443
]

PORT_SERVICE_MAP = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    135: "MSRPC",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    993: "IMAPS",
    995: "POP3S",
    1514: "Wazuh Agent Communication",
    1515: "Wazuh Agent Enrollment",
    3389: "RDP",
    3306: "MySQL",
    5000: "UPnP / Dev Web Server",
    5223: "Apple Push Notifications",
    8000: "HTTP Alternate",
    8002: "HTTP Alternate",
    8080: "HTTP Proxy / Tomcat",
    8083: "Secure Web Admin",
    8443: "HTTPS Alternate"
}

def export_cdb_file(filename="common-ports", ports=None):
    """Exports ports in Wazuh CDB key-only format ('port:')"""
    if ports is None:
        ports = DEFAULT_LAB_PORTS
    sorted_ports = sorted(set(ports))
    with open(filename, "w") as f:
        for p in sorted_ports:
            f.write(f"{p}:\n")
    print(f"[+] Successfully exported {len(sorted_ports)} ports to '{filename}' in CDB format.")
    print(f"[*] Ownership reminder on Ubuntu:")
    print(f"    sudo chown wazuh:wazuh {filename}")
    print(f"    sudo chmod 660 {filename}")

def validate_cdb_file(filename):
    """Validates that each line conforms to key: or key:value format."""
    if not os.path.exists(filename):
        print(f"[-] File not found: {filename}")
        return False

    valid = True
    ports = []
    with open(filename, "r") as f:
        for idx, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            if ":" not in line:
                print(f"[-] Line {idx} is invalid (missing colon delimiter): '{line}'")
                valid = False
                continue
            key = line.split(":")[0].strip()
            if not key.isdigit():
                print(f"[-] Line {idx} key is not numeric: '{key}'")
                valid = False
                continue
            ports.append(int(key))

    if valid:
        print(f"[✓] Syntax VALID: Loaded {len(ports)} valid port keys.")
        print(f"[+] Ports defined: {sorted(ports)}")
    return valid

def print_port_table(ports=None):
    """Prints a formatted table of ports and common protocol descriptions."""
    if ports is None:
        ports = DEFAULT_LAB_PORTS
    print("\n+-------+-----------------------------+----------------+")
    print("| Port  | Common Service Name         | Baseline Role  |")
    print("+-------+-----------------------------+----------------+")
    for p in sorted(ports):
        svc = PORT_SERVICE_MAP.get(p, "Custom / Unassigned")
        print(f"| {p:<5} | {svc:<27} | Allowed        |")
    print("+-------+-----------------------------+----------------+\n")

def main():
    parser = argparse.ArgumentParser(
        description="Wazuh Constant Database (CDB) Port Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--export", action="store_true", help="Export default lab common-ports file")
    parser.add_argument("--output", type=str, default="common-ports", help="Output file name (default: common-ports)")
    parser.add_argument("--validate", type=str, help="Validate an existing CDB file")
    parser.add_argument("--list", action="store_true", help="Display table of default whitelisted ports")

    args = parser.parse_args()

    if args.export:
        export_cdb_file(args.output)
    elif args.validate:
        validate_cdb_file(args.validate)
    elif args.list:
        print_port_table()
    else:
        print_port_table()
        parser.print_help()

if __name__ == "__main__":
    main()
