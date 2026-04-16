# Competitive Intelligence Scout (Uplizd) - Automated market research and competitor monitoring

## Summary
The Competitive Intelligence Scout is an Uplizd AI workflow designed to automate the collection, analysis, and reporting of competitor activities. By leveraging the Zenserp integration, this solution empowers teams to maintain a single source of truth regarding market shifts, pricing changes, and content strategies, significantly increasing pipeline velocity and strategic decision-making accuracy.

---

## Demo
![Competitive Intelligence Scout workflow dashboard showing automated search queries and data extraction](image.png)
**Alt text (SEO-ready):** Competitive Intelligence Scout Uplizd workflow, automated market research, competitor monitoring, Zenserp integration, and AI-driven data extraction.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/641eb5ab-6d60-5927-9ec8-a6c34418a2a1)

---

## Category
- **Primary category:** Market Intelligence
- **Secondary tags:** competitive intelligence, zenserp, market research, data extraction, ai workflow, sales strategy, composio, business insights
- This solution bridges the gap between raw web data and actionable business strategy by automating the discovery of competitor movements.

---

## Who is this for?
This solution is designed for professionals who need to stay ahead of market trends without manual research overhead.

- **Market Researcher**
    - Automates the collection of competitor pricing and product updates across search engines.
- **Sales Operations Manager**
    - Tracks competitor activities to provide the sales team with real-time battlecards and objection handling data.
- **Product Manager**
    - Monitors feature releases and market positioning to inform the product roadmap.
- **Growth Strategist**
    - Identifies gaps in the market by analyzing competitor search visibility and content distribution.

---

## Features
- **Automated Search Execution**
    - Uses the Zenserp integration to perform real-time, high-accuracy search queries across global markets.
- **Intelligent Data Extraction**
    - Parses complex search results into structured formats, filtering out noise to highlight relevant competitor signals.
- **Cross-Platform Sync**
    - Seamlessly pushes intelligence reports into your CRM or project management tools via the Composio Toolset.
- **Trend Analysis**
    - Identifies patterns in competitor behavior over time, allowing for proactive rather than reactive strategy adjustments.
- **Customizable Alerting**
    - Configures automated notifications when specific competitor keywords or product changes are detected.

---

## Use Cases
**Competitor Pricing Monitoring**
- Track daily price fluctuations for key product SKUs across major e-commerce platforms.
- Generate weekly reports comparing your pricing strategy against top-tier market competitors.

**Market Positioning Research**
- Analyze search engine result pages (SERPs) to identify which competitors are winning on specific industry keywords.
- Extract meta-descriptions and ad copy to understand how competitors are positioning their value propositions.

**Product Launch Tracking**
- Monitor competitor websites and news sources for announcements of new features or service updates.
- Automatically summarize competitor press releases and update internal product battlecards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the builder.
2. Connect your Zenserp API credentials within the Composio Toolset node.
3. Configure your target competitor domains and search keywords in the Agent node.
4. Ensure nodes are connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the search parameters and competitor domains from the user.
- **Agent**: Processes the search intent and orchestrates the Zenserp tool calls.
- **Composio Toolset**: Executes the web search and data extraction via Zenserp.
- **Chat Output**: Delivers the summarized intelligence report back to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Find the latest pricing updates for [Competitor Name] on their primary product page.`
- `Search for recent press releases regarding [Competitor Name] and summarize their new feature announcements.`
- `Compare the search visibility of our top 3 competitors for the keyword '[Industry Keyword]'.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain, translating search results into business insights.
- **Instruction Pattern:**
    - Focus on extracting specific data points like price, feature names, and sentiment.
    - Maintain a consistent professional tone for all generated intelligence reports.
    - Prioritize recent search results (last 30 days) to ensure data relevance.

### 2) Composio Toolset Node
- Requires a valid Zenserp API key to perform web searches.
- Connection scope should include read-only access to search engine result data.

### 3) Tool Availability
- **Zenserp Search**: Performs targeted queries to retrieve live web data.
- **Data Parser**: Cleans and structures raw HTML/text into readable summaries.
- **Notification Hook**: Optional integration to send reports to Slack or Email.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Tracks account-level signals and visitor intent.
- [YouTube Competitor Intelligence Agent](../you-tube-competitor-intelligence-agent-by-youtube/README.md) — Monitors competitor video content and audience engagement.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Gathers deep firmographic data on target accounts.
