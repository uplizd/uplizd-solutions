# Smart Escalation Manager (Uplizd) - Automated ticket prioritization and stakeholder notification

## Summary
The Smart Escalation Manager is an intelligent Uplizd workflow that monitors incoming support tickets in Freshdesk, identifies high-priority issues based on sentiment and urgency, and automatically routes them to the appropriate stakeholders. By streamlining the escalation process, this solution reduces response times, ensures critical customer issues are never missed, and maintains high service level agreement (SLA) compliance.

---

## Demo
![Smart Escalation Manager workflow diagram showing Freshdesk ticket intake, AI analysis, and stakeholder notification](image.png)
**Alt text (SEO-ready):** Smart Escalation Manager workflow for Freshdesk, featuring Uplizd AI automation, ticket prioritization, and real-time stakeholder notification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7ee0ea31-de77-54e8-9db4-5cb025d69acc)

---

## Category
**Primary category:** Customer Support Automation
**Secondary tags:** freshdesk, ticketing, escalation, ai workflow, customer experience, incident management, composio, support operations.
This solution bridges the gap between raw support volume and actionable incident response through automated intelligence.

---

## Who is this for?
This solution is designed for support teams looking to eliminate manual triage bottlenecks and improve resolution speed.

* **Support Manager**
    * Ensures high-priority customer issues are escalated to senior staff immediately.
* **Customer Success Lead**
    * Maintains account health by proactively addressing negative sentiment in support tickets.
* **Technical Support Engineer**
    * Receives pre-qualified, urgent technical tickets directly in their workflow.
* **Operations Analyst**
    * Tracks escalation patterns to optimize team resource allocation and training.

---

## Features
- **Intelligent Sentiment Analysis**
    * Uses AI to detect frustration or urgency in ticket text, triggering immediate escalation for sensitive cases.
- **Automated Freshdesk Integration**
    * Seamlessly connects with Freshdesk via the Composio Toolset to fetch, update, and categorize tickets in real-time.
- **Dynamic Stakeholder Routing**
    * Routes tickets to specific Slack channels or email aliases based on the severity and product category identified.
- **SLA-Aware Prioritization**
    * Automatically flags tickets approaching SLA breaches, ensuring the team focuses on the most time-sensitive tasks.
- **Contextual Summarization**
    * Generates concise summaries of long ticket threads for stakeholders, saving time during the handoff process.

---

## Use Cases
**Critical Incident Management**
* Escalating security-related or system-outage tickets to the engineering team within minutes.
* Notifying account managers when a high-value client submits a "blocking" issue.

**Customer Experience Optimization**
* Identifying tickets with negative sentiment to prevent churn before it happens.
* Prioritizing tickets from VIP customers to ensure a premium support experience.

**Operational Efficiency**
* Automatically tagging tickets based on content to reduce manual sorting by support agents.
* Syncing ticket status updates across platforms to keep all stakeholders informed without manual data entry.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Freshdesk account within the Composio Toolset configuration.
3. Configure your notification channels (e.g., Slack or Email) to receive escalation alerts.
4. Ensure nodes are correctly mapped and all API credentials are saved before activating the flow.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger event from Freshdesk (e.g., New Ticket Created).
* **Agent**: Processes ticket content, evaluates urgency, and decides on the escalation path.
* **Composio Toolset**: Executes actions like updating ticket priority or posting to notification channels.
* **Chat Output**: Confirms the escalation action and logs the ticket status update.

### 3) Run the Flow
Use the Playground to test your escalation logic with these prompts:
* `Analyze the latest ticket in Freshdesk and escalate if the sentiment is negative.`
* `Check for tickets with 'Urgent' status and notify the engineering Slack channel.`
* `Summarize the last 5 tickets from high-value accounts and flag any that require immediate attention.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a triage expert that interprets ticket intent and urgency.
* Use a model with strong reasoning capabilities (e.g., GPT-4o).
* Instruction: "Analyze the ticket content for urgency, sentiment, and technical complexity."
* Instruction: "If the ticket meets escalation criteria, format a summary and trigger the notification tool."

### 2) Composio Toolset Node
* Provide your Freshdesk API key and ensure the connection scope includes `tickets:read` and `tickets:write`.
* Authenticate your notification provider (e.g., Slack) to allow the agent to send alerts.

### 3) Tool Availability
* `freshdesk_get_ticket`: Fetch full ticket details and history.
* `freshdesk_update_ticket`: Modify priority or status labels.
* `slack_send_message`: Send alerts to designated support channels.
* `email_send`: Dispatch notifications to account managers.

---

## Related Solutions
* [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Deploy an AI-powered chatbot to handle initial customer inquiries.
* [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Automate support ticket triage specifically for WhatsApp channels.
* [action-item-prioritizer-by-rootly](../action-item-prioritizer-by-rootly/README.md) - Prioritize and manage action items derived from support incidents.
