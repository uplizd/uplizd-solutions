# Client Pitch Research Agent (Uplizd) - Accelerate sales discovery with automated advertising intelligence

## Summary
The Client Pitch Research Agent automates the discovery of prospect advertising strategies, enabling sales teams to deliver highly personalized pitches with minimal manual effort. By leveraging real-time data from Adyntel, this Uplizd workflow acts as a force multiplier for BDRs and Account Executives, ensuring they arrive at every meeting with actionable insights into a prospect's digital footprint and market positioning.

---

## Demo
![Client Pitch Research Agent workflow diagram showing Adyntel data integration and automated pitch generation](../image.png)
**Alt text (SEO-ready):** Client Pitch Research Agent workflow on Uplizd, featuring Adyntel advertising intelligence integration for automated sales pitch preparation and prospect research.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7a5d39ef-eb8f-5b6c-92a8-d85152546afc)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales intelligence, adyntel, prospect research, pitch preparation, bdr, account executive, sales operations, ai workflow
- This solution bridges the gap between raw advertising data and high-impact sales conversations by automating the research phase of the deal cycle.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to reduce research time and increase meeting conversion rates.

- **Business Development Representatives (BDRs)**
    - Quickly qualify leads by understanding their current ad spend and platform focus before the first outreach.
- **Account Executives (AEs)**
    - Build hyper-personalized pitch decks that address specific pain points identified in a prospect's live ad campaigns.
- **Sales Managers**
    - Standardize the quality of prospect research across the team to ensure consistent messaging and higher win rates.
- **Revenue Operations (RevOps)**
    - Integrate automated intelligence into the CRM workflow to keep sales data enriched and actionable.

---

## Features
- **Automated Ad Intelligence**
    - Pulls real-time advertising strategy data via Adyntel to provide an instant snapshot of where a prospect is spending their budget.
- **Context-Aware Pitch Generation**
    - Uses the Agent node to synthesize research findings into tailored talking points that resonate with the prospect's specific market activity.
- **Composio-Powered Connectivity**
    - Seamlessly connects to external research tools and CRM platforms to ensure data flows directly into your existing sales stack.
- **Real-Time Data Retrieval**
    - Eliminates the need for manual browser searches by fetching the latest ad trends and campaign performance metrics on demand.
- **Customizable Output Formats**
    - Configures the Chat Output to deliver insights in various formats, from concise email summaries to detailed pitch deck bullet points.

---

## Use Cases
**Prospect Discovery**
- Automatically pull a company's top-performing ad channels before a discovery call.
- Identify shifts in a prospect's messaging strategy to time your outreach for maximum relevance.

**Pitch Personalization**
- Generate a "Competitive Edge" summary that highlights how your solution solves problems identified in their current ad creatives.
- Create custom value propositions based on the prospect's historical ad spend and platform presence.

**Sales Workflow Efficiency**
- Reduce research time per lead by 80% by automating the data gathering and synthesis process.
- Sync research summaries directly into your CRM to keep the entire account team aligned on the prospect's status.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the agent.
3. Connect your Adyntel and CRM credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the prospect's company name or domain.
- **Agent**: Analyzes the input and triggers the research logic.
- **Composio Toolset**: Executes the Adyntel API calls to fetch advertising data.
- **Chat Output**: Returns the synthesized pitch research to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Research the advertising strategy for [Company Name] and suggest 3 pitch angles.`
- `What are the primary ad channels used by [Domain] and how can we position our product against them?`
- `Summarize the recent ad campaign trends for [Company Name] for an upcoming sales meeting.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized sales researcher.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a sales intelligence expert. Analyze the provided ad data and craft a pitch that highlights specific opportunities for the prospect."
- Ensure the agent is configured to prioritize actionable insights over raw data dumps.

### 2) Composio Toolset Node
- Provide your Adyntel API key within the Composio configuration.
- Set the connection scope to allow read-only access to advertising analytics and campaign performance endpoints.

### 3) Tool Availability
- **Adyntel Search**: Retrieves live advertising data and campaign metrics.
- **Data Formatter**: Cleans and structures raw API responses for the Agent.
- **CRM Connector**: (Optional) Pushes research summaries to your CRM account records.

---

## Related Solutions
- [Ad Trend Tracking Agent](../ad-trend-tracking-agent-by-adyntel/README.md) - Monitor competitor ad spend and market trends.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive into firmographic data and contact intelligence.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate automated reports on prospect website intent.
