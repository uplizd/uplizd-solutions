# Sprint Health Monitor (Uplizd) - Automated Jira sprint risk detection and velocity tracking

## Summary
The Sprint Health Monitor (Uplizd) is an intelligent AI workflow designed to provide real-time visibility into Jira sprint progress. By analyzing ticket status, completion rates, and potential bottlenecks, this solution empowers engineering teams and managers to proactively address risks, maintain pipeline velocity, and ensure sprint commitments are met with data-driven precision.

---

## Demo
![Sprint Health Monitor dashboard showing real-time Jira ticket status and risk alerts](image.png)
**Alt text (SEO-ready):** Sprint Health Monitor dashboard showing real-time Jira ticket status, risk alerts, and velocity metrics within the Uplizd AI workflow and Composio integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/78b84cbc-a4af-5d72-8b1d-8f07ab095496)

---

## Category
**Primary category:** Engineering Operations
**Secondary tags:** jira, sprint, velocity, project management, devops, ai workflow, composio, data sync.
This solution bridges the gap between raw Jira data and actionable project insights, streamlining sprint management through automated monitoring.

---

## Who is this for?
This solution is designed for technical teams and leadership focused on maintaining delivery consistency and operational transparency.

* **Engineering Managers**
    * Gain immediate visibility into stalled tickets and sprint-at-risk indicators without manual status meetings.
* **Scrum Masters**
    * Identify blockers early in the development lifecycle to keep the team focused on high-priority sprint goals.
* **Product Owners**
    * Monitor feature delivery timelines and adjust roadmap expectations based on real-time sprint velocity data.
* **Software Developers**
    * Reduce administrative overhead by automating status reporting and surfacing critical dependency issues.

---

## Features
- **Automated Sprint Risk Detection**
    Real-time monitoring of Jira boards to flag tickets that are stalled or unlikely to meet the sprint deadline.
- **Velocity Trend Analysis**
    Calculates team velocity based on historical completion rates to provide accurate forecasting for future sprints.
- **Composio-Powered Jira Integration**
    Seamlessly connects with your Jira instance to pull ticket metadata, status updates, and assignee information.
- **Proactive Alerting**
    Triggers notifications when critical tasks are blocked or when the sprint burn-down deviates from the expected trajectory.
- **Customizable Thresholds**
    Allows teams to define their own "health" metrics, ensuring the agent monitors what matters most to your specific workflow.

---

## Use Cases
**Sprint Risk Mitigation**
* Automatically flag tickets that have remained in the "In Progress" column for longer than the defined threshold.
* Identify high-priority bugs that have not been assigned or updated within the last 24 hours.

**Velocity & Capacity Planning**
* Calculate the average story points completed per sprint to assist in future capacity planning.
* Generate a summary of unfinished tasks at the end of a sprint to facilitate smoother carry-over processes.

**Team Communication & Hygiene**
* Summarize daily blockers for the team to review during stand-ups, reducing the need for manual Jira board scrubbing.
* Ensure all tickets have accurate labels and due dates by auditing sprint board hygiene automatically.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Flow" to add the Sprint Health Monitor to your workspace.
3. Configure your Jira credentials within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives your natural language queries regarding sprint status.
* **Agent**: Processes Jira data using LLM logic to interpret sprint health.
* **Composio Toolset**: Executes secure API calls to fetch and filter Jira project data.
* **Chat Output**: Delivers a human-readable summary of sprint risks and velocity metrics.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `What is the current health status of the active sprint?`
* `List all tickets that are currently blocked or stalled in the development pipeline.`
* `Calculate our average velocity over the last three sprints and identify any risks for the current cycle.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your technical project assistant.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Act as a Jira expert. Analyze the provided ticket data to identify risks and summarize sprint progress."
* Instruction: "Prioritize identifying blockers and providing actionable insights for the engineering team."

### 2) Composio Toolset Node
* Provide your Jira API key and ensure the connection scope includes `read:jira-work` and `read:jira-user`.
* Ensure the toolset is authorized to access the specific Jira project boards you wish to monitor.

### 3) Tool Availability
* `jira_search_issues`: To find tickets based on status, assignee, or priority.
* `jira_get_issue_details`: To pull deep-dive information on specific stalled tasks.
* `jira_list_projects`: To scope the agent's monitoring to relevant project boards.

---

## Related Solutions
* [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Track general team workflow efficiency and daily stand-up metrics.
* [Action Item Prioritizer by Rootly](../action-item-prioritizer-by-rootly/README.md) - Manage and rank incident response tasks and action items.
* [Account Health Usage Monitor by Jotform](../account-health-usage-monitor-by-jotform/README.md) - Monitor customer account health and usage metrics for success teams.
