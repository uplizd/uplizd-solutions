# Account Research Agent (Uplizd) - Automated account intelligence and strategic sales insights

## Summary
The Account Research Agent is an intelligent workflow designed to automate the collection and synthesis of firmographic and strategic data for target accounts. By leveraging the Composio Toolset to query OnePage CRM and other intelligence sources, this agent provides sales teams with a single source of truth, significantly reducing manual research time and accelerating pipeline velocity through high-quality, real-time account insights.

---

## Demo
![Account Research Agent workflow diagram showing data ingestion from OnePage CRM and AI-driven report generation](image.png)
**Alt text (SEO-ready):** Account Research Agent workflow diagram showing data ingestion from OnePage CRM and AI-driven report generation, powered by Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/44bfe9e2-5bdf-5f13-b94b-0c831560f272)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, onepage, account intelligence, sales research, data enrichment, pipeline, salesops, ai workflow
- This solution streamlines the account research process by integrating real-time CRM data with AI-driven analysis to empower data-backed sales strategies.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual data gathering and improve engagement quality.

- **Account Executives**
    - Spend less time on manual research and more time on high-value prospect interactions.
- **Sales Development Reps (SDRs)**
    - Quickly identify key account signals to personalize outreach and improve conversion rates.
- **Sales Operations Managers**
    - Ensure consistent, high-quality account data across the organization to maintain pipeline hygiene.
- **Growth Marketers**
    - Leverage deep account insights to tailor account-based marketing (ABM) campaigns effectively.

---

## Features
- **Automated Intelligence Gathering**
    - Automatically pulls firmographic data and recent activity from OnePage CRM to build comprehensive account profiles.
- **AI-Driven Strategic Summaries**
    - Synthesizes raw data into actionable insights, highlighting potential pain points and growth opportunities.
- **Real-Time Data Integration**
    - Uses the Composio Toolset to ensure the agent always has access to the most current account information.
- **Customizable Research Templates**
    - Tailor the output format to match your specific sales playbooks and reporting requirements.
- **Seamless Workflow Orchestration**
    - Connects directly to your existing CRM stack, ensuring that research findings are ready for immediate use in sales outreach.

---

## Use Cases
**Strategic Account Planning**
- Generate pre-call briefings that summarize recent account activity and key stakeholders.
- Identify cross-sell and up-sell opportunities based on historical account usage and interaction patterns.

**Sales Outreach Personalization**
- Create hyper-personalized email drafts based on recent news or company updates discovered during research.
- Align messaging with the specific business challenges identified in the automated account report.

**Pipeline Hygiene & Management**
- Automatically flag accounts with missing or outdated information for immediate enrichment.
- Standardize the research process across the team to ensure every opportunity is backed by consistent intelligence.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Account Research Agent template from the marketplace.
3. Authenticate your OnePage CRM connection via the Composio integration menu.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target account name or domain from the user.
- **Agent**: Processes the request and determines which research tools to invoke.
- **Composio Toolset**: Executes API calls to fetch account details and external intelligence.
- **Chat Output**: Delivers the finalized, structured account research report to the user.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Research the current account status and key contacts for [Company Name].`
- `Generate a strategic briefing for [Company Name] focusing on recent growth signals.`
- `What are the primary pain points for [Company Name] based on our latest CRM interactions?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting CRM data and formatting it into professional reports.
- **Instruction Pattern**:
    - Focus on extracting high-value signals rather than just raw data.
    - Maintain a professional, objective tone suitable for executive briefings.
    - Prioritize information that directly impacts the sales cycle.

### 2) Composio Toolset Node
- **API Key**: Ensure your OnePage CRM API key is active within the Composio dashboard.
- **Connection Scope**: Grant read-only access to account, contact, and activity modules to ensure secure data retrieval.

### 3) Tool Availability
- **CRM Data Fetcher**: Retrieves account firmographics and contact lists.
- **Activity Logger**: Pulls recent notes, calls, and meeting summaries.
- **Intelligence Parser**: Analyzes unstructured text for sentiment and key business triggers.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account profiles with external firmographic data.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Map and manage complex stakeholder relationships within your CRM.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the creation and configuration of new accounts in your CRM.
