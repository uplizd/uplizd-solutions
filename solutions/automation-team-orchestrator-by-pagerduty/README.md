# Automation Team Orchestrator (Uplizd) - Intelligent cross-team workflow routing and incident management

## Summary
The Automation Team Orchestrator (Uplizd) streamlines incident response and operational tasks by intelligently routing automation actions to the appropriate teams based on real-time expertise, availability, and PagerDuty incident data. This workflow eliminates manual triage bottlenecks, ensuring that critical alerts reach the right engineers instantly, thereby improving mean time to resolution (MTTR) and reducing operational overhead for DevOps and SRE teams.

---

## Demo
![Automation Team Orchestrator workflow diagram showing PagerDuty incident ingestion, AI-driven routing, and team notification](image.png)
**Alt text (SEO-ready):** Automation Team Orchestrator workflow diagram showing PagerDuty incident ingestion, AI-driven routing, and team notification via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7a8ee74c-8fb6-59a2-82e5-a9b54812be84)

---

## Category
- **Primary category:** Operations Automation
- **Secondary tags:** pagerduty, incident management, team orchestration, workflow automation, devops, sre, composio, ai routing
- This solution bridges the gap between incident detection and team resolution by leveraging AI to map complex operational demands to the correct human responders.

---

## Who is this for?
This solution is designed for technical organizations looking to optimize their incident response lifecycle and reduce manual triage fatigue.

- **DevOps Engineer**
    - Automates the initial assignment of infrastructure alerts to reduce manual ticket routing.
- **SRE (Site Reliability Engineer)**
    - Ensures high-priority incidents are routed to on-call experts based on real-time service ownership.
- **Engineering Manager**
    - Gains visibility into team workload distribution and incident response efficiency.
- **IT Support Lead**
    - Standardizes the triage process across distributed teams to ensure no alert goes unaddressed.

---

## Features
- **Intelligent Routing Engine**
    - Uses AI to analyze incident metadata and match it against team skill sets and current on-call schedules.
- **PagerDuty Integration**
    - Seamlessly connects with PagerDuty via the Composio Toolset to fetch, update, and reassign incidents in real-time.
- **Dynamic Availability Awareness**
    - Filters routing decisions based on team member status to prevent assigning tasks to unavailable personnel.
- **Automated Context Enrichment**
    - Automatically attaches relevant logs or documentation to the incident before notifying the assigned team.
- **Feedback Loop Integration**
    - Captures resolution data to refine future routing logic, continuously improving the accuracy of the orchestrator.

---

## Use Cases
**Incident Triage & Assignment**
- Automatically reassigning high-severity database alerts to the specific SRE team responsible for storage infrastructure.
- Escalating stalled incidents to secondary on-call responders if no acknowledgment is received within a defined time window.

**Operational Workflow Automation**
- Triggering automated diagnostic scripts upon incident creation and attaching the output to the PagerDuty ticket.
- Syncing incident status updates across Slack and Jira to keep cross-functional stakeholders informed without manual updates.

**Team Workload Balancing**
- Distributing non-critical maintenance tasks across the team to prevent burnout and ensure equitable ticket distribution.
- Identifying recurring incident patterns to suggest team-wide training or process adjustments based on historical routing data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the `automation-team-orchestrator-by-pagerduty` template from the library.
3. Connect your PagerDuty account via the Composio Toolset integration settings.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the incident trigger or manual triage request.
- **Agent**: Processes the incident context and determines the optimal routing logic.
- **Composio Toolset**: Executes PagerDuty API calls to update incident assignments.
- **Chat Output**: Confirms the successful routing and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test your orchestration logic with these prompts:
- `Route the latest high-severity incident from the 'Database' service to the primary on-call SRE.`
- `Check the current on-call schedule for the 'Platform' team and reassign incident #12345 to the available lead.`
- `Summarize the last 5 incidents handled by the 'Backend' team and suggest a routing optimization.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central brain for decision-making.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate routing.
- Provide clear instructions on team hierarchies and escalation policies.
- Ensure the system prompt includes constraints regarding PagerDuty API permissions.

### 2) Composio Toolset Node
- Authenticate using your PagerDuty API Key with `read` and `write` scopes.
- Ensure the connection is active in the Composio dashboard before running the flow.

### 3) Tool Availability
- `pagerduty_get_incidents`: Fetch active incidents and their current status.
- `pagerduty_update_incident`: Reassign incidents or update priority levels.
- `pagerduty_get_oncall_schedule`: Identify the current on-call responder for specific services.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automates the resolution and cleanup of stale action items.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Uses AI to rank and prioritize incoming operational action items.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the performance and health of automated team workflows.
