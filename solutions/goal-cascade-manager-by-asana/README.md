# Goal Cascade Manager (Uplizd) - Automate objective alignment and team goal breakdown

## Summary
The Goal Cascade Manager is an intelligent Uplizd workflow that automatically decomposes high-level company objectives into actionable team and individual goals within Asana. By leveraging AI to map strategic initiatives to specific tasks, this solution ensures organizational alignment, eliminates manual planning bottlenecks, and provides a single source of truth for progress tracking across all levels of the enterprise.

---

## Demo
![Goal Cascade Manager workflow interface showing objective decomposition from company level to individual tasks in Asana](image.png)
**Alt text (SEO-ready):** Goal Cascade Manager Uplizd workflow for automated Asana objective alignment and team goal decomposition.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ea916a2d-fa4a-5a77-8943-1aad1ffaa88f)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** asana, goal management, okr, strategic alignment, workflow automation, project management, composio, ai planning
- This solution bridges the gap between high-level corporate strategy and daily execution by automating the cascade of objectives across your Asana workspace.

---

## Who is this for?
This solution is designed for leadership and operations teams focused on maintaining organizational focus and execution velocity.

- **Operations Managers**
    - Streamline the quarterly planning process by automating the creation of sub-tasks and team-level objectives.
- **Project Leads**
    - Ensure every team member understands how their daily work contributes to the broader company mission.
- **Executive Leadership**
    - Gain real-time visibility into goal progression and identify misaligned initiatives before they impact performance.
- **HR & People Ops**
    - Facilitate transparent performance management by linking individual KPIs directly to verified company goals.

---

## Features
- **Automated Goal Decomposition**
    - Uses AI to parse high-level company objectives and generate granular, actionable team-level goals in Asana.
- **Real-time Synchronization**
    - Maintains a live connection between strategy documents and project management boards via the Composio Toolset.
- **Context-Aware Mapping**
    - Intelligently assigns tasks to the correct team members based on historical project data and current capacity.
- **Progress Tracking Integration**
    - Automatically updates parent goal status in Asana as individual sub-tasks reach completion.
- **Strategic Alignment Audit**
    - Identifies orphaned tasks or unassigned objectives that lack a clear connection to company-wide priorities.

---

## Use Cases
**Strategic Planning**
- Automatically convert annual company OKRs into quarterly team-specific milestones.
- Map cross-departmental initiatives to shared project boards to ensure collaborative alignment.

**Performance Execution**
- Break down complex product launches into individual sprint goals assigned to specific engineering squads.
- Sync personal development goals with team-wide performance targets to ensure professional growth aligns with business needs.

**Operational Hygiene**
- Identify and flag "ghost" tasks that are not linked to any active company objective.
- Generate automated status reports that summarize goal completion rates for department heads.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Goal Cascade Manager template file provided in this repository.
3. Authenticate your Asana account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the high-level objective or strategic document text.
- **Agent**: Processes the input to determine the necessary breakdown and task hierarchy.
- **Composio Toolset**: Executes the creation and linking of tasks within the Asana API.
- **Chat Output**: Returns a summary of the created goal structure and confirmation of successful sync.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Break down the 'Q3 Revenue Growth' objective into 5 actionable team goals for the Sales and Marketing departments.`
- `Create a project structure in Asana for the 'New Feature Rollout' goal, assigning tasks to the Product team.`
- `List all unaligned tasks in the 'Engineering' project and suggest an objective they should be mapped to.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the strategic architect for your organization.
- **Instruction Pattern:**
    - Act as an expert Operations Strategist specializing in OKR frameworks.
    - Analyze input text to identify key deliverables, timelines, and responsible stakeholders.
    - Format output as structured API calls for the Composio Toolset to ensure Asana compatibility.

### 2) Composio Toolset Node
- **API Key:** Provide your Asana Personal Access Token or OAuth credentials.
- **Connection Scope:** Ensure the agent has 'Read/Write' access to your target Workspaces and Projects.

### 3) Tool Availability
- **Asana Create Task**: Generates the individual sub-tasks for team members.
- **Asana Update Project**: Modifies project metadata to reflect new goal hierarchies.
- **Asana Search**: Locates existing goals to prevent duplicate task creation.
- **Asana Get User**: Validates team member availability and assignment permissions.

---

## Related Solutions
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Manage complex client hierarchies and relationship data.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Automate repetitive project management and task routing.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track operational health and goal-related metrics.
