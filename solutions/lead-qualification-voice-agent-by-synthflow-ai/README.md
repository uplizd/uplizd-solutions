# Lead Qualification Voice Agent (Uplizd) - Automated AI-driven lead screening and qualification

## Summary
The Lead Qualification Voice Agent by Synthflow AI automates the initial engagement and screening of inbound leads through intelligent, real-time voice conversations. By leveraging advanced AI to handle discovery calls, this solution ensures that only high-intent prospects reach your sales team, significantly increasing pipeline velocity and reducing manual administrative overhead for BDRs.

---

## Demo
![Lead Qualification Voice Agent workflow diagram showing voice input processing and CRM synchronization](image.png)
**Alt text (SEO-ready):** Lead Qualification Voice Agent workflow diagram showing voice input processing, AI-driven lead screening, and CRM synchronization via Uplizd and Synthflow AI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d87f163a-9127-5eb5-aa2f-448d9ed63ba0)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead qualification, voice agent, synthflow, crm, sales ops, pipeline, ai workflow, composio
- This solution bridges the gap between raw lead generation and sales readiness by automating the voice-based qualification process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach without increasing headcount.

- **Sales Development Representatives (SDRs)**
    - Offload repetitive discovery calls to focus exclusively on high-value, qualified opportunities.
- **Revenue Operations (RevOps) Managers**
    - Standardize the qualification process across all inbound channels to ensure consistent data quality.
- **Growth Marketers**
    - Improve lead-to-opportunity conversion rates by ensuring immediate engagement with new prospects.
- **Sales Managers**
    - Gain real-time visibility into lead intent and pipeline health through automated CRM logging.

---

## Features
- **Intelligent Voice Interaction**
    - Uses Synthflow AI to conduct natural, human-like discovery calls that adapt to prospect responses in real-time.
- **Automated CRM Sync**
    - Seamlessly updates lead status, contact information, and qualification notes directly in your CRM via the Composio Toolset.
- **Real-time Lead Scoring**
    - Dynamically assigns scores to leads based on conversation sentiment and specific qualification criteria.
- **Customizable Qualification Scripts**
    - Easily configure the agent’s logic to match your specific industry discovery questions and brand voice.
- **Instant Follow-up Triggers**
    - Automatically schedules meetings or sends personalized follow-up emails based on the outcome of the voice call.

---

## Use Cases
**Inbound Lead Screening**
- Automatically call new web form leads within minutes to verify interest and capture budget details.
- Filter out unqualified leads early, preventing sales teams from wasting time on low-intent prospects.

**Pipeline Acceleration**
- Update lead stages in your CRM automatically based on the voice agent's qualification summary.
- Flag high-priority leads for immediate human intervention when specific buying signals are detected.

**Data Hygiene & Enrichment**
- Verify contact details and company size during the conversation to ensure CRM records remain accurate.
- Append qualitative notes from the voice transcript to the lead profile for better context during sales handoffs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your Synthflow AI and CRM accounts within the integration settings.
4. Ensure nodes are correctly mapped to your specific API credentials and field requirements.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event from your lead source or CRM.
- **Agent**: Processes the lead data and executes the qualification logic using the Synthflow voice model.
- **Composio Toolset**: Connects the agent to your CRM to perform lookups and update lead records.
- **Chat Output**: Logs the final qualification report and notifies the sales team via Slack or email.

### 3) Run the Flow
Use the Playground to test your agent's responses:
- `Qualify this new lead: John Doe, interested in enterprise pricing.`
- `Update the CRM status for lead ID 98765 based on the latest voice transcript.`
- `Summarize the qualification call for the lead from the last 30 minutes.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a professional sales assistant.
- Maintain a helpful, inquisitive, and professional tone.
- Follow the qualification script strictly while allowing for natural conversational flow.
- Ensure all key data points (budget, timeline, authority) are captured before concluding the call.

### 2) Composio Toolset Node
- Requires an active API key for your CRM (e.g., Salesforce, HubSpot).
- Ensure the connection scope includes read/write access to Leads, Contacts, and Opportunities.

### 3) Tool Availability
- **CRM Search**: Locate existing records to prevent duplicate entries.
- **Lead Update**: Modify lead fields based on conversation outcomes.
- **Calendar Integration**: Schedule discovery calls directly into the assigned AE's calendar.
- **Notification Service**: Alert the sales team when a lead is marked as "Qualified."

---

## Related Solutions
- [../whats-app-lead-qualifier-by-wati/README.md](../whats-app-lead-qualifier-by-wati/README.md) - Automate lead qualification via WhatsApp messaging.
- [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data to improve qualification accuracy.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms for unified reporting.
