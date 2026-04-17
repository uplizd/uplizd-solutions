# Campaign Health Monitor (Uplizd) - Automated email deliverability and list hygiene optimization

## Summary
The Campaign Health Monitor (Uplizd) is an automated AI workflow designed to maintain high email deliverability by continuously auditing contact lists against NeverBounce. By identifying invalid, risky, or disposable email addresses in real-time, this solution ensures your marketing campaigns reach their intended audience, reduces bounce rates, and protects your sender reputation, providing a single source of truth for your email marketing hygiene.

---

## Demo
![Campaign Health Monitor workflow dashboard showing email list validation status and NeverBounce integration nodes](../image.png)
**Alt text (SEO-ready):** Campaign Health Monitor Uplizd workflow showing email list validation, NeverBounce integration, and automated deliverability reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/campaign-health-monitor-by-neverbounce)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** email marketing, list hygiene, deliverability, neverbounce, data quality, automation, composio, ai workflow

This solution bridges the gap between raw contact databases and high-performance email delivery by automating the validation lifecycle.

---

## Who is this for?
This solution is designed for teams managing high-volume email outreach who need to maintain sender authority and campaign performance.

- **Email Marketing Manager**
    - Automates list cleaning before every major campaign launch to prevent hard bounces.
- **RevOps Specialist**
    - Ensures CRM data integrity by purging invalid contacts and updating status fields automatically.
- **Growth Marketer**
    - Increases conversion rates by ensuring outreach efforts are directed only at verified, reachable leads.
- **Deliverability Consultant**
    - Monitors sender reputation metrics and flags risky domains or patterns before they trigger ISP blocks.

---

## Features
- **Real-Time Validation**
    - Instantly verify email addresses via NeverBounce API to filter out invalid, disposable, or catch-all accounts.
- **Automated List Hygiene**
    - Automatically flag or remove contacts from your mailing lists based on validation scores to maintain list health.
- **Proactive Bounce Prevention**
    - Identify risky email patterns before they impact your sender reputation or lead to blacklisting.
- **Seamless CRM Integration**
    - Sync validation results directly back to your CRM or marketing automation platform using the Composio Toolset.
- **Performance Reporting**
    - Generate automated summaries of list health and deliverability trends to inform future outreach strategies.

---

## Use Cases
**Pre-Campaign List Scrubbing**
- Automatically validate a new lead list imported from a trade show or webinar before triggering an automated nurture sequence.
- Filter out high-risk email addresses from your primary newsletter list to maintain a clean sender reputation.

**CRM Data Maintenance**
- Run a scheduled audit on your entire CRM contact database to identify and update the status of decayed email addresses.
- Automatically tag contacts as "Do Not Email" based on NeverBounce validation results to prevent future bounce events.

**Deliverability Monitoring**
- Monitor the percentage of "risky" vs "deliverable" emails across different acquisition channels to identify low-quality lead sources.
- Trigger an alert to the marketing team when the bounce rate of a specific segment exceeds a predefined threshold.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your dashboard.
2. Connect your NeverBounce API credentials within the integration settings.
3. Map your CRM or data source to the input node of the workflow.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the list of email addresses or triggers the periodic audit.
- **Agent**: Analyzes the validation requirements and orchestrates the NeverBounce verification process.
- **Composio Toolset**: Executes the API calls to NeverBounce and updates the corresponding contact records.
- **Chat Output**: Returns the summary report of cleaned records and identified invalid addresses.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Validate the email list in the 'Q3-Newsletter' segment and update the CRM.`
- `Check the health of my recent lead import and generate a report of invalid addresses.`
- `Run a full audit on all contacts created in the last 30 days and flag risky emails.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for list validation logic.
- Use a model capable of structured data handling (e.g., GPT-4o).
- Instruction: "You are an email hygiene expert. Your goal is to validate contact lists using NeverBounce and update CRM records based on the results."
- Instruction: "Always prioritize the removal of 'invalid' status emails and flag 'risky' emails for manual review."

### 2) Composio Toolset Node
- Provide your NeverBounce API key in the Composio configuration.
- Ensure the connection scope includes read/write access to your CRM (e.g., HubSpot, Salesforce) to allow for automatic field updates.

### 3) Tool Availability
- **NeverBounce API**: For email verification and status retrieval.
- **CRM Connector**: For updating contact properties (e.g., "Email Status", "Validation Date").
- **Notification Service**: For sending summary reports to the marketing team.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track and analyze account engagement metrics.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize contact data across multiple platforms.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and verify contact information.
