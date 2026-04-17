# Proposal Analytics Agent (Uplizd) - Optimize win rates with automated proposal performance tracking

## Summary
The Proposal Analytics Agent streamlines the post-submission lifecycle by automatically monitoring proposal status, engagement metrics, and win-loss outcomes. By integrating directly with Bidsketch and your CRM, this Uplizd workflow eliminates manual data entry, provides real-time visibility into pipeline health, and empowers sales teams to focus on high-probability opportunities through data-driven insights.

---

## Demo
![Proposal Analytics Agent dashboard showing real-time proposal status, win rates, and engagement metrics tracked via Bidsketch and CRM integrations.](image.png)

**Alt text (SEO-ready):** Proposal Analytics Agent dashboard for Uplizd, tracking Bidsketch proposal performance, sales pipeline win rates, and automated CRM data synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAK+P///38GgAEEA0Y1Gg0jYBSMglEwCkbBKBgFo2AUjIJRMApGwSgYBaNgFGAEAAAM4w4B5t6u3gAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/3c4c4e8e-6a41-5d8d-ba25-5cbb129c4286)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** proposal management, bidsketch, crm, win rate, sales analytics, pipeline velocity, data integration, ai workflow
- This solution bridges the gap between document generation and revenue operations by automating the analysis of proposal performance data.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to turn proposal data into actionable sales intelligence.

- **Sales Operations Manager**
    - Automates the collection of win/loss data to refine sales forecasting and reporting accuracy.
- **Account Executive**
    - Receives real-time alerts on proposal engagement, allowing for timely follow-ups that increase conversion.
- **Revenue Analyst**
    - Identifies trends in proposal performance across different segments to optimize pricing and content strategy.
- **Sales Director**
    - Gains high-level visibility into pipeline health and team performance without manual spreadsheet updates.

---

## Features
- **Automated Status Tracking**
    - Syncs proposal states from Bidsketch to your CRM in real-time, ensuring the source of truth is always current.
- **Engagement Analytics**
    - Monitors client interaction with proposals to score lead interest and prioritize follow-up activities.
- **Win-Loss Intelligence**
    - Aggregates outcome data to provide automated reports on why proposals are won or lost.
- **Pipeline Velocity Insights**
    - Calculates the time taken from proposal delivery to signature, highlighting bottlenecks in the closing process.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely bridge Bidsketch data with major CRM platforms for seamless workflow execution.

---

## Use Cases
**Pipeline Optimization**
- Automatically update CRM deal stages based on Bidsketch proposal acceptance events.
- Flag stalled proposals that have been viewed multiple times but remain unsigned for over 48 hours.

**Performance Reporting**
- Generate weekly summaries of win rates segmented by proposal template or client industry.
- Identify top-performing proposal content that correlates with the highest contract values.

**Sales Follow-up Automation**
- Trigger Slack or email notifications to the assigned AE when a high-value proposal is opened.
- Create follow-up tasks in the CRM for proposals that have reached the "viewed" stage but lack a signature.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Proposal Analytics Agent template from the solution library.
3. Connect your Bidsketch and CRM accounts via the integration settings.
4. Ensure nodes are correctly mapped to your specific API credentials and environment variables.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled requests for proposal data analysis.
- **Agent**: Processes proposal metrics and performs logic-based scoring on deal health.
- **Composio Toolset**: Executes secure API calls to fetch Bidsketch data and update CRM records.
- **Chat Output**: Delivers actionable insights, performance summaries, and follow-up recommendations.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Analyze the win rate for all proposals sent in the last 30 days.`
- `List all proposals viewed by clients but not yet signed, sorted by deal value.`
- `Summarize the performance of the 'Enterprise Service Agreement' template for Q3.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a data analyst, interpreting raw proposal metrics into strategic sales advice.
- Focus on identifying patterns in client engagement and proposal outcomes.
- Maintain a professional, objective tone when summarizing win/loss data.
- Prioritize actionable recommendations for the sales team based on the provided data.

### 2) Composio Toolset Node
- Requires a valid API key with read/write access to your Bidsketch and CRM accounts.
- Scoping should be limited to the specific workspaces and objects required for proposal tracking.

### 3) Tool Availability
- **Bidsketch API**: Fetch proposal status, view counts, and signature timestamps.
- **CRM Connector**: Update deal stages, create tasks, and log activity notes.
- **Data Processor**: Perform aggregation and trend analysis on retrieved metrics.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregate lead data to improve account-based marketing efforts.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and follow-ups to accelerate deal velocity.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensure consistent data across your sales and marketing technology stack.
