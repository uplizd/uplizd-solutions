# Customer Health Monitor (Uplizd) - Proactive account retention and satisfaction tracking

## Summary
The Customer Health Monitor is an automated AI workflow designed to aggregate customer sentiment, usage metrics, and support interactions into a single source of truth. By leveraging real-time data from Gorgias and other integrated platforms, this solution enables support teams and account managers to identify at-risk accounts before churn occurs, significantly improving pipeline velocity and customer retention hygiene.

---

## Demo
![Customer Health Monitor workflow dashboard showing Gorgias support ticket trends and sentiment analysis](image.png)
**Alt text (SEO-ready):** Customer Health Monitor dashboard showing Gorgias support ticket trends, sentiment analysis, and at-risk account identification using Uplizd AI workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/57d6880d-75e5-57ba-a7fd-485ec6734582)

---

## Category
**Primary category:** Customer Support Operations  
**Secondary tags:** crm, gorgias, customer health, churn prevention, support automation, data sync, ai workflow, composio  
This solution bridges the gap between raw support tickets and actionable business intelligence to maintain high customer satisfaction standards.

---

## Who is this for?
This solution is designed for teams managing high-volume customer interactions who need to synthesize support data into actionable health scores.

*   **Customer Success Manager**
    *   Proactively identify accounts showing signs of frustration to intervene before churn.
*   **Support Operations Lead**
    *   Monitor ticket resolution efficiency and sentiment trends across the entire support organization.
*   **Account Executive**
    *   Receive automated alerts on key accounts to ensure renewal conversations are backed by data.
*   **RevOps Analyst**
    *   Sync support interaction data with CRM records to maintain a unified view of customer health.

---

## Features
- **Real-time Sentiment Analysis**
    Automatically parses incoming Gorgias tickets to detect negative sentiment patterns and urgency.
- **Automated Health Scoring**
    Calculates a dynamic health score based on ticket volume, resolution time, and customer feedback.
- **Proactive Alerting System**
    Triggers notifications to the relevant account owner when a customer's health score drops below a defined threshold.
- **Cross-Platform Data Sync**
    Uses the Composio Toolset to push support-derived insights directly into your primary CRM or communication tools.
- **Trend Reporting**
    Generates weekly summaries of support health, highlighting recurring issues that impact long-term retention.

---

## Use Cases
**Churn Prevention**
*   Identify high-value accounts with escalating ticket counts over a 7-day window.
*   Flag customers who have submitted multiple "urgent" or "complaint" tagged tickets in a single week.

**Support Efficiency**
*   Automate the categorization of support tickets to prioritize responses based on account health status.
*   Sync resolution time data to identify bottlenecks in the support pipeline that negatively impact satisfaction.

**Account Intelligence**
*   Aggregate qualitative feedback from Gorgias interactions to inform product roadmap and feature requests.
*   Provide account managers with a "Health Snapshot" prior to renewal meetings to ensure data-driven discussions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Health Monitor template from the solution library.
3. Connect your Gorgias and CRM credentials via the Composio Toolset.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual query for account health.
*   **Agent**: Processes ticket data, calculates sentiment, and evaluates account status.
*   **Composio Toolset**: Executes API calls to fetch Gorgias tickets and update CRM records.
*   **Chat Output**: Delivers the health summary and recommended actions to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
* `Check the health status of account [Company Name] based on recent Gorgias tickets.`
* `Identify all customers with a health score below 50 and list their top 3 pain points.`
* `Summarize the support sentiment for our enterprise tier customers over the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, synthesizing support data into actionable insights.
*   **Instruction Pattern:**
    *   Analyze sentiment using a 1-5 scale based on ticket tone and resolution history.
    *   Prioritize accounts based on their subscription tier and recent interaction frequency.
    *   Format output as a concise summary with clear "Next Action" recommendations.

### 2) Composio Toolset Node
Requires an active API key for Gorgias and your CRM. Ensure the connection scope includes read access to tickets and write access to CRM notes or custom fields.

### 3) Tool Availability
*   **Gorgias API:** Fetch tickets, update ticket status, and retrieve customer metadata.
*   **CRM Connector:** Update account health fields and log internal notes.
*   **Notification Service:** Send alerts via Slack or Email when health thresholds are breached.

---

## Related Solutions
* [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automate routine support inquiries and ticket triage.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track product usage metrics to supplement support data.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Enrich account profiles with external intent and firmographic data.
