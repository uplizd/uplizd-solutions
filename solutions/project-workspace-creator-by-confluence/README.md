# Project Workspace Creator (Uplizd) - Automated Confluence workspace provisioning

## Summary
The Project Workspace Creator (Uplizd) is an intelligent AI workflow designed to automate the setup of structured project environments within Confluence. By leveraging the Composio Toolset, this solution eliminates manual configuration overhead, ensuring consistent project documentation, standardized page hierarchies, and immediate team readiness. It serves as a single source of truth for project managers and operations teams looking to accelerate pipeline velocity and maintain organizational hygiene.

---

## Demo
![Project Workspace Creator workflow showing automated Confluence page generation and template application](image.png)
**Alt text (SEO-ready):** Project Workspace Creator workflow using Uplizd and Composio to automate Confluence workspace setup, page templates, and project documentation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3f3ad289-a531-5882-ad68-927eb3d7a06a)

---

## Category
**Primary category:** Productivity & Operations
**Secondary tags:** confluence, project management, automation, workspace, documentation, composio, ai workflow, team collaboration.
This solution streamlines the creation of complex project documentation structures, ensuring teams spend less time on administrative setup and more time on execution.

---

## Who is this for?
This solution is designed for teams that require rapid, standardized project onboarding and documentation management.

* **Project Managers**
    * Automate the creation of project charters, meeting notes, and status report templates instantly.
* **Operations Leads**
    * Enforce organizational standards by ensuring every new project workspace follows a pre-defined structure.
* **Engineering Managers**
    * Quickly provision technical documentation hubs and sprint planning pages for new initiatives.
* **Team Leads**
    * Reduce onboarding friction by providing new team members with a fully populated and organized workspace.

---

## Features
- **Automated Page Creation**
  Instantly generate Confluence pages based on predefined templates, reducing manual data entry.
- **Hierarchical Structuring**
  Automatically organize project documentation into logical parent-child page relationships.
- **Template Integration**
  Apply existing Confluence templates to ensure consistent formatting across all project workspaces.
- **Composio-Powered Execution**
  Utilize the Composio Toolset to securely interface with Confluence APIs for real-time workspace updates.
- **Customizable Metadata**
  Inject project-specific details like timelines, stakeholders, and goals directly into the generated documentation.

---

## Use Cases
**New Project Onboarding**
* Automatically create a "Project Home" page with links to all relevant sub-pages.
* Populate the workspace with standard project charter and risk assessment templates.

**Standardized Reporting**
* Generate weekly status report pages with pre-filled fields for key metrics and blockers.
* Create recurring meeting note pages linked to the project workspace for centralized tracking.

**Documentation Hygiene**
* Automate the cleanup of legacy project workspaces by archiving outdated pages during new project setup.
* Maintain consistent naming conventions across all project assets to improve searchability and discoverability.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the `project-workspace-creator-by-confluence` JSON configuration.
3. Connect your Confluence account via the Composio integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives the project name and template requirements from the user.
* **Agent:** Processes the request and determines the necessary Confluence page structure.
* **Composio Toolset:** Executes the API calls to create pages and apply templates in Confluence.
* **Chat Output:** Confirms the successful creation of the workspace and provides direct links to the new pages.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Create a new project workspace for "Q4 Marketing Campaign" using the standard project template.`
* `Set up a workspace for "Internal Tool Migration" and include a page for technical requirements.`
* `Initialize a new project space named "Client X Onboarding" with a meeting notes template.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for workspace logic and template selection.
* Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruct the agent to validate project naming conventions before triggering creation.
* Ensure the agent is configured to handle errors gracefully if a page already exists.

### 2) Composio Toolset Node
* Provide a valid Confluence API Key and ensure the connection scope includes `page:write` and `space:read` permissions.
* Map the toolset to your specific Confluence instance URL.

### 3) Tool Availability
* `confluence_create_page`: For generating new project documentation.
* `confluence_get_templates`: For fetching available organizational templates.
* `confluence_add_label`: For tagging project pages for better searchability.

---

## Related Solutions
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automate CRM account provisioning and data entry.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform task management and status updates.
* [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manage and deploy collaborative workshop templates for remote teams.
