# Pipeline Health Monitor (Uplizd) - Real-time Zoho Bigin deal progression tracking

## Summary
The Pipeline Health Monitor (Uplizd) is an automated AI workflow designed to track deal velocity and identify stalled opportunities within Zoho Bigin. By leveraging the Composio Toolset to interface with your CRM, this solution provides SalesOps teams and Account Executives with a single source of truth for pipeline hygiene, ensuring that no deal slips through the cracks due to inactivity or missed follow-ups.

---

## Demo
![Pipeline Health Monitor dashboard showing stalled deals and Zoho Bigin integration status](image.png)
**Alt text (SEO-ready):** Pipeline Health Monitor Uplizd workflow for Zoho Bigin CRM data hygiene, sales pipeline velocity tracking, and automated opportunity management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFRQyq4XG7QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfoAwoUFCK3W1zNAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFRQyq4XG7QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfoAwoUFCK3W1zNAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFRQyq4XG7QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfoAwoUFCK3W1zNAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFRQyq4XG7QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZkAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfoAwoUFCK3W1zNAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFRQyq4XG7QAAABl0RVh0Q29tbWVudABDcmVhdGVk)](https://uplizd.ai/solutions/pipeline-health-monitor-by-zoho-bigin)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, zoho bigin, pipeline, sales operations, data hygiene, ai workflow, composio, opportunity management  
This solution bridges the gap between raw CRM data and actionable sales intelligence, categorizing it under core RevOps and sales automation workflows.

---

## Who is this for?
This workflow is designed for teams managing high-volume sales pipelines who need proactive monitoring to maintain deal momentum.

*   **Sales Operations Manager**
    *   Automates the identification of stalled deals to maintain clean, accurate pipeline reporting.
*   **Account Executive**
    *   Receives real-time alerts on inactive opportunities, allowing for immediate re-engagement.
*   **Sales Director**
    *   Gains visibility into pipeline velocity and team performance metrics without manual data entry.
*   **Revenue Operations Analyst**
    *   Ensures data hygiene across the Zoho Bigin ecosystem by flagging inconsistencies in deal stages.

---

## Features
- **Automated Stalled Deal Detection**
    - Scans Zoho Bigin for opportunities that have remained in the same stage beyond a defined threshold.
- **Real-time CRM Synchronization**
    - Uses the Composio Toolset to fetch and update deal records instantly, ensuring data accuracy.
- **Intelligent Follow-up Prompts**
    - Generates context-aware communication drafts for AEs to re-engage prospects on stalled accounts.
- **Pipeline Hygiene Reporting**
    - Aggregates health metrics to provide a high-level view of pipeline velocity and potential bottlenecks.
- **Customizable Threshold Logic**
    - Allows users to define "stalled" based on specific deal value, stage, or last-modified timestamps.

---

## Use Cases
**Pipeline Velocity Optimization**
*   Identify deals that have exceeded the average sales cycle duration for their specific stage.
*   Automate the transition of stale leads to a "Nurture" stage to keep the active pipeline clean.

**Sales Performance Management**
*   Flag opportunities missing key fields or next-step activities to improve data completeness.
*   Generate weekly summaries of "at-risk" deals for management review meetings.

**CRM Data Hygiene**
*   Automatically archive or flag dead-end opportunities that haven't seen activity in over 90 days.
*   Sync deal status updates across multiple Zoho Bigin modules to prevent data silos.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the `pipeline-health-monitor-by-zoho-bigin` template file.
3. Connect your Zoho Bigin account via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual request to audit the pipeline.
*   **Agent**: Analyzes the CRM data against your defined health criteria.
*   **Composio Toolset**: Executes read/write operations within Zoho Bigin.
*   **Chat Output**: Delivers the health report and suggested actions to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
*   `"List all deals in the 'Negotiation' stage that haven't been updated in 14 days."`
*   `"Identify stalled opportunities worth over $50,000 and draft a re-engagement email."`
*   `"Provide a summary of the current pipeline health for the North American sales team."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a CRM analyst, prioritizing data accuracy and actionable insights.
*   Focus on identifying patterns of inactivity in deal stages.
*   Maintain a professional, sales-oriented tone for generated communications.
*   Strictly adhere to the provided CRM schema when querying Zoho Bigin.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Zoho Bigin API key is active within the Composio dashboard.
*   **Connection Scope**: Grant read/write access to `Deals`, `Accounts`, and `Contacts` modules.

### 3) Tool Availability
*   `zoho_bigin_list_deals`: Retrieve filtered lists of opportunities.
*   `zoho_bigin_update_deal`: Modify deal stages or custom fields.
*   `zoho_bigin_get_deal_details`: Fetch specific metadata for deep-dive analysis.

---

## Related Solutions
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage complex sales stages and follow-up cadences.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across multiple CRM platforms and tools.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain CRM data quality through automated cleanup and formatting.
