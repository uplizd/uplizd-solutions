# Lead Qualification Agent (Uplizd) - Automate lead scoring and routing for Dynamics 365

## Summary
The Lead Qualification Agent is an intelligent Uplizd workflow designed to streamline your sales pipeline by automatically evaluating, scoring, and routing incoming leads within Microsoft Dynamics 365. By leveraging the Composio Toolset to interface directly with your CRM, this solution ensures that high-intent prospects are prioritized for sales outreach while maintaining data hygiene, ultimately increasing pipeline velocity and conversion rates for revenue teams.

---

## Demo
![Lead Qualification Agent workflow showing Chat Input, Agent node, Composio Toolset for Dynamics 365, and Chat Output](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow in Uplizd, automating Dynamics 365 lead scoring, routing, and CRM data synchronization for sales teams.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fe1ac1d9-536c-51ae-a901-30b350f6ce47)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, dynamics365, lead qualification, sales pipeline, lead scoring, composio, ai workflow, data sync
- This solution bridges the gap between raw lead generation and CRM readiness by automating the qualification process using AI-driven insights.

---

## Who is this for?
This agent is built for revenue-focused teams looking to reduce manual administrative overhead and improve lead response times.

- **Sales Development Representative (SDR)**
    - Focuses on high-value prospects by automating the initial qualification and data entry steps.
- **Revenue Operations (RevOps) Manager**
    - Ensures consistent lead scoring criteria and data integrity across the entire Dynamics 365 ecosystem.
- **Sales Manager**
    - Gains visibility into lead quality and pipeline health through automated routing and status updates.
- **CRM Administrator**
    - Reduces manual cleanup tasks and ensures that only qualified, enriched leads enter the active sales funnel.

---

## Features
- **Automated Lead Scoring**
    - Evaluates incoming leads against custom business logic to assign priority scores in real-time.
- **Dynamics 365 Integration**
    - Uses the Composio Toolset to perform bi-directional syncs, updating lead status and fields directly in your CRM.
- **Intelligent Routing**
    - Automatically assigns qualified leads to the appropriate account owners based on territory or industry tags.
- **Data Hygiene Enforcement**
    - Validates lead information upon entry to prevent duplicate records and ensure field consistency.
- **Real-time Notification**
    - Triggers instant alerts to sales teams when a high-intent lead is successfully qualified and routed.

---

## Use Cases
**Lead Prioritization**
- Automatically flagging leads with high engagement scores for immediate follow-up by the sales team.
- Filtering out low-intent or incomplete lead submissions to keep the CRM pipeline clean.

**CRM Data Management**
- Syncing lead contact information from web forms directly into Dynamics 365 with automated field mapping.
- Updating lead lifecycle stages (e.g., New to Qualified) based on AI-analyzed prospect interactions.

**Sales Pipeline Optimization**
- Routing qualified leads to specific regional sales queues based on geographic data found in the lead profile.
- Generating summary reports of daily qualified leads for management review within the CRM environment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Agent template from the marketplace.
3. Connect your Dynamics 365 account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or trigger events from your lead sources.
- **Agent**: Processes the data, applies qualification logic, and determines the lead score.
- **Composio Toolset**: Executes CRUD operations within Dynamics 365 to update lead records.
- **Chat Output**: Confirms the qualification status and routing destination to the user.

### 3) Run the Flow
Use the Playground to test your agent with the following prompts:
- `Qualify the latest lead from the web form and update their status in Dynamics 365.`
- `Check the lead score for [Lead Name] and route them to the enterprise sales queue.`
- `Identify and flag any duplicate leads created in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the decision engine for your qualification logic.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on your scoring rubric (e.g., "Assign 10 points for C-suite titles").
- Define the output format to ensure the Composio Toolset receives structured JSON for CRM updates.

### 2) Composio Toolset Node
- Authenticate using your Dynamics 365 API credentials within the Composio dashboard.
- Ensure the connection scope includes `Lead.Read` and `Lead.Write` permissions.

### 3) Tool Availability
- **Lead Management**: Create, update, and search lead records.
- **Account Mapping**: Link leads to existing accounts based on domain matching.
- **Task Creation**: Automatically create follow-up tasks for assigned sales reps.

---

## Related Solutions
- [Account Relationship Builder (Dynamics 365)](../account-relationship-builder-by-dynamics365/README.md) - Automate the mapping and enrichment of account relationships.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms with conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean CRM data through automated deduplication and formatting.
