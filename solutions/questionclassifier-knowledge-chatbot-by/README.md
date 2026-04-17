# Question Classifier and Knowledge Chatbot (Uplizd) - Intelligent intent routing and automated query resolution

## Summary
The Question Classifier and Knowledge Chatbot is an AI-driven workflow that automatically categorizes incoming user queries and routes them to the appropriate knowledge base or support flow. By leveraging advanced LLM intent detection, this solution reduces manual triage time, ensures accurate information delivery, and significantly improves response velocity for customer-facing teams.

---

## Demo
![Question classifier and knowledge chatbot workflow diagram showing intent detection and automated routing](image.png)
**Alt text (SEO-ready):** Uplizd question classifier and knowledge chatbot workflow diagram showing intent detection, automated routing, and AI-powered query resolution.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f484dbc9-cd6b-5c27-b94d-a02f54db97ef)

---

## Category
- **Primary category:** Customer Support Automation
- **Secondary tags:** ai workflow, intent classification, knowledge base, chatbot, automated routing, customer experience, nlp, composio
- This solution bridges the gap between raw user inquiries and structured knowledge retrieval by automating the classification and response process.

---

## Who is this for?
This solution is designed for teams looking to scale their support operations without increasing headcount.

- **Customer Support Manager**
    - Automates initial ticket triage to ensure high-priority issues reach human agents faster.
- **Technical Support Engineer**
    - Provides instant, accurate answers to common technical queries using indexed knowledge bases.
- **Operations Lead**
    - Reduces the volume of repetitive queries, allowing the team to focus on complex account issues.
- **Product Manager**
    - Gains insights into common user questions to identify gaps in existing documentation or product features.

---

## Features
- **Intelligent Intent Classification**
    - Uses LLMs to analyze user input and categorize questions into specific support topics or departments.
- **Dynamic Knowledge Retrieval**
    - Automatically queries internal documentation or knowledge bases to fetch relevant answers in real-time.
- **Seamless Routing Logic**
    - Directs complex or unresolved queries to human agents via integrated CRM or ticketing platforms.
- **Context-Aware Responses**
    - Maintains conversation history to provide personalized, relevant answers based on previous user interactions.
- **Composio Toolset Integration**
    - Connects the agent to external tools and APIs to verify data or perform actions based on the classified intent.

---

## Use Cases
**Automated Support Triage**
- Automatically route billing-related questions to the finance queue while technical bugs go to engineering.
- Identify urgent keywords in user messages to trigger immediate notifications for the on-call support team.

**Knowledge Base Self-Service**
- Provide instant answers to FAQs by querying internal documentation, reducing the need for live agent intervention.
- Summarize complex knowledge base articles into concise, user-friendly responses tailored to the user's specific question.

**Proactive Customer Engagement**
- Detect common product usage questions and suggest relevant help articles before the user submits a formal ticket.
- Analyze query patterns to identify trending issues and update the knowledge base proactively.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Question Classifier and Knowledge Chatbot template from the marketplace.
3. Connect your preferred LLM provider and API credentials within the configuration panel.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input:** Captures the user's raw question or support query.
- **Agent:** Analyzes the input, determines the intent, and selects the appropriate knowledge source.
- **Composio Toolset:** Executes the search or data retrieval task required to answer the query.
- **Chat Output:** Delivers the final, classified response back to the user.

### 3) Run the Flow
Test the workflow in the Uplizd Playground with these example prompts:
- `How do I reset my account password if I lost access to my email?`
- `What are the current limitations of the API rate usage for my plan?`
- `I need to speak with a billing representative regarding my recent invoice.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the operation. Use the following instruction pattern:
- Define the classification schema clearly (e.g., Billing, Technical, General).
- Instruct the agent to prioritize accuracy and cite sources from the knowledge base.
- Set a fallback instruction for when the intent is unclear or the knowledge base returns no results.

### 2) Composio Toolset Node
- Provide your API key for the relevant knowledge base or CRM integration.
- Define the scope of access to ensure the agent can only read necessary documentation or ticket fields.

### 3) Tool Availability
- **Search API:** For querying internal knowledge bases and help center articles.
- **CRM Connector:** For checking user account status or ticket history.
- **Notification Tool:** For escalating high-priority issues to human support staff.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-powered assistant for 24/7 customer support automation.
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Automated chatbot solution for continuous customer engagement.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Intelligent triage agent for managing WhatsApp support tickets.
