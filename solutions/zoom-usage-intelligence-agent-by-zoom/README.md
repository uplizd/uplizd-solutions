# Zoom Usage Intelligence Agent (Uplizd) - Optimize meeting efficiency and platform utilization

## Summary
The Zoom Usage Intelligence Agent is an automated workflow designed to track, analyze, and report on meeting metrics and platform utilization. By leveraging the Composio Toolset to interface directly with Zoom’s API, this agent provides actionable insights into meeting frequency, participant engagement, and resource allocation, helping organizations reduce "Zoom fatigue" and maximize ROI on their communication stack.

---

## Demo
![Zoom Usage Intelligence Agent dashboard showing meeting analytics and participant engagement metrics](image.png)
**Alt text (SEO-ready):** Zoom Usage Intelligence Agent dashboard displaying meeting analytics, participant engagement metrics, and Uplizd workflow automation for platform optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0abb27a4-eb06-59d8-b2e6-0ab50d2531b3)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** zoom, analytics, meeting intelligence, productivity, data sync, workflow automation, composio, ai agent
- This solution bridges the gap between raw Zoom usage data and strategic decision-making by automating the extraction and analysis of meeting performance metrics.

---

## Who is this for?
This agent is designed for teams looking to gain visibility into their digital collaboration habits and improve meeting culture.

- **IT Administrators**
    - Automate the monitoring of license utilization and identify inactive accounts to optimize software spend.
- **Operations Managers**
    - Analyze meeting duration and frequency to identify bottlenecks in cross-departmental communication.
- **HR Business Partners**
    - Track engagement trends to proactively address burnout and improve employee well-being.
- **Team Leads**
    - Gain insights into meeting efficiency to ensure team time is spent on high-impact collaboration.

---

## Features
- **Automated Usage Tracking**
    - Real-time ingestion of meeting data, including participant counts, duration, and scheduling frequency via the Composio Toolset.
- **Engagement Analytics**
    - Advanced processing of meeting metadata to highlight trends in participation and identify high-frequency meeting patterns.
- **Cost Optimization Insights**
    - Identification of underutilized Zoom licenses and meeting rooms to streamline subscription costs and resource allocation.
- **Customizable Reporting**
    - Automated generation of summary reports that can be routed directly to stakeholders or integrated into existing BI dashboards.
- **Proactive Alerting**
    - Intelligent triggers that notify managers when specific usage thresholds or meeting duration limits are consistently exceeded.

---

## Use Cases
**Meeting Efficiency Audits**
- Identify recurring meetings with low participant engagement or excessive duration.
- Analyze the ratio of "productive" meeting time versus total time spent in calls.

**Resource & License Management**
- Audit inactive user accounts to reclaim licenses and reduce monthly SaaS expenditure.
- Monitor meeting room utilization to determine if current physical or virtual infrastructure meets team needs.

**Communication Health Monitoring**
- Detect "meeting overload" trends across specific departments or project teams.
- Correlate meeting frequency with project delivery timelines to ensure optimal balance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Zoom Usage Intelligence Agent.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your Zoom account via the Composio connection prompt.
4. Ensure nodes are correctly linked from Chat Input to Agent, then to the Composio Toolset, and finally to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding meeting data or specific date ranges.
- **Agent**: Processes natural language requests and maps them to specific Zoom API calls.
- **Composio Toolset**: Executes the authenticated requests to fetch meeting reports and user activity.
- **Chat Output**: Formats the retrieved data into clear, actionable insights or summary tables.

### 3) Run the Flow
Use the Playground to test the agent with prompts such as:
- `Show me a summary of meeting activity for the marketing team over the last 30 days.`
- `Identify all users who have not hosted a meeting in the past 60 days.`
- `Which recurring meetings are lasting longer than 90 minutes on average?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data analyst specialized in Zoom platform metrics.
- Focus on extracting quantitative data from API responses.
- Maintain a neutral, analytical tone when presenting usage statistics.
- Prioritize identifying outliers or anomalies in meeting behavior.

### 2) Composio Toolset Node
- Requires a valid Zoom API key and OAuth connection scope.
- Ensure the agent has "Read" permissions for reports, users, and meetings.

### 3) Tool Availability
- `zoom_get_meeting_reports`: Fetches detailed metrics for specific meeting instances.
- `zoom_list_users`: Retrieves user activity status and account details.
- `zoom_get_account_usage`: Aggregates platform-wide meeting statistics.

---

## Related Solutions
- [Workspace Usage Analyzer](../workspace-usage-analyzer-by-baserow/README.md) - Track and optimize workspace resource utilization.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor the efficiency and status of team workflows.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track account engagement and health metrics.
