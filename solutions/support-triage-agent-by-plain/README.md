# Support Triage Agent (Uplizd) - Intelligent customer lookup and automated ticket routing

## Summary
The Support Triage Agent is an AI-driven workflow that streamlines customer service operations by automatically analyzing incoming support requests, performing real-time customer lookup via Plain, and routing threads to the appropriate internal teams. By automating the initial triage process, support teams can significantly reduce response latency, eliminate manual data entry, and ensure that high-priority issues are addressed by the right agents immediately.

---

## Demo
![Support Triage Agent workflow diagram showing Chat Input, Agent, Plain API integration, and Chat Output](image.png)
**Alt text (SEO-ready):** Support Triage Agent workflow diagram showing Chat Input, Agent, Plain API integration, and Chat Output for automated customer service routing on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e9984131-7d83-539a-b709-4d884c3507ae)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** support automation, plain, ticket routing, customer experience, helpdesk, ai workflow, composio, triage
- This solution optimizes helpdesk operations by integrating AI-driven triage directly into your existing support infrastructure.

---

## Who is this for?
This solution is designed for support operations teams and customer success managers looking to scale their service capacity without increasing headcount.

- **Support Operations Manager**
    - Automates ticket classification and routing to reduce manual overhead and improve response times.
- **Customer Success Lead**
    - Ensures high-value accounts receive priority attention by routing their queries to senior support staff.
- **Technical Support Engineer**
    - Eliminates repetitive triage tasks, allowing focus on complex technical resolutions.
- **Head of Customer Experience**
    - Maintains consistent service quality and SLA compliance through standardized, automated ticket handling.

---

## Features
- **Intelligent Intent Classification**
    - Automatically categorizes incoming tickets based on sentiment, urgency, and topic using advanced LLM analysis.
- **Real-time Plain Integration**
    - Seamlessly queries the Plain API to fetch customer profile data and historical interaction context.
- **Automated Routing Logic**
    - Dynamically assigns tickets to specific queues or team members based on pre-defined business rules.
- **Context-Aware Summarization**
    - Generates concise summaries of customer history to provide agents with immediate context upon ticket opening.
- **SLA-Driven Prioritization**
    - Flags urgent requests and escalates them based on customer tier or keyword-based priority detection.

---

## Use Cases
**Ticket Routing & Escalation**
- Automatically route billing-related inquiries to the Finance support queue.
- Escalate tickets containing specific "churn-risk" keywords to a dedicated success manager.

**Customer Profile Enrichment**
- Fetch recent order status directly from Plain to provide immediate answers in the initial response.
- Update ticket metadata with customer lifetime value (CLV) to inform routing priority.

**Support Workflow Optimization**
- Auto-close spam or non-actionable inquiries based on content analysis.
- Draft initial responses for common queries, allowing agents to simply review and approve.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Support Triage Agent template from the marketplace.
3. Connect your Plain API credentials within the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the incoming customer support message or ticket payload.
- **Agent**: Analyzes the input, determines intent, and queries the Plain API.
- **Composio Toolset**: Executes the lookup and routing actions within the Plain platform.
- **Chat Output**: Delivers the triaged ticket status or suggested response to the support dashboard.

### 3) Run the Flow
Test the workflow in the Uplizd Playground using these prompts:
- `Analyze the latest ticket from user ID 12345 and route to the technical team.`
- `Fetch the support history for this customer and summarize their recent issues.`
- `Check if this ticket is urgent based on the customer's subscription tier in Plain.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the triage process, interpreting customer intent and executing API calls.
- **Instruction Pattern:**
    - "Act as a professional support triage assistant."
    - "Always prioritize tickets from enterprise-tier customers."
    - "Use the provided toolset to fetch customer context before routing."

### 2) Composio Toolset Node
- **API Key:** Provide your Plain API key in the environment variables.
- **Connection Scope:** Ensure the agent has read/write access to ticket objects and customer profiles.

### 3) Tool Availability
- **Customer Lookup:** Retrieve profile details, subscription status, and contact info.
- **Ticket Management:** Update ticket status, assignees, and priority labels.
- **History Retrieval:** Fetch previous interaction logs to provide context for the current request.

---

## Related Solutions
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - A comprehensive AI assistant for 24/7 customer query handling.
- [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Automated triage specifically optimized for WhatsApp support channels.
- [WhatsApp Support Ticket Manager](../whats-app-support-ticket-manager-by-spoki/README.md) - End-to-end ticket management for WhatsApp-based customer service.
