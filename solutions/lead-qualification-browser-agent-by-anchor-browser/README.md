# Lead Qualification Browser Agent (Uplizd) - Automated web-based lead research and qualification

## Summary
The Lead Qualification Browser Agent is an intelligent Uplizd workflow that automates the research and vetting of potential leads by navigating the web to gather firmographic data and intent signals. By leveraging the Composio Toolset to interact with browser-based tools, this solution enables sales teams to instantly qualify prospects, reduce manual research time, and ensure only high-intent leads enter the CRM pipeline.

---

## Demo
![Lead Qualification Browser Agent workflow interface showing automated web research and data extraction](image.png)
**Alt text (SEO-ready):** Lead Qualification Browser Agent workflow for automated web research, lead scoring, and sales pipeline data hygiene using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwCuA/AA0G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8G/w8A4s0J/00028sAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/93d6c75a-78e4-5920-b0dc-686b851e780f)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** lead qualification, browser automation, sales intelligence, crm, lead scoring, web scraping, composio, ai workflow  
This solution bridges the gap between raw web data and actionable CRM insights, streamlining the lead qualification process for modern sales teams.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual lead research and improve pipeline quality.

* **Sales Development Representative (SDR)**
    * Accelerates daily prospecting by automating the initial research phase for new inbound leads.
* **Account Executive (AE)**
    * Provides instant context on prospect pain points and company size before discovery calls.
* **RevOps Manager**
    * Standardizes the lead qualification criteria across the team to ensure consistent data hygiene.
* **Growth Marketer**
    * Identifies high-intent prospects by monitoring web signals and company news in real-time.

---

## Features
- **Automated Web Research**
    Uses browser-based agents to visit company websites and extract key firmographic details automatically.
- **Intelligent Lead Scoring**
    Analyzes gathered web data against your specific qualification criteria to assign a lead score.
- **Composio Toolset Integration**
    Seamlessly connects the agent to web browsers and search tools to fetch live, up-to-date information.
- **Real-time Data Sync**
    Pushes qualified lead profiles directly into your CRM, ensuring your sales team has the latest data.
- **Custom Qualification Logic**
    Allows for tailored instructions to the Agent node to match your unique business model and target persona.

---

## Use Cases
**Lead Enrichment**
* Extracting employee count and industry vertical from a prospect's company website.
* Identifying current technology stacks or software competitors used by the lead.

**Qualification Filtering**
* Automatically disqualifying leads that do not meet minimum company size or revenue thresholds.
* Flagging high-priority leads for immediate outreach based on recent news or funding announcements.

**Pipeline Hygiene**
* Updating CRM fields with verified contact information gathered from the web.
* Removing duplicate or outdated lead entries based on the most recent web-scraped data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Browser Agent template from the marketplace.
3. Configure your API credentials for the integrated browser and CRM tools.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the lead URL or company domain to be researched.
* **Agent:** Processes the research request and applies qualification logic.
* **Composio Toolset:** Executes browser actions to fetch data from the web.
* **Chat Output:** Returns the qualified lead summary and scoring results.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Research the company at https://example.com and qualify them based on our enterprise criteria.`
* `Find the latest funding news for this prospect and update their lead score.`
* `Extract the primary industry and key services from the provided URL.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the research analyst, interpreting web data and applying business rules.
* Instruct the agent to prioritize specific data points like revenue, industry, and tech stack.
* Define clear "Pass/Fail" thresholds for lead qualification.
* Set the tone for the output summary to be concise and actionable for sales reps.

### 2) Composio Toolset Node
* Provide your Composio API key to enable secure browser-based tool execution.
* Ensure the connection scope includes read access to web search and browser navigation tools.

### 3) Tool Availability
* **Web Search:** For finding company news and public firmographic data.
* **Browser Navigation:** For visiting specific URLs to extract page content.
* **Data Parser:** For converting unstructured web text into structured CRM-ready fields.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automates the collection of detailed firmographic data for target accounts.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Streamlines deep-dive research into prospect accounts for personalized outreach.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensures seamless data synchronization across multiple CRM and sales platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitors and scores sales opportunities to improve pipeline management.
