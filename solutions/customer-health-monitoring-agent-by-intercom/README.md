# Customer Health Monitoring Agent (Uplizd) - Proactive churn prevention through real-time engagement analytics

## Summary
The Customer Health Monitoring Agent is an automated workflow designed to track customer sentiment and engagement metrics by synthesizing data from Intercom. By continuously analyzing interaction patterns and support history, this agent empowers teams to identify at-risk accounts, prioritize high-value outreach, and maintain long-term customer retention through data-driven insights.

---

## Demo
![Customer Health Monitoring Agent workflow dashboard showing real-time sentiment analysis and churn risk alerts](image.png)
**Alt text (SEO-ready):** Customer Health Monitoring Agent dashboard displaying Uplizd AI workflow, Intercom integration, sentiment analysis, and churn risk metrics.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/220fd865-329a-5ba4-944b-8f586a6fa0b3)

---

## Category
- **Primary category:** Customer Success
- **Secondary tags:** intercom, churn prevention, sentiment analysis, customer health, engagement tracking, ai workflow, composio, retention
- This solution bridges the gap between raw support interactions and actionable customer success strategy.

---

## Who is this for?
This agent is built for teams focused on maintaining high customer lifetime value and reducing churn through proactive intervention.

- **Customer Success Manager**
    - Receive automated alerts for at-risk accounts before they churn.
- **Support Lead**
    - Monitor team performance and sentiment trends across all support tickets.
- **Account Executive**
    - Access summarized health reports to prepare for renewal conversations.
- **Operations Analyst**
    - Aggregate engagement data to refine customer segmentation strategies.

---

## Features
- **Real-time Sentiment Analysis**
    - Automatically processes incoming Intercom messages to detect shifts in customer tone and satisfaction levels.
- **Churn Risk Scoring**
    - Calculates a dynamic health score based on ticket frequency, resolution time, and sentiment markers.
- **Automated Alerting**
    - Triggers notifications to the relevant account owner when a customer's health score drops below a defined threshold.
- **Unified Data Synthesis**
    - Integrates disparate support interactions into a single source of truth for account health.
- **Composio-Powered Orchestration**
    - Leverages the Composio Toolset to securely query Intercom and push updates to your CRM or communication channels.

---

## Use Cases
**Proactive Retention**
- Identify customers with declining sentiment scores to trigger personalized outreach campaigns.
- Flag accounts with high ticket volume for immediate intervention by a senior success manager.

**Performance Benchmarking**
- Analyze sentiment trends across different product tiers to identify common pain points.
- Track the impact of new feature releases on customer engagement and support volume.

**Operational Efficiency**
- Automate the classification of support tickets based on urgency and customer health status.
- Sync health scores directly into your CRM to ensure sales and support are aligned on account status.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided JSON configuration file for the Customer Health Monitoring Agent.
3. Authenticate your Intercom connection via the Composio Toolset node.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to analyze specific account health.
- **Agent**: Processes customer data and applies sentiment analysis logic.
- **Composio Toolset**: Executes API calls to fetch Intercom conversation history and user metadata.
- **Chat Output**: Delivers the health summary and recommended actions to your workspace.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Analyze the health score for customer ID 98765 and summarize recent sentiment.`
- `List all accounts that have shown a negative sentiment shift in the last 48 hours.`
- `Generate a churn risk report for our top 10 enterprise accounts based on Intercom interactions.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized Customer Success analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a Customer Success AI. Analyze the provided Intercom data to calculate a health score from 1-100."
- Instruction: "Always provide a brief justification for the score based on specific ticket content."
- Instruction: "Prioritize identifying 'at-risk' signals such as frustration, repeated issues, or lack of engagement."

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable secure access to the Intercom integration.
- Ensure the connection scope includes `read_conversations` and `read_users` permissions.

### 3) Tool Availability
- **Intercom Search**: Retrieve conversation threads and user profile details.
- **Sentiment Analyzer**: Evaluate text-based feedback for emotional context.
- **Data Aggregator**: Compile metrics into a structured report for the final output.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automated support ticket resolution and management.
- [whats-app-support-ticket-manager-by-spoki](../whats-app-support-ticket-manager-by-spoki/README.md) - Centralized ticket management for WhatsApp communications.
- [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md) - Monitoring account health through form submission data.
