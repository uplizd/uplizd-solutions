# Lead Qualification Bot (Uplizd) - Automated web-based lead research and qualification

## Summary
The Lead Qualification Bot is an intelligent Uplizd workflow that leverages the Browserbase toolset to autonomously research, analyze, and score incoming leads. By automating the extraction of firmographic and intent data from public web sources, this solution enables sales teams to focus their energy on high-probability prospects, significantly increasing pipeline velocity and ensuring only qualified leads reach the CRM.

---

## Demo
![Lead Qualification Bot workflow diagram showing web research, data extraction, and qualification scoring](image.png)
**Alt text (SEO-ready):** Uplizd Lead Qualification Bot workflow using Browserbase for automated sales lead research, data enrichment, and qualification scoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/68ff36a2-cfa4-559d-a021-2fb4b6c5de01)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** lead qualification, browserbase, sales intelligence, lead scoring, pipeline management, web scraping, automation, ai workflow

This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the manual research process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual data entry and prioritize high-value prospects.

*   **Sales Development Representative (SDR)**
    *   Reduces time spent on manual research per lead, allowing for higher daily outreach volume.
*   **Revenue Operations (RevOps) Manager**
    *   Standardizes the qualification criteria across the team to ensure consistent pipeline hygiene.
*   **Account Executive (AE)**
    *   Receives pre-qualified leads with actionable context, leading to higher conversion rates on discovery calls.
*   **Growth Marketer**
    *   Provides rapid feedback loops on lead quality from specific campaigns or inbound channels.

---

## Features
- **Automated Web Research**
    Utilizes Browserbase to navigate and extract relevant business intelligence from prospect websites in real-time.
- **Intelligent Qualification Scoring**
    Applies custom logic to rank leads based on firmographic fit, technology stack, and intent signals.
- **Seamless CRM Integration**
    Connects with your existing sales stack via the Composio Toolset to update lead records automatically.
- **Real-time Data Enrichment**
    Gathers and synthesizes public data points to provide a comprehensive view of the prospect before the first contact.
- **Customizable Qualification Logic**
    Easily adjust the Agent's instructions to align with your specific Ideal Customer Profile (ICP) and disqualification triggers.

---

## Use Cases
**Inbound Lead Triage**
*   Automatically research company size and industry for every new form submission.
*   Flag leads that match high-priority target accounts for immediate notification.

**Outbound Prospecting Support**
*   Verify current website content and recent news for prospects before adding them to a sequence.
*   Identify key decision-makers by scraping "About Us" or "Team" pages during the qualification phase.

**Data Hygiene & Enrichment**
*   Update lead records with missing website descriptions or social media links found during the research process.
*   Flag outdated or incorrect company URLs to keep your CRM data clean and actionable.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Bot template from the solution library.
3. Connect your required API credentials for Browserbase and your CRM.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the lead's website URL or company name.
*   **Agent**: Processes the request and determines the research strategy.
*   **Composio Toolset**: Executes browser-based navigation and data extraction tasks.
*   **Chat Output**: Returns the qualification score and summary report to the user.

### 3) Run the Flow
Open the Playground and test with these prompts:
* `Qualify this lead: https://example-company.com and check for recent news.`
* `Research the target account: Acme Corp and identify their primary product offering.`
* `Analyze this prospect website and determine if they fit our enterprise software ICP.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your lead research analyst. 
*   Define the ICP clearly in the system prompt to ensure consistent scoring.
*   Instruct the agent to prioritize specific data points (e.g., employee count, tech stack).
*   Set a strict output format for the qualification report to ensure CRM compatibility.

### 2) Composio Toolset Node
*   Provide your Browserbase API key to enable headless web navigation.
*   Configure the connection scope to allow read-only access to web content and write access to your CRM.

### 3) Tool Availability
*   **Web Navigation**: Ability to visit URLs and extract text content.
*   **Search Integration**: Capability to query search engines for company background.
*   **CRM Write Access**: Ability to push qualification scores and notes to lead records.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research for specific target accounts.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting on account-level intent signals.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score sales opportunities in your pipeline.
