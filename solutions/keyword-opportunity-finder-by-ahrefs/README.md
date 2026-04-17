# Keyword Opportunity Finder (Uplizd) - Automated SEO research and high-value content discovery

## Summary
The Keyword Opportunity Finder (Uplizd) is an automated AI workflow that leverages Ahrefs data to identify high-potential search terms, analyze competitor gaps, and surface actionable content opportunities. By streamlining the research process, this solution enables marketing teams to maintain a competitive edge, improve organic search visibility, and ensure their content strategy is driven by real-time search intent data.

---

## Demo
![Keyword Opportunity Finder workflow showing Ahrefs integration and AI analysis](image.png)
**Alt text (SEO-ready):** Keyword Opportunity Finder workflow on Uplizd, showing Ahrefs integration for SEO research, content gap analysis, and automated keyword opportunity reporting.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/8c27e01f-bf77-5461-ad59-071044bc1819)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** seo, ahrefs, keyword research, content strategy, organic growth, search intent, composio, ai workflow
- This solution bridges the gap between raw search data and content execution, providing a scalable way to automate SEO research workflows.

---

## Who is this for?
This solution is designed for marketing and growth teams looking to scale their organic search efforts through data-driven insights.

- **Content Strategist**
    - Identifies high-volume, low-difficulty keywords to prioritize in the editorial calendar.
- **SEO Specialist**
    - Monitors competitor keyword gaps and tracks search intent shifts in real-time.
- **Growth Marketer**
    - Uncovers untapped market niches to drive qualified traffic and lead generation.
- **Marketing Manager**
    - Ensures content production aligns with proven search demand to maximize ROI.

---

## Features
- **Automated Keyword Discovery**
    - Uses the Composio Toolset to query Ahrefs for high-value search terms based on specific industry topics.
- **Competitor Gap Analysis**
    - Automatically compares your domain's keyword rankings against top competitors to find missing content opportunities.
- **Search Intent Classification**
    - Analyzes keyword data to categorize terms by user intent, ensuring content matches the target audience's needs.
- **Real-Time Data Sync**
    - Connects directly to Ahrefs via the Composio Toolset to ensure research is based on the most current search metrics.
- **Actionable Reporting**
    - Generates summarized insights and content recommendations directly within the Chat Output node for immediate team review.

---

## Use Cases
**Content Strategy Planning**
- Automatically generate a list of 10 high-potential keywords for upcoming blog posts.
- Identify long-tail keyword clusters that have low competition but high search volume.

**Competitor Intelligence**
- Monitor competitor domains to see which new keywords they are ranking for this month.
- Perform a content gap analysis to find topics your competitors cover that you currently ignore.

**Performance Optimization**
- Audit existing high-traffic pages to find related keywords for internal linking opportunities.
- Refresh underperforming content by identifying new, relevant keywords to target in updates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Keyword Opportunity Finder template via the provided solution URL.
3. Connect your Ahrefs account within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts the target topic or competitor domain as the primary query.
- **Agent**: Processes the request and formulates the logic for keyword research.
- **Composio Toolset**: Executes the API calls to Ahrefs to fetch search volume, difficulty, and ranking data.
- **Chat Output**: Delivers the final, formatted list of keyword opportunities and strategic suggestions.

### 3) Run the Flow
Use the Playground to test your research prompts:
- `Find 10 high-volume, low-difficulty keywords for the topic 'AI marketing automation' in the US market.`
- `Analyze the keyword gap between my domain 'example.com' and 'competitor.com' for the 'SaaS' category.`
- `What are the top 5 trending search queries related to 'remote work tools' this month?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your SEO research assistant, translating natural language queries into structured data requests.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- Instruct the agent to prioritize keywords with a difficulty score below 30.
- Ensure the output is formatted as a clear, prioritized table for easy export to spreadsheets.

### 2) Composio Toolset Node
- Provide your Ahrefs API key within the Composio integration settings.
- Scope the connection to allow read-only access to keyword explorer and site explorer endpoints.

### 3) Tool Availability
- **Keyword Explorer**: Fetches search volume, keyword difficulty, and CPC data.
- **Site Explorer**: Retrieves domain-specific ranking data and competitor keyword profiles.
- **Content Gap Tool**: Identifies keywords that competitors rank for but the target domain does not.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automates the gathering of account-level insights and lead signals.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyzes video content performance and audience search trends.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Streamlines deep-dive research on target accounts and prospects.
