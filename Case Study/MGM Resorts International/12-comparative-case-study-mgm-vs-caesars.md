# Chapter 12: Comparative Case Study — MGM Resorts vs. Caesars Entertainment

> **Seminar Module:** Strategic Decision-Making Under Extortion & The Twin Vegas Breaches  
> **Target Audience:** Board Members, Chief Executive Officers, Chief Legal Officers, CISOs, Risk Committees  
> **The Parallel Breaches:** August–September 2023 Gaming Industry Cyber Campaign

---

## 1. The Tale of Two Casinos: Same Threat Actor, Opposite Strategies

In late summer 2023, the Las Vegas gaming and hospitality corridor experienced an unprecedented coordinated cyber offensive. The exact same threat actor collective—**Scattered Spider (UNC3944)**—targeted both of the Strip's dominant titans within weeks of each other:
1. **Caesars Entertainment** (Targeted August 2023)
2. **MGM Resorts International** (Targeted September 2023)

Both organizations were compromised using virtually identical initial access tradecraft: **social engineering and voice phishing targeting IT help desks**.

However, the strategic responses executed by the executive leadership and boards of directors of these two corporations diverged completely, creating the most compelling real-world comparative case study in corporate cybersecurity history.

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                     THE STRATEGIC DIVERGENCE: VEGAS 2023                         │
├────────────────────────────────────────┬─────────────────────────────────────────┤
│          CAESARS ENTERTAINMENT         │        MGM RESORTS INTERNATIONAL        │
├────────────────────────────────────────┼─────────────────────────────────────────┤
│ • Targeted: Late August 2023           │ • Targeted: Early September 2023        │
│ • Initial Vector: Outsourced IT vendor │ • Initial Vector: Internal IT Help Desk │
│   support desk social engineering      │   vishing targeting Okta Admin          │
│ • Strategy: Pragmatic Capitulation     │ • Strategy: Total Refusal / Isolation   │
│ • Ransom Decision: PAID ~$15 MILLION   │ • Ransom Decision: PAID $0 (REFUSED)    │
│ • Operational Uptime: 100% Online      │ • Operational Uptime: Catastrophic Down │
│ • Financial Impact: ~$15M direct cost  │ • Financial Impact: ~$100M EBITDAR loss │
│ • Public Visibility: Low / Quiet       │ • Public Visibility: Viral Public Crisis│
└────────────────────────────────────────┴─────────────────────────────────────────┘
```

---

## 2. Caesars Entertainment: The Economics of Capitulation

In late August 2023, Scattered Spider compromised an external outsourced IT support vendor utilized by Caesars. Using this access, the threat actors penetrated Caesars' loyalty program database, exfiltrating tens of millions of customer driver's license and Social Security numbers.

### The Corporate Calculation
When presented with the extortion demand, Caesars' executive leadership evaluated the operational realities:
* Caesars operates 50+ properties with millions of casino rewards members.
* A complete operational shutdown would cost tens of millions of dollars per week in lost gaming, hotel, and dining revenue.
* The attackers offered a verifiable agreement: pay the ransom, receive assurances that the stolen data would be suppressed, and avoid destructive hypervisor encryption.

Caesars reportedly negotiated the ransom down to approximately **$15 million in cryptocurrency** and paid the extortionists. 

### The Operational Result
To the casual casino patron walking through Caesars Palace, the Paris, or the Flamingo, **nothing appeared amiss**:
* Slot machines continued spinning and accepting cash.
* Hotel key cards functioned normally.
* Website and mobile app reservations remained fully operational.
* Caesars disclosed the incident quietly in an SEC Form 8-K filing on September 14, 2023, noting that customer loyalty data had been stolen but business operations had continued uninterrupted.

---

## 3. MGM Resorts International: The Cost of Principle and Isolation

Weeks later, when Scattered Spider penetrated MGM's Okta environment and brought in ALPHV/BlackCat to deploy ransomware, MGM took the opposite path:
* **MGM refused to negotiate or pay the ransom demand.**
* **MGM executed immediate "scorched earth" infrastructure severance**, proactively isolating internal networks and cloud connectors.

### The Operational Result
MGM stood firmly on corporate principle and compliance with federal law enforcement recommendations (the FBI advises victims never to pay ransomware demands). However, the immediate operational consequences were brutal:
* 31 properties suffered severe operational paralysis for over a week.
* Front desk lobbies descended into chaos with multi-hour lines.
* Slot machines went dark across the Las Vegas Strip.
* MGM absorbed a verified **$100 million negative impact to Adjusted Property EBITDAR**.

---

## 4. Comprehensive Comparative Matrix

| Evaluation Dimension | Caesars Entertainment | MGM Resorts International | Strategic Assessment |
| :--- | :--- | :--- | :--- |
| **Initial Intrusion Vector** | Vishing outsourced vendor help desk | Vishing internal IT service desk | Identical vulnerability in human verification |
| **Data Compromised** | Massive customer loyalty database (PII, SSNs, Driver's Licenses) | Customer PII (Names, Contact, DOB; small subset of SSNs/Passports) | Both suffered significant customer PII loss |
| **Ransom Demanded** | ~$30 Million | ~$30+ Million | Similar extortion thresholds |
| **Ransom Paid** | **~$15 Million (Paid)** | **$0 (Refused)** | Diametrically opposed board strategies |
| **Direct Financial Impact** | ~$15 Million ransom + legal expenses | ~$100 Million EBITDAR loss + <$10M IR expenses | Caesars saved ~$85M in short-term financial loss |
| **Operational Availability** | Maintained 100% uptime; zero physical disruptions | 10+ days of severe operational disruptions | Caesars avoided public operational paralysis |
| **Reputational Impact** | Minimal public awareness; seen as managed | Viral public crisis; extensive media headlines | MGM suffered intense public brand scrutiny |
| **Legal & Regulatory Risk** | Facing multiple class-action lawsuits | Facing multiple class-action lawsuits & FTC inquiry | Both face identical post-breach litigation |
| **Moral Hazard / Future Risk** | High: Funded cybercriminals; painted target on back | Low: Proven unwilling to pay extortionists | MGM eliminated extortion incentives |
| **Infrastructure Hygiene** | Restored or maintained with adversary footprint | Full clean-slate forensic rebuild of core systems | MGM achieved higher verified security assurance |

---

## 5. The Executive Debate: Fiduciary Duty vs. Moral Hazard

The twin casino breaches represent the quintessential modern corporate cybersecurity paradox, frequently debated in executive MBA programs and boardroom crisis simulations:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           THE BOARDROOM DILEMMA                                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   ARGUMENT FOR CAESARS STRATEGY (PRAGMATIC REALISM):                            │
│   "The primary fiduciary duty of corporate directors is to protect shareholder  │
│    value and ensure enterprise continuity. Spending $15 million to prevent a    │
│    $100 million operational catastrophe and preserve customer experience is a   │
│    rational, defensible financial decision."                                    │
│                                                                                 │
│   ARGUMENT FOR MGM STRATEGY (PRINCIPLED RESILIENCE):                            │
│   "Paying ransoms fuels the cybercrime economy, finances future attacks against │
│    our peers, provides zero legal guarantee that data won't be leaked anyway,   │
│    and paints a target on the company's back for repeat extortion. Refusing to  │
│    pay and executing a clean rebuild is the only sustainable long-term defense."│
└─────────────────────────────────────────────────────────────────────────────────┘
```

### The Unspoken Risks of Paying (The Caesars Strategy)
1. **The Criminal Honor Fallacy:** Threat actors frequently retain copies of stolen data and re-extort victims months later, or sell the records privately despite payment.
2. **OFAC Sanctions Liability:** Paying ransoms to designated cybercrime syndicates carries severe regulatory risks under the U.S. Department of the Treasury's Office of Foreign Assets Control (OFAC).
3. **Repeat Targeting:** Cybercriminal forums track which corporations pay. An organization known to have paid $15 million becomes an irresistible target for competing cybercrime syndicates.

---

## 6. Seminar Discussion Questions

1. **The Shareholder Lawsuit Question:** If you were a major institutional shareholder in MGM Resorts, would you sue the board for losing $100M when a $15M payment could have prevented the outage, or would you commend the board for ethical governance?
2. **The Ransom Negotiation Protocol:** If a corporation decides to negotiate, what forensic guarantees must exist before cryptocurrency is released, and why are guarantees on data deletion mathematically unprovable?
