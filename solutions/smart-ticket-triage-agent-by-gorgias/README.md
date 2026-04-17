# Smart Ticket Triage Agent (Uplizd) - Automated customer support routing and categorization

## Summary
The Smart Ticket Triage Agent is an intelligent Uplizd workflow that streamlines customer support operations by automatically analyzing incoming tickets, categorizing them by intent, and routing them to the appropriate support queue. By leveraging AI-driven classification, this solution reduces manual triage time, eliminates human error in ticket assignment, and ensures that high-priority issues reach the right agents immediately, significantly improving overall pipeline velocity and customer satisfaction.

---

## Demo
![Smart Ticket Triage Agent workflow diagram showing ticket input, AI classification, and routing to Gorgias support queues](image.png)
**Alt text (SEO-ready):** Smart Ticket Triage Agent workflow for automated customer support routing, AI-powered ticket categorization, and Gorgias integration on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8391ae28-539f-563e-ac7f-8243873fca44)

---

## Category
- **Primary category:** Support operations
- **Secondary tags:** customer support, gorgias, ticket triage, ai workflow, automation, helpdesk, ticketing, composio
- This solution optimizes helpdesk efficiency by automating the classification and distribution of support requests across your Gorgias infrastructure.

---

## Who is this for?
This solution is designed for support teams and operations managers looking to scale their response capabilities without increasing headcount.

- **Support Manager**
    - Reduces ticket backlog by automating the initial triage and routing process for incoming inquiries.
- **Customer Experience Lead**
    - Ensures consistent service levels by routing high-priority or sensitive tickets to specialized agents immediately.
- **Support Operations Specialist**
    - Maintains clean ticket data and accurate reporting by standardizing categorization across all support channels.
- **Frontline Support Agent**
    - Eliminates time spent on manual ticket sorting, allowing for faster resolution of customer issues.

---

## Features
- **Intelligent Intent Classification**
    - Uses advanced LLMs to analyze ticket content and assign accurate categories based on your specific business logic.
- **Automated Routing Logic**
    - Dynamically assigns tickets to the correct Gorgias team or agent based on priority, language, or product expertise.
- **Real-Time Integration**
    - Connects directly to your helpdesk via the Composio Toolset to fetch and update ticket statuses in real-time.
- **Priority Detection**
    - Automatically flags urgent or sensitive customer inquiries for immediate escalation to senior support staff.
- **Workflow Customization**
    - Easily adjust triage rules and routing criteria within the Uplizd builder to match evolving support requirements.

---

## Use Cases
**High-Volume Support Management**
- Automatically route "Order Status" inquiries to the shipping queue while flagging "Refund Request" tickets for billing specialists.
- Reduce first-response time by pre-populating ticket metadata before it reaches a human agent.

**Priority Escalation**
- Identify and escalate tickets containing negative sentiment or urgent keywords to a dedicated "VIP Support" team.
- Ensure that technical bugs are routed directly to the engineering support queue based on specific error code detection.

**Data Hygiene & Reporting**
- Standardize ticket tagging across all channels to ensure accurate reporting on support volume and common customer pain points.
- Automatically archive or close spam-like inquiries to keep the active support queue focused on genuine customer needs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in the Uplizd builder.
2. Connect your Gorgias account within the Composio Toolset node.
3. Configure your specific routing rules in the Agent instructions.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw ticket data or customer inquiry text.
- **Agent**: Processes the text, identifies the intent, and determines the appropriate routing action.
- **Composio Toolset**: Executes the API calls to update the ticket status or assign it to a specific queue in Gorgias.
- **Chat Output**: Confirms the successful triage and routing of the ticket to the agent dashboard.

### 3) Run the Flow
Test the triage logic in the Playground using these example prompts:
- `Categorize and route this ticket: "My order #12345 hasn't arrived yet, where is it?"`
- `Analyze this message and escalate if urgent: "I am extremely frustrated, my account is locked and I cannot access my data!"`
- `Triage this inquiry: "How do I update my billing information for my monthly subscription?"`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the triage process, interpreting customer intent and applying business rules.
- **Recommended instruction pattern:**
    - Act as a professional support triage assistant.
    - Analyze the ticket content to determine the primary intent and urgency level.
    - Map the intent to the predefined Gorgias queue and apply the correct tags.

### 2) Composio Toolset Node
- **API Key**: Ensure your Gorgias API key is securely stored in the Composio configuration.
- **Connection Scope**: Grant the toolset permissions to read tickets, update ticket fields, and modify assignments.

### 3) Tool Availability
- **Ticket Fetcher**: Retrieves new ticket details from the helpdesk queue.
- **Ticket Updater**: Modifies ticket status, tags, and assignee fields.
- **Queue Manager**: Identifies and selects the appropriate destination queue for the ticket.

---

## Related Solutions
- [../247-customer-support-assistant-by-ai-ml-api/README.md](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-driven assistant for 24/7 customer support automation.
- [../247-customer-support-chatbot-by-botstar/README.md](../247-customer-support-chatbot-by-botstar/README.md) - Automated chatbot solution for handling customer inquiries.
- [../whats-app-support-triage-agent-by-wati/README.md](../whats-app-support-triage-agent-by-wati/README.md) - Specialized triage agent for WhatsApp support channels.
