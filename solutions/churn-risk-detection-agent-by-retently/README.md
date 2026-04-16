# Churn Risk Detection Agent (Uplizd) - Proactive customer retention and churn mitigation

## Summary
The Churn Risk Detection Agent by Retently is an automated AI workflow designed to identify at-risk customers by analyzing NPS scores, feedback patterns, and usage signals. By centralizing customer sentiment data, this solution enables RevOps and Customer Success teams to intervene early, improve retention rates, and maintain a single source of truth for account health.

---

## Demo
![Churn Risk Detection Agent workflow showing data ingestion from Retently and automated alert triggers](image.png)
**Alt text (SEO-ready):** Churn Risk Detection Agent workflow by Retently for automated NPS analysis, customer sentiment tracking, and churn prevention on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/churn-risk-detection-agent-by-retently)

---

## Category
**Primary category:** Customer Success Automation
**Secondary tags:** churn, retently, nps, customer sentiment, retention, revops, data sync, ai workflow
This solution bridges the gap between raw customer feedback data and actionable retention strategies through intelligent analysis.

---

## Who is this for?
This workflow is designed for teams focused on maintaining high customer lifetime value and reducing revenue leakage.

* **Customer Success Manager**
    * Proactively identifies accounts showing declining sentiment before they reach a churn threshold.
* **RevOps Lead**
    * Standardizes the process of flagging at-risk accounts across the entire customer base.
* **Account Executive**
    * Receives automated alerts to prioritize high-touch outreach for key accounts.
* **Product Manager**
    * Gains aggregate insights into common pain points that drive negative NPS scores.

---

## Features
- **Automated Sentiment Analysis**
  Processes qualitative feedback from Retently to categorize customer mood and urgency.
- **NPS Score Thresholding**
  Triggers immediate alerts when customer NPS scores drop below defined organizational benchmarks.
- **Unified Account Health Dashboard**
  Aggregates disparate feedback signals into a single, actionable view for the success team.
- **Real-time Alerting**
  Pushes notifications to Slack or CRM platforms the moment a high-risk churn signal is detected.
- **Composio-Powered Integrations**
  Seamlessly connects Retently data with your existing CRM and communication toolsets for end-to-end automation.

---

## Use Cases
**Proactive Retention Outreach**
* Triggering automated email sequences to "detractor" segments immediately after a low NPS survey submission.
* Scheduling internal follow-up tasks in your CRM for account managers when sentiment trends downward.

**Account Health Monitoring**
* Generating weekly reports on account health status based on combined usage and sentiment data.
* Identifying "at-risk" patterns by correlating feedback frequency with product engagement metrics.

**Feedback Loop Optimization**
* Routing specific product-related feedback directly to the engineering backlog for rapid resolution.
* Categorizing customer complaints to identify recurring issues that impact long-term retention.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Churn Risk Detection Agent.
2. Click "Import" to load the workflow into your workspace.
3. Authenticate your Retently and CRM accounts via the Composio connection manager.
4. Ensure nodes are correctly mapped to your specific API endpoints and data fields.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger event or manual request for an account health check.
* **Agent**: Analyzes the sentiment data and determines the risk level of the account.
* **Composio Toolset**: Executes data retrieval from Retently and updates the CRM status.
* **Chat Output**: Delivers a summary of the risk assessment and recommended next steps.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Check the churn risk for account ID 98765 based on the latest NPS feedback.`
* `Summarize the sentiment trends for our top 10 enterprise accounts this month.`
* `Identify all customers who submitted a negative survey in the last 48 hours and create a follow-up task.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized analyst for customer sentiment and churn prediction.
* Instruction: Focus on identifying negative sentiment markers and urgency.
* Instruction: Maintain a professional, empathetic tone for all generated outreach suggestions.
* Instruction: Always prioritize high-value accounts when multiple churn signals are detected.

### 2) Composio Toolset Node
Requires a valid Retently API key and CRM (e.g., Salesforce or HubSpot) connection scope to read feedback and write task updates.

### 3) Tool Availability
* **Retently API**: Fetch survey results, NPS scores, and customer feedback logs.
* **CRM Connector**: Update account status, create tasks, and log activity notes.
* **Notification Service**: Send alerts to Slack or email for urgent churn risks.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Deep dive into account-level engagement signals.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track product usage metrics to complement sentiment data.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Manage and rank follow-up tasks generated by risk alerts.
