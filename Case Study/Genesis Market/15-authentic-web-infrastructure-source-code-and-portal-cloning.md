# 🌐 15: Authentic Web Infrastructure, Source Code Dissection & Portal Cloning
## *Reverse Engineering Genesis Market's Web Application Stack (Yii Framework, RSA Client-Side Crypto, Invite Ledgers & Law Enforcement Seizure)*

![Genesis Vector Logo](./images/genesis_logo_vector.svg)

> **Chapter Focus:** Primary source web application reverse engineering, authentic HTML/JavaScript source code analysis from live Internet Archive snapshots, cryptographic password protection mechanisms, invite token validation, and complete web portal cloning.  
> **Primary Web Artifacts Recovered:**
> * Authentic Vector SVG Brand Identity: [`images/genesis_logo_vector.svg`](./images/genesis_logo_vector.svg)
> * Raw 2021 Sign-In Portal: [`demo-site/authentic-login-page.html`](./demo-site/authentic-login-page.html)
> * Raw 2021 Invite Registration Portal: [`demo-site/authentic-register-page.html`](./demo-site/authentic-register-page.html)
> * Raw 4 April 2023 Seizure Landing Page: [`demo-site/authentic-seizure-page.html`](./demo-site/authentic-seizure-page.html)
> * Interactive Web Simulator & Media Hub: [`demo-site/index.html`](./demo-site/index.html)

---

## 🏛️ 1. Introduction: Forensic Recovery of Web Infrastructure

While many threat intelligence analyses examine Genesis Market through second-hand screenshots and post-takedown press summaries, digital forensics demands direct inspection of primary source artifacts. 

By analyzing unredacted historical web archives preserved in the **Internet Archive (Wayback Machine)** from 2021 up to the **Operation Cookie Monster** takedown on 4 April 2023, investigators can deconstruct the exact web application architecture, client-side security measures, user registration workflows, and the official law enforcement seizure infrastructure.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│               GENESIS MARKET WEB ARCHITECTURE FORENSIC TIMELINE                 │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   [2018 – March 2023: Active Commercial Operations]                             │
│   • Domain: genesis.market (and multiple clear-web / onion mirrors)             │
│   • Web Stack: PHP 7.x / 8.x running on Yii Framework 2.0                      │
│   • Reverse Proxy: Nginx + Cloudflare DDoS protection                           │
│   • Database Backend: MySQL / MariaDB (dual server clusters seized)             │
│   • Client-Side Encryption: RSA-2048 public key encryption in JavaScript        │
│   • Access Control: Invite-only gating (32-character tokens) + Jabber/XMPP      │
│                                                                                 │
│   [4 April 2023: Operation Cookie Monster Seizure]                             │
│   • Infrastructure: Complete DNS redirection to law enforcement Cloudflare NS   │
│   • Landing Page: Static black-background HTML with embedded Base64 PNG image   │
│   • Legal Authorities: 18 U.S.C. §§ 1028, 1029, 1030 (E.D. Wisconsin)           │
│   • Victim Notification: Integration with Politie 'CheckYourHack' & HIBP       │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 2. Web Application Framework Stack (Yii PHP)

Primary source inspection of [`authentic-login-page.html`](./demo-site/authentic-login-page.html) reveals that the developers of Genesis Market chose the **Yii 2.0 PHP Framework** to power the marketplace frontend.

### A. Framework Footprint & DOM Identifiers:
The DOM structure contains multiple unambiguous indicators of Yii 2.0:
1. **CSRF Protection Parameter:**  
   `<meta name="csrf-param" content="_csrf-clientzone">`  
   `<meta name="csrf-token" content="...">`  
   Yii's native anti-CSRF token protection was implemented across all form submissions to prevent cross-site request forgery attacks from competitor cybercrime groups.
2. **Client-Side Form Validation Scripts:**  
   * `/assets/afe82d8/yii.js`
   * `/assets/afe82d8/yii.validation.js`
   * `/assets/afe82d8/yii.activeForm.js`  
   Form elements utilized Yii's `yiiActiveForm` jQuery plugin to handle asynchronous inline validation, field trimming, and client-side error rendering.
3. **HTTP Session Cookie Architecture:**  
   When a user connected to `https://genesis.market`, the server issued two core cookies:
   * `genesis-clientzone`: The primary PHP session cookie (`HttpOnly; path=/; secure`).
   * `_all_cookies_params_id`: A persistent client-tracking cookie with a 365-day expiry (`Max-Age=31536000; path=/; httponly`), used to correlate visitor telemetry and detect unauthorized multiple-account registrations.

---

