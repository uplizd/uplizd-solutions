# Competitive Intelligence Agent (Uplizd) - Automate competitor tracking and team insights

## Summary
The Competitive Intelligence Agent by Hunter is an automated workflow designed to streamline market research by monitoring competitor hiring patterns and organizational changes. By leveraging real-time email discovery and web intelligence, this Uplizd solution provides RevOps and sales teams with a single source of truth for competitor activity, ensuring pipeline velocity and proactive market positioning.

---

## Demo
![Competitive Intelligence Agent workflow dashboard showing Hunter integration and data extraction nodes](image.png)
**Alt text (SEO-ready):** Competitive Intelligence Agent by Uplizd, automated market research workflow, Hunter email discovery, competitor tracking, and sales intelligence integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMJFR0W+7/35QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxK04AAAAiSURBVEjHY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwChgBAAAGAAH5314AAAAASUVORK5DMII=)](https://uplizd.ai/solutions/5fd9a927-d053-543a-b3ce-45683e365046)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** competitive intelligence, hunter, lead generation, sales ops, market research, data enrichment, ai workflow, composio

This solution empowers teams to automate the gathering of competitive insights, turning raw web data into actionable sales intelligence.

---

## Who is this for?
This workflow is designed for growth-oriented teams looking to gain a strategic edge through automated data collection and analysis.

- **Sales Operations Manager**
    - Automates the tracking of competitor hiring trends to adjust territory planning and outreach strategies.
- **Account Executive**
    - Receives real-time alerts on competitor organizational changes to better position product value during discovery calls.
- **Market Research Analyst**
    - Eliminates manual data scraping by centralizing competitor intelligence into a structured, searchable format.
- **Growth Marketer**
    - Identifies shifts in competitor focus by monitoring public-facing team growth and key personnel updates.

---

## Features
- **Automated Hunter Integration**
    - Seamlessly connects with Hunter to discover and verify professional contact data associated with competitor organizations.
- **Real-time Market Monitoring**
    - Continuously scans for updates in competitor team structures, ensuring your intelligence database remains current.
- **Intelligent Data Synthesis**
    - Uses advanced LLM processing to summarize complex organizational data into concise, actionable insights for stakeholders.
- **Pipeline Velocity Optimization**
    - Reduces the time spent on manual research, allowing sales teams to focus on high-intent engagement.
- **Composio-Powered Tooling**
    - Leverages the Composio Toolset to orchestrate complex API interactions between web scrapers and CRM platforms.

---

## Use Cases
**Competitor Hiring Analysis**
- Track new engineering or sales hires at target competitor firms to gauge their expansion strategy.
- Automatically enrich contact information for key decision-makers identified within competitor teams.

**Market Positioning Alerts**
- Receive automated summaries when a competitor updates their leadership team or key department heads.
- Compare competitor growth metrics against internal benchmarks to refine your competitive battlecards.

**Sales Intelligence Enrichment**
- Populate your CRM with verified contact data discovered through competitor research workflows.
- Generate weekly reports on competitor activity to keep the entire sales organization aligned.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Competitive Intelligence Agent template from the solution library.
3. Connect your Hunter API credentials within the integration settings.
4. Ensure nodes are correctly linked from the Chat Input to the Agent and finally to the Output.

### 2) Setup the Nodes
- **Chat Input**: Accepts the competitor domain or company name to initiate the research.
- **Agent**: Processes the request, determines the research scope, and queries the necessary tools.
- **Composio Toolset**: Executes the Hunter API calls and web data extraction tasks.
- **Chat Output**: Delivers the synthesized competitive report directly to your workspace.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Analyze the hiring trends for [Competitor Domain] over the last 30 days.`
- `Find key decision-makers at [Competitor Name] and verify their professional emails.`
- `Summarize the recent organizational changes at [Competitor Domain] and suggest a sales angle.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a research assistant, prioritizing accuracy and data synthesis.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for best results.
- Instruct the agent to prioritize verified contact data over speculative information.
- Ensure the agent follows a structured output format for all generated reports.

### 2) Composio Toolset Node
- Provide your Hunter API key to enable email discovery capabilities.
- Set the connection scope to allow the agent to perform search and verification operations on your behalf.

### 3) Tool Availability
- **Hunter Search API**: For finding professional contact information.
- **Hunter Email Verifier**: For ensuring the accuracy of discovered leads.
- **Web Search/Scraping Tools**: For gathering public organizational data and news.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate the collection of firmographic data for target accounts.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research into prospect organizations using ZoomInfo.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score sales opportunities based on real-time signals.
