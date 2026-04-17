# Customer Onboarding Orchestrator (Uplizd) - Streamline client setup and task management

## Summary
The Customer Onboarding Orchestrator is an intelligent Uplizd workflow designed to automate the transition from sales to success. By integrating Kommo with your project management tools, this solution ensures that every new client receives a consistent, high-touch onboarding experience, reducing manual administrative overhead and accelerating time-to-value for your customers.

---

## Demo
![Customer Onboarding Orchestrator workflow showing Kommo integration and automated task creation](image.png)
**Alt text (SEO-ready):** Customer Onboarding Orchestrator workflow in Uplizd, automating client setup, Kommo CRM task management, and onboarding pipeline tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2ZmZiI+PHBhdGggZD0iTTEyIDJMMiAxMnYxMGgyMFYxMkwxMiAyem0wIDE4bC04LTRWOGw4IDQgOC00djZMMTIgMjB6Ii8+PC9zdmc+)](https://uplizd.ai/solutions/985bb854-8ef3-5d44-bc13-f6292a3321d1)

---

## Category
**Primary category:** Customer Success Operations
**Secondary tags:** kommo, onboarding, crm, workflow automation, client success, task management, composio, ai workflow.
This solution bridges the gap between CRM lead conversion and long-term client retention through automated onboarding orchestration.

---

## Who is this for?
This solution is built for teams looking to standardize their client handoff and improve operational efficiency.

*   **Customer Success Manager**
    *   Automates the creation of onboarding checklists and task assignments immediately upon deal closure.
*   **Sales Operations Lead**
    *   Ensures data integrity and process compliance by syncing CRM status changes to downstream project tools.
*   **Implementation Specialist**
    *   Reduces manual data entry by automatically populating client profiles and project boards from CRM data.
*   **Account Executive**
    *   Provides a seamless transition for clients, ensuring no follow-up items are missed during the handoff phase.

---

## Features
- **Automated Handoff Triggers**
    Real-time detection of deal status changes in Kommo to initiate onboarding workflows instantly.
- **Dynamic Task Generation**
    Automatically creates and assigns onboarding tasks based on specific client requirements or service tiers.
- **Cross-Platform Sync**
    Seamlessly connects Kommo CRM data with project management platforms via the Composio Toolset.
- **Standardized Client Communication**
    Generates personalized welcome emails or internal notifications to keep stakeholders informed of onboarding progress.
- **Pipeline Hygiene Monitoring**
    Maintains clean CRM data by updating deal stages and logging activity logs throughout the onboarding lifecycle.

---

## Use Cases
**Client Setup Automation**
*   Automatically create a new project board in your task manager when a deal is marked as "Won" in Kommo.
*   Populate client contact information and project scope fields directly from the CRM into the onboarding template.

**Task Management & Tracking**
*   Assign onboarding milestones to specific team members based on the client's industry or service package.
*   Send automated reminders to the Success team when an onboarding task approaches its deadline.

**Communication & Reporting**
*   Trigger a welcome email sequence to the client once the initial onboarding tasks are successfully provisioned.
*   Generate a summary report of onboarding progress for management review at the end of each week.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your dashboard.
3. Connect your Kommo account and relevant task management tools via the Composio integration menu.
4. Ensure nodes are correctly mapped and all API credentials are authenticated before activating the flow.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event or manual onboarding request.
*   **Agent**: Orchestrates the logic, interpreting CRM data and determining the necessary onboarding steps.
*   **Composio Toolset**: Executes actions across Kommo and project management platforms.
*   **Chat Output**: Confirms task creation and provides a status summary of the onboarding initiation.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Initialize onboarding for the latest won deal in Kommo.`
* `Create a new onboarding task list for client [Client Name] based on the standard template.`
* `Check the status of onboarding tasks for all active clients and report any delays.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, ensuring that CRM data is accurately translated into actionable tasks.
*   Focus on extracting key client metadata from the CRM payload.
*   Prioritize task assignment logic based on the service tier identified in the deal.
*   Maintain a professional, proactive tone in all generated internal notifications.

### 2) Composio Toolset Node
Requires an active Kommo API key and connection scope to read deal stages and write project tasks. Ensure the agent has "Read/Write" permissions for the relevant CRM and project management modules.

### 3) Tool Availability
*   **CRM Connector**: Fetch deal details, update deal stages, and retrieve contact information.
*   **Project Management Connector**: Create boards, add tasks, and assign due dates.
*   **Notification Service**: Send internal alerts or client-facing emails based on workflow triggers.

---

## Related Solutions
* [Account Relationship Builder (Dynamics 365)](../account-relationship-builder-by-dynamics365/README.md) - Manage complex client relationships and account hierarchies.
* [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) - Automate field service and project workflows.
* [Workforce Onboarding Automator (Connecteam)](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline internal employee onboarding and training.
