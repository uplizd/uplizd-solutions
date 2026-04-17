# Error Triage Specialist (Uplizd) - Automated bug prioritization and resolution workflow

## Summary
The Error Triage Specialist is an intelligent Uplizd workflow that automates the ingestion, analysis, and prioritization of software bugs reported via Bugsnag. By leveraging AI to categorize incoming errors based on severity and impact, this solution reduces manual overhead for engineering teams, ensures critical issues are addressed immediately, and maintains high pipeline velocity for product development.

---

## Demo
![Error Triage Specialist workflow interface showing Bugsnag integration and AI-driven prioritization nodes](image.png)
**Alt text (SEO-ready):** Error Triage Specialist (Uplizd) workflow for automated Bugsnag error prioritization, incident categorization, and engineering team notification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8e393291-fa80-5374-83a9-7729bddb23be)

---

## Category
**Primary category:** Support operations
**Secondary tags:** bugsnag, error tracking, incident management, engineering, automation, ai workflow, composio, devops
This solution streamlines technical support by bridging the gap between raw error logs and actionable engineering tasks.

---

## Who is this for?
This workflow is designed for technical teams looking to minimize downtime and optimize their incident response lifecycle.

* **Engineering Manager**
    * Gains real-time visibility into system stability and team workload distribution.
* **Site Reliability Engineer (SRE)**
    * Automates the initial triage of alerts to focus on high-impact infrastructure issues.
* **QA Lead**
    * Ensures that recurring bugs are correctly categorized and linked to existing tickets.
* **Developer**
    * Receives pre-triaged, context-rich error reports, reducing time spent on investigation.

---

## Features
- **Automated Error Ingestion**
  Real-time synchronization with Bugsnag to capture new exceptions as they occur.
- **AI-Driven Severity Scoring**
  Uses LLM analysis to classify errors based on frequency, user impact, and system criticality.
- **Intelligent Routing**
  Automatically assigns high-priority bugs to the appropriate engineering squad or Slack channel.
- **Contextual Enrichment**
  Appends relevant metadata, stack traces, and environment details to every triage report.
- **Composio Toolset Integration**
  Seamlessly connects with project management tools to create or update tickets based on triage outcomes.

---

## Use Cases
**Incident Response**
* Automatically escalating critical production errors to the on-call engineer via PagerDuty or Slack.
* Creating incident tickets in Jira immediately upon detection of a high-frequency exception.

**Bug Lifecycle Management**
* Deduplicating incoming error reports by linking them to existing, unresolved issues in the tracker.
* Archiving low-priority or "noise" exceptions to keep the engineering backlog clean and actionable.

**Performance Monitoring**
* Generating daily summaries of error trends to identify regressions introduced in recent deployments.
* Mapping error spikes to specific releases or feature flags to speed up root-cause analysis.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Error Triage Specialist.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your Bugsnag and project management tool credentials within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives raw error notifications from Bugsnag webhooks.
* **Agent:** Analyzes the error stack trace and determines the urgency and assignment.
* **Composio Toolset:** Executes actions to create tickets or notify teams in external platforms.
* **Chat Output:** Confirms the triage action taken and logs the result to the dashboard.

### 3) Run the Flow
Use the Playground to test your triage logic with these prompts:
* `Analyze the latest critical error from Bugsnag and create a Jira ticket if it affects more than 50 users.`
* `Summarize the top 3 recurring errors from the last 24 hours and post them to the #engineering-standup channel.`
* `Check if the current error is a duplicate of an existing open issue and update the ticket status if necessary.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the technical brain, interpreting error logs and making routing decisions.
* **Role:** Act as a Senior DevOps Engineer with expertise in bug triage and incident response.
* **Instruction Pattern:** 
    * Prioritize errors based on user impact and frequency.
    * Maintain a neutral, professional tone in all automated notifications.
    * Always include a link to the original Bugsnag error report in the output.

### 2) Composio Toolset Node
Requires a valid API key for your project management and communication platforms. Ensure the connection scope includes read/write permissions for ticket creation and channel messaging.

### 3) Tool Availability
* **Bugsnag API:** For fetching detailed error logs and stack traces.
* **Jira/Linear API:** For creating and updating issue tickets.
* **Slack/Teams API:** For sending real-time alerts to engineering channels.

---

## Related Solutions
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automate the sorting and assignment of technical action items.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the status and performance of automated operational workflows.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Monitor system usage and account health metrics for proactive support.
