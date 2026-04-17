# Campaign Performance Tracker (Uplizd) - Real-time marketing link analytics and reporting

## Summary
The Campaign Performance Tracker is an automated Uplizd AI workflow designed to bridge the gap between Short.io link data and marketing performance reporting. By continuously monitoring click-through rates and geographical engagement, this solution provides marketing teams with a single source of truth for campaign effectiveness, eliminating manual data entry and ensuring pipeline velocity through timely, data-driven insights.

---

## Demo
![Campaign Performance Tracker dashboard showing real-time link click analytics and geographic distribution](image.png)
**Alt text (SEO-ready):** Campaign Performance Tracker dashboard showing real-time link click analytics, geographic distribution, and marketing automation insights via Uplizd and Short.io.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e915a26e-7f4c-5bbd-9203-a9f1e27a2b88)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** marketing, analytics, short.io, link tracking, campaign performance, data integration, automation, roi
- This solution streamlines marketing operations by automating the retrieval and analysis of link performance metrics from Short.io.

---

## Who is this for?
This solution is built for marketing and growth professionals who need to maintain high-visibility campaign tracking without manual spreadsheet maintenance.

- **Marketing Manager**
    - Automates daily performance reporting to stakeholders without manual data extraction.
- **Growth Marketer**
    - Identifies high-performing channels in real-time to optimize ad spend allocation.
- **Content Strategist**
    - Tracks engagement across distributed content pieces to refine future messaging.
- **RevOps Specialist**
    - Ensures accurate attribution data flows from link clicks into broader pipeline reporting.

---

## Features
- **Real-time Link Monitoring**
    - Automatically fetches click counts and referral sources from Short.io to provide up-to-the-minute campaign visibility.
- **Geographic Insight Mapping**
    - Analyzes click locations to help teams understand the regional reach and impact of their global marketing efforts.
- **Automated Performance Summaries**
    - Uses the Agent node to synthesize raw link data into actionable natural language reports for team communication.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely connect with Short.io APIs, ensuring reliable and authenticated data retrieval.
- **Pipeline Velocity Optimization**
    - Reduces the time spent on manual data hygiene, allowing teams to pivot strategies faster based on actual performance.

---

## Use Cases
**Campaign Optimization**
- Identify underperforming links within 24 hours of launch to reallocate budget to high-converting channels.
- Compare click-through rates across different social media platforms to determine the most effective distribution strategy.

**Reporting & Attribution**
- Generate weekly performance summaries for executive stakeholders with zero manual intervention.
- Map link engagement data to specific marketing initiatives to improve ROI calculation accuracy.

**Audience Intelligence**
- Analyze regional click patterns to tailor localized content for specific geographic markets.
- Detect spikes in traffic to specific landing pages to trigger follow-up lead nurturing workflows.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your Short.io account via the Composio integration settings.
3. Configure the **Chat Input** to accept your campaign ID or link alias.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the specific campaign link or ID you wish to analyze.
- **Agent**: Processes the request, interprets the performance data, and generates a summary.
- **Composio Toolset**: Executes secure API calls to Short.io to fetch the latest click metrics.
- **Chat Output**: Delivers the formatted performance report directly to your dashboard or Slack.

### 3) Run the Flow
Use the Playground to test your tracking:
- `Fetch the total click count and top referral sources for the 'summer-sale-2024' campaign.`
- `Analyze the geographic distribution of clicks for my latest product launch link.`
- `Compare the performance of the last three marketing campaigns and summarize the findings.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your dedicated marketing analyst.
- Use a model capable of structured data interpretation (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a marketing analyst. Retrieve data via the Composio Toolset, identify trends, and provide a concise summary."
- Instruction: "Highlight any significant anomalies in click volume or geographic distribution."

### 2) Composio Toolset Node
- Provide your Short.io API key within the Composio dashboard.
- Set the connection scope to read-only access for link analytics to ensure data security.

### 3) Tool Availability
- `shortio_get_link_stats`: Retrieves click counts and metadata for specific links.
- `shortio_list_campaigns`: Lists active campaigns for bulk performance review.
- `shortio_get_geographic_data`: Extracts location-based engagement metrics.

---

## Related Solutions
- [Affiliate Link Performance Tracker](../affiliate-link-performance-tracker-by-cutt-ly/README.md) - Monitor and optimize affiliate marketing link engagement.
- [AB Test Performance Analyzer](../ab-test-performance-analyzer-by-microsoft-clarity/README.md) - Analyze A/B test results to improve conversion rates.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather and report on account-level engagement data.
