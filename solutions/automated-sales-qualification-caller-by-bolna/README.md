# Automated Sales Qualification Caller (Uplizd) - Scale lead qualification with intelligent voice AI

## Summary
The Automated Sales Qualification Caller (Uplizd) leverages advanced voice AI to engage, screen, and qualify inbound leads in real-time. By automating the initial discovery phase, this workflow ensures that sales teams focus exclusively on high-intent prospects, significantly increasing pipeline velocity and improving lead hygiene across your CRM.

---

## Demo
![Automated Sales Qualification Caller workflow diagram showing Bolna voice agent integration with CRM tools](image.png)
**Alt text (SEO-ready):** Automated Sales Qualification Caller workflow using Uplizd, Bolna voice AI, and CRM integrations for real-time lead screening.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/e3e0fce0-4c71-519e-b1f1-4e685545adbf)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales, voice-ai, bolna, lead-qualification, crm, pipeline, automation, composio
- This solution bridges the gap between raw lead generation and sales readiness by using voice AI to perform automated discovery calls.

---

## Who is this for?
This solution is designed for revenue teams looking to eliminate manual discovery bottlenecks and improve lead conversion rates.

- **Sales Development Representative (SDR)**
    - Automatically offloads repetitive discovery calls, allowing focus on high-value closing activities.
- **Revenue Operations Manager**
    - Standardizes the qualification process across all incoming leads to ensure consistent data quality.
- **Sales Manager**
    - Gains immediate visibility into lead intent and pipeline health through automated call summaries.
- **Growth Marketer**
    - Increases ROI on lead generation campaigns by ensuring only qualified prospects reach the sales team.

---

## Features
- **Intelligent Voice Interaction**
    - Uses Bolna AI to conduct natural, human-like conversations that adapt to prospect responses in real-time.
- **Automated CRM Sync**
    - Seamlessly pushes qualification data, call transcripts, and sentiment scores directly into your CRM.
- **Dynamic Lead Scoring**
    - Updates lead priority fields based on the outcome of the voice conversation and predefined qualification criteria.
- **Real-time Triage**
    - Instantly routes high-intent leads to the appropriate account executive via Slack or email notifications.
- **Composio Toolset Integration**
    - Connects the voice agent to your entire stack, enabling lookups and updates across multiple platforms during the call.

---

## Use Cases
**Lead Screening & Routing**
- Automatically verify contact information and budget availability during the first touchpoint.
- Route "Ready to Buy" leads directly to the calendar of a senior account executive.

**Pipeline Hygiene**
- Update lead status to "Disqualified" for non-responsive or out-of-market prospects to keep the CRM clean.
- Log detailed call summaries to ensure historical data is preserved for future nurturing campaigns.

**Sales Velocity Optimization**
- Reduce the time-to-contact for new inbound leads from hours to seconds.
- Ensure all discovery questions are asked consistently, regardless of the volume of incoming traffic.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the `automated-sales-qualification-caller-by-bolna` template from the library.
3. Configure your Bolna API credentials and CRM connection within the project settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead trigger (e.g., new form submission or CRM entry).
- **Agent**: Processes the lead context and manages the voice conversation flow using the Bolna engine.
- **Composio Toolset**: Executes CRM updates, lead lookups, and calendar scheduling based on agent instructions.
- **Chat Output**: Delivers the final call summary and status update to your notification channels.

### 3) Run the Flow
Use the Playground to test your voice agent with the following prompts:
- `Initiate a qualification call for the latest lead in the 'New' pipeline stage.`
- `Verify the budget and timeline for the prospect identified as 'High Intent'.`
- `Summarize the last 5 qualification calls and update the CRM lead status accordingly.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary voice interface and decision-maker.
- **Instruction Pattern:**
    - Maintain a professional, consultative tone while adhering to the discovery script.
    - Extract key qualification data points (Budget, Authority, Need, Timeline) from the conversation.
    - Trigger CRM update tools immediately upon identifying a qualified prospect.

### 2) Composio Toolset Node
- Provide your API key to enable secure access to your CRM and communication platforms.
- Set the connection scope to allow the agent to read lead details and write qualification notes.

### 3) Tool Availability
- **CRM Connector**: For reading lead profiles and updating status fields.
- **Calendar API**: For booking discovery meetings directly into AE calendars.
- **Notification Service**: For alerting sales teams when a lead is successfully qualified.

---

## Related Solutions
- [WhatsApp Lead Qualifier (by Wati)](../whats-app-lead-qualifier-by-wati/README.md) — Automate lead qualification via WhatsApp messaging.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage and track your sales pipeline stages effectively.
- [Account Research Agent (by ZoomInfo)](../account-research-agent-by-zoominfo/README.md) — Enrich lead data with deep account intelligence.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your CRM data consistent across multiple platforms.
