# Brand Protection Scanner (Uplizd) - Automated BIMI and Email Security Verification

## Summary
The Brand Protection Scanner is an intelligent Uplizd workflow designed to automate the verification of BIMI (Brand Indicators for Message Identification) records and email security protocols. By leveraging the Composio Toolset to interface with MX Toolbox, this solution enables security teams and domain administrators to proactively identify configuration gaps, prevent domain spoofing, and maintain high email deliverability standards through continuous, automated monitoring.

---

## Demo
![Brand Protection Scanner workflow interface showing MX Toolbox integration for BIMI and DMARC verification](image.png)
**Alt text (SEO-ready):** Brand Protection Scanner Uplizd workflow for automated BIMI, DMARC, and email security verification using MX Toolbox and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/b7382311-7b28-5af5-9b6e-d7204c1f45e3)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** security, email, bimi, dmarc, domain, compliance, mx-toolbox, composio, ai workflow
- This solution streamlines domain security hygiene by automating the technical audit of email authentication records.

---

## Who is this for?
This workflow is built for professionals responsible for maintaining brand integrity and secure communication channels.

- **Security Operations Manager**
    - Ensures consistent enforcement of DMARC policies across all corporate domains.
- **Email Marketing Lead**
    - Protects sender reputation by verifying BIMI logo display and authentication records.
- **IT Infrastructure Administrator**
    - Automates the detection of misconfigured DNS records that lead to email spoofing.
- **Brand Compliance Officer**
    - Audits digital assets to ensure brand identity is correctly represented in external email clients.

---

## Features
- **Automated BIMI Validation**
    - Real-time checks to ensure your brand logo is correctly associated with your domain for supported email clients.
- **DMARC Policy Monitoring**
    - Continuous scanning of DNS records to verify that DMARC, SPF, and DKIM policies are correctly implemented.
- **MX Toolbox Integration**
    - Leverages the Composio Toolset to execute deep-dive diagnostic queries against global DNS infrastructure.
- **Security Gap Alerting**
    - Automatically flags missing or invalid security headers that expose the organization to phishing risks.
- **Centralized Audit Logs**
    - Maintains a single source of truth for domain health, simplifying reporting for compliance and security audits.

---

## Use Cases
**Domain Security Audits**
- Perform bulk verification of SPF/DKIM/DMARC records across a portfolio of company-owned domains.
- Generate instant reports on domain vulnerability status to prioritize remediation efforts.

**Brand Identity Protection**
- Verify that BIMI records are correctly formatted and discoverable by major mailbox providers.
- Monitor for unauthorized changes to DNS records that could impact brand display or email deliverability.

**Compliance and Reporting**
- Automate the collection of security posture data for quarterly internal security reviews.
- Maintain documentation of email security compliance for regulatory and insurance requirements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your MX Toolbox API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target domain name for the security scan.
- **Agent**: Analyzes the domain and orchestrates the diagnostic sequence.
- **Composio Toolset**: Executes specific MX Toolbox API calls to fetch DNS and security records.
- **Chat Output**: Returns a summarized health report and actionable security recommendations.

### 3) Run the Flow
Open the Uplizd Playground and try these prompts:
- `Scan the domain 'example.com' for BIMI and DMARC configuration errors.`
- `Check the email security posture for 'mybrand.org' and list any missing headers.`
- `Perform a full DNS diagnostic for 'company.net' and summarize the findings.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a security analyst, interpreting raw DNS data into human-readable insights.
- Instruct the agent to prioritize critical security failures (e.g., DMARC 'none' policies).
- Configure the agent to provide clear, step-by-step remediation instructions for identified issues.
- Ensure the agent maintains a professional, security-focused tone in all output reports.

### 2) Composio Toolset Node
- Provide a valid MX Toolbox API key to enable deep-link diagnostics.
- Set the connection scope to allow read-only access to DNS and security record lookup tools.

### 3) Tool Availability
- **DNS Lookup**: Fetches current TXT and CNAME records for authentication verification.
- **Security Header Scanner**: Analyzes DMARC, SPF, and DKIM policy configurations.
- **BIMI Validator**: Confirms the presence and validity of BIMI record syntax.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Automates infrastructure and account security audits.
- [Abuse Report Manager](../abuse-report-manager-by-abuselpdb/README.md) — Tracks and manages external abuse reports for domain security.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Ensures continuous operational uptime for automated workflows.
