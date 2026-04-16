# Account Research Assistant (Uplizd) - Automated B2B account intelligence and sales preparation

## Summary
The Account Research Assistant by ZoomInfo is an intelligent Uplizd workflow designed to automate the gathering of firmographic data, recent news, and strategic talking points for B2B sales teams. By leveraging real-time data retrieval through the Composio Toolset, this solution eliminates manual research time, ensuring sales representatives enter every discovery call with a comprehensive, data-backed understanding of their prospects.

---

## Demo
![Account Research Assistant workflow showing ZoomInfo data integration and AI-driven profile generation](image.png)
**Alt text (SEO-ready):** Uplizd Account Research Assistant workflow using ZoomInfo integration for automated B2B sales intelligence and prospect profile generation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a6568608-31e0-5b35-9820-a94ee566d404)

---

## Category
**Sales automation**
- **Secondary tags:** `account research`, `zoominfo`, `sales intelligence`, `b2b sales`, `prospecting`, `composio`, `ai workflow`, `data enrichment`
This solution streamlines the sales research process by integrating live account intelligence directly into your CRM-adjacent workflows.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maximize pipeline velocity through better preparation.

- **Account Executive**
    - Reduces pre-call research time from hours to minutes by surfacing relevant account insights instantly.
- **Sales Development Representative**
    - Increases outreach personalization by leveraging specific company news and firmographic triggers.
- **Sales Operations Manager**
    - Standardizes the quality of account research across the team, ensuring consistent data hygiene and preparation.
- **Revenue Leader**
    - Improves win rates by ensuring the team is equipped with strategic talking points and competitive intelligence.

---

## Features
- **Automated Account Profiling**
    - Instantly generates a structured summary of target accounts including industry, size, and key stakeholders.
- **Real-Time News Integration**
    - Pulls the latest company announcements and press releases via ZoomInfo to provide timely conversation starters.
- **Strategic Talking Point Extraction**
    - Identifies potential pain points and growth opportunities based on the retrieved account data.
- **Composio-Powered Connectivity**
    - Seamlessly bridges the gap between raw data sources and your AI agent for accurate, real-time information retrieval.
- **Customizable Output Formats**
    - Configures research briefs into standardized templates suitable for CRM logging or email preparation.

---

## Use Cases
**Strategic Account Planning**
- Compiling executive-level briefs for high-stakes enterprise discovery calls.
- Mapping organizational hierarchies to identify key decision-makers and influencers.

**Sales Outreach Personalization**
- Crafting hyper-personalized email sequences based on recent company funding or leadership changes.
- Identifying "trigger events" that signal a high probability of a successful sales conversation.

**Competitive Intelligence**
- Monitoring competitor mentions and market positioning within a target account's industry.
- Benchmarking account growth metrics against industry standards to tailor value propositions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Account Research Assistant.
2. Click "Import" to add the workflow to your workspace.
3. Connect your ZoomInfo API credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company domain or account name from the user.
- **Agent**: Processes the request, determines the research strategy, and instructs the toolset.
- **Composio Toolset**: Executes the ZoomInfo search queries to fetch real-time account data.
- **Chat Output**: Formats the retrieved intelligence into a readable, actionable research brief.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Research the current growth trajectory and recent news for [Company Name].`
- `Generate a list of strategic talking points for a discovery call with the VP of Sales at [Company Name].`
- `Provide a summary of the firmographic profile and key decision-makers for [Company Name].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized sales researcher.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set system instructions to prioritize recent data and professional, sales-oriented tone.
- Ensure the agent is instructed to cite sources for all retrieved news or firmographic claims.

### 2) Composio Toolset Node
- Provide your ZoomInfo API key in the node configuration.
- Set the connection scope to allow read-only access to account and company intelligence endpoints.

### 3) Tool Availability
- `zoominfo_search_company`: Retrieves firmographic data and company overview.
- `zoominfo_get_news`: Fetches recent press releases and media mentions.
- `zoominfo_get_contacts`: Identifies key personnel and leadership roles.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automated data enrichment and contact discovery.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Mapping and managing complex B2B account hierarchies.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automating the creation and configuration of new CRM accounts.
