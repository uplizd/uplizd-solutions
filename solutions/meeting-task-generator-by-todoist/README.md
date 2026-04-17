# Meeting Task Generator (Uplizd) - Automate task creation from meeting notes

## Summary
The Meeting Task Generator is an intelligent Uplizd workflow that parses unstructured meeting transcripts and notes to extract, categorize, and sync action items directly into Todoist. By automating the transition from conversation to execution, this solution eliminates manual data entry, ensures no follow-up is missed, and maintains high pipeline velocity for project-driven teams.

---

## Demo
![Meeting Task Generator workflow showing transcript input, AI extraction, and Todoist task creation](image.png)
**Alt text (SEO-ready):** Meeting Task Generator workflow in Uplizd, automating task extraction from meeting notes to Todoist via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ddf590bd-11ef-5cf9-bea1-e073c98ec36d)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** todoist, task management, meeting notes, productivity, automation, composio, ai workflow, project management
- This solution bridges the gap between collaborative discussions and task execution by integrating AI-driven parsing with your preferred project management tool.

---

## Who is this for?
This workflow is designed for professionals who manage complex projects and need to convert verbal commitments into tracked deliverables.

- **Project Managers**
    - Automatically generate project backlogs from recurring status meetings.
- **Account Executives**
    - Ensure client follow-ups are captured and scheduled immediately after discovery calls.
- **Team Leads**
    - Delegate action items to specific team members without manual ticket creation.
- **Operations Specialists**
    - Maintain a single source of truth for cross-departmental initiatives and deadlines.

---

## Features
- **Intelligent Extraction**
    - Uses advanced LLMs to identify action items, owners, and deadlines from raw meeting transcripts.
- **Todoist Integration**
    - Leverages the Composio Toolset to push tasks directly into your Todoist projects with correct priority levels.
- **Contextual Categorization**
    - Automatically tags tasks based on project themes or meeting types to keep your workspace organized.
- **Real-time Sync**
    - Eliminates the delay between meeting conclusion and task assignment, ensuring immediate accountability.
- **Customizable Formatting**
    - Allows for tailored instruction patterns to match your team's specific task naming conventions and priority schemas.

---

## Use Cases
**Meeting Follow-ups**
- Convert discovery call transcripts into immediate CRM-linked tasks for the sales team.
- Extract action items from internal sprint planning sessions to populate project boards.

**Project Planning**
- Transform brainstorming session notes into structured task lists with assigned owners.
- Sync weekly sync-up outcomes to Todoist to track progress against quarterly goals.

**Administrative Efficiency**
- Automate the creation of recurring maintenance tasks identified during operational reviews.
- Capture ad-hoc requests from stakeholder meetings to prevent task leakage.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Task Generator template from the solution library.
3. Connect your Todoist account via the Composio integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw meeting transcript or summary text.
- **Agent**: Processes the text to extract actionable items, owners, and due dates.
- **Composio Toolset**: Executes the API calls to create tasks in your Todoist workspace.
- **Chat Output**: Confirms the successful creation of tasks and provides a summary of the generated items.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Extract all action items from this transcript and add them to my 'Project Alpha' list in Todoist.`
- `Find tasks for Sarah in these notes and set a due date for next Friday.`
- `Create a high-priority task for every item mentioned in this meeting summary.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized administrative assistant that parses natural language into structured data.
- **Instruction Pattern:**
    - Identify all action items, assignees, and deadlines mentioned in the input text.
    - Map extracted data to the required fields for the Todoist API.
    - Maintain a professional tone and provide a summary of created tasks in the final output.

### 2) Composio Toolset Node
- **API Key:** Ensure your Todoist API key is authenticated within the Composio dashboard.
- **Connection Scope:** Grant the agent permission to create tasks and read project lists to ensure accurate routing.

### 3) Tool Availability
- `todoist_create_task`: Adds new items to your project lists.
- `todoist_get_projects`: Retrieves project IDs for accurate task placement.
- `todoist_update_task`: Allows the agent to modify existing tasks if follow-up meetings update deadlines.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Manage and resolve stale action items across your organization.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and prioritize tasks based on urgency and impact.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex operational workflows across multiple platforms.
