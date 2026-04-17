# Lead Qualification Agent (Uplizd) - Automate form submission scoring and routing

## Summary
The Lead Qualification Agent by Formcarry streamlines your sales pipeline by automatically ingesting, scoring, and routing incoming form submissions. By leveraging AI to analyze lead intent and fit, this Uplizd workflow eliminates manual data entry, reduces response times, and ensures high-priority leads are routed to the appropriate sales representatives instantly.

---

## Demo
![Lead Qualification Agent workflow showing form submission processing and CRM routing](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow by Uplizd for automated form submission processing, lead scoring, and CRM routing using Composio integrations.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e0982b78-4694-56a2-8e6a-2e66367ffd7d)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** lead qualification, formcarry, crm, lead scoring, sales pipeline, data sync, composio, ai workflow

This solution bridges the gap between web-based lead capture and CRM execution to maintain high pipeline velocity.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to optimize their lead-to-opportunity conversion rates.

* **Sales Development Representative (SDR)**
    * Focuses on high-intent leads that have been pre-qualified and routed to their queue.
* **Marketing Operations Manager**
    * Ensures that form data is clean, standardized, and correctly attributed before hitting the CRM.
* **Revenue Operations (RevOps) Lead**
    * Maintains a consistent lead scoring framework across all inbound channels to improve forecasting accuracy.
* **Small Business Owner**
    * Automates the lead intake process to ensure no potential customer inquiry is missed, even outside of business hours.

---

## Features
- **Real-time Lead Scoring**
    * Automatically assigns a lead score based on form input fields and intent signals.
- **Automated CRM Routing**
    * Dynamically assigns leads to the correct sales representative based on territory or company size.
- **Formcarry Integration**
    * Seamlessly pulls data from Formcarry webhooks to trigger the qualification workflow.
- **Intelligent Data Enrichment**
    * Uses the Composio Toolset to cross-reference lead data with external business intelligence tools.
- **Instant Notification Alerts**
    * Triggers immediate Slack or email notifications to the sales team when a high-value lead is qualified.

---

## Use Cases
**Inbound Lead Triage**
* Automatically filtering out spam or low-quality submissions before they reach the CRM.
* Prioritizing enterprise-level inquiries for immediate follow-up by senior account executives.

**Sales Pipeline Acceleration**
* Reducing the time-to-lead-contact by automating the assignment process in Salesforce or HubSpot.
* Syncing lead qualification notes directly into the CRM opportunity record for better context.

**Data Hygiene & Enrichment**
* Standardizing contact information (e.g., phone formats, job titles) during the qualification phase.
* Appending missing company data to leads to provide sales reps with a 360-degree view.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Qualification Agent template using the provided solution ID.
3. Connect your Formcarry account and your target CRM (e.g., Salesforce or HubSpot) via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are authenticated in the settings panel.

### 2) Setup the Nodes
* **Chat Input**: Receives raw form submission data from Formcarry.
* **Agent**: Analyzes the lead's intent and applies your custom scoring logic.
* **Composio Toolset**: Executes the routing, enrichment, and CRM update actions.
* **Chat Output**: Confirms the lead status and logs the outcome to your notification channel.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Qualify this submission: { "email": "prospect@company.com", "company_size": "500+", "intent": "enterprise demo" }`
* `Score and route this lead based on the provided form data and assign to the West Coast team.`
* `Check if this lead exists in the CRM; if not, create a new record and notify the SDR manager.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your digital sales assistant, ensuring consistent qualification standards.
* Focus on identifying "high-intent" keywords in the form submission.
* Apply a strict scoring rubric (1–10) based on company size and job title.
* Route leads only when they meet the minimum threshold for "Sales Qualified."

### 2) Composio Toolset Node
* Provide your Composio API key to enable secure connectivity.
* Set the connection scope to include read/write access for your specific CRM and notification platforms.

### 3) Tool Availability
* **CRM Connector**: For creating/updating leads and opportunities.
* **Data Enrichment Tool**: For verifying company details and firmographics.
* **Notification Service**: For sending alerts to Slack, Microsoft Teams, or Email.

---

## Related Solutions
* [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate detailed reports on incoming account activity.
* [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) — Synchronize lead data across multiple platforms and CRMs.
* [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) — Manage and track your sales pipeline stages effectively.
* [../whats-app-lead-qualifier-by-wati/README.md](../whats-app-lead-qualifier-by-wati/README.md) — Qualify leads directly through WhatsApp messaging.
