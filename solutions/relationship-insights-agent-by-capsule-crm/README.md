# Relationship Insights Agent (Uplizd) - Uncover hidden CRM interaction patterns and relationship health

## Summary
The Relationship Insights Agent leverages AI to analyze communication history and interaction patterns within Capsule CRM, providing actionable intelligence on account health and engagement velocity. By synthesizing fragmented touchpoints into a single source of truth, this workflow enables revenue teams to identify at-risk relationships and high-potential opportunities, significantly improving pipeline hygiene and account management efficiency.

---

## Demo
![Relationship Insights Agent dashboard showing interaction trends and CRM health scores](image.png)
**Alt text (SEO-ready):** Relationship Insights Agent by Uplizd for Capsule CRM, showing AI-driven interaction analysis, relationship health scoring, and automated sales pipeline insights.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/08e1d462-eb3d-53a8-afb8-eb6acabe364a)

---

## Category
**Primary category:** CRM data
**Secondary tags:** capsule crm, relationship management, sales intelligence, account health, data sync, ai workflow, composio, pipeline velocity.
This solution bridges the gap between raw CRM interaction logs and strategic account planning for data-driven sales organizations.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to turn historical CRM data into a competitive advantage.

*   **Account Managers**
    *   Proactively identify accounts with declining engagement before churn occurs.
*   **Sales Operations**
    *   Standardize relationship health metrics across the entire customer portfolio.
*   **Revenue Leaders**
    *   Gain high-level visibility into team interaction velocity and relationship depth.
*   **Customer Success Managers**
    *   Automate the identification of key milestones and follow-up opportunities.

---

## Features
- **Interaction Pattern Analysis**
  Deep-dives into communication frequency and sentiment to map the health of every account.
- **Automated Health Scoring**
  Calculates real-time relationship scores based on recent activity, meetings, and email exchanges.
- **Composio-Powered CRM Sync**
  Seamlessly connects with Capsule CRM to pull live interaction data without manual exports.
- **Proactive Risk Alerts**
  Flags stalled accounts or missing touchpoints to ensure no relationship goes cold.
- **Strategic Insight Summaries**
  Generates concise executive briefings on account status, ready for weekly pipeline reviews.

---

## Use Cases
**Account Health Monitoring**
*   Detecting accounts with no recorded interaction in the last 30 days.
*   Flagging negative sentiment trends in recent communication logs.

**Pipeline Velocity Optimization**
*   Prioritizing follow-ups for accounts showing high engagement but stalled deal stages.
*   Identifying "dormant" contacts that require immediate re-engagement campaigns.

**Relationship Mapping**
*   Analyzing the frequency of touchpoints across different stakeholders within a single account.
*   Correlating interaction volume with successful deal closure rates in Capsule CRM.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and import the workflow definition.
3. Authenticate your Capsule CRM account via the Composio connection prompt.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target account name or ID for analysis.
*   **Agent**: Processes CRM data using the configured LLM instructions to derive insights.
*   **Composio Toolset**: Executes secure API calls to Capsule CRM to fetch interaction history.
*   **Chat Output**: Delivers the synthesized relationship report and health score.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
* `Analyze the relationship health for [Account Name] and summarize recent interaction trends.`
* `Which accounts have had no activity in the last 45 days?`
* `Provide a summary of the top 3 most engaged stakeholders for [Account Name].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent requires a reasoning-capable model to interpret CRM logs.
* Set the temperature to 0.2 for factual, data-driven analysis.
* Use system instructions to prioritize recent interaction dates.
* Ensure the agent is instructed to output insights in a structured, bulleted format.

### 2) Composio Toolset Node
* Provide your Capsule CRM API key within the Composio dashboard.
* Scope the connection to read-only access for contacts, opportunities, and history logs.

### 3) Tool Availability
* `capsule_crm_list_contacts`: Fetches account metadata.
* `capsule_crm_get_interaction_history`: Retrieves communication logs and meeting notes.
* `capsule_crm_search_opportunities`: Links interaction data to specific deal stages.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into target accounts and prospects.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data and verify contact information automatically.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and automate follow-up workflows for stalled deals.
