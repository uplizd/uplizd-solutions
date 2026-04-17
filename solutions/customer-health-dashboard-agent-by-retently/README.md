# Customer Health Dashboard Agent (Uplizd) - Automated NPS and feedback insights for proactive retention

## Summary
The Customer Health Dashboard Agent by Retently streamlines customer success workflows by synthesizing Net Promoter Score (NPS) data with qualitative feedback insights. This Uplizd AI workflow empowers teams to maintain a single source of truth for account health, accelerating response times to at-risk customers and improving overall pipeline velocity through automated, data-driven reporting.

---

## Demo
![Customer Health Dashboard Agent workflow showing NPS data integration and feedback analysis](image.png)
**Alt text (SEO-ready):** Customer Health Dashboard Agent by Retently showing automated NPS data integration, feedback analysis, and Uplizd workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1033463f-a91c-5bdb-be79-039ae9f3d667)

---

## Category
**Primary category:** Customer Success
**Secondary tags:** nps, retently, customer health, feedback analysis, churn prevention, data sync, composio, ai workflow.
This solution bridges the gap between raw customer sentiment data and actionable business intelligence for modern RevOps teams.

---

## Who is this for?
This agent is designed for teams managing high-volume customer relationships who need to prioritize outreach based on real-time sentiment.

- **Customer Success Manager**
    - Proactively identify at-risk accounts before churn occurs using automated sentiment triggers.
- **Support Operations Lead**
    - Standardize health reporting across the organization to ensure consistent service levels.
- **Account Executive**
    - Gain immediate visibility into client satisfaction scores prior to renewal negotiations.
- **Product Manager**
    - Aggregate qualitative feedback to prioritize feature requests based on high-value customer input.

---

## Features
- **Automated NPS Aggregation**
    - Seamlessly pulls real-time scores from Retently to maintain an up-to-date health dashboard.
- **Sentiment Analysis Engine**
    - Leverages AI to categorize open-ended feedback into actionable themes and urgency levels.
- **Composio-Powered Integrations**
    - Connects directly to your CRM and communication tools to trigger alerts based on health status changes.
- **Dynamic Health Scoring**
    - Calculates custom health scores by blending quantitative NPS data with qualitative feedback signals.
- **Real-time Alerting**
    - Notifies stakeholders instantly when a customer's health score drops below a predefined threshold.

---

## Use Cases
**Churn Prevention**
- Automatically flag accounts with declining NPS scores for immediate account manager intervention.
- Generate weekly "At-Risk" reports for leadership meetings based on negative feedback trends.

**Customer Engagement**
- Trigger personalized outreach sequences when a customer provides high NPS scores to encourage advocacy.
- Sync health status updates to CRM custom fields to keep the entire sales team informed.

**Feedback Loop Optimization**
- Route specific product-related feedback directly to the engineering backlog via Jira or Trello integrations.
- Identify common pain points across customer segments to inform quarterly business reviews.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Retently Customer Health Dashboard template from the marketplace.
3. Configure your API credentials for Retently and your CRM within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or scheduled interval for health report generation.
- **Agent**: Processes NPS data and feedback using the configured instruction set.
- **Composio Toolset**: Executes API calls to fetch Retently data and update CRM records.
- **Chat Output**: Delivers the final health summary or alert notification to the user.

### 3) Run the Flow
Use the Playground to test your agent with the following prompts:
- `Generate a health summary for all accounts with an NPS score below 7 in the last 30 days.`
- `Identify top 5 recurring feedback themes from our detractors this month.`
- `Update the CRM health status for all accounts that showed a significant drop in sentiment.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data analyst and customer success strategist.
- Focus on identifying patterns in qualitative feedback rather than just reporting raw numbers.
- Maintain a professional, objective tone when summarizing health risks.
- Prioritize actionable insights that lead to specific follow-up tasks.

### 2) Composio Toolset Node
- Requires a valid Retently API key and appropriate read/write scopes for your CRM.
- Ensure the agent has permission to query feedback endpoints and update account objects.

### 3) Tool Availability
- **Retently API**: For fetching NPS surveys, scores, and respondent feedback.
- **CRM Connector**: For updating account health fields and creating follow-up tasks.
- **Notification Service**: For sending alerts to Slack or email when critical health changes occur.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks product usage metrics to complement NPS data.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Enriches account data with external intent signals.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes customer data across disparate platforms to ensure consistency.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages sales opportunities and deal stages alongside account health.
