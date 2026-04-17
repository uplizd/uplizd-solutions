# Developer Onboarding Assistant (Uplizd) - Automate team setup and project access

## Summary
The Developer Onboarding Assistant is an AI-driven workflow designed to accelerate the integration of new engineers into technical environments. By automating the provisioning of repository access, documentation sharing, and tool configuration, this solution eliminates manual administrative bottlenecks, ensuring new hires reach full productivity on day one while maintaining strict security and access hygiene.

---

## Demo
![Developer Onboarding Assistant workflow showing automated Sentry project access and team provisioning](image.png)
**Alt text (SEO-ready):** Developer Onboarding Assistant workflow for automated team setup, repository access, and Sentry project provisioning using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/975664be-e16f-5173-99fd-ade298f2b3f8)

---

## Category
**Primary category:** Developer Operations
**Secondary tags:** onboarding, devops, sentry, access management, automation, team productivity, composio, ai workflow.
This solution streamlines the technical onboarding lifecycle by programmatically managing developer permissions and project configurations.

---

## Who is this for?
This solution is designed for engineering leaders and operations teams looking to standardize the new hire experience.

* **Engineering Manager**
    * Reduces time spent on manual access requests and permission provisioning for new team members.
* **DevOps Engineer**
    * Ensures consistent environment setup and security compliance across all new developer accounts.
* **Technical Recruiter**
    * Provides a seamless "first day" experience by ensuring all necessary project tools are ready upon arrival.
* **New Developer**
    * Eliminates friction by providing immediate, automated access to required repositories and monitoring tools.

---

## Features
- **Automated Access Provisioning**
    Seamlessly grant repository and project access based on team roles via integrated API connectors.
- **Sentry Project Integration**
    Automatically configure Sentry project alerts and environment monitoring for new developers.
- **Standardized Documentation Delivery**
    Trigger automated welcome messages containing links to internal wikis, style guides, and setup instructions.
- **Role-Based Permission Mapping**
    Utilize logic-based triggers to assign appropriate access levels based on the developer’s specific team or seniority.
- **Real-time Audit Logging**
    Maintain a clear record of all access grants and setup actions for compliance and security reporting.

---

## Use Cases
**New Hire Setup**
* Automatically add a new developer to the relevant Sentry projects and GitHub organizations.
* Send a personalized welcome message with links to the team's internal documentation and onboarding checklist.

**Project Access Management**
* Provision access to specific staging and production environments based on the developer's assigned project.
* Revoke or update access permissions dynamically when a developer changes teams or projects.

**Compliance and Security**
* Ensure all new accounts are created with mandatory security settings and MFA requirements enforced.
* Generate automated reports of all onboarding actions for quarterly security audits.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Developer Onboarding Assistant template from the solution library.
3. Connect your Sentry and GitHub accounts via the Composio Toolset node.
4. Ensure nodes are correctly linked from **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the new hire's details and team assignment.
* **Agent**: Processes the request and determines the necessary access levels.
* **Composio Toolset**: Executes the API calls to provision access and configure tools.
* **Chat Output**: Confirms successful setup and sends the welcome notification.

### 3) Run the Flow
Use the Playground to test the onboarding process with these prompts:
* `Onboard new developer John Doe to the 'Frontend' team with access to the 'Core-App' Sentry project.`
* `Provision access for Sarah Smith to the 'Backend' repository and send the onboarding documentation link.`
* `Check current access status for user 'dev-user-01' and ensure they are added to all 'Production' monitoring projects.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for onboarding logic.
* Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate role mapping.
* Instruction: "You are an expert DevOps assistant. When provided with a new hire's name and team, identify the required tools and permissions, then trigger the necessary Composio actions."
* Ensure the agent is configured to handle missing information by asking the user for clarification before executing provisioning.

### 2) Composio Toolset Node
* Provide your Composio API key in the node settings.
* Ensure the connection scope includes `sentry:write` and `github:write` permissions to allow the agent to modify project settings and access.

### 3) Tool Availability
* **Sentry API**: For project creation, team assignment, and alert configuration.
* **GitHub API**: For repository invitation and team membership management.
* **Notification Service**: For sending automated welcome emails or Slack messages.

---

## Related Solutions
* [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automates administrative account setup and user provisioning.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamlines CRM account creation and configuration.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Orchestrates complex cross-platform business process automations.
