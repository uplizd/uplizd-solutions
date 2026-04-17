# Earnings Alert Agent (Uplizd) - Real-time financial data monitoring and automated market notifications

## Summary
The Earnings Alert Agent is an automated workflow designed to monitor, capture, and notify users of critical corporate earnings announcements. By leveraging the Benzinga API through the Composio Toolset, this solution ensures investors and financial analysts receive timely, actionable intelligence, reducing the manual effort required to track market-moving events and providing a single source of truth for portfolio-impacting data.

---

## Demo
![Earnings Alert Agent workflow diagram showing Benzinga API integration and automated notification flow](image.png)
**Alt text (SEO-ready):** Earnings Alert Agent workflow diagram showing Benzinga API integration, automated financial data tracking, and market notification flow on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bb0f5709-e30d-53e7-a597-901f2c7b2c25)

---

## Category
- **Primary category:** Financial Operations
- **Secondary tags:** benzinga, earnings, market data, financial intelligence, automated alerts, investment tracking, composio, ai workflow
- This solution bridges the gap between raw financial market data and real-time user awareness through intelligent automation.

---

## Who is this for?
This agent is built for finance professionals and active investors who require immediate updates on market performance.

- **Financial Analyst**
    - Automates the collection of quarterly earnings reports to focus on high-level data interpretation.
- **Portfolio Manager**
    - Receives instant alerts on holdings to make rapid, data-driven rebalancing decisions.
- **Day Trader**
    - Gains a competitive edge by reacting to earnings surprises before the broader market adjusts.
- **Investment Researcher**
    - Maintains a structured database of historical earnings trends for long-term strategy development.

---

## Features
- **Real-time Earnings Tracking**
    - Connects directly to the Benzinga API to pull live earnings announcements as they are released.
- **Automated Notification Engine**
    - Triggers instant alerts via your preferred communication channel when specific tickers report earnings.
- **Intelligent Data Filtering**
    - Uses the Agent node to parse complex financial filings and extract key metrics like EPS and revenue beats.
- **Seamless Composio Integration**
    - Utilizes the Composio Toolset to securely authenticate and execute API calls to financial data providers.
- **Customizable Alert Thresholds**
    - Allows users to define specific watchlists and sensitivity levels for market-moving announcements.

---

## Use Cases
**Portfolio Monitoring**
- Automatically track earnings dates for all stocks currently held in your brokerage account.
- Receive summary reports of earnings surprises for your top 10 high-conviction assets.

**Market Intelligence**
- Monitor competitor earnings to identify shifts in industry performance and market share.
- Aggregate earnings call highlights to prepare for daily morning briefings or client meetings.

**Automated Research**
- Build a historical archive of earnings performance for specific sectors to identify seasonal trends.
- Trigger automated follow-up research tasks when an earnings report deviates significantly from analyst expectations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import" to add the Earnings Alert Agent to your workspace.
3. Connect your Benzinga API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user-defined tickers or watchlists to monitor.
- **Agent**: Processes financial data and determines if an alert condition is met.
- **Composio Toolset**: Executes authenticated requests to the Benzinga API for real-time data.
- **Chat Output**: Delivers the formatted earnings report or alert notification to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Check if AAPL has released earnings today and summarize the results.`
- `Monitor my watchlist [TSLA, NVDA, AMD] for upcoming earnings announcements this week.`
- `Get the latest earnings report for MSFT and highlight any revenue surprises.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a financial analyst, summarizing complex data into readable insights.
- Instruct the agent to prioritize "Earnings Surprise" and "Revenue vs. Estimate" metrics.
- Configure the agent to ignore non-essential market noise and focus on actionable financial data.
- Set the output format to be concise, professional, and notification-ready.

### 2) Composio Toolset Node
- Provide your valid Benzinga API key within the integration settings.
- Ensure the connection scope includes read access to market data and earnings calendars.

### 3) Tool Availability
- **Earnings Calendar API**: Fetch upcoming and historical earnings dates.
- **Market Data Fetcher**: Retrieve real-time price and volume data surrounding earnings events.
- **Financial News Parser**: Extract qualitative sentiment from earnings-related press releases.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregate and report on account-level intelligence and signals.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on target accounts and companies.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage and strengthen B2B account connections within your CRM.
