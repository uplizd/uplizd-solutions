# WhatsApp Lead Qualifier (Uplizd) - Automate lead qualification and routing via WhatsApp

## Summary
The WhatsApp Lead Qualifier by TimelinesAI is an intelligent Uplizd workflow that automates the screening and categorization of incoming leads directly within your WhatsApp conversations. By leveraging AI to analyze prospect intent and urgency in real-time, this solution ensures that high-value leads are prioritized and routed to the correct sales representative, significantly reducing response times and increasing pipeline velocity.

---

## Demo
![WhatsApp Lead Qualifier workflow diagram showing message intake, AI analysis, and CRM routing](image.png)
**Alt text (SEO-ready):** WhatsApp Lead Qualifier workflow diagram showing message intake, AI analysis, and CRM routing via Uplizd and TimelinesAI.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/15dcf985-2121-5187-9597-d3a38b017db9)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** whatsapp, lead qualification, crm, sales, pipeline, ai workflow, composio, lead routing  
This solution streamlines the sales funnel by transforming unstructured WhatsApp messages into actionable, qualified CRM opportunities.

---

## Who is this for?
This solution is designed for revenue teams looking to eliminate manual lead entry and ensure no prospect is left behind.

* **Sales Development Representative (SDR)**
    * Focuses on high-intent leads while the AI handles initial screening and data entry.
* **Sales Operations Manager**
    * Maintains data hygiene by ensuring all WhatsApp-sourced leads follow a standardized qualification process.
* **Small Business Owner**
    * Provides 24/7 automated engagement to capture and qualify leads even outside of standard business hours.
* **Account Executive**
    * Receives pre-qualified leads directly in the CRM, allowing for faster discovery calls and improved conversion rates.

---

## Features
- **Real-time Intent Analysis**
  Uses advanced LLMs to detect buying signals, urgency, and product interest within incoming WhatsApp messages.
- **Automated CRM Routing**
  Seamlessly maps qualified leads to your CRM, ensuring that contact information and conversation summaries are always up to date.
- **Custom Qualification Logic**
  Configurable criteria that allow the agent to filter leads based on budget, timeline, or specific service requirements.
- **Instant Response Generation**
  Drafts personalized, context-aware replies to keep prospects engaged while the qualification process completes in the background.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to bridge the gap between TimelinesAI and your existing sales stack, ensuring secure and reliable data synchronization.

---

## Use Cases
**Lead Screening & Prioritization**
* Automatically tagging leads as "Hot," "Warm," or "Cold" based on their initial WhatsApp inquiry.
* Flagging urgent support or sales requests for immediate human intervention.

**Automated CRM Data Sync**
* Creating or updating contact records in your CRM automatically when a new lead is identified.
* Logging full conversation transcripts to the lead profile for historical context.

**Sales Pipeline Acceleration**
* Scheduling discovery calls directly through the chat interface when a lead meets specific qualification thresholds.
* Sending automated follow-up reminders to sales reps when a lead has been qualified but not yet contacted.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the WhatsApp Lead Qualifier template from the solution library.
3. Connect your TimelinesAI and CRM accounts via the integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives raw WhatsApp messages from the TimelinesAI webhook.
* **Agent:** Analyzes the message content against your predefined qualification criteria.
* **Composio Toolset:** Executes CRM updates and lead tagging actions.
* **Chat Output:** Sends a confirmation or follow-up message back to the prospect.

### 3) Run the Flow
Open the Uplizd Playground and test with these prompts:
* `Analyze the following message for buying intent: "Hi, I'm interested in your enterprise pricing for 50 users."`
* `Qualify this lead based on the conversation history and update the CRM status to 'Qualified'.`
* `Draft a professional response to this lead acknowledging their request and asking for their preferred time for a demo.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the qualification process.
* Set the system prompt to define your specific "Ideal Customer Profile" (ICP).
* Use a temperature setting of 0.2–0.3 for consistent, objective qualification.
* Enable tool-calling capabilities to allow the agent to interact with your CRM API.

### 2) Composio Toolset Node
* Provide your API key within the Composio node configuration.
* Define the connection scope to include read/write access for your CRM and TimelinesAI.

### 3) Tool Availability
* **CRM Connector:** For creating/updating leads and opportunities.
* **TimelinesAI API:** For sending outbound messages and retrieving conversation history.
* **Data Parser:** For extracting email addresses, phone numbers, and company names from chat text.

---

## Related Solutions
* [WhatsApp Lead Nurturing Agent](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Automate follow-ups and engagement for existing WhatsApp leads.
* [WhatsApp Support Triage Agent](../whats-app-support-triage-agent-by-wati/README.md) — Categorize and route incoming support tickets from WhatsApp.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your customer data consistent across multiple platforms and tools.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage sales stages and track deal velocity effectively.
