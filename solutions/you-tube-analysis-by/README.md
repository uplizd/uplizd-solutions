# YouTube Analysis Agent (Uplizd) - Automated Video Insight and Sentiment Extraction

## Summary
The YouTube Analysis Agent (Uplizd) automates the extraction and interpretation of video metadata, transcripts, and audience engagement signals. By leveraging AI-driven sentiment analysis and content theme categorization, this workflow enables creators and marketers to transform raw video data into actionable intelligence, significantly reducing manual review time and improving content strategy velocity.

---

## Demo
![YouTube Analysis Agent workflow dashboard showing transcript extraction and sentiment analysis nodes](image.png)
**Alt text (SEO-ready):** YouTube Analysis Agent workflow dashboard showing transcript extraction, sentiment analysis, and audience engagement metrics using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1e5e7845-eaed-5855-a087-7b567057c87f)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** youtube, content strategy, sentiment analysis, video analytics, data extraction, ai workflow, audience insights, composio
- This solution bridges the gap between raw video engagement data and strategic content planning through automated AI analysis.

---

## Who is this for?
This solution is designed for professionals who need to derive rapid insights from video content at scale.

- **Content Strategist**
    - Identify high-performing content themes and audience sentiment trends to inform future video production.
- **Social Media Manager**
    - Automate the aggregation of viewer feedback and comments to improve community management response times.
- **Market Researcher**
    - Extract and synthesize competitor video transcripts to identify market gaps and trending industry topics.
- **Growth Marketer**
    - Analyze audience engagement signals to optimize video distribution and maximize organic reach.

---

## Features
- **Automated Transcript Extraction**
    - Seamlessly pull full video transcripts using the Composio Toolset to enable deep-text analysis without manual transcription.
- **Sentiment Pattern Recognition**
    - Utilize advanced LLM processing to categorize viewer comments into positive, neutral, or negative sentiment clusters.
- **Content Theme Categorization**
    - Automatically tag video segments and comments based on recurring topics, keywords, and audience pain points.
- **Real-time Engagement Monitoring**
    - Sync video performance metrics directly into your workflow to track how sentiment shifts over time.
- **Actionable Insight Generation**
    - Transform raw data into structured summaries that highlight key takeaways and recommended content improvements.

---

## Use Cases
**Content Performance Optimization**
- Analyze viewer drop-off points by correlating transcript themes with engagement timestamps.
- Generate monthly performance reports that summarize audience sentiment across your entire video library.

**Competitor Intelligence Gathering**
- Monitor competitor channels to extract and summarize key arguments or product mentions from long-form video content.
- Identify recurring questions in competitor comment sections to fuel your own FAQ-style content strategy.

**Community Engagement Management**
- Automatically flag negative sentiment or urgent customer support queries within video comments for immediate human review.
- Aggregate common viewer requests to prioritize future video topics that align with audience demand.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your YouTube API credentials within the Composio integration settings.
3. Configure your preferred LLM model in the Agent node to handle the analysis logic.
4. Ensure nodes are correctly mapped: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the YouTube video URL or channel ID to begin the analysis process.
- **Agent**: Orchestrates the logic, deciding when to fetch transcripts or analyze comment sentiment.
- **Composio Toolset**: Executes the API calls to retrieve video data and metadata from YouTube.
- **Chat Output**: Delivers the final structured analysis, sentiment report, or content recommendations.

### 3) Run the Flow
Use the Playground to test your analysis:
- `Analyze the sentiment of the top 50 comments for this video: [URL]`
- `Extract the main themes and key talking points from this video transcript: [URL]`
- `Compare the audience sentiment of these two videos: [URL1] and [URL2]`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting the data retrieved by the Composio Toolset.
- Use a model with high context window capacity for processing long transcripts.
- Instruct the agent to prioritize specific sentiment metrics relevant to your brand.
- Configure the agent to output findings in a structured format (e.g., JSON or Markdown tables).

### 2) Composio Toolset Node
- Provide your YouTube API Key within the Composio dashboard to authorize data retrieval.
- Ensure the connection scope includes read-only access to video metadata, transcripts, and comments.

### 3) Tool Availability
- **YouTube Data API**: For fetching video details, descriptions, and channel statistics.
- **YouTube Transcript API**: For extracting time-coded text content from videos.
- **Sentiment Analysis Tool**: For processing text strings and returning emotional polarity scores.

---

## Related Solutions
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Identify and segment your target audience based on video interaction data.
- [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) — Improve video reach and engagement through data-driven content adjustments.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) — Track and analyze competitor strategies to refine your own content roadmap.
