# Customer Feedback Processing Agent (Uplizd) - Automated sentiment analysis and HubSpot routing

## Summary
The Customer Feedback Processing Agent streamlines your support operations by automatically ingesting, categorizing, and routing customer feedback directly into HubSpot. By leveraging AI to interpret sentiment and urgency, this workflow eliminates manual ticket triage, ensures high-priority issues reach the right team immediately, and maintains a single source of truth for customer satisfaction data.

---

## Demo
![Customer Feedback Processing Agent workflow showing Chat Input, AI Agent, HubSpot connector, and Chat Output](image.png)
**Alt text (SEO-ready):** Customer Feedback Processing Agent (Uplizd) workflow for automated HubSpot ticket routing, sentiment analysis, and support automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/79755125-015c-5be9-9db7-d6a8f0c81bd1)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** hubspot, feedback, sentiment analysis, ticket routing, support automation, ai workflow, composio, customer experience
- This solution bridges the gap between raw customer feedback and actionable CRM data, enabling teams to scale their response times without increasing headcount.

---

## Who is this for?
This solution is designed for support and success teams looking to reduce manual administrative overhead and improve response quality.

- **Support Manager**
    - Automate ticket triage to ensure urgent issues are addressed by the correct team members instantly.
- **Customer Success Lead**
    - Gain real-time visibility into customer sentiment trends and identify churn risks before they escalate.
- **Operations Specialist**
    - Maintain clean, categorized data within HubSpot by enforcing standardized feedback tagging across all channels.
- **Product Manager**
    - Extract actionable feature requests and pain points directly from support tickets to inform the product roadmap.

---

## Features
- **Intelligent Sentiment Analysis**
    - Automatically detects the emotional tone of feedback, allowing agents to prioritize angry or frustrated customers.
- **Automated HubSpot Routing**
    - Seamlessly creates or updates tickets in HubSpot based on the feedback content and urgency level.
- **Contextual Categorization**
    - Uses AI to classify feedback into predefined buckets like "Feature Request," "Bug Report," or "Billing Inquiry."
- **Real-time Data Sync**
    - Ensures that every piece of feedback is logged in your CRM immediately, providing a unified view of the customer journey.
- **Composio Toolset Integration**
    - Leverages the Composio Toolset to securely interact with HubSpot APIs, ensuring reliable and authenticated data operations.

---

## Use Cases
**Support Ticket Triage**
- Automatically route "Urgent" feedback to the Tier 2 support queue in HubSpot.
- Assign "Billing" related feedback directly to the finance support alias.

**Customer Sentiment Tracking**
- Flag negative feedback for immediate follow-up by a Customer Success Manager.
- Generate weekly sentiment reports based on the categorized feedback stored in HubSpot.

**Product Feedback Loop**
- Automatically tag and group feature requests to identify the most requested improvements.
- Link feedback directly to specific customer accounts in HubSpot for better account intelligence.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and click "Import Flow."
3. Connect your HubSpot account within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw customer feedback text and metadata.
- **Agent**: Processes the text, performs sentiment analysis, and determines the appropriate HubSpot action.
- **Composio Toolset**: Executes the API calls to create or update records in HubSpot.
- **Chat Output**: Confirms the successful routing or logging of the feedback to the user.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Analyze this feedback: "I'm really frustrated that the export feature has been broken for three days. Please help!"`
- `Categorize this: "It would be amazing if you added a dark mode to the dashboard."`
- `Process this feedback: "The billing invoice I received today is incorrect, please fix it."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the operation, interpreting intent and mapping it to CRM actions.
- Use a system instruction that emphasizes objective sentiment scoring.
- Define specific output schemas for HubSpot ticket fields (e.g., Priority, Category).
- Instruct the agent to summarize the feedback before sending it to the CRM.

### 2) Composio Toolset Node
- Provide your HubSpot API key or OAuth credentials within the Composio configuration.
- Ensure the connection scope includes read/write access to Tickets, Contacts, and Companies.

### 3) Tool Availability
- **HubSpot CRM**: For creating tickets and updating contact properties.
- **Sentiment Analyzer**: For evaluating the urgency and tone of incoming messages.
- **Data Formatter**: For standardizing input text before CRM ingestion.

---

## Related Solutions
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - A general-purpose support agent for 24/7 query resolution.
- [WhatsApp Support Ticket Manager](../whats-app-support-ticket-manager-by-spoki/README.md) - Manage support tickets directly through WhatsApp channels.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your CRM data consistent across multiple platforms.
