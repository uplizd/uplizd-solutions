# Lead Intelligence Researcher (Uplizd) - Automate lead enrichment and prospect research

## Summary
The Lead Intelligence Researcher (Uplizd) workflow automates the gathering of deep prospect insights, transforming raw contact lists into high-context profiles. By leveraging the Composio Toolset to query external data sources, this solution enables sales teams to personalize outreach at scale, significantly reducing manual research time while increasing conversion rates through data-driven engagement.

---

## Demo
![Lead Intelligence Researcher workflow dashboard showing automated prospect data enrichment and CRM integration](image.png)
**Alt text (SEO-ready):** Lead Intelligence Researcher Uplizd workflow, automated prospect data enrichment, sales intelligence, and CRM integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0037d69c-3757-51cc-a66b-d8229c313c06)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** lead intelligence, lemlist, prospect research, sales outreach, data enrichment, crm, ai workflow, composio

This solution bridges the gap between raw lead data and actionable sales intelligence by automating the research process for modern revenue teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual research bottlenecks and improve outreach relevance.

* **Sales Development Representative (SDR)**
    * Automates the pre-call research process to focus on high-value prospect interactions.
* **Account Executive (AE)**
    * Gains immediate access to deep company and prospect insights to tailor discovery calls.
* **Growth Marketer**
    * Ensures lead lists are enriched with high-quality data for targeted multi-channel campaigns.
* **Sales Operations Manager**
    * Standardizes the research data format across the team to maintain high-quality CRM hygiene.

---

## Features
- **Automated Prospect Enrichment**
    Automatically pulls professional background, company news, and recent activities for any lead.
- **Composio-Powered Research**
    Utilizes the Composio Toolset to securely interface with external research APIs and data providers.
- **Real-Time Data Synthesis**
    Aggregates disparate data points into a concise, readable summary for immediate use in outreach.
- **CRM Integration Ready**
    Seamlessly maps enriched intelligence back to your CRM fields to maintain a single source of truth.
- **Customizable Research Depth**
    Adjust the agent's focus to prioritize specific data points like funding rounds, tech stack, or hiring trends.

---

## Use Cases
**Personalized Cold Outreach**
* Generate custom icebreakers based on a prospect's recent LinkedIn posts or company announcements.
* Tailor email messaging to address specific pain points identified during the automated research phase.

**Account-Based Marketing (ABM)**
* Identify key decision-makers within target accounts and map their professional history.
* Monitor target company growth signals to trigger timely, relevant outreach sequences.

**Sales Pipeline Hygiene**
* Refresh stale lead data with current contact information and professional updates.
* Categorize leads based on enriched intelligence to prioritize high-intent prospects in the pipeline.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the builder.
3. Configure your API credentials for the integrated research tools within the Composio node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the prospect's name, email, or LinkedIn URL.
* **Agent**: Processes the input and orchestrates the research strategy.
* **Composio Toolset**: Executes the specific search and enrichment queries.
* **Chat Output**: Delivers the finalized, enriched prospect profile to the user.

### 3) Run the Flow
Use the Playground to test your research agent with these prompts:
* `Research the recent funding news for [Company Name] and identify the key stakeholders.`
* `Find the latest professional achievements for [Prospect Name] at [Company Name].`
* `Create a summary of [Company Name]'s current tech stack and recent hiring trends.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the research analyst, synthesizing raw data into actionable insights.
* **Role:** Expert Sales Researcher.
* **Instruction Pattern:** 
    * Focus on identifying high-signal data points relevant to sales outreach.
    * Maintain a professional, concise tone for all generated summaries.
    * Prioritize the most recent and relevant information found during the research process.

### 2) Composio Toolset Node
* **API Key:** Ensure your Composio API key is active and authorized for the necessary research connectors.
* **Connection Scope:** Grant the toolset read-only access to relevant research platforms to ensure data security.

### 3) Tool Availability
* **Search APIs:** Real-time web and news searching.
* **Professional Databases:** LinkedIn and company profile enrichment tools.
* **Data Formatting:** Structured output generation for CRM compatibility.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate deep-dive research on target accounts.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Streamline account-level data collection and reporting.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Leverage ZoomInfo for comprehensive prospect intelligence.
