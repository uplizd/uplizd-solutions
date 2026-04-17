# Developer Onboarding Assistant (Uplizd) - Streamline repository access and environment setup for new engineers

## Summary
The Developer Onboarding Assistant is an automated Uplizd workflow designed to accelerate the technical integration of new team members by managing repository access, environment configuration, and documentation provisioning. By leveraging the Bitbucket API via the Composio Toolset, this solution eliminates manual setup bottlenecks, ensuring developers have immediate access to the codebases and tools required to contribute from day one.

---

## Demo
![Developer Onboarding Assistant workflow showing automated Bitbucket repository access and environment provisioning](image.png)
**Alt text (SEO-ready):** Developer Onboarding Assistant (Uplizd) workflow for automated Bitbucket repository access, environment setup, and team member provisioning.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/04a90240-322f-5349-ad8b-65d0750c7c97)

---

## Category
**Primary category:** Operations  
**Secondary tags:** developer experience, bitbucket, onboarding, automation, devops, repository management, composio, ai workflow  
This solution optimizes the developer lifecycle by automating repetitive access management tasks and environment configuration workflows.

---

## Who is this for?
This solution is designed for engineering and operations teams looking to reduce time-to-productivity for new hires.

* **Engineering Managers**
    * Reduce the administrative burden of manual repository permissions and access requests.
* **DevOps Engineers**
    * Standardize environment setup processes across the organization to ensure consistent tooling.
* **New Hires**
    * Gain immediate, friction-free access to necessary project repositories and documentation.
* **HR/People Operations**
    * Ensure compliance and security by automating the offboarding and onboarding access lifecycle.

---

## Features
- **Automated Repository Provisioning**
  Instantly grant access to specific Bitbucket repositories based on team roles and project requirements.
- **Environment Configuration Sync**
  Automatically trigger setup scripts or documentation links to configure local development environments.
- **Role-Based Access Control (RBAC)**
  Integrate with existing identity providers to ensure developers only receive the access levels appropriate for their seniority.
- **Real-time Status Notifications**
  Send automated updates via chat or email once the onboarding workflow successfully completes.
- **Audit-Ready Logging**
  Maintain a clear record of all access grants and setup actions for security and compliance reporting.

---

## Use Cases
**New Hire Repository Access**
* Automatically add new developers to the correct Bitbucket project groups based on their department.
* Provision read/write permissions to specific microservice repositories during the first day of onboarding.

**Environment Setup Automation**
* Trigger a personalized onboarding checklist containing links to internal documentation and setup guides.
* Automatically assign Jira tickets or tasks related to environment setup to the new developer.

**Security and Compliance**
* Revoke access automatically when a developer transitions to a different project or leaves the team.
* Ensure all new repository access requests are logged and verified against internal security policies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to access the solution template.
2. Select your workspace and click "Import Flow" to add the workflow to your dashboard.
3. Configure your Bitbucket API credentials within the Composio Toolset settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the new hire's name, email, and team/project details.
* **Agent**: Processes the request and determines the necessary repository permissions.
* **Composio Toolset**: Executes the Bitbucket API calls to manage repository access and user groups.
* **Chat Output**: Confirms the successful completion of the onboarding tasks to the requester.

### 3) Run the Flow
Use the Playground to test the onboarding process with these example prompts:
* `Onboard new hire John Doe (jdoe@company.com) to the 'backend-core' and 'api-gateway' repositories.`
* `Grant read-only access to the 'documentation-portal' repository for the new intern.`
* `List all current repository access permissions for the 'frontend-team' group.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for repository management.
* Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Identify the requested repositories and user email, then map these to the correct Bitbucket API calls."
* Instruction: "Confirm the action success and provide a summary of the permissions granted."

### 2) Composio Toolset Node
* Requires a valid Bitbucket API key with `repo` and `team` scope permissions.
* Ensure the Bitbucket integration is active within your Composio account.

### 3) Tool Availability
* `bitbucket_add_user_to_repository`: Adds a user to a specific project or repo.
* `bitbucket_get_repository_list`: Fetches available repositories for validation.
* `bitbucket_create_pull_request`: Optional automation for initial repository setup tasks.

---

## Related Solutions
* [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Automates general employee onboarding tasks and HR workflows.
* [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Manages administrative access and user provisioning for platform admins.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates account creation and configuration within CRM systems.
