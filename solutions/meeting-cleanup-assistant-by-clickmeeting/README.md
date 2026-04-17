# Meeting Cleanup Assistant (Uplizd) - Automate meeting archival and storage optimization

## Summary
The Meeting Cleanup Assistant is an intelligent Uplizd workflow designed to streamline digital workspace hygiene by automatically identifying, archiving, and managing stale meeting data. By leveraging the ClickMeeting integration, this solution helps operations teams and project managers maintain a single source of truth, reduce storage overhead, and ensure pipeline velocity by keeping meeting records organized and compliant.

---

## Demo
![Meeting Cleanup Assistant workflow dashboard showing automated archival triggers and storage management status](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Cleanup Assistant workflow for automated ClickMeeting archival, data hygiene, and storage optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/12f898c8-9c85-598e-8db8-6c2f96325380)

---

## Category
- **Primary category**: Operations automation
- **Secondary tags**: clickmeeting, data hygiene, storage management, workflow automation, meeting archival, composio, ai workflow
- This solution bridges the gap between high-volume meeting activity and efficient data governance through automated lifecycle management.

---

## Who is this for?
This solution is designed for professionals managing high-frequency meeting environments who need to maintain clean, searchable, and compliant records.

- **Operations Manager**
    - Automates the cleanup of legacy meeting data to maintain workspace performance and reduce manual administrative overhead.
- **Project Lead**
    - Ensures that historical meeting artifacts are archived systematically, providing a clear audit trail for team retrospectives.
- **IT Administrator**
    - Optimizes cloud storage utilization by enforcing retention policies on inactive meeting recordings and transcripts.
- **Compliance Officer**
    - Maintains data hygiene standards by ensuring sensitive meeting data is handled according to organizational retention protocols.

---

## Features
- **Automated Archival Triggers**
    - Automatically detects meetings that have passed their retention period and triggers archival processes via the Composio Toolset.
- **Intelligent Storage Optimization**
    - Identifies large or redundant meeting files and moves them to cold storage to free up active workspace capacity.
- **ClickMeeting Integration**
    - Utilizes deep integration with ClickMeeting to perform real-time data retrieval and management actions without manual intervention.
- **Customizable Retention Policies**
    - Allows users to define specific time-based rules for when a meeting should be flagged for cleanup or permanent deletion.
- **Audit Logging**
    - Generates detailed logs of all cleanup actions, providing transparency into which meetings were archived or removed.

---

## Use Cases
**Meeting Lifecycle Management**
- Automatically archive meeting recordings older than 90 days to maintain a clean dashboard.
- Move transcripts from completed project syncs to a centralized documentation repository.

**Storage Cost Reduction**
- Identify and delete duplicate meeting assets that exceed storage quotas.
- Flag inactive meeting rooms for decommissioning to optimize subscription usage.

**Compliance and Governance**
- Ensure all meeting data is purged after the mandatory legal retention window expires.
- Maintain a consistent naming and archival structure across all team meeting records.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your ClickMeeting account via the Composio integration settings.
4. Ensure nodes are correctly mapped from Chat Input to the Agent and verify the toolset connection.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled commands to initiate the cleanup process.
- **Agent**: Analyzes meeting metadata against defined retention policies to determine which items require action.
- **Composio Toolset**: Executes the specific API calls to ClickMeeting for archiving or deleting records.
- **Chat Output**: Returns a summary report of all processed meetings and storage space recovered.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `List all meetings older than 60 days and prepare them for archival.`
- `Archive all recordings from the 'Q3 Project' folder and move them to cold storage.`
- `Run a cleanup audit and report how much storage space can be reclaimed.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making layer for your data retention strategy.
- Focus on identifying meeting timestamps and status flags.
- Prioritize accuracy when filtering meetings to prevent accidental deletion of active records.
- Maintain a neutral, reporting-focused tone when summarizing cleanup results.

### 2) Composio Toolset Node
- Provide your ClickMeeting API credentials within the Composio dashboard.
- Ensure the connection scope includes `read` and `write` permissions for meeting management.

### 3) Tool Availability
- **List Meetings**: Retrieves metadata for all meetings within a specified date range.
- **Archive Meeting**: Moves meeting data to a secure, long-term storage state.
- **Delete Meeting**: Permanently removes meeting assets based on policy triggers.
- **Get Storage Stats**: Provides real-time data on current usage and potential savings.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automates the resolution and cleanup of stale action items.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks the efficiency and status of internal team workflows.
- [Workspace Setup Optimizer](../workspace-setup-optimizer-by-clockify/README.md) — Streamlines workspace configuration and time-tracking data.
