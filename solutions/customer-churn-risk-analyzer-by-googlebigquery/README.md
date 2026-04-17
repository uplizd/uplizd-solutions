# Customer Churn Risk Analyzer (Uplizd) - Proactive retention through behavioral data intelligence

## Summary
The Customer Churn Risk Analyzer is an automated Uplizd workflow that ingests behavioral data from Google BigQuery to identify at-risk accounts before they churn. By synthesizing usage patterns, support ticket volume, and engagement metrics, this solution empowers RevOps and Customer Success teams to intervene with data-driven retention strategies, ultimately increasing customer lifetime value and reducing revenue leakage.

---

## Demo
![Customer Churn Risk Analyzer workflow dashboard showing BigQuery data integration and risk scoring nodes](image.png)
**Alt text (SEO-ready):** Customer Churn Risk Analyzer dashboard in Uplizd, showcasing Google BigQuery data integration, churn prediction logic, and automated risk scoring for customer retention workflows.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDREuG6127QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lPUEckHc6jAAAAF0lEQVR42mP8z8AABgBhoGqQoQAAAP//AwD/9wQ+9o8AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/7f0d8f12-1f44-54b5-b0c0-887c9f67fe91)

---

## Category
- **Primary category:** Customer Success
- **Secondary tags:** churn, bigquery, data analytics, retention, customer health, predictive modeling, composio, ai workflow
- This solution bridges the gap between raw warehouse data and actionable retention insights for customer-facing teams.

---

## Who is this for?
This solution is designed for data-driven organizations focused on maintaining high net revenue retention (NRR) through proactive account management.

- **Customer Success Managers**
    - Receive automated alerts on accounts showing declining engagement or increased support friction.
- **RevOps Analysts**
    - Standardize churn risk scoring across the organization using unified BigQuery datasets.
- **Account Executives**
    - Access real-time health scores before renewal calls to tailor their messaging and value proposition.
- **Product Managers**
    - Correlate feature usage drops with churn risk to prioritize roadmap items that drive stickiness.

---

## Features
- **BigQuery Data Integration**
    - Seamlessly queries large-scale behavioral datasets to extract meaningful usage trends.
- **Predictive Risk Scoring**
    - Calculates a weighted churn probability score based on custom business logic and historical patterns.
- **Automated Alerting**
    - Triggers notifications to CRM or Slack when an account crosses a critical risk threshold.
- **Contextual Insights**
    - Aggregates support ticket history and recent activity logs to provide a 360-degree view of account health.
- **Composio-Powered Execution**
    - Leverages the Composio Toolset to bridge the gap between BigQuery data and external communication platforms.

---

## Use Cases
**Proactive Retention Outreach**
- Identify "at-risk" accounts with low login frequency in the last 30 days.
- Automatically draft personalized email templates for CSMs to send to high-risk clients.

**Support Friction Analysis**
- Flag accounts that have submitted more than three high-priority tickets in a single week.
- Correlate support ticket volume with feature adoption rates to identify product-related frustration.

**Renewal Pipeline Management**
- Generate a "Health Score" report for all accounts with renewals due in the next 90 days.
- Prioritize account outreach based on the calculated churn risk score to maximize renewal success.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Churn Risk Analyzer template from the marketplace.
3. Configure your Google BigQuery credentials within the environment settings.
4. Ensure nodes are correctly mapped from Chat Input to the Agent and finally to the Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the account ID or customer segment request.
- **Agent**: Processes data queries and evaluates churn risk based on provided instructions.
- **Composio Toolset**: Executes SQL queries against BigQuery and formats the resulting data.
- **Chat Output**: Returns a summarized risk report with actionable recommendations.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Analyze churn risk for Account ID 8842 and summarize recent support activity.`
- `Which accounts in the 'Enterprise' segment have a churn risk score higher than 70?`
- `Provide a list of customers with declining usage patterns over the last quarter.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data analyst that translates natural language queries into actionable retention insights.
- Instruct the agent to prioritize high-impact metrics like login frequency and ticket volume.
- Ensure the agent maintains a professional, objective tone when reporting risk scores.
- Configure the agent to provide specific, actionable steps for CSMs to take based on the risk level.

### 2) Composio Toolset Node
- Provide a valid Google BigQuery API key with read-only access to the relevant customer data tables.
- Set the connection scope to include specific datasets containing usage logs and support ticket history.

### 3) Tool Availability
- **BigQuery Query Executor**: Allows the agent to run complex SQL queries on usage data.
- **Data Formatter**: Converts raw SQL output into readable summaries for the end user.
- **Notification Connector**: Enables the agent to push alerts to configured communication channels.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks real-time account engagement and usage metrics.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages sales stages and identifies stalled opportunities.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gathers external account intelligence for deeper customer insights.
