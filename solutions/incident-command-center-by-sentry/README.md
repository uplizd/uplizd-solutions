# Incident Command Center (Uplizd) - Automated incident response and team coordination

## Summary
The Incident Command Center by Sentry streamlines your technical response lifecycle by automating incident triage, communication, and resolution workflows. By integrating real-time monitoring alerts with collaborative tools, this Uplizd AI workflow ensures that engineering teams maintain high system reliability, reduce mean time to resolution (MTTR), and keep stakeholders informed without manual overhead.

---

## Demo
![Incident Command Center dashboard showing automated Sentry alert triage and team notification workflow](image.png)
**Alt text (SEO-ready):** Incident Command Center dashboard showing automated Sentry alert triage, incident response orchestration, and team notification workflow on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMTJoM3Y5aDZ2LTZoMnY2aDZ2LTloM0wxMiAyeiIvPjwvc3ZnPg==)](https://uplizd.ai/solutions/33f48045-7754-59dc-b861-76366d18787e)

---

## Category
**Primary category:** Operations  
**Secondary tags:** incident management, sentry, devops, alert triage, automation, reliability engineering, composio, ai workflow  
This solution acts as a central nervous system for technical operations, bridging the gap between Sentry monitoring and team response tools.

---

## Who is this for?
This solution is designed for technical teams looking to minimize downtime and eliminate manual incident coordination overhead.

- **Site Reliability Engineer (SRE)**
    - Automate the initial triage of incoming Sentry alerts to reduce alert fatigue.
- **Engineering Manager**
    - Gain visibility into incident response times and team workload distribution.
- **DevOps Lead**
    - Standardize incident response playbooks across distributed engineering squads.
- **Support Operations Specialist**
    - Ensure timely communication to stakeholders when critical system incidents occur.

---

## Features
- **Automated Alert Triage**
  Intelligently filters and categorizes incoming Sentry errors based on severity and impact.
- **Cross-Platform Notification**
  Automatically triggers alerts in Slack, PagerDuty, or Jira to ensure the right team is notified instantly.
- **Contextual Incident Enrichment**
  Attaches relevant stack traces and recent deployment data to incident tickets via the Composio Toolset.
- **Real-time Status Updates**
  Maintains a single source of truth by updating incident status across connected project management tools.
- **Resolution Workflow Automation**
  Executes predefined remediation scripts or documentation lookups when specific incident patterns are detected.

---

## Use Cases
**Incident Triage & Routing**
- Automatically route high-priority Sentry errors to the on-call engineer's Slack channel.
- Escalate unresolved incidents to management if no acknowledgment is received within a defined time window.

**Operational Documentation**
- Generate initial incident summaries including affected services and error frequency metrics.
- Link related Jira tickets to the active incident to prevent duplicate work during troubleshooting.

**Post-Incident Analysis**
- Archive incident resolution logs for automated post-mortem report generation.
- Sync incident closure data back to Sentry to mark issues as resolved in the monitoring dashboard.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your Sentry and communication tool accounts via the Composio integration menu.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw alert data or manual incident triggers.
- **Agent**: Analyzes the incident context and determines the appropriate response action.
- **Composio Toolset**: Executes API calls to Sentry, Jira, or Slack to perform actions.
- **Chat Output**: Delivers the final incident summary and confirmation of actions taken.

### 3) Run the Flow
Use the Playground to test your incident response logic:
- `Analyze the latest high-priority Sentry alerts and notify the on-call engineer on Slack.`
- `Create a Jira ticket for the most recent critical error and link it to the Sentry issue.`
- `Summarize the current status of all open incidents and post the report to the #devops channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the incident commander, interpreting technical logs and executing response protocols.
- **Instruction Pattern:**
    - "You are an expert SRE assistant; prioritize alerts based on system impact."
    - "Always verify the service name and environment before triggering notifications."
    - "Maintain a professional, concise tone when updating stakeholders on incident status."

### 2) Composio Toolset Node
Requires a valid API key for your Sentry account and the target communication platform (e.g., Slack or Jira). Ensure the connection scope includes read/write access to incident and issue management endpoints.

### 3) Tool Availability
- **Sentry API**: Fetching error details, stack traces, and issue status updates.
- **Slack/Teams API**: Sending automated notifications and incident updates to channels.
- **Jira/Linear API**: Creating, updating, and tracking incident tickets.
- **PagerDuty API**: Managing on-call rotations and alert escalations.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automates the cleanup and organization of post-incident action items.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Uses AI to rank and assign incident-related tasks based on urgency.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks the overall health and execution status of automated operational workflows.
