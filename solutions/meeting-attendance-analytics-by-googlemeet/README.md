# Meeting Attendance Analytics (Uplizd) - Optimize team engagement and meeting productivity

## Summary
The Meeting Attendance Analytics workflow by Uplizd provides a centralized system for tracking, analyzing, and reporting on meeting participation patterns. By integrating directly with Google Meet data, this solution enables managers and operations teams to identify engagement trends, optimize scheduling, and ensure high-value attendance, ultimately driving better meeting hygiene and organizational pipeline velocity.

---

## Demo
![Meeting Attendance Analytics dashboard showing participant engagement trends and Google Meet integration](image.png)
**Alt text (SEO-ready):** Meeting Attendance Analytics dashboard showing participant engagement trends and Google Meet integration for Uplizd AI workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/244eb3a6-ead5-53cc-a609-e77d2859153a)

---

## Category
**Primary category:** Operations  
**Secondary tags:** google meet, meeting analytics, team engagement, productivity, data sync, ai workflow, composio, operations  
This solution bridges the gap between raw meeting data and actionable insights to improve team collaboration and meeting efficiency.

---

## Who is this for?
This solution is designed for teams looking to transform passive meeting data into active management insights.

*   **Operations Managers**
    *   Gain visibility into meeting attendance trends to optimize resource allocation and meeting frequency.
*   **Team Leads**
    *   Identify disengagement patterns early to improve team morale and meeting participation.
*   **Project Managers**
    *   Ensure key stakeholders are present for critical project syncs and decision-making sessions.
*   **HR Business Partners**
    *   Monitor organizational meeting culture to prevent burnout and ensure effective communication channels.

---

## Features
- **Automated Data Sync**
    - Seamlessly pull attendance logs from Google Meet into your centralized reporting environment using the Composio Toolset.
- **Engagement Scoring**
    - Automatically calculate attendance rates and engagement metrics to highlight high-value vs. low-value meetings.
- **Real-time Alerts**
    - Receive notifications when critical stakeholders miss essential meetings or when attendance drops below a defined threshold.
- **Trend Analysis**
    - Visualize long-term participation data to identify seasonal or project-based attendance decay.
- **Actionable Reporting**
    - Generate summary reports that provide clear recommendations for scheduling adjustments and meeting optimization.

---

## Use Cases
**Meeting Hygiene Optimization**
*   Identify recurring meetings with consistently low attendance for potential consolidation or cancellation.
*   Analyze the correlation between meeting duration and participant drop-off rates to refine scheduling.

**Stakeholder Accountability**
*   Track attendance for mandatory project updates to ensure cross-functional alignment.
*   Generate weekly reports on key stakeholder participation to support project governance.

**Team Performance Insights**
*   Correlate meeting attendance patterns with project milestone completion to identify potential bottlenecks.
*   Assess the impact of meeting timing on team participation levels across different time zones.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Attendance Analytics template from the solution library.
3. Connect your Google Workspace credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the request for meeting data or specific date ranges.
*   **Agent**: Interprets the query and orchestrates the data retrieval and analysis logic.
*   **Composio Toolset**: Executes the API calls to Google Meet to fetch attendance logs.
*   **Chat Output**: Returns the processed analytics, trends, and actionable insights to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Analyze meeting attendance for the 'Q3 Project Sync' series over the last 30 days.`
* `Which team members have missed more than 50% of the weekly leadership meetings this month?`
* `Generate a report on meeting engagement trends for the engineering department.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your data analyst, translating natural language queries into structured data requests.
*   Maintain a professional, analytical tone in all generated summaries.
*   Prioritize identifying trends and anomalies in attendance data.
*   Always provide clear, bulleted recommendations based on the analyzed metrics.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Google Workspace API key is active with read-only access to calendar and meeting events.
*   **Connection Scope**: Configure the scope to include `calendar.events.readonly` and `meet.attendance.read`.

### 3) Tool Availability
*   **Google Meet API**: For fetching participant lists and meeting duration.
*   **Google Calendar API**: For cross-referencing meeting metadata and attendee lists.
*   **Data Processor**: For calculating attendance percentages and trend analysis.

---

## Related Solutions
* [Zoom Usage Intelligence Agent](../zoom-usage-intelligence-agent/README.md) - Track and analyze meeting patterns across the Zoom platform.
* [Workflow Health Monitor](../workflow-health-monitor/README.md) - Monitor the operational efficiency and health of your automated business workflows.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically prioritize and track action items derived from meeting transcripts.
