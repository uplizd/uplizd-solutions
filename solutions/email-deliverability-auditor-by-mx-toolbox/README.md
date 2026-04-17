# Email Deliverability Auditor (Uplizd) - Optimize inbox placement and domain reputation

## Summary
The Email Deliverability Auditor is an automated Uplizd workflow designed to monitor, analyze, and improve your email infrastructure health. By leveraging real-time data from MX Toolbox, this solution identifies potential configuration issues—such as SPF, DKIM, and DMARC failures—before they impact your sender reputation, ensuring your communications reach the primary inbox rather than the spam folder.

---

## Demo
![Email Deliverability Auditor workflow dashboard showing MX record analysis and domain health scores](image.png)
**Alt text (SEO-ready):** Email Deliverability Auditor dashboard in Uplizd showing MX record analysis, domain health scores, and automated remediation workflows for improved inbox placement.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/85b3b83c-4825-5a2b-a659-1b7fd3a41e50)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email, deliverability, mx toolbox, domain health, dmarc, spf, dkim, automation
- This solution streamlines technical email compliance and domain reputation management for high-volume senders.

---

## Who is this for?
This solution is built for teams managing high-volume outbound communication who need to maintain strict sender authority.

- **Email Marketing Manager**
    - Ensures campaign ROI by preventing critical emails from being flagged as spam.
- **IT/DevOps Engineer**
    - Automates the monitoring of complex DNS records like SPF, DKIM, and DMARC.
- **Sales Operations Lead**
    - Protects outreach sequences from being blocked by major email service providers.
- **Compliance Officer**
    - Maintains audit trails of domain authentication settings for security and regulatory standards.

---

## Features
- **Automated DNS Scanning**
    - Performs real-time lookups of MX, SPF, DKIM, and DMARC records via the Composio Toolset.
- **Reputation Health Scoring**
    - Translates complex technical errors into actionable health scores for non-technical stakeholders.
- **Proactive Alerting**
    - Triggers immediate notifications when domain authentication records drift or expire.
- **Remediation Guidance**
    - Provides step-by-step instructions for fixing configuration gaps detected during the audit.
- **Multi-Domain Support**
    - Scales auditing capabilities across multiple sending domains within a single centralized dashboard.

---

## Use Cases
**Domain Authentication Compliance**
- Automatically verify that all sending domains meet current Google and Yahoo bulk sender requirements.
- Detect and alert on missing or misconfigured DMARC policies that expose domains to spoofing.

**Infrastructure Health Monitoring**
- Schedule recurring audits to catch DNS record decay before it impacts daily email throughput.
- Identify blacklisted IP addresses associated with your mail server infrastructure.

**Outreach Campaign Protection**
- Pre-flight check of domain settings before launching large-scale cold email or marketing campaigns.
- Analyze deliverability impact of recent changes to mail server configurations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Email Deliverability Auditor.
2. Click "Import" to add the workflow to your workspace.
3. Connect your MX Toolbox API credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target domain name and audit parameters from the user.
- **Agent**: Interprets the audit request and orchestrates the diagnostic sequence.
- **Composio Toolset**: Executes the specific MX Toolbox API calls to fetch DNS data.
- **Chat Output**: Formats the technical audit results into a clear, readable summary report.

### 3) Run the Flow
Use the Playground to test your domain health:
- `Audit my domain example.com and check for DMARC failures.`
- `Run a full deliverability scan on our primary sending domain.`
- `Check if our SPF records are correctly configured for our current mail provider.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical infrastructure analyst.
- Focus on identifying critical DNS misconfigurations.
- Prioritize clear, non-technical explanations for remediation steps.
- Maintain a professional, security-focused tone in all output reports.

### 2) Composio Toolset Node
- Requires a valid MX Toolbox API key with read-only access to DNS diagnostic tools.
- Scope should be limited to domain lookup and record verification capabilities.

### 3) Tool Availability
- **DNS Lookup**: Fetches current A, MX, and TXT records.
- **Authentication Validator**: Checks validity of SPF, DKIM, and DMARC syntax.
- **Blacklist Checker**: Queries common RBLs to ensure IP reputation.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track and optimize platform usage data.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Maintain operational efficiency across automated pipelines.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Audit and secure user permissions and access logs.
