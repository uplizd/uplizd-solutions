# Employee Onboarding Assistant (Uplizd) - Automate new hire provisioning and team integration

## Summary
The Employee Onboarding Assistant is an automated AI workflow designed to streamline the provisioning of new hires within Microsoft Teams. By orchestrating user access, channel assignments, and welcome communications, this solution eliminates manual administrative bottlenecks, ensuring new team members are productive from day one while maintaining consistent organizational hygiene.

---

## Demo
![Employee Onboarding Assistant workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Employee Onboarding Assistant workflow in Uplizd, automating Microsoft Teams user provisioning, channel access, and onboarding tasks via the Composio Toolset.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/336495af-3896-5461-b61d-892ef8b16f6f)

---

## Category
- **Primary category:** HR Operations
- **Secondary tags:** microsoft teams, onboarding, automation, employee lifecycle, composio, ai workflow, provisioning, hr tech
- This solution bridges the gap between HR systems and Microsoft Teams to automate repetitive administrative tasks during the employee onboarding lifecycle.

---

## Who is this for?
This solution is designed for HR and IT teams looking to standardize the new hire experience through intelligent automation.

- **HR Manager**
    - Reduces manual data entry and ensures all new hires receive a consistent, welcoming onboarding experience.
- **IT Administrator**
    - Automates the provisioning of user accounts and access permissions, reducing the risk of configuration errors.
- **Team Lead**
    - Accelerates time-to-productivity for new direct reports by ensuring they are added to relevant project channels immediately.
- **Operations Specialist**
    - Maintains organizational hygiene by standardizing the workflow for adding and removing users across team workspaces.

---

## Features
- **Automated Provisioning**
    - Instantly adds new employees to designated Microsoft Teams channels based on their department or role.
- **Intelligent Welcome Messages**
    - Triggers personalized welcome communications to new hires, providing them with essential resources and team introductions.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely interact with the Microsoft Teams API for real-time user and channel management.
- **Role-Based Access Control**
    - Dynamically assigns team permissions based on input data, ensuring new hires have the correct level of access from the start.
- **Workflow Auditability**
    - Provides a clear, traceable log of all onboarding actions, simplifying compliance and internal auditing processes.

---

## Use Cases
**New Hire Provisioning**
- Automatically add new employees to the "General" and "Department" channels upon hire date.
- Assign specific user roles and permissions within Teams based on the employee's job title.

**Team Integration**
- Send automated welcome messages including links to internal wikis, handbooks, and team contact lists.
- Facilitate team introductions by tagging the new hire in the relevant project channel.

**Administrative Cleanup**
- Sync employee status changes to ensure that offboarded employees are removed from sensitive project channels.
- Generate summary reports of all onboarding activities completed during a specific week or month.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Employee Onboarding Assistant template from the marketplace.
3. Connect your Microsoft Teams account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives employee details (name, email, department, role).
- **Agent**: Processes the input and determines the appropriate Teams channels and welcome message content.
- **Composio Toolset**: Executes the API calls to Microsoft Teams to provision the user and post messages.
- **Chat Output**: Confirms successful onboarding completion or flags errors for review.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Onboard John Doe (j.doe@company.com) to the Engineering team.`
- `Add Sarah Smith to the Marketing and Design channels.`
- `Provision access for the new hire in Sales and send the standard welcome message.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for onboarding logic.
- Use a model capable of structured data extraction (e.g., GPT-4o).
- **Instruction Pattern:**
    - Identify the employee's department and role from the input.
    - Map the department to the pre-defined list of Microsoft Teams channels.
    - Format the welcome message to include the employee's name and relevant team links.

### 2) Composio Toolset Node
- Provide your Microsoft Teams API key within the Composio configuration.
- Set the connection scope to allow `Team.ReadWrite.All` and `Channel.ReadWrite.All` permissions.

### 3) Tool Availability
- `teams_add_member`: Adds a user to a specific channel.
- `teams_send_message`: Posts a welcome message to a channel.
- `teams_list_channels`: Retrieves available channels for mapping.
- `teams_get_user`: Verifies user existence before provisioning.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Automates broader workforce management and onboarding tasks.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Manages CRM account creation and user provisioning.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamlines administrative user access and onboarding.