## 🔐 3. Client-Side Cryptography (RSA-2048 Password Encryption)

A remarkable finding in Genesis Market's frontend source code is the presence of **client-side public-key cryptography** on both the login and registration forms:

```html
<form id="register-form" 
      class="prevent-doublesubmit" 
      action="/guest/register" 
      method="post" 
      data-rsa-exponent="010001" 
      data-rsa-modulus="a44583a2277517b0625c9c005984967e694f1a322bd751de0ceb3b6726b906eeb8a0f3602bc1df5b231b225cebf5453ec8f16621c7c398b88e5f5c520e4a0519c8c2ae3df08cbdfe8a928981a822f7ea209870a9c4252aaaa462cfc96a1f5b8f0559ade8b5eed1de8ac1aa1542fa8f2fdf587b00dfb037b8860e05bc8a15e02ec583100889efd86498d687766aeb5cd4bf8199ed9e2509f63fe9d5333b9e7c2fd181444d77cd34c36b95567ca2caf8f7d7a6b541f84153efdece72c6a3b0ec7b5639f746bea7d8f38ef4d5dcea5ffe269baa8ce84db0b70ca13462324b9d382198dde78cff17963ea754cce90cd2194eba3c37b40fa5c92e8a9463d10112fbf1" 
      data-rsa-keysize="2048">
```

### Technical Significance:
* **The Mechanism:** When the user entered their plaintext password into `#registerform-password`, an event listener intercepted the submit event. Rather than sending the plaintext password over HTTP/HTTPS, the JavaScript engine invoked an RSA library (`login.min.js`), encrypted the password using the public key (`exponent: 65537`, `2048-bit modulus`), and wrote the ciphertext into a hidden input field:  
  `<input type="hidden" id="registerform-password-encrypted" name="RegisterForm[password]" value="...">`
* **Adversary Operational Rationale:**  
  Even though the clear-web mirrors operated behind TLS, cybercriminals frequently accessed Genesis through Tor exit nodes, unencrypted public VPNs, or compromised proxies. Client-side RSA encryption ensured that even if TLS was terminated or stripped by a malicious proxy or intelligence agency intercept, the buyer's master password could never be recovered in plaintext.

---

## 🎟️ 4. The Invite-Only Gated Economy & Validation Rules

Unlike public fraud forums that allow unrestricted account registration, Genesis Market maintained a strict invite-only access policy to prevent infiltration by security researchers and low-capital fraudsters.

### Regex Validation for Invite Tokens:
From `/guest/register`:
```javascript
yii.validation.regularExpression(value, messages, {
    "pattern": /^invite_[a-zA-Z0-9_]{25}$/,
    "not": false,
    "message": "Invite must be valid and generated by registered clients, must contain exactly 32 symbols and starts with invite_....",
    "skipOnEmpty": 1
});
```

### Operational Takeaways:
1. **The 32-Character Token:** Every valid invite code had an exact 32-character length, comprising the prefix `invite_` followed by exactly 25 base62/underscore characters (e.g., `invite_aB3dE5gH7jK9mN1pQ3sU5wY7z`).
2. **Internal Generation:** Invites could only be generated by active, paying clients who had deposited cryptocurrency and maintained an active balance.
3. **Mandatory Jabber/XMPP Requirement:** Registration strictly required a valid Jabber ID (`RegisterForm[jabber_id]`). Telegram was disallowed for core account recovery because Jabber/XMPP with OTR (Off-the-Record Messaging) offered decentralized, non-subpoenaable end-to-end encryption.

---

## 🇷🇺 5. The CIS "Safe-Harbor" Clause (Geopolitical Cybercrime Doctrine)

The most revealing forensic discovery in the authentic Genesis Market Terms of Service modal is the inclusion of an explicit **CIS (Commonwealth of Independent States) Safe-Harbor Clause**, presented in both English and Russian.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│               GENESIS MARKET TERMS OF SERVICE: RULE 6 COMPARISON                │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   [Russian Language Version (Original Master)]:                                 │
│   «6. Магазин не использует и не продаёт продукты под ресурсы стран СНГ.»      │
│                                                                                 │
│   [English Translation (Exported for Foreign Buyers)]:                          │
│   "6. The store does not use and does not sell products for resources          │
│       of the CIS countries."                                                    │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Geopolitical & Legal Forensic Analysis:
In Russian and post-Soviet cybercrime law, **Article 272** (Unlawful Access to Computer Information) and **Article 273** (Creation, Use, and Distribution of Malicious Computer Software) of the Russian Federation Criminal Code penalize cyber intrusions committed against entities located within the Russian Federation or CIS member states.

