# Employee Wellness Monitor (Uplizd) - Automate work-life balance and health tracking

## Summary
The Employee Wellness Monitor is an intelligent Uplizd workflow that integrates with DeskTime to track work patterns, identify potential burnout indicators, and promote sustainable work habits. By analyzing real-time activity data, this solution provides actionable insights for managers and employees to maintain productivity without compromising well-being, serving as a single source of truth for workforce health and operational hygiene.

---

## Demo
![Employee Wellness Monitor dashboard showing work pattern anomalies and health alerts](image.png)
**Alt text (SEO-ready):** Employee Wellness Monitor Uplizd workflow dashboard showing work pattern anomalies, DeskTime integration, and health alerts for improved workforce productivity.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1194a049-07b9-561b-9550-c8952018c962)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** desktime, employee wellness, workforce management, productivity, burnout prevention, data hygiene, composio, ai workflow
- This solution bridges the gap between raw time-tracking data and proactive human resource management through automated AI analysis.

---

## Who is this for?
This solution is designed for organizations prioritizing employee retention and sustainable performance.

- **HR Managers**
    - Identify teams at risk of burnout before turnover occurs.
- **Operations Leads**
    - Optimize resource allocation based on actual work-pattern data.
- **Team Leads**
    - Foster a culture of transparency and healthy work-life balance.
- **Individual Contributors**
    - Receive personalized nudges to take breaks and maintain focus.

---

## Features
- **Real-time Activity Sync**
  Seamlessly pulls time-tracking data from DeskTime to ensure the AI always has the latest work-pattern context.
- **Burnout Anomaly Detection**
  Uses advanced LLM reasoning to flag irregular hours, excessive overtime, or lack of breaks.
- **Automated Wellness Nudges**
  Triggers proactive notifications or reports when specific health thresholds are breached.
- **Productivity Trend Analysis**
  Aggregates historical data to visualize long-term work habits and team performance cycles.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely connect and query DeskTime APIs without manual data exports.

---

## Use Cases
**Burnout Prevention**
- Automatically flag employees working more than 10 hours for three consecutive days.
- Generate weekly wellness reports for managers highlighting teams with high intensity scores.

**Operational Efficiency**
- Identify "always-on" patterns that correlate with decreased output quality.
- Correlate break frequency with task completion rates to optimize daily schedules.

**Policy Compliance**
- Monitor adherence to company-wide "no-email" or "offline" hours policies.
- Generate audit logs for HR to ensure compliance with regional labor regulations regarding rest periods.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and import the Employee Wellness Monitor workflow.
3. Connect your DeskTime API credentials via the Composio integration portal.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Accepts user queries or trigger signals for wellness reports.
- **Agent**: Processes DeskTime data to identify patterns and generate insights.
- **Composio Toolset**: Executes secure API calls to fetch and filter time-tracking metrics.
- **Chat Output**: Delivers the final wellness summary or alert to the dashboard.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Analyze the last 7 days of work patterns for the Engineering team and highlight any burnout risks.`
- `Which employees have been working consistently over 9 hours daily this week?`
- `Generate a summary of break-taking habits for the Marketing department.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an analytical HR assistant.
- Focus on objective data interpretation rather than subjective judgment.
- Maintain a supportive, non-punitive tone in all generated reports.
- Prioritize privacy by anonymizing individual data points in team-wide summaries.

### 2) Composio Toolset Node
- Requires a valid DeskTime API Key with read-only access to time-tracking and activity logs.
- Connection scope should be limited to the specific departments being monitored.

### 3) Tool Availability
- `desktime_get_activity_logs`: Retrieves raw time-tracking data.
- `desktime_get_user_stats`: Fetches aggregated performance metrics per user.
- `desktime_list_teams`: Identifies team structures for segmented reporting.

---

## Related Solutions
- [Work Hours Compliance Monitor](../work-hours-compliance-monitor-by-timely/README.md) - Ensures team adherence to scheduled working hours.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks overall team operational health and communication patterns.
- [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) - Proactively identifies and mitigates workplace risks.
