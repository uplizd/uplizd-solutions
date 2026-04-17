# Prospect Research Assistant (Uplizd) - Automate prospect enrichment and research for high-conversion outreach

## Summary
The Prospect Research Assistant is an intelligent Uplizd workflow that automates the gathering of firmographic and lead-specific data directly within your Attio CRM. By leveraging the Composio Toolset to query external intelligence sources, this agent eliminates manual research time, ensuring your sales team has a unified, enriched source of truth for every prospect before they initiate outreach.

---

## Demo
![Prospect Research Assistant workflow interface showing data enrichment from Attio CRM to sales outreach](image.png)
**Alt text (SEO-ready):** Prospect Research Assistant workflow in Uplizd, automating Attio CRM data enrichment, lead qualification, and sales intelligence gathering.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d3dd261f-cb57-517e-b313-52a731a9f553)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, attio, prospect research, lead enrichment, sales intelligence, pipeline velocity, composio, ai workflow
- This solution streamlines the pre-outreach research phase, allowing sales teams to focus on closing rather than data entry.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce administrative overhead and improve lead personalization.

- **Sales Development Representative (SDR)**
    - Drastically reduces the time spent manually researching prospect backgrounds before cold calls.
- **Account Executive (AE)**
    - Ensures every discovery call is backed by deep, up-to-date account intelligence.
- **RevOps Manager**
    - Standardizes the data quality and enrichment process across the entire sales pipeline.
- **Sales Manager**
    - Increases team capacity by automating the repetitive research tasks that hinder daily outreach volume.

---

## Features
- **Automated Attio Sync**
    - Seamlessly pulls prospect records from Attio and pushes enriched insights back into custom fields.
- **Intelligent Data Enrichment**
    - Uses the Composio Toolset to fetch real-time company news, funding rounds, and professional history.
- **Customizable Research Logic**
    - Configure the agent to prioritize specific data points like recent leadership changes or technology stack usage.
- **Real-time Pipeline Updates**
    - Automatically updates lead status or adds research summaries to CRM notes as soon as the agent completes its analysis.
- **Human-in-the-loop Validation**
    - Provides a review step for the agent's findings before final CRM synchronization to ensure 100% data accuracy.

---

## Use Cases
**Pre-Outreach Preparation**
- Automatically generate a "Research Brief" for every new lead assigned to an SDR in Attio.
- Identify recent company milestones to personalize the opening line of your cold emails.

**Account Qualification**
- Cross-reference prospect data against ideal customer profile (ICP) criteria to score leads automatically.
- Flag accounts that have recently undergone significant organizational changes for immediate follow-up.

**CRM Data Hygiene**
- Fill in missing job titles, LinkedIn URLs, and company descriptions to keep your CRM database pristine.
- Standardize company name formatting and industry tagging across your entire prospect list.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Attio account via the integration settings.
3. Configure your preferred LLM model (e.g., GPT-4o or Claude 3.5 Sonnet) in the Agent node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the prospect email or ID from your CRM trigger.
- **Agent**: Analyzes the prospect and determines which research tools to invoke.
- **Composio Toolset**: Executes API calls to fetch external intelligence and update Attio records.
- **Chat Output**: Confirms the enrichment status and provides a summary of the research performed.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Research the company associated with this prospect email: [email address]`
- `Find the latest funding news for this prospect's company and update the 'Notes' field in Attio.`
- `Summarize the professional background of this lead and suggest three personalized talking points.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your primary research analyst.
- **Instruction Pattern:**
    - "You are an expert sales researcher; use the provided tools to gather data on the prospect's company."
    - "Always prioritize recent, verified information over outdated cached data."
    - "Format all output as a concise summary for a sales professional."

### 2) Composio Toolset Node
- **API Key:** Ensure your Composio API key is active and authorized for Attio and relevant search tools.
- **Connection Scope:** Grant read/write access to your Attio CRM to allow the agent to update prospect records directly.

### 3) Tool Availability
- **Attio API**: For reading and updating lead and company objects.
- **Web Search/Intelligence Tools**: For fetching real-time news and professional data.
- **Data Parser**: For cleaning and structuring unstructured text into CRM-ready fields.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Specialized research for high-value accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automated reporting on account engagement and intent signals.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizing prospect data across multiple CRM platforms.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Mapping and strengthening complex account relationships.
