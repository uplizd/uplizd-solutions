# New User Onboarding Assistant (Uplizd) - Automated Salesmate setup and team member ramp-up

## Summary
The New User Onboarding Assistant is an automated Uplizd workflow designed to streamline the integration of new team members into Salesmate. By orchestrating account configuration, resource provisioning, and best-practice guidance, this solution ensures that new hires reach peak productivity faster while maintaining organizational data hygiene and standard operating procedures.

---

## Demo
![New User Onboarding Assistant workflow showing Chat Input, Agent, Salesmate Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Uplizd New User Onboarding Assistant workflow for Salesmate, featuring automated account setup, team member ramp-up, and CRM integration via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a72a3b68-ea02-5a34-bfd4-79cf2fa325b8)

---

## Category
**Primary category:** Sales Operations  
**Secondary tags:** salesmate, onboarding, crm, employee ramp-up, automation, workflow, composio, sales enablement  
This solution automates the technical and administrative hurdles of onboarding to ensure new sales team members are fully operational within their CRM environment from day one.

---

## Who is this for?
This solution is designed for organizations looking to standardize their sales onboarding process and reduce manual administrative overhead.

*   **Sales Operations Manager**
    *   Ensures consistent configuration across all new user accounts to maintain data integrity.
*   **Sales Enablement Lead**
    *   Automates the delivery of training materials and best-practice documentation to new hires.
*   **IT Administrator**
    *   Reduces manual ticket volume by automating user provisioning and permission settings in Salesmate.
*   **New Sales Representative**
    *   Provides an immediate, guided path to understanding CRM workflows and daily task management.

---

## Features
- **Automated Account Provisioning**
    Streamlines the creation and setup of new user profiles within Salesmate, ensuring correct role-based access.
- **Guided Onboarding Path**
    Delivers step-by-step instructions and resource links directly to the user to accelerate their learning curve.
- **Standardized CRM Configuration**
    Applies consistent settings, pipeline views, and notification preferences to every new account automatically.
- **Real-time Integration Sync**
    Utilizes the Composio Toolset to bridge Salesmate with external communication and task management platforms.
- **Compliance & Hygiene Checks**
    Validates that new user setups adhere to company security policies and data entry standards from the start.

---

## Use Cases
**Automated User Setup**
*   Automatically assign new sales reps to the correct team and pipeline in Salesmate upon account creation.
*   Configure default email signatures and notification settings to match company branding standards.

**Training & Enablement**
*   Trigger a personalized welcome message containing links to internal sales playbooks and product documentation.
*   Schedule automated check-ins to monitor the user's progress through their initial CRM setup tasks.

**Operational Efficiency**
*   Sync new user data with internal Slack or Microsoft Teams channels to notify the team of a new hire.
*   Audit new user permissions to ensure they have access only to the specific modules required for their role.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the New User Onboarding Assistant JSON template provided in the solution repository.
3. Connect your Salesmate API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the new user's details and onboarding request.
*   **Agent**: Processes the request using instructions to configure the user profile and provide guidance.
*   **Composio Toolset**: Executes the necessary API calls to Salesmate for account updates and resource provisioning.
*   **Chat Output**: Delivers the confirmation of setup and the onboarding roadmap to the user.

### 3) Run the Flow
Use the Playground to test the onboarding logic with these prompts:
* `Setup a new user account for John Doe with the Sales Representative role.`
* `Provide the onboarding checklist and Salesmate best practices for a new hire.`
* `Verify if the new user account has the correct pipeline access and notification settings.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for onboarding tasks.
*   Maintain a professional, encouraging tone suitable for new employees.
*   Prioritize security and accuracy when modifying CRM user settings.
*   Always reference the latest company documentation provided in the system prompt.

### 2) Composio Toolset Node
*   **API Key**: Provide your Salesmate API key to enable secure tool execution.
*   **Connection Scope**: Ensure the toolset has `write` access to user management and `read` access to configuration settings.

### 3) Tool Availability
*   `salesmate_create_user`: Provisions new accounts.
*   `salesmate_update_permissions`: Adjusts role-based access controls.
*   `salesmate_get_documentation`: Retrieves internal onboarding resources.
*   `salesmate_verify_config`: Audits account settings against company standards.

---

## Related Solutions
* [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) - Automates user provisioning and CRM configuration for Salesforce environments.
* [Workforce Onboarding Automator (Connecteam)](../workforce-onboarding-automator-by-connecteam/README.md) - Streamlines general employee onboarding and internal communications.
* [Admin User Onboarding Assistant (Storeganise)](../admin-user-onboarding-assistant-by-storeganise/README.md) - Specialized onboarding flow for administrative roles in Storeganise.
