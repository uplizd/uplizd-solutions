# Email Domain Health Monitor (Uplizd) - Automated deliverability and reputation tracking

## Summary
The Email Domain Health Monitor by Resend is an automated AI workflow designed to protect your sender reputation by continuously auditing DNS records, SPF, DKIM, and DMARC configurations. By leveraging real-time monitoring, this solution helps email marketers, DevOps engineers, and IT administrators prevent domain blacklisting, ensure high inbox placement rates, and maintain a single source of truth for email infrastructure health.

---

## Demo
![Email Domain Health Monitor workflow dashboard showing real-time DNS and deliverability status checks](image.png)
**Alt text (SEO-ready):** Email Domain Health Monitor dashboard showing real-time DNS, SPF, DKIM, and DMARC status checks for improved email deliverability and sender reputation on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c44251ad-6d77-5d2b-ab86-7be1d7d1dd89)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** email deliverability, dns monitoring, resend, sender reputation, automation, infrastructure health, composio, ai workflow
- This solution bridges the gap between technical DNS configuration and proactive email infrastructure management.

---

## Who is this for?
This solution is designed for teams managing high-volume email traffic who need to maintain strict compliance and deliverability standards.

- **Email Marketers**
    - Ensure marketing campaigns reach the inbox rather than the spam folder by monitoring domain health.
- **DevOps Engineers**
    - Automate the verification of DNS records and security protocols to prevent infrastructure-related downtime.
- **IT Administrators**
    - Maintain a centralized audit trail of domain configurations and security posture across multiple business domains.
- **Compliance Officers**
    - Guarantee that all outgoing communications adhere to industry-standard authentication protocols like DMARC.

---

## Features
- **Automated DNS Auditing**
    - Continuously scans your domain's DNS records to ensure SPF, DKIM, and DMARC settings are correctly implemented.
- **Real-time Health Alerts**
    - Triggers immediate notifications if domain reputation drops or if critical authentication records are modified or deleted.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely interface with Resend and DNS management APIs for accurate data retrieval.
- **Deliverability Scoring**
    - Provides a simplified health score that helps non-technical stakeholders understand the current state of their email infrastructure.
- **Historical Reporting**
    - Tracks changes in domain health over time, allowing for trend analysis and proactive troubleshooting of deliverability issues.

---

## Use Cases
**Proactive Infrastructure Monitoring**
- Automatically verify that new domain additions have the correct security records before they are used for production mail.
- Receive alerts when a DNS provider update inadvertently removes or alters critical DKIM signatures.

**Security and Compliance Audits**
- Perform weekly audits of all managed domains to ensure compliance with evolving email security standards.
- Generate reports for stakeholders detailing the current authentication status of all corporate email domains.

**Reputation Management**
- Identify and remediate domain blacklisting issues before they impact large-scale marketing or transactional email campaigns.
- Monitor for unauthorized domain usage by cross-referencing active DNS records against authorized infrastructure lists.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Email Domain Health Monitor template from the solution library.
3. Connect your Resend API credentials and preferred DNS management tools via the integration settings.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the domain name or monitoring request from the user.
- **Agent**: Analyzes the request and orchestrates the diagnostic checks.
- **Composio Toolset**: Executes the specific API calls to fetch DNS and health data.
- **Chat Output**: Returns a human-readable summary of the domain's health status.

### 3) Run the Flow
Use the Uplizd Playground to test your monitoring capabilities:
- `Check the health status of example-domain.com and report any missing SPF records.`
- `Run a full DNS audit for all domains in my account and highlight any DMARC failures.`
- `Provide a summary of my current sender reputation and suggest improvements for my DKIM configuration.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical analyst, interpreting raw DNS data into actionable insights.
- **Recommended instruction pattern:**
    - Act as an expert email deliverability consultant.
    - Prioritize security-critical failures (DMARC/DKIM) in your response summaries.
    - Provide clear, step-by-step remediation instructions for any detected issues.

### 2) Composio Toolset Node
- **API Key**: Ensure your Resend and DNS provider API keys are stored in your Uplizd environment variables.
- **Connection Scope**: Grant the toolset read-only access to your DNS and email domain settings for security.

### 3) Tool Availability
- **DNS Lookup Tool**: Fetches current TXT, SPF, and DMARC records.
- **Resend API Connector**: Retrieves domain-specific deliverability metrics.
- **Alerting Service**: Formats and dispatches health status notifications.

---

## Related Solutions
- [Account Health Usage Monitor by Jotform](../account-health-usage-monitor-by-jotform/README.md) - Track and report on account activity and usage metrics.
- [Account Health Compliance Monitor by Brevo](../account-health-compliance-monitor-by-brevo/README.md) - Ensure your email marketing accounts remain compliant with platform standards.
- [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational status of your automated business workflows.
