# Compliance Action Monitor (Uplizd) - Automated incident response and audit readiness

## Summary
The Compliance Action Monitor is an intelligent Uplizd workflow designed to automate the tracking, validation, and remediation of incident action items. By integrating with Rootly, this solution ensures that every task generated during an incident lifecycle adheres to internal compliance standards and audit requirements, significantly reducing manual oversight and improving organizational pipeline velocity.

---

## Demo
![Compliance Action Monitor dashboard showing incident action item status and audit compliance logs](../image.png)
**Alt text (SEO-ready):** Compliance Action Monitor dashboard showing incident action item status, audit compliance logs, and Rootly integration for automated incident response.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/34fb1d76-8daf-50de-94d4-7763d6425815)

---

## Category
- **Primary category:** Legal & Compliance
- **Secondary tags:** rootly, incident management, audit, compliance, workflow automation, composio, risk mitigation
- This solution bridges the gap between technical incident response and regulatory compliance by automating the audit trail for every action item.

---

## Who is this for?
This workflow is built for teams that need to maintain rigorous documentation standards during high-pressure incident resolution.

- **Compliance Officer**
    - Ensures all incident-related tasks are documented and compliant with internal policies without manual review.
- **Incident Commander**
    - Reduces the cognitive load of tracking action item status during active incidents by delegating monitoring to the agent.
- **DevOps Engineer**
    - Automates the verification of post-incident action items to ensure infrastructure changes meet security benchmarks.
- **Legal Counsel**
    - Maintains a clean, verifiable audit log of incident remediation steps for regulatory reporting and risk assessment.

---

## Features
- **Automated Compliance Auditing**
    - Automatically scans incident action items for required metadata and adherence to security protocols.
- **Rootly Integration**
    - Deep connectivity with Rootly to pull real-time incident data and push status updates directly into the incident timeline.
- **Real-time Remediation Alerts**
    - Proactively notifies stakeholders when an action item is nearing a deadline or fails a compliance check.
- **Standardized Reporting**
    - Generates structured summaries of incident resolutions, ready for internal audit or external regulatory review.
- **Intelligent Contextual Analysis**
    - Uses AI to understand the urgency and impact of action items, prioritizing them based on compliance risk levels.

---

## Use Cases
**Incident Lifecycle Management**
- Automatically verifying that all post-mortem action items have assigned owners and due dates.
- Syncing incident status updates between Rootly and internal compliance tracking dashboards.

**Regulatory Audit Preparation**
- Compiling comprehensive incident reports that map specific actions to regulatory control requirements.
- Flagging incomplete or non-compliant action items for immediate review before an audit window closes.

**Risk Mitigation & Governance**
- Enforcing mandatory documentation fields for high-severity incidents to prevent data decay.
- Identifying stalled incident tasks that pose a risk to system stability or compliance posture.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Compliance Action Monitor.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your Rootly API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives incident IDs or manual audit triggers from the user.
- **Agent**: Analyzes the incident context and evaluates action items against compliance rules.
- **Composio Toolset**: Executes API calls to Rootly to fetch, update, or verify incident action items.
- **Chat Output**: Delivers the final compliance status report and remediation recommendations.

### 3) Run the Flow
Use the Playground to test your monitor with the following prompts:
- `Check the compliance status of all open action items for incident #12345.`
- `List all overdue action items in the current Rootly incident and suggest remediation steps.`
- `Generate an audit summary for the last three incidents managed by the SRE team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the compliance engine, interpreting incident data and policy requirements.
- **Instruction Pattern:**
    - "Act as a compliance auditor; evaluate incident tasks against the provided security checklist."
    - "Prioritize action items based on regulatory impact and due date proximity."
    - "Maintain a professional, objective tone in all generated audit summaries."

### 2) Composio Toolset Node
- **API Key:** Provide your Rootly API key to enable read/write access to your incident management data.
- **Connection Scope:** Ensure the agent has 'Read' access to incident timelines and 'Write' access to update action item statuses.

### 3) Tool Availability
- `rootly_get_incident_action_items`: Retrieves the list of tasks for a specific incident.
- `rootly_update_action_item`: Allows the agent to flag or update task status based on compliance findings.
- `rootly_list_incidents`: Fetches recent incident history for broader audit reporting.

---

## Related Solutions
- [Action Item Prioritizer (Rootly)](../action-item-prioritizer-by-rootly/README.md) — Focuses on task urgency and resource allocation for incident teams.
- [Action Item Cleanup Agent (Rootly)](../action-item-cleanup-agent-by-rootly/README.md) — Automates the removal of stale or duplicate tasks in your incident management system.
- [Account Health Compliance Monitor (Brevo)](../account-health-compliance-monitor-by-brevo/README.md) — Monitors account-level compliance and usage metrics for external stakeholders.
