# Property Portfolio Auditor (Uplizd) - Automated real estate asset health and performance monitoring

## Summary
The Property Portfolio Auditor is an intelligent Uplizd workflow designed to streamline the oversight of vacation rental assets managed via Lodgify. By automating data extraction and performance analysis, this solution provides property managers with a single source of truth for occupancy rates, revenue metrics, and maintenance status, significantly increasing operational pipeline velocity and data hygiene across your entire portfolio.

---

## Demo
![Property Portfolio Auditor workflow dashboard showing automated Lodgify data synchronization and asset health metrics](image.png)
**Alt text (SEO-ready):** Property Portfolio Auditor Uplizd workflow for Lodgify, featuring automated real estate asset health monitoring, rental performance tracking, and data synchronization.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/81ea1363-64a9-5a79-81f0-236013765fd9)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** lodgify, property management, real estate, asset audit, portfolio monitoring, data sync, workflow automation, ai agent
- This solution bridges the gap between raw rental data and actionable insights, ensuring your property portfolio remains optimized and compliant.

---

## Who is this for?
This solution is built for professionals managing short-term rentals who need to maintain high occupancy and operational standards.

- **Property Managers**
  - Automate routine portfolio health checks to identify underperforming assets before they impact revenue.
- **Real Estate Investors**
  - Gain a consolidated view of portfolio performance metrics without manual spreadsheet consolidation.
- **Operations Leads**
  - Ensure data hygiene across Lodgify accounts by flagging discrepancies in property listings and booking status.
- **Revenue Managers**
  - Receive real-time alerts on booking trends and occupancy gaps to adjust pricing strategies dynamically.

---

## Features
- **Automated Portfolio Sync**
  - Seamlessly pulls real-time property data from Lodgify using the Composio Toolset for up-to-date reporting.
- **Performance Health Scoring**
  - Evaluates individual property metrics against portfolio benchmarks to highlight high-growth and stagnant assets.
- **Data Hygiene Audits**
  - Automatically identifies missing listing information, incomplete booking details, or formatting inconsistencies.
- **Proactive Alerting**
  - Triggers notifications based on custom thresholds for occupancy drops or maintenance-related status changes.
- **Centralized Reporting**
  - Aggregates complex rental data into clear, actionable summaries for stakeholders and management teams.

---

## Use Cases
**Portfolio Performance Analysis**
- Identify properties with occupancy rates falling below 60% over a rolling 30-day window.
- Compare revenue generation across different geographic regions within your Lodgify account.

**Operational Data Cleanup**
- Detect and flag listings missing high-quality images or essential amenity descriptions.
- Standardize property naming conventions and status tags across the entire portfolio for better searchability.

**Asset Maintenance Tracking**
- Monitor property status updates to ensure maintenance tickets are reflected in the booking availability calendar.
- Generate weekly summaries of property downtime due to repairs or renovations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import" option.
2. Upload the `property-portfolio-auditor-by-lodgify` configuration file.
3. Connect your Lodgify credentials via the Composio integration portal.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your audit request or specific property query.
- **Agent**: Processes the request, interprets Lodgify data, and performs the audit logic.
- **Composio Toolset**: Executes secure API calls to fetch and update property data.
- **Chat Output**: Delivers the final audit report or status summary back to the user.

### 3) Run the Flow
Use the Playground to test your auditor with these prompts:
- `Audit my entire portfolio and highlight properties with occupancy below 50% for the last month.`
- `Check for any missing amenity data in my active Lodgify listings.`
- `Generate a summary report of all maintenance-related status changes from the past week.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized real estate analyst.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a Property Portfolio Auditor. Focus on identifying performance gaps and data inconsistencies."
- Ensure the agent maintains a professional, data-driven tone in all generated reports.

### 2) Composio Toolset Node
- Requires a valid Lodgify API key configured within the Composio dashboard.
- Scope should include read/write access to property listings, bookings, and account settings.

### 3) Tool Availability
- **Property Fetcher**: Retrieves listing details and current status.
- **Booking Analyzer**: Aggregates occupancy and revenue data.
- **Data Validator**: Scans for missing fields and formatting errors.
- **Notification Dispatcher**: Sends alerts for critical performance drops.

---

## Related Solutions
- [../crm-data-hygiene-manager/README.md](CRM Data Hygiene Manager) — Automate data cleanup and formatting across your CRM.
- [../account-health-usage-monitor-by-jotform/README.md](Account Health Usage Monitor) — Track user engagement and account health metrics.
- [../workflow-automation-agent-by-jobnimbus/README.md](Workflow Automation Agent) — Streamline operational tasks and project management workflows.
