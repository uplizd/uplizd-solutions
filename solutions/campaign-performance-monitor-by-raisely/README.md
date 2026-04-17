# Campaign Performance Monitor (Uplizd) - Automated fundraising metrics and campaign analytics

## Summary
The Campaign Performance Monitor is an automated AI workflow designed to track, analyze, and report on fundraising campaign metrics in real-time. By connecting directly to Raisely data, this solution provides non-profits and fundraising managers with a single source of truth for campaign velocity, donor engagement, and financial goal tracking, significantly reducing manual reporting time and improving data-driven decision-making.

---

## Demo
![Campaign Performance Monitor dashboard showing real-time fundraising metrics and automated report generation](../image.png)
**Alt text (SEO-ready):** Campaign performance monitor dashboard by Uplizd, showing real-time fundraising analytics, Raisely data integration, and automated reporting workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0f15ebf8-9a97-5375-ac44-43f19cb9b669)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** fundraising, raisely, campaign analytics, data sync, non-profit, reporting, composio, ai workflow  
This solution streamlines the monitoring of fundraising campaigns by automating the extraction and synthesis of performance data from Raisely.

---

## Who is this for?
This solution is designed for teams managing complex fundraising efforts who need to maintain high visibility into campaign health.

* **Fundraising Manager**
    * Gains immediate visibility into campaign progress against financial targets without manual data entry.
* **Non-profit Operations Lead**
    * Ensures consistent data hygiene across all active fundraising initiatives and donor outreach programs.
* **Marketing Coordinator**
    * Receives automated performance summaries to quickly pivot messaging based on real-time donation trends.
* **Data Analyst**
    * Automates the collection of raw campaign metrics, allowing for deeper focus on strategic donor insights.

---

## Features
- **Real-time Performance Tracking**
  Continuous monitoring of campaign donation totals and donor conversion rates via integrated API connections.
- **Automated Reporting Cycles**
  Scheduled or trigger-based generation of performance summaries, delivered directly to your preferred communication channel.
- **Raisely Data Integration**
  Seamless connectivity with Raisely platforms using the Composio Toolset to fetch accurate, up-to-date campaign records.
- **Goal Variance Alerts**
  Proactive notifications when campaign velocity deviates from established fundraising milestones or timelines.
- **Unified Data Synthesis**
  Consolidates fragmented campaign data into a single, readable format for stakeholders and executive review.

---

## Use Cases
**Campaign Health Monitoring**
* Tracking daily donation inflow against monthly fundraising targets.
* Identifying stalled campaigns that require immediate marketing intervention.

**Donor Engagement Analysis**
* Correlating specific campaign messaging with spikes in donor activity.
* Segmenting high-value donor contributions for targeted follow-up communications.

**Operational Reporting**
* Generating end-of-week performance summaries for board-level presentations.
* Automating the export of campaign metrics into centralized CRM or spreadsheet systems.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import Flow" option.
2. Upload the `campaign-performance-monitor` JSON configuration file.
3. Authenticate your Raisely credentials within the Composio connection settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives your natural language queries regarding campaign status or specific timeframes.
* **Agent**: Processes requests and determines which metrics to retrieve from the fundraising platform.
* **Composio Toolset**: Executes secure API calls to fetch real-time data from your Raisely account.
* **Chat Output**: Formats the retrieved data into a clear, actionable summary for the user.

### 3) Run the Flow
Access the Playground to test your workflow with these prompts:
* `Summarize the total donations raised across all active campaigns this week.`
* `Which fundraising campaign is currently furthest behind its financial goal?`
* `Generate a performance report for the 'Summer Gala' campaign including donor count and total revenue.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting fundraising data and summarizing it for the user.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are a fundraising data assistant. Always prioritize accuracy when reporting financial figures."
* Instruction: "If a campaign is underperforming, suggest a brief action item for the marketing team."

### 2) Composio Toolset Node
* Requires a valid Raisely API key stored within your Composio account.
* Ensure the connection scope includes read-access to `campaigns`, `donations`, and `profiles`.

### 3) Tool Availability
* **Raisely Fetcher**: Retrieves campaign metadata and donation logs.
* **Data Formatter**: Normalizes currency and date fields for consistent reporting.
* **Alert Trigger**: Evaluates performance against set thresholds to initiate notifications.

---

## Related Solutions
* [Affiliate Performance Monitor](../affiliate-performance-monitor-by-tapfiliate/README.md) — Track and optimize affiliate-driven revenue and program health.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Monitor account engagement and usage metrics for improved retention.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the operational efficiency and status of your automated business workflows.
