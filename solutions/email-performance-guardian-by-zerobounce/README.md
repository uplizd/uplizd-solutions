# Email Performance Guardian (Uplizd) - Automated email deliverability and campaign optimization

## Summary
The Email Performance Guardian is an intelligent Uplizd workflow that monitors email campaign metrics and proactively manages list hygiene to maximize deliverability. By integrating ZeroBounce with your CRM, this solution identifies high-risk addresses, automates bounce management, and ensures your sender reputation remains pristine, ultimately increasing pipeline velocity and reducing marketing waste.

---

## Demo
![Email Performance Guardian dashboard showing real-time bounce rate monitoring and automated list cleaning actions](image.png)
**Alt text (SEO-ready):** Email Performance Guardian dashboard showing real-time bounce rate monitoring, automated list cleaning, ZeroBounce integration, and Uplizd workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-4ded6527--2f5b--5b85--8ccc--100eb9e4dd4e-blue)](https://uplizd.ai/solutions/4ded6527-2f5b-5b85-8ccc-100eb9e4dd4e)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, deliverability, zerobounce, crm, data hygiene, list management, automation, composio
- This solution bridges the gap between raw campaign data and actionable list hygiene to protect your sender domain reputation.

---

## Who is this for?
This workflow is designed for teams managing high-volume outreach who need to maintain strict data quality standards.

- **Email Marketing Manager**
    - Automates the removal of invalid or risky contacts to maintain high engagement rates.
- **RevOps Specialist**
    - Ensures CRM data integrity by syncing real-time validation status across sales and marketing platforms.
- **Growth Marketer**
    - Protects sender reputation to ensure critical outreach reaches the inbox rather than the spam folder.
- **Customer Success Lead**
    - Monitors communication health to ensure transactional and nurture emails are delivered successfully.

---

## Features
- **Real-time Validation**
    - Automatically triggers ZeroBounce checks for new leads or updated contact records via the Composio Toolset.
- **Automated Bounce Management**
    - Instantly flags or suppresses contacts that return hard bounces, preventing further damage to sender reputation.
- **CRM Synchronization**
    - Seamlessly updates contact status fields in your CRM based on validation results, ensuring a single source of truth.
- **Proactive Health Alerts**
    - Sends automated notifications when bounce rates exceed defined thresholds, allowing for immediate intervention.
- **Compliance-Aware Cleanup**
    - Applies logic-based filtering to ensure data handling adheres to privacy regulations while maintaining list hygiene.

---

## Use Cases
**Campaign Deliverability Protection**
- Automatically validate new sign-ups before they enter your primary nurture sequence.
- Quarantine contacts with "catch-all" or "risky" status to prevent potential bounce spikes.

**CRM Data Hygiene**
- Run bulk validation jobs on legacy lists to identify and purge decayed contact information.
- Sync validation scores to custom CRM fields to inform lead scoring and segmentation strategies.

**Reputation Monitoring**
- Trigger an alert to the marketing team if a specific campaign's bounce rate crosses a 2% threshold.
- Generate weekly reports on list health trends to track the long-term impact of automated cleaning.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select "Email Performance Guardian."
2. Click "Import" to add the workflow to your workspace.
3. Connect your CRM and ZeroBounce accounts via the Composio integration portal.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or automated webhooks from your email platform.
- **Agent**: Analyzes the request and determines the necessary validation or cleanup action.
- **Composio Toolset**: Executes API calls to ZeroBounce and your CRM to perform validation and updates.
- **Chat Output**: Returns a summary report of the actions taken and the current health status of the list.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Validate the new contacts added to the 'Q3 Newsletter' list in HubSpot.`
- `Check the bounce status for the latest batch of leads and update the 'Email_Status' field in Salesforce.`
- `Identify all high-risk email addresses in our master database and move them to a suppression list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your email hygiene strategy.
- Instruct the agent to prioritize ZeroBounce validation results over existing CRM data.
- Define clear thresholds for what constitutes a "risky" email address.
- Configure the agent to provide concise summaries of actions performed after every execution.

### 2) Composio Toolset Node
- Provide your ZeroBounce API key and CRM credentials within the Composio connection settings.
- Ensure the scope includes read/write access to contact objects and email fields.

### 3) Tool Availability
- **ZeroBounce API**: For email validation, toxicity checks, and bounce analysis.
- **CRM Connector**: For reading contact data and updating status fields (e.g., Salesforce, HubSpot).
- **Notification Service**: For sending alerts via Slack or Email when health thresholds are breached.

---

## Related Solutions
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Comprehensive tools for maintaining overall CRM data quality and deduplication.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize contact and lead data across multiple platforms to ensure consistency.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage sales opportunities and pipeline stages to maximize revenue conversion.
