# Prospect Research Assistant (Uplizd) - Automated deep intelligence gathering for personalized sales outreach

## Summary
The Prospect Research Assistant is an automated Uplizd AI workflow designed to streamline the pre-call research process by aggregating real-time data from the web. By leveraging the Exa search engine and Composio toolset, this solution identifies key company insights, recent news, and leadership updates, providing sales teams with a single source of truth to drive higher engagement and pipeline velocity.

---

## Demo
![Prospect Research Assistant workflow showing Chat Input, Exa Search Agent, and structured output](image.png)
**Alt text (SEO-ready):** Prospect Research Assistant Uplizd workflow using Exa search for automated sales intelligence and lead data gathering.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0430101d-2e7d-54bb-9fd2-9169640ae4be)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** prospect research, exa, sales intelligence, lead enrichment, outbound sales, ai workflow, composio, pipeline velocity
- This solution bridges the gap between raw web data and actionable sales intelligence, enabling teams to personalize outreach at scale.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual research time and increase meeting conversion rates.

- **Account Executive**
    - Spend less time on manual Google searches and more time conducting high-quality discovery calls.
- **Sales Development Representative (SDR)**
    - Generate hyper-personalized icebreakers for cold emails based on the latest company news.
- **Revenue Operations Manager**
    - Standardize the research process across the team to ensure consistent data quality and lead scoring.
- **Growth Marketer**
    - Identify target account triggers to align outbound campaigns with current market events.

---

## Features
- **Automated Web Intelligence**
    - Uses Exa to perform deep-web searches, filtering out noise to deliver high-signal data about target prospects.
- **Contextual Summarization**
    - Transforms complex search results into concise, readable briefings tailored for sales preparation.
- **Composio-Powered Integration**
    - Seamlessly connects the research agent to your existing CRM and communication stack for instant data handoff.
- **Real-Time Trigger Detection**
    - Monitors for specific company events like funding rounds, leadership changes, or product launches.
- **Personalized Outreach Generation**
    - Drafts custom email openers based on the specific research findings retrieved during the workflow execution.

---

## Use Cases
**Pre-Call Preparation**
- Automatically generate a "cheat sheet" for upcoming meetings including recent company news and competitor mentions.
- Extract key pain points from a prospect's recent public interviews or blog posts.

**Outbound Lead Enrichment**
- Enrich lead profiles with recent funding data and growth signals to prioritize high-intent accounts.
- Identify commonalities between the prospect's company and your current successful customer base.

**Market Intelligence**
- Track industry-wide shifts by aggregating news across a list of target accounts in a specific vertical.
- Monitor competitor activity to adjust sales positioning in real-time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Prospect Research Assistant template file provided in this repository.
3. Configure your API keys for Exa and your chosen CRM within the integration settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company name or prospect URL.
- **Agent**: Analyzes the request and determines the necessary search queries.
- **Composio Toolset**: Executes precise web searches and retrieves structured data.
- **Chat Output**: Delivers the final, formatted research briefing to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Research the recent funding news for [Company Name] and summarize how it impacts their growth strategy.`
- `Find the latest leadership changes at [Company Name] and draft a personalized email opener for their VP of Sales.`
- `What are the top 3 strategic priorities for [Company Name] based on their recent press releases?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the research analyst, synthesizing search results into actionable sales insights.
- **Recommended instruction pattern:**
    - Act as a senior sales researcher focused on high-intent signals.
    - Prioritize recent news (last 90 days) over generic company descriptions.
    - Format output with clear headers: "Company Overview," "Recent Triggers," and "Outreach Suggestions."

### 2) Composio Toolset Node
- Requires a valid Exa API key to perform high-quality web searches.
- Connection scope should include read-access to web search tools and your CRM for data syncing.

### 3) Tool Availability
- **Exa Search**: For deep-web intelligence gathering.
- **CRM Connector**: For saving research notes directly to account records.
- **Email Client**: For drafting and sending personalized outreach.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Targeted deep-dive research for specific account profiles.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Automated reporting on account activity and intent signals.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrichment of account data with contact-level details.
