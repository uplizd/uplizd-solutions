# Instagram Performance Analyst (Uplizd) - Automated social media insights and engagement tracking

## Summary
The Instagram Performance Analyst is an intelligent Uplizd workflow designed to automate the collection, analysis, and reporting of social media metrics. By connecting directly to your Instagram professional account, this agent eliminates manual data entry, providing marketing teams and content creators with a single source of truth for engagement rates, follower growth, and post performance to drive data-backed content strategies.

---

## Demo
![Instagram Performance Analyst dashboard showing engagement metrics and growth trends](image.png)
**Alt text (SEO-ready):** Instagram Performance Analyst dashboard showing engagement metrics, follower growth trends, and automated social media reporting via Uplizd workflow and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/253548f9-2b62-5f60-bc80-70f6f99880fc)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** instagram, social media, analytics, engagement, content strategy, data sync, composio, ai workflow
- This solution bridges the gap between raw social media data and actionable marketing intelligence through automated performance tracking.

---

## Who is this for?
This workflow is built for professionals who need to turn social media data into growth opportunities without spending hours in manual spreadsheets.

- **Social Media Manager**
    - Automate weekly performance reports and identify top-performing content formats.
- **Digital Marketing Lead**
    - Monitor campaign ROI across multiple channels with real-time Instagram data integration.
- **Content Creator**
    - Gain deep insights into audience behavior to optimize posting schedules and engagement.
- **Growth Marketer**
    - Track follower growth trends and correlate engagement spikes with specific marketing initiatives.

---

## Features
- **Automated Data Retrieval**
    - Seamlessly pulls post-level metrics including likes, comments, and reach using the Composio Toolset.
- **Engagement Trend Analysis**
    - Identifies patterns in audience interaction to determine the most effective content themes.
- **Real-Time Performance Alerts**
    - Triggers notifications when engagement rates deviate from historical benchmarks.
- **Cross-Platform Synchronization**
    - Syncs Instagram insights with external databases or CRM tools for unified marketing analytics.
- **Custom Reporting Engine**
    - Generates summarized performance insights in natural language, ready for stakeholder review.

---

## Use Cases
**Content Strategy Optimization**
- Analyze which media types (Reels vs. Carousels) drive the highest engagement for specific audience segments.
- Automatically identify the best times to post based on historical interaction data from the last 30 days.

**Campaign Performance Tracking**
- Monitor the reach and conversion potential of influencer collaborations or sponsored posts.
- Aggregate performance data from multiple campaigns to calculate total engagement lift.

**Audience Growth Monitoring**
- Track daily follower acquisition rates to measure the impact of viral content or paid promotions.
- Detect sudden drops in engagement to proactively adjust content tactics before performance declines.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd template library and select the Instagram Performance Analyst.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your Instagram account via the Composio connection prompt.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your analytical queries or reporting triggers.
- **Agent**: Processes data requests and interprets Instagram performance metrics.
- **Composio Toolset**: Executes API calls to fetch real-time social media data.
- **Chat Output**: Delivers the final analysis or report directly to your dashboard.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Analyze my top 5 performing posts from the last month and explain why they succeeded.`
- `Generate a weekly performance summary focusing on follower growth and engagement rate.`
- `Compare the reach of my recent Reels against static image posts.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized data analyst.
- Use a model capable of high-reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize quantitative accuracy in metric reporting.
- Configure the system prompt to maintain a professional, analytical tone.

### 2) Composio Toolset Node
- Provide your Instagram API credentials within the Composio dashboard.
- Ensure the connection scope includes read-only access to `instagram_basic` and `instagram_manage_insights`.

### 3) Tool Availability
- **Insights Fetcher**: Retrieves reach, impressions, and profile visits.
- **Media Analyzer**: Extracts engagement counts for individual posts.
- **Audience Tracker**: Monitors follower count fluctuations over time.

---

## Related Solutions
- [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) — Automate video analytics and audience growth tracking.
- [Affiliate Performance Monitor](../affiliate-performance-monitor-by-tapfiliate/README.md) — Track and optimize affiliate marketing campaign results.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather and report on account-level engagement data.
