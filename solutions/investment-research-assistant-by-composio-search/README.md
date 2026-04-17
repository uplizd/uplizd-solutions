# Investment Research Assistant (Uplizd) - Automated market intelligence and financial data analysis

## Summary
The Investment Research Assistant is an AI-powered workflow designed to streamline the collection, synthesis, and analysis of complex financial data. By leveraging the Composio Toolset to query real-time market search engines and financial databases, this solution provides analysts and investors with a single source of truth, significantly reducing the time spent on manual data gathering and accelerating informed decision-making.

---

## Demo
![Investment Research Assistant workflow showing automated search, data synthesis, and report generation](image.png)
**Alt text (SEO-ready):** Investment Research Assistant (Uplizd) workflow for automated financial data analysis, market intelligence gathering, and real-time research using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/712415f5-2bb4-5c70-9a9b-b1ef6d51f0d9)

---

## Category
**Primary category:** Financial Operations
**Secondary tags:** investment research, market intelligence, financial analysis, data synthesis, composio, ai workflow, automated reporting, equity research.
This solution bridges the gap between raw market data and actionable investment insights through intelligent automation.

---

## Who is this for?
This assistant is designed for professionals who need to synthesize vast amounts of financial information into clear, actionable reports.

* **Investment Analyst**
    * Automates the aggregation of quarterly reports and market sentiment analysis to save hours of manual research.
* **Portfolio Manager**
    * Provides real-time tracking of asset performance and news alerts to maintain a competitive edge in volatile markets.
* **Financial Researcher**
    * Enables rapid deep-dives into industry trends and competitor filings with structured data extraction.
* **Growth Strategist**
    * Identifies emerging market opportunities by correlating macroeconomic data with sector-specific performance metrics.

---

## Features
- **Real-time Market Search**
  Utilizes the Composio Toolset to fetch the latest financial news, stock updates, and regulatory filings instantly.
- **Automated Data Synthesis**
  The Agent node processes unstructured text from multiple sources to extract key performance indicators and sentiment scores.
- **Structured Report Generation**
  Automatically formats research findings into professional summaries, ready for stakeholder review or internal documentation.
- **Cross-Platform Integration**
  Seamlessly connects with financial databases and search APIs to ensure data integrity and breadth of coverage.
- **Intelligent Querying**
  Supports complex natural language prompts, allowing users to ask nuanced questions about market trends and asset valuations.

---

## Use Cases
**Market Trend Analysis**
- Summarizing the impact of macroeconomic shifts on specific industry sectors over the last quarter.
- Identifying emerging patterns in competitor earnings calls and public disclosures.

**Asset Performance Monitoring**
- Tracking daily volatility and news sentiment for a specific portfolio of tickers.
- Comparing historical performance metrics against current market benchmarks.

**Due Diligence Automation**
- Compiling comprehensive background research on potential investment targets from multiple web sources.
- Extracting and verifying key financial data points from unstructured PDF reports and news articles.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Investment Research Assistant template from the solution library.
3. Connect your preferred LLM provider and the necessary Composio API keys.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives your specific research query or ticker symbol.
* **Agent**: Orchestrates the search strategy and synthesizes the retrieved data.
* **Composio Toolset**: Executes precise web searches and database queries to fetch external financial intelligence.
* **Chat Output**: Delivers the final, structured research report to your interface.

### 3) Run the Flow
Use the Playground to test your research capabilities with these prompts:
- `Analyze the recent market sentiment for NVDA and summarize the top 3 risks identified in the latest earnings call.`
- `Compare the Q3 performance metrics of the top 5 companies in the renewable energy sector.`
- `Provide a comprehensive research summary on the impact of recent interest rate changes on the real estate market.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized financial analyst.
* Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data synthesis.
* Instruction pattern: "You are an expert financial researcher. Always cite your sources. Prioritize data from official filings and reputable financial news outlets."
* Ensure the system prompt includes constraints on formatting to maintain consistency in output reports.

### 2) Composio Toolset Node
* Provide your Composio API key to enable secure access to search and financial data tools.
* Set the connection scope to include web search, financial news APIs, and document retrieval services.

### 3) Tool Availability
* **Search Tools**: Google Search, Bing Search, or specialized financial news aggregators.
* **Data Extraction**: Tools for parsing PDFs and web-based financial tables.
* **Analysis Tools**: Mathematical and logical reasoning functions for calculating performance ratios.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research on corporate accounts and business entities.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generates detailed reports on account activity and lead signals.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Collects and verifies contact and firmographic data for target accounts.
