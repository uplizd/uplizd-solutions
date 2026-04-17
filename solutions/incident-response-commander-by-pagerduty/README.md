# Incident Response Commander (Uplizd) - Automate critical incident escalation and resolution

## Summary
The Incident Response Commander is an intelligent Uplizd workflow designed to streamline mission-critical operations by automating incident triage, cross-team communication, and resolution tracking. By integrating PagerDuty with your existing communication stack, this solution reduces mean time to resolution (MTTR) and ensures that high-priority alerts are routed to the right responders instantly, providing a single source of truth for engineering and DevOps teams.

---

## Demo
![Incident Response Commander dashboard showing automated PagerDuty incident triage and escalation workflow](image.png)
**Alt text (SEO-ready):** Incident Response Commander Uplizd workflow, PagerDuty incident automation, automated escalation, DevOps incident management, and real-time incident triage.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4bca2149-bce5-5048-a9d8-48c2f9de1c4d)

---

## Category
**Primary category:** Operations
**Secondary tags:** incident response, pagerduty, devops, automation, escalation, mttr, site reliability, composio, ai workflow.
This solution bridges the gap between technical monitoring alerts and human-led incident resolution through automated orchestration.

---

## Who is this for?
This workflow is built for technical teams managing high-availability systems who need to minimize downtime and manual coordination overhead.

- **Site Reliability Engineer (SRE)**
    - Automates the initial triage of incoming alerts to reduce manual investigation time.
- **DevOps Manager**
    - Ensures consistent escalation policies are followed across distributed engineering teams.
- **Incident Commander**
    - Maintains a centralized record of incident status and communication logs during active outages.
- **Support Lead**
    - Provides real-time updates to stakeholders by syncing incident status with internal communication channels.

---

## Features
- **Automated Alert Triage**
    - Instantly categorizes incoming PagerDuty incidents based on severity and service impact.
- **Dynamic Escalation Routing**
    - Automatically triggers secondary on-call rotations when primary responders are unavailable.
- **Contextual Incident Summarization**
    - Generates concise summaries of incident logs to speed up the hand-off between responders.
- **Real-time Status Synchronization**
    - Keeps incident status updated across Slack, Jira, and PagerDuty via the Composio Toolset.
- **Resolution Documentation**
    - Automatically captures resolution steps and links them to the original incident ticket for post-mortem analysis.

---

## Use Cases
**Active Incident Management**
- Automatically create incident channels in Slack when a PagerDuty alert exceeds a severity threshold.
- Notify on-call engineers via multiple channels if an incident remains unacknowledged for more than 10 minutes.

**Post-Incident Reporting**
- Aggregate all communication logs and system metrics into a single summary document upon incident closure.
- Automatically update Jira tickets with resolution notes and root cause analysis tags provided by the responder.

**Team Coordination**
- Sync on-call schedules with internal team calendars to ensure accurate routing of alerts.
- Provide non-technical stakeholders with automated status updates during ongoing service disruptions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your PagerDuty account and any desired communication tools (e.g., Slack, Jira) via the Composio dashboard.
3. Configure the trigger settings to listen for your specific PagerDuty service webhooks.
4. Ensure nodes are correctly mapped to your environment variables and API keys before activating.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw alert data or manual incident trigger command.
- **Agent**: Analyzes the incident context and decides on the appropriate escalation or notification path.
- **Composio Toolset**: Executes the PagerDuty API calls to update incident status or trigger escalations.
- **Chat Output**: Delivers the final incident summary and resolution confirmation to the designated team channel.

### 3) Run the Flow
Use the Uplizd Playground to test your workflow with the following prompts:
- `Check the current status of all high-priority PagerDuty incidents.`
- `Escalate the active incident #1234 to the secondary on-call engineer.`
- `Summarize the last 3 resolved incidents and post them to the #devops-reports channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, prioritizing speed and accuracy.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) to handle complex incident logic.
- Instruction: "You are an Incident Response Commander. Analyze incoming alerts, determine severity, and execute escalation protocols strictly according to the provided PagerDuty service rules."
- Instruction: "Always maintain a professional, concise tone when communicating status updates to stakeholders."

### 2) Composio Toolset Node
- Provide your PagerDuty API Key and ensure the connection scope includes `incidents.read` and `incidents.write`.
- Configure the toolset to allow the agent to query on-call schedules and update incident metadata.

### 3) Tool Availability
- **PagerDuty API**: For incident retrieval, acknowledgment, and escalation.
- **Communication APIs**: For posting updates to Slack or Microsoft Teams.
- **Ticketing APIs**: For updating Jira or Linear with incident resolution details.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Manage and prioritize incoming technical tasks and alerts.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automate the archival and organization of resolved incident tasks.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the performance and reliability of your automated operational workflows.
