# WhatsApp Feedback Collection Agent (Uplizd) - Automated customer sentiment and feedback gathering

## Summary
The WhatsApp Feedback Collection Agent (Uplizd) streamlines the post-interaction experience by automatically soliciting, capturing, and categorizing customer feedback directly through WhatsApp. By leveraging the Composio Toolset to integrate with your messaging infrastructure, this workflow ensures that qualitative customer insights are converted into actionable data, reducing manual follow-up time and increasing response rates for businesses seeking to improve service quality and product satisfaction.

---

## Demo
![WhatsApp Feedback Collection Agent workflow diagram showing Chat Input, Agent processing, and WhatsApp integration](image.png)
**Alt text (SEO-ready):** WhatsApp Feedback Collection Agent (Uplizd) workflow diagram showing automated customer sentiment analysis and feedback integration via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/58f67310-0a52-51db-8e8e-3864199a3955)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** whatsapp, feedback, sentiment analysis, crm, automation, customer experience, composio, ai workflow
- This solution bridges the gap between conversational messaging and data-driven customer experience management.

---

## Who is this for?
This solution is designed for teams looking to capture high-quality customer insights without friction.

- **Customer Success Manager**
    - Automate the collection of CSAT scores immediately following a support ticket resolution.
- **Product Manager**
    - Gather direct user feedback on new feature releases to iterate based on real-world sentiment.
- **Operations Lead**
    - Centralize feedback data from disparate WhatsApp conversations into a single source of truth.
- **Support Team Lead**
    - Reduce manual outreach efforts by triggering automated feedback requests after specific interaction milestones.

---

## Features
- **Automated Triggering**
    - Initiates feedback requests via WhatsApp based on predefined event triggers or ticket closure status.
- **Sentiment Analysis**
    - Utilizes the Agent node to interpret natural language responses and categorize customer sentiment as positive, neutral, or negative.
- **Composio-Powered Integration**
    - Seamlessly connects with WhatsApp APIs and CRM platforms to log feedback directly against customer profiles.
- **Real-time Data Sync**
    - Ensures that captured feedback is instantly available for reporting and team review in your connected dashboard.
- **Customizable Prompting**
    - Allows for tailored feedback questions that adapt based on the context of the previous customer interaction.

---

## Use Cases
**Post-Support Satisfaction**
- Trigger a WhatsApp message asking for a 1-5 star rating immediately after a support ticket is marked as "Resolved."
- Automatically log the rating and any accompanying comments into your CRM for performance tracking.

**Product Feature Validation**
- Send targeted feedback requests to users who have recently engaged with a specific new product feature.
- Analyze qualitative responses to identify common pain points or requested improvements.

**Customer Churn Prevention**
- Identify negative sentiment in real-time and alert the account management team to intervene before a customer churns.
- Route urgent negative feedback directly to a human agent for immediate follow-up.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your WhatsApp and CRM accounts via the Composio connection manager.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or customer message payload.
- **Agent**: Processes the feedback content, performs sentiment analysis, and formats the data.
- **Composio Toolset**: Executes the API calls to update your CRM or messaging platform.
- **Chat Output**: Confirms the successful logging of feedback or triggers a follow-up response.

### 3) Run the Flow
Use the Playground to test your feedback collection logic:
- `Send a feedback request to the last customer who closed a ticket.`
- `Analyze the sentiment of the latest WhatsApp feedback and update the CRM notes.`
- `Summarize the feedback received today and send a report to the support team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the intelligence layer for parsing customer tone and intent.
- Use a model capable of high-accuracy sentiment classification (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a feedback analyst. Extract the sentiment score and key topics from the customer's WhatsApp message."
- Instruction: "If the sentiment is negative, flag the entry as 'Urgent' for the support team."

### 2) Composio Toolset Node
- Provide your API key to enable secure communication with your WhatsApp Business API and CRM.
- Set the connection scope to allow the agent to read conversation history and write feedback data to your customer records.

### 3) Tool Availability
- **WhatsApp API**: For sending and receiving messages.
- **CRM Connector**: For logging feedback and updating customer status.
- **Sentiment Analyzer**: For real-time classification of incoming text.

---

## Related Solutions
- [WhatsApp Feedback Collector (WATI)](../whats-app-feedback-collector-by-wati/README.md) - Alternative feedback collection using WATI integration.
- [WhatsApp Support Triage Agent (2Chat)](../whats-app-support-triage-agent-by2chat/README.md) - Manage incoming support inquiries and triage them automatically.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your customer data synchronized across multiple platforms.
- [WhatsApp Lead Qualifier (2Chat)](../whats-app-lead-qualifier-by2chat/README.md) - Qualify leads directly through WhatsApp conversations.
