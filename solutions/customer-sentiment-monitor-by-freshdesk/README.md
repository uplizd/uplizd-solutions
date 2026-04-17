# Customer Sentiment Monitor (Uplizd) - Real-time support feedback analysis and churn prevention

## Summary
The Customer Sentiment Monitor is an automated Uplizd workflow that ingests support tickets from Freshdesk to analyze customer emotional tone and urgency. By leveraging the Composio Toolset to interface with your helpdesk, this solution provides RevOps and Support teams with a single source of truth for account health, enabling proactive intervention before negative sentiment leads to churn.

---

## Demo
![Customer Sentiment Monitor workflow dashboard showing Freshdesk ticket analysis and sentiment scoring](image.png)
**Alt text (SEO-ready):** Customer Sentiment Monitor dashboard in Uplizd showing Freshdesk ticket sentiment analysis, automated support triage, and churn prevention workflows.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/282ea3fe-419c-5a0b-9f51-87c90fd2a80a)

---

## Category
- **Primary category:** Support operations
- **Secondary tags:** freshdesk, sentiment analysis, customer success, churn prevention, support automation, composio, ai workflow, data hygiene
- This solution bridges the gap between raw support interactions and actionable business intelligence by categorizing customer feedback at scale.

---

## Who is this for?
This solution is designed for teams managing high-volume support environments who need to prioritize human intervention based on data-driven sentiment signals.

- **Customer Success Manager**
    - Proactively identify at-risk accounts before they reach a critical churn threshold.
- **Support Operations Lead**
    - Optimize ticket routing by surfacing high-urgency, negative sentiment issues to senior agents.
- **Product Manager**
    - Aggregate qualitative feedback trends to inform product roadmap priorities and feature requests.
- **RevOps Analyst**
    - Maintain data hygiene by tagging CRM records with sentiment scores derived from support interactions.

---

## Features
- **Real-time Sentiment Scoring**
    - Automatically evaluates the emotional tone of incoming Freshdesk tickets using advanced LLM analysis.
- **Automated Triage Logic**
    - Dynamically updates ticket priority levels based on sentiment intensity and keyword detection.
- **Seamless Freshdesk Integration**
    - Utilizes the Composio Toolset to read, update, and categorize tickets directly within your helpdesk environment.
- **Churn Risk Alerting**
    - Triggers internal notifications when specific negative sentiment patterns or "churn" keywords are identified.
- **Historical Trend Reporting**
    - Aggregates sentiment data over time to visualize shifts in customer satisfaction across different product segments.

---

## Use Cases
**Proactive Churn Mitigation**
- Automatically flag tickets containing "cancel" or "refund" for immediate escalation to a Success Manager.
- Generate a weekly summary of accounts showing a downward trend in sentiment over the last 30 days.

**Support Efficiency Optimization**
- Route tickets with "frustrated" sentiment to specialized retention agents instead of the general queue.
- Auto-tag tickets with sentiment labels (e.g., "Positive," "Neutral," "Urgent Negative") to streamline reporting.

**Product Feedback Loop**
- Extract feature requests from positive sentiment tickets to prioritize development efforts.
- Identify recurring pain points in negative tickets to create targeted knowledge base articles or bug reports.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your Freshdesk account via the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives ticket data triggers from Freshdesk.
- **Agent**: Processes text to determine sentiment and urgency.
- **Composio Toolset**: Executes API actions to update ticket tags and custom fields.
- **Chat Output**: Returns the analysis summary to your dashboard or Slack notification channel.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Analyze the sentiment of the latest 10 tickets in the 'General' queue.`
- `Identify all tickets from the last 24 hours that contain negative sentiment and escalate them.`
- `Summarize the top 3 customer complaints from this week and suggest a response strategy.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the analytical engine.
- **Role:** Customer Support Sentiment Analyst.
- **Recommended instruction pattern:**
    - Analyze the provided ticket body for emotional cues and urgency.
    - Categorize the sentiment on a scale of 1–5.
    - Output the result in a structured format compatible with Freshdesk custom fields.

### 2) Composio Toolset Node
- **API Key:** Provide your Freshdesk API key within the Composio connection settings.
- **Connection Scope:** Ensure the scope allows for `read_tickets` and `update_ticket_properties`.

### 3) Tool Availability
- `freshdesk_get_tickets`: Fetches recent ticket data for analysis.
- `freshdesk_update_ticket`: Applies sentiment tags and priority updates.
- `freshdesk_list_customers`: Retrieves account context for high-value customer identification.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-powered assistant for general support query resolution.
- [247-customer-support-chatbot-by-botstar](../247-customer-support-chatbot-by-botstar/README.md) - Automated chatbot solution for instant customer response.
- [whats-app-support-triage-agent-by-wati](../whats-app-support-triage-agent-by-wati/README.md) - Triage support tickets specifically for WhatsApp channels.
