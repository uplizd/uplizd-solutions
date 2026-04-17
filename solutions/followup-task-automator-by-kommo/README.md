# Follow-up Task Automator (Uplizd) - Intelligent CRM task scheduling and automated follow-up management

## Summary
The Follow-up Task Automator is an AI-driven workflow designed to eliminate manual CRM tracking by automatically identifying, scheduling, and reminding teams of pending follow-up actions. By leveraging the Composio Toolset to interface directly with your CRM, this solution ensures that no lead or client interaction falls through the cracks, significantly increasing pipeline velocity and improving overall sales hygiene.

---

## Demo
![Follow-up Task Automator workflow interface showing automated CRM task creation and notification triggers](image.png)
**Alt text (SEO-ready):** Follow-up Task Automator workflow in Uplizd for automated CRM task management, sales follow-up scheduling, and pipeline hygiene.

---

## 🚀 Run on Uplizd
[Launch 'Follow-up Task Automator'](https://uplizd.ai/solutions/761a4610-244c-5638-90ba-d2eed20b9f09)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, kommo, task management, sales follow-up, pipeline, automation, composio, ai workflow
- This solution bridges the gap between customer interactions and actionable CRM tasks to ensure consistent follow-through.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to standardize their outreach and task management processes.

- **Sales Representatives**
    - Automate the creation of follow-up tasks immediately after client meetings to maintain momentum.
- **Sales Operations Managers**
    - Enforce standardized follow-up cadences across the team to ensure consistent lead engagement.
- **Account Managers**
    - Receive proactive reminders for account check-ins, reducing the risk of churn due to inactivity.
- **Business Development Managers**
    - Streamline the transition from initial outreach to scheduled follow-up without manual data entry.

---

## Features
- **Automated Task Creation**
  Instantly generates follow-up tasks in Kommo based on conversation summaries or meeting notes.
- **Intelligent Scheduling**
  Calculates optimal follow-up windows based on lead priority and historical engagement data.
- **CRM Synchronization**
  Ensures real-time data parity between the AI agent and your Kommo CRM environment via the Composio Toolset.
- **Proactive Notifications**
  Triggers alerts for upcoming or overdue tasks to keep the sales team focused on high-priority actions.
- **Contextual Enrichment**
  Attaches relevant interaction context to every task, providing reps with the necessary background before they reach out.

---

## Use Cases
**Pipeline Acceleration**
- Automatically create follow-up tasks for "Stalled" deals to ensure immediate re-engagement.
- Sync meeting outcomes directly to CRM task fields to keep deal history accurate and up-to-date.

**Lead Nurturing**
- Schedule automated follow-up reminders for cold leads that have shown recent website or email activity.
- Assign follow-up tasks to specific team members based on lead ownership and current capacity.

**Customer Success**
- Generate recurring check-in tasks for high-value accounts to maintain long-term relationship health.
- Create urgent follow-up tasks when negative sentiment is detected in recent customer communications.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the "Follow-up Task Automator" solution.
2. Click "Import" to load the workflow into your workspace.
3. Authenticate your Kommo account within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request to initiate a follow-up task.
- **Agent**: Processes the context, interprets the required follow-up action, and determines the task parameters.
- **Composio Toolset**: Executes the API calls to create or update tasks within your Kommo CRM.
- **Chat Output**: Confirms the successful creation of the task and provides a summary of the scheduled follow-up.

### 3) Run the Flow
Use the Playground to test the automation with these prompts:
- `Create a follow-up task for John Doe at Acme Corp for next Tuesday regarding the contract renewal.`
- `Review the last meeting notes for the pending deal with TechFlow and schedule a follow-up call.`
- `Set a high-priority follow-up task for the account manager to check in on the recent implementation issue.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic layer, parsing natural language into structured CRM actions.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on identifying task deadlines and priority levels.
- Ensure the system prompt includes the current date to accurately calculate "next Tuesday" or "in 3 days" timeframes.

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure communication with the Kommo CRM.
- Set the connection scope to include `tasks:write` and `leads:read` to allow the agent to fetch deal info and create tasks.

### 3) Tool Availability
- **Kommo Task API**: For creating, updating, and listing follow-up tasks.
- **Kommo Lead API**: For retrieving deal status and customer contact information.
- **Date/Time Utility**: For calculating precise follow-up dates based on relative natural language inputs.

---

## Related Solutions
- [WhatsApp Lead Qualifier by Kommo](../whats-app-lead-qualifier-by-wati/README.md) - Automate lead qualification and initial outreach via WhatsApp.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent data across multiple CRM platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and optimize sales velocity.
