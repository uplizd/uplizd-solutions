# Campaign Health Auditor (Uplizd) - Automated Google Ads performance monitoring and optimization

## Summary
The Campaign Health Auditor is an intelligent Uplizd workflow designed to provide real-time visibility into Google Ads performance. By leveraging the Composio Toolset to interface directly with ad platforms, this solution identifies underperforming campaigns, detects budget inefficiencies, and generates actionable optimization recommendations, ensuring your marketing spend is always aligned with your growth objectives.

---

## Demo
![Campaign Health Auditor dashboard showing automated performance insights and budget optimization alerts](image.png)
**Alt text (SEO-ready):** Campaign Health Auditor Uplizd workflow for Google Ads performance monitoring, budget optimization, and automated marketing data analysis.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/564d4786-f633-5692-9beb-1079183cc38a)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** google ads, ppc, campaign optimization, marketing automation, data analysis, roi, composio, ai workflow
- This solution bridges the gap between raw ad performance data and strategic decision-making through automated auditing.

---

## Who is this for?
This solution is designed for marketing professionals and growth teams who need to maintain high-performing ad accounts without manual daily oversight.

- **Performance Marketers**
    - Automate the identification of high-cost, low-conversion keywords to improve overall ROAS.
- **Marketing Operations Managers**
    - Standardize campaign health reporting across multiple accounts to ensure consistent data hygiene.
- **Growth Leads**
    - Receive proactive alerts on budget pacing issues to prevent overspending or missed opportunity windows.
- **Agency Account Managers**
    - Scale client management by automating the audit process for dozens of active ad campaigns simultaneously.

---

## Features
- **Automated Performance Audits**
    - Continuous scanning of campaign metrics to flag anomalies in CTR, CPC, and conversion rates.
- **Budget Pacing Intelligence**
    - Real-time tracking of spend versus targets to ensure optimal budget distribution throughout the month.
- **Actionable Optimization Insights**
    - AI-generated recommendations for bid adjustments, negative keyword additions, and ad copy refinements.
- **Composio-Powered Integration**
    - Seamless connection to Google Ads APIs to pull live data and execute changes securely.
- **Custom Alerting Thresholds**
    - Configurable triggers that notify stakeholders only when specific performance KPIs deviate from the baseline.

---

## Use Cases
**Budget Efficiency**
- Identify campaigns that have exhausted their daily budget before noon to reallocate funds to top-performers.
- Detect "zombie" campaigns that are spending budget without generating meaningful clicks or conversions.

**Conversion Optimization**
- Analyze landing page performance metrics linked to specific ad groups to identify friction points in the user journey.
- Automatically flag ad groups with high impression volume but zero conversions for immediate review.

**Competitive Monitoring**
- Track changes in average CPC trends to identify when market competition is driving up acquisition costs.
- Audit ad quality scores to ensure your messaging remains relevant and cost-effective against industry benchmarks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Google Ads account via the Composio integration settings.
3. Configure your notification channels (e.g., Slack, Email, or CRM) to receive audit reports.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or scheduled interval for the audit.
- **Agent**: Processes performance data and applies logic to identify health issues.
- **Composio Toolset**: Executes API calls to fetch campaign metrics and push optimization updates.
- **Chat Output**: Delivers the final audit summary and recommended actions to the user.

### 3) Run the Flow
Use the Playground to test your audit logic with these prompts:
- `Run a full health audit on all active campaigns for the last 30 days.`
- `Identify the top 5 campaigns by spend and suggest budget reallocations.`
- `List all keywords with a CPC above $5.00 that have zero conversions this week.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your dedicated PPC analyst.
- Use a high-reasoning model (e.g., GPT-4o) for accurate data interpretation.
- Instruction: "You are an expert Google Ads analyst. Analyze the provided campaign data for anomalies, budget waste, and optimization opportunities."
- Instruction: "Prioritize recommendations that directly impact ROAS and conversion volume."

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable secure authentication with Google Ads.
- Set the connection scope to `read_only` for auditing or `read_write` if you intend to allow the agent to apply changes automatically.

### 3) Tool Availability
- **Google Ads Fetcher**: Retrieves campaign, ad group, and keyword performance data.
- **Budget Manager**: Monitors spend pacing and alerts on budget exhaustion.
- **Recommendation Engine**: Generates specific bid and keyword adjustment suggestions.

---

## Related Solutions
- [Ad Trend Tracking Agent](../ad-trend-tracking-agent-by-adyntel/README.md) - Monitor market-wide advertising trends and competitor shifts.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track overall account health and platform engagement metrics.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform marketing and sales workflows.
