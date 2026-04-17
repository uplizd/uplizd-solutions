# Incident Auto-Responder by ServiceNow (Uplizd) - Automated IT incident triage and resolution

## Summary
The Incident Auto-Responder by ServiceNow (Uplizd) streamlines IT operations by automatically analyzing incoming incident tickets, determining severity, and triggering appropriate response or escalation workflows. By leveraging the Composio Toolset to interface directly with ServiceNow, this solution reduces mean time to resolution (MTTR), eliminates manual triage bottlenecks, and ensures high-priority issues are addressed with immediate, data-driven precision.

---

## Demo
![Incident Auto-Responder workflow showing Chat Input, Agent, ServiceNow Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Incident Auto-Responder workflow by Uplizd for ServiceNow, showing automated ticket triage, severity analysis, and IT incident escalation via Composio integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5bf375c4-9671-5409-884b-9e3ad10f29fc)

---

## Category
**Primary category:** Operations
**Secondary tags:** servicenow, it-service-management, itsm, incident-response, automation, ticketing, ai-workflow, composio

This solution optimizes IT service management by automating the classification and initial response phases of the incident lifecycle.

---

## Who is this for?
This solution is designed for IT teams and support organizations looking to scale their incident response capabilities without increasing manual overhead.

- **IT Support Manager**
    - Gains real-time visibility into incident volume and ensures SLA compliance through automated escalation.
- **System Administrator**
    - Reduces repetitive manual ticket tagging and routing tasks, allowing focus on complex infrastructure issues.
- **DevOps Engineer**
    - Accelerates incident resolution by automatically triggering diagnostic scripts or notifying on-call personnel based on ticket severity.
- **Service Desk Analyst**
    - Experiences lower cognitive load as the agent handles initial triage and provides recommended resolution steps for common incidents.

---

## Features
- **Automated Severity Scoring**
    - Analyzes ticket descriptions and metadata to assign accurate priority levels, ensuring critical issues are escalated immediately.
- **ServiceNow Integration**
    - Utilizes the Composio Toolset to perform real-time read/write operations on ServiceNow incidents, comments, and status fields.
- **Intelligent Routing**
    - Dynamically assigns tickets to the correct support queue or team based on the incident category and detected urgency.
- **Contextual Response Generation**
    - Drafts professional, templated responses or status updates for end-users, maintaining consistent communication standards.
- **Escalation Triggering**
    - Automatically notifies on-call engineers via integrated channels when high-severity incidents are detected.

---

## Use Cases
**Incident Triage & Classification**
- Automatically categorize incoming tickets based on keywords and user-provided descriptions.
- Update ticket priority fields in ServiceNow based on pre-defined business impact rules.

**Automated Communication**
- Send immediate acknowledgment emails to end-users with estimated resolution times.
- Provide status updates to stakeholders when an incident moves through different stages of the lifecycle.

**Operational Escalation**
- Escalate high-priority tickets to senior engineering teams if a resolution is not found within a specific timeframe.
- Trigger alerts in external messaging platforms when critical system-wide incidents are logged.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the builder.
2. Connect your ServiceNow account via the Composio integration settings.
3. Configure the trigger settings to monitor your desired incident intake queue.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw incident data or user-reported issues.
- **Agent**: Processes the incident text, evaluates severity, and determines the next action.
- **Composio Toolset**: Executes ServiceNow API calls to update records, add comments, or escalate tickets.
- **Chat Output**: Returns the final status of the incident processing to the dashboard or user.

### 3) Run the Flow
Test the workflow in the Playground using these example prompts:
- `Analyze the latest incident in the queue and set the priority to High if it mentions 'server outage'.`
- `Draft a response to the user for incident INC-12345 explaining that we are investigating the issue.`
- `Escalate incident INC-98765 to the Network Engineering team and add a comment about the urgency.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an IT operations specialist.
- Use a model capable of logical reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction pattern: "You are an IT Incident Manager. Analyze the incident description, determine the priority, and use the ServiceNow tool to update the record."
- Ensure the agent is instructed to maintain a professional and empathetic tone in all user-facing communications.

### 2) Composio Toolset Node
- Provide your ServiceNow API credentials within the Composio dashboard.
- Ensure the connection scope includes `incident:read`, `incident:write`, and `incident:update` permissions.

### 3) Tool Availability
- `servicenow_get_incident`: Fetch details for a specific ticket.
- `servicenow_update_incident`: Modify fields like priority, state, or assignment group.
- `servicenow_add_comment`: Append internal notes or user-facing updates to the ticket.
- `servicenow_escalate_incident`: Trigger escalation workflows for high-priority items.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - General purpose AI assistant for handling customer support inquiries.
- [action-item-cleanup-agent-by-rootly](../action-item-cleanup-agent-by-rootly/README.md) - Automated cleanup and organization of incident action items.
- [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Prioritization engine for incident-related tasks and follow-ups.
