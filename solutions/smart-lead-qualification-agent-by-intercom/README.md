# Smart Lead Qualification Agent (Uplizd) - Automate lead scoring and routing via Intercom

## Summary
The Smart Lead Qualification Agent (Uplizd) streamlines your sales pipeline by automatically analyzing incoming Intercom conversations to qualify prospects in real-time. By leveraging AI to extract intent, budget, and authority, this workflow ensures your sales team focuses only on high-intent leads, significantly increasing pipeline velocity and reducing manual data entry.

---

## Demo
![Smart Lead Qualification Agent workflow showing Intercom conversation analysis and CRM routing](image.png)
**Alt text (SEO-ready):** Smart Lead Qualification Agent (Uplizd) workflow for Intercom, automating lead scoring, intent analysis, and CRM routing for sales teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8626a6f9-11a7-5cbf-9de0-a866524e781c)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** intercom, lead qualification, crm, sales pipeline, ai workflow, lead scoring, composio, automation
- This solution bridges the gap between customer support conversations and sales pipeline management by automating the qualification process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual lead triage and improve response times.

- **Sales Development Rep (SDR)**
    - Automatically receives qualified leads in the CRM, allowing for immediate outreach to high-intent prospects.
- **Revenue Operations Manager**
    - Standardizes lead qualification criteria across all inbound Intercom channels to ensure data hygiene.
- **Customer Support Lead**
    - Offloads the burden of identifying sales-ready leads from support tickets, allowing the team to focus on resolution.
- **Growth Marketer**
    - Gains insights into which conversation topics and user behaviors correlate with high-value lead conversion.

---

## Features
- **Real-time Intent Analysis**
    - Automatically parses Intercom chat logs to identify buying signals and urgency using advanced LLM reasoning.
- **Automated Lead Scoring**
    - Assigns dynamic scores to leads based on predefined business rules and conversation context.
- **Seamless CRM Integration**
    - Syncs qualified lead data directly into your CRM via the Composio Toolset to keep records up to date.
- **Intelligent Routing**
    - Routes high-priority leads to the appropriate account executive or sales queue based on lead score and territory.
- **Contextual Summarization**
    - Generates concise conversation summaries for sales reps, providing instant context before they engage with the prospect.

---

## Use Cases
**Inbound Lead Triage**
- Automatically tag and route leads that mention "pricing" or "demo" to the sales team's priority queue.
- Filter out support-only inquiries to ensure the sales pipeline remains focused on revenue-generating opportunities.

**Sales Pipeline Acceleration**
- Update CRM lead status automatically when a prospect expresses clear intent during a chat session.
- Trigger automated follow-up tasks for sales reps when a lead meets specific qualification thresholds.

**Data Hygiene and Enrichment**
- Extract company size, role, and pain points from chat transcripts to enrich existing CRM contact profiles.
- Standardize lead entry formatting to prevent duplicate records and maintain a clean sales database.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Intercom and CRM accounts via the Composio integration portal.
3. Configure the trigger node to monitor incoming conversations from your target channels.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Captures the raw conversation text and metadata from Intercom.
- **Agent**: Analyzes the text against your qualification criteria to determine if the lead is "Sales Ready."
- **Composio Toolset**: Executes the CRM update or lead creation action based on the agent's decision.
- **Chat Output**: Sends a confirmation message or notification to the internal team regarding the lead status.

### 3) Run the Flow
Test the workflow in the Uplizd Playground using these prompts:
- `Analyze the last 5 messages in this chat and determine if the user is a qualified lead.`
- `Extract the company name and job title from this conversation and update the CRM record.`
- `If the user asks for a demo, route this lead to the 'Enterprise Sales' queue in Salesforce.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary decision-maker for lead qualification.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on what constitutes a "qualified" lead for your business.
- Ensure the agent is instructed to output JSON-formatted data for reliable CRM syncing.

### 2) Composio Toolset Node
- Authenticate with your CRM (e.g., Salesforce, HubSpot) using your API key.
- Set the connection scope to allow the agent to read and write lead/contact objects.

### 3) Tool Availability
- `crm_search_contact`: Locate existing records to prevent duplicates.
- `crm_update_lead`: Modify lead status or score fields.
- `crm_create_task`: Assign follow-up actions to specific sales representatives.
- `intercom_get_conversation`: Retrieve full chat history for deep analysis.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](CRM Data Sync Agent) - Synchronize lead data across multiple platforms.
- [../deal-pipeline-manager/README.md](Deal Pipeline Manager) - Manage and track sales pipeline stages effectively.
- [../account-intelligence-reporter-by-leadfeeder/README.md](Account Intelligence Reporter) - Gather deep insights on incoming accounts.
