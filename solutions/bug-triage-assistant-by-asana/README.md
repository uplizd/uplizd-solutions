# Bug Triage Assistant (Uplizd) - Automated issue categorization and routing for engineering teams

## Summary
The Bug Triage Assistant is an intelligent Uplizd workflow that automates the intake, classification, and routing of incoming bug reports from Asana. By leveraging AI to analyze report severity and context, this solution ensures that technical debt is addressed with precision, reducing manual overhead for support teams and accelerating pipeline velocity for developers.

---

## Demo
![Bug Triage Assistant workflow dashboard showing automated Asana ticket routing](image.png)
**Alt text (SEO-ready):** Bug Triage Assistant Uplizd workflow for automated Asana bug report categorization and routing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d1bd06cc-d186-5275-9195-408cdf5e4c7c)

---

## Category
**Primary category:** Support operations
**Secondary tags:** asana, bug tracking, issue management, automated routing, support automation, ai workflow, composio, engineering efficiency.
This solution streamlines the technical support lifecycle by connecting Asana issue tracking with intelligent AI-driven triage logic.

---

## Who is this for?
This solution is designed for technical teams looking to eliminate manual ticket sorting and ensure critical bugs reach the right engineers immediately.

*   **Support Leads**
    *   Reduce time-to-first-response by automating the initial classification of incoming bug reports.
*   **Engineering Managers**
    *   Maintain high-quality backlogs by ensuring bugs are tagged and routed to the correct feature squads.
*   **Product Managers**
    *   Gain visibility into bug trends and severity distributions without manual spreadsheet maintenance.
*   **DevOps Engineers**
    *   Integrate automated triage into existing CI/CD and issue-tracking workflows to maintain pipeline hygiene.

---

## Features
- **Automated Severity Scoring**
    Analyze incoming bug descriptions to assign priority levels based on predefined impact criteria.
- **Intelligent Asana Routing**
    Automatically assign tickets to specific project boards or team members based on the detected bug category.
- **Contextual Summary Generation**
    Generate concise summaries of complex bug reports to help engineers understand the issue faster.
- **Real-time Sync**
    Utilize the Composio Toolset to ensure Asana status updates reflect the current triage state instantly.
- **Customizable Triage Rules**
    Define flexible logic to handle edge cases, such as high-priority security vulnerabilities or recurring user complaints.

---

## Use Cases
**Support Ticket Management**
*   Automatically move tickets from a general "Inbox" project to specific "Engineering" or "QA" boards.
*   Flag duplicate bug reports by comparing new submissions against existing open issues in Asana.

**Engineering Workflow Optimization**
*   Assign bugs to the relevant feature owner based on keywords found in the bug description.
*   Update custom fields in Asana (e.g., "Triage Status") automatically once the AI has reviewed the report.

**Data Hygiene and Reporting**
*   Standardize bug report formatting to ensure all incoming data is consistent for quarterly performance reviews.
*   Escalate critical bugs to a dedicated Slack or email channel while simultaneously creating the Asana task.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the **Bug Triage Assistant**.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Asana account via the Composio integration settings.
4. Ensure nodes are correctly mapped to your specific Asana project IDs and workspace triggers.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw bug report text or webhook payload from Asana.
*   **Agent**: Processes the input, determines severity, and selects the appropriate routing logic.
*   **Composio Toolset**: Executes the API calls to update, tag, or move the ticket within Asana.
*   **Chat Output**: Confirms the triage action taken and logs the result for the support team.

### 3) Run the Flow
Use the Uplizd Playground to test your triage logic:
*   `"Triage this new bug: The login button is unresponsive on mobile Safari."`
*   `"Analyze the severity of this report: Database connection timeout occurring every 5 minutes."`
*   `"Route all tickets tagged as 'Security' to the Infrastructure team's Asana board."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your support pipeline.
*   **Role:** Act as a technical triage expert that categorizes bugs based on severity and functional area.
*   **Instruction Pattern:**
    *   Analyze the bug description for keywords related to system components.
    *   Assign a priority level (P0-P4) based on the reported impact.
    *   Map the bug to the correct engineering squad based on the component identified.

### 2) Composio Toolset Node
Connect your Asana account to allow the agent to perform write operations. Ensure the connection scope includes `read` and `write` permissions for your target projects.

### 3) Tool Availability
*   **Asana Create Task**: Generate new tasks for escalated issues.
*   **Asana Update Task**: Modify status, priority, or assignee fields.
*   **Asana Search**: Query existing tasks to prevent duplicate creation.
*   **Asana Add Comment**: Append AI-generated summaries to existing tickets.

---

## Related Solutions
*   [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automatically rank and prioritize incoming action items.
*   [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Maintain clean and organized task lists by removing stale items.
*   [24/7 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Provide round-the-clock automated support responses.
