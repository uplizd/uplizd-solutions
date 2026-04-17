# Apollo Smart Task Creator (Uplizd) - Automate contextual sales follow-ups based on deal behavior

## Summary
The Apollo Smart Task Creator is an intelligent Uplizd workflow that automatically generates high-context follow-up tasks for sales representatives by analyzing deal stages and prospect engagement signals. By integrating Apollo.io data with automated task management, this solution eliminates manual data entry, ensures no lead falls through the cracks, and significantly increases pipeline velocity for RevOps and sales teams.

---

## Demo
![Apollo Smart Task Creator workflow diagram showing Apollo.io data ingestion, AI task generation, and CRM synchronization](image.png)
**Alt text (SEO-ready):** Apollo Smart Task Creator workflow diagram showing Apollo.io data ingestion, AI task generation, and CRM synchronization within the Uplizd platform.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d4520736-a22f-584b-b3d8-328329f069c0)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** apollo, crm, sales, task management, pipeline, lead nurturing, composio, ai workflow  
This solution bridges the gap between prospect intelligence and actionable sales tasks to streamline daily workflows.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to optimize their outreach efficiency and maintain high-quality pipeline hygiene.

- **Sales Development Representative (SDR)**
    - Automates the creation of daily follow-up tasks based on real-time prospect engagement.
- **Account Executive (AE)**
    - Ensures that high-intent deals receive immediate attention without manual administrative overhead.
- **RevOps Manager**
    - Standardizes the follow-up process across the team to improve conversion rates and data consistency.
- **Sales Manager**
    - Gains visibility into team activity by ensuring every interaction is backed by a tracked, contextual task.

---

## Features
- **Contextual Task Generation**
  Uses AI to analyze Apollo.io prospect data and draft specific, actionable follow-up tasks tailored to the deal stage.
- **Automated CRM Sync**
  Leverages the Composio Toolset to push generated tasks directly into your CRM, ensuring your system of record is always up to date.
- **Behavior-Driven Triggers**
  Identifies key engagement signals from Apollo to prioritize tasks that require immediate human intervention.
- **Standardized Outreach Templates**
  Ensures that every generated task follows your team's best practices for tone, timing, and value proposition.
- **Real-Time Pipeline Updates**
  Automatically updates deal notes and status fields in response to task completion, keeping the entire sales cycle moving.

---

## Use Cases
**Lead Qualification**
- Automatically create a "Discovery Call" task when a lead hits a specific engagement score in Apollo.
- Generate a research task for prospects who have opened multiple emails but haven't booked a meeting.

**Pipeline Acceleration**
- Create a "Follow-up" task for stalled deals that haven't seen activity in the last 7 days.
- Trigger a "Contract Review" task immediately after a prospect moves to the negotiation stage.

**Administrative Hygiene**
- Batch create tasks for all new inbound leads to ensure a 5-minute response time.
- Automatically archive or re-assign tasks for prospects that have been marked as "Disqualified" in Apollo.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Apollo Smart Task Creator template from the marketplace.
3. Configure your Apollo.io and CRM API credentials within the integration settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to initiate task creation.
- **Agent**: Processes prospect data and determines the appropriate follow-up action.
- **Composio Toolset**: Executes the API calls to Apollo.io and your CRM to create the task.
- **Chat Output**: Confirms the task creation and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Create a follow-up task for all leads in the 'Discovery' stage who haven't been contacted in 3 days.`
- `Analyze the latest Apollo engagement data and generate tasks for high-intent prospects.`
- `Sync the new follow-up tasks for the 'Enterprise' segment to my Salesforce instance.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that translates prospect behavior into sales tasks.
- Instruction: "Analyze the provided Apollo.io data for prospect engagement signals."
- Instruction: "Determine the most relevant follow-up action based on the current deal stage."
- Instruction: "Format the task description to include the prospect's recent interactions and suggested talking points."

### 2) Composio Toolset Node
- **API Key**: Ensure your Apollo.io and CRM API keys are active in the Composio dashboard.
- **Connection Scope**: Grant read/write access to your CRM's Task and Opportunity objects and Apollo's contact data.

### 3) Tool Availability
- `apollo_get_contacts`: Fetches prospect engagement metrics.
- `crm_create_task`: Creates the follow-up record in your CRM.
- `crm_update_deal`: Updates deal stage or notes based on task creation.
- `apollo_list_activities`: Retrieves recent email/call history for context.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate prospect research and company intelligence gathering.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage deal stages and follow-up cadences for sales teams.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize prospect data across multiple platforms and CRMs.
