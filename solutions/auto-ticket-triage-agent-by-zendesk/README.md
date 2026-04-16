# Auto Ticket Triage Agent (Uplizd) - Intelligent support ticket categorization and priority routing

## Summary
The Auto Ticket Triage Agent leverages Uplizd AI workflows to automatically analyze, categorize, and prioritize incoming support tickets from Zendesk. By integrating with the Composio Toolset, this solution ensures that high-priority issues are routed to the correct teams instantly, reducing response times and maintaining high customer satisfaction standards through automated ticket hygiene.

---

## Demo
![Auto Ticket Triage Agent workflow diagram showing Zendesk input, AI analysis, and automated ticket routing](image.png)
**Alt text (SEO-ready):** Auto Ticket Triage Agent workflow for Zendesk, featuring Uplizd AI-driven ticket categorization, priority routing, and automated support operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/5a0a1b59-d623-5909-ab78-ea74ae5605d9)

---

## Category
- **Primary category:** Support operations
- **Secondary tags:** zendesk, ticket triage, ai workflow, customer support, automation, composio, helpdesk, incident management
- This solution streamlines helpdesk efficiency by automating the initial classification and routing of support requests.

---

## Who is this for?
This solution is designed for support teams looking to eliminate manual ticket sorting and improve response velocity.

- **Support Manager**
    - Ensures consistent SLA adherence by automating the triage process for all incoming tickets.
- **Customer Success Lead**
    - Identifies urgent customer issues faster, allowing for proactive outreach and retention efforts.
- **IT Operations Specialist**
    - Reduces manual overhead by routing technical tickets directly to the appropriate engineering queues.
- **Support Agent**
    - Focuses on high-value problem solving rather than repetitive categorization and tag management.

---

## Features
- **Automated Categorization**
    - Uses AI to scan ticket content and assign relevant categories based on historical support data.
- **Priority Scoring**
    - Evaluates ticket urgency and sentiment to automatically set priority levels in Zendesk.
- **Smart Routing**
    - Directs tickets to specific agent groups based on the detected topic and required technical expertise.
- **Real-time Integration**
    - Connects directly to Zendesk via the Composio Toolset for seamless, real-time ticket updates.
- **Workflow Transparency**
    - Provides clear logs of every triage decision, ensuring auditability and easy performance tuning.

---

## Use Cases
**Urgent Incident Management**
- Automatically escalating tickets containing keywords like "outage" or "critical" to the engineering response team.
- Flagging high-sentiment negative feedback for immediate review by a senior support lead.

**Routine Support Efficiency**
- Routing billing-related inquiries directly to the finance support queue without human intervention.
- Auto-tagging tickets based on product features mentioned to help product teams track recurring issues.

**Support Hygiene & Organization**
- Closing duplicate tickets or spam entries identified by the agent during the initial triage phase.
- Standardizing ticket formatting and labels across the entire support organization for better reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Auto Ticket Triage Agent template from the solution library.
3. Connect your Zendesk account within the Composio Toolset configuration.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw ticket data and metadata from the Zendesk webhook.
- **Agent**: Analyzes ticket content and determines the optimal category and priority.
- **Composio Toolset**: Executes the update command to apply tags and priority levels in Zendesk.
- **Chat Output**: Confirms the triage action and logs the final ticket status.

### 3) Run the Flow
Use the Playground to test your triage logic with these example prompts:
- `Categorize the latest incoming ticket from Zendesk and set priority to High if it mentions a system outage.`
- `Analyze the sentiment of ticket #12345 and route it to the Billing team if it relates to subscription issues.`
- `Scan the unassigned queue and apply appropriate tags based on the product mentioned in the ticket body.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for ticket classification.
- Use a model with strong reasoning capabilities to interpret nuanced customer language.
- Instruction pattern: "Analyze the ticket body for intent," "Map intent to predefined support categories," and "Assign priority based on urgency indicators."

### 2) Composio Toolset Node
- Provide your Zendesk API credentials within the Composio dashboard.
- Ensure the connection scope includes read/write access for tickets, tags, and user fields.

### 3) Tool Availability
- **Ticket Reader**: Fetches ticket details and metadata.
- **Ticket Updater**: Modifies ticket priority, status, and tags.
- **Commenter**: Adds internal notes to tickets regarding the triage decision.

---

## Related Solutions
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-powered round-the-clock support assistance.
- [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Automated triage for WhatsApp-based support channels.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Prioritize and manage action items from support incidents.
