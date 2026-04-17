# Client Onboarding Tracker (Uplizd) - Automated task management and progress monitoring

## Summary
The Client Onboarding Tracker is an intelligent Uplizd workflow designed to automate the transition from sales to success by syncing client data directly into Asana. By leveraging AI to parse onboarding requirements and trigger project creation, this solution eliminates manual data entry, ensures consistent project setup, and accelerates time-to-value for new customers.

---

## Demo
![Client Onboarding Tracker workflow showing data flow from Chat Input to Asana project creation](image.png)
**Alt text (SEO-ready):** Client Onboarding Tracker workflow in Uplizd, automating Asana task creation and project tracking for seamless customer onboarding and CRM data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/02034dee-412b-56a6-b09f-2da33a2ea27c)

---

## Category
**Primary category:** Operations
**Secondary tags:** asana, onboarding, project management, workflow automation, crm, client success, task tracking, composio

This solution bridges the gap between client acquisition and service delivery by automating administrative project management tasks.

---

## Who is this for?
This solution is built for teams looking to standardize their customer implementation process and reduce operational friction.

*   **Customer Success Managers**
    *   Automate the creation of onboarding checklists to ensure no client requirements are missed.
*   **Operations Leads**
    *   Standardize project templates across the organization for consistent service delivery.
*   **Account Executives**
    *   Seamlessly hand off new accounts to the delivery team without manual ticket creation.
*   **Project Coordinators**
    *   Gain real-time visibility into onboarding progress and identify potential bottlenecks early.

---

## Features
- **Automated Task Generation**
    Trigger Asana project creation and task assignment automatically based on incoming client data.
- **Intelligent Data Mapping**
    Use AI to extract key client details from emails or forms and map them to specific Asana fields.
- **Cross-Platform Synchronization**
    Maintain a single source of truth by syncing status updates between your CRM and Asana.
- **Standardized Onboarding Templates**
    Ensure every client follows the same high-quality implementation path with pre-configured project structures.
- **Real-time Progress Monitoring**
    Receive automated notifications and status reports as onboarding milestones are completed.

---

## Use Cases
**New Client Kickoff**
*   Automatically generate a project board in Asana the moment a deal is marked "Closed Won" in your CRM.
*   Populate onboarding tasks with specific client requirements gathered during the sales process.

**Milestone Tracking**
*   Update project status in Asana based on feedback received through client communication channels.
*   Trigger automated follow-up tasks for the implementation team when a milestone deadline approaches.

**Resource Allocation**
*   Assign onboarding tasks to specific team members based on client industry or project complexity.
*   Monitor team workload by aggregating active onboarding tasks across multiple client projects.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and import the workflow into your project.
3. Connect your Asana account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives client details and project parameters.
*   **Agent**: Analyzes input to determine task requirements and project scope.
*   **Composio Toolset**: Executes API calls to create projects and tasks in Asana.
*   **Chat Output**: Confirms successful project creation and provides a summary link.

### 3) Run the Flow
Use the Playground to test your onboarding automation:
*   `Create a new onboarding project for Acme Corp with a 2-week timeline and assign to the implementation team.`
*   `Generate a task list for a new enterprise client including security review and platform configuration.`
*   `Sync the latest onboarding status for the project ID 12345 and notify the project lead.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your project management logic.
*   **Instruction Pattern:**
    *   Extract client name, project scope, and deadline from the user prompt.
    *   Map extracted data to the required fields for Asana project creation.
    *   Verify task completion and provide a clear confirmation message to the user.

### 2) Composio Toolset Node
*   **API Key:** Ensure your Asana API key is configured within the Composio dashboard.
*   **Connection Scope:** Grant read/write access to your Asana projects and tasks to allow the agent to manage workflows.

### 3) Tool Availability
*   **Asana Create Project:** Initializes new onboarding boards.
*   **Asana Create Task:** Adds specific action items to the project.
*   **Asana Update Task:** Modifies status or assignee as the project progresses.
*   **Asana Get Project Details:** Retrieves current status for reporting.

---

## Related Solutions
*   [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automate CRM account configuration.
*   [Workflow Automation Agent by JobNimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex business processes.
*   [Workforce Onboarding Automator by Connecteam](../workforce-onboarding-automator-by-connecteam/README.md) - Manage internal team onboarding workflows.
