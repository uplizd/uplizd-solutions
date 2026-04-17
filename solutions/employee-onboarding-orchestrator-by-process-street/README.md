# Employee Onboarding Orchestrator (Uplizd) - Streamline new hire workflows and task management

## Summary
The Employee Onboarding Orchestrator automates the complex lifecycle of bringing new hires into an organization by synchronizing tasks across HR platforms and internal communication tools. By leveraging the Composio Toolset to trigger actions in Process Street and other management systems, this workflow ensures consistent onboarding experiences, reduces manual administrative overhead, and maintains high pipeline velocity for People Operations teams.

---

## Demo
![Employee Onboarding Orchestrator dashboard showing automated task assignment and progress tracking](image.png)
**Alt text (SEO-ready):** Employee Onboarding Orchestrator workflow in Uplizd showing automated task assignment, Process Street integration, and new hire pipeline management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKAAABAAAB)](https://uplizd.ai/solutions/9aa49cb9-15e8-554e-9d5b-d16a64b30da7)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** onboarding, hr automation, process street, workflow, employee lifecycle, task management, composio, ai agent
- This solution bridges the gap between HR documentation and execution, providing a unified interface for managing complex onboarding checklists.

---

## Who is this for?
This solution is designed for teams managing high-volume hiring and complex internal processes.

- **People Operations Manager**
    - Automates repetitive checklist creation to ensure every new hire follows the same compliant process.
- **IT Administrator**
    - Triggers automated provisioning tasks across software platforms immediately upon onboarding initiation.
- **HR Coordinator**
    - Gains real-time visibility into onboarding status, reducing the time spent manually updating spreadsheets.
- **Department Lead**
    - Receives automated notifications and task assignments to facilitate team-specific training and integration.

---

## Features
- **Automated Checklist Generation**
    - Dynamically creates onboarding workflows in Process Street based on the new hire's role and department.
- **Cross-Platform Synchronization**
    - Uses the Composio Toolset to push data between HRIS systems and task management tools in real-time.
- **Role-Based Task Routing**
    - Intelligent assignment of onboarding tasks to relevant stakeholders based on the employee's specific profile.
- **Status Tracking & Alerts**
    - Monitors progress across all onboarding stages and triggers reminders for incomplete or overdue items.
- **Compliance Documentation**
    - Ensures all mandatory training and documentation tasks are logged and verified within the central workflow.

---

## Use Cases
**New Hire Provisioning**
- Automatically trigger account creation requests in IT systems upon contract signature.
- Assign hardware setup tasks to the IT team based on the new hire's office location.

**Departmental Integration**
- Deploy role-specific training modules in Process Street for engineering, sales, or marketing hires.
- Schedule introductory meetings with team leads and mentors automatically.

**Compliance & Documentation**
- Track the completion of mandatory legal and security training modules for new employees.
- Generate automated audit logs for completed onboarding checklists to ensure regulatory compliance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd solution library and select the Employee Onboarding Orchestrator.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your Process Street and relevant HRIS accounts via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are authenticated in the settings panel.

### 2) Setup the Nodes
- **Chat Input**: Receives new hire details (Name, Role, Department).
- **Agent**: Processes input and determines the required onboarding checklist.
- **Composio Toolset**: Executes API calls to create tasks and update status in external platforms.
- **Chat Output**: Confirms successful workflow initiation and provides a summary of assigned tasks.

### 3) Run the Flow
Use the Playground to test the orchestration:
- `Initiate onboarding for John Doe, Role: Software Engineer, Dept: Engineering`
- `Check status of onboarding tasks for Jane Smith`
- `Create a new onboarding checklist for the Sales team lead role`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central orchestrator for HR tasks.
- Instruction: Act as an expert HR operations assistant.
- Instruction: Map incoming employee data to the correct Process Street template.
- Instruction: Maintain a professional tone and provide clear confirmation of task creation.

### 2) Composio Toolset Node
- Requires an active API key for Process Street and any integrated HRIS.
- Connection scope should include read/write access to task lists and user profiles.

### 3) Tool Availability
- **Process Street API**: For checklist creation and task management.
- **HRIS Connector**: For employee data retrieval and validation.
- **Notification Service**: For sending alerts to department leads.

---

## Related Solutions
- [../workforce-onboarding-automator-by-connecteam/README.md](../workforce-onboarding-automator-by-connecteam/README.md) - Alternative onboarding automation for frontline workforce management.
- [../admin-user-onboarding-assistant-by-storeganise/README.md](../admin-user-onboarding-assistant-by-storeganise/README.md) - Specialized onboarding assistant for administrative user access.
- [../account-setup-agent-by-salesforce/README.md](../account-setup-agent-by-salesforce/README.md) - Automates account provisioning and setup within Salesforce environments.
