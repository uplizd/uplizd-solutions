# WhatsApp Support Triage Agent (Uplizd) - Automated customer request routing and categorization

## Summary
The WhatsApp Support Triage Agent is an intelligent workflow designed to streamline customer service operations by automatically analyzing, categorizing, and routing incoming WhatsApp messages. By leveraging the WATI integration, this solution ensures that support teams reduce response times, eliminate manual ticket sorting, and maintain high-quality service standards through real-time AI-driven classification.

---

## Demo
![WhatsApp Support Triage Agent workflow diagram showing message intake, AI classification, and WATI routing](image.png)

**Alt text (SEO-ready):** WhatsApp Support Triage Agent workflow diagram showing message intake, AI classification, and WATI routing using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5d188df5-d4f7-5d28-ad59-3eaf37f7cba0)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** whatsapp, wati, triage, automation, support tickets, ai workflow, composio, customer experience
- This solution bridges the gap between high-volume WhatsApp communication and organized support ticketing systems to improve operational efficiency.

---

## Who is this for?
This solution is designed for support teams and operations managers looking to automate their communication workflows.

- **Support Manager**
    - Reduces manual triage time by automating the categorization of incoming customer queries.
- **Customer Success Lead**
    - Ensures high-priority issues are routed to the correct team members immediately.
- **Operations Specialist**
    - Maintains clean support queues by filtering out spam and non-actionable messages.
- **WhatsApp Marketing Manager**
    - Improves customer satisfaction scores by ensuring faster, more accurate response times.

---

## Features
- **Intelligent Intent Classification**
    - Automatically detects the nature of a request (e.g., billing, technical, general inquiry) using advanced LLM analysis.
- **Seamless WATI Integration**
    - Utilizes the Composio Toolset to push categorized messages directly into the WATI platform for agent visibility.
- **Real-time Routing Logic**
    - Dynamically assigns tickets to specific support queues based on message sentiment and urgency.
- **Automated Response Triggers**
    - Initiates immediate acknowledgment messages for common queries to manage customer expectations.
- **Data-Driven Hygiene**
    - Cleans and formats incoming contact data before syncing it to your CRM or support dashboard.

---

## Use Cases
**Support Ticket Management**
- Automatically tagging incoming WhatsApp messages as "Urgent" or "Standard" based on keyword analysis.
- Routing technical support requests to the engineering queue while directing billing queries to the finance team.

**Customer Experience Optimization**
- Sending instant, personalized status updates to customers based on their specific support ticket ID.
- Reducing "time-to-first-response" by pre-filling support agent dashboards with summarized customer context.

**Operational Efficiency**
- Filtering out automated bot messages or irrelevant inquiries to keep support queues focused on human-led interactions.
- Aggregating feedback from WhatsApp conversations to identify recurring product issues or service bottlenecks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided JSON template for the WhatsApp Support Triage Agent.
3. Connect your WATI account via the Composio integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw WhatsApp message data from the WATI webhook.
- **Agent**: Analyzes the message context, intent, and sentiment to determine the appropriate action.
- **Composio Toolset**: Executes the routing commands and updates ticket statuses within WATI.
- **Chat Output**: Confirms the successful triage and routing of the message to the support team.

### 3) Run the Flow
Test your workflow in the Uplizd Playground:
- `Categorize this message: "My order #12345 hasn't arrived yet and it's been 2 weeks."`
- `Analyze the urgency of: "I need help resetting my password immediately, this is blocking my work."`
- `Route this inquiry: "Do you offer discounts for non-profit organizations?"`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the triage system, interpreting natural language and mapping it to business logic.
- **Instruction Pattern:**
    - Analyze the incoming WhatsApp message for intent, sentiment, and urgency.
    - Map the intent to the corresponding WATI support category.
    - Format the output to include the customer ID, issue summary, and priority level.

### 2) Composio Toolset Node
- Requires a valid WATI API key to authenticate and perform write operations.
- Connection scope should include read/write access to support tickets and contact management endpoints.

### 3) Tool Availability
- **WATI Ticket Creation**: Capability to generate new tickets from messages.
- **WATI Tagging**: Ability to apply labels for categorization.
- **WATI Message Dispatch**: Capability to send automated confirmation replies.

---

## Related Solutions
- [WhatsApp Support Automator (by TimelinesAI)](../whats-app-support-automator-by-timelinesai/README.md) — Streamline support workflows across WhatsApp and TimelinesAI.
- [WhatsApp Support Ticket Manager (by Spoki)](../whats-app-support-ticket-manager-by-spoki/README.md) — Manage support tickets efficiently using Spoki and WhatsApp.
- [WhatsApp Support Triage Agent (by 2Chat)](../whats-app-support-triage-agent-by2chat/README.md) — Alternative triage solution for WhatsApp support via 2Chat.
- [24/7 Customer Support Assistant (by AI ML API)](../247-customer-support-assistant-by-ai-ml-api/README.md) — Comprehensive round-the-clock support automation.
