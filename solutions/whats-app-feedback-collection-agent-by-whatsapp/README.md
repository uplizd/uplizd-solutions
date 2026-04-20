# WhatsApp Feedback Collection Agent (Uplizd) - Automated conversational customer insights

## Summary
The WhatsApp Feedback Collection Agent is an intelligent Uplizd workflow designed to automate the solicitation and capture of customer sentiment directly within WhatsApp. By leveraging conversational AI to engage users at key touchpoints, this solution eliminates manual follow-up, ensures high response rates, and provides a single source of truth for actionable customer feedback, ultimately driving product improvements and service excellence.

---

## Demo
![WhatsApp Feedback Collection Agent interface showing an automated survey flow with a customer on WhatsApp](image.png)
**Alt text (SEO-ready):** WhatsApp Feedback Collection Agent (Uplizd) workflow interface showing automated customer survey integration and sentiment analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/42c263e2-7b61-5fe9-84e1-01e3e0362646)

---

## Category
**Primary category:** Customer Experience
**Secondary tags:** whatsapp, feedback, sentiment analysis, conversational ai, customer support, automation, composio, data collection.
This solution streamlines the feedback loop by integrating real-time conversational data collection into your existing customer support and engagement stack.

---

## Who is this for?
This workflow is designed for teams looking to transform passive customer interactions into structured, actionable data.

* **Customer Success Manager**
    * Proactively identify at-risk accounts by gathering sentiment data immediately after support interactions.
* **Product Manager**
    * Collect qualitative feature feedback directly from power users to inform the product roadmap.
* **Marketing Operations Specialist**
    * Automate post-purchase surveys to measure Net Promoter Score (NPS) and customer satisfaction.
* **Support Lead**
    * Reduce ticket resolution time by automating the feedback collection process post-ticket closure.

---

## Features
- **Automated Conversational Surveys**
    Engage customers with natural, human-like questions via WhatsApp to maximize completion rates.
- **Real-time Sentiment Analysis**
    Process incoming text responses using AI to categorize feedback as positive, neutral, or negative instantly.
- **Seamless CRM Integration**
    Automatically sync feedback logs and sentiment scores back to your CRM using the Composio Toolset.
- **Dynamic Follow-up Logic**
    Trigger secondary actions or human intervention based on specific negative feedback keywords or low scores.
- **Centralized Data Repository**
    Aggregate all WhatsApp-based feedback into a unified dashboard for trend analysis and reporting.

---

## Use Cases
**Post-Support Satisfaction**
* Trigger a WhatsApp survey immediately after a support ticket is marked as "Resolved" in your helpdesk.
* Log satisfaction scores directly into the customer's profile for long-term health tracking.

**Product Feature Feedback**
* Reach out to users via WhatsApp after they have utilized a new feature for the first time.
* Capture specific feature requests and store them in your product management tool for review.

**Net Promoter Score (NPS) Campaigns**
* Send automated, non-intrusive NPS surveys to your active user base on a quarterly basis.
* Analyze trends in sentiment over time to measure the impact of recent service improvements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the workflow template.
2. Connect your WhatsApp Business API account within the integration settings.
3. Configure your desired survey questions and logic triggers in the Agent node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the trigger event (e.g., ticket closure or time-based interval).
* **Agent:** Processes the conversation flow and interprets user responses using LLM instructions.
* **Composio Toolset:** Executes API calls to update your CRM or database with the collected feedback.
* **Chat Output:** Sends the survey questions to the customer and confirms receipt of their feedback.

### 3) Run the Flow
Use the Uplizd Playground to test your survey logic:
* `Send a post-support survey to the last closed ticket contact.`
* `Ask the user for a rating from 1 to 10 regarding their recent experience.`
* `Log the feedback and notify the support team if the sentiment is negative.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the conversational engine, ensuring the survey feels natural and context-aware.
* Maintain a professional yet friendly tone consistent with your brand voice.
* Use clear, concise questions to minimize user friction.
* Implement conditional branching to handle non-standard user responses gracefully.

### 2) Composio Toolset Node
Connect your WhatsApp Business API and CRM (e.g., Salesforce, HubSpot) to enable data persistence. Ensure the connection scope includes read/write access to contact records and custom fields for feedback storage.

### 3) Tool Availability
* **WhatsApp API:** For sending and receiving messages.
* **CRM Connector:** For updating contact records and custom feedback objects.
* **Sentiment Analysis Tool:** For real-time classification of incoming text.

---

## Related Solutions
* [WhatsApp Lead Qualification Agent](../whats-app-lead-qualification-agent-by-whatsapp/README.md) - Automate lead scoring and qualification via WhatsApp.
* [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Efficiently route support tickets based on urgency and intent.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean, accurate contact data across your CRM ecosystem.
