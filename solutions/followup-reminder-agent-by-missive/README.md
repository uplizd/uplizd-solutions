# Follow-up Reminder Agent (Uplizd) - Automated CRM engagement and task tracking

## Summary
The Follow-up Reminder Agent by Missive is an intelligent automation workflow designed to eliminate missed sales opportunities by monitoring communication threads and CRM data. By leveraging the Composio Toolset, this agent identifies pending action items and automatically generates draft follow-up messages, ensuring pipeline velocity and consistent prospect engagement for busy sales and support teams.

---

## Demo
![Follow-up Reminder Agent workflow showing Chat Input, Agent node, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Follow-up Reminder Agent workflow in Uplizd, automating CRM task tracking and email drafts via Missive and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7ae271c3-e6ac-5448-9930-aa8ad57049c5)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, missive, follow-up, pipeline, sales operations, task management, composio, ai workflow
- This solution streamlines the manual burden of tracking sales conversations by syncing communication platforms with CRM task management.

---

## Who is this for?
This agent is designed for revenue-focused teams who need to maintain high-touch relationships without manual oversight.

- **Account Executives**
    - Automate the creation of follow-up drafts after client meetings to ensure no lead goes cold.
- **Sales Development Reps (SDRs)**
    - Prioritize daily outreach by having the agent flag stalled conversations that require immediate attention.
- **Customer Success Managers**
    - Monitor account health by tracking pending action items across multiple communication channels.
- **RevOps Managers**
    - Standardize the follow-up process across the team to improve data hygiene and pipeline conversion rates.

---

## Features
- **Automated Draft Generation**
    - Instantly creates personalized follow-up email drafts based on the context of the last interaction.
- **Intelligent Context Retrieval**
    - Uses the Composio Toolset to pull relevant conversation history from Missive and sync it with your CRM.
- **Proactive Task Monitoring**
    - Scans for unanswered inquiries or stalled deals, alerting users before a follow-up window expires.
- **Seamless CRM Integration**
    - Automatically logs follow-up activities and updates deal stages within your preferred CRM platform.
- **Customizable Tone and Style**
    - Configurable agent instructions allow the AI to match your company’s unique voice and brand guidelines.

---

## Use Cases
**Pipeline Acceleration**
- Automatically trigger follow-up reminders 24 hours after a demo call is logged in the CRM.
- Draft responses for stalled opportunities that haven't seen activity in over 5 business days.

**Customer Relationship Management**
- Sync pending action items from Missive threads directly into CRM task lists.
- Identify and prioritize high-intent leads that require a personalized follow-up touchpoint.

**Operational Efficiency**
- Reduce manual data entry by automating the logging of follow-up interactions.
- Standardize outreach cadences across the entire sales team to ensure consistent prospect experience.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Follow-up Reminder Agent template from the marketplace.
3. Connect your Missive and CRM accounts within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to check for pending tasks.
- **Agent**: Analyzes conversation context and determines the necessary follow-up action.
- **Composio Toolset**: Executes the retrieval of thread data and the creation of CRM drafts.
- **Chat Output**: Delivers the final summary or confirmation that the draft has been created.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Check for any pending follow-ups for deals in the 'Negotiation' stage.`
- `Draft a follow-up email for the last conversation with Acme Corp.`
- `List all stalled opportunities that require a follow-up today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical core, interpreting conversation data and CRM status.
- Use a high-reasoning model (e.g., GPT-4o) for accurate context extraction.
- Instruction: "Analyze the provided thread and CRM data to identify unanswered questions."
- Instruction: "Draft a professional follow-up email that references the specific last interaction."

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure communication with Missive and your CRM.
- Ensure the connection scope includes read/write access to email threads and CRM objects.

### 3) Tool Availability
- **Missive API**: For fetching conversation history and thread metadata.
- **CRM Connector**: For updating deal stages and creating task records.
- **Drafting Tool**: For generating and saving email drafts directly to the platform.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on prospects to personalize outreach.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and identify stalled deals for SalesOps teams.
- [WhatsApp Lead Qualifier](../whats-app-lead-qualifier-by-wati/README.md) — Qualify incoming leads via WhatsApp to streamline the handoff process.
