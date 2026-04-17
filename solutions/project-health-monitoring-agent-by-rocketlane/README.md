# Project Health Monitoring Agent (Uplizd) - Proactively identify at-risk projects and automate intervention workflows

## Summary
The Project Health Monitoring Agent is an intelligent automation workflow designed to track project status, identify potential bottlenecks, and trigger corrective actions in real-time. By leveraging the Composio Toolset to integrate with project management platforms like Rocketlane, this solution helps project managers and operations teams maintain pipeline velocity, ensure data hygiene, and prevent project slippage before it impacts delivery timelines.

---

## Demo
![Project Health Monitoring Agent dashboard showing real-time risk alerts and automated intervention triggers](image.png)
**Alt text (SEO-ready):** Project health monitoring agent dashboard for Rocketlane tracking project risk, pipeline velocity, and automated intervention workflows on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0d3c5d43-da20-5972-8fcc-e036b304b823)

---

## Category
**Primary category:** Project Management  
**Secondary tags:** rocketlane, project health, automation, pipeline velocity, risk management, composio, ai workflow, data monitoring.  
This solution bridges the gap between raw project data and actionable insights by automating the oversight of complex delivery lifecycles.

---

## Who is this for?
This agent is built for teams managing high-stakes delivery pipelines who need to reduce manual oversight.

- **Project Managers**
    - Automate the identification of stalled tasks and overdue milestones to keep projects on track.
- **Operations Leads**
    - Gain a bird's-eye view of portfolio health across multiple client engagements.
- **Customer Success Managers**
    - Receive proactive alerts when project health scores drop, allowing for timely client communication.
- **Delivery Directors**
    - Standardize intervention strategies to ensure consistent project outcomes across the organization.

---

## Features
- **Real-time Risk Detection**
    - Continuously monitors project milestones and status updates to flag potential delays before they become critical.
- **Automated Intervention Logic**
    - Triggers predefined workflows or notifications when a project health metric falls below a specific threshold.
- **Composio-Powered Integration**
    - Seamlessly connects with Rocketlane and other project management tools to fetch and update project data in real-time.
- **Customizable Health Scoring**
    - Allows users to define what "healthy" looks like based on custom field values, deadlines, and task completion rates.
- **Actionable Insight Generation**
    - Provides AI-driven recommendations for next steps, helping teams resolve bottlenecks faster.

---

## Use Cases
**Proactive Risk Mitigation**
- Automatically flag projects where the "Last Activity" date exceeds a 3-day threshold.
- Notify stakeholders when a critical path milestone is marked as "At Risk" in Rocketlane.

**Operational Efficiency**
- Sync project status updates across internal communication channels to reduce manual reporting time.
- Generate weekly summary reports of all "Red" status projects for leadership review.

**Data Hygiene & Compliance**
- Identify projects missing mandatory documentation or required custom field inputs.
- Ensure all project timelines are updated to reflect current resource availability and constraints.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project environment.
3. Authenticate your Rocketlane connection via the Composio integration portal.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual query regarding project status.
- **Agent**: Analyzes project data against defined health criteria and determines the necessary intervention.
- **Composio Toolset**: Executes read/write operations within Rocketlane to fetch project details or update task statuses.
- **Chat Output**: Delivers the final summary, risk alert, or confirmation of the automated action taken.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Check the health of all active projects and list those with overdue milestones.`
- `Identify projects that haven't been updated in the last 5 days and flag them for review.`
- `Generate a summary of the current project portfolio and highlight any high-risk accounts.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets project data and applies business logic.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on how to interpret "Risk" vs "Healthy" status labels.
- Define the tone for automated notifications to ensure consistency with your team's communication style.

### 2) Composio Toolset Node
- Ensure your Rocketlane API key is securely stored in your environment variables.
- Configure the connection scope to include read/write access for projects, tasks, and custom fields.

### 3) Tool Availability
- **Project Fetcher**: Retrieves metadata for active project lists.
- **Milestone Auditor**: Scans task completion dates and status flags.
- **Status Updater**: Modifies project health fields or adds comments when interventions are triggered.
- **Notification Dispatcher**: Sends alerts to designated channels or stakeholders.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational efficiency of your internal automation workflows.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track account health based on usage metrics and form submissions.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign action items based on project urgency.
