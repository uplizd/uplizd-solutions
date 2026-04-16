# Automated Sales Dashboard with Google Sheets (Uplizd) - Real-time pipeline visualization and data synchronization

## Summary
The Automated Sales Dashboard with Google Sheets workflow enables sales teams to maintain a real-time, single source of truth by automatically syncing CRM opportunity data into structured spreadsheet reports. By leveraging the Composio Toolset to bridge CRM platforms and Google Sheets, this solution eliminates manual data entry, reduces reporting latency, and provides RevOps teams with immediate visibility into pipeline health and performance metrics.

---

## Demo
![Automated Sales Dashboard with Google Sheets workflow showing CRM data syncing to a spreadsheet](image.png)
**Alt text (SEO-ready):** Automated Sales Dashboard with Google Sheets, Uplizd workflow for CRM data synchronization, sales pipeline reporting, and automated spreadsheet updates via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/31332203-f843-5822-831f-6a91fd08053d)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, google sheets, sales pipeline, data sync, revops, reporting, automation, composio
- This solution bridges the gap between complex CRM environments and accessible spreadsheet reporting to drive data-informed decision-making.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate their reporting infrastructure and improve data accessibility.

- **Sales Operations Manager**
    - Automates the generation of weekly pipeline reports without manual spreadsheet maintenance.
- **Account Executive**
    - Gains instant visibility into deal status and upcoming milestones directly within their preferred tracking sheet.
- **Revenue Analyst**
    - Ensures data integrity across platforms by syncing CRM opportunity fields to Google Sheets in real-time.
- **Sales Director**
    - Monitors team performance and pipeline velocity through live, auto-updating dashboards.

---

## Features
- **Real-time Data Sync**
    - Automatically pushes CRM opportunity updates to Google Sheets as soon as they occur.
- **Customizable Mapping**
    - Easily map specific CRM fields like deal stage, close date, and amount to your preferred spreadsheet columns.
- **Composio Toolset Integration**
    - Utilizes secure API connections to bridge CRM platforms and Google Sheets seamlessly.
- **Automated Formatting**
    - Ensures incoming data is cleaned and formatted correctly upon entry into the spreadsheet.
- **Pipeline Health Alerts**
    - Triggers updates that highlight stalled deals or high-priority opportunities within the dashboard view.

---

## Use Cases
**Pipeline Performance Tracking**
- Automatically log new opportunities into a master tracker as they are created in the CRM.
- Update deal stages in real-time to reflect the most current status of the sales funnel.

**Sales Forecasting**
- Aggregate monthly revenue projections by syncing weighted deal values to a forecasting sheet.
- Track historical close rates by maintaining a persistent log of won and lost opportunities.

**Data Hygiene and Cleanup**
- Identify and flag missing data points in the CRM by comparing them against required spreadsheet fields.
- Standardize naming conventions across sales records during the synchronization process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your CRM and Google Sheets accounts within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives commands to refresh data or generate specific report views.
- **Agent**: Processes natural language requests and orchestrates data retrieval from the CRM.
- **Composio Toolset**: Executes the API calls to read CRM data and write updates to Google Sheets.
- **Chat Output**: Confirms successful synchronization or provides a summary of the updated dashboard metrics.

### 3) Run the Flow
Use the Playground to test your dashboard automation:
- `Sync all open opportunities from the CRM to the Sales Dashboard sheet.`
- `Update the 'Q3 Forecast' tab with the latest deal stages from Salesforce.`
- `Identify any stalled deals in the pipeline and add them to the 'Action Required' sheet.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the bridge between your natural language requests and the API toolset.
- Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a data synchronization assistant. Map CRM opportunity fields to the specified Google Sheets columns accurately."
- Instruction: "Always verify the existence of the target sheet before attempting to write data."

### 2) Composio Toolset Node
- Provide your **Composio API Key** in the node configuration.
- Ensure the connection scope includes `crm:read` and `googlesheets:write` permissions.

### 3) Tool Availability
- **CRM Connector**: Fetch, filter, and update opportunity records.
- **Google Sheets Connector**: Append rows, update cells, and format spreadsheet ranges.
- **Data Transformer**: Clean and normalize field values before synchronization.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates gathering deep intelligence on target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Facilitates multi-platform data synchronization and conflict resolution.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages pipeline stages and automates follow-up actions for sales teams.
