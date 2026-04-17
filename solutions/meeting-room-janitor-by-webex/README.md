# Meeting Room Janitor (Uplizd) - Automated Webex space cleanup and membership management

## Summary
The Meeting Room Janitor by Webex is an intelligent Uplizd workflow designed to automate the maintenance of digital collaboration spaces. By identifying inactive rooms and streamlining team membership updates, this solution ensures your communication environment remains organized, secure, and clutter-free, significantly reducing manual administrative overhead for IT and operations teams.

---

## Demo
![Meeting Room Janitor dashboard showing automated cleanup logs and Webex space status](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Room Janitor workflow dashboard showing automated Webex space cleanup, inactive room identification, and team membership management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAHAAABAAAB)](https://uplizd.ai/solutions/8ce82550-f2e0-51e9-bda5-402bba5a0b25)

---

## Category
**Primary category:** Operations  
**Secondary tags:** webex, meeting management, automation, workspace hygiene, it operations, composio, ai workflow  
This solution bridges the gap between static collaboration tools and dynamic workspace management through automated cleanup policies.

---

## Who is this for?
This solution is built for teams looking to maintain high-signal communication environments and reduce digital sprawl.

- **IT Administrators**
  - Automate the decommissioning of stale meeting rooms to reclaim system resources and maintain security compliance.
- **Operations Managers**
  - Ensure team memberships are accurate and up-to-date without manual intervention in the Webex admin console.
- **Project Leads**
  - Keep project-specific collaboration spaces organized by automatically removing inactive participants or archived rooms.
- **Office Managers**
  - Reduce digital clutter and improve meeting efficiency by enforcing room hygiene policies across the organization.

---

## Features
- **Automated Inactivity Detection**
  - Uses intelligent triggers to identify Webex spaces that have not seen activity within a defined timeframe.
- **Bulk Membership Management**
  - Syncs team rosters automatically, ensuring that only active employees have access to relevant collaboration spaces.
- **Policy-Driven Cleanup**
  - Executes custom deletion or archival rules based on space usage metrics and organizational compliance standards.
- **Composio-Powered Integration**
  - Leverages the Composio Toolset to securely interface with the Webex API for real-time room and user management.
- **Audit Logging**
  - Tracks every cleanup action and membership change, providing a transparent record for security and administrative review.

---

## Use Cases
**Workspace Hygiene**
- Automatically archive Webex spaces that have been inactive for more than 90 days.
- Flag duplicate or redundant meeting rooms for manual review by the IT department.

**Access Governance**
- Remove users from specific project rooms immediately upon their departure from the organization.
- Audit team memberships monthly to ensure alignment with current department structures.

**Operational Efficiency**
- Streamline the onboarding process by automatically adding new hires to relevant departmental Webex spaces.
- Generate weekly reports on total active vs. inactive meeting rooms to optimize license utilization.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to add the Meeting Room Janitor workflow to your Uplizd workspace.
3. Connect your Webex credentials via the Composio integration portal.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives trigger commands or scheduled cleanup requests.
- **Agent**: Processes logic for identifying stale rooms and determining membership changes.
- **Composio Toolset**: Executes API calls to Webex to perform cleanup and user updates.
- **Chat Output**: Returns a summary report of all actions taken during the execution.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `List all Webex rooms that have been inactive for over 60 days.`
- `Archive the 'Project Alpha' room and remove all external guests.`
- `Sync the current team membership list with the 'Engineering' Webex space.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for your cleanup policies.
- **Instruction Pattern:**
  - "Analyze the provided Webex space metadata to determine if it meets the inactivity threshold."
  - "When performing membership updates, prioritize security and access control lists."
  - "Always provide a clear, concise summary of actions taken in the final output."

### 2) Composio Toolset Node
- **API Key:** Provide your Webex API credentials within the Composio dashboard.
- **Connection Scope:** Ensure the connection has `spark:rooms_read`, `spark:rooms_write`, and `spark:memberships_write` permissions.

### 3) Tool Availability
- **Webex Room Manager:** Capability to list, archive, and delete spaces.
- **Webex Membership Controller:** Capability to add/remove users and update participant roles.
- **Reporting Utility:** Capability to format and export execution logs for audit purposes.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automates the resolution and cleanup of stale action items.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks and reports on the operational status of your automated workflows.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Audits and manages user permissions across administrative platforms.
