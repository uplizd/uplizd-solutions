# AI Prospect Research Assistant (Uplizd) - Automate deep-dive prospect intelligence and lead research

## Summary
The AI Prospect Research Assistant is an automated workflow that streamlines the sales discovery process by aggregating, synthesizing, and formatting prospect data from PeopleDataLabs. By automating the manual collection of professional profiles, company insights, and contact signals, this Uplizd solution empowers sales teams to increase pipeline velocity and ensure every outreach is backed by high-quality, actionable intelligence.

---

## Demo
![AI Prospect Research Assistant workflow dashboard showing automated data enrichment and prospect report generation](image.png)
**Alt text (SEO-ready):** AI Prospect Research Assistant workflow dashboard showing automated data enrichment and prospect report generation via Uplizd and PeopleDataLabs integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/a1d328a9-380f-53ac-8e80-5ee4c67abd2b)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** `prospecting`, `peopledatalabs`, `lead enrichment`, `sales intelligence`, `data sync`, `composio`, `ai workflow`  
This solution bridges the gap between raw contact data and personalized sales outreach by automating the research phase of the CRM lifecycle.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual research bottlenecks and improve lead conversion rates.

*   **Sales Development Reps (SDRs)**
    *   Accelerate lead qualification by receiving pre-researched prospect dossiers before initial outreach.
*   **Account Executives (AEs)**
    *   Prepare for high-stakes discovery calls with comprehensive company and contact intelligence.
*   **Sales Operations Managers**
    *   Standardize the quality of prospect data entering the CRM to ensure consistent lead scoring.
*   **Growth Marketers**
    *   Identify high-intent prospects by leveraging enriched data signals for targeted account-based marketing.

---

## Features
- **Automated Data Enrichment**
  Instantly pull professional background, work history, and company details using the PeopleDataLabs API.
- **Intelligent Synthesis**
  The Agent node processes raw data points into a concise, readable intelligence report tailored for sales conversations.
- **Composio Toolset Integration**
  Seamlessly connects the Uplizd workflow to external data providers, ensuring real-time access to accurate prospect information.
- **Customizable Output Formatting**
  Configure the Chat Output node to deliver research summaries in your preferred format, whether for email templates or CRM notes.
- **Scalable Research Pipeline**
  Handle bulk prospect lists by automating the research loop, significantly reducing the time spent on manual data entry.

---

## Use Cases
**Pre-Call Preparation**
*   Generate a summary of a prospect's recent career moves and professional achievements before a scheduled demo.
*   Extract key company growth signals to tailor the value proposition during initial discovery calls.

**Lead Qualification**
*   Validate contact information and professional seniority against ideal customer profile (ICP) criteria.
*   Score leads based on enriched data points like company size, industry, and recent funding events.

**Outreach Personalization**
*   Create hyper-personalized icebreakers based on the prospect's specific professional background and interests.
*   Identify common connections or shared professional experiences to build rapport faster in cold emails.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your PeopleDataLabs API credentials within the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the prospect's name, email, or LinkedIn profile URL.
*   **Agent**: Analyzes the input and triggers the necessary research tools.
*   **Composio Toolset**: Executes the API calls to fetch and normalize prospect data.
*   **Chat Output**: Delivers the final, formatted intelligence report to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
* `Research the professional background and current role of [Prospect Name] at [Company Name].`
* `Provide a summary of recent company news and growth signals for [Company Name].`
* `Create a personalized outreach summary for [Prospect Name] based on their recent career history.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the research analyst, interpreting raw data into actionable insights.
*   **Instruction Pattern:**
    *   Focus on identifying key professional milestones and company-level signals.
    *   Maintain a professional, sales-oriented tone suitable for B2B communication.
    *   Prioritize data accuracy by cross-referencing provided API outputs.

### 2) Composio Toolset Node
*   **API Key:** Input your PeopleDataLabs API key in the Composio configuration.
*   **Connection Scope:** Ensure the toolset has read access to professional profile and company search endpoints.

### 3) Tool Availability
*   **Profile Search:** Retrieve detailed professional history and contact information.
*   **Company Intelligence:** Fetch firmographic data, industry tags, and growth signals.
*   **Data Normalization:** Clean and format raw API responses into structured text.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate comprehensive reports on account engagement and intent.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with verified contact details.
