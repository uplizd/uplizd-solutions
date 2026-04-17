# Multi-Account Email Marketing Dashboard (Uplizd) - Centralized campaign monitoring and cross-account analytics

## Summary
The Multi-Account Email Marketing Dashboard (Uplizd) provides a unified command center for managing complex email marketing operations across multiple Benchmark Email accounts. By leveraging AI-driven data aggregation, this workflow eliminates the need for manual platform switching, offering marketing teams a single source of truth for campaign performance, audience engagement, and deliverability metrics.

---

## Demo
![Multi-Account Email Marketing Dashboard interface showing cross-account campaign metrics and performance charts](image.png)
**Alt text (SEO-ready):** Multi-Account Email Marketing Dashboard by Uplizd featuring cross-account campaign analytics, Benchmark Email integration, and automated marketing performance reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/baae8c86-896e-5c49-959d-06dfe191d474)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, benchmark email, cross-account, analytics, campaign management, marketing automation, data integration, composio
- This solution streamlines multi-account marketing oversight by consolidating disparate email data into a single, actionable dashboard.

---

## Who is this for?
This solution is designed for marketing professionals managing high-volume email programs across multiple brands or regions.

- **Marketing Manager**
    - Gain immediate visibility into cross-account campaign performance without manual data exports.
- **Email Marketing Specialist**
    - Identify underperforming segments across different accounts to optimize send times and content.
- **Growth Marketer**
    - Track aggregate conversion rates and list growth trends across the entire portfolio.
- **Operations Lead**
    - Ensure consistent deliverability standards and hygiene practices across all managed email instances.

---

## Features
- **Unified Analytics Engine**
    - Aggregates real-time performance data from multiple Benchmark Email accounts into one centralized view.
- **Cross-Account Campaign Sync**
    - Automates the collection of open rates, click-through rates, and bounce metrics for comparative analysis.
- **Intelligent Alerting**
    - Monitors deliverability health and flags anomalies across accounts to prevent reputation decay.
- **Composio-Powered Integration**
    - Uses the Composio Toolset to securely interface with the Benchmark Email API for seamless data retrieval.
- **Automated Reporting**
    - Generates consolidated summary reports, allowing for rapid executive-level insights into marketing ROI.

---

## Use Cases
**Campaign Performance Monitoring**
- Compare open and click-through rates across different regional accounts to identify high-performing content templates.
- Track real-time engagement spikes during seasonal promotions across all active email lists.

**Deliverability & Hygiene Management**
- Monitor bounce rates and unsubscribe trends across multiple accounts to maintain sender reputation.
- Identify inactive segments across the portfolio that require re-engagement or suppression.

**Strategic Growth Analysis**
- Aggregate subscriber growth data to measure the effectiveness of lead acquisition strategies across different brands.
- Analyze long-term engagement trends to inform future email marketing budget allocation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import" option.
2. Paste the solution template URL or upload the provided JSON configuration file.
3. Map your Benchmark Email API credentials to the environment variables.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding specific campaign metrics or account performance.
- **Agent**: Processes natural language requests and orchestrates data retrieval via the toolset.
- **Composio Toolset**: Executes secure API calls to Benchmark Email to fetch requested data points.
- **Chat Output**: Formats and returns the consolidated analytics or performance insights to the user.

### 3) Run the Flow
Use the Playground to test your dashboard with these prompts:
- `Show me the total open rate across all my Benchmark Email accounts for the last 30 days.`
- `Compare the click-through performance of the latest newsletter campaign between the US and EU accounts.`
- `Identify which account has the highest bounce rate this week and provide a summary of the affected campaigns.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a marketing data analyst, translating complex API outputs into human-readable insights.
- Prioritize accuracy when reporting numerical campaign data.
- Maintain a professional, analytical tone for all marketing performance summaries.
- If data is missing for a specific account, clearly state the limitation rather than inferring values.

### 2) Composio Toolset Node
- **API Key**: Ensure your Benchmark Email API key is active and has read-access to your account reporting modules.
- **Connection Scope**: Limit the toolset to read-only permissions for analytics and campaign endpoints to ensure data security.

### 3) Tool Availability
- `benchmark_email_get_campaign_reports`: Fetches detailed metrics for specified campaigns.
- `benchmark_email_list_accounts`: Retrieves a list of all connected accounts for cross-account aggregation.
- `benchmark_email_get_subscriber_stats`: Pulls engagement and growth data for audience segments.

---

## Related Solutions
- [../abandoned-cart-recovery-agent-by-klaviyo/README.md](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automate recovery workflows for e-commerce stores.
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed intelligence reports on account activity.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize customer data across multiple platforms and CRM instances.
