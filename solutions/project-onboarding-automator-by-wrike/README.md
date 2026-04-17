# Project Onboarding Automator (Uplizd) - Streamline project setup and team assignments

## Summary
The Project Onboarding Automator is an intelligent Uplizd workflow designed to eliminate manual setup friction by instantly provisioning project structures, assigning team roles, and configuring initial task boards. By leveraging the Composio Toolset to interface with Wrike, this solution ensures project consistency, accelerates pipeline velocity, and provides a single source of truth for all new project launches.

---

## Demo
![Project Onboarding Automator workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Project Onboarding Automator workflow in Uplizd, demonstrating automated project creation, team assignment, and Wrike integration for streamlined project management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dee444cf-6ec7-57dc-90cb-ca9a0512e117)

---

## Category
**Primary category:** Project Management
**Secondary tags:** wrike, project onboarding, workflow automation, team management, task automation, composio, ai workflow, operational efficiency.
This solution bridges the gap between project initiation and execution by automating repetitive administrative tasks within your project management ecosystem.

---

## Who is this for?
This solution is designed for operations teams and project leads who need to maintain high standards of project hygiene while reducing manual administrative overhead.

- **Project Managers**
    - Automate the creation of standardized project folders and task hierarchies to ensure consistent delivery.
- **Operations Leads**
    - Standardize team assignments and permission settings across new project launches to maintain operational compliance.
- **Team Leads**
    - Reduce time-to-productivity by instantly provisioning resources and task boards for new project members.
- **Resource Managers**
    - Gain real-time visibility into project allocations and team capacity from the moment a project is initialized.

---

## Features
- **Automated Project Provisioning**
    - Instantly creates new project folders and structures in Wrike based on predefined templates.
- **Intelligent Team Assignment**
    - Automatically maps team members to project roles based on project type and department requirements.
- **Standardized Task Generation**
    - Populates new projects with essential baseline tasks and milestones to ensure immediate project momentum.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely communicate with Wrike APIs for real-time data synchronization.
- **Workflow Consistency Engine**
    - Enforces organizational standards by ensuring every project follows the same setup protocol, reducing human error.

---

## Use Cases
**New Project Launch**
- Automatically generate a full project folder structure in Wrike when a new client contract is signed.
- Assign the appropriate project lead and department stakeholders based on the project category.

**Team Resource Allocation**
- Sync team availability and role-based assignments to new project boards upon creation.
- Notify team members via Wrike comments or task assignments as soon as their specific project modules are ready.

**Operational Compliance**
- Ensure all new projects include mandatory compliance and documentation tasks by default.
- Standardize naming conventions and metadata fields across all active projects to simplify reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Project Onboarding Automator template from the solution library.
3. Connect your Wrike account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the project name, type, and primary stakeholder details.
- **Agent**: Processes the request and determines the necessary project structure and team assignments.
- **Composio Toolset**: Executes API calls to Wrike to create projects, tasks, and assignments.
- **Chat Output**: Confirms successful project creation and provides a summary of assigned resources.

### 3) Run the Flow
Use the Playground to test your onboarding logic:
- `Create a new project named 'Q4 Marketing Campaign' for the Creative team.`
- `Initialize a new project for 'Client X' using the standard 'Web Development' template.`
- `Set up a project for 'Internal Audit' and assign the 'Compliance' team as stakeholders.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer that interprets project requirements and maps them to Wrike actions.
- Use a model capable of structured output to ensure project parameters are correctly parsed.
- Instruct the agent to validate input data (e.g., project name, team names) before calling the toolset.
- Maintain a professional, operational tone in all confirmation messages.

### 2) Composio Toolset Node
- Provide your Wrike API key within the Composio configuration panel.
- Ensure the connection scope includes permissions for project creation, task management, and user assignment.

### 3) Tool Availability
- `wrike_create_project`: For initializing new project containers.
- `wrike_create_task`: For populating projects with baseline milestones.
- `wrike_assign_user`: For mapping team members to specific tasks or projects.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline employee setup and access provisioning.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automate CRM account creation and data entry.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Manage complex business process workflows across platforms.
