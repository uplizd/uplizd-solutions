# PostHog Team Onboarding Coordinator (Uplizd) - Automated team setup and access management

## Summary
The PostHog Team Onboarding Coordinator is an intelligent workflow designed to automate the provisioning of new team members and the configuration of project access within PostHog. By integrating directly with the PostHog API via the Composio Toolset, this solution eliminates manual administrative overhead, ensures consistent permissioning across new hires, and accelerates time-to-productivity for engineering and product teams.

---

## Demo
![PostHog Team Onboarding Coordinator workflow showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** PostHog Team Onboarding Coordinator workflow in Uplizd for automated user provisioning, team access management, and product analytics onboarding.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f7b40cd2-5ef7-5d55-87b9-722e2196b733)

---

## Category
- **Primary category:** Team Operations
- **Secondary tags:** posthog, onboarding, user provisioning, access management, devops, team automation, composio, ai workflow
- This solution streamlines the technical onboarding process by automating repetitive PostHog administrative tasks through intelligent AI-driven orchestration.

---

## Who is this for?
This solution is designed for technical leads and operations managers who need to maintain secure and efficient team environments.

- **Engineering Managers**
    - Automate the addition of new developers to specific PostHog projects without manual console navigation.
- **Product Operations Leads**
    - Ensure consistent access levels for cross-functional team members across multiple product environments.
- **DevOps Engineers**
    - Standardize the onboarding lifecycle to reduce configuration drift and security gaps in analytics access.
- **HR/People Ops Managers**
    - Accelerate the setup of new hire toolkits by triggering automated provisioning workflows upon account creation.

---

## Features
- **Automated User Provisioning**
    - Instantly add new team members to PostHog projects using natural language commands.
- **Role-Based Access Control (RBAC)**
    - Dynamically assign appropriate permissions to ensure team members have the right level of data access.
- **Cross-Project Coordination**
    - Manage user access across multiple PostHog instances or projects from a single centralized interface.
- **Real-time Audit Logging**
    - Maintain a clear record of onboarding actions and permission changes for compliance and security tracking.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to execute secure, authenticated API calls directly to the PostHog platform.

---

## Use Cases
**New Hire Onboarding**
- Automatically invite a new engineer to the core product analytics project on their first day.
- Assign read-only access to junior analysts to ensure data integrity during the training phase.

**Project Access Management**
- Bulk update team permissions when a project moves from development to production status.
- Revoke access for team members transitioning to different departments to maintain security hygiene.

**Administrative Cleanup**
- Identify and remove inactive users from PostHog projects to optimize seat utilization.
- Sync team member lists from internal directories to ensure PostHog access remains current.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the PostHog Team Onboarding Coordinator template from the library.
3. Connect your PostHog API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the onboarding request (e.g., "Add john@company.com to the Mobile App project").
- **Agent**: Processes the intent and maps it to the required PostHog API actions.
- **Composio Toolset**: Executes the authenticated API calls to manage users and roles in PostHog.
- **Chat Output**: Confirms the successful provisioning or reports any configuration errors.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these prompts:
- `Add user alex@company.com to the Web Analytics project with member access.`
- `List all current users in the Mobile App project and verify their roles.`
- `Remove access for user old-dev@company.com from all active PostHog projects.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for administrative tasks, ensuring instructions are translated into precise API calls.
- Use a high-reasoning model (e.g., GPT-4o) for accurate command parsing.
- Set the system prompt to prioritize security and strict adherence to permission schemas.
- Ensure the agent is instructed to verify user existence before attempting to modify access.

### 2) Composio Toolset Node
- Provide your PostHog API Key and Project ID to establish a secure connection.
- Define the scope to include user management and project configuration capabilities.

### 3) Tool Availability
- `posthog_add_user`: Adds a new member to a specified project.
- `posthog_update_user_role`: Modifies the permission level of an existing user.
- `posthog_list_users`: Retrieves current project membership for audit purposes.
- `posthog_remove_user`: Revokes project access for specified users.

---

## Related Solutions
- [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) - Automate CRM user provisioning and role assignment.
- [Admin User Onboarding Assistant (Storeganise)](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamline administrative access for operations platforms.
- [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) - Manage complex team workflows and task assignments.
