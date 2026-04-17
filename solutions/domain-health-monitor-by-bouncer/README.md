# Domain Health Monitor (Uplizd) - Proactive email reputation and configuration management

## Summary
The Domain Health Monitor is an automated Uplizd AI workflow designed to safeguard your email deliverability by continuously auditing domain configurations and reputation status. By integrating with Bouncer, this solution provides real-time visibility into DNS health, blacklist status, and authentication protocols, ensuring your outreach infrastructure remains clean, compliant, and highly performant for marketing and sales operations.

---

## Demo
![Domain Health Monitor workflow dashboard showing automated Bouncer API checks and DNS validation status](image.png)
**Alt text (SEO-ready):** Domain Health Monitor Uplizd workflow dashboard showing automated Bouncer API email reputation checks and DNS configuration validation status.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIVDQs5Yv25GgAAAB1pVFh0Q29tbWVudAAAAAAAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAIklEQVR42mP8z8AARsBw1AABgBqG0f8PBAyD0f8PBGzGAAAu/gYJ+5682QAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/a76ebd1d-9bf7-5d71-aab6-da5e0e38e4cc)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** email deliverability, domain reputation, bouncer, dns, authentication, spf, dkim, dmarc
- This solution bridges the gap between technical DNS management and marketing operations to prevent email bounce-backs and spam folder placement.

---

## Who is this for?
This solution is designed for teams prioritizing high-impact email communication and infrastructure reliability.

- **Deliverability Specialist**
    - Automates the monitoring of domain blacklists and authentication health to ensure maximum inbox placement.
- **Marketing Operations Manager**
    - Protects campaign ROI by preventing domain-wide reputation decay that impacts bulk email performance.
- **IT Security Administrator**
    - Maintains strict compliance with SPF, DKIM, and DMARC protocols to prevent domain spoofing and unauthorized usage.
- **Sales Enablement Lead**
    - Ensures that SDR outreach domains remain healthy, preventing critical sales communications from being flagged as malicious.

---

## Features
- **Automated Reputation Audits**
    - Executes scheduled checks against global blacklists to identify and report domain reputation issues before they impact outreach.
- **DNS Protocol Validation**
    - Continuously verifies the integrity of SPF, DKIM, and DMARC records to ensure your domain meets modern security standards.
- **Real-time Alerting**
    - Triggers immediate notifications when domain health metrics drop below defined thresholds, allowing for rapid remediation.
- **Composio-Powered Bouncer Integration**
    - Leverages the Composio Toolset to interface directly with Bouncer, enabling seamless data retrieval and health reporting.
- **Centralized Health Dashboard**
    - Consolidates complex technical data into a single source of truth for non-technical stakeholders to track domain status.

---

## Use Cases
**Proactive Reputation Management**
- Automatically scan domains for presence on major spam blacklists every 24 hours.
- Generate weekly reports on domain health trends to identify early signs of reputation decay.

**Infrastructure Compliance**
- Audit DNS records to ensure SPF, DKIM, and DMARC are correctly configured and preventing spoofing.
- Validate that all subdomains are inheriting correct security policies from the primary domain.

**Outreach Optimization**
- Verify domain health before launching high-volume marketing campaigns to ensure maximum deliverability.
- Monitor the impact of recent DNS changes on overall email bounce rates and engagement metrics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Domain Health Monitor template file provided in this repository.
3. Connect your Bouncer API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target domain and audit parameters from the user.
- **Agent**: Analyzes the domain configuration and interprets Bouncer API diagnostic data.
- **Composio Toolset**: Executes secure API calls to Bouncer to fetch reputation and DNS health metrics.
- **Chat Output**: Delivers a human-readable summary of the domain's health and recommended remediation steps.

### 3) Run the Flow
Use the Playground to test your domain health:
- `Check the health status and blacklist report for mydomain.com`
- `Verify if mydomain.com has valid SPF and DMARC records configured`
- `Run a full domain reputation audit and summarize the findings`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical auditor, translating raw DNS and reputation data into actionable insights.
- Prioritize accuracy when reporting security protocol failures.
- Maintain a professional, objective tone for technical audit summaries.
- Suggest specific remediation steps (e.g., "Update SPF record") when issues are detected.

### 2) Composio Toolset Node
- **API Key**: Input your Bouncer API key to enable secure domain data retrieval.
- **Connection Scope**: Ensure the toolset has read-only access to domain reputation and DNS diagnostic endpoints.

### 3) Tool Availability
- `bouncer_get_domain_reputation`: Fetches current blacklist and reputation scores.
- `dns_validator_check`: Validates the presence and syntax of SPF, DKIM, and DMARC records.
- `notification_service_alert`: Sends alerts via email or Slack when critical health issues are identified.

---

## Related Solutions
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) — Monitor and maintain account security and compliance standards.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate data cleanup and formatting to maintain a pristine CRM.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather and report on account-level intelligence for sales teams.
