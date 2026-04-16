
# Content Research Assistant (Uplizd) - Automate Trending Topics & Competitor Analysis

## Summary
The Content Research Assistant is an advanced Uplizd agent designed for content marketers, social media managers, and SEO specialists. It automates the tedious process of monitoring multiple platforms (Reddit, Twitter, blogs) and competitor websites, transforming raw web data into actionable content ideas and performance insights. By utilizing scheduled scraping and real-time alerting, it ensures your content strategy is always aligned with emerging trends and competitor gaps.

---

## Demo

![Content Research Assistant workflow showing Apify integration for automated scraping and trend analysis](../image.png)

**Alt text:** Uplizd Content Research Assistant workflow illustrating an AI agent utilizing Apify tools to monitor platforms, store dataset results, and generate content strategy reports.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e91b52bc-dbe5-4af2-87b3-bdd50516717f)

---
## Who is this for?
Designed for creators and marketers who need to stay ahead of the digital curve:

- **Social Media Managers**
    - Identify viral hashtags and trending discussions before they peak.

- **Content Marketers**
    - Discover "content gaps" in competitor strategies to create high-value, unique assets.

- **SEO Specialists**
    - Monitor industry blogs and competitor domains for new keyword opportunities.

- **Brand Strategists**
    - Track sentiment and engagement levels across niche communities (e.g., specific subreddits).

---

## Features

- **Automated Platform Monitoring**  
  Deploys specialized scrapers for Reddit, Twitter, industry blogs, and competitor domains to capture discussions and new publications.

- **Structured Content Datasets**  
  Establishes organized storage for different content streams, capturing essential metrics like engagement rates, publication timing, and headlines.

- **Real-Time Strategy Alerting**  
  Configures webhooks to notify you immediately when content in your niche exceeds engagement thresholds or when competitors publish new material.

- **Competitor Performance Analysis**  
  Retrieves historical data to identify which formats and topics are performing best for competitors, allowing for data-driven brainstorming.

- **Weekly Insight Reports**  
  Synthesizes collected data into reports featuring ranked content ideas, audience sentiment analysis, and recommended creation priorities.

---

## Use Cases

- **Trending Topic Discovery**
  - "Find the top 10 most discussed topics in r/marketing over the last 24 hours with engagement scores."

- **Competitor Content Audit**
  - "Monitor [Competitor URL] and alert me whenever they publish a new case study or long-form guide."

- **Engagement Benchmarking**
  - "Track engagement rates for specific hashtags across industry news sites to prioritize our next LinkedIn post."

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all nodes are connected correctly:
   - **Chat Input**
   - **Agent**
   - **Apify - APIFY_CREATE_ACTOR**
   - **Apify - APIFY_CREATE_DATASET**
   - **Apify - APIFY_GET_DATASET_ITEMS**
   - **Apify - APIFY_CREATE_TASK_WEBHOOK**
   - **Chat Output**

### 2) Setup the Nodes
Verify the core configuration:

- **Apify Nodes** → Orchestrated via Composio to handle the heavy lifting of web scraping and data storage.
- **Agent** → Instructed with the "Content Research Assistant" workflow to synthesize raw data into insights.
- **Chat Output** → Displays the final content ideas and reports.

### 3) Run the Flow
1. Click **Playground**.
2. Start your research query:
   - *"Set up a monitor for the top AI subreddits and alert me of engagement spikes."*
   - *"Analyze the recent content strategy of [Competitor Name] and suggest 5 article ideas."*
   - *"Give me a summary of trending hashtags in the sustainable fashion niche."*

---

## Configuration

### 1) Language Model (Agent Node)
Optimized for creative synthesis and data analysis.

Recommended settings:
- **Model**: GPT-4o or Claude-3.5-Sonnet (excellent for identifying qualitative patterns).
- **System Prompt**: Built-in instructions for Platform Monitoring → Data Organization → Alerting → Analysis.

### 2) Apify Connection
Requires an **Apify API Key** (managed via Composio). Ensure your Apify account has sufficient resource credits for the scraping frequency you define.

### 3) Tool Availability (Apify Actions)
The agent utilizes these specific actions via Composio:
- **APIFY_CREATE_ACTOR**: The engine for targeted platform scraping.
- **APIFY_CREATE_DATASET**: Ensures all research results are stored in a queryable format.
- **APIFY_GET_DATASET_ITEMS**: Allows the agent to read and analyze historical performance.
- **APIFY_CREATE_TASK_WEBHOOK**: Enables automated real-time alerts for trending content and competitor updates.

---

## Related Solutions

* **[Market Research Assistant](../market-research-assistant/README.md)**  
  Deep-dive into firmographics, funding status, and detailed profiling of competitor companies.

* **[Research Insight Synthesizer](../research-insight-synthesizer/README.md)**  
  Synthesize qualitative findings from the web and community discussions into strategic reports.

* **[Professional Email Clarity Assistant](../professional-email-clarity-assistant/README.md)**  
  Reach out to influencers or partners identified during your content research with clarity.

* **[Contact Sync Manager](../contact-sync-manager/README.md)**  
  Save and sync your enriched content data and contacts directly into your marketing stack.
