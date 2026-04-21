# Ticket Cleanup Automation (Uplizd) - Streamline support queues and resolve stale tickets

## Summary
The Ticket Cleanup Automation workflow by Uplizd provides an intelligent mechanism to identify, categorize, and resolve stale or low-priority support tickets within Zendesk. By leveraging AI-driven analysis, support teams can maintain a clean, actionable queue, significantly reducing noise and improving response times for high-priority customer inquiries.

---

## Demo
![Workflow diagram showing Zendesk ticket ingestion, AI analysis, and automated cleanup actions](image.png)
**Alt text (SEO-ready):** Uplizd ticket cleanup automation workflow for Zendesk, featuring AI-powered ticket triage, stale queue management, and automated support operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a023547c-edfb-521d-a020-d9af3b716bc8)

---

## Category
- **Primary category:** Support operations
- **Secondary tags:** zendesk, ticket management, automation, ai workflow, support hygiene, composio, queue optimization
- This solution integrates directly with your support platform to automate the maintenance of ticket hygiene and operational efficiency.

---

## Who is this for?
This solution is designed for support teams looking to reclaim time spent on manual ticket maintenance.

- **Support Manager**
    - Ensures team focus remains on active, high-value customer issues by automating the closure of stale requests.
- **Customer Success Lead**
    - Maintains a pristine support environment that reflects accurate response time metrics and customer satisfaction data.
- **Operations Analyst**
    - Reduces queue bloat and improves reporting accuracy by programmatically managing ticket lifecycle states.
- **Support Agent**
    - Minimizes time spent manually filtering through abandoned or duplicate tickets, allowing for faster resolution of active cases.

---

## Features
- **Automated Stale Detection**
    - Identifies tickets that have remained inactive beyond a defined threshold using real-time Zendesk data.
- **Intelligent Triage**
    - Uses AI to determine if a ticket requires human intervention or if it qualifies for automated closure or archival.
- **Composio-Powered Integration**
    - Seamlessly executes actions within Zendesk, such as updating statuses, adding internal notes, or tagging tickets, via the Composio Toolset.
- **Customizable Cleanup Rules**
    - Allows users to define specific criteria for ticket cleanup, ensuring compliance with internal support policies.
- **Audit Logging**
    - Provides a clear record of all automated actions taken, ensuring transparency and accountability in support operations.

---

## Use Cases
**Queue Hygiene Management**
- Automatically close tickets that have been in a "Pending" state for more than 14 days without customer response.
- Flag duplicate tickets for agent review to prevent redundant work across the support team.

**Operational Efficiency**
- Route stale tickets to a specific "Archived" view to keep the active dashboard focused on urgent customer needs.
- Automatically add internal notes to tickets before closure, documenting the automated cleanup action for future reference.

**Compliance and Reporting**
- Ensure that support metrics are not skewed by abandoned tickets by maintaining a clean, active-only queue.
- Apply specific tags to tickets processed by the automation to track the impact of cleanup efforts on overall ticket volume.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Ticket Cleanup Automation template from the solution library.
3. Connect your Zendesk account within the Composio Toolset configuration.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal to initiate the ticket scan.
- **Agent**: Analyzes ticket metadata and determines the appropriate cleanup action based on your configured rules.
- **Composio Toolset**: Executes the Zendesk API calls to update, tag, or close tickets.
- **Chat Output**: Returns a summary report of the cleanup actions performed during the execution.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Scan for all tickets in 'Pending' status older than 10 days and close them.`
- `Identify duplicate tickets from the last 30 days and tag them for review.`
- `Provide a report of all tickets cleaned up by the automation today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for ticket lifecycle management.
- Use a model capable of logical reasoning to interpret ticket timestamps and status fields.
- Instruct the agent to prioritize accuracy to avoid closing tickets that require human attention.
- Configure the agent to output structured summaries of actions taken for the final Chat Output.

### 2) Composio Toolset Node
- Provide your Zendesk API credentials within the Composio dashboard.
- Ensure the connection scope includes read/write permissions for tickets, tags, and internal notes.

### 3) Tool Availability
- `zendesk_update_ticket`: Used to change status or add internal notes.
- `zendesk_search_tickets`: Used to query the ticket queue based on age and status.
- `zendesk_add_tag`: Used to categorize tickets for reporting or agent review.

---

## Related Solutions
- [247 Customer Support Assistant by AI ML API](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-driven support assistance for 24/7 coverage.
- [WhatsApp Support Triage Agent by Wati](../whats-app-support-triage-agent-by-wati/README.md) - Automated triage for support tickets via WhatsApp.
- [Action Item Cleanup Agent by Rootly](../action-item-cleanup-agent-by-rootly/README.md) - Manage and resolve pending action items in support workflows.
