# Customer Insights Generator (Uplizd) - Automated customer intelligence and behavioral analysis

## Summary
The Customer Insights Generator is an intelligent Uplizd workflow designed to aggregate, process, and synthesize customer data into actionable business intelligence. By leveraging the Composio Toolset to connect with your existing CRM and support platforms, this solution identifies hidden patterns, sentiment trends, and behavioral preferences, providing a single source of truth for product and marketing teams to improve pipeline velocity and customer retention.

---

## Demo
![Customer Insights Generator workflow dashboard showing data ingestion, sentiment analysis, and insight reporting](image.png)
**Alt text (SEO-ready):** Customer Insights Generator Uplizd workflow dashboard showing data ingestion, sentiment analysis, and insight reporting for CRM and support data.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/847e6791-de2d-594b-bbfc-acf558c2f522)

---

## Category
**Primary category:** CRM data
**Secondary tags:** customer insights, data analytics, sentiment analysis, business intelligence, crm, composio, ai workflow, data hygiene.
This solution transforms raw customer interactions into structured intelligence, enabling data-driven decision-making across your organization.

---

## Who is this for?
This solution is designed for teams looking to bridge the gap between raw customer data and strategic action.

- **Product Manager**
    - Identifies feature requests and pain points directly from customer support tickets.
- **Marketing Operations**
    - Segments audiences based on behavioral patterns and sentiment scores.
- **Customer Success Lead**
    - Detects churn signals early by monitoring shifts in customer engagement.
- **Sales Operations**
    - Uncovers upsell opportunities by analyzing historical interaction data.

---

## Features
- **Automated Data Aggregation**
    - Seamlessly pulls interaction data from multiple CRM and support platforms using the Composio Toolset.
- **Sentiment & Intent Analysis**
    - Uses advanced LLM reasoning to categorize customer feedback into actionable intent groups.
- **Real-time Insight Synthesis**
    - Generates concise, executive-level summaries of customer health and product feedback.
- **Cross-Platform Correlation**
    - Connects disparate data points to provide a unified view of the customer journey.
- **Actionable Reporting**
    - Automatically formats insights into ready-to-share reports for internal stakeholders.

---

## Use Cases
**Customer Feedback Analysis**
- Aggregating recurring feature requests from support tickets to inform the product roadmap.
- Identifying common friction points in the user onboarding process to reduce churn.

**Sales Intelligence**
- Scoring leads based on sentiment and engagement levels to prioritize high-value accounts.
- Detecting buying signals in communication history to trigger timely outreach.

**Operational Reporting**
- Creating weekly summaries of customer satisfaction trends across different regions.
- Automating the cleanup of fragmented customer profiles to ensure data hygiene.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Customer Insights Generator.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your CRM and support platform connections via the Composio dashboard.
4. Ensure nodes are correctly mapped from Chat Input to Agent, Toolset, and Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the query or trigger for data analysis.
*   **Agent**: Processes the raw data using defined instructions to extract insights.
*   **Composio Toolset**: Executes API calls to fetch and update customer records.
*   **Chat Output**: Delivers the synthesized report or insight summary.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Analyze the last 30 days of support tickets and summarize the top 3 recurring product issues.`
- `Identify high-value accounts that have shown negative sentiment in recent interactions.`
- `Generate a report on customer engagement trends for the Q3 marketing campaign.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets customer data.
- **Instruction Pattern:**
    - Focus on extracting objective sentiment and actionable intent.
    - Maintain consistency in output formatting for downstream reporting.
    - Prioritize data privacy by anonymizing sensitive customer information.

### 2) Composio Toolset Node
- Requires an active API key with read/write access to your CRM and support platforms.
- Connection scope should be limited to the specific data objects required for analysis (e.g., Tickets, Contacts, Deals).

### 3) Tool Availability
- **CRM Connector**: Fetching contact and deal history.
- **Support API**: Retrieving ticket metadata and customer feedback.
- **Data Processor**: Formatting and cleaning raw text for analysis.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting for account-level intelligence.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizing customer data across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Managing sales stages and opportunity follow-ups.
