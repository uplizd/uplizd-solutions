# Team Onboarding Assistant with Slack (Uplizd) - Automate new hire workflows and communication

## Summary
The Team Onboarding Assistant with Slack streamlines the new hire experience by automating administrative tasks, documentation delivery, and team introductions. By integrating Uplizd with Slack, this workflow ensures that every new employee receives consistent, timely information, reducing manual HR overhead and accelerating time-to-productivity for growing teams.

---

## Demo
![Team Onboarding Assistant workflow showing Slack integration for new hire welcome messages and document distribution](image.png)
**Alt text (SEO-ready):** Team Onboarding Assistant with Slack workflow, Uplizd automation, new hire onboarding, Slack integration, HR process automation, employee productivity.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6e30006d-9fb3-5a4e-9fc2-73c313fb6288)

---

## Category
- **Primary category**: Human Resources Operations
- **Secondary tags**: slack, onboarding, hr automation, employee experience, productivity, workflow, composio, internal communications
- This solution bridges the gap between HR management systems and team communication platforms to standardize the onboarding journey.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual onboarding bottlenecks and improve new hire engagement.

- **HR Managers**
    - Automate repetitive welcome tasks and document distribution to ensure compliance and consistency.
- **Team Leads**
    - Facilitate faster team integration by automating Slack introductions and resource sharing.
- **Operations Specialists**
    - Standardize the onboarding pipeline across departments to reduce administrative overhead.
- **New Hires**
    - Receive timely, accurate information and support via Slack, creating a welcoming and organized first-day experience.

---

## Features
- **Automated Slack Notifications**
    - Trigger personalized welcome messages and task reminders directly in Slack channels upon new hire entry.
- **Document Distribution**
    - Automatically share onboarding handbooks, policy documents, and setup guides via the Composio Toolset.
- **Task Tracking**
    - Monitor the completion of onboarding milestones and nudge employees or managers when action is required.
- **Real-time Integration**
    - Syncs seamlessly with Slack and HR platforms to ensure data accuracy and immediate communication.
- **Customizable Workflows**
    - Adapt the onboarding sequence to specific roles or departments using flexible AI logic.

---

## Use Cases
**New Hire Welcome**
- Automatically send a welcome message to the team channel when a new employee is added to the system.
- Deliver a curated list of "first-day" links and resources to the new hire's private Slack thread.

**Administrative Compliance**
- Prompt new hires to sign necessary documents or complete profile setups via automated Slack reminders.
- Track the status of onboarding checklists and report completion metrics to the HR dashboard.

**Team Integration**
- Schedule automated "coffee chat" introductions between the new hire and key team members.
- Provide automated answers to common internal FAQs regarding office policies or software access.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Slack and HR platform connections within the Uplizd dashboard.
4. Ensure nodes are correctly connected and all required API keys are active.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger (e.g., new employee added to HR system).
- **Agent**: Processes the onboarding logic and determines the appropriate Slack communication.
- **Composio Toolset**: Executes actions like sending Slack messages or fetching document links.
- **Chat Output**: Confirms the successful delivery of onboarding tasks and updates the status.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these prompts:
- `Send a welcome message to the #general channel for the new hire, John Doe.`
- `Check if the onboarding handbook has been sent to the new hire and remind them if not.`
- `Schedule a team introduction message for the new hire in the engineering Slack channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the HR coordinator, managing the flow of information and tone of communication.
- Maintain a professional, welcoming, and helpful tone.
- Prioritize clear, actionable instructions for the new hire.
- Ensure all sensitive data is handled according to internal privacy policies.

### 2) Composio Toolset Node
Requires an active Slack API token and relevant HR platform credentials. Ensure the scope includes `channels:write`, `chat:write`, and `users:read`.

### 3) Tool Availability
- **Slack API**: For channel messaging and direct user communication.
- **HRIS Connector**: For fetching new hire data and status updates.
- **Document Management**: For retrieving and sharing onboarding assets.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - A broader solution for managing end-to-end workforce lifecycle tasks.
- [Workforce Onboarding Automator by Connecteam](../workforce-onboarding-automator-by-connecteam/README.md) - Specialized onboarding automation using the Connecteam platform.
- [Admin User Onboarding Assistant by Storeganise](../admin-user-onboarding-assistant-by-storeganise/README.md) - Focused onboarding for administrative and platform users.
