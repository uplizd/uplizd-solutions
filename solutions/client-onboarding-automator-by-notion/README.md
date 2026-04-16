# Client Onboarding Automator (Uplizd) - Streamline personalized client workspace creation

## Summary
The Client Onboarding Automator is an intelligent Uplizd workflow designed to eliminate manual setup friction by automatically provisioning personalized client workspaces, checklists, and documentation. By leveraging the Composio Toolset to interface with platforms like Notion, this solution ensures a consistent, high-velocity onboarding experience that improves client retention and operational hygiene from day one.

---

## Demo
![Client Onboarding Automator workflow screenshot showing Notion workspace provisioning and checklist generation](image.png)
**Alt text (SEO-ready):** Client Onboarding Automator workflow in Uplizd, showing automated Notion workspace setup, checklist generation, and CRM integration for seamless client onboarding.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/client-onboarding-automator-by-notion)

---

## Category
**Primary category:** Operations automation
**Secondary tags:** crm, notion, onboarding, workflow automation, client success, data sync, composio, ai workflow

This solution bridges the gap between CRM lead status changes and project management execution to ensure no client is left waiting.

---

## Who is this for?
This solution is built for teams looking to scale their client intake process without increasing headcount.

*   **Customer Success Managers**
    *   Automate the creation of personalized client portals to reduce manual administrative overhead.
*   **Operations Leads**
    *   Standardize onboarding documentation and checklists across all new client accounts.
*   **Account Executives**
    *   Ensure a seamless handoff from sales to implementation by triggering workspace setup upon deal closure.
*   **Project Managers**
    *   Maintain visibility into onboarding progress with real-time status updates synced directly to Notion.

---

## Features
- **Automated Workspace Provisioning**
  Instantly generate a new Notion page or workspace for every new client based on predefined templates.
- **Dynamic Checklist Generation**
  Automatically populate client-specific tasks and milestones based on the service package sold.
- **CRM-to-Notion Sync**
  Trigger onboarding workflows directly from CRM status changes, ensuring data consistency across platforms.
- **Intelligent Documentation Mapping**
  Map client contact details and project requirements from the CRM into the onboarding documentation.
- **Real-time Progress Tracking**
  Monitor the status of onboarding tasks and receive notifications when critical setup steps are completed.

---

## Use Cases
**New Client Intake**
*   Automatically create a dedicated client dashboard in Notion when a deal is marked as "Closed Won" in your CRM.
*   Populate the dashboard with essential company information and key stakeholder contact details.

**Standardized Implementation**
*   Generate a customized onboarding checklist that adapts based on the specific product tier purchased by the client.
*   Assign due dates and owners to onboarding tasks automatically to maintain project velocity.

**Operational Hygiene**
*   Sync client feedback and onboarding notes back to the CRM to maintain a single source of truth for account health.
*   Archive or update client status in Notion once the onboarding phase is successfully completed.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the `client-onboarding-automator` JSON template from the repository.
3. Connect your Notion and CRM accounts via the Composio Toolset.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input:** Receives the client details and trigger event from your CRM.
*   **Agent:** Processes the request and determines the necessary onboarding steps.
*   **Composio Toolset:** Executes the API calls to Notion to create pages and databases.
*   **Chat Output:** Confirms the successful creation of the workspace and provides a link to the client.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these prompts:
* `Create a new onboarding workspace for client Acme Corp based on the Enterprise template.`
* `Generate an onboarding checklist for the new client signed in the CRM under ID 98765.`
* `Update the onboarding status for all active clients in Notion and sync to the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your CRM data and Notion's API.
*   Instruction: "You are an expert onboarding assistant. Extract client details from the input and map them to the correct Notion template."
*   Instruction: "Verify that all required fields are present before triggering the Composio Toolset."
*   Instruction: "Provide a clear confirmation message to the user once the Notion workspace is successfully provisioned."

### 2) Composio Toolset Node
*   **API Key:** Ensure your Notion integration key is active within the Composio dashboard.
*   **Connection Scope:** Grant read/write access to the specific Notion pages or databases used for onboarding.

### 3) Tool Availability
*   `notion_create_page`: To instantiate new client workspaces.
*   `notion_append_block`: To add checklists and tasks to the workspace.
*   `crm_get_deal_details`: To fetch necessary client metadata for the onboarding process.

---

## Related Solutions
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate CRM account creation and field population.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the performance and completion rates of your automated processes.
* [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Manage and visualize complex client account hierarchies.
