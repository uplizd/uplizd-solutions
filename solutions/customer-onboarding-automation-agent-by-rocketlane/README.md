# Customer Onboarding Automation Agent (Uplizd) - Streamline client setup and project workflows

## Summary
The Customer Onboarding Automation Agent by Rocketlane is an intelligent workflow designed to eliminate manual data entry and project setup friction. By connecting your CRM and customer data directly to Rocketlane project templates, this agent ensures that every new client account is provisioned, tasks are assigned, and stakeholders are notified instantly, resulting in faster time-to-value and improved operational hygiene.

---

## Demo
![Customer Onboarding Automation Agent workflow showing CRM data flowing into Rocketlane project templates via Uplizd](image.png)
**Alt text (SEO-ready):** Uplizd customer onboarding automation workflow, Rocketlane project setup, CRM data integration, and automated task management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue?logo=uplizd)](https://uplizd.ai/solutions/e1963dfa-a4cf-5968-b9df-0e17179da709)

---

## Category
**Primary category:** Operations
**Secondary tags:** rocketlane, onboarding, crm, project management, workflow automation, client success, data sync, composio.
This solution bridges the gap between sales-closed deals and active project delivery through automated lifecycle management.

---

## Who is this for?
This solution is designed for RevOps and Customer Success teams looking to scale their service delivery without increasing headcount.

*   **Customer Success Manager**
    *   Reduces manual project setup time by automatically triggering Rocketlane templates upon deal closure.
*   **Implementation Specialist**
    *   Ensures all project tasks and milestones are pre-populated and assigned to the correct internal stakeholders.
*   **RevOps Lead**
    *   Maintains data integrity between the CRM and project management tools, ensuring a single source of truth.
*   **Account Executive**
    *   Provides a seamless transition for the client from the sales process to the onboarding phase.

---

## Features
- **Automated Project Provisioning**
  Instantly creates new projects in Rocketlane based on specific CRM triggers or deal stages.
- **Dynamic Template Mapping**
  Automatically selects the appropriate onboarding template based on the customer segment or product tier.
- **Cross-Platform Data Sync**
  Synchronizes key client information and contact details from your CRM directly into the project workspace.
- **Real-Time Task Assignment**
  Assigns onboarding tasks to the relevant team members based on pre-defined project roles and availability.
- **Proactive Status Notifications**
  Triggers automated updates and welcome emails to stakeholders once the project environment is ready.

---

## Use Cases
**Seamless Handover**
*   Automatically trigger a Rocketlane project the moment a deal is marked as "Closed-Won" in your CRM.
*   Populate project fields with custom data points like contract value, primary contact, and technical requirements.

**Resource Allocation**
*   Assign specific onboarding tasks to team members based on their current workload and expertise.
*   Sync project milestones with internal calendars to ensure timely delivery of onboarding phases.

**Operational Hygiene**
*   Standardize the onboarding process by enforcing the use of approved templates for every new client.
*   Archive or update project status in the CRM automatically once the onboarding phase reaches completion.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Rocketlane and CRM accounts within the Composio Toolset.
4. Ensure nodes are correctly mapped and all required API keys are active in the configuration panel.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event (e.g., "New Deal Closed") or manual request.
*   **Agent**: Processes the request, extracts client data, and determines the correct project template.
*   **Composio Toolset**: Executes the API calls to Rocketlane and your CRM to create projects and update records.
*   **Chat Output**: Confirms successful project creation and provides a summary of assigned tasks.

### 3) Run the Flow
Use the Playground to test your onboarding logic:
*   `"Create a new onboarding project for Acme Corp using the Enterprise template."`
*   `"Sync the latest deal details from Salesforce to Rocketlane for project ID 12345."`
*   `"Check the status of onboarding tasks for the new client assigned to the implementation team."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestration layer between your data sources and project management tool.
*   Focus on extracting structured data from unstructured CRM inputs.
*   Prioritize accuracy in mapping project templates to client tiers.
*   Maintain a professional and helpful tone for all generated status notifications.

### 2) Composio Toolset Node
Requires an active API key for both Rocketlane and your CRM (e.g., Salesforce or HubSpot). Ensure the connection scope includes read/write permissions for projects, tasks, and deal objects.

### 3) Tool Availability
*   **Rocketlane API**: Project creation, template selection, and task assignment.
*   **CRM Connector**: Data retrieval, deal status updates, and contact synchronization.
*   **Notification Service**: Automated email or Slack alerts for project stakeholders.

---

## Related Solutions
*   [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) — Automates CRM account provisioning and field population.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages deal stages and pipeline velocity for sales teams.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensures consistent data synchronization across multiple platforms.
*   [Account Relationship Builder (Dynamics 365)](../account-relationship-builder-by-dynamics365/README.md) — Strengthens client relationships through automated engagement tracking.
