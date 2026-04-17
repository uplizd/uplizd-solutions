# Repository Onboarding Manager (Uplizd) - Automate developer access and repository setup

## Summary
The Repository Onboarding Manager is an intelligent Uplizd workflow designed to automate the provisioning of developer access, repository permissions, and environment setup. By leveraging the Composio Toolset to interface with GitHub, this solution eliminates manual configuration bottlenecks, ensures consistent security compliance for new hires, and accelerates team velocity from day one.

---

## Demo
![Repository Onboarding Manager workflow showing GitHub integration and automated access provisioning](image.png)
**Alt text (SEO-ready):** Repository Onboarding Manager Uplizd workflow for automated GitHub access provisioning, developer onboarding, and repository setup.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=github)](https://uplizd.ai/solutions/77fad5a4-5047-51d3-8d64-386d44c2f2e0)

---

## Category
**Primary category:** Operations
**Secondary tags:** github, onboarding, devops, automation, access control, repository management, developer experience, composio.
This solution streamlines the technical onboarding process by synchronizing human resource needs with automated repository access and permission management.

---

## Who is this for?
This solution is designed for engineering and operations teams looking to standardize and accelerate the technical onboarding of new contributors.

*   **Engineering Managers**
    *   Reduce time-to-productivity for new hires by automating access to essential codebases.
*   **DevOps Engineers**
    *   Maintain consistent security posture by programmatically managing repository permissions and team memberships.
*   **HR Operations Specialists**
    *   Trigger automated provisioning workflows immediately upon new hire status updates in the system.
*   **Technical Leads**
    *   Ensure all team members have the correct environment setup and repository access without manual configuration tickets.

---

## Features
- **Automated Access Provisioning**
  Instantly grant repository read/write permissions based on team roles via the Composio GitHub integration.
- **Role-Based Permission Mapping**
  Define granular access levels that automatically apply to new users based on their department or project assignment.
- **Real-Time Audit Logging**
  Track every access request and permission change to maintain a transparent audit trail for security compliance.
- **Environment Setup Automation**
  Trigger automated scripts that prepare local developer environments and sync necessary configuration files.
- **Error Handling & Notifications**
  Receive instant alerts if an access request fails or if a user is missing required credentials, ensuring no onboarding step is skipped.

---

## Use Cases
**New Hire Onboarding**
*   Automatically add new engineers to the appropriate GitHub teams based on their project assignment.
*   Send an automated welcome message with links to documentation and repository setup instructions.

**Project Access Management**
*   Grant temporary access to external contractors for specific repositories with automated expiration dates.
*   Sync repository permissions across multiple GitHub organizations to ensure consistent access levels.

**Security & Compliance Audits**
*   Generate reports of all active repository permissions to identify and revoke access for offboarded employees.
*   Automate the rotation of access tokens and credentials for new team members to maintain high security standards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution in your workspace.
2. Select your target GitHub organization and project repository.
3. Configure your API credentials within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input:** Receives the new hire's details and requested access level.
*   **Agent:** Processes the request and determines the necessary GitHub permission changes.
*   **Composio Toolset:** Executes the API calls to GitHub to update team memberships and repository access.
*   **Chat Output:** Confirms the successful provisioning of access or reports any configuration errors.

### 3) Run the Flow
Use the Playground to test the onboarding logic with these example prompts:
* `Add user 'jdoe' to the 'backend-engineers' team with write access to the 'core-api' repository.`
* `Provision access for new hire 'asmith' to all repositories tagged with 'internal-tools'.`
* `Check current repository permissions for user 'bwayne' and grant access to the 'security-patch' repo.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for permission logic and user validation.
* Use a model capable of structured JSON output for reliable API parameter mapping.
* Instruction pattern: "Identify the user and requested repository," "Verify permission levels against organization policy," and "Execute the Composio tool call."

### 2) Composio Toolset Node
* Requires a valid GitHub Personal Access Token (PAT) or OAuth connection with `repo`, `admin:org`, and `user` scopes.
* Ensure the connection scope is limited to the specific organization being managed.

### 3) Tool Availability
* `github_add_team_member`: Adds a user to a specified GitHub team.
* `github_update_repository_permission`: Modifies individual or team access to a repository.
* `github_get_user_details`: Validates user existence before attempting access changes.

---

## Related Solutions
* [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automates administrative access and user profile setup.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General-purpose automation for complex business process workflows.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamlines account creation and configuration across CRM platforms.
