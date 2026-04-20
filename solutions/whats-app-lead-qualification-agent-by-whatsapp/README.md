# WhatsApp Lead Qualification Agent (Uplizd) - Automate lead screening and qualification via WhatsApp

## Summary
The WhatsApp Lead Qualification Agent is an intelligent automation workflow designed to streamline the lead screening process by engaging prospects directly through WhatsApp. By leveraging real-time conversational AI, this solution captures lead intent, validates contact information, and updates your CRM automatically, ensuring that sales teams focus only on high-intent, qualified opportunities while maintaining pipeline velocity.

---

## Demo
![WhatsApp Lead Qualification Agent workflow interface showing automated lead screening and CRM synchronization](image.png)
**Alt text (SEO-ready):** WhatsApp Lead Qualification Agent workflow for automated lead screening, CRM data synchronization, and real-time prospect engagement on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4ecd5bc0-bc3b-53c3-8e50-b8145ccce077)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** whatsapp, lead qualification, crm, sales, conversational ai, lead nurturing, automation, composio

This solution bridges the gap between instant messaging and CRM management, providing a scalable way to handle lead qualification without manual intervention.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual data entry and improve lead response times.

* **Sales Development Representatives (SDRs)**
    * Automate the initial qualification of inbound leads to prioritize high-value prospects.
* **RevOps Managers**
    * Ensure consistent data hygiene by syncing qualified lead information directly into the CRM.
* **Marketing Managers**
    * Improve conversion rates by engaging leads immediately through their preferred communication channel.
* **Small Business Owners**
    * Manage customer inquiries and lead screening 24/7 without the need for a dedicated support team.

---

## Features
- **Automated Lead Screening**
  Engage prospects with intelligent, pre-defined questions to determine lead quality and intent automatically.
- **Real-time CRM Integration**
  Seamlessly push qualified lead data, including contact details and intent scores, into your CRM via the Composio Toolset.
- **Conversational Nurturing**
  Maintain a natural, human-like dialogue with leads to keep them engaged throughout the qualification process.
- **Instant Notification Alerts**
  Trigger real-time alerts to the sales team when a lead meets specific qualification criteria or requests a demo.
- **Data Hygiene & Validation**
  Automatically verify and format lead information before it enters your database to ensure clean, actionable records.

---

## Use Cases
**Lead Qualification & Scoring**
* Automatically categorize leads based on their responses to budget, authority, and timeline questions.
* Assign lead scores in the CRM based on the depth of engagement during the WhatsApp conversation.

**Sales Pipeline Acceleration**
* Schedule discovery calls directly from the WhatsApp interface by checking agent availability in real-time.
* Route qualified leads to the appropriate account executive based on industry or geographic tags.

**Data Enrichment & Sync**
* Update existing CRM records with new contact information or preferences captured during the chat.
* Sync conversation logs to the CRM to provide a single source of truth for the entire sales team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Authenticate your WhatsApp Business API and CRM accounts within the integration settings.
4. Ensure nodes are correctly mapped to your specific API credentials and environment variables.

### 2) Setup the Nodes
* **Chat Input**: Receives incoming WhatsApp messages from prospects.
* **Agent**: Processes intent and determines the next step in the qualification flow.
* **Composio Toolset**: Executes CRM updates and data retrieval tasks based on agent instructions.
* **Chat Output**: Sends personalized, automated responses back to the prospect via WhatsApp.

### 3) Run the Flow
Use the Uplizd Playground to test your flow with these example prompts:
* `Qualify this lead based on their interest in our enterprise pricing plan.`
* `Check if this contact exists in Salesforce and update their status to 'Qualified'.`
* `Send a follow-up message to the lead asking for their preferred time for a discovery call.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the conversational engine, interpreting prospect intent and managing the flow logic.
* Use a system prompt that defines the brand voice and qualification criteria.
* Enable tool-calling capabilities to allow the agent to interact with the CRM.
* Set temperature to 0.3 for consistent, professional lead qualification responses.

### 2) Composio Toolset Node
Connect your CRM (e.g., Salesforce, HubSpot) and WhatsApp Business API via the Composio Toolset. Ensure the API key has sufficient scope to read and write lead objects.

### 3) Tool Availability
* **CRM Search/Create**: Find existing leads or create new entries.
* **Calendar Integration**: Check availability and book discovery meetings.
* **WhatsApp Messaging**: Send templates and free-form responses to prospects.

---

## Related Solutions
* [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automated follow-up sequences for leads.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Multi-platform data synchronization and conflict resolution.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage pipeline stages and stalled deal follow-ups.
* [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) - Route customer support inquiries from WhatsApp.
