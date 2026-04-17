# Competitor Intelligence Agent (Uplizd) - Automated HackerNews market monitoring and trend analysis

## Summary
The Competitor Intelligence Agent leverages the Composio Toolset to monitor HackerNews for real-time mentions of your competitors and industry keywords. By automating the extraction and analysis of community sentiment, this workflow provides RevOps and Marketing teams with a single source of truth for market positioning, enabling faster responses to emerging industry trends and potential threats.

---

## Demo
![Competitor Intelligence Agent dashboard showing real-time HackerNews sentiment analysis and competitor mention alerts](image.png)
**Alt text (SEO-ready):** Competitor Intelligence Agent dashboard showing real-time HackerNews sentiment analysis and competitor mention alerts on the Uplizd AI workflow platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7e6c69d3-3289-5b3e-962b-e9e25ffb9306)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** competitor analysis, hackernews, sentiment analysis, market research, trend tracking, ai workflow, composio, business intelligence
- This solution bridges the gap between raw community discussions and actionable market insights through automated data extraction.

---

## Who is this for?
This agent is designed for teams that need to stay ahead of the curve in fast-moving technical markets.

- **Product Manager**
    - Identify feature gaps and user pain points mentioned by the community to inform the product roadmap.
- **Marketing Strategist**
    - Monitor brand sentiment and competitor positioning to refine messaging and campaign strategy.
- **Sales Operations Lead**
    - Gain early warning signals on competitor activity to better equip the sales team with battle cards.
- **Growth Marketer**
    - Discover trending topics and industry discussions to capitalize on viral content opportunities.

---

## Features
- **Real-time Monitoring**
    - Automatically scans HackerNews threads for specific competitor names and industry-relevant keywords.
- **Sentiment Analysis**
    - Uses advanced LLM processing to categorize community feedback as positive, negative, or neutral.
- **Automated Summarization**
    - Converts long, complex discussion threads into concise, actionable executive summaries.
- **Composio Integration**
    - Seamlessly connects to external tools to pipe intelligence directly into your CRM or communication channels.
- **Custom Alerting**
    - Configurable thresholds to notify your team immediately when a competitor reaches a specific mention volume.

---

## Use Cases
**Market Positioning**
- Track how users compare your product features against competitors in real-time discussions.
- Identify shifts in industry sentiment regarding specific technologies or market trends.

**Competitive Intelligence**
- Receive instant alerts when a competitor launches a new product or receives significant community feedback.
- Analyze the "why" behind negative sentiment directed at competitors to identify your own unique value propositions.

**Product Development**
- Aggregate recurring feature requests from community threads to prioritize your development backlog.
- Monitor discussions around industry-wide technical challenges to identify opportunities for new service offerings.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Competitor Intelligence Agent template from the marketplace.
3. Authenticate your HackerNews API credentials within the Composio connection settings.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your target competitor list and industry keywords.
- **Agent**: Processes search results and performs sentiment analysis on the retrieved text.
- **Composio Toolset**: Executes the search queries and data extraction from HackerNews.
- **Chat Output**: Delivers the final intelligence report and trend summary to your preferred interface.

### 3) Run the Flow
Use the Playground to test the agent with prompts such as:
- `Analyze the sentiment of recent HackerNews mentions for [Competitor Name] regarding their pricing.`
- `What are the top 3 technical complaints users have about [Technology Category] this week?`
- `Summarize the community reaction to the latest product launch from [Competitor Name].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a market research analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system prompt to prioritize objective analysis and sentiment accuracy.
- Configure temperature to 0.3 for consistent, fact-based reporting.

### 2) Composio Toolset Node
- Provide your API key to enable secure access to the HackerNews search endpoints.
- Define the connection scope to include read-only access to public discussion threads.

### 3) Tool Availability
- **HackerNews Search**: Query threads by keyword or domain.
- **Thread Parser**: Extract comment trees and metadata from specific URLs.
- **Sentiment Classifier**: Categorize text based on predefined business criteria.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Track account-level signals and engagement data.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) - Monitor competitor video content and audience engagement.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research into target accounts and market positioning.
