# Customer Research Assistant (Uplizd) - Automated deep-dive insights for high-conversion sales calls

## Summary
The Customer Research Assistant is an intelligent Uplizd workflow that automates the collection and synthesis of prospect data, providing sales teams with a single source of truth before every meeting. By leveraging the Composio Toolset to query external databases and web sources, this agent eliminates manual research time, improves pipeline velocity, and ensures every conversation is backed by actionable intelligence.

---

## Demo
![Customer Research Assistant workflow dashboard showing automated data retrieval and synthesis](image.png)
**Alt text (SEO-ready):** Customer Research Assistant Uplizd workflow, automated sales intelligence gathering, CRM data enrichment, and prospect research pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4759afa4-e083-55b8-981d-f0d73419f7de)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, research, sales intelligence, lead enrichment, pipeline, sales productivity, composio, ai workflow
- This solution bridges the gap between raw lead data and meaningful sales conversations by automating the research process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maximize the impact of every customer interaction.

- **Account Executives**
    - Spend less time on manual research and more time closing deals with pre-call briefing notes.
- **Sales Development Reps (SDRs)**
    - Qualify leads faster by instantly accessing relevant company news and recent funding or hiring activity.
- **Revenue Operations (RevOps)**
    - Standardize the quality of prospect data across the team to ensure consistent pipeline hygiene.
- **Customer Success Managers**
    - Prepare for quarterly business reviews by automatically pulling the latest account usage and sentiment signals.

---

## Features
- **Automated Prospect Profiling**
    - Instantly aggregates company background, recent news, and social signals into a structured briefing document.
- **Composio-Powered Integration**
    - Seamlessly connects with CRM platforms and web search tools to pull real-time data without leaving the workflow.
- **Intelligent Synthesis**
    - Uses advanced LLMs to filter out noise and highlight only the most relevant talking points for your specific sales motion.
- **Customizable Research Depth**
    - Configure the agent to prioritize specific data points, such as recent leadership changes or competitor mentions.
- **Real-time Data Sync**
    - Updates lead records directly in your CRM, ensuring the entire organization has access to the latest research.

---

## Use Cases
**Pre-Call Preparation**
- Automatically generate a "cheat sheet" for upcoming meetings 30 minutes before the call starts.
- Identify key pain points based on recent company announcements or industry trends.

**Lead Qualification**
- Enrich incoming leads with firmographic data to determine if they meet your ideal customer profile (ICP).
- Flag high-intent signals such as recent expansion news or product launches for immediate follow-up.

**Account Intelligence**
- Monitor existing accounts for trigger events that indicate an opportunity for upsell or cross-sell.
- Compile historical research summaries to provide a comprehensive view of the account relationship.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your preferred workspace and project destination.
3. Authenticate your required CRM and search tool connections within the Composio dashboard.
4. Ensure nodes are correctly mapped and all API keys are validated in the settings panel.

### 2) Setup the Nodes
- **Chat Input**: Receives the prospect's company name or URL.
- **Agent**: Processes the request and determines which research tools to trigger.
- **Composio Toolset**: Executes real-time queries against external databases and search engines.
- **Chat Output**: Delivers the synthesized research report to the user.

### 3) Run the Flow
Open the Uplizd Playground and try these prompts:
- `Research the recent funding news for [Company Name] and summarize how it impacts our value proposition.`
- `Find the latest leadership changes at [Company Name] and draft a personalized outreach email.`
- `Provide a comprehensive summary of [Company Name]'s recent market activity and potential pain points.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a research analyst, prioritizing accuracy and relevance.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a senior sales researcher. Focus on actionable insights that help an AE build rapport."
- Instruction: "If data is conflicting, prioritize the most recent news sources."

### 2) Composio Toolset Node
- Provide your API key in the node settings to enable secure access to your connected tools.
- Ensure the connection scope includes read access to your CRM and web search capabilities.

### 3) Tool Availability
- **CRM Connector**: For pulling existing account data and contact history.
- **Web Search Tool**: For fetching the latest news, press releases, and public company information.
- **Data Enrichment API**: For firmographic and technographic details.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Specialized research workflows for one-page account summaries.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting for lead intelligence and intent signals.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research utilizing ZoomInfo data integration.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Workflow for mapping and strengthening account relationships in Dynamics 365.
