# Cohort Performance Tracker (Uplizd) - Automated retention insights and user behavior analytics

## Summary
The Cohort Performance Tracker (Uplizd) is an automated AI workflow designed to streamline user retention analysis and behavioral trend identification. By integrating directly with Mixpanel, this solution enables product managers and data analysts to maintain a single source of truth for cohort health, automate the extraction of retention metrics, and improve pipeline velocity by surfacing actionable insights from complex user event data.

---

## Demo
![Cohort Performance Tracker dashboard showing retention curves and user cohort breakdown](image.png)
**Alt text (SEO-ready):** Cohort Performance Tracker dashboard showing retention curves and user cohort breakdown for Uplizd AI workflow and Mixpanel data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAK+A81/w8EwP8fA/8/fPj/Pwb+f/j//z8G/n9A8v8/Bv5/GPj/wYgBwP8fA/8/fPj/PwAAL0Y/m0u63+cAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/f76440f1-ca40-57e8-8f5f-c40f3a45865b)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** mixpanel, cohort analysis, retention, product analytics, data sync, user behavior, ai workflow, composio
- This solution bridges the gap between raw event data in Mixpanel and strategic product decision-making through automated reporting.

---

## Who is this for?
This solution is designed for data-driven teams looking to optimize product-market fit and user lifecycle management.

- **Product Manager**
    - Identifies feature adoption bottlenecks and churn triggers across specific user cohorts.
- **Data Analyst**
    - Automates the extraction of complex retention metrics, saving hours of manual query time.
- **Growth Marketer**
    - Monitors the performance of acquisition channels by tracking long-term user engagement.
- **Customer Success Lead**
    - Pinpoints at-risk accounts based on declining usage patterns within their cohort.

---

## Features
- **Automated Cohort Extraction**
    - Seamlessly pulls user event data from Mixpanel to generate real-time cohort performance reports.
- **Retention Trend Analysis**
    - Automatically calculates day-N retention rates to visualize user stickiness over time.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely authenticate and query Mixpanel APIs without manual coding.
- **Actionable Insight Generation**
    - Uses advanced LLM reasoning to summarize performance data into clear, executive-ready summaries.
- **Real-Time Data Sync**
    - Ensures your analytics dashboard reflects the latest user interactions for immediate decision-making.

---

## Use Cases
**Product Lifecycle Optimization**
- Analyze the impact of new feature releases on user retention rates within the first 30 days.
- Compare cohort behavior between free-trial users and paid subscribers to identify conversion drivers.

**Customer Health Monitoring**
- Detect sudden drops in engagement for specific segments to trigger proactive outreach.
- Track long-term value of cohorts acquired through different marketing campaigns.

**Data-Driven Reporting**
- Generate weekly performance summaries for stakeholders without manual spreadsheet manipulation.
- Automate the identification of "power user" behaviors to inform future product development.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Cohort Performance Tracker template JSON file.
3. Connect your Mixpanel API credentials via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language request for specific cohort data.
- **Agent**: Processes the intent and determines the necessary Mixpanel API calls.
- **Composio Toolset**: Executes the data retrieval and filtering operations.
- **Chat Output**: Delivers the formatted analysis and actionable insights to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Analyze the retention rate for the cohort that signed up in January 2024.`
- `Compare the 30-day retention of users who used the 'Export' feature vs those who did not.`
- `Summarize the top 3 trends in user engagement for our most recent cohort.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized data analyst capable of interpreting product metrics.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on how to interpret retention percentages and cohort sizes.
- Ensure the agent is instructed to cite specific data points from the Mixpanel response.

### 2) Composio Toolset Node
- Provide your Mixpanel API Key and Project ID.
- Ensure the connection scope includes read-only access to event and cohort data.

### 3) Tool Availability
- **Mixpanel Query Tool**: Fetches raw event data and calculated retention metrics.
- **Data Formatter**: Converts JSON API responses into readable tables or summaries.
- **Trend Analyzer**: Identifies statistical significance in cohort performance shifts.

---

## Related Solutions
- [AB Test Optimizer](../ab-test-optimizer-by-mixpanel/README.md) - Optimize your product experiments using Mixpanel data.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track user activity and account health metrics.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize user data across your CRM and analytics platforms.
