# Deal Pipeline Integrator (Uplizd) - Unified multi-platform deal synchronization

## Summary
The Deal Pipeline Integrator is an intelligent Uplizd workflow designed to automate the synchronization of sales opportunities across disparate CRM and project management systems. By leveraging the Composio Toolset, this solution eliminates manual data entry, ensures pipeline velocity, and maintains a single source of truth for sales teams operating in complex, multi-tool environments.

---

## Demo
![Deal Pipeline Integrator workflow screenshot showing automated data sync between CRM and project management tools](image.png)
**Alt text (SEO-ready):** Deal Pipeline Integrator workflow in Uplizd, automating CRM data synchronization and sales pipeline management using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6ef542da-8758-544b-bfb5-1e8c6b7c1035)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, pipeline, sales, data sync, composio, ai workflow, revenue operations, integration
- This solution bridges the gap between sales platforms to ensure consistent deal tracking and automated pipeline management.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual data silos and improve operational efficiency.

- **Sales Operations Manager**
    - Automates cross-platform data hygiene to ensure accurate reporting and forecasting.
- **Account Executive**
    - Reduces time spent on administrative data entry, allowing more focus on closing deals.
- **Revenue Operations (RevOps) Lead**
    - Standardizes deal stages and data fields across the entire sales technology stack.
- **Sales Enablement Specialist**
    - Ensures that sales collateral and deal status updates are reflected instantly across all integrated tools.

---

## Features
- **Automated Cross-Platform Sync**
    - Real-time synchronization of deal stages and metadata between major CRM platforms and project management tools.
- **Intelligent Conflict Resolution**
    - Automated logic to handle data discrepancies between systems, ensuring the most recent update always takes precedence.
- **Composio-Powered Connectivity**
    - Utilizes the Composio Toolset to securely interface with diverse APIs, including Salesforce, HubSpot, and Pipedrive.
- **Pipeline Velocity Tracking**
    - Monitors the time deals spend in each stage, triggering alerts when opportunities stall or require immediate attention.
- **Customizable Field Mapping**
    - Flexible configuration to map unique custom fields across different systems without requiring custom code.

---

## Use Cases
**Pipeline Synchronization**
- Automatically mirror deal status changes from your primary CRM to internal project management boards.
- Sync opportunity values and close dates across multiple sales platforms to maintain consistent forecasting.

**Data Hygiene & Maintenance**
- Identify and update stale deal records that have not seen activity in over 30 days.
- Standardize naming conventions for deal stages across different regional sales teams.

**Sales Efficiency**
- Trigger automated follow-up tasks in project management tools whenever a deal moves to a "Negotiation" stage.
- Consolidate lead signals from marketing platforms into the main deal record for a 360-degree view.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Deal Pipeline Integrator template from the solution library.
3. Connect your required CRM and project management accounts via the Composio integration menu.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or automated webhooks containing deal update data.
- **Agent**: Processes the data, interprets the intent, and determines the necessary synchronization actions.
- **Composio Toolset**: Executes the API calls to update records in your connected sales and project tools.
- **Chat Output**: Returns a confirmation summary of the sync operation or flags any errors for review.

### 3) Run the Flow
Use the Playground to test the synchronization logic:
- `Sync all deals from the 'Negotiation' stage in HubSpot to the 'Active' board in Jira.`
- `Update the close date for deal ID 98765 to next Friday across all connected platforms.`
- `Check for any stalled deals in the pipeline that haven't been updated in the last two weeks.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer, translating natural language or webhook data into structured API commands.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate field mapping.
- Instruction: "You are a sales data synchronization expert. Map incoming deal data to the correct CRM fields and ensure consistency across all connected platforms."
- Instruction: "If a conflict occurs, prioritize the data from the primary CRM and log the discrepancy in the output."

### 2) Composio Toolset Node
- Provide your Composio API Key in the node settings to enable secure authentication.
- Set the connection scope to include read/write access for your specific CRM and project management tools.

### 3) Tool Availability
- **CRM Connectors**: Read/Write access for deal objects, stages, and custom fields.
- **Project Management APIs**: Capability to create, update, and move tasks/cards.
- **Data Validation Tools**: Logic to verify date formats and currency values before pushing updates.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage pipeline stages and follow-ups.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Multi-platform data synchronization and conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated data decay and formatting cleanup.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score high-value opportunities.
