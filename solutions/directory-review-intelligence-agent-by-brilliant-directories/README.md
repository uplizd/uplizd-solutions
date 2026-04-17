# Directory Review Intelligence Agent (Uplizd) - Automated sentiment analysis and trend extraction for user feedback

## Summary
The Directory Review Intelligence Agent is an automated workflow designed to ingest, analyze, and synthesize user feedback from directory platforms. By leveraging the Composio Toolset to interface with review APIs, this solution transforms raw customer sentiment into actionable business intelligence, enabling teams to identify product trends, address service gaps, and maintain a high-quality brand reputation with minimal manual oversight.

---

## Demo
![Directory Review Intelligence Agent dashboard showing sentiment analysis and trend extraction](image.png)
**Alt text (SEO-ready):** Directory Review Intelligence Agent dashboard showing sentiment analysis, trend extraction, and automated review processing via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/444058cc-13d3-5750-bce7-ec56ac79dde4)

---

## Category
- **Primary category:** Customer Experience
- **Secondary tags:** review management, sentiment analysis, feedback loop, business intelligence, directory, reputation management, composio, ai workflow
- This solution bridges the gap between raw directory feedback and strategic operations by automating the classification and reporting of customer reviews.

---

## Who is this for?
This solution is designed for teams managing high-volume feedback across multiple digital directories.

- **Customer Success Manager**
    - Proactively identify and resolve recurring product issues before they escalate into churn.
- **Brand Reputation Manager**
    - Monitor sentiment trends across platforms to maintain a positive public image and address negative feedback instantly.
- **Product Manager**
    - Extract feature requests and usability insights directly from user reviews to inform the product roadmap.
- **Operations Analyst**
    - Automate the aggregation of qualitative data into structured reports for executive stakeholders.

---

## Features
- **Automated Review Ingestion**
    - Real-time monitoring and retrieval of new reviews from connected directory platforms using the Composio Toolset.
- **Sentiment Classification**
    - Advanced AI analysis to categorize feedback into positive, neutral, or negative buckets with intensity scoring.
- **Trend Extraction**
    - Automatically identifies recurring keywords and topics to highlight what users love or dislike most.
- **Actionable Alerting**
    - Triggers notifications for negative reviews or urgent customer issues requiring immediate human intervention.
- **Structured Data Export**
    - Formats analyzed feedback into clean, machine-readable data for integration with CRM or BI tools.

---

## Use Cases
**Reputation Management**
- Automatically flag reviews with a rating below 3 stars for immediate review by the support team.
- Generate weekly summaries of brand sentiment shifts across different directory channels.

**Product Development**
- Aggregate all mentions of specific feature requests to prioritize the upcoming sprint backlog.
- Identify common usability pain points mentioned in recent user feedback to guide UI/UX improvements.

**Customer Experience Optimization**
- Analyze the response time and sentiment of existing replies to ensure consistent brand voice.
- Correlate review volume spikes with recent marketing campaigns to measure real-world impact.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Connect your required directory API credentials within the Composio integration settings.
3. Configure your preferred LLM provider in the Agent node to handle the sentiment analysis logic.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger or manual request to scan for new reviews.
- **Agent**: Processes text, performs sentiment analysis, and identifies key themes.
- **Composio Toolset**: Executes API calls to fetch and filter directory data.
- **Chat Output**: Delivers the summarized report or alert to your preferred communication channel.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Analyze the latest 50 reviews from the directory and summarize the top 3 complaints.`
- `Identify any negative reviews from the last 24 hours that mention 'billing' or 'pricing'.`
- `Generate a sentiment trend report for this month compared to the previous month.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent requires a model capable of nuanced text analysis and structured output generation.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system prompt to prioritize objective sentiment classification.
- Ensure the output format is set to JSON for downstream integration compatibility.

### 2) Composio Toolset Node
- Provide your API keys for the specific directory platforms you wish to monitor.
- Set the connection scope to "Read-Only" for review retrieval to ensure data security.

### 3) Tool Availability
- **Review Fetcher**: Retrieves raw review text, timestamps, and user ratings.
- **Sentiment Analyzer**: Evaluates text for emotional tone and urgency.
- **Keyword Extractor**: Parses text for recurring product or service topics.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Aggregate account-level insights and signals for sales teams.
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Provide round-the-clock support automation for customer inquiries.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze video feedback and audience sentiment at scale.
