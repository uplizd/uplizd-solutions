# Connection Follow-up Scheduler (Uplizd) - Automated relationship management for high-velocity sales

## Summary
The Connection Follow-up Scheduler is an intelligent Uplizd workflow designed to automate the tracking and scheduling of professional follow-ups. By leveraging AI to analyze interaction history and set timely reminders, this solution ensures that no lead falls through the cracks, significantly increasing pipeline velocity and improving relationship hygiene for sales and business development teams.

---

## Demo
![Connection Follow-up Scheduler workflow diagram showing the integration between Leadoku, AI agent logic, and calendar scheduling tools](image.png)
**Alt text (SEO-ready):** Uplizd Connection Follow-up Scheduler workflow diagram, automated sales follow-up system, CRM integration, and AI-powered lead nurturing pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7297a6d9-65c4-58c0-8a4c-160f485f46d6)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, leadoku, sales, follow-up, pipeline, relationship management, ai workflow, composio  
This solution bridges the gap between initial outreach and long-term relationship maintenance by automating the scheduling of critical touchpoints.

---

## Who is this for?
This solution is designed for professionals who need to maintain consistent engagement with a growing network of prospects and clients.

*   **Sales Development Representative (SDR)**
    *   Automates the scheduling of follow-up tasks to ensure no prospect is forgotten after the initial outreach.
*   **Account Executive (AE)**
    *   Maintains high-touch relationships by surfacing pending follow-ups directly within the workflow.
*   **Growth Marketer**
    *   Ensures that leads generated from campaigns are nurtured through timely, automated communication sequences.
*   **Customer Success Manager**
    *   Tracks interaction cadence to proactively reach out to clients before renewals or check-ins are due.

---

## Features
- **Automated Trigger Logic**
    Detects new connections or interaction events via Leadoku and initiates the follow-up sequence automatically.
- **Intelligent Scheduling**
    Utilizes AI to suggest optimal follow-up windows based on previous interaction patterns and lead priority.
- **Composio Toolset Integration**
    Seamlessly connects with your calendar and CRM tools to log activities and create reminders without manual entry.
- **Real-time Sync**
    Ensures that all follow-up data is updated across your sales stack, maintaining a single source of truth.
- **Customizable Outreach Templates**
    Generates personalized follow-up prompts that the agent can execute or suggest for human review.

---

## Use Cases
**Lead Nurturing**
*   Scheduling automated follow-ups for leads who haven't responded to the initial outreach within 48 hours.
*   Prioritizing high-intent prospects for immediate follow-up based on engagement signals.

**Meeting Management**
*   Setting post-meeting follow-up reminders to ensure action items are delivered on time.
*   Automating the scheduling of "check-in" calls for long-term relationship maintenance.

**Pipeline Hygiene**
*   Cleaning up stale follow-up tasks by re-assigning or archiving outdated connection requests.
*   Synchronizing follow-up status across multiple platforms to prevent duplicate outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Connection Follow-up Scheduler JSON template.
3. Connect your Leadoku and CRM accounts via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the lead data or trigger event from Leadoku.
*   **Agent**: Analyzes the lead's status and determines the appropriate follow-up action.
*   **Composio Toolset**: Executes the calendar event creation or CRM update.
*   **Chat Output**: Confirms the scheduled follow-up or provides a summary of the action taken.

### 3) Run the Flow
Open the Playground and test with these prompts:
* `Check for new connections in Leadoku and schedule a follow-up for any lead added in the last 24 hours.`
* `Find all pending follow-ups for high-priority leads and create calendar reminders for tomorrow morning.`
* `Summarize my follow-up activity for the week and identify any leads that have been neglected for more than 5 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your digital sales assistant, responsible for interpreting lead intent and managing the follow-up cadence.
*   Prioritize leads based on the "last contacted" field.
*   Maintain a professional and helpful tone in all generated follow-up suggestions.
*   Always verify if a follow-up already exists before creating a duplicate entry.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Leadoku and CRM API keys are active in your Composio account.
*   **Connection Scope**: Grant read/write access to your calendar and CRM contact modules to allow the agent to read lead data and write follow-up tasks.

### 3) Tool Availability
*   **CRM Connector**: For updating lead status and logging interaction history.
*   **Calendar API**: For creating and managing follow-up reminders.
*   **Leadoku Integration**: For real-time monitoring of new connections and lead signals.

---

## Related Solutions
*   [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects before your scheduled follow-up.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage the broader sales pipeline and track deal stages alongside your follow-ups.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your contact data synchronized across all platforms to ensure follow-ups are always accurate.
