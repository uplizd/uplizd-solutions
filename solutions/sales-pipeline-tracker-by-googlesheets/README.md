# Sales Pipeline Tracker (Uplizd) - Automated deal stage management and revenue forecasting

## Summary
The Sales Pipeline Tracker is an intelligent Uplizd workflow designed to streamline sales operations by automatically synchronizing deal stages and updating revenue forecasts within Google Sheets. By leveraging the Composio Toolset to bridge communication between CRM data and spreadsheet tracking, this solution eliminates manual entry errors, ensures a single source of truth for sales teams, and significantly increases pipeline velocity for RevOps professionals.

---

## Demo
![Sales Pipeline Tracker workflow diagram showing CRM data flowing into Google Sheets via Uplizd](image.png)
**Alt text (SEO-ready):** Uplizd Sales Pipeline Tracker workflow diagram, automating CRM deal stage updates and revenue forecasting via Google Sheets and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/282f2e43-1861-5eac-b7f3-f61ab611d124)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, google sheets, pipeline, revenue forecasting, salesops, data sync, composio, ai workflow
- This solution bridges the gap between CRM platforms and spreadsheet-based reporting to maintain accurate, real-time sales pipeline visibility.

---

## Who is this for?
This solution is built for sales and operations teams looking to automate manual tracking and improve forecast accuracy.

- **Sales Operations Manager**
    - Eliminates manual data entry and reduces reporting latency across the sales organization.
- **Account Executive**
    - Ensures deal stages are always up-to-date, allowing for more accurate commission and quota tracking.
- **Revenue Operations (RevOps) Lead**
    - Maintains a single source of truth for pipeline health and revenue projections across disparate tools.
- **Sales Director**
    - Gains real-time visibility into deal progression and team performance without waiting for manual updates.

---

## Features
- **Automated Stage Sync**
    - Real-time updates to deal stages in Google Sheets whenever a change is detected in the CRM.
- **Revenue Forecasting**
    - Dynamic calculation of projected revenue based on current pipeline stages and deal values.
- **Composio-Powered Connectivity**
    - Seamless integration with CRM APIs and Google Sheets via the Composio Toolset for secure data handling.
- **Data Hygiene Enforcement**
    - Standardizes deal naming and formatting conventions during the synchronization process.
- **Proactive Alerting**
    - Triggers notifications or updates when high-value deals stall or move into critical closing stages.

---

## Use Cases
**Pipeline Visibility**
- Automatically populate a master Google Sheet with all active opportunities from the CRM.
- Sync deal stage changes instantly to keep leadership dashboards accurate.

**Revenue Management**
- Aggregate total weighted pipeline value by stage for monthly forecasting reports.
- Flag deals that have remained in a single stage beyond the defined sales cycle duration.

**Sales Operations Efficiency**
- Map custom CRM fields to specific columns in Google Sheets for customized reporting.
- Automate the cleanup of closed-lost or stale deals to keep the active pipeline focused.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to access the template.
2. Select "Import" to add the workflow to your Uplizd workspace.
3. Connect your Google Sheets and CRM accounts via the integration settings.
4. Ensure nodes are correctly mapped and all required API scopes are authorized.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to refresh pipeline data.
- **Agent**: Interprets the request and orchestrates the data extraction and formatting logic.
- **Composio Toolset**: Executes the API calls to fetch CRM data and write updates to Google Sheets.
- **Chat Output**: Confirms the successful synchronization or reports any data mapping errors.

### 3) Run the Flow
Use the Playground to test your pipeline synchronization:
- `Sync all active deals from the CRM to the master pipeline sheet.`
- `Update the revenue forecast for the current quarter in Google Sheets.`
- `Identify and flag all deals that have been in the 'Discovery' stage for over 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for data transformation and mapping.
- Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a sales operations assistant. Map CRM deal objects to the specified Google Sheet columns accurately."
- Instruction: "Maintain strict data formatting for currency and date fields during the sync process."

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure connectivity.
- Ensure the connection scope includes read access to your CRM and write access to your target Google Sheet.

### 3) Tool Availability
- **CRM Connector**: For fetching deal objects, stages, and revenue values.
- **Google Sheets API**: For appending rows, updating cells, and clearing stale data.
- **Data Parser**: For transforming raw CRM JSON into spreadsheet-compatible formats.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates deep-dive research on prospective accounts.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages pipeline stages and identifies stalled opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes data between multiple CRM platforms and external databases.
