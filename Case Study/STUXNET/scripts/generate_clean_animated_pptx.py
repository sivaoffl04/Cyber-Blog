"""
STUXNET Masterclass Seminar: Clean & Animated PowerPoint (.pptx) Generator
Produces STUXNET_Masterclass_Seminar_20_Slides.pptx with:
1. Ultra-clean, modern cyber/SCADA visual layout (16:9 Widescreen)
2. Precision image scaling and centering via PIL (zero distortion)
3. Native OpenXML slide transitions (<p:transition>)
4. Native OpenXML sequential shape entrance animations (<p:timing>)
5. Comprehensive speaker notes and talking script for all 20 slides
"""

import os
import sys
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml

def create_timing_xml(shape_ids):
    """
    Constructs a valid OpenXML <p:timing> block that animates shapes sequentially.
    Shape 1 appears first, then subsequent shapes fade in on click or sequential timing.
    """
    seq_children = []
    node_id = 3
    
    for idx, spid in enumerate(shape_ids):
        # First shape appears on click or initial delay, next shapes follow
        delay = 200 if idx == 0 else 120
        st_cond = f'<p:cond delay="{delay}"/>' if idx == 0 else f'<p:cond evt="onEnd" delay="120"><p:tnRef val="{node_id-4}"/></p:cond>'
        
        par_xml = f'''
        <p:par xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
          <p:cTn id="{node_id}" fill="hold">
            <p:stCondLst>
              {st_cond}
            </p:stCondLst>
            <p:childTnLst>
              <p:par>
                <p:cTn id="{node_id+1}" fill="hold">
                  <p:stCondLst>
                    <p:cond delay="0"/>
                  </p:stCondLst>
                  <p:childTnLst>
                    <p:set>
                      <p:cBhvr>
                        <p:cTn id="{node_id+2}" dur="1" fill="hold">
                          <p:stCondLst>
                            <p:cond delay="0"/>
                          </p:stCondLst>
                        </p:cTn>
                        <p:tgtEl>
                          <p:spTgt spid="{spid}"/>
                        </p:tgtEl>
                        <p:attrNameLst>
                          <p:attrName>style.visibility</p:attrName>
                        </p:attrNameLst>
                      </p:cBhvr>
                      <p:to>
                        <p:strVal val="visible"/>
                      </p:to>
                    </p:set>
                    <p:animEffect transition="in" filter="fade">
                      <p:cBhvr>
                        <p:cTn id="{node_id+3}" dur="350" fill="hold"/>
                        <p:tgtEl>
                          <p:spTgt spid="{spid}"/>
                        </p:tgtEl>
                      </p:cBhvr>
                    </p:animEffect>
                  </p:childTnLst>
                </p:cTn>
              </p:par>
            </p:childTnLst>
          </p:cTn>
        </p:par>
        '''
        seq_children.append(par_xml)
        node_id += 4
        
    full_timing = f'''
    <p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
      <p:tnLst>
        <p:par>
          <p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
            <p:childTnLst>
              <p:seq concurrent="1" nextAc="seek">
                <p:cTn id="2" dur="indefinite" nodeType="mainSeq">
                  <p:childTnLst>
                    {''.join(seq_children)}
                  </p:childTnLst>
                </p:cTn>
                <p:prevCondLst>
                  <p:cond evt="onPrev" delay="0">
                    <p:tgtEl><p:sldTgt/></p:tgtEl>
                  </p:cond>
                </p:prevCondLst>
                <p:nextCondLst>
                  <p:cond evt="onNext" delay="0">
                    <p:tgtEl><p:sldTgt/></p:tgtEl>
                  </p:cond>
                </p:nextCondLst>
              </p:seq>
            </p:childTnLst>
          </p:cTn>
        </p:par>
      </p:tnLst>
    </p:timing>
    '''
    return parse_xml(full_timing)

