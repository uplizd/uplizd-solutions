# Team Onboarding Assistant (Uplizd) - Automated employee welcome and resource provisioning

## Summary
The Team Onboarding Assistant is an intelligent Uplizd workflow designed to automate the complex, multi-step process of integrating new hires into an organization. By leveraging the Composio Toolset to interact with communication platforms like Missive, this solution ensures new team members receive timely access, documentation, and welcome sequences, significantly reducing manual administrative overhead and improving the new hire experience.

---

## Demo
![Team Onboarding Assistant workflow showing automated welcome sequences and resource provisioning via Missive](image.png)
**Alt text (SEO-ready):** Team Onboarding Assistant (Uplizd) workflow automation for employee welcome sequences and resource provisioning using Missive and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4ce7c19b-0bc9-57ac-8b12-fc0b011236dc)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** onboarding, missive, employee experience, automation, hr ops, workflow, composio, team management
- This solution streamlines HR and team operations by automating the repetitive tasks associated with new hire integration and resource access.

---

## Who is this for?
This workflow is designed for teams looking to standardize their onboarding process and reduce time-to-productivity for new hires.

- **HR Managers**
    - Automate the delivery of welcome packets and policy documentation to ensure consistent compliance.
- **Team Leads**
    - Automatically provision access to shared communication channels and project management tools.
- **Operations Specialists**
    - Reduce manual ticket creation and administrative follow-ups during the first week of a new hire.
- **New Hires**
    - Receive a structured, welcoming introduction to company resources without waiting for manual intervention.

---

## Features
- **Automated Welcome Sequences**
    - Trigger personalized welcome messages and onboarding checklists immediately upon a new hire's status change.
- **Resource Provisioning**
    - Automatically add new team members to relevant Missive shared inboxes and collaboration threads.
- **Document Distribution**
    - Securely share essential company handbooks, security policies, and setup guides via automated messaging.
- **Real-time Status Tracking**
    - Monitor onboarding progress and identify bottlenecks where new hires might be missing critical access.
- **Composio-Powered Integration**
    - Seamlessly connect with Missive and other enterprise tools to execute actions without leaving the Uplizd environment.

---

## Use Cases
**New Hire Setup**
- Automatically invite new employees to team-specific Missive inboxes based on their department.
- Send a "Day One" checklist containing links to internal wikis and project management boards.

**Policy & Compliance**
- Distribute mandatory security training links and employee handbooks to new staff via automated email.
- Track acknowledgment of company policies by logging responses directly back into your HR system.

**Team Communication**
- Introduce new members to their respective project leads through automated introductory threads.
- Sync team member contact information and role descriptions across internal communication channels.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Paste the solution URL or upload the provided JSON configuration file.
3. Authenticate your Missive account within the Composio integration settings.
4. Ensure nodes are correctly mapped and the API keys are active before deploying.

### 2) Setup the Nodes
- **Chat Input**: Captures the new hire's details and department information.
- **Agent**: Processes the onboarding logic and determines which resources to provision.
- **Composio Toolset**: Executes the API calls to Missive to invite users and send messages.
- **Chat Output**: Confirms the successful completion of the onboarding tasks to the administrator.

### 3) Run the Flow
Use the Playground to test your onboarding logic:
- `Initialize onboarding for John Doe, email john@example.com, department Engineering.`
- `Send welcome packet and Missive invite to the new Marketing hire.`
- `List all pending onboarding tasks for the current week.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer for the onboarding process.
- Use a clear, instruction-based prompt to define the hierarchy of onboarding tasks.
- Ensure the agent has access to the current list of team resources and documentation URLs.
- Set the temperature to 0.2 to ensure consistent and reliable execution of HR procedures.

### 2) Composio Toolset Node
- Provide your Missive API key to enable the agent to manage team members and communication threads.
- Configure the connection scope to allow "Read" and "Write" access to relevant inboxes and contacts.

### 3) Tool Availability
- **Missive API**: For managing team inboxes, sending messages, and updating contact lists.
- **Notification Service**: For alerting HR managers once onboarding steps are completed.
- **Data Logger**: For maintaining a record of provisioned resources and sent documentation.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - A broader solution for managing general workforce integration tasks.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Specialized onboarding for administrative user roles.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamlines the creation and configuration of new CRM accounts.
