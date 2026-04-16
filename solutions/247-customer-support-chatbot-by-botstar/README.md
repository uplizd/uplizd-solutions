# 24/7 Customer Support Chatbot (Uplizd) - Automated AI-driven customer inquiry resolution

## Summary
The 24/7 Customer Support Chatbot by Botstar is an intelligent AI workflow designed to provide instant, accurate responses to customer inquiries around the clock. By leveraging the Composio toolset to interface with support platforms, this solution reduces response latency, ensures consistent brand messaging, and offloads repetitive ticket volume from human agents, ultimately driving higher customer satisfaction and operational efficiency.

---

## Demo
![24/7 Customer Support Chatbot workflow interface showing automated inquiry handling and agent response routing](image.png)
**Alt text (SEO-ready):** 24/7 Customer Support Chatbot workflow in Uplizd, featuring automated AI inquiry resolution and Botstar integration for real-time customer service.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/a851e93e-47cb-5f98-9291-352a1c69ed30)

---

## Category
**Customer Support Automation**
- `support`, `chatbot`, `botstar`, `ai-agent`, `customer-experience`, `automation`, `composio`, `real-time`
This solution streamlines customer service operations by automating routine interactions and providing a scalable AI-first support layer.

---

## Who is this for?
This solution is designed for teams looking to scale their support capacity without increasing headcount.

- **Customer Support Manager**
    - Reduces ticket backlog and decreases average response time for common inquiries.
- **Operations Lead**
    - Standardizes support quality across all customer touchpoints using AI-driven logic.
- **Product Owner**
    - Gains insights into recurring customer pain points through automated conversation logging.
- **Growth Marketer**
    - Ensures 24/7 engagement with prospects, preventing lead drop-off during off-hours.

---

## Features
- **Intelligent Intent Recognition**
    - Uses advanced LLMs to accurately categorize customer queries and determine the appropriate resolution path.
- **Botstar Integration**
    - Seamlessly connects with the Botstar platform to sync conversation history and trigger automated workflows.
- **Real-Time Response Generation**
    - Delivers instant, context-aware answers to FAQs, reducing the need for human intervention.
- **Escalation Logic**
    - Automatically identifies complex or high-priority issues and routes them to human support agents.
- **Workflow Observability**
    - Provides a transparent view of the agent's decision-making process via the Uplizd node architecture.

---

## Use Cases
**Routine Inquiry Resolution**
- Automatically answering common "Where is my order?" (WISMO) queries using real-time tracking data.
- Providing instant responses to pricing and feature questions based on the latest knowledge base documentation.

**After-Hours Support**
- Maintaining continuous service coverage during weekends and holidays without requiring manual staffing.
- Capturing detailed customer information and issue descriptions for follow-up by the support team the next business day.

**Customer Feedback Collection**
- Proactively asking for CSAT scores immediately following the resolution of a chat interaction.
- Aggregating common user complaints to identify trends for product improvement.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to access the solution template.
2. Select "Import" to load the workflow into your workspace.
3. Connect your Botstar API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw customer messages and triggers the workflow.
- **Agent**: Analyzes the intent and formulates a helpful, brand-aligned response.
- **Composio Toolset**: Executes specific support actions or retrieves data from connected platforms.
- **Chat Output**: Delivers the final response back to the customer interface.

### 3) Run the Flow
Use the Playground to test the bot with these prompts:
- `What are your current shipping timelines for international orders?`
- `I need to update the billing address on my recent invoice #12345.`
- `How do I reset my account password if I no longer have access to my recovery email?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the support bot, interpreting user intent and managing the conversation flow.
- Set the system prompt to define the brand voice and support boundaries.
- Enable "Function Calling" to allow the agent to utilize the Composio Toolset.
- Configure temperature settings (recommended: 0.2–0.4) to ensure factual and consistent responses.

### 2) Composio Toolset Node
- Input your Botstar API key to authorize the agent to perform actions on your behalf.
- Define the connection scope to include read/write access to support tickets and customer profiles.

### 3) Tool Availability
- **Ticket Retrieval**: Fetch status updates for existing customer inquiries.
- **Knowledge Base Query**: Search internal documentation to provide accurate answers.
- **Escalation Trigger**: Flag conversations for human review based on sentiment or complexity.

---

## Related Solutions
- [24/7 Customer Support Assistant (AI/ML API)](../247-customer-support-assistant-by-ai-ml-api/README.md) - Alternative support automation using AI/ML API.
- [WhatsApp Support Triage Agent (Wati)](../whats-app-support-triage-agent-by-wati/README.md) - Automated triage for support requests via WhatsApp.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean customer records for better support context.
- [Smart Task Management Agent](../smart-task-management-agent/README.md) - Automate follow-up tasks generated from support conversations.
