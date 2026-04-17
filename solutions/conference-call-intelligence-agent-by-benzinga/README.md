# Conference Call Intelligence Agent (Uplizd) - Automated earnings call insights and executive summary extraction

## Summary
The Conference Call Intelligence Agent streamlines the extraction of critical financial data and strategic insights from corporate earnings calls. By leveraging the Benzinga API through the Composio Toolset, this Uplizd workflow automates the monitoring of market-moving events, providing RevOps and investor relations teams with a single source of truth for real-time executive sentiment, guidance updates, and performance metrics.

---

## Demo
![Conference Call Intelligence Agent workflow dashboard showing automated transcript analysis and sentiment extraction](image.png)
**Alt text (SEO-ready):** Uplizd Conference Call Intelligence Agent workflow for automated earnings call transcript analysis, financial insight extraction, and market sentiment tracking using Benzinga API.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f47c1c77-1e4f-51a6-9548-82c2df744421)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** `earnings calls`, `financial intelligence`, `benzinga`, `market data`, `sentiment analysis`, `investor relations`, `composio`, `ai workflow`
- This solution bridges the gap between raw financial audio transcripts and actionable executive intelligence for data-driven decision-making.

---

## Who is this for?
This agent is designed for professionals who need to synthesize complex financial communications into clear, actionable summaries.

- **Investor Relations Manager**
    - Automate the drafting of internal briefing notes following high-stakes earnings announcements.
- **Financial Analyst**
    - Rapidly identify key guidance metrics and revenue projections across multiple company portfolios.
- **Market Researcher**
    - Track shifts in executive sentiment and strategic priorities during quarterly call cycles.
- **Portfolio Manager**
    - Receive summarized alerts on market-moving statements to inform immediate investment adjustments.

---

## Features
- **Automated Transcript Retrieval**
    - Seamlessly pulls the latest earnings call transcripts via the Benzinga API integration.
- **Executive Sentiment Analysis**
    - Evaluates the tone and confidence levels of leadership teams during Q&A sessions.
- **Key Metric Extraction**
    - Automatically isolates revenue targets, EPS guidance, and growth projections from unstructured text.
- **Real-time Alerting**
    - Triggers notifications when specific keywords or financial thresholds are met during a live or recorded call.
- **Strategic Summary Generation**
    - Compiles multi-page transcripts into concise, executive-ready summaries formatted for internal reporting.

---

## Use Cases
**Earnings Season Monitoring**
- Automatically generate summary reports for all companies in a specific watchlist immediately after earnings release.
- Compare current quarter guidance against historical data to identify trends in company performance.

**Competitive Intelligence**
- Extract strategic commentary from competitor earnings calls to benchmark against your own organization's messaging.
- Monitor industry-wide sentiment shifts regarding macroeconomic factors mentioned by executives.

**Investor Relations Preparation**
- Create "cheat sheets" for leadership teams based on recent peer earnings calls to prepare for upcoming investor meetings.
- Identify frequently asked questions from analysts to proactively update internal FAQ documents.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Conference Call Intelligence Agent template from the marketplace.
3. Connect your Benzinga API credentials within the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the ticker symbol and the specific quarter/year requested by the user.
*   **Agent**: Processes the request, instructs the toolset to fetch data, and synthesizes the final report.
*   **Composio Toolset**: Executes the API calls to Benzinga to retrieve accurate transcript data.
*   **Chat Output**: Delivers the structured summary and sentiment analysis back to the user interface.

### 3) Run the Flow
*   `Summarize the Q3 earnings call for AAPL and highlight the main revenue guidance.`
*   `What was the executive sentiment regarding supply chain constraints in the latest TSLA earnings call?`
*   `Extract all forward-looking statements from the most recent MSFT earnings transcript.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial analyst assistant.
- Focus on extracting quantitative data points (EPS, Revenue, Guidance).
- Maintain a neutral, professional tone suitable for corporate reporting.
- Prioritize accuracy by citing specific sections of the transcript when possible.

### 2) Composio Toolset Node
- Requires a valid Benzinga API key configured within your Composio account.
- Scope should be set to allow read access to financial transcripts and market news endpoints.

### 3) Tool Availability
- `get_transcript`: Fetches the full text of earnings call transcripts.
- `get_market_sentiment`: Analyzes text for positive/negative sentiment indicators.
- `search_financial_news`: Retrieves supplemental news articles related to the ticker.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Identify and track key account signals for sales teams.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep-dive research and data gathering for enterprise accounts.
- [YouTube Audience Research Agent](../you-tube-audience-research-agent-by-youtube/README.md) — Analyze video content and audience engagement for market insights.
