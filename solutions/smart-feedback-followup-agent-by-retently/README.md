# Smart Feedback Follow-up Agent (Uplizd) - Automate personalized responses to customer feedback

## Summary
The Smart Feedback Follow-up Agent is an intelligent workflow designed to bridge the gap between customer sentiment and proactive engagement. By automatically analyzing feedback scores and comments from Retently, the agent crafts and sends personalized follow-up responses to both detractors and promoters. This solution ensures no customer voice goes unheard, significantly improving retention rates, closing the feedback loop, and maintaining high-quality customer relationships without manual intervention.

---

## Demo
![Smart Feedback Follow-up Agent workflow diagram showing Retently feedback analysis and automated response generation](image.png)
**Alt text (SEO-ready):** Smart Feedback Follow-up Agent workflow diagram showing Retently feedback analysis and automated response generation using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dbd39d15-a5b4-5485-a77b-7683f413fb23)

---

## Category
- **Primary category:** Customer Experience
- **Secondary tags:** retently, feedback loop, customer sentiment, nps, automated follow-up, customer retention, composio, ai workflow
- This solution streamlines the customer feedback lifecycle by automating personalized outreach based on real-time sentiment analysis.

---

## Who is this for?
This agent is designed for teams focused on maintaining high customer satisfaction and proactive relationship management.

- **Customer Success Manager**
    - Automate the initial response to negative feedback to prevent churn and address concerns immediately.
- **Support Operations Lead**
    - Standardize the feedback follow-up process to ensure consistent communication across all customer segments.
- **Product Manager**
    - Gain deeper insights into user sentiment by facilitating direct follow-up conversations with power users.
- **Growth Marketer**
    - Leverage positive feedback from promoters to encourage referrals and build brand advocacy.

---

## Features
- **Automated Sentiment Analysis**
    - Instantly categorizes incoming Retently feedback as positive, neutral, or negative to trigger appropriate response paths.
- **Personalized Response Generation**
    - Uses advanced LLMs to draft context-aware replies that reference specific feedback comments for a human-like touch.
- **Multi-Channel Integration**
    - Connects seamlessly with your CRM and communication tools via the Composio Toolset to deliver messages where they matter most.
- **Real-Time Feedback Loop**
    - Reduces the time-to-response by triggering actions immediately upon feedback submission, ensuring customers feel valued.
- **Customizable Tone and Policy**
    - Allows for fine-tuned instruction sets to ensure all automated follow-ups align with your company's brand voice and support guidelines.

---

## Use Cases
**Churn Prevention**
- Automatically escalate negative feedback from detractors to a human agent for urgent intervention.
- Draft empathetic apology and resolution emails to customers who report low satisfaction scores.

**Advocacy Building**
- Identify high-scoring promoters and send automated requests for testimonials or case study participation.
- Send personalized thank-you messages to loyal customers to reinforce positive brand sentiment.

**Operational Efficiency**
- Categorize and tag feedback automatically within your CRM to keep customer profiles updated with the latest sentiment data.
- Sync feedback data across platforms to ensure cross-functional teams have visibility into customer health.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Authenticate your Retently and CRM accounts within the Uplizd dashboard.
3. Configure your API keys for the required integrations in the settings panel.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw feedback data and sentiment metadata from Retently.
- **Agent**: Processes the feedback, determines the sentiment, and drafts a tailored response.
- **Composio Toolset**: Executes the delivery of the response via your chosen communication platform (e.g., Email or CRM).
- **Chat Output**: Confirms the successful delivery of the follow-up and logs the action.

### 3) Run the Flow
Use the Playground to test your agent with these example prompts:
- `Analyze the latest feedback from Retently and draft a response for a detractor who mentioned slow support.`
- `Identify all promoters from the last 24 hours and send a thank-you message via email.`
- `Summarize recent negative feedback and suggest a follow-up action plan for the success team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a customer experience specialist, balancing empathy with professional efficiency.
- **Instruction Pattern:**
    - Analyze the sentiment score and the specific text provided in the feedback.
    - Adopt a tone that matches the customer's sentiment (apologetic for detractors, celebratory for promoters).
    - Ensure all responses include a clear call to action or a path for further resolution.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable secure access to your integrated tools.
- **Connection Scope:** Ensure the toolset has read/write permissions for your Retently account and your primary CRM or email provider.

### 3) Tool Availability
- **Retently API**: For fetching feedback scores and customer comments.
- **CRM/Email Connectors**: For sending personalized follow-up messages.
- **Sentiment Analysis Engine**: For classifying feedback intensity.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-powered support assistant for 24/7 customer query resolution.
- [whats-app-feedback-collection-agent-by-wati](../whats-app-feedback-collection-agent-by-wati/README.md) - Collect customer feedback directly through WhatsApp channels.
- [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md) - Monitor account health and usage metrics to proactively manage customer satisfaction.
