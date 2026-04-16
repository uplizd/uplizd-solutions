# Automated Sales Follow-up Agent (Uplizd) - Persistent AI-driven lead engagement and pipeline velocity

## Summary
The Automated Sales Follow-up Agent leverages advanced AI voice technology to ensure no lead is left behind, automating persistent outreach to prospects. By integrating directly with your CRM, this workflow identifies stalled opportunities and initiates timely, personalized follow-ups, significantly increasing conversion rates and reducing the manual burden on sales teams.

---

## Demo
![Automated Sales Follow-up Agent workflow diagram showing CRM integration and AI voice outreach](image.png)
**Alt text (SEO-ready):** Automated Sales Follow-up Agent workflow diagram showing CRM integration, AI voice outreach, lead nurturing, and Uplizd pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/71393a46-be3e-5a35-a1a5-7a06a6de981a)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** sales, follow-up, voice agent, crm, lead nurturing, pipeline, synthflow, ai workflow  
This solution bridges the gap between CRM data and proactive outreach, ensuring consistent engagement across the entire sales cycle.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach without sacrificing personalization.

* **Sales Development Representative (SDR)**
    * Automates initial outreach and follow-up sequences to focus on high-intent meetings.
* **Account Executive (AE)**
    * Ensures stalled opportunities receive consistent touchpoints to accelerate deal closure.
* **RevOps Manager**
    * Standardizes follow-up cadences across the organization to maintain high data hygiene and pipeline velocity.
* **Sales Manager**
    * Gains visibility into lead engagement patterns and ensures no prospect falls through the cracks.

---

## Features
- **Persistent AI Outreach**
    Automated voice-based follow-ups that adapt to prospect responses for a natural, human-like interaction.
- **CRM Integration**
    Real-time synchronization with your CRM to pull lead status and log all follow-up activity automatically.
- **Intelligent Scheduling**
    Optimizes outreach timing based on prospect behavior and historical engagement data to maximize connection rates.
- **Customizable Scripts**
    Tailor the agent's tone and messaging to align with your brand voice and specific campaign goals.
- **Pipeline Velocity Tracking**
    Automatically updates lead stages in your CRM based on the outcome of the AI-driven follow-up conversation.

---

## Use Cases
**Lead Nurturing**
* Triggering automated follow-ups for leads who have not responded to initial email outreach within 48 hours.
* Re-engaging cold leads with personalized offers based on their previous interaction history.

**Pipeline Acceleration**
* Following up with prospects who have reached the "Proposal Sent" stage but have not moved forward in 5 days.
* Scheduling discovery calls automatically by checking calendar availability via the Composio Toolset.

**Meeting Management**
* Confirming upcoming demo appointments to reduce no-show rates through proactive voice reminders.
* Rescheduling missed appointments by offering alternative time slots directly during the voice conversation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in your workspace.
2. Select your preferred CRM integration (e.g., Salesforce, HubSpot) within the configuration panel.
3. Configure your API keys for the voice provider (Synthflow) and your CRM.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives lead data and trigger signals from your CRM.
* **Agent**: Processes the lead context and determines the optimal follow-up strategy.
* **Composio Toolset**: Executes CRM updates and triggers voice outreach actions.
* **Chat Output**: Logs the interaction summary and final status back to the CRM.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
* `Follow up with lead ID 98765 who hasn't responded to the last proposal.`
* `Check the status of all leads in the 'Discovery' stage and initiate a follow-up call if inactive for 3 days.`
* `Send a reminder to John Doe regarding our scheduled demo tomorrow at 2 PM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a persistent sales assistant. Recommended instruction pattern:
* Act as a professional sales representative with a helpful, non-intrusive tone.
* Prioritize CRM data accuracy when logging call outcomes and follow-up notes.
* Use the Composio Toolset to verify lead status before initiating any voice outreach.

### 2) Composio Toolset Node
Requires a valid API key and connection scope for your CRM (e.g., HubSpot or Salesforce) to read lead objects and write activity logs.

### 3) Tool Availability
* **CRM Read/Write**: Accessing lead contact info and updating deal stages.
* **Calendar Integration**: Checking availability and booking follow-up meetings.
* **Voice Outreach Engine**: Initiating outbound calls via Synthflow API.

---

## Related Solutions
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and stalled deals effectively.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensure multi-platform data consistency and conflict resolution.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score high-value opportunities for your sales team.
