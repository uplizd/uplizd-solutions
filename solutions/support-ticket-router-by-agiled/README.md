# Support Ticket Router (Uplizd) - Intelligent AI-driven customer inquiry classification and routing

## Summary
The Support Ticket Router (Uplizd) automates the triage process by analyzing incoming customer inquiries, categorizing them by intent, and routing them to the appropriate support queue or agent. By leveraging AI-driven classification, this workflow eliminates manual sorting, reduces response latency, and ensures that critical issues are prioritized, providing a single source of truth for support operations.

---

## Demo
![Support Ticket Router workflow diagram showing Chat Input, Agent classification, Composio Toolset integration, and ticket routing output](image.png)
**Alt text (SEO-ready):** Support Ticket Router workflow diagram showing Chat Input, Agent classification, Composio Toolset integration, and ticket routing output for Uplizd AI automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7f4dbbd4-3900-58d0-b607-d8d16b0a3007)

---

## Category
**Primary category:** Customer Support
**Secondary tags:** support automation, ticket routing, helpdesk, ai workflow, composio, customer experience, triage, ticketing system

This solution streamlines support operations by integrating AI-powered classification directly into your existing helpdesk infrastructure.

---

## Who is this for?
This solution is designed for support teams looking to scale their operations without increasing manual overhead.

*   **Support Manager**
    *   Optimizes team bandwidth by ensuring tickets reach the right specialists immediately.
*   **Customer Success Lead**
    *   Reduces churn by accelerating response times for high-priority account issues.
*   **IT Operations Specialist**
    *   Maintains clean ticketing data by enforcing consistent categorization across all incoming requests.
*   **Helpdesk Administrator**
    *   Automates the repetitive task of manual ticket tagging and queue assignment.

---

## Features
- **Intelligent Intent Classification**
    Uses advanced LLMs to analyze the sentiment and subject matter of incoming messages to determine the correct support category.
- **Automated Queue Routing**
    Automatically assigns tickets to specific departments or agents based on the classification result, reducing manual triage time.
- **Composio Toolset Integration**
    Seamlessly connects with popular helpdesk platforms to create, update, and track tickets in real-time.
- **Priority Scoring**
    Identifies urgent keywords or customer tiers to escalate high-priority tickets to the front of the queue.
- **Customizable Routing Logic**
    Allows for flexible rule-based configuration to adapt to changing business needs and support team structures.

---

## Use Cases
**High-Volume Support Triage**
*   Automatically routing technical bugs to the engineering support queue.
*   Flagging billing inquiries for immediate review by the finance support team.

**Urgent Issue Escalation**
*   Detecting "outage" or "critical" keywords to trigger immediate notifications for on-call engineers.
*   Prioritizing tickets from enterprise-tier customers to ensure SLA compliance.

**Data Hygiene and Organization**
*   Standardizing ticket tags across multiple support channels for better reporting.
*   Filtering out spam or non-support inquiries to keep the active ticket queue clean.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Support Ticket Router template from the solution library.
3. Connect your preferred helpdesk API credentials within the Composio configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw customer inquiry text.
*   **Agent**: Analyzes the intent and determines the appropriate routing path.
*   **Composio Toolset**: Executes the API call to create or update the ticket in your helpdesk.
*   **Chat Output**: Confirms the ticket creation and provides the ticket ID to the user.

### 3) Run the Flow
Use the Playground to test the routing logic with these prompts:
* `Create a ticket for a user reporting a login failure on the mobile app.`
* `Route this inquiry about a billing discrepancy to the finance department.`
* `Flag this message as urgent: The system is completely down for our team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the operation, responsible for parsing intent and mapping it to your internal categories.
*   Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate classification.
*   Provide a clear list of your support categories in the system prompt.
*   Instruct the agent to extract specific entities like "Priority" and "Department" from the input.

### 2) Composio Toolset Node
*   **API Key**: Ensure your helpdesk platform API key is securely stored in the Composio environment.
*   **Connection Scope**: Grant the toolset permission to "Create" and "Update" tickets within your helpdesk workspace.

### 3) Tool Availability
*   `helpdesk_create_ticket`: Creates a new ticket record.
*   `helpdesk_update_status`: Modifies ticket metadata or status.
*   `helpdesk_add_tag`: Applies relevant labels for reporting.
*   `helpdesk_assign_agent`: Moves the ticket to a specific team queue.

---

## Related Solutions
* [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - A general-purpose AI assistant for 24/7 customer queries.
* [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Specialized triage for support requests arriving via WhatsApp.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Focuses on identifying and prioritizing critical tasks from support logs.
