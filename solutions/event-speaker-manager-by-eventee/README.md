# Event Speaker Manager (Uplizd) - Streamline speaker coordination and event logistics

## Summary
The Event Speaker Manager by Uplizd is an intelligent workflow designed to automate the end-to-end coordination of event speakers. By integrating directly with Eventee, this solution centralizes speaker data, automates outreach, and maintains a single source of truth for session details, significantly reducing manual administrative overhead and improving pipeline velocity for event organizers.

---

## Demo
![Event Speaker Manager workflow dashboard showing automated speaker data synchronization and session assignment](image.png)
**Alt text (SEO-ready):** Event Speaker Manager Uplizd workflow automation for event logistics, speaker data synchronization, and Eventee integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5613b9f6-eb32-59b7-9e09-3d561e706d87)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** event management, speaker coordination, eventee, workflow automation, data synchronization, logistics, ai agent, scheduling
- This solution bridges the gap between raw speaker data and event platform execution, ensuring seamless data hygiene and operational efficiency.

---

## Who is this for?
This solution is built for professionals tasked with managing complex event logistics and speaker relationships.

- **Event Coordinator**
    - Automates the collection and verification of speaker bios, headshots, and session requirements.
- **Operations Manager**
    - Ensures event data consistency across platforms, reducing manual entry errors and scheduling conflicts.
- **Community Manager**
    - Facilitates timely communication and follow-ups with speakers to keep them engaged throughout the event lifecycle.
- **Marketing Lead**
    - Maintains accurate speaker profiles for promotional materials and event landing pages.

---

## Features
- **Automated Speaker Sync**
    - Real-time synchronization of speaker profiles and session assignments between your database and Eventee.
- **Intelligent Data Validation**
    - Automatically checks for missing speaker information or conflicting session times before pushing updates.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely connect and execute actions within the Eventee API environment.
- **Dynamic Status Tracking**
    - Monitors the onboarding status of each speaker, from initial invitation to final session confirmation.
- **Centralized Communication Hub**
    - Triggers automated notifications and reminders to speakers based on their current status in the event pipeline.

---

## Use Cases
**Speaker Onboarding**
- Automatically send intake forms to new speakers upon session assignment.
- Update speaker status to 'Confirmed' once all required documentation is uploaded.

**Session Logistics Management**
- Sync session time slots and room assignments directly to the Eventee platform.
- Flag sessions with missing speaker details to ensure no gaps in the event agenda.

**Event Data Hygiene**
- Identify and resolve duplicate speaker entries across multiple event tracks.
- Bulk update speaker bios and headshots to ensure consistent branding across all event touchpoints.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the 'Event Speaker Manager' template.
2. Click 'Import' to initialize the workflow in your workspace.
3. Authenticate your Eventee account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives commands or triggers for speaker updates.
- **Agent**: Processes natural language requests to manage speaker data.
- **Composio Toolset**: Executes API calls to Eventee for data retrieval and updates.
- **Chat Output**: Returns confirmation messages or error logs to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `List all speakers currently missing a bio for the upcoming conference.`
- `Update the session time for speaker John Doe to 2:00 PM in Eventee.`
- `Sync all confirmed speakers from the spreadsheet to the Eventee event portal.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the operational brain, interpreting event requirements and executing logic.
- Use a model with strong reasoning capabilities (e.g., GPT-4o).
- Instruction: "You are an expert event coordinator. Always verify speaker data against the Eventee API before confirming updates."
- Instruction: "If a speaker record is incomplete, request the missing information from the user."

### 2) Composio Toolset Node
- Provide your Eventee API key within the Composio configuration.
- Set the connection scope to 'Read/Write' to allow the agent to manage speaker profiles and session data.

### 3) Tool Availability
- `get_speaker_details`: Retrieve current profile data.
- `update_speaker_profile`: Push changes to Eventee.
- `list_event_sessions`: Fetch current schedule for validation.
- `send_speaker_notification`: Trigger automated outreach.

---

## Related Solutions
- [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Manage collaborative workshop logistics and participant engagement.
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline team member onboarding and data management.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for complex operational pipelines.
