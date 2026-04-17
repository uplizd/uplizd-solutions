# Performance Insight Reporter (Uplizd) - Automated website performance monitoring and reporting

## Summary
The Performance Insight Reporter is an intelligent Uplizd workflow that automates the collection, analysis, and reporting of website performance metrics using StatusCake. By integrating real-time uptime and latency data into a centralized reporting pipeline, this solution eliminates manual monitoring overhead, ensures rapid incident response, and provides stakeholders with actionable insights into site health and availability.

---

## Demo
![Performance Insight Reporter dashboard showing uptime metrics and automated incident alerts](image.png)
**Alt text (SEO-ready):** Performance Insight Reporter dashboard showing uptime metrics, automated incident alerts, and StatusCake integration for Uplizd AI workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/83367827-8ed7-52e9-b2b4-0dd091cb1411)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** performance monitoring, statuscake, uptime, site health, automated reporting, devops, api integration, composio
- This solution bridges the gap between raw infrastructure telemetry and business-ready performance reporting.

---

## Who is this for?
This workflow is designed for technical teams and stakeholders responsible for maintaining high-availability web services.

- **Site Reliability Engineers (SREs)**
    - Automate the generation of incident reports and uptime summaries to reduce manual documentation time.
- **DevOps Managers**
    - Gain immediate visibility into infrastructure performance trends across multiple environments.
- **Product Managers**
    - Monitor service level agreement (SLA) compliance through automated, recurring performance updates.
- **IT Operations Leads**
    - Receive proactive alerts and synthesized performance data to streamline troubleshooting workflows.

---

## Features
- **Automated Data Extraction**
    - Pulls real-time uptime and latency data directly from StatusCake via the Composio Toolset.
- **Intelligent Performance Analysis**
    - Uses the Agent node to synthesize raw monitoring logs into human-readable performance summaries.
- **Customizable Reporting Frequency**
    - Configures automated triggers to generate reports on a schedule or in response to specific uptime events.
- **Multi-Platform Integration**
    - Seamlessly connects monitoring data with communication channels for instant team notification.
- **Historical Trend Tracking**
    - Aggregates performance metrics over time to identify recurring bottlenecks or infrastructure degradation.

---

## Use Cases
**Incident Response Management**
- Automatically trigger a summary report when StatusCake detects a site outage or latency spike.
- Notify the on-call engineer with a pre-compiled list of affected endpoints and recent performance history.

**SLA Compliance Reporting**
- Generate weekly uptime reports for executive stakeholders to demonstrate adherence to service level agreements.
- Compare monthly performance benchmarks against historical data to track infrastructure improvement.

**Infrastructure Health Audits**
- Perform a deep-dive analysis of latency patterns across global server locations to optimize CDN routing.
- Identify underperforming assets that require immediate maintenance based on automated health scores.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Performance Insight Reporter template from the solution library.
3. Connect your StatusCake API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the request for performance data or triggers the automated report.
- **Agent**: Processes monitoring data and generates actionable insights based on system instructions.
- **Composio Toolset**: Executes secure API calls to StatusCake to fetch real-time site metrics.
- **Chat Output**: Delivers the final performance report to the user or designated notification channel.

### 3) Run the Flow
Use the Playground to test your reporting capabilities:
- `Generate a summary report of all website uptime metrics for the last 24 hours.`
- `Check the current latency status for the production environment and alert if it exceeds 200ms.`
- `Create a weekly performance trend report comparing this week's uptime against the previous period.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a technical analyst, converting raw API data into clear, actionable reporting.
- Focus on identifying anomalies, latency spikes, and uptime percentages.
- Maintain a professional, concise tone suitable for technical stakeholders.
- Prioritize clear, bulleted summaries for incident-related reports.

### 2) Composio Toolset Node
- Requires a valid StatusCake API Key with read-only access to monitoring data.
- Connection scope should be limited to the specific sites or tags you wish to monitor.

### 3) Tool Availability
- `get_uptime_metrics`: Fetches current availability status for monitored URLs.
- `get_latency_history`: Retrieves historical response time data for performance trend analysis.
- `list_alerts`: Pulls active incident reports to include in the summary output.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track and report on account activity and usage metrics.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor the operational status of your automated business processes.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform security and configuration audits on your infrastructure.
