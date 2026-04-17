# New Hire Onboarding Bot (Uplizd) - Automated Employee Onboarding via Slack

## Summary
The New Hire Onboarding Bot is an intelligent Uplizd workflow designed to streamline the employee induction process by automating task assignments, documentation delivery, and team introductions directly within Slack. By leveraging the Composio Toolset to interface with HR and communication platforms, this solution ensures a consistent, high-velocity onboarding experience that reduces manual administrative overhead and improves new hire time-to-productivity.

---

## Demo
![New Hire Onboarding Bot workflow showing Slack integration and automated task assignment](image.png)
**Alt text (SEO-ready):** New Hire Onboarding Bot Uplizd workflow automating Slack employee onboarding, task management, and team integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ec30d29c-faff-5450-9a9e-1b3ba8640a6f)

---

## Category
- **Primary category:** HR Operations
- **Secondary tags:** slack, onboarding, automation, employee experience, hr, workflow, composio, internal communications
- This solution bridges the gap between HR systems and team communication platforms to create a seamless, automated onboarding lifecycle.

---

## Who is this for?
This solution is designed for organizations looking to standardize their employee induction process and reduce the manual burden on HR teams.

- **HR Manager**
    - Automates the delivery of welcome packets and policy documents to ensure 100% compliance.
- **Operations Lead**
    - Standardizes the onboarding checklist across departments to maintain operational consistency.
- **Team Lead**
    - Automatically triggers Slack introductions and tool access requests for new team members.
- **New Hire**
    - Receives a guided, interactive experience that answers common questions and provides immediate access to resources.

---

## Features
- **Automated Slack Notifications**
    - Triggers personalized welcome messages and task reminders directly in the new hire's Slack workspace.
- **Document Distribution**
    - Automatically shares essential onboarding documentation and handbooks based on the hire's role and department.
- **Task Management Integration**
    - Syncs onboarding milestones with project management tools to track completion status in real-time.
- **Interactive Q&A Agent**
    - Uses an AI-powered agent to answer common new hire questions regarding company culture, benefits, and IT setup.
- **Cross-Platform Sync**
    - Connects with HRIS and identity management systems via the Composio Toolset to provision access automatically.

---

## Use Cases
**Standardized Induction**
- Automating the delivery of the employee handbook and security policy acknowledgment forms.
- Scheduling automated check-ins for the first 30, 60, and 90 days of employment.

**Team Integration**
- Automatically posting a welcome announcement in the relevant department Slack channel.
- Facilitating "coffee chat" scheduling between the new hire and key team members.

**Administrative Automation**
- Triggering IT hardware request tickets immediately upon hire profile creation.
- Updating internal employee directories and Slack profiles with the new hire's details.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided JSON configuration file for the New Hire Onboarding Bot.
3. Connect your Slack workspace and HRIS credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives new hire triggers and manual onboarding requests from HR staff.
- **Agent**: Processes onboarding logic, interprets employee data, and determines the next step in the induction sequence.
- **Composio Toolset**: Executes actions across Slack, HRIS, and task management platforms to provision access and send messages.
- **Chat Output**: Delivers confirmation messages and status updates back to the Slack channel or HR dashboard.

### 3) Run the Flow
Use the Uplizd Playground to test your onboarding logic:
- `Initiate onboarding for John Doe, department: Engineering, start date: 2023-11-01`
- `Send welcome packet and Slack invite to the new hire in the Marketing team`
- `Check status of onboarding tasks for all new hires starting this week`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central coordinator for all onboarding communications and task scheduling.
- Instruct the agent to maintain a welcoming, professional, and helpful tone.
- Define the hierarchy of onboarding tasks to ensure critical security steps are completed first.
- Configure the agent to escalate incomplete tasks to the HR Manager after a set time threshold.

### 2) Composio Toolset Node
- Provide your Slack API token and HRIS integration keys within the Composio configuration.
- Set the connection scope to allow the agent to read user lists, post messages, and update task statuses.

### 3) Tool Availability
- **Slack API**: For sending direct messages, creating channels, and posting announcements.
- **HRIS Connector**: For retrieving employee metadata and updating onboarding status.
- **Task Manager**: For creating and tracking onboarding checklist items.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - A broader tool for managing full-scale workforce onboarding and compliance.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Specialized assistant for provisioning administrative access and permissions.
- [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-driven support workflow for handling incoming inquiries and ticket triage.
