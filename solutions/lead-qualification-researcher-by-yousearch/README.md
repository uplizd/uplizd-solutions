# Lead Qualification Researcher (Uplizd) - Automated prospect research and lead qualification

## Summary
The Lead Qualification Researcher (Uplizd) is an intelligent AI workflow designed to automate the discovery and vetting of sales prospects. By leveraging the YouSearch engine, this solution streamlines the research process, allowing sales teams to instantly gather firmographic data, verify contact intent, and score leads. It serves as a single source of truth for prospect intelligence, significantly reducing manual research time and increasing pipeline velocity.

---

## Demo
![Lead Qualification Researcher workflow diagram showing Chat Input, Agent, YouSearch Toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** Lead Qualification Researcher workflow diagram showing Chat Input, Agent, YouSearch Toolset, and Chat Output for automated sales prospecting and lead scoring on Uplizd.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAHAAABAAAB)](https://uplizd.ai/solutions/bbd7bad8-16bc-56c6-9e59-dd817a9d5d25)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead qualification, prospect research, yousearch, sales intelligence, pipeline, data enrichment, ai workflow, composio
- This solution bridges the gap between raw web data and actionable sales intelligence by automating deep-dive prospect research.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to prioritize high-intent prospects through automated research.

- **Sales Development Representative (SDR)**
    - Automates the initial research phase to focus on high-quality outreach rather than manual data gathering.
- **Account Executive (AE)**
    - Gains instant access to prospect background, company news, and pain points before discovery calls.
- **Revenue Operations Manager**
    - Ensures consistent lead qualification standards across the team by standardizing the research workflow.
- **Growth Marketer**
    - Identifies target account signals and trends to refine outbound messaging and campaign targeting.

---

## Features
- **Automated Prospect Research**
    - Uses the YouSearch engine to pull real-time company and individual data from across the web.
- **Intelligent Lead Scoring**
    - Evaluates prospect information against defined criteria to prioritize high-value opportunities.
- **Structured Data Extraction**
    - Converts unstructured search results into clean, actionable summaries for CRM entry.
- **Composio Toolset Integration**
    - Seamlessly connects the AI agent to external research tools to execute complex queries.
- **Real-time Insight Generation**
    - Delivers concise briefings on prospect intent, recent funding, or company milestones.

---

## Use Cases
**Prospect Vetting**
- Automatically verify if a lead matches your Ideal Customer Profile (ICP) based on recent company news.
- Filter out low-intent leads by cross-referencing industry keywords and recent hiring trends.

**Account Intelligence**
- Generate a comprehensive briefing document on a target account before a scheduled sales meeting.
- Identify recent pain points or technical challenges mentioned in public forums or company blogs.

**Pipeline Prioritization**
- Rank incoming leads based on the depth of research findings and alignment with current product offerings.
- Trigger follow-up tasks for high-scoring leads that show strong signals of immediate need.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Researcher template from the library.
3. Connect your YouSearch API credentials to the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the prospect name and company domain from the user.
- **Agent**: Processes the research request and determines the necessary search queries.
- **Composio Toolset**: Executes the web search and data retrieval via YouSearch.
- **Chat Output**: Formats the research findings into a readable summary for the sales team.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Research the recent funding and growth of Acme Corp and identify if they are a good fit for our enterprise software.`
- `Find the latest news on John Doe at TechFlow and summarize his recent professional focus.`
- `Identify potential pain points for a mid-sized logistics company based on current industry trends.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized research analyst.
- **Recommended instruction pattern:**
    - Act as a senior sales researcher focused on identifying high-intent prospects.
    - Use the provided search tools to find verified company information and recent news.
    - Summarize findings into a structured format: Company Overview, Recent Signals, and Qualification Score.

### 2) Composio Toolset Node
- Requires a valid YouSearch API key to perform external web lookups.
- Connection scope should be set to "Read-Only" for search operations to ensure data security.

### 3) Tool Availability
- **Search Engine Access**: Allows the agent to query the web for real-time data.
- **Data Summarization**: Processes search results into concise, bulleted insights.
- **Entity Extraction**: Pulls specific names, dates, and funding figures from search snippets.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research for target account planning.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automating lead intelligence and reporting.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enriching account data for sales outreach.
