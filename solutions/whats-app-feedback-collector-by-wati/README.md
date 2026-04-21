# WhatsApp Feedback Collector (Uplizd) - Automated Customer Sentiment and Feedback Pipeline

## Summary
The WhatsApp Feedback Collector by WATI is an intelligent automation workflow designed to capture, categorize, and analyze customer feedback directly from WhatsApp conversations. By leveraging the Composio Toolset to interface with WATI, this solution enables businesses to transform unstructured chat data into actionable insights, improving response times and customer satisfaction metrics without manual intervention.

---

## Demo
![WhatsApp Feedback Collector workflow diagram showing Chat Input, Agent, WATI integration, and Chat Output](image.png)
**Alt text (SEO-ready):** WhatsApp Feedback Collector workflow diagram showing Chat Input, Agent, WATI integration, and Chat Output for Uplizd automated feedback analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/89699632-5697-537a-978a-ad4adae6eee9)

---

## Category
**Primary category:** Customer Experience (CX) Automation
**Secondary tags:** whatsapp, wati, feedback, sentiment analysis, customer support, automation, composio, ai workflow
This solution bridges the gap between conversational messaging and data-driven product development by automating the feedback loop.

---

## Who is this for?
This solution is designed for teams managing high-volume customer communication who need to extract value from every interaction.

- **Customer Support Manager**
    - Automate the triage of feedback to ensure critical issues are escalated to the right team immediately.
- **Product Manager**
    - Gain real-time visibility into feature requests and pain points directly from the user's preferred messaging channel.
- **Customer Success Lead**
    - Identify at-risk accounts by monitoring sentiment trends in recurring WhatsApp feedback.
- **Operations Specialist**
    - Reduce manual data entry by syncing WhatsApp feedback directly into centralized CRM or analytics platforms.

---

## Features
- **Automated Feedback Capture**
    - Automatically ingest incoming WhatsApp messages categorized as feedback via the WATI API.
- **Sentiment Analysis Engine**
    - Use the Agent node to classify feedback as positive, neutral, or negative in real-time.
- **Intelligent Tagging**
    - Automatically assign relevant tags to feedback based on content, such as "Bug," "Feature Request," or "Pricing."
- **Seamless CRM Integration**
    - Push processed feedback data into your existing stack using the Composio Toolset for unified reporting.
- **Automated Response Loops**
    - Trigger immediate follow-up messages to customers to acknowledge receipt of their feedback, boosting engagement.

---

## Use Cases
**Feedback Triage and Escalation**
- Automatically route negative feedback to the support ticket queue for immediate resolution.
- Flag feature requests and send them to a dedicated product feedback board for review.

**Customer Sentiment Monitoring**
- Track daily sentiment scores across different product lines based on WhatsApp user input.
- Generate weekly reports summarizing common customer complaints and praise for leadership review.

**Operational Efficiency**
- Eliminate manual copy-pasting of feedback from WhatsApp into spreadsheets or project management tools.
- Standardize feedback collection formats to ensure data consistency across all customer interactions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in the builder.
2. Connect your WATI account via the Composio Toolset configuration.
3. Map your preferred WhatsApp trigger events to the workflow input.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input:** Receives raw message data from the WhatsApp webhook.
- **Agent:** Processes the text, determines sentiment, and extracts key entities.
- **Composio Toolset:** Executes actions to update WATI or external databases.
- **Chat Output:** Sends a confirmation message back to the customer or logs the result.

### 3) Run the Flow
Test the flow in the Playground using these prompts:
- `Analyze the sentiment of the last 5 messages from the support queue.`
- `Tag the latest feedback as a "Feature Request" and push it to my product tracker.`
- `Summarize the top 3 customer complaints received via WhatsApp today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain of the workflow.
- **Role:** Act as a Customer Experience Analyst capable of interpreting WhatsApp colloquialisms.
- **Instruction Pattern:** 
    - Always maintain a neutral, objective tone when classifying feedback.
    - Prioritize identifying actionable requests over general sentiment.
    - Ensure all output tags conform to the predefined organizational schema.

### 2) Composio Toolset Node
- **API Key:** Provide your WATI API credentials within the Composio dashboard.
- **Connection Scope:** Ensure the agent has "Read" access to messages and "Write" access to tags or ticket fields.

### 3) Tool Availability
- **WATI Message Reader:** Fetches incoming chat history.
- **WATI Tagging Utility:** Applies labels to conversations.
- **CRM Connector:** Syncs feedback to external databases.

---

## Related Solutions
- [WhatsApp Support Triage Agent (WATI)](../whats-app-support-triage-agent-by-wati/README.md) — Automate ticket routing for support teams.
- [WhatsApp Order Status Agent (WATI)](../whats-app-order-status-agent-by-wati/README.md) — Provide real-time order updates to customers.
- [WhatsApp Lead Qualifier (WATI)](../whats-app-lead-qualifier-by-wati/README.md) — Qualify incoming leads automatically via WhatsApp.
