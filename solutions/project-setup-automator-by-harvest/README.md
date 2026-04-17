# Project Setup Automator (Uplizd) - Streamline project initiation and resource allocation

## Summary
The Project Setup Automator by Harvest is an intelligent workflow designed to eliminate manual administrative overhead when launching new client engagements. By automating the creation of projects, task lists, and team assignments, this Uplizd AI solution ensures project managers maintain consistent operational standards, improves data accuracy across Harvest, and significantly accelerates the transition from sales close to project execution.

---

## Demo
![Project Setup Automator workflow interface showing automated task creation and team assignment in Harvest](image.png)
**Alt text (SEO-ready):** Project Setup Automator (Uplizd) workflow interface showing automated task creation and team assignment in Harvest for streamlined project management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/c2453944-d2e5-53dd-b36b-cb7e2e0d940f)

---

## Category
**Primary category:** Operations Automation
**Secondary tags:** harvest, project management, workflow automation, resource allocation, onboarding, composio, ai workflow, productivity.
This solution bridges the gap between project planning and execution by automating repetitive setup tasks within the Harvest ecosystem.

---

## Who is this for?
This solution is designed for teams looking to standardize their project launch process and reduce manual data entry.

*   **Project Managers**
    *   Ensures consistent project structure and task templates are applied to every new client engagement.
*   **Operations Leads**
    *   Reduces administrative bottlenecks by automating the provisioning of new projects and team assignments.
*   **Resource Coordinators**
    *   Provides real-time visibility into team capacity by ensuring projects are populated with accurate task estimates immediately.
*   **Account Executives**
    *   Enables a seamless handoff from the sales pipeline to the delivery team without manual configuration delays.

---

## Features
- **Automated Project Provisioning**
  Instantly create new projects in Harvest based on standardized templates, ensuring all metadata and settings are correctly configured from day one.
- **Intelligent Task Generation**
  Automatically populate projects with predefined task lists and time estimates, leveraging the Composio Toolset to interact directly with Harvest APIs.
- **Dynamic Team Assignment**
  Assign team members to specific tasks or project roles based on input parameters, ensuring the right resources are allocated without manual intervention.
- **Real-time Data Synchronization**
  Maintain a single source of truth by syncing project details across your internal documentation and Harvest, reducing the risk of data drift.
- **Error-Resilient Execution**
  Utilize the Agent node to validate inputs and handle API responses, ensuring that project setups are completed successfully or flagged for review.

---

## Use Cases
**Standardized Client Onboarding**
*   Automatically generate a new project folder and task list the moment a contract is marked as "Closed-Won."
*   Apply consistent billing rates and project settings across all new client accounts to ensure financial reporting accuracy.

**Resource and Capacity Planning**
*   Populate project timelines with specific milestones and task durations based on historical project data.
*   Assign internal team members to project phases automatically to provide immediate visibility for resource managers.

**Operational Workflow Hygiene**
*   Archive or update legacy project structures to match current organizational standards during periodic audits.
*   Sync project-level notes and client requirements from CRM inputs directly into the Harvest project description field.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your Harvest account via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives project details, client name, and team member IDs.
*   **Agent**: Processes the request, maps inputs to Harvest fields, and determines the necessary API actions.
*   **Composio Toolset**: Executes the creation of projects, tasks, and assignments via the Harvest API.
*   **Chat Output**: Confirms successful project creation and provides a summary link to the new Harvest project.

### 3) Run the Flow
Use the Playground to test your setup with these example prompts:
* `Create a new project for 'Acme Corp' using the 'Standard Web Dev' template and assign 'John Doe' as the lead.`
* `Set up a new project named 'Q4 Marketing Campaign' with a budget of 50 hours and add 'Marketing Team' to the task list.`
* `Launch a new project for 'Beta Client' and pre-populate it with the 'Discovery' and 'Design' task phases.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your project setup logic.
*   Focus on mapping natural language inputs to structured Harvest API parameters.
*   Ensure the agent is instructed to verify project existence before attempting creation to prevent duplicates.
*   Maintain a professional tone in the final confirmation message provided to the user.

### 2) Composio Toolset Node
*   **API Key**: Provide your Harvest API credentials within the Composio dashboard.
*   **Connection Scope**: Ensure the connection has `projects:write`, `tasks:write`, and `assignments:write` permissions.

### 3) Tool Availability
*   `harvest_create_project`: Initializes the project container.
*   `harvest_add_task`: Populates the project with required work items.
*   `harvest_assign_user`: Maps team members to the project or specific tasks.
*   `harvest_get_templates`: Retrieves existing project templates for consistent setup.

---

## Related Solutions
* [Workspace Setup Optimizer](../workspace-setup-optimizer-by-clockify/README.md) — Streamline your workspace configuration and time-tracking setup.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Automate complex project workflows and status updates.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Standardize account provisioning and CRM data entry.
