# Sales Report Automation Agent (Uplizd) - Streamline weekly sales reporting and data formatting

## Summary
The Sales Report Automation Agent is an intelligent workflow designed to eliminate manual data entry by automatically aggregating, cleaning, and formatting raw sales data into professional reports. By leveraging the Composio Toolset to interface with spreadsheet and CRM platforms, this solution provides RevOps teams and sales managers with a single source of truth, significantly reducing pipeline reporting latency and ensuring data hygiene across the organization.

---

## Demo
![Sales Report Automation Agent dashboard showing automated data aggregation and report generation](image.png)
**Alt text (SEO-ready):** Uplizd Sales Report Automation Agent workflow interface for automated CRM data processing, spreadsheet reporting, and sales pipeline analytics.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6o3952gAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAACRSURBVDjLY2AYBaNgFIyCUUAHAAABAAAB)](https://uplizd.ai/solutions/2234daec-95dd-5eeb-ac8e-fd22731cbd61)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, excel, sales reporting, data sync, pipeline, automation, composio, ai workflow
- This solution bridges the gap between raw CRM data and actionable management insights through automated report generation.

---

## Who is this for?
This solution is designed for professionals who need to transform complex sales data into clear, actionable reporting without manual overhead.

- **Sales Operations Manager**
    - Automates the consolidation of weekly performance metrics across disparate regional teams.
- **Account Executive**
    - Reduces time spent on administrative reporting, allowing for more focus on high-value client interactions.
- **Revenue Analyst**
    - Ensures data accuracy in quarterly forecasts by eliminating human error in manual spreadsheet updates.
- **Sales Director**
    - Gains real-time visibility into pipeline health and conversion trends through standardized automated reporting.

---

## Features
- **Automated Data Aggregation**
    - Connects directly to CRM and spreadsheet sources via Composio to pull raw sales figures in real-time.
- **Intelligent Formatting**
    - Uses AI to apply consistent styling, headers, and conditional formatting to generated reports.
- **Error Detection & Hygiene**
    - Identifies and flags missing fields or anomalous entries before the final report is compiled.
- **Scheduled Delivery Triggers**
    - Configurable to run on specific cadences, ensuring reports are ready exactly when leadership needs them.
- **Cross-Platform Integration**
    - Seamlessly bridges data between CRM platforms and external analytical tools or shared drives.

---

## Use Cases
**Weekly Pipeline Reviews**
- Automatically generate a summary of all deals closed-won versus closed-lost for the previous week.
- Format team-specific performance summaries to be shared directly in executive Slack or email channels.

**Quarterly Forecasting**
- Aggregate historical sales data to identify trends in deal velocity and average contract value.
- Compare current quarter projections against historical benchmarks to highlight potential revenue gaps.

**Data Hygiene Audits**
- Scan CRM records for incomplete contact information or missing deal stages during the report generation process.
- Export clean, sanitized datasets for use in external business intelligence dashboards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your preferred workspace to initialize the workflow.
3. Authenticate your CRM and Spreadsheet integrations within the Composio connection manager.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all API connections are active.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or date range for the requested report.
- **Agent**: Interprets the request and orchestrates the data retrieval and formatting logic.
- **Composio Toolset**: Executes secure API calls to fetch and push data to your sales platforms.
- **Chat Output**: Delivers the final report link or summary text to the user.

### 3) Run the Flow
Use the Playground to test your automation with the following prompts:
- `Generate a weekly sales performance report for the North American team.`
- `Create a summary of all stalled deals from the last 30 days.`
- `Format the latest Q3 pipeline data into a clean spreadsheet structure.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your sales data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for complex data interpretation.
- Instruction: "You are a Sales Operations assistant. Prioritize accuracy in data extraction and maintain a professional, concise tone in all generated reports."
- Instruction: "Always verify the date range provided by the user before querying the CRM."

### 2) Composio Toolset Node
- Provide your unique Composio API key in the node settings.
- Ensure the connection scope includes read/write access to your CRM (e.g., Salesforce, HubSpot) and spreadsheet tools (e.g., Google Sheets, Excel).

### 3) Tool Availability
- **CRM Connector**: Fetch deal, contact, and account objects.
- **Spreadsheet API**: Create, update, and format rows/columns in target files.
- **Notification Service**: Send report summaries via email or messaging platforms.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage pipeline stages and identify stalled deals.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate data cleanup and formatting compliance.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score new sales opportunities.
