# Customer Health Dashboard (Uplizd) - Real-time churn prediction and account health monitoring

## Summary
The Customer Health Dashboard (Uplizd) is an automated AI workflow designed to aggregate usage metrics, support interactions, and account data into a single source of truth. By leveraging the Composio Toolset to connect with platforms like Klipfolio, this solution empowers Customer Success teams to proactively identify churn risks, improve account hygiene, and maintain high pipeline velocity through data-driven insights.

---

## Demo
![Customer Health Dashboard workflow showing data ingestion from Klipfolio to the AI agent for churn risk analysis](image.png)
**Alt text (SEO-ready):** Customer Health Dashboard workflow on Uplizd, featuring Klipfolio data integration for churn risk analysis, account health monitoring, and automated customer success reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/77abf97e-cdfe-5d8b-8902-149d2a320c19)

---

## Category
**Primary category:** Customer Success Operations
**Secondary tags:** crm, klipfolio, churn, account health, data integration, composio, ai workflow, customer retention.
This solution bridges the gap between raw dashboard metrics and actionable customer success strategy.

---

## Who is this for?
This workflow is designed for teams managing high-volume customer portfolios who need to move from reactive support to proactive account management.

*   **Customer Success Manager**
    *   Gain immediate visibility into at-risk accounts before churn occurs.
*   **Operations Lead**
    *   Standardize health scoring across the entire customer base.
*   **Account Executive**
    *   Identify upsell and expansion opportunities based on usage trends.
*   **Support Analyst**
    *   Automate the synthesis of support ticket volume and dashboard health metrics.

---

## Features
- **Automated Health Scoring**
    Calculates real-time health scores by pulling usage data directly from Klipfolio and CRM sources.
- **Churn Risk Alerts**
    Triggers proactive notifications when account health metrics dip below predefined thresholds.
- **Unified Data Sync**
    Centralizes disparate data points into a single, cohesive view for better decision-making.
- **Composio-Powered Integration**
    Uses the Composio Toolset to securely query and update customer metrics across your tech stack.
- **Actionable Insights**
    Generates natural language summaries of account performance for executive reporting.

---

## Use Cases
**Proactive Churn Prevention**
*   Identify accounts with declining usage patterns over a 30-day window.
*   Automatically flag high-value accounts that have not logged into the platform for over a week.

**Account Expansion Identification**
*   Detect accounts nearing usage limits to trigger timely upgrade conversations.
*   Analyze feature adoption rates to identify potential cross-sell opportunities.

**Operational Reporting**
*   Generate weekly health summaries for the entire customer success team.
*   Sync health status updates back to the CRM to keep the entire organization aligned.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to access the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your Klipfolio and CRM accounts within the Composio Toolset node.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the query or trigger signal for the health check.
*   **Agent**: Processes the request and determines which metrics to fetch.
*   **Composio Toolset**: Executes API calls to retrieve data from Klipfolio and relevant CRM fields.
*   **Chat Output**: Delivers the synthesized health report or alert to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
*   `"Show me the top 5 accounts at risk of churn based on current Klipfolio metrics."`
*   `"Generate a health summary for account ID 12345 and identify any recent usage drops."`
*   `"Which accounts have shown the highest growth in usage over the last 30 days?"`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your customer data.
*   Use a model capable of high-reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Instruction: Focus on identifying trends, anomalies, and actionable churn signals.
*   Instruction: Maintain a professional, objective tone suitable for executive reporting.

### 2) Composio Toolset Node
*   Ensure your API keys for Klipfolio and your CRM are active.
*   Set the connection scope to allow read access to usage dashboards and write access to CRM notes/tags.

### 3) Tool Availability
*   **Klipfolio API**: For fetching real-time dashboard metrics and usage data.
*   **CRM Connector**: For retrieving account metadata and updating health status fields.
*   **Notification Service**: For sending alerts to Slack or Email when churn risk is detected.

---

## Related Solutions
*   [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks account engagement and usage patterns.
*   [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gathers external intelligence on account activity.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages sales stages and opportunity follow-ups.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes customer data across multiple platforms.