def build_clean_animated_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Clean Modern Cyber Aesthetic
    C_BG = RGBColor(11, 15, 25)          # #0B0F19 Dark Obsidian
    C_CARD = RGBColor(19, 28, 46)        # #131C2E Card Background
    C_BORDER = RGBColor(31, 46, 71)      # #1F2E47 Border Line
    C_CYAN = RGBColor(0, 240, 255)       # #00F0FF Vibrant Cyan
    C_CRIMSON = RGBColor(255, 51, 102)   # #FF3366 Crimson Alert
    C_AMBER = RGBColor(245, 158, 11)     # #F59E0B Warning Amber
    C_EMERALD = RGBColor(16, 185, 129)   # #10B981 Safe Emerald
    C_WHITE = RGBColor(255, 255, 255)    # #FFFFFF Pure White
    C_TEXT = RGBColor(241, 245, 249)     # #F1F5F9 Off White
    C_MUTED = RGBColor(148, 163, 184)    # #94A3B8 Slate Gray
    C_DIM = RGBColor(71, 85, 105)        # #475569 Dim Gray

    # Slide Data
    slides_data = [
        # Slide 1
        {
            "tag": "ACT 01 // OVERVIEW",
            "title": "STUXNET: The Cyber-Physical Rubicon",
            "subtitle": "Deconstructing the World's First Kinetic Weapon & The Sabotage of Natanz",
            "bullets_title": "Strategic Executive Summary",
            "bullets": [
                "Target Facility: Natanz Fuel Enrichment Plant (FEP), Iran (~8,000 IR-1 gas centrifuges).",
                "Strategic Mission: Clandestinely destroy nuclear enrichment hardware without overt kinetic warfare.",
                "Novel Weaponry: 4 simultaneous Windows zero-days, 2 stolen hardware code-signing certificates.",
                "Kinetic Result: Physical destruction and decommissioning of an estimated ~1,000 centrifuges.",
                "Historical Milestone: Proved that digital software instructions can bend steel and shatter industrial hardware."
            ],
            "stats": [
                ("4 ZERO-DAYS", "Shell, Spooler, EoP", C_CRIMSON),
                ("2 STOLEN CERTS", "Realtek & JMicron", C_AMBER),
                ("~1,000 ROTORS", "Centrifuges Broken", C_CYAN),
                ("500 KB BINARY", "54 In-Memory DLLs", C_EMERALD)
            ],
            "img": "image/stuxnet_how_it_worked_infographic.jpg",
            "caption": "FIGURE 1.1: Stuxnet's end-to-end cyber-physical kill chain: USB infiltration to PLC manipulation.",
            "notes": "Welcome to the Stuxnet masterclass seminar. In June 2010, the global cybersecurity landscape fundamentally shifted. Up until that point, malware was designed to steal passwords or hold financial data hostage. Stuxnet reached out from cyberspace to physically destroy industrial hardware located 8 meters beneath the Iranian desert."
        },
        # Slide 2
        {
            "tag": "ACT 01 // GEOPOLITICS & GEOGRAPHY",
            "title": "The Natanz Fuel Enrichment Facility",
            "subtitle": "A Subterranean Fortress Shielded by Reinforced Concrete and Air Gaps",
            "bullets_title": "Facility Hardening & Defense",
            "bullets": [
                "Geographical Isolation: Located 300 km south of Tehran in the central desert of Isfahan Province.",
                "Subterranean Hardening: Cascade halls buried 8 meters underground beneath a 2.5-meter reinforced concrete roof.",
                "Perimeter Security: Ringed by anti-aircraft missile batteries, radar installations, and elite military guards.",
                "The Air Gap: Completely disconnected from the public Internet; zero incoming public telco fiber connections.",
                "The Geopolitical Impasse: Military airstrikes carried high risks of regional war; a covert cyber weapon was the surgical alternative."
            ],
            "stats": [
                ("8 METERS", "Bunker Depth", C_CYAN),
                ("2.5 METERS", "Concrete Ceiling", C_AMBER),
                ("0% INTERNET", "Strict Air Gap", C_EMERALD)
            ],
            "img": "image/natanz_enrichment_facility_aerial.jpg",
            "caption": "FIGURE 2.1: Satellite reconnaissance of the Natanz Fuel Enrichment Plant showing subterranean cascade halls.",
            "notes": "Natanz was designed to be impervious to conventional military strikes. The cascade halls were buried 8 meters underground, capped with reinforced concrete and earth. There was no internet connection. Plant operators believed physical isolation guaranteed absolute security."
        },
        # Slide 3
        {
            "tag": "ACT 01 // PARADIGM SHIFT",
            "title": "The Cyber-Physical Paradigm Shift",
            "subtitle": "The Transition from Information Security to Physical Kinetic Consequences",
            "bullets_title": "Conventional IT vs. Cyber-Physical Sabotage",
            "bullets": [
                "Conventional IT Threat: Focuses on the CIA Triad (Confidentiality, Integrity, Availability of data).",
                "Cyber-Physical Threat (OT): Focuses on physical safety, containment, and machinery integrity.",
                "Mechanical Translation: Stuxnet translated CPU logic into torque: Delta Logic -> Delta Torque -> Resonance -> Shear.",
                "Slow Attrition Doctrine: The goal was NOT to blow up the entire plant at once, which would reveal an attack.",
                "Manufacturing Defect Illusion: Stuxnet broke centrifuges gradually, causing Iran to fire engineers and blame domestic suppliers."
            ],
            "stats": [
                ("CIA TRIAD", "IT Security Target", C_MUTED),
                ("KINETIC SABOTAGE", "OT Attack Target", C_CRIMSON),
                ("PARANOIA", "Psychological Impact", C_AMBER)
            ],
            "img": "image/stuxnet_natanz_centrifuges_cascade.jpg",
            "caption": "FIGURE 3.1: Cascade hall containing 164 IR-1 centrifuges spinning UF6 gas under high vacuum.",
            "notes": "The core genius of Stuxnet was psychological and kinetic warfare combined. If you bomb a facility, the enemy rebuilds it. But if their own machines silently tear themselves apart while computer monitors report normal operation, they blame their engineers and domestic suppliers."
        },
        # Slide 4
        {
            "tag": "ACT 02 // ARCHITECTURE",
            "title": "Industrial Topology & The Purdue Model",
            "subtitle": "How Modern Critical Infrastructure Separates Business IT from Physical Processes",
            "bullets_title": "The 6 Levels of Purdue (PERA)",
            "bullets": [
                "Level 4/5 (Enterprise IT): Corporate network, email, ERP, public internet.",
                "Level 3.5 (Industrial DMZ): Jump servers, patch mirrors, data historians.",
                "Level 3 (Operations Management): SCADA central servers, maintenance tracking.",
                "Level 2 (Supervisory Control): Human-Machine Interfaces (WinCC), Engineering Workstations (STEP 7).",
                "Level 1 (Basic Control): Siemens S7-315 and S7-417 Programmable Logic Controllers.",
                "Level 0 (Physical Process): Variable Frequency Drives, vacuum pumps, valves, and rotating IR-1 centrifuges."
            ],
            "stats": [
                ("LEVELS 0-5", "Purdue Architecture", C_CYAN),
                ("SUPPLY CHAIN", "Infiltration Route", C_CRIMSON),
                ("LEVEL 1 & 0", "Compromised Domain", C_AMBER)
            ],
            "img": "image/stuxnet_purdue_model_deep_dive.jpg",
            "caption": "FIGURE 4.1: The Purdue Enterprise Reference Architecture (PERA) showing Stuxnet's path from Level 4 to Level 0.",
            "notes": "The Purdue Model defines strict zones of trust. You never connect a Level 1 PLC directly to the internet. Firewalls and air gaps isolate Level 2 and Level 1. Stuxnet bypassed perimeter firewalls by riding the supply chain straight into Level 2 on contractor flash drives."
        },
        # Slide 5
        {
            "tag": "ACT 02 // INITIAL ACCESS",
            "title": "Crossing the Chasm: The Air-Gap Breach",
            "subtitle": "Supply-Chain Compromise & Zero-Click Removable Media Exploitation",
            "bullets_title": "The Infiltration Pathway",
            "bullets": [
                "Targeting Contractors: Attackers infected 5 Iranian engineering contractor firms (Foolad, Behpajooh, Neda, Kala, CG-IT).",
                "The Trojan Horse: Technicians entered Natanz with infected laptops and USB drives to perform maintenance.",
                "Zero-Click USB Execution: Inserting the flash drive was sufficient; no need to click or execute any file.",
                "CVE-2010-2568: Windows Shell parser in shell32.dll loaded malicious DLL (~WTR4141.tmp) merely to display shortcut icons.",
                "Lateral Subnet Spread: Traversed internal Level 2 subnets via Print Spooler RPC, SMB shares, and STEP 7 project files."
            ],
            "stats": [
                ("5 COMPANIES", "Target Contractors", C_AMBER),
                ("ZERO-CLICK", "Icon Rendering Exploit", C_CRIMSON),
                ("CVE-2010-2568", "Windows Shell LNK", C_CYAN)
            ],
            "img": "image/stuxnet_scada_plc_network_architecture.jpg",
            "caption": "FIGURE 5.1: SCADA and PLC industrial network topology illustrating lateral propagation.",
            "notes": "An air gap is only as secure as the people who maintain it. Stuxnet did not need an internet cable. The attackers targeted third-party integration contractors. When a technician plugged a calibration laptop into the Level 2 switch at Natanz, Stuxnet hopped the air gap in seconds."
        },
        # Slide 6
        {
            "tag": "ACT 03 // VULNERABILITY EXPLOITATION",
            "title": "The Arsenal: Four Windows Zero-Days",
            "subtitle": "An Unprecedented R&D Investment in Remote Execution and Privilege Escalation",
            "bullets_title": "The 4 Zero-Day CVE Breakdown",
            "bullets": [
                "CVE-2010-2568 (Windows Shell LNK): Zero-click execution via shortcut icon rendering in shell32.dll.",
                "CVE-2010-2729 (Print Spooler RPC): Remote code execution via spoolsv.exe over port 445 for lateral movement.",
                "CVE-2010-3338 (Task Scheduler EoP): Local privilege escalation in taskschd.dll to obtain NT AUTHORITY\\SYSTEM.",
                "CVE-2010-2743 (Win32k.sys Graphics EoP): TrueType keyboard layout memory corruption granting Ring-0 kernel execution.",
                "Economic Scale: Assembling four working zero-days simultaneously represented millions of dollars in nation-state R&D."
            ],
            "stats": [
                ("4 ZERO-DAYS", "Simultaneous Weapons", C_CRIMSON),
                ("RING 0", "Kernel Execution", C_AMBER),
                ("$1M+ VALUE", "Exploit Market Price", C_CYAN)
            ],
            "img": "image/stuxnet_windows_zero_days_internals.jpg",
            "caption": "FIGURE 6.1: Dissection of Stuxnet's 4 zero-days and dual code-signing certificate compromise.",
            "notes": "Prior to 2010, the security industry had never seen a piece of malware armed with four distinct zero-days. In the commercial exploit broker market, this represents millions of dollars. It was definitive proof of a well-funded nation-state intelligence apparatus at work."
        },
        # Slide 7
        {
            "tag": "ACT 03 // CRYPTOGRAPHIC EVASION",
            "title": "Subverting Cryptographic Trust",
            "subtitle": "Bypassing 64-bit Windows Driver Signature Enforcement (DSE)",
            "bullets_title": "The Driver Signature Enforcement Barrier",
            "bullets": [
                "The Security Barrier: 64-bit Windows strictly requires all kernel drivers to have a valid WHQL digital signature.",
                "The Intelligence Heist: Attackers breached two reputable hardware manufacturers in Hsinchu Science Park, Taiwan.",
                "Compromised Vendors: Realtek Semiconductor Corp. and JMicron Technology Corp.",
                "Private Key Theft: Exfiltrated private signing keys to sign malicious kernel rootkit drivers (mrxnet.sys, mrxcls.sys).",
                "AV Whitelisting: Contemporary antivirus engines and Windows kernel verifiers treated the drivers as trusted software."
            ],
            "stats": [
                ("REALTEK CORP", "Primary Stolen Cert", C_CYAN),
                ("JMICRON TECH", "Secondary Failover", C_AMBER),
                ("100% TRUST", "AV Engines Blinded", C_CRIMSON)
            ],
            "img": "image/stuxnet_windows_zero_days_internals.jpg",
            "caption": "FIGURE 7.1: Driver Signature Enforcement bypass using stolen Realtek and JMicron digital certificates.",
            "notes": "Why didn't antivirus catch Stuxnet? Because Stuxnet carried legitimate, cryptographically valid signatures from Realtek and JMicron. The attackers didn't crack RSA-2048 cryptography; they hacked the software supply chain to steal the private keys."
        },
        # Slide 8
        {
            "tag": "ACT 03 // ROOTKIT & STEALTH",
            "title": "Kernel Rootkit & Memory Anti-Forensics",
            "subtitle": "Hooking Native APIs and Hiding Malicious Artifacts in Plain Sight",
            "bullets_title": "The mrxnet.sys Rootkit Engine",
            "bullets": [
                "Native API Hooking: Hooked NtQueryDirectoryFile and ZwQueryDirectoryFile in the Windows kernel.",
                "Ghost Files: Hidden files matching ~WTR*.tmp and malicious .lnk shortcuts were filtered out of directory listings.",
                "In-Memory Virtual Filesystem: Decrypted and linked 54 DLL components entirely in RAM; never touched disk unencrypted.",
                "Process Injection: Injected into trusted system processes (services.exe, lsass.exe, explorer.exe) to hide activity.",
                "Operational Hygiene: Enforced 3-hop infection limit per USB drive; hardcoded kill switch date of June 24, 2012."
            ],
            "stats": [
                ("54 DLLs", "RAM-Only Decryption", C_CYAN),
                ("3 HOPS MAX", "USB Hygiene Limit", C_AMBER),
                ("JUNE 24 2012", "Hard Killswitch Date", C_EMERALD)
            ],
            "img": "image/stuxnet_step7_dll_proxy_architecture.jpg",
            "caption": "FIGURE 8.1: Kernel memory injection and DLL proxying architecture.",
            "notes": "Stuxnet's authors exhibited extraordinary operational discipline. They implemented an in-memory virtual file system and hooked kernel directory calls so their exploit files were literally invisible. They even built in an infection hop counter: after 3 machines, the USB stopped spreading."
        },
        # Slide 9
        {
            "tag": "ACT 04 // TARGET IDENTIFICATION",
            "title": "Target Fingerprinting: The Narrow Funnel",
            "subtitle": "Exacting Hardware Filters Designed to Prevent Collateral Damage",
            "bullets_title": "The 6-Stage Qualification Funnel",
            "bullets": [
                "Filter 1 (Operating System): Windows 2000, XP, Server 2003, or Windows 7.",
                "Filter 2 (Industrial Software): Siemens SIMATIC STEP 7 must be installed and active.",
                "Filter 3 (Communications Card): Must detect Siemens CP 342-5 communications processor on Profibus DP.",
                "Filter 4 (Device Count): Exactly 33 Variable Frequency Drives (VFDs) connected per subnet.",
                "Filter 5 (Specific Manufacturers): VFDs must carry vendor IDs belonging to Fararo Paya (Iran) or Vacon (Finland).",
                "Filter 6 (Cascade Geometry): Exactly 164 centrifuges arranged in 18 sub-cascades. If ANY check failed, Stuxnet went dormant."
            ],
            "stats": [
                ("33 DRIVES", "VFD Subnet Count", C_CYAN),
                ("FARARO & VACON", "Target VFD Vendors", C_AMBER),
                ("164 ROTORS", "Cascade Requirement", C_CRIMSON)
            ],
            "img": "image/stuxnet_natanz_centrifuges_cascade.jpg",
            "caption": "FIGURE 9.1: The 164-centrifuge cascade hall at Natanz matching Stuxnet's exact hardware profile.",
            "notes": "Imagine releasing a weapon that can only infect someone who is exactly 6 feet tall, has blue eyes, and wears a red tie. That is what Stuxnet did in software. If a machine did not match all six hardware criteria, Stuxnet did nothing. It was laser-guided."
        },
        # Slide 10
        {
            "tag": "ACT 04 // ENGINEERING MAN-IN-THE-MIDDLE",
            "title": "The Man-in-the-Middle: s7otbxdx.dll",
            "subtitle": "Hijacking the Siemens Engineering Workstation and Intercepting PLC Code",
            "bullets_title": "The DLL Replacement Technique",
            "bullets": [
                "Core Siemens Library: s7otbxdx.dll handles communication between STEP 7 and Siemens PLCs over Port 102.",
                "The Substitution: Renamed legitimate DLL to s7otbxsx.dll and placed weaponized s7otbxdx.dll in its directory.",
                "Export Forwarding: Hooked 16 critical PLC functions, including s7blk_read and s7blk_write.",
                "Blinding the Engineer: When an engineer clicked 'Compare Blocks' or 'Upload Program from PLC':",
                "Stuxnet intercepted the request, fetched the original clean code from s7otbxsx.dll, and displayed clean ladder logic!"
            ],
            "stats": [
                ("PORT 102", "ISO-on-TCP Target", C_CYAN),
                ("16 HOOKS", "S7 APIs Intercepted", C_AMBER),
                ("CLEAN SPOOF", "Zero Alarms Raised", C_EMERALD)
            ],
            "img": "image/stuxnet_step7_dll_proxy_architecture.jpg",
            "caption": "FIGURE 10.1: Architecture of Stuxnet's DLL proxy hooking STEP 7 communication between EWS and PLC.",
            "notes": "Even if an engineer connected their laptop directly to the PLC and asked STEP 7: 'Show me what code is running on this controller', Stuxnet's hooked DLL intercepted the query, filtered out its own malicious blocks, and presented a clean copy. The engineer had no idea the PLC was compromised."
        },
        # Slide 11
        {
            "tag": "ACT 05 // PLC INTERNALS",
            "title": "Inside the Controller: Siemens S7 PLCs",
            "subtitle": "Direct Microcode Injection into S7-315 and S7-417 Controllers",
            "bullets_title": "S7 Cyclic Execution Model",
            "bullets": [
                "Organization Blocks: OB1 (main continuous execution loop) and OB35 (100ms cyclic interrupt timer).",
                "Function Blocks (FB/FC): Injected its own malicious blocks: FC1865 through FC1874.",
                "Data Blocks (DB): Allocated DB890 and DB8062 to store state-machine timers and recorded sensor readings.",
                "Cyclic Splicing: Spliced call to FC1865 into OB1; intercepted DP_SEND (FC1) and DP_RECV (FC2) to hijack Profibus.",
                "MC7 Bytecode: Stuxnet was the first malware in history to carry an MC7 compiler targeting PLC microcode directly."
            ],
            "stats": [
                ("OB1 / OB35", "Hooked S7 Loops", C_CYAN),
                ("FC1865-1874", "Malicious Function Blocks", C_CRIMSON),
                ("MC7 BYTECODE", "Direct PLC Assembly", C_AMBER)
            ],
            "img": "image/stuxnet_siemens_s7_mc7_bytecode_injection.jpg",
            "caption": "FIGURE 11.1: Microcode injection layout inside S7 CPU memory hooking OB1/OB35 cyclic loops.",
            "notes": "A PLC doesn't run Python or C; it runs a compiled microcode called MC7. Stuxnet was the first malware in history to carry an MC7 compiler. It injected new Function Blocks directly into PLC memory and hooked OB1—the cyclic heartbeat of the industrial controller."
        },
        # Slide 12
        {
            "tag": "ACT 06 // KINETIC PHYSICS SABOTAGE",
            "title": "The Physics of Sabotage: Centrifuge Destruction",
            "subtitle": "Exploiting Harmonic Resonance and Rotor Tensile Strength",
            "bullets_title": "Rotational Sabotage Sequence",
            "bullets": [
                "Normal Operation: 1,064 Hz (63,840 RPM). The aluminum rotor spins at Mach 1.5 in a high vacuum.",
                "Phase 1 (Overspeed Attack): Forced frequency drives up to 1,410 Hz (84,600 RPM) for 15 minutes, exceeding tensile limits.",
                "Phase 2 (The Rest Period): Slowed rotors back to normal for 27 days to prevent operational suspicion.",
                "Phase 3 (Resonance Crash): Dropped speed down to 2 Hz (120 RPM) for 50 minutes, forcing rotors through harmonic resonance.",
                "Catastrophic Impact: Violent flexural bending caused rotors to wobble, strike the vacuum casing, and disintegrate!"
            ],
            "stats": [
                ("1,064 Hz", "Nominal (63,840 RPM)", C_EMERALD),
                ("1,410 Hz", "Overspeed (+32.5%)", C_CRIMSON),
                ("2 Hz", "Resonance Crash", C_AMBER)
            ],
            "img": "image/stuxnet_centrifuge_rotor_physics_breakdown.jpg",
            "caption": "FIGURE 12.1: Physical stress breakdown of IR-1 rotor overspeed and harmonic resonance modes.",
            "notes": "At nominal speed, 1,064 Hz, the centrifuge spins safely. But during the overspeed phase, Stuxnet boosted the frequency to 1,410 Hz—pushing the aluminum rotor past its mechanical limit. Then, 27 days later, Stuxnet dropped the frequency to 2 Hz. In physics, when an object with high inertia slows down, it passes through its critical harmonic resonance frequencies. The rotor wobbled and struck the casing."
        },
        # Slide 13
        {
            "tag": "ACT 07 // SENSOR DECEPTION",
            "title": "The Deception Engine: The 21-Second Replay",
            "subtitle": "Blinding Control Rooms with Pre-Recorded Authentic Telemetry",
            "bullets_title": "Virtual Reality for SCADA Operators",
            "bullets": [
                "The 'Ocean's Eleven' Playbook: In the heist film, thieves tap security cameras and broadcast a 21-second loop.",
                "Recording Phase: Stuxnet captured 21 continuous seconds of authentic sensor data (vibration, pressure, temperature).",
                "Replay Phase: During the destructive 1,410 Hz attack, severed live sensor feeds and replayed the 21-second nominal recording.",
                "Alarm Suppression: Spliced logic suppressed emergency high-vibration trips; operators saw serene green indicators.",
                "Human Impact: Plant engineers believed the centrifuges were failing due to poor metallurgy or defective domestic parts."
            ],
            "stats": [
                ("21 SECONDS", "Recorded Telemetry Buffer", C_CYAN),
                ("DB89 MEMORY", "Replay Data Block", C_AMBER),
                ("0 TRIPS", "Safety Alarms Muted", C_CRIMSON)
            ],
            "img": "image/stuxnet_deception_engine_replay_timeline.jpg",
            "caption": "FIGURE 13.1: 65-minute comparative timeline: SCADA WinCC display vs. physical reality inside the cascade hall.",
            "notes": "Why didn't anyone press the emergency stop button? Because on the WinCC operator monitors, everything looked perfect. The pressure was optimal, vibration was flat, and all indicators were green. Stuxnet recorded 21 seconds of normal telemetry before the attack, and fed that loop back to the SCADA system throughout the sabotage."
        },
        # Slide 14
        {
            "tag": "ACT 07 // PRESSURE SABOTAGE",
            "title": "The Overpressure Attack: Valve Sabotage",
            "subtitle": "Suffocating Rotors with Uranium Hexafluoride (UF6) Overpressure",
            "bullets_title": "Stuxnet 0.5: The Gas Valve Sequence",
            "bullets": [
                "The Siemens S7-417 Controller: Managed gas piping, isolation valves, and vacuum exhaust for cascades.",
                "Closing the Valves: Systematically closed isolation and exhaust valves on active centrifuge cascades.",
                "Pressure Buildup: Uranium hexafluoride (UF6) gas accumulated inside the centrifuge cylinder, increasing internal pressure.",
                "Molecular Drag: Increased pressure caused massive aerodynamic drag on the rotor spinning at Mach 1.5, generating extreme heat.",
                "Gas Solidification: Pressure spikes caused UF6 gas to desublimate into solid crystals, unbalancing rotors and destroying bearings."
            ],
            "stats": [
                ("SIEMENS S7-417", "Heavy Industrial PLC", C_CYAN),
                ("UF6 GAS", "Uranium Hexafluoride", C_AMBER),
                ("DESUBLIMATION", "Solid Crystal Crash", C_CRIMSON)
            ],
            "img": "image/siemens_simatic_s7_400_hardware.jpg",
            "caption": "FIGURE 14.1: Siemens SIMATIC S7-400 controller targeted by Stuxnet 0.5 for cascade gas valve manipulation.",
            "notes": "Most people only know about Stuxnet's motor speed attack. But historical reverse-engineering of Stuxnet version 0.5 revealed a complementary attack targeting the Siemens S7-400 PLCs governing the gas valves. By closing exhaust valves, Stuxnet caused UF6 gas pressure to surge. At supersonic speeds, gas drag generates enormous friction."
        },
        # Slide 15
        {
            "tag": "ACT 08 // THE ESCAPE",
            "title": "The Outbreak: Escape into the Wild",
            "subtitle": "Aggressive Propagation Variants, Global Spread, and the Minsk Discovery",
            "bullets_title": "The Unintended Outbreak",
            "bullets": [
                "The Fatal Update: In early 2010, an aggressive variant incorporating the Print Spooler exploit (MS10-061) was released.",
                "Leaking the Air Gap: A contractor plugged their laptop into Natanz and then an internet-connected home office.",
                "Global Infection Distribution (July 2010): Iran (58.8%), Indonesia (18.2%), India (8.3%), Azerbaijan (2.6%), USA (1.6%).",
                "The Minsk Anomaly: In June 2010, an Iranian client PC in Minsk, Belarus experienced infinite blue-screen crash loops.",
                "Discovery by VirusBlokAda: Sergey Ulasen and Oleg Kupreev isolated ~WTR4141.tmp and discovered the LNK zero-day."
            ],
            "stats": [
                ("58.8% IRAN", "Infection Ground Zero", C_CRIMSON),
                ("18.2% INDONESIA", "Secondary Spread", C_AMBER),
                ("VIRUSBLOKADA", "Minsk Discovery Team", C_CYAN)
            ],
            "img": "image/stuxnet_global_investigation_and_forensics.jpg",
            "caption": "FIGURE 15.1: Global infection distribution and timeline leading to discovery in Minsk, Belarus.",
            "notes": "How did Stuxnet get caught? An aggressive propagation variant was loaded in 2010. A contractor carried an infected laptop home, connected to the internet, and the worm spread virally across the globe. Over 58% of all infections were centered in Iran. In Minsk, Belarus, VirusBlokAda investigated a customer's computer stuck in a reboot loop."
        },
        # Slide 16
        {
            "tag": "ACT 09 // REVERSE ENGINEERING",
            "title": "Reverse Engineering: Cracking the Code",
            "subtitle": "How Global Researchers Assembled the Pieces of the Stuxnet Puzzle",
            "bullets_title": "The Forensic Investigation",
            "bullets": [
                "Symantec Core Team: Liam O'Murchu, Eric Chien, and Nicolas Falliere spent six months reconstructing the 500 KB binary.",
                "Ralph Langner's Epiphany: German ICS consultant Ralph Langner recognized Siemens MC7 assembly commands and frequency parameters.",
                "The Sabotage Realization: 'This is not a corporate espionage tool. It is looking for frequency drives to destroy centrifuges!'",
                "Operation Olympic Games: In 2012, investigative reporting confirmed Stuxnet was a joint US-Israeli program (NSA, CIA, Unit 8200).",
                "Interdisciplinary Forensics: Required Windows kernel specialists, industrial automation engineers, and nuclear physicists."
            ],
            "stats": [
                ("SYMANTEC", "6-Month Code Analysis", C_CYAN),
                ("RALPH LANGNER", "Decoded PLC Sabotage", C_AMBER),
                ("OLYMPIC GAMES", "US-Israeli Intelligence", C_CRIMSON)
            ],
            "img": "image/stuxnet_global_investigation_and_forensics.jpg",
            "caption": "FIGURE 16.1: Global forensic timeline: VirusBlokAda, Symantec, Ralph Langner, and Kaspersky reverse-engineering teams.",
            "notes": "When security analysts first looked at Stuxnet, they were baffled. Why did it have 500 kilobytes of code—twenty times larger than typical malware? It wasn't until Ralph Langner recognized the Siemens MC7 assembly commands and frequency parameters that the world realized: someone had written software to physically attack a uranium enrichment plant."
        },
        # Slide 17
        {
            "tag": "ACT 09 // THREAT FRAMEWORK",
            "title": "MITRE ATT&CK for ICS: Stuxnet Matrix",
            "subtitle": "Tactics, Techniques & Procedures (TTPs) of an Advanced Cyber Weapon",
            "bullets_title": "Enterprise & ICS Tactics Breakdown",
            "bullets": [
                "Initial Access: T0847 (Replication Through Removable Media), T0865 (Supply Chain).",
                "Execution: T0807 (Command-Line Interface), T0833 (Modify Controller Tasking).",
                "Persistence: T0839 (Module Firmware/Logic Modification), T0859 (Valid Digital Certificates).",
                "Evasion: T0820 (Exploitation for Evasion), T0851 (Rootkit / DLL Proxy), T0856 (Spoof Reporting Message).",
                "Impair Control & Impact: T0836 (Modify Parameter), T0855 (Unauthorized Command), T0879 (Damage to Property).",
                "Birth of ICS Matrix: Stuxnet's tradecraft served as the foundational blueprint for creating the MITRE ATT&CK for ICS matrix."
            ],
            "stats": [
                ("10 TACTICS", "MITRE ICS Breakdown", C_CYAN),
                ("T0856 SPOOF", "Reporting Message", C_AMBER),
                ("T0879 DAMAGE", "Property Destruction", C_CRIMSON)
            ],
            "img": "image/stuxnet_purdue_model_deep_dive.jpg",
            "caption": "FIGURE 17.1: Mapping Stuxnet's tactical lifecycle across the Purdue industrial levels.",
            "notes": "Today, every security operations center relies on the MITRE ATT&CK framework. But in 2010, the IT matrix didn't have categories for 'Modify Controller Tasking' or 'Spoof Reporting Message'. Stuxnet forced the cybersecurity industry to invent MITRE ATT&CK for ICS."
        },
        # Slide 18
        {
            "tag": "ACT 10 // BLUE TEAM DEFENSE",
            "title": "OT Detection Engineering & Playbooks",
            "subtitle": "Suricata Signatures, Workstation Baselines & Out-of-Band Telemetry",
            "bullets_title": "4-Tier Defensive Hardening Architecture",
            "bullets": [
                "1. Network DPI: Monitor S7comm over Port 102. Alert on Function 0x1A (Download Block) outside maintenance windows.",
                "2. Workstation FIM: Cryptographically hash all DLLs in %ProgramFiles%\\Siemens\\Step7\\S7BIN\\ to detect s7otbxdx.dll tampering.",
                "3. Controller Memory Verification: Implement out-of-band automated memory hashing comparing active PLC blocks against golden Git repos.",
                "4. Out-of-Band Physical Sensors: Mount independent vibration and acoustic sensors wired to an isolated analog recorder bypassing the PLC!",
                "Ground Truth Principle: When digital SCADA screens can be spoofed by man-in-the-middle replays, only physics provides reality."
            ],
            "stats": [
                ("SURICATA DPI", "Port 102 Inspection", C_CYAN),
                ("FIM HASHING", "s7otbxdx.dll Baselines", C_AMBER),
                ("PHYSICAL SENSORS", "Out-of-Band Verification", C_EMERALD)
            ],
            "img": "image/stuxnet_scada_plc_network_architecture.jpg",
            "caption": "FIGURE 18.1: Defensive sensor placement across Level 1 and Level 2 industrial networks.",
            "notes": "How do we stop the next Stuxnet? We cannot rely solely on the engineering workstation's screen, because that screen can be spoofed. We need defense in depth: Deep Packet Inspection of industrial protocols on Port 102, cryptographic hashing of STEP 7 libraries, and most importantly: out-of-band physical sensors."
        },
        # Slide 19
        {
            "tag": "ACT 10 // EVOLUTION & THREAT LANDSCAPE",
            "title": "The Weaponized ICS Dynasty (2010-2026)",
            "subtitle": "From Stuxnet to PIPEDREAM: The Evolution of Industrial Cyber Warfare",
            "bullets_title": "The Lineage of Kinetic Malware",
            "bullets": [
                "2010 // STUXNET: First kinetic malware; targeted Siemens PLCs to destroy uranium centrifuges.",
                "2011-2012 // DUQU & FLAME: Modular cyber-reconnaissance platforms sharing Stuxnet's Tilded platform framework.",
                "2015 // BLACKENERGY 3: First cyberattack to cause an electrical blackout; shut down 30 substations in Ukraine.",
                "2016 // INDUSTROYER: Automated malware directly speaking IEC 60870-5-104 and IEC 61850 substation protocols.",
                "2017 // TRITON / TRISIS: First attack targeting Safety Instrumented Systems (Schneider Triconex) in a petrochemical plant.",
                "2022 // PIPEDREAM: Modular, multi-vendor toolkit capable of targeting Omron, Schneider PLCs, and OPC UA worldwide."
            ],
            "stats": [
                ("2010 STUXNET", "Centrifuge Destruction", C_CYAN),
                ("2015 BLACKENERGY", "Grid Blackout (Ukraine)", C_AMBER),
                ("2017 TRITON", "Safety Systems (SIS)", C_CRIMSON)
            ],
            "img": "image/stuxnet_how_it_worked_infographic.jpg",
            "caption": "FIGURE 19.1: Evolution from bespoke single-target malware to modular cross-industry ICS attack frameworks.",
            "notes": "Stuxnet was the Wright Brothers' plane of cyber-physical weapons. In the 16 years since, we have seen that primitive biplane evolve into supersonic fighter jets. In 2015, BlackEnergy cut power to 225,000 citizens. In 2017, Triton attacked Safety Instrumented Systems in a refinery. The threat has generalized to every critical infrastructure sector."
        },
        # Slide 20
        {
            "tag": "ACT 10 // CONCLUSION & SIMULATION",
            "title": "Conclusion & Tabletop Simulation",
            "subtitle": "Key Seminar Takeaways & Launching 'Operation Centrifuge Shadow'",
            "bullets_title": "3 Enduring Seminar Lessons",
            "bullets": [
                "1. The Air Gap is an Operational Delusion: Physical isolation is routinely bridged by human routines and removable media.",
                "2. Physics is the Ground Truth: Digital SCADA displays can be deceived; only out-of-band physical telemetry provides reality.",
                "3. Code Can Bend Steel: Cybersecurity is no longer an IT support function—it is a matter of safety and physical defense.",
                "Tabletop Exercise Kickoff: Veritas Chemical & Separation Facility (Centrifuge Cascade Unit 4).",
                "Simulation Injects: Inject 1 (USB Calibration) -> Inject 2 (S7comm Alert) -> Inject 3 (Telemetry Lag) -> Inject 4 (Trip Failure)."
            ],
            "stats": [
                ("ASSUME BREACH", "Air Gap Principle", C_CYAN),
                ("OUT-OF-BAND", "Ground Truth Rule", C_EMERALD),
                ("OPERATION CENTRIFUGE", "Tabletop Exercise TTX", C_CRIMSON)
            ],
            "img": "image/natanz_underground_site_overview.jpg",
            "caption": "FIGURE 20.1: Operation Centrifuge Shadow Tabletop Simulation scenario environment.",
            "notes": "To conclude our seminar: Stuxnet taught us that cybersecurity is not about firewalls and antivirus—it is about physical reality. Air gaps do not protect you if your contractors plug in USB drives. Screens cannot be trusted without out-of-band sensors. And software can bend steel. Now, we will transition into our interactive Tabletop Exercise: 'Operation Centrifuge Shadow'."
        }
    ]

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for idx, data in enumerate(slides_data, start=1):
        slide = prs.slides.add_slide(blank_layout)

        # 1. Background (shape 0)
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_BG
        bg.line.fill.background()

        # 2. Top Header Accent Line
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.035))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_CYAN
        top_bar.line.fill.background()

        # 3. Top Tag & Meta Pill
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.48), Inches(8.0), Inches(0.3))
        tf_tag = tag_box.text_frame
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = f"{data['tag']}  //  SLIDE {idx:02d} OF 20"
        p_tag.font.size = Pt(9.5)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_CYAN

        # 4. Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(10.5), Inches(0.55))
        tf_title = title_box.text_frame
        p_title = tf_title.paragraphs[0]
        p_title.text = data["title"]
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE

        # 5. Slide Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.32), Inches(11.733), Inches(0.35))
        tf_sub = sub_box.text_frame
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = data["subtitle"]
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = C_MUTED

        # 6. Left Column: Main Bullet Card
        card_l = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.75), Inches(5.7), Inches(3.7))
        card_l.fill.solid()
        card_l.fill.fore_color.rgb = C_CARD
        card_l.line.color.rgb = C_BORDER
        card_l.line.width = Pt(1)

        # Card Title
        ct_box = slide.shapes.add_textbox(Inches(1.0), Inches(1.85), Inches(5.3), Inches(0.35))
        tf_ct = ct_box.text_frame
        p_ct = tf_ct.paragraphs[0]
        p_ct.text = data["bullets_title"]
        p_ct.font.size = Pt(12.5)
        p_ct.font.bold = True
        p_ct.font.color.rgb = C_WHITE

        # Bullets
        b_box = slide.shapes.add_textbox(Inches(1.0), Inches(2.25), Inches(5.3), Inches(3.0))
        tf_b = b_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = Inches(0.0)
        tf_b.margin_right = Inches(0.0)
        tf_b.margin_top = Inches(0.0)

        for b_idx, b_text in enumerate(data["bullets"]):
            p = tf_b.paragraphs[0] if b_idx == 0 else tf_b.add_paragraph()
            p.text = f"•  {b_text}"
            p.font.size = Pt(10)
            p.font.color.rgb = C_TEXT
            p.space_after = Pt(6)

        # 7. Left Column: Compact Stats Row (Under Card)
        stat_shapes = []
        num_stats = len(data["stats"])
        stat_w = (Inches(5.7) - (Inches(0.12) * (num_stats - 1))) / num_stats
        for s_idx, (val, lbl, color) in enumerate(data["stats"]):
            s_left = Inches(0.8) + (stat_w + Inches(0.12)) * s_idx
            sc = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, s_left, Inches(5.6), stat_w, Inches(1.2))
            sc.fill.solid()
            sc.fill.fore_color.rgb = C_CARD
            sc.line.color.rgb = C_BORDER
            sc.line.width = Pt(1)
            stat_shapes.append(sc)

            s_box = slide.shapes.add_textbox(s_left + Inches(0.05), Inches(5.68), stat_w - Inches(0.1), Inches(1.0))
            tf_s = s_box.text_frame
            tf_s.word_wrap = True
            tf_s.margin_top = Inches(0)
            tf_s.margin_bottom = Inches(0)
            tf_s.margin_left = Inches(0)
            tf_s.margin_right = Inches(0)

            p_val = tf_s.paragraphs[0]
            p_val.text = val
            p_val.font.size = Pt(11)
            p_val.font.bold = True
            p_val.font.color.rgb = color
            p_val.alignment = PP_ALIGN.CENTER

            p_lbl = tf_s.add_paragraph()
            p_lbl.text = lbl
            p_lbl.font.size = Pt(8.5)
            p_lbl.font.color.rgb = C_MUTED
            p_lbl.alignment = PP_ALIGN.CENTER
            p_lbl.space_before = Pt(2)

        # 8. Right Column: Graphic/Diagram Frame
        card_r = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.75), Inches(5.733), Inches(5.05))
        card_r.fill.solid()
        card_r.fill.fore_color.rgb = C_CARD
        card_r.line.color.rgb = C_BORDER
        card_r.line.width = Pt(1)

        # Embed properly scaled & centered image
        img_full_path = os.path.join(base_dir, data["img"])
        if os.path.exists(img_full_path):
            try:
                with Image.open(img_full_path) as im:
                    orig_w, orig_h = im.size
                
                # Card image canvas bounds
                max_w = Inches(5.333)
                max_h = Inches(4.15)
                aspect = orig_w / orig_h
                
                # Calculate fitted dimensions
                target_w = max_w
                target_h = target_w / aspect
                if target_h > max_h:
                    target_h = max_h
                    target_w = target_h * aspect

                # Centered coordinates inside card_r
                img_x = Inches(6.8) + (Inches(5.733) - target_w) / 2
                img_y = Inches(1.9) + (max_h - target_h) / 2
                
                pic = slide.shapes.add_picture(img_full_path, img_x, img_y, width=target_w, height=target_h)
            except Exception as e:
                pass

        # Caption Bar at bottom of card_r
        cap_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.82), Inches(6.25), Inches(5.693), Inches(0.53))
        cap_bar.fill.solid()
        cap_bar.fill.fore_color.rgb = RGBColor(14, 21, 35)
        cap_bar.line.fill.background()

        cap_box = slide.shapes.add_textbox(Inches(6.85), Inches(6.28), Inches(5.633), Inches(0.45))
        tf_cap = cap_box.text_frame
        tf_cap.word_wrap = True
        tf_cap.margin_top = Inches(0)
        tf_cap.margin_bottom = Inches(0)
        p_cap = tf_cap.paragraphs[0]
        p_cap.text = data["caption"]
        p_cap.font.size = Pt(8.5)
        p_cap.font.color.rgb = C_MUTED
        p_cap.alignment = PP_ALIGN.CENTER

        # 9. Bottom Footer Bar
        foot_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.98), Inches(11.733), Inches(0.015))
        foot_bar.fill.solid()
        foot_bar.fill.fore_color.rgb = C_BORDER
        foot_bar.line.fill.background()

        foot_left = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(8.0), Inches(0.3))
        tf_fl = foot_left.text_frame
        p_fl = tf_fl.paragraphs[0]
        p_fl.text = "STUXNET: CYBER-PHYSICAL KINETIC SABOTAGE  //  MASTERCLASS CURRICULUM"
        p_fl.font.size = Pt(8)
        p_fl.font.color.rgb = C_DIM

        foot_right = slide.shapes.add_textbox(Inches(9.5), Inches(7.05), Inches(3.033), Inches(0.3))
        tf_fr = foot_right.text_frame
        p_fr = tf_fr.paragraphs[0]
        p_fr.text = f"CONFIDENTIAL CASE STUDY  |  SLIDE {idx:02d} / 20"
        p_fr.font.size = Pt(8)
        p_fr.font.color.rgb = C_DIM
        p_fr.alignment = PP_ALIGN.RIGHT

        # 10. Presenter Speaker Notes
        slide.notes_slide.notes_text_frame.text = data["notes"]

        # 11. Native OpenXML Slide Transition (<p:transition>)
        tr_xml = parse_xml(
            '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med" advClick="1">'
            '<p:fade/>'
            '</p:transition>'
        )
        slide._element.append(tr_xml)

        # 12. Native OpenXML Shape Entrance Animations (<p:timing>)
        # Animate the key content shapes: title_box, card_l, stats, card_r
        all_shapes = list(slide.shapes)
        # We animate the key functional visual shapes (title, cards, graphics)
        # Exclude background (shape 0)
        animated_ids = [s.shape_id for s in all_shapes[2:8]]
        if animated_ids:
            timing_xml = create_timing_xml(animated_ids)
            slide._element.append(timing_xml)

    output_file = os.path.join(base_dir, "STUXNET_Clean_Animated_Presentation_20_Slides.pptx")
    prs.save(output_file)
    print(f"Generated clean & animated presentation: {output_file} ({len(prs.slides)} slides)")
    
    # Also attempt to update STUXNET_Masterclass_Seminar_20_Slides.pptx if not locked
    primary_file = os.path.join(base_dir, "STUXNET_Masterclass_Seminar_20_Slides.pptx")
    try:
        prs.save(primary_file)
        print(f"Also updated: {primary_file}")
    except Exception as e:
        print(f"Note: {primary_file} is currently open in PowerPoint ({e}); clean animated version saved to {output_file}")
        
    return output_file

if __name__ == '__main__':
    build_clean_animated_pptx()
