# Box User Onboarding Manager (Uplizd) - Automated user provisioning and group assignment

## Summary
The Box User Onboarding Manager streamlines identity and access management by automating the provisioning of new users and their assignment to specific collaboration groups. This Uplizd AI workflow eliminates manual administrative overhead, ensures consistent security policies across the organization, and accelerates time-to-productivity for new hires by integrating directly with the Box platform.

---

## Demo
![Box User Onboarding Manager workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Box User Onboarding Manager workflow diagram, Uplizd automation for user provisioning, group assignment, and Box API integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/d91e94bd-83b9-5a0c-b95b-5aea882ad759)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** box, user onboarding, identity management, provisioning, automation, saas, composio, ai workflow
- This solution bridges the gap between HR onboarding processes and IT infrastructure by automating user lifecycle management tasks within Box.

---

## Who is this for?
This solution is designed for IT and Operations teams looking to standardize their user lifecycle management.

- **IT Administrator**
    - Automates repetitive account creation and group assignment tasks to reduce ticket volume.
- **HR Operations Manager**
    - Ensures new employees have immediate access to necessary project folders upon their start date.
- **Security Compliance Officer**
    - Maintains consistent access control policies by ensuring users are assigned to the correct, audited security groups.
- **Department Lead**
    - Accelerates team onboarding by ensuring new members are automatically provisioned into relevant collaboration workspaces.

---

## Features
- **Automated Provisioning**
    - Triggers the creation of new user accounts in Box based on verified input data.
- **Dynamic Group Assignment**
    - Automatically maps users to specific collaboration groups based on their department or project role.
- **Real-time API Integration**
    - Utilizes the Composio Toolset to execute secure, authenticated calls directly to the Box API.
- **Error Handling & Validation**
    - Validates user data before execution to prevent provisioning failures or duplicate account creation.
- **Audit-Ready Logging**
    - Captures every onboarding action in the Chat Output node for easy review and compliance reporting.

---

## Use Cases
**New Hire Onboarding**
- Automatically create a Box account for a new employee based on a standardized onboarding form.
- Assign the new user to the "Company-Wide" and "Department-Specific" folders instantly.

**Project-Based Access Management**
- Add existing users to new project-specific groups when a new initiative is launched.
- Remove users from sensitive groups automatically when their project role expires.

**Departmental Scaling**
- Bulk-process group assignments for entire cohorts of new hires during seasonal hiring spikes.
- Sync department-level permissions to ensure all team members have access to the correct documentation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Box User Onboarding Manager template from the solution library.
3. Connect your Box account credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the new user's email, name, and department details.
- **Agent**: Processes the request and determines the required group memberships.
- **Composio Toolset**: Executes the Box API commands to provision users and update group settings.
- **Chat Output**: Confirms successful account creation and group assignment to the administrator.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Provision a new user: john.doe@example.com, Name: John Doe, Department: Engineering`
- `Add user jane.smith@example.com to the Marketing-Assets group`
- `Onboard new user: alex.rivera@example.com, Role: Product Manager, Group: Product-Roadmap`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer, interpreting user requests and mapping them to API actions.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize accuracy in email formatting and group naming conventions.
- Ensure the agent verifies that all required fields are present before triggering the Composio Toolset.

### 2) Composio Toolset Node
- Provide a valid Box API key with sufficient scopes for user management and group administration.
- Ensure the connection scope includes `manage_users` and `manage_groups` permissions.

### 3) Tool Availability
- **Box User Management**: Capability to create, update, and deactivate user accounts.
- **Box Group Management**: Capability to create groups, add members, and manage group-level permissions.
- **Data Validation**: Capability to check for existing users to prevent provisioning conflicts.

---

## Related Solutions
- [../admin-user-onboarding-assistant-by-storeganise/README.md](Admin User Onboarding Assistant) - Streamlines administrative user setup for retail and store management platforms.
- [../workforce-onboarding-automator-by-connecteam/README.md](Workforce Onboarding Automator) - Automates employee onboarding workflows across communication and HR platforms.
- [../account-setup-agent-by-salesforce/README.md](Account Setup Agent) - Automates CRM account creation and configuration for sales teams.
