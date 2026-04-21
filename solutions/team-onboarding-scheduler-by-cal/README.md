# Team Onboarding Scheduler (Uplizd) - Automated meeting orchestration for new hire integration

## Summary
The Team Onboarding Scheduler (Uplizd) automates the complex task of coordinating onboarding meetings between new hires, department leads, and HR representatives. By leveraging real-time calendar availability and intelligent routing, this workflow eliminates manual scheduling friction, ensures consistent onboarding experiences, and accelerates time-to-productivity for new team members.

---

## Demo
![Team Onboarding Scheduler workflow showing calendar integration and automated meeting invites](image.png)
**Alt text (SEO-ready):** Team Onboarding Scheduler Uplizd workflow, automated meeting orchestration, calendar integration, and new hire onboarding automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c5efbad9-b9e6-59ae-a8d2-f22ef290b2f7)

---

## Category
**Primary category:** Operations automation
**Secondary tags:** onboarding, scheduling, calendar, hr tech, team productivity, composio, ai workflow, meeting management.
This solution bridges the gap between HR systems and team calendars to provide a seamless, automated scheduling experience for growing organizations.

---

## Who is this for?
This workflow is designed for teams looking to standardize their onboarding process and reduce administrative overhead for hiring managers.

- **HR Managers**
    - Automate the scheduling of orientation sessions without manual back-and-forth emails.
- **Department Leads**
    - Ensure new hires are automatically booked for essential team introductions and technical deep-dives.
- **New Hires**
    - Receive a structured, pre-populated onboarding calendar immediately upon joining the company.
- **Operations Specialists**
    - Maintain visibility into onboarding capacity and meeting attendance across the organization.

---

## Features
- **Intelligent Calendar Sync**
    - Automatically queries team member availability via Composio to find optimal meeting slots.
- **Dynamic Participant Routing**
    - Dynamically assigns relevant stakeholders to onboarding meetings based on the new hire's role and department.
- **Automated Invite Generation**
    - Triggers calendar invites with pre-configured agendas and meeting links directly from the workflow.
- **Conflict Resolution Logic**
    - Identifies scheduling overlaps and suggests alternative times based on real-time calendar data.
- **Onboarding Progress Tracking**
    - Logs scheduled sessions to ensure no critical onboarding milestone is missed during the first week.

---

## Use Cases
**New Hire Orientation**
- Automatically schedule the "Day 1" welcome meeting with the direct manager.
- Coordinate group orientation sessions for cohorts of new employees.

**Departmental Integration**
- Book technical setup meetings with the IT department based on hardware provisioning status.
- Schedule introductory 1:1s with key cross-functional team members.

**HR Compliance & Documentation**
- Automate the scheduling of mandatory policy review meetings with HR.
- Ensure all required training sessions are booked within the first 48 hours of employment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Import the workflow into your Uplizd workspace.
3. Connect your calendar provider (e.g., Google Calendar, Outlook) via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific calendar IDs and team member email lists.

### 2) Setup the Nodes
- **Chat Input**: Receives the new hire's details and department information.
- **Agent**: Processes the scheduling request and determines the necessary meeting participants.
- **Composio Toolset**: Executes the calendar lookup and invite creation commands.
- **Chat Output**: Confirms the scheduled meetings and provides a summary to the HR coordinator.

### 3) Run the Flow
Use the Playground to test the scheduling logic:
- `Schedule onboarding meetings for John Doe (Engineering) starting next Monday.`
- `Find availability for the IT team to meet with the new hire in the Marketing department.`
- `Check the calendar for the next available slot for a team orientation session.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for scheduling logic and participant selection.
- Use a model with strong reasoning capabilities to handle multi-participant availability.
- Instruct the agent to prioritize manager availability over secondary stakeholders.
- Ensure the agent is configured to handle time-zone conversions automatically.

### 2) Composio Toolset Node
- Provide your API key within the Composio node settings.
- Ensure the connection scope includes `calendar.read` and `calendar.write` permissions.

### 3) Tool Availability
- **Calendar Search**: Query availability for specific team members.
- **Event Creation**: Generate calendar invites with descriptions and meeting links.
- **Contact Lookup**: Retrieve email addresses for internal team members.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - End-to-end employee lifecycle and onboarding management.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamlined access provisioning and user setup.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automated CRM account creation and configuration.
