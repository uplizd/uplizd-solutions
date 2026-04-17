# Lead Qualification Chatbot (Uplizd) - Automate lead screening and routing with conversational AI

## Summary
The Lead Qualification Chatbot (Uplizd) streamlines your sales pipeline by automating the initial engagement, screening, and routing of inbound leads. By leveraging conversational AI to interact with prospects in real-time, this workflow ensures that only high-intent leads reach your sales team, significantly reducing manual data entry and increasing pipeline velocity.

---

## Demo
![Lead Qualification Chatbot workflow interface showing conversational AI screening and CRM routing](image.png)
**Alt text (SEO-ready):** Lead Qualification Chatbot workflow in Uplizd, demonstrating automated lead screening, conversational AI engagement, and CRM data routing for sales teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/354c4ad0-9af2-5ae8-a915-91408e72b2b1)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead qualification, conversational ai, crm, sales pipeline, botstar, lead routing, salesops, automation
- This solution bridges the gap between initial prospect interest and sales-ready opportunities by automating the qualification process.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to optimize their inbound lead management process.

- **Sales Development Representative (SDR)**
    - Focuses on high-value conversations rather than manual screening of unqualified leads.
- **Revenue Operations (RevOps) Manager**
    - Ensures consistent data hygiene and standardized qualification criteria across the entire sales pipeline.
- **Marketing Manager**
    - Improves lead conversion rates by providing immediate, personalized engagement to website visitors.
- **Sales Director**
    - Gains visibility into lead quality and pipeline health through automated, real-time reporting.

---

## Features
- **Automated Lead Screening**
    - Uses conversational AI to ask qualifying questions and score leads based on predefined business criteria.
- **Real-time CRM Integration**
    - Automatically syncs qualified lead data and conversation transcripts directly into your CRM platform.
- **Intelligent Lead Routing**
    - Routes prospects to the appropriate sales representative based on lead score, geography, or company size.
- **Customizable Conversation Logic**
    - Easily adapt the chatbot's tone and qualification flow to match your brand voice and specific product offerings.
- **Instant Notification Alerts**
    - Triggers real-time alerts to the sales team when a high-intent lead completes the qualification process.

---

## Use Cases
**Inbound Lead Triage**
- Automatically filter out non-target prospects by verifying company size and budget during the chat.
- Flag high-intent leads for immediate follow-up by a human representative via Slack or email.

**Pipeline Data Hygiene**
- Ensure all new leads are created in the CRM with standardized fields and accurate contact information.
- Update existing lead records with the latest conversation insights to keep the CRM as the single source of truth.

**Sales Velocity Acceleration**
- Reduce the time-to-lead-response by engaging prospects 24/7, regardless of the sales team's availability.
- Eliminate manual data entry tasks by automating the transfer of lead details from the chatbot to the CRM.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and project to import the workflow.
3. Authenticate your Botstar and CRM accounts within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Captures the initial user message and triggers the qualification sequence.
- **Agent**: Processes the conversation, evaluates answers, and determines the lead's qualification score.
- **Composio Toolset**: Executes CRM actions to create or update lead records based on agent instructions.
- **Chat Output**: Delivers the final response to the prospect, confirming their status or scheduling a meeting.

### 3) Run the Flow
Open the Uplizd Playground and test the following prompts:
- `Hi, I'm interested in your enterprise software solutions and would like to learn about pricing.`
- `Can you tell me if your platform integrates with Salesforce and HubSpot?`
- `I'm a student looking for a free trial for my personal project, is that possible?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary decision-maker for lead qualification.
- Set the system prompt to define your specific qualification criteria (e.g., "Only qualify leads with a budget over $5k").
- Configure the agent to maintain a professional, helpful, and concise tone.
- Enable memory settings to ensure the agent remembers previous answers within the same session.

### 2) Composio Toolset Node
- Provide your CRM API key to enable secure read/write access.
- Define the connection scope to allow the agent to create new leads or update existing contact records.

### 3) Tool Availability
- **CRM Lead Creation**: Capability to generate new records in your CRM.
- **Lead Scoring Engine**: Logic to calculate and append scores to lead profiles.
- **Notification Service**: Ability to send alerts to sales channels when a lead is qualified.

---

## Related Solutions
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages to improve sales conversion.
- [247 Customer Support Chatbot](../247-customer-support-chatbot-by-botstar/README.md) - Provide automated, round-the-clock support for your customers.
