# Customer Behavior Analyzer (Uplizd) - Transform Loyverse transaction data into actionable customer insights

## Summary
The Customer Behavior Analyzer is an intelligent Uplizd workflow that bridges the gap between raw point-of-sale data and strategic decision-making. By leveraging the Composio Toolset to interface with Loyverse, this solution automatically processes transaction histories, identifies purchasing patterns, and segments customers based on their behavior, enabling businesses to increase retention and optimize inventory velocity through data-driven precision.

---

## Demo
![Customer Behavior Analyzer workflow diagram showing data flow from Loyverse to the AI Agent for segmentation and insight generation](image.png)
**Alt text (SEO-ready):** Customer Behavior Analyzer workflow diagram showing data flow from Loyverse to the AI Agent for segmentation and insight generation, powered by Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d3647fc8-80ed-5299-b8d6-5ff212db3bb7)

---

## Category
- **Primary category:** Customer Analytics
- **Secondary tags:** loyverse, pos, customer insights, behavioral analysis, data sync, retail operations, composio, ai workflow
- This solution empowers retail managers to turn fragmented point-of-sale transactions into a unified source of truth for customer engagement strategies.

---

## Who is this for?
This solution is designed for retail and hospitality professionals who need to move beyond basic reporting to predictive customer understanding.

- **Store Manager**
    - Identifies top-performing products and peak shopping hours to optimize staff scheduling.
- **Marketing Lead**
    - Creates hyper-personalized loyalty campaigns based on actual purchase frequency and recency.
- **Inventory Planner**
    - Predicts stock requirements by analyzing seasonal buying trends and customer preferences.
- **Business Owner**
    - Gains a high-level view of customer lifetime value and churn risk to inform long-term growth.

---

## Features
- **Automated Data Extraction**
    - Seamlessly pulls transaction logs and customer profiles from Loyverse via the Composio Toolset.
- **Behavioral Segmentation**
    - Automatically categorizes customers into cohorts based on spending habits, visit frequency, and average order value.
- **Trend Identification**
    - Detects shifts in buying patterns in real-time, highlighting emerging product favorites or declining interest.
- **Actionable Insight Generation**
    - Translates complex data sets into plain-language summaries and recommended marketing actions.
- **Unified Reporting**
    - Consolidates disparate POS data into a single, readable format for immediate stakeholder review.

---

## Use Cases
**Customer Retention Strategies**
- Identify "at-risk" customers who haven't visited in 30+ days for targeted win-back email campaigns.
- Reward high-value "VIP" customers with exclusive offers based on their total lifetime spend.

**Operational Efficiency**
- Analyze peak transaction times to adjust store opening hours or staffing levels accordingly.
- Correlate product bundles with high-frequency shoppers to optimize store layout and cross-selling.

**Inventory & Sales Optimization**
- Track the performance of new product launches against historical customer purchase data.
- Forecast demand for seasonal items by comparing current behavior with year-over-year transaction trends.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your Loyverse account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language queries regarding customer data.
- **Agent**: Processes the request, interprets the data, and formulates strategic insights.
- **Composio Toolset**: Executes secure API calls to fetch and filter Loyverse transaction records.
- **Chat Output**: Delivers the final analysis, segmented reports, or actionable recommendations.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Analyze the top 50 customers by spend from the last quarter and suggest a loyalty reward.`
- `Which product categories are trending downward in purchase frequency this month?`
- `Identify customers who have not visited in 60 days and draft a personalized re-engagement message.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your data analyst, summarizing complex POS data into business-ready insights.
- **Instruction Pattern**: "You are an expert retail analyst. Use the provided Composio tools to fetch Loyverse data."
- **Instruction Pattern**: "Analyze the retrieved transaction history to identify behavioral trends and segments."
- **Instruction Pattern**: "Provide clear, concise recommendations that a store manager can implement immediately."

### 2) Composio Toolset Node
- **API Key**: Ensure your Loyverse API key is active within the Composio dashboard.
- **Connection Scope**: Grant read-only access to `customers`, `transactions`, and `inventory` endpoints for secure operation.

### 3) Tool Availability
- `loyverse_get_customers`: Retrieves detailed customer profiles and contact info.
- `loyverse_list_transactions`: Fetches historical sales data for specified date ranges.
- `loyverse_get_inventory`: Provides current stock levels to correlate with sales velocity.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich customer profiles with firmographic data.
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automate follow-ups for unclosed sales opportunities.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track customer engagement metrics to prevent churn.