By strictly excluding all Russian, Belarusian, Kazakh, and other CIS corporate domains, government portals, and banking services from its bot inventory:
1. **Domestic Immunity Strategy:** Marketplace operators and infostealer developers operated under the belief that local law enforcement would ignore their activities as long as no domestic victims filed complaints.
2. **Malware Geofencing Alignment:** This policy mirrored the code-level geofencing discovered in RedLine and Vidar stealers (which abort execution if `GetUserDefaultUILanguage()` returns `0x0419` for Russian).

---

## 🚨 6. Law Enforcement Seizure Infrastructure (4 April 2023)

On 4 April 2023, federal agents executed seizure warrants issued by Magistrate Judge Stephen C. Dries in the Eastern District of Wisconsin. The live web servers were seized, DNS records were altered, and visitors were greeted by the official seizure landing page.

Inspection of the raw captured file [`authentic-seizure-page.html`](./demo-site/authentic-seizure-page.html) reveals:
```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title>This Website Has Been Seized</title>
</head>
<body style="background-color: black;">
<p><img border="0" 
alt="Genesis Market's domains have been seized byt he FBI pursuant to a seizure warrant issued by the United States District Court for the Eastern District of Wisconsin. These seizures were possible because of international law enforcement and private sector coordinatuion involving the partners listed below.

Been active on Genesis Market? In contact with Genesis Market administrators?
Email us, we're interested: FBIMW-Genesis@fbi.gov" 
src="data:image/png;base64,/9j/4gxYSUNDX1BST0ZJTEUAAQEAAAxITGlubwIQAABtbnRyUkdCIFhZWiAHzgACAAkABgAxAABh...">
</p>
</body>
</html>
```

### Key Technical Elements of the Seizure Page:
1. **Self-Contained Base64 Payload:** Rather than hosting external image files that could fail if a secondary CDN was disrupted, the entire law enforcement notice—including the official seals of the FBI, Dutch Police, Europol, Eurojust, and partner agencies—was encoded directly as a 1.9 MB Base64 data URI string within the HTML document.
2. **Direct Investigative Tipline:** The notice explicitly established an FBI contact channel (`FBIMW-Genesis@fbi.gov`), inviting marketplace users and administrators to make contact.
3. **Statutory Seizure Citations:** The seizure warrant operated under **18 U.S.C. §§ 981 and 982** (criminal forfeiture), tied to underlying violations of:
   * **18 U.S.C. § 1028:** Fraud and related activity in connection with identification documents.
   * **18 U.S.C. § 1029:** Fraud and related activity in connection with access devices.
   * **18 U.S.C. § 1030:** Computer Fraud and Abuse Act (CFAA).

---

## 🧪 7. Educational Clones & Interactive Simulators

To allow researchers, incident responders, and students to safely interact with this historical infrastructure without touching dark-web proxies or live malware, this case study provides a complete educational frontend suite:

| Artifact / Tool | File Location | Purpose & Interactive Features |
|---|---|---|
| **Interactive Research Hub** | [`demo-site/index.html`](./demo-site/index.html) | Fully unified web simulator featuring: <br>• Authentic Sign-In & Invite-Only Sign-Up<br>• Russian/English Terms of Service Modal<br>• Client-Side RSA-2048 Cryptography Visualizer<br>• Politie Nederland **CheckYourHack** Verification Engine<br>• Genesis Chromium CDP Hooking Simulator<br>• 13 High-Resolution Media Blueprints & Video Hub |
| **Raw Seizure Page** | [`demo-site/authentic-seizure-page.html`](./demo-site/authentic-seizure-page.html) | Exact 1:1 raw capture of the 4 April 2023 law enforcement landing page with embedded Base64 graphics. |
| **Raw 2021 Sign-In** | [`demo-site/authentic-login-page.html`](./demo-site/authentic-login-page.html) | Primary source HTML capture of the Yii 2.0 login interface. |
| **Raw 2021 Registration** | [`demo-site/authentic-register-page.html`](./demo-site/authentic-register-page.html) | Primary source HTML capture containing client-side RSA modulus attributes and full Terms of Service text. |
| **Vector SVG Logo** | [`images/genesis_logo_vector.svg`](./images/genesis_logo_vector.svg) | Clean vector graphic extracted directly from the 2021 Genesis web asset bundle. |

---

## ⏭️ Next Chapter
Proceed to [**Master Case Study Index**](./README.md) to explore the complete threat intelligence, SOC detection queries, Splunk analytics, and incident response playbooks for Genesis Market and Operation Cookie Monster.
