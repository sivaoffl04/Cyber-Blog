"""
Generates STUXNET_Masterclass_Seminar_20_Slides.pptx
Full 20-slide widescreen (16:9) professional PowerPoint presentation
with deep cyber/SCADA theme, high-res diagrams, formatted tables/cards,
and presenter notes for all 20 slides.
"""

import os
import sys

def create_powerpoint_presentation():
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE

    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_slide_layout = prs.slide_layouts[6] # blank layout

    # Color Palette
    COLOR_BG = RGBColor(10, 14, 23)        # #0A0E17
    COLOR_PANEL = RGBColor(19, 27, 44)     # #131B2C
    COLOR_CARD = RGBColor(16, 24, 39)      # #101827
    COLOR_BORDER = RGBColor(31, 44, 68)    # #1F2C44
    COLOR_CYAN = RGBColor(0, 240, 255)     # #00F0FF
    COLOR_CRIMSON = RGBColor(255, 51, 102) # #FF3366
    COLOR_AMBER = RGBColor(255, 184, 0)    # #FFB800
    COLOR_EMERALD = RGBColor(0, 255, 157)  # #00FF9D
    COLOR_TEXT = RGBColor(240, 244, 252)   # #F0F4FC
    COLOR_MUTED = RGBColor(139, 155, 180)  # #8B9BB4

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background() # no line
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text, slide_num):
        # Top banner line
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.04))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = COLOR_CYAN
        top_bar.line.fill.background()

        # Tag
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.48), Inches(9.0), Inches(0.3))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = f"{tag_text.upper()}  //  SLIDE {slide_num:02d} OF 20"
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_CYAN

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(10.0), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.35))
        tf_sub = sub_box.text_frame
        tf_sub.word_wrap = True
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle_text
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = COLOR_MUTED

    def add_bullet_card(slide, left, top, width, height, card_title, bullets, badge_text="", badge_color=COLOR_CYAN):
        # Card background
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        # Title Box
        title_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.4))
        tf_t = title_box.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = card_title
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_TEXT

        # Bullets
        bullets_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.6), width - Inches(0.4), height - Inches(0.7))
        tf_b = bullets_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = Inches(0.05)
        tf_b.margin_right = Inches(0.05)
        tf_b.margin_top = Inches(0.05)

        for i, b_text in enumerate(bullets):
            p = tf_b.paragraphs[0] if i == 0 else tf_b.add_paragraph()
            p.text = f"•  {b_text}"
            p.font.size = Pt(11)
            p.font.color.rgb = RGBColor(220, 228, 240)
            p.space_after = Pt(7)

    def add_image_card(slide, left, top, width, height, img_path, caption):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        if os.path.exists(img_path):
            try:
                # Add picture inside card
                slide.shapes.add_picture(img_path, left + Inches(0.2), top + Inches(0.2), width=width - Inches(0.4))
            except Exception as e:
                pass

        # Caption
        cap_box = slide.shapes.add_textbox(left + Inches(0.1), top + height - Inches(0.55), width - Inches(0.2), Inches(0.45))
        tf_c = cap_box.text_frame
        tf_c.word_wrap = True
        p_c = tf_c.paragraphs[0]
        p_c.text = caption
        p_c.font.size = Pt(9.5)
        p_c.font.color.rgb = COLOR_MUTED
        p_c.alignment = PP_ALIGN.CENTER

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        text_frame = notes_slide.notes_text_frame
        text_frame.text = notes_text

    # Data for the 20 slides
    slides_data = [
        # Slide 1
        {
            "tag": "Act 01 // Overview",
            "title": "STUXNET: The Cyber-Physical Rubicon",
            "subtitle": "Deconstructing the World's First Kinetic Industrial Weapon & The Sabotage of Natanz",
            "bullets_title": "Strategic Executive Summary",
            "bullets": [
                "Target Facility: Natanz Fuel Enrichment Plant (FEP), Iran (~8,000 IR-1 gas centrifuges).",
                "Strategic Mission: Clandestinely destroy nuclear enrichment hardware without overt kinetic warfare.",
                "Novel Weaponry: 4 simultaneous Windows zero-days, 2 stolen hardware code-signing certificates.",
                "Kinetic Result: Physical destruction of an estimated ~1,000 centrifuges via rotor overspeed and resonance.",
                "Historical Milestone: Proved that digital software instructions can bend steel and shatter industrial hardware."
            ],
            "img": "image/stuxnet_how_it_worked_infographic.jpg",
            "caption": "FIGURE 1.1: Stuxnet's end-to-end cyber-physical kill chain: USB infiltration to PLC manipulation.",
            "notes": "Welcome to the Stuxnet masterclass seminar. In June 2010, the global cybersecurity landscape fundamentally shifted. Up until that point, malware was designed to steal passwords or hold financial data hostage. Stuxnet reached out from cyberspace to physically destroy industrial hardware located 8 meters beneath the Iranian desert."
        },
        # Slide 2
        {
            "tag": "Act 01 // Geopolitics & Geography",
            "title": "The Natanz Fuel Enrichment Facility",
            "subtitle": "A Subterranean Fortress Shielded by Reinforced Concrete and Air Gaps",
            "bullets_title": "Facility Hardening & Defense",
            "bullets": [
                "Geographical Isolation: Located 300 km south of Tehran in the central desert of Isfahan Province.",
                "Subterranean Hardening: Cascade halls buried 8 meters underground beneath a 2.5-meter reinforced concrete roof.",
                "Perimeter Security: Ringed by anti-aircraft missile batteries, radar installations, and elite military guards.",
                "The Air Gap: Completely disconnected from the public Internet; zero incoming public telco fiber connections.",
                "The Geopolitical Impasse: Military airstrikes risked regional war; a covert cyber weapon was the surgical alternative."
            ],
            "img": "image/natanz_enrichment_facility_aerial.jpg",
            "caption": "FIGURE 2.1: Satellite reconnaissance of the Natanz Fuel Enrichment Plant showing subterranean cascade halls.",
            "notes": "Natanz was designed to be impervious to conventional military strikes. The cascade halls were buried 8 meters underground, capped with reinforced concrete and earth. There was no internet connection. Plant operators believed physical isolation guaranteed absolute security."
        },
        # Slide 3
        {
            "tag": "Act 01 // Paradigm Shift",
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
            "img": "image/stuxnet_natanz_centrifuges_cascade.jpg",
            "caption": "FIGURE 3.1: Cascade hall containing 164 IR-1 centrifuges spinning UF6 gas under high vacuum.",
            "notes": "The core genius of Stuxnet was psychological and kinetic warfare combined. If you bomb a facility, the enemy rebuilds it. But if their own machines silently tear themselves apart while computer monitors report normal operation, they blame their engineers and domestic suppliers."
        },
        # Slide 4
        {
            "tag": "Act 02 // Architecture",
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
            "img": "image/stuxnet_purdue_model_deep_dive.jpg",
            "caption": "FIGURE 4.1: The Purdue Enterprise Reference Architecture (PERA) showing Stuxnet's path from Level 4 to Level 0.",
            "notes": "The Purdue Model defines strict zones of trust. You never connect a Level 1 PLC directly to the internet. Firewalls and air gaps isolate Level 2 and Level 1. Stuxnet bypassed perimeter firewalls by riding the supply chain straight into Level 2 on contractor flash drives."
        },
        # Slide 5
        {
            "tag": "Act 02 // Initial Access",
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
            "img": "image/stuxnet_scada_plc_network_architecture.jpg",
            "caption": "FIGURE 5.1: SCADA and PLC industrial network topology illustrating lateral propagation.",
            "notes": "An air gap is only as secure as the people who maintain it. Stuxnet did not need an internet cable. The attackers targeted third-party integration contractors. When a technician plugged a calibration laptop into the Level 2 switch at Natanz, Stuxnet hopped the air gap in seconds."
        },
        # Slide 6
        {
            "tag": "Act 03 // Vulnerability Exploitation",
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
            "img": "image/stuxnet_windows_zero_days_internals.jpg",
            "caption": "FIGURE 6.1: Dissection of Stuxnet's 4 zero-days and dual code-signing certificate compromise.",
            "notes": "Prior to 2010, the security industry had never seen a piece of malware armed with four distinct zero-days. In the commercial exploit broker market, this represents millions of dollars. It was definitive proof of a well-funded nation-state intelligence apparatus at work."
        },
        # Slide 7
        {
            "tag": "Act 03 // Cryptographic Evasion",
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
            "img": "image/stuxnet_windows_zero_days_internals.jpg",
            "caption": "FIGURE 7.1: Driver Signature Enforcement bypass using stolen Realtek and JMicron digital certificates.",
            "notes": "Why didn't antivirus catch Stuxnet? Because Stuxnet carried legitimate, cryptographically valid signatures from Realtek and JMicron. The attackers didn't crack RSA-2048 cryptography; they hacked the software supply chain to steal the private keys."
        },
        # Slide 8
        {
            "tag": "Act 03 // Rootkit & Stealth",
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
            "img": "image/stuxnet_step7_dll_proxy_architecture.jpg",
            "caption": "FIGURE 8.1: Kernel memory injection and DLL proxying architecture.",
            "notes": "Stuxnet's authors exhibited extraordinary operational discipline. They implemented an in-memory virtual file system and hooked kernel directory calls so their exploit files were literally invisible. They even built in an infection hop counter: after 3 machines, the USB stopped spreading."
        },
        # Slide 9
        {
            "tag": "Act 04 // Target Identification",
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
            "img": "image/stuxnet_natanz_centrifuges_cascade.jpg",
            "caption": "FIGURE 9.1: The 164-centrifuge cascade hall at Natanz matching Stuxnet's exact hardware profile.",
            "notes": "Imagine releasing a weapon that can only infect someone who is exactly 6 feet tall, has blue eyes, and wears a red tie. That is what Stuxnet did in software. If a machine did not match all six hardware criteria, Stuxnet did nothing. It was laser-guided."
        },
        # Slide 10
        {
            "tag": "Act 04 // Engineering Man-in-the-Middle",
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
            "img": "image/stuxnet_step7_dll_proxy_architecture.jpg",
            "caption": "FIGURE 10.1: Architecture of Stuxnet's DLL proxy hooking STEP 7 communication between EWS and PLC.",
            "notes": "Even if an engineer connected their laptop directly to the PLC and asked STEP 7: 'Show me what code is running on this controller', Stuxnet's hooked DLL intercepted the query, filtered out its own malicious blocks, and presented a clean copy. The engineer had no idea the PLC was compromised."
        },
        # Slide 11
        {
            "tag": "Act 05 // PLC Internals",
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
            "img": "image/stuxnet_siemens_s7_mc7_bytecode_injection.jpg",
            "caption": "FIGURE 11.1: Microcode injection layout inside S7 CPU memory hooking OB1/OB35 cyclic loops.",
            "notes": "A PLC doesn't run Python or C; it runs a compiled microcode called MC7. Stuxnet was the first malware in history to carry an MC7 compiler. It injected new Function Blocks directly into PLC memory and hooked OB1—the cyclic heartbeat of the industrial controller."
        },
        # Slide 12
        {
            "tag": "Act 06 // Kinetic Physics Sabotage",
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
            "img": "image/stuxnet_centrifuge_rotor_physics_breakdown.jpg",
            "caption": "FIGURE 12.1: Physical stress breakdown of IR-1 rotor overspeed and harmonic resonance modes.",
            "notes": "At nominal speed, 1,064 Hz, the centrifuge spins safely. But during the overspeed phase, Stuxnet boosted the frequency to 1,410 Hz—pushing the aluminum rotor past its mechanical limit. Then, 27 days later, Stuxnet dropped the frequency to 2 Hz. In physics, when an object with high inertia slows down, it passes through its critical harmonic resonance frequencies. The rotor wobbled and struck the casing."
        },
        # Slide 13
        {
            "tag": "Act 07 // Sensor Deception",
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
            "img": "image/stuxnet_deception_engine_replay_timeline.jpg",
            "caption": "FIGURE 13.1: 65-minute comparative timeline: SCADA WinCC display vs. physical reality inside the cascade hall.",
            "notes": "Why didn't anyone press the emergency stop button? Because on the WinCC operator monitors, everything looked perfect. The pressure was optimal, vibration was flat, and all indicators were green. Stuxnet recorded 21 seconds of normal telemetry before the attack, and fed that loop back to the SCADA system throughout the sabotage."
        },
        # Slide 14
        {
            "tag": "Act 07 // Pressure Sabotage",
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
            "img": "image/siemens_simatic_s7_400_hardware.jpg",
            "caption": "FIGURE 14.1: Siemens SIMATIC S7-400 controller targeted by Stuxnet 0.5 for cascade gas valve manipulation.",
            "notes": "Most people only know about Stuxnet's motor speed attack. But historical reverse-engineering of Stuxnet version 0.5 revealed a complementary attack targeting the Siemens S7-400 PLCs governing the gas valves. By closing exhaust valves, Stuxnet caused UF6 gas pressure to surge. At supersonic speeds, gas drag generates enormous friction."
        },
        # Slide 15
        {
            "tag": "Act 08 // The Escape",
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
            "img": "image/stuxnet_global_investigation_and_forensics.jpg",
            "caption": "FIGURE 15.1: Global infection distribution and timeline leading to discovery in Minsk, Belarus.",
            "notes": "How did Stuxnet get caught? An aggressive propagation variant was loaded in 2010. A contractor carried an infected laptop home, connected to the internet, and the worm spread virally across the globe. Over 58% of all infections were centered in Iran. In Minsk, Belarus, VirusBlokAda investigated a customer's computer stuck in a reboot loop."
        },
        # Slide 16
        {
            "tag": "Act 09 // Reverse Engineering",
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
            "img": "image/stuxnet_global_investigation_and_forensics.jpg",
            "caption": "FIGURE 16.1: Global forensic timeline: VirusBlokAda, Symantec, Ralph Langner, and Kaspersky reverse-engineering teams.",
            "notes": "When security analysts first looked at Stuxnet, they were baffled. Why did it have 500 kilobytes of code—twenty times larger than typical malware? It wasn't until Ralph Langner recognized the Siemens MC7 assembly commands and frequency parameters that the world realized: someone had written software to physically attack a uranium enrichment plant."
        },
        # Slide 17
        {
            "tag": "Act 09 // Threat Framework",
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
            "img": "image/stuxnet_purdue_model_deep_dive.jpg",
            "caption": "FIGURE 17.1: Mapping Stuxnet's tactical lifecycle across the Purdue industrial levels.",
            "notes": "Today, every security operations center relies on the MITRE ATT&CK framework. But in 2010, the IT matrix didn't have categories for 'Modify Controller Tasking' or 'Spoof Reporting Message'. Stuxnet forced the cybersecurity industry to invent MITRE ATT&CK for ICS."
        },
        # Slide 18
        {
            "tag": "Act 10 // Blue Team Defense",
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
            "img": "image/stuxnet_scada_plc_network_architecture.jpg",
            "caption": "FIGURE 18.1: Defensive sensor placement across Level 1 and Level 2 industrial networks.",
            "notes": "How do we stop the next Stuxnet? We cannot rely solely on the engineering workstation's screen, because that screen can be spoofed. We need defense in depth: Deep Packet Inspection of industrial protocols on Port 102, cryptographic hashing of STEP 7 libraries, and most importantly: out-of-band physical sensors."
        },
        # Slide 19
        {
            "tag": "Act 10 // Evolution & Threat Landscape",
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
            "img": "image/stuxnet_how_it_worked_infographic.jpg",
            "caption": "FIGURE 19.1: Evolution from bespoke single-target malware to modular cross-industry ICS attack frameworks.",
            "notes": "Stuxnet was the Wright Brothers' plane of cyber-physical weapons. In the 16 years since, we have seen that primitive biplane evolve into supersonic fighter jets. In 2015, BlackEnergy cut power to 225,000 citizens. In 2017, Triton attacked Safety Instrumented Systems in a refinery. The threat has generalized to every critical infrastructure sector."
        },
        # Slide 20
        {
            "tag": "Act 10 // Conclusion & Simulation",
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
            "img": "image/natanz_underground_site_overview.jpg",
            "caption": "FIGURE 20.1: Operation Centrifuge Shadow Tabletop Simulation scenario environment.",
            "notes": "To conclude our seminar: Stuxnet taught us that cybersecurity is not about firewalls and antivirus—it is about physical reality. Air gaps do not protect you if your contractors plug in USB drives. Screens cannot be trusted without out-of-band sensors. And software can bend steel. Now, we will transition into our interactive Tabletop Exercise: 'Operation Centrifuge Shadow'."
        }
    ]

    # Generate each slide
    for idx, data in enumerate(slides_data, start=1):
        slide = prs.slides.add_slide(blank_slide_layout)
        add_background(slide)
        add_header(slide, data["tag"], data["title"], data["subtitle"], idx)

        # Left Column: Bullet Card
        add_bullet_card(slide, Inches(0.8), Inches(1.8), Inches(6.2), Inches(5.1), data["bullets_title"], data["bullets"])

        # Right Column: Image Card
        img_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), data["img"])
        add_image_card(slide, Inches(7.2), Inches(1.8), Inches(5.333), Inches(5.1), img_full_path, data["caption"])

        # Speaker Notes
        add_notes(slide, data["notes"])

    # Output file path
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_pptx = os.path.join(root_dir, "STUXNET_Masterclass_Seminar_20_Slides.pptx")
    prs.save(output_pptx)
    print(f"Successfully generated PowerPoint presentation: {output_pptx}")
    return output_pptx

if __name__ == "__main__":
    create_powerpoint_presentation()
