# Task Automation Coordinator (Uplizd) - Streamline sales follow-ups and task scheduling

## Summary
The Task Automation Coordinator is an intelligent Uplizd workflow designed to synchronize task management and follow-up activities across your CRM ecosystem. By automating the transition from lead engagement to actionable task creation, this solution ensures no opportunity is missed, significantly reducing manual data entry and improving overall pipeline velocity for revenue teams.

---

## Demo
![Task Automation Coordinator workflow dashboard showing automated task scheduling and CRM sync](image.png)
**Alt text (SEO-ready):** Task Automation Coordinator (Uplizd) workflow dashboard showing automated task scheduling, CRM data synchronization, and pipeline management features.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/37d81354-ef7f-56ab-a216-76985c44c7d0)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, task management, pipeline, sales operations, automation, composio, ai workflow
- This solution bridges the gap between CRM activity and execution, providing a centralized hub for automated task orchestration.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual administrative overhead.

- **Sales Operations Manager**
    - Standardizes task creation workflows to ensure consistent follow-up cadences across the entire sales department.
- **Account Executive**
    - Automates the scheduling of post-meeting action items, allowing more time for high-value client interactions.
- **Revenue Operations Lead**
    - Maintains data hygiene by ensuring all CRM tasks are correctly categorized and linked to active opportunities.
- **Sales Development Representative**
    - Accelerates lead qualification by automatically generating follow-up tasks based on real-time engagement signals.

---

## Features
- **Intelligent Task Routing**
    - Automatically assigns tasks to the correct owner based on CRM lead status and territory mapping.
- **Real-time CRM Sync**
    - Leverages the Composio Toolset to push task updates directly into your CRM, ensuring a single source of truth.
- **Automated Follow-up Logic**
    - Triggers timely reminders and calendar events based on custom pipeline stage changes.
- **Context-Aware Prioritization**
    - Uses AI to evaluate task urgency and adjust deadlines based on deal value and interaction history.
- **Seamless Integration Layer**
    - Connects disparate sales tools into a unified automation pipeline without requiring complex custom code.

---

## Use Cases
**Pipeline Management**
- Automatically create "Follow-up" tasks when a deal moves to the "Negotiation" stage.
- Sync task completion status back to the CRM to update deal health metrics in real-time.

**Lead Nurturing**
- Generate personalized outreach tasks for leads that have not been contacted within a 48-hour window.
- Schedule recurring check-in tasks for long-term prospects to maintain engagement momentum.

**Administrative Efficiency**
- Extract action items from meeting notes and convert them into structured CRM tasks instantly.
- Batch-update task priorities across multiple accounts based on upcoming renewal dates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your CRM and productivity tool connections via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific CRM fields and user IDs.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language instructions or trigger events from your CRM.
- **Agent**: Processes the request, determines the necessary follow-up, and prioritizes the task.
- **Composio Toolset**: Executes the API calls to create, update, or delete tasks in your connected CRM.
- **Chat Output**: Confirms the successful creation or update of tasks back to the user.

### 3) Run the Flow
Use the Playground to test your automation with prompts like:
- `Create a follow-up task for the lead in the 'Negotiation' stage for tomorrow at 10 AM.`
- `Sync all pending action items from my meeting notes into the CRM for the Acme Corp account.`
- `List all high-priority tasks due today and update their status to 'In Progress'.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for task prioritization and CRM interaction.
- Use a model capable of structured output (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a sales automation assistant. Analyze the input, identify the CRM entity, and map the action to the appropriate Composio tool."
- Ensure the system prompt includes your organization's specific task naming conventions.

### 2) Composio Toolset Node
- Provide your unique API key within the node configuration.
- Ensure the connection scope includes `write` permissions for Tasks and `read` permissions for Opportunities/Leads.

### 3) Tool Availability
- **CRM Task Manager**: For creating and updating task objects.
- **Calendar Integrator**: For scheduling follow-up events.
- **Opportunity Lookup**: For retrieving context on deal status and owner information.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage pipeline stages and stalled deals.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Sync data across platforms with conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean up CRM data and manage decay.
- [Account Research Agent](../account-research-agent/README.md) - Gather intelligence on target accounts.
