# Employee Offboarding Security Agent (Uplizd) - Automated SharePoint Access Revocation

## Summary
The Employee Offboarding Security Agent is an automated workflow designed to streamline the secure removal of departing employees from SharePoint environments. By integrating directly with SharePoint via the Composio Toolset, this agent ensures that sensitive organizational data remains protected by automating user access revocation, permission audits, and document ownership transfers, providing a single source of truth for security compliance and reducing manual administrative overhead.

---

## Demo
![Employee Offboarding Security Agent workflow diagram showing SharePoint access revocation and permission cleanup](image.png)
**Alt text (SEO-ready):** Employee Offboarding Security Agent workflow for SharePoint access revocation, automated permission cleanup, and data security using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e457c75c-031b-5d68-95fd-75b1467564e3)

---

## Category
**Primary category:** IT Operations
**Secondary tags:** sharepoint, security, offboarding, access control, compliance, identity management, composio, ai workflow.
This solution automates the critical security lifecycle of employee offboarding to ensure organizational data hygiene and compliance.

---

## Who is this for?
This agent is designed for IT and HR professionals responsible for maintaining secure digital workspaces and enforcing offboarding protocols.

- **IT Security Manager**
    - Ensures consistent enforcement of security policies across all SharePoint sites without manual intervention.
- **HR Operations Specialist**
    - Accelerates the offboarding process by triggering automated access removal the moment an employee status changes.
- **System Administrator**
    - Eliminates "permission creep" by automatically auditing and stripping access rights from inactive accounts.
- **Compliance Officer**
    - Maintains a verifiable audit trail of all access revocation actions to satisfy internal and external security audits.

---

## Features
- **Automated Access Revocation**
    - Instantly removes user permissions across specified SharePoint sites and document libraries upon trigger.
- **Permission Audit Reporting**
    - Generates a summary report of all removed access rights for verification by the security team.
- **Ownership Transfer**
    - Automatically reassigns document ownership from the departing employee to a designated manager or team lead.
- **Real-time Security Sync**
    - Leverages the Composio Toolset to execute commands in real-time, ensuring no delay between offboarding and access termination.
- **Compliance-Ready Logging**
    - Records every action taken by the agent, providing a clear history of security operations for audit purposes.

---

## Use Cases
**Access Lifecycle Management**
- Automatically strip access from SharePoint sites when an employee is marked as "terminated" in the HR system.
- Revoke guest access permissions for external contractors upon project completion.

**Data Security & Governance**
- Identify and remove orphaned accounts that still hold edit permissions on sensitive project folders.
- Ensure that departing employees cannot download or sync files by revoking their active SharePoint sessions.

**Administrative Efficiency**
- Batch process offboarding tasks for multiple employees simultaneously to save hours of manual IT labor.
- Send automated confirmation notifications to department heads once an employee's access has been fully secured.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Employee Offboarding Security Agent template from the solution library.
3. Connect your SharePoint environment via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the employee email and offboarding request details.
- **Agent**: Analyzes the request and determines the necessary SharePoint permission changes.
- **Composio Toolset**: Executes the specific API calls to modify SharePoint user permissions.
- **Chat Output**: Confirms the successful revocation of access and provides a summary report.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Revoke all SharePoint access for user john.doe@company.com and transfer ownership to manager@company.com.`
- `Audit and remove access for all users with 'Contractor' status in the Marketing SharePoint site.`
- `Provide a status report on the offboarding security cleanup for the Finance department.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security orchestrator, interpreting offboarding requests and mapping them to specific security actions.
- Use a model capable of high-precision instruction following (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize security and verify user identities before executing revocation.
- Configure the system prompt to require a confirmation step for bulk permission changes.

### 2) Composio Toolset Node
- Provide a valid SharePoint API key with sufficient administrative scopes (e.g., `Sites.Manage.All`, `User.ReadWrite.All`).
- Ensure the connection is scoped to the specific SharePoint sites requiring management.

### 3) Tool Availability
- **SharePoint User Management**: Capability to list, add, and remove users from sites.
- **Permission Management**: Capability to modify read/write/owner access levels.
- **File/Folder Operations**: Capability to reassign ownership of documents and folders.

---

## Related Solutions
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Monitors and audits administrative access rights across systems.
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) — Streamlines the setup and provisioning for new employees.
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) — Tracks and enforces account-level security and compliance standards.
