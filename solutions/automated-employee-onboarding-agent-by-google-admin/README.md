# Automated Employee Onboarding Agent (Uplizd) - Streamline new hire setup with automated Google Workspace provisioning

## Summary
The Automated Employee Onboarding Agent is an intelligent workflow designed to eliminate manual administrative bottlenecks during the new hire lifecycle. By integrating directly with Google Workspace via the Composio Toolset, this solution automates user account creation, group assignment, and access provisioning. It serves as a single source of truth for IT and HR operations, ensuring consistent onboarding hygiene, reducing manual configuration errors, and significantly accelerating the time-to-productivity for new employees.

---

## Demo
![Automated Employee Onboarding Agent workflow showing Google Workspace user provisioning and group assignment](image.png)

**Alt text (SEO-ready):** Automated Employee Onboarding Agent (Uplizd) workflow for Google Workspace user provisioning, account setup, and automated onboarding tasks.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/887ddc1b-6557-566c-918f-a4ade18b119b)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** google workspace, onboarding, automation, identity management, hr ops, composio, ai workflow, provisioning
- This solution bridges the gap between HR requests and IT infrastructure, automating repetitive identity management tasks.

---

## Who is this for?
This solution is designed for teams looking to standardize their technical onboarding process through automation.

- **IT Administrators**
    - Automate the creation of user accounts and email aliases to save hours of manual entry per hire.
- **HR Operations Managers**
    - Ensure new hires have immediate access to required tools and systems on their first day.
- **Office Managers**
    - Maintain consistent security and access policies across the organization without manual oversight.
- **Startup Founders**
    - Scale team growth rapidly by removing administrative friction from the employee onboarding pipeline.

---

## Features
- **Automated User Provisioning**
    - Instantly create new user accounts in Google Workspace based on provided employee details.
- **Dynamic Group Assignment**
    - Automatically add new hires to relevant department-specific mailing lists and security groups.
- **Secure Access Management**
    - Standardize permissions and access levels to ensure compliance from the moment of hire.
- **Real-time Integration**
    - Leverages the Composio Toolset to execute commands directly within your Google Workspace environment.
- **Error-Free Execution**
    - Minimizes human error in account configuration by following a predefined, repeatable logic flow.

---

## Use Cases
**New Hire Setup**
- Automatically generate professional email addresses and credentials for incoming staff.
- Provision access to shared company resources and department-specific Google Drive folders.

**Departmental Scaling**
- Assign users to specific Google Groups based on their role or team designation.
- Update organizational unit (OU) structures automatically as the company grows.

**Compliance & Hygiene**
- Ensure all new accounts follow company naming conventions and security standards.
- Audit onboarding status by tracking successful account creation events in your logs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to access the solution template.
2. Select your workspace and project destination.
3. Configure your Google Workspace credentials within the Composio connection settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives employee details (Name, Role, Department).
- **Agent**: Processes the request and determines the necessary provisioning steps.
- **Composio Toolset**: Executes the API calls to Google Workspace for account creation.
- **Chat Output**: Confirms successful provisioning and provides account details.

### 3) Run the Flow
Use the Playground to test your onboarding automation:
- `Create a new user account for Jane Doe in the Marketing department.`
- `Provision a new employee, John Smith, and add him to the Engineering group.`
- `Set up a new user account for Sarah Connor with access to the Sales team resources.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for identity management tasks.
- Instruction: Act as an IT provisioning assistant that maps human-readable requests to Google Workspace actions.
- Instruction: Validate all required fields (email format, department) before executing account creation.
- Instruction: Provide clear confirmation messages once the user is successfully provisioned.

### 2) Composio Toolset Node
- Requires a valid Google Workspace API key or OAuth connection.
- Ensure the connection scope includes `admin.directory.user` and `admin.directory.group` permissions.

### 3) Tool Availability
- `google_workspace_create_user`: Creates the identity in the directory.
- `google_workspace_add_to_group`: Assigns the user to specific mailing or security groups.
- `google_workspace_update_user`: Modifies attributes or organizational units as needed.

---

## Related Solutions
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Monitor and audit user permissions across your organization.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate account creation and management within Salesforce.
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) — Manage employee onboarding workflows and task tracking.
