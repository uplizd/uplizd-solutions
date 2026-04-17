# Survey Campaign Optimization Agent (Uplizd) - Data-driven survey timing and response targeting

## Summary
The Survey Campaign Optimization Agent leverages Uplizd AI workflows to analyze customer behavior and response patterns, enabling businesses to automate the timing and targeting of survey distributions. By integrating real-time engagement data with Retently, this solution improves response rates, minimizes survey fatigue, and provides a single source of truth for customer sentiment analysis.

---

## Demo
![Survey Campaign Optimization Agent dashboard showing response rate analytics and automated trigger configurations](image.png)
**Alt text (SEO-ready):** Survey Campaign Optimization Agent dashboard for Uplizd, showing automated Retently survey triggers, customer response analytics, and data-driven campaign timing workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/68ee1a0c-5e40-56fc-8c82-d1ae48a96ba0)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** retently, survey, customer feedback, campaign optimization, customer experience, data-driven, automation, ai workflow
- This solution bridges the gap between raw customer interaction data and actionable feedback collection strategies to drive higher engagement.

---

## Who is this for?
This agent is designed for teams looking to maximize the quality and volume of customer feedback through intelligent automation.

- **Customer Success Manager**
    - Automate survey triggers based on specific customer milestones to ensure timely feedback collection.
- **Marketing Operations Lead**
    - Optimize campaign schedules to reduce survey fatigue and increase overall response rates.
- **Product Manager**
    - Gain deeper insights into user sentiment by correlating product usage data with survey feedback.
- **Growth Marketer**
    - Segment audiences for targeted surveys based on behavioral triggers and past interaction history.

---

## Features
- **Behavior-Based Triggers**
    - Automatically initiate survey campaigns when users reach specific engagement thresholds or complete key actions.
- **Intelligent Timing Engine**
    - Analyze historical response patterns to determine the optimal time of day and frequency for sending survey requests.
- **Retently Integration**
    - Seamlessly sync survey data and campaign status with Retently using the Composio Toolset for real-time updates.
- **Response Rate Analytics**
    - Monitor campaign performance metrics directly within the workflow to identify high-performing segments.
- **Automated Feedback Loop**
    - Route survey results into downstream CRM or communication platforms to trigger follow-up actions based on sentiment scores.

---

## Use Cases
**Feedback Lifecycle Management**
- Trigger NPS surveys immediately following a successful support ticket resolution or feature adoption.
- Automatically pause survey campaigns for customers who have provided feedback within the last 30 days to prevent over-surveying.

**Campaign Performance Optimization**
- A/B test different survey delivery times to identify which windows yield the highest completion rates.
- Adjust survey frequency dynamically based on the customer's historical engagement level and account health score.

**Sentiment-Driven Segmentation**
- Segment survey recipients based on their recent product usage intensity to ensure feedback is representative of active users.
- Automatically flag negative feedback for immediate review by the customer success team via Slack or email notifications.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to import the template into your workspace.
2. Connect your Retently account via the Composio Toolset node.
3. Configure your environment variables for API authentication and notification channels.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers from your CRM or behavioral analytics platform.
- **Agent**: Processes customer data to determine if a survey should be sent based on defined logic.
- **Composio Toolset**: Executes the API calls to Retently to trigger campaigns or fetch response data.
- **Chat Output**: Returns the status of the campaign trigger or a summary of the latest survey metrics.

### 3) Run the Flow
Use the Playground to test your agent with these example prompts:
- `Check the current response rate for the 'Q3 Product Feedback' campaign in Retently.`
- `Trigger a new satisfaction survey for customer ID 98765 based on their recent feature usage.`
- `Identify which customer segments have the lowest survey response rates over the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your survey strategy.
- Prioritize accuracy when interpreting customer behavioral data.
- Maintain a neutral, professional tone when summarizing feedback trends.
- Strictly adhere to the logic gates defined for survey frequency and exclusion criteria.

### 2) Composio Toolset Node
- Provide your Retently API key to enable secure communication with your survey campaigns.
- Set the connection scope to allow the agent to read campaign metrics and trigger new survey distributions.

### 3) Tool Availability
- **Campaign Management**: Ability to list, create, and update survey campaigns.
- **Response Tracking**: Capability to fetch individual and aggregate survey response data.
- **Customer Data Access**: Integration with CRM tools to verify customer status before triggering surveys.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automate recovery campaigns based on user behavior.
- [WhatsApp Feedback Collection Agent](../whats-app-feedback-collection-agent-by-whatsapp/README.md) — Collect customer feedback directly through WhatsApp.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Monitor customer usage to inform survey timing.
