# Lead Qualification Engine (Uplizd) - Automate lead scoring and routing from Formsite submissions

## Summary
The Lead Qualification Engine by Uplizd streamlines your sales pipeline by automatically processing incoming Formsite submissions. This AI-driven workflow evaluates lead quality in real-time, scores prospects based on your custom criteria, and routes them to the appropriate sales representative or CRM pipeline, ensuring your team focuses only on high-intent opportunities.

---

## Demo
![Lead Qualification Engine workflow showing Formsite input, AI scoring agent, and CRM routing output](image.png)
**Alt text (SEO-ready):** Lead Qualification Engine workflow on Uplizd, showing automated Formsite lead scoring, CRM integration, and sales pipeline routing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1f68e0e4-f98d-518f-a4a5-c6548d19e9c3)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** formsite, lead qualification, crm, sales pipeline, lead scoring, data integration, composio, ai workflow
- This solution bridges the gap between raw form data and actionable sales intelligence by automating the qualification lifecycle.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual data entry and improve lead response times.

- **Sales Development Representative (SDR)**
    - Receives pre-qualified leads directly in their dashboard, eliminating the need for manual research.
- **Revenue Operations (RevOps) Manager**
    - Standardizes lead scoring logic across all incoming form traffic to ensure consistent pipeline hygiene.
- **Marketing Manager**
    - Gains immediate insights into which form campaigns are generating the highest quality, sales-ready leads.
- **Sales Director**
    - Increases conversion velocity by ensuring high-intent leads are routed to the right account owner instantly.

---

## Features
- **Automated Lead Scoring**
    - Dynamically assigns scores to incoming Formsite entries based on predefined business rules and prospect intent signals.
- **Intelligent CRM Routing**
    - Automatically creates or updates records in your CRM, assigning leads to the correct owner based on territory or score.
- **Real-time Data Enrichment**
    - Uses the Composio Toolset to fetch additional company context, turning sparse form submissions into complete profiles.
- **Instant Notification Alerts**
    - Triggers high-priority notifications for "Hot" leads, ensuring your sales team never misses a critical opportunity.
- **Customizable Qualification Logic**
    - Easily adjust the Agent's instructions to match your evolving ideal customer profile (ICP) and qualification thresholds.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads with high-budget or enterprise-level job titles for immediate follow-up.
- Filter out spam or low-intent form submissions before they reach your CRM, keeping your database clean.

**Sales Pipeline Acceleration**
- Sync qualified leads directly into your CRM pipeline stages, reducing the time from form submission to first contact.
- Assign "Hot" leads to specific sales queues based on geographic or industry-specific routing rules.

**Data Hygiene & Enrichment**
- Standardize formatting for phone numbers and company names across all incoming Formsite data.
- Append missing firmographic data to leads to provide your sales team with better context before their first outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your Formsite account to the trigger node.
3. Authenticate your CRM and any necessary enrichment tools via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw form submission data from Formsite.
- **Agent**: Analyzes the submission, applies scoring logic, and determines the next action.
- **Composio Toolset**: Executes CRM updates, data enrichment, and routing commands.
- **Chat Output**: Confirms the lead status and logs the routing outcome.

### 3) Run the Flow
Use the Playground to test your qualification logic:
- `Qualify this lead: [Paste Formsite JSON data]`
- `Score this submission based on an enterprise budget of $50k+`
- `Route this lead to the North American sales queue`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your automated sales assistant.
- **Recommended instruction pattern:**
    - "Act as a sales qualification expert; evaluate the lead against the provided ICP criteria."
    - "If the lead score exceeds 80, trigger the 'High Priority' routing protocol."
    - "Always format the output as a clean summary for the sales CRM record."

### 2) Composio Toolset Node
- Provide your API key to enable secure connections to your CRM and enrichment services.
- Set the connection scope to allow the agent to read/write lead objects and perform lookups.

### 3) Tool Availability
- **CRM Connector**: For creating/updating leads and opportunities.
- **Data Enrichment API**: For verifying company size and industry.
- **Notification Service**: For sending alerts to Slack or Email.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Automate deep-dive research on incoming leads.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain consistent lead data across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and track lead progression through your sales stages.
