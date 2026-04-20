# YouTube Insight Agent (Uplizd) - Automated video intelligence and content performance analytics

## Summary
The YouTube Insight Agent is an intelligent workflow designed to extract, analyze, and synthesize actionable data from YouTube channels and video content. By leveraging the Composio Toolset to interface with YouTube’s data APIs, this solution enables creators and marketers to gain deep insights into audience engagement, content performance, and competitor strategies, transforming raw video metrics into a single source of truth for data-driven content planning.

---

## Demo
![YouTube Insight Agent dashboard showing video performance metrics and audience engagement trends](image.png)
**Alt text (SEO-ready):** YouTube Insight Agent dashboard displaying video performance metrics, audience engagement trends, and content analytics powered by Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5ab2d23e-e480-550f-8d32-446181859d50)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** youtube, content strategy, analytics, video marketing, competitor intelligence, composio, ai workflow, data insights
- This solution bridges the gap between raw video metadata and strategic content decision-making for marketing and creative teams.

---

## Who is this for?
This solution is designed for professionals who need to turn video metrics into a competitive advantage.

- **Content Strategist**
    - Identifies high-performing content pillars to inform future video production schedules.
- **Social Media Manager**
    - Monitors audience sentiment and engagement velocity to optimize posting times and interaction.
- **Growth Marketer**
    - Tracks competitor channel activity to uncover new market opportunities and trending topics.
- **YouTube Creator**
    - Automates the extraction of video performance data to streamline reporting and channel growth analysis.

---

## Features
- **Automated Data Extraction**
    - Seamlessly pulls video metadata, view counts, and engagement metrics using the Composio Toolset.
- **Competitor Intelligence**
    - Monitors and benchmarks competitor channel growth and content trends in real-time.
- **Sentiment & Engagement Analysis**
    - Processes comment sections and engagement ratios to gauge audience reaction to specific video topics.
- **Performance Reporting**
    - Generates summarized insights that highlight what is working and where content strategy needs adjustment.
- **Unified Workflow Integration**
    - Connects YouTube data directly into your existing AI-driven pipeline for immediate action and reporting.

---

## Use Cases
**Content Optimization**
- Analyze top-performing videos from the last 30 days to identify key themes and visual styles.
- Automatically generate summaries of audience feedback to refine scripts for upcoming video projects.

**Competitor Benchmarking**
- Track the release frequency and engagement rates of top industry competitors.
- Identify trending keywords and topics that competitors are successfully leveraging to capture market share.

**Channel Growth Analysis**
- Correlate video upload times with peak engagement periods to optimize your channel's publishing schedule.
- Monitor subscriber growth trends against specific content campaigns to measure overall brand impact.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the YouTube Insight Agent.
2. Click "Import" to add the workflow to your workspace.
3. Authenticate your YouTube account within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your analytical queries or channel URLs.
- **Agent**: Processes the request and determines which YouTube data tools to invoke.
- **Composio Toolset**: Executes API calls to fetch video, channel, or comment data.
- **Chat Output**: Delivers the synthesized insight report back to the user.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Analyze the last 5 videos on [Channel URL] and summarize the key engagement trends.`
- `What are the top 3 trending topics in my niche based on recent competitor video performance?`
- `Generate a report on audience sentiment for my latest video based on the top 50 comments.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting data and providing strategic recommendations.
- Instruct the agent to prioritize quantitative metrics over qualitative assumptions.
- Set the tone to be professional, data-driven, and actionable.
- Define specific output formats (e.g., bulleted lists or markdown tables) for easier reporting.

### 2) Composio Toolset Node
- Provide a valid YouTube API key within the Composio dashboard.
- Ensure the connection scope includes read-only access to public video and channel data.

### 3) Tool Availability
- **Video Metadata Fetcher**: Retrieves title, description, and publish date.
- **Engagement Metrics Tool**: Pulls view counts, likes, and comment statistics.
- **Channel Analytics Tool**: Aggregates subscriber growth and total channel performance.

---

## Related Solutions
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) - Deep dive into viewer demographics and behavior patterns.
- [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) - Focuses on SEO and metadata refinement for higher visibility.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) - Specialized tracking for competitive landscape analysis.
