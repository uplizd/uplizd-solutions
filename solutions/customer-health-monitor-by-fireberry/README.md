# Customer Health Monitor (Uplizd) - Proactive churn prevention and engagement tracking

## Summary
The Customer Health Monitor is an intelligent Uplizd workflow that aggregates customer interaction data and usage metrics to provide real-time churn risk assessments. By automating the analysis of support tickets and engagement patterns, this solution enables Customer Success teams to maintain a single source of truth, improve account retention, and proactively address at-risk accounts before they churn.

---

## Demo
![Customer Health Monitor dashboard showing real-time churn risk scores and account engagement metrics](image.png)
**Alt text (SEO-ready):** Customer Health Monitor Uplizd workflow dashboard displaying churn risk, account engagement metrics, and CRM integration status for proactive customer success management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/62777f9f-6066-52a4-8039-c4610fe0da3b)

---

## Category
- **Primary category:** Customer Success
- **Secondary tags:** crm, fireberry, churn, customer health, retention, data analysis, ai workflow, composio
- This solution bridges the gap between raw customer data and actionable retention strategies by leveraging AI to monitor account health in real-time.

---

## Who is this for?
This solution is designed for teams managing high-volume customer relationships who need to prioritize their outreach based on data-driven insights.

- **Customer Success Manager**
    - Identifies at-risk accounts early to initiate personalized retention campaigns.
- **Account Executive**
    - Monitors account health trends to prepare for renewal discussions and upsell opportunities.
- **Support Lead**
    - Tracks ticket volume and sentiment to identify systemic product issues impacting customer satisfaction.
- **RevOps Analyst**
    - Maintains data hygiene across CRM platforms to ensure health scores are based on accurate, up-to-date engagement metrics.

---

## Features
- **Real-time Risk Scoring**
    - Automatically calculates health scores based on recent support activity and engagement frequency.
- **Fireberry CRM Integration**
    - Seamlessly pulls account data and updates health status fields directly within your Fireberry environment.
- **Automated Alerting**
    - Triggers notifications to Slack or email when an account's health score drops below a defined threshold.
- **Sentiment Analysis**
    - Processes support ticket content to detect frustration or churn intent using advanced language models.
- **Composio-Powered Orchestration**
    - Utilizes the Composio Toolset to securely execute read/write operations across your entire customer data stack.

---

## Use Cases
**Churn Prevention**
- Automatically flag accounts with zero logins in the last 14 days for immediate outreach.
- Trigger a "High Risk" status update in the CRM when negative sentiment is detected in recent support tickets.

**Account Expansion**
- Identify "Healthy" accounts with high usage frequency that are prime candidates for upsell conversations.
- Aggregate usage data to provide personalized quarterly business review (QBR) summaries for key stakeholders.

**Support Optimization**
- Prioritize support tickets based on the customer's current health score to ensure high-value clients receive rapid resolution.
- Sync ticket resolution times with account health metrics to identify bottlenecks in the support pipeline.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Connect your Fireberry API credentials within the integration settings.
3. Map your CRM fields to the corresponding workflow variables.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled webhook signals to initiate a health check.
- **Agent**: Analyzes the aggregated data and determines the current health status of the account.
- **Composio Toolset**: Executes the necessary API calls to fetch usage data and update CRM records.
- **Chat Output**: Delivers a summary report of the account's status and recommended next steps.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Check the health status for account ID 98765 and update the CRM if the score is below 50.`
- `List all accounts that have shown a decrease in engagement over the last 30 days.`
- `Generate a summary report for the top 5 at-risk accounts identified this week.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting customer data and applying business logic to score health.
- **Recommended instruction pattern:**
    - "Analyze the provided engagement metrics and support ticket history to assign a health score from 0 to 100."
    - "If the score is below 40, flag the account as 'At-Risk' and provide a brief justification."
    - "Always output the final status in a structured format compatible with CRM field updates."

### 2) Composio Toolset Node
- **API Key**: Ensure your Fireberry and relevant CRM API keys are active in the Composio dashboard.
- **Connection Scope**: Grant read access to support ticket history and write access to account health fields.

### 3) Tool Availability
- **CRM Data Fetcher**: Retrieves account usage and interaction logs.
- **Sentiment Analyzer**: Processes text data from support tickets.
- **CRM Updater**: Writes health scores and risk status back to the CRM.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research into account background and firmographics.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensures consistent data across multiple CRM and support platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Tracks sales stages and manages follow-up workflows for active opportunities.
