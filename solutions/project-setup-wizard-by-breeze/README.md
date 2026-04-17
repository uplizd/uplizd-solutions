# Project Setup Wizard (Uplizd) - Automated project orchestration and team provisioning

## Summary
The Project Setup Wizard by Breeze is an intelligent Uplizd AI workflow designed to streamline the initiation of new business initiatives. By automating the creation of structured project environments, team assignments, and initial workflow configurations, it eliminates manual administrative overhead, ensures consistent project hygiene, and accelerates pipeline velocity from day one.

---

## Demo
![Project Setup Wizard workflow interface showing automated team provisioning and project structure creation](image.png)
**Alt text (SEO-ready):** Uplizd Project Setup Wizard workflow interface showing automated team provisioning, project structure creation, and Composio toolset integration for project management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjZBgFowAHEjAwMDCw/P9/BqYgA0wN/v//z8D0/38GpiADTA0MDAwM/P//GZgCDDA1MDAwMDCw/P9/BqYgA0wN/v//z8D0/38GpiADTA0MDAwM/P//GZgCDDA1MDAwMDCw/P9/BqYgA0wN/v//z8D0/38GpiADTAwAALa/H1+7qF6AAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/d050e6f4-7a17-5bc4-aafa-e1cdefc739ce)

---

## Category
**Primary category:** Product operations
**Secondary tags:** project management, automation, team provisioning, workflow, onboarding, composio, ai workflow, operational efficiency.
This solution serves as a centralized orchestration layer for standardizing project launches across diverse organizational tools.

---

## Who is this for?
This solution is designed for operations leaders and project managers who need to standardize the "Day 0" experience for new business initiatives.

*   **Project Manager**
    *   Reduces manual setup time by automating the creation of project boards and task hierarchies.
*   **Operations Lead**
    *   Ensures organizational compliance by enforcing standardized project templates and naming conventions.
*   **Team Lead**
    *   Accelerates team onboarding by automatically provisioning access and assigning initial project responsibilities.
*   **RevOps Specialist**
    *   Maintains data integrity by linking new projects directly to existing CRM accounts and pipeline records.

---

## Features
- **Automated Project Provisioning**
  Instantly generate project containers and workspaces across your integrated tool stack via the Composio Toolset.
- **Dynamic Team Assignment**
  Automatically map team members to specific project roles based on predefined project requirements and availability.
- **Standardized Workflow Templates**
  Deploy consistent task structures and milestone tracking to ensure every project starts with the same operational rigor.
- **Real-time CRM Synchronization**
  Maintain a single source of truth by syncing project metadata back to your CRM platform automatically.
- **Intelligent Configuration Validation**
  Ensure all required project fields are populated correctly before the workflow finalizes the setup process.

---

## Use Cases
**New Client Onboarding**
*   Automatically create a dedicated project folder and task list upon closing a deal in your CRM.
*   Provision team access and send welcome notifications to stakeholders based on the project scope.

**Internal Initiative Launch**
*   Standardize the setup of quarterly OKR tracking projects across different departments.
*   Assign resource budgets and timeline milestones automatically based on project category.

**Cross-Platform Sync**
*   Bridge gaps between project management tools and communication platforms by auto-creating channels for new projects.
*   Sync project status updates across multiple platforms to keep cross-functional teams aligned.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Project Setup Wizard template from the solution library.
3. Connect your required API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked from Chat Input to Agent, Toolset, and Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives project parameters (name, scope, team size).
*   **Agent**: Processes requirements and determines the necessary provisioning steps.
*   **Composio Toolset**: Executes API calls to create projects, assign users, and set permissions.
*   **Chat Output**: Confirms successful project creation and provides a summary of the new environment.

### 3) Run the Flow
Open the Playground and test with these prompts:
* `Create a new project named 'Q4 Marketing Launch' with the standard 'Growth' template.`
* `Setup a new client project for 'Acme Corp' and assign the 'Sales' and 'Support' teams.`
* `Initialize a project for the 'Internal Audit' initiative and set the deadline for 30 days from now.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for project logic.
*   Maintain a professional, structured tone for all project documentation.
*   Prioritize data accuracy when mapping project fields to external APIs.
*   Always confirm project parameters with the user before executing creation commands.

### 2) Composio Toolset Node
Requires an active connection to your project management suite (e.g., Jira, Asana, or Monday.com) via Composio. Ensure the API key has "Write" and "Admin" scopes to allow for project and user provisioning.

### 3) Tool Availability
*   **Project Management API**: Create projects, update metadata, and set milestones.
*   **User Management API**: Assign team members and manage role-based access control.
*   **CRM Connector**: Sync project IDs and status updates to customer records.

---

## Related Solutions
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automates the configuration of new CRM accounts and client profiles.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamlines cross-platform task execution and operational workflows.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Manages complex stakeholder mapping and account hierarchies.
