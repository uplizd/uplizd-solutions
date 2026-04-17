# Lead Research Assistant (Uplizd) - Automate prospect intelligence and personalize outreach

## Summary
The Lead Research Assistant is an AI-driven workflow that automates the gathering of prospect data and company insights to fuel highly personalized sales outreach. By leveraging the Tavily search engine via the Composio Toolset, this solution eliminates manual research time, ensuring sales teams have a single source of truth for prospect context, resulting in higher response rates and improved pipeline velocity.

---

## Demo
![Lead Research Assistant workflow showing Chat Input, Tavily search agent, and output generation](image.png)
**Alt text (SEO-ready):** Lead Research Assistant workflow by Uplizd using Tavily for automated prospect intelligence and sales outreach personalization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/6712409c-e23a-5729-b438-453dde4edbf3)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** `lead research`, `tavily`, `prospecting`, `sales outreach`, `ai agent`, `composio`, `pipeline`, `data enrichment`

This solution integrates real-time web intelligence into your sales stack to transform cold outreach into data-backed conversations.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outbound efforts without sacrificing quality.

* **Sales Development Representative (SDR)**
    * Drastically reduces time spent on manual account research before drafting emails.
* **Account Executive (AE)**
    * Provides deep context on prospect pain points to improve discovery call readiness.
* **Sales Operations Manager**
    * Standardizes the research process across the team to ensure consistent lead qualification.
* **Growth Marketer**
    * Enables hyper-personalized messaging based on current company news and industry trends.

---

## Features
- **Real-time Web Intelligence**
  Uses the Tavily search engine to fetch the latest news, funding rounds, and company updates.
- **Automated Prospect Summarization**
  Synthesizes complex web data into actionable insights for immediate use in outreach.
- **Composio Toolset Integration**
  Seamlessly connects the agent to external search tools, ensuring reliable and up-to-date information retrieval.
- **Personalization Engine**
  Drafts tailored opening lines based on specific prospect achievements or company milestones.
- **Workflow Pipeline Velocity**
  Accelerates the transition from lead identification to meaningful engagement by automating the research phase.

---

## Use Cases
**Outbound Email Personalization**
* Researching recent company press releases to craft a relevant "hook" for cold emails.
* Identifying recent leadership changes to tailor the value proposition to the new stakeholder.

**Account Discovery & Qualification**
* Gathering background data on a prospect's industry competitors to identify potential pain points.
* Summarizing a prospect's recent public-facing projects to assess product-market fit.

**Sales Meeting Preparation**
* Generating a "cheat sheet" of recent company activity to use during discovery calls.
* Extracting key industry trends to position your solution as the timely answer to market shifts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Research Assistant template file provided in this repository.
3. Configure your API keys for the Tavily search provider within the Composio settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the prospect's name, company, and target URL.
* **Agent**: Processes the input and orchestrates the research logic.
* **Composio Toolset**: Executes real-time web searches to retrieve prospect data.
* **Chat Output**: Delivers the formatted research summary and personalized email draft.

### 3) Run the Flow
Open the Playground and test the flow with these prompts:
* `Research the recent funding news for [Company Name] and draft a personalized outreach email.`
* `Find the latest product launches for [Company Name] and summarize how it impacts their market position.`
* `Give me a 3-bullet point summary of [Prospect Name]'s recent professional activities and industry focus.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a research analyst, prioritizing accuracy and relevance.
* Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Act as a senior sales researcher. Use the provided tools to find specific, recent, and relevant information."
* Instruction: "Synthesize findings into a concise summary followed by a 2-sentence personalized outreach hook."

### 2) Composio Toolset Node
* Requires a valid Tavily API key to perform web searches.
* Connection scope should be set to allow read-only access to public web data.

### 3) Tool Availability
* **Search Tool**: Enables the agent to perform targeted queries on company websites and news outlets.
* **Summarization Tool**: Processes raw search results into readable, professional insights.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research for high-value account planning.
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - ZoomInfo-integrated intelligence for enterprise prospecting.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting on account intent and visitor data.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Scoring and tracking lead signals for pipeline management.
