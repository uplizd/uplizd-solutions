# Smart Time-Off Assistant (Uplizd) - Automated leave management and approval workflows

## Summary
The Smart Time-Off Assistant streamlines employee leave management by integrating directly with your HR and calendar systems. This Uplizd AI workflow automates the entire lifecycle of time-off requests—from checking remaining balances and validating policy compliance to routing approval notifications—ensuring HR teams and managers maintain accurate records while reducing manual administrative overhead.

---

## Demo
![Smart Time-Off Assistant workflow showing chat input, balance check, and approval routing](image.png)
**Alt text (SEO-ready):** Smart Time-Off Assistant (Uplizd) workflow for automated leave balance checking, HR policy validation, and calendar synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4b915f7c-cb1f-596f-8584-6fd41297d816)

---

## Category
**Primary category:** Operations
**Secondary tags:** hr, time-off, workday, leave management, automation, employee experience, composio, ai workflow.
This solution bridges the gap between employee requests and HR system updates, creating a seamless, automated pipeline for leave administration.

---

## Who is this for?
This solution is designed for organizations looking to modernize their HR operations and empower employees with self-service tools.

*   **HR Managers**
    *   Automate policy enforcement and reduce manual data entry for leave accruals.
*   **Team Leads**
    *   Receive instant, context-rich approval requests directly in their preferred communication channel.
*   **Employees**
    *   Get real-time visibility into remaining time-off balances without waiting for HR support.
*   **Operations Specialists**
    *   Maintain data hygiene across HRIS and calendar platforms with automated synchronization.

---

## Features
- **Real-time Balance Validation**
  Instantly cross-reference requested dates against current leave balances using the Composio Toolset.
- **Automated Approval Routing**
  Intelligently identify the correct manager and trigger notification workflows based on organizational hierarchy.
- **Calendar Synchronization**
  Automatically update team calendars upon approval to prevent scheduling conflicts and improve visibility.
- **Policy Compliance Engine**
  Ensure all requests adhere to company-specific leave policies and blackout dates before submission.
- **Unified HR Integration**
  Connects seamlessly with Workday and other HRIS platforms to ensure a single source of truth for all time-off data.

---

## Use Cases
**Leave Request Processing**
*   Automated validation of remaining PTO days before submitting a request to the manager.
*   Instant confirmation messages sent to employees once a manager approves the request in the HRIS.

**Team Scheduling & Coverage**
*   Syncing approved leave dates to shared team calendars to ensure adequate project coverage.
*   Generating weekly reports of upcoming absences for department heads to assist in resource planning.

**HR Policy Enforcement**
*   Flagging requests that fall during restricted company blackout periods for manual HR review.
*   Calculating carry-over balances automatically at the end of the fiscal year based on current usage.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Smart Time-Off Assistant template from the solution library.
3. Authenticate your HRIS and calendar integrations via the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the employee's time-off request details (dates, type of leave).
*   **Agent**: Evaluates the request against HR policies and determines the next action.
*   **Composio Toolset**: Executes the API calls to check balances and update HRIS records.
*   **Chat Output**: Delivers the status update or approval confirmation back to the user.

### 3) Run the Flow
Open the Playground and test the workflow with the following prompts:
* `Check my remaining vacation balance for this year.`
* `I would like to request time off from October 12th to October 15th for personal reasons.`
* `What is the status of my pending leave request for next week?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the HR assistant, interpreting natural language requests and managing the logic flow.
*   Maintain a professional, helpful, and policy-compliant tone.
*   Prioritize data accuracy when querying HRIS systems.
*   Always confirm the specific dates and leave type before finalizing a request.

### 2) Composio Toolset Node
*   **API Key**: Provide your Workday or HRIS integration key.
*   **Connection Scope**: Ensure the agent has read/write permissions for employee leave and calendar modules.

### 3) Tool Availability
*   **HRIS Connector**: Fetching leave balances and submitting time-off entries.
*   **Calendar API**: Creating events and checking team availability.
*   **Notification Service**: Sending alerts to managers for pending approvals.

---

## Related Solutions
* [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - Streamline new hire documentation and system access.
* [Work Hours Compliance Monitor](../work-hours-compliance-monitor-by-timely/README.md) - Track employee work hours and ensure labor regulation compliance.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automate the creation and configuration of new user accounts.
