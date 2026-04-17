# Deal Pipeline Cleanup Agent (Uplizd) - Automate stale deal archiving and maintain CRM hygiene

## Summary
The Deal Pipeline Cleanup Agent is an intelligent Uplizd workflow designed to automate the maintenance of your sales pipeline by identifying and archiving stale or inactive opportunities. By leveraging real-time CRM data, this solution ensures your team focuses on high-intent prospects, reduces manual data entry, and maintains a single source of truth for pipeline velocity and forecasting accuracy.

---

## Demo
![Deal Pipeline Cleanup Agent workflow showing CRM integration and automated archiving logic](image.png)
**Alt text (SEO-ready):** Deal Pipeline Cleanup Agent for automated CRM data hygiene, sales pipeline management, and stale opportunity archiving using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/386866c9-50ff-5971-8dc9-ce3c62b99746)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, hubspot, salesforce, pipeline, data hygiene, salesops, composio, ai workflow
- This solution streamlines RevOps by automating the identification and cleanup of stagnant deal records within your CRM.

---

## Who is this for?
This solution is built for revenue-focused teams looking to eliminate manual pipeline maintenance and improve forecast reliability.

- **Sales Operations Manager**
    - Automates routine data hygiene tasks to ensure pipeline reports reflect actual deal health.
- **Account Executive**
    - Reduces time spent manually updating or closing out stale records, allowing more time for active selling.
- **Revenue Operations (RevOps) Lead**
    - Maintains a clean, high-velocity pipeline by enforcing consistent data archival policies across the organization.
- **Sales Manager**
    - Gains visibility into true pipeline health by removing noise caused by abandoned or stalled opportunities.

---

## Features
- **Automated Stale Deal Detection**
    - Uses time-based triggers to identify deals that have remained inactive beyond your organization's defined threshold.
- **Intelligent CRM Archiving**
    - Seamlessly updates deal stages or archives records in HubSpot or Salesforce via the Composio Toolset.
- **Customizable Threshold Logic**
    - Allows for granular control over what constitutes a "stale" deal based on last activity date, deal value, or stage.
- **Real-time Sync & Validation**
    - Ensures changes made by the agent are immediately reflected in your CRM, maintaining data integrity across platforms.
- **Automated Notification Workflow**
    - Optionally alerts account owners via email or Slack before a deal is moved to an archived status.

---

## Use Cases
**Pipeline Hygiene Maintenance**
- Automatically move deals that have had no activity for 60+ days to a "Closed-Lost" or "Archived" stage.
- Flag high-value opportunities that have stalled in the negotiation phase for immediate manager review.

**Sales Velocity Optimization**
- Clear out clutter from the active pipeline to ensure sales forecasting tools provide accurate, real-time revenue projections.
- Segment inactive leads into a separate nurturing campaign rather than keeping them in the active sales funnel.

**Compliance & Data Governance**
- Enforce strict data retention policies by automatically archiving deals that exceed the maximum allowed duration in a specific stage.
- Standardize the cleanup process across multiple regional sales teams to ensure uniform reporting metrics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Deal Pipeline Cleanup Agent template from the marketplace.
3. Connect your CRM credentials (e.g., HubSpot or Salesforce) via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or schedule signal to initiate the cleanup process.
- **Agent**: Analyzes CRM data against your defined "stale" criteria and decides which records require action.
- **Composio Toolset**: Executes the API calls to update or archive deal records within your connected CRM.
- **Chat Output**: Provides a summary report of all deals processed, updated, or archived during the run.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Find all deals in the 'Discovery' stage that have had no activity in the last 45 days and move them to 'Stale'.`
- `List all opportunities with a value over $50k that have not been updated in 30 days.`
- `Archive all deals marked as 'Closed-Lost' that are older than 90 days to clean up the workspace.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making layer for your pipeline logic.
- **Role:** Sales Data Analyst.
- **Recommended instruction pattern:**
    - "You are an expert CRM administrator responsible for maintaining pipeline hygiene."
    - "Always verify the last activity date before triggering an archive action."
    - "Prioritize high-value deals for manual review if they meet the stale criteria."

### 2) Composio Toolset Node
- **API Key:** Ensure your CRM API key is active within the Composio dashboard.
- **Connection Scope:** Grant read/write access to `Deals`, `Contacts`, and `Companies` objects to allow the agent to perform full lifecycle management.

### 3) Tool Availability
- **CRM Search:** Query deals based on stage, date, and owner.
- **Record Update:** Modify deal stages and custom fields.
- **Bulk Action:** Process multiple records in a single execution cycle.
- **Notification:** Trigger alerts to CRM owners via integrated communication channels.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms and tools.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Automate bulk data cleanup and formatting for CRM records.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage pipeline stages and track follow-ups for active deals.
- [../deal-opportunity-tracker/README.md](../deal-opportunity-tracker/README.md) - Identify and score new opportunities based on lead signals.
