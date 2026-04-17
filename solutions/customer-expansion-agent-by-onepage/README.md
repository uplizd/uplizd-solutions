# Customer Expansion Agent (Uplizd) - Automate upsell and cross-sell opportunity identification

## Summary
The Customer Expansion Agent is an intelligent Uplizd workflow designed to monitor customer company changes and identify high-value upsell or cross-sell opportunities in real-time. By leveraging the OnePage integration, this agent automates the detection of account growth signals, ensuring your sales and account management teams can proactively engage clients at the perfect moment to maximize customer lifetime value and pipeline velocity.

---

## Demo
![Customer Expansion Agent workflow diagram showing data flow from OnePage to the AI agent for opportunity identification](image.png)
**Alt text (SEO-ready):** Customer Expansion Agent workflow diagram, Uplizd AI automation, OnePage CRM integration, upsell and cross-sell opportunity identification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/96e01328-4443-5790-96a2-2069fd444b0a)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, onepage, upsell, cross-sell, account expansion, pipeline, ai workflow, sales intelligence
- This solution bridges the gap between raw CRM data and actionable revenue growth by automating the identification of expansion signals within your existing customer base.

---

## Who is this for?
This agent is built for revenue-focused teams looking to turn static account data into a dynamic engine for growth.

- **Account Managers**
    - Proactively identify accounts ready for service upgrades or additional product tiers.
- **Sales Operations**
    - Maintain pipeline hygiene by automating the flagging of expansion-ready leads.
- **Customer Success Managers**
    - Detect usage or company-level changes that signal a need for expanded support.
- **Revenue Leaders**
    - Increase net revenue retention by ensuring no expansion opportunity goes unnoticed.

---

## Features
- **Real-time Account Monitoring**
    - Continuously tracks changes in customer profiles via OnePage to detect growth triggers.
- **Intelligent Opportunity Scoring**
    - Uses AI to evaluate account signals and prioritize leads based on expansion potential.
- **Automated CRM Sync**
    - Seamlessly updates account status and notes within OnePage using the Composio Toolset.
- **Context-Aware Insights**
    - Generates personalized outreach summaries based on the specific company changes detected.
- **Pipeline Velocity Optimization**
    - Reduces manual research time, allowing teams to focus on high-conversion expansion conversations.

---

## Use Cases
**Proactive Upsell Identification**
- Automatically flag accounts that have increased their headcount or department size.
- Trigger alerts when a customer reaches a specific usage milestone defined in your CRM.

**Cross-Sell Opportunity Discovery**
- Identify existing customers who are missing key product modules based on their current profile.
- Map account relationships to suggest relevant product bundles that align with recent company pivots.

**Account Health & Retention**
- Monitor for negative sentiment or stalled usage patterns that require immediate intervention.
- Automate the creation of follow-up tasks for account managers when expansion signals are detected.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in the builder.
2. Connect your OnePage account via the Composio Toolset node.
3. Configure your preferred LLM in the Agent node settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to scan accounts.
- **Agent**: Analyzes account data against expansion criteria to determine next steps.
- **Composio Toolset**: Executes read/write operations within OnePage to fetch data and update records.
- **Chat Output**: Delivers the summary of identified opportunities to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Scan all accounts in OnePage and identify those with significant growth in the last 30 days.`
- `Find cross-sell opportunities for our Enterprise plan among current Mid-Market customers.`
- `Summarize the top 5 expansion opportunities identified this week and create follow-up tasks.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized revenue analyst.
- Use a model capable of high-reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction pattern: Focus on identifying growth signals, ignore noise, and prioritize high-value accounts.
- Ensure the agent follows a consistent output format for CRM updates.

### 2) Composio Toolset Node
- Provide your OnePage API key within the Composio configuration.
- Set the connection scope to allow read/write access to account and opportunity objects.

### 3) Tool Availability
- `onepage_get_accounts`: Fetches current customer data.
- `onepage_update_opportunity`: Creates or updates expansion deals.
- `onepage_search_contacts`: Retrieves contact information for targeted outreach.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on target accounts.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with external intelligence.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track sales pipeline stages effectively.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms.
