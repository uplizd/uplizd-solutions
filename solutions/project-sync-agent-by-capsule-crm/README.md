# Project Sync Agent (Uplizd) - Automated CRM project alignment and status synchronization

## Summary
The Project Sync Agent is an intelligent Uplizd workflow designed to bridge the gap between client communications and CRM project data. By leveraging the Composio Toolset to interface with Capsule CRM, this agent automatically updates project statuses, logs communication milestones, and ensures that project delivery timelines remain accurate, providing RevOps and project managers with a single source of truth for all client engagements.

---

## Demo
![Project Sync Agent workflow diagram showing Chat Input, Agent node, Composio Toolset, and Chat Output](image.png)
**Alt text (SEO-ready):** Project Sync Agent workflow in Uplizd, demonstrating automated CRM data synchronization, project status updates, and client communication tracking via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/10e41b9c-627d-5aad-bc05-57540576dbd6)

---

## Category
**Primary category:** CRM data integration
**Secondary tags:** crm, capsule, project management, data sync, workflow automation, revops, composio, ai agent
This solution streamlines project hygiene by keeping CRM records in perfect sync with real-time delivery status.

---

## Who is this for?
This solution is built for teams managing complex client projects who need to reduce manual data entry and improve reporting accuracy.

*   **Project Managers**
    *   Automate status updates to ensure stakeholders see real-time progress without manual logging.
*   **RevOps Specialists**
    *   Maintain high-quality CRM data hygiene by syncing project milestones directly from communication threads.
*   **Account Executives**
    *   Gain instant visibility into project health and delivery status before client renewal or upsell conversations.
*   **Operations Leads**
    *   Standardize project tracking workflows across the organization to reduce administrative overhead.

---

## Features
- **Automated CRM Sync**
  Seamlessly push project updates from communication logs into Capsule CRM fields using the Composio Toolset.
- **Real-time Status Tracking**
  Monitor project milestones and delivery phases with automated triggers that update CRM records as work progresses.
- **Intelligent Data Mapping**
  Extract key project details from unstructured chat or email inputs and map them accurately to specific CRM project objects.
- **Communication Logging**
  Automatically append client feedback and project-related discussions to the corresponding CRM account profile.
- **Error-Resilient Pipeline**
  Built-in validation ensures that data syncs only occur when all required project parameters are met, preventing CRM clutter.

---

## Use Cases
**Project Status Updates**
*   Automatically transition a project from "In Progress" to "Review" when a final deliverable is uploaded.
*   Update project completion percentages based on task completion signals detected in team communications.

**Client Communication Alignment**
*   Log critical client feedback directly into the CRM project notes to ensure the delivery team is aligned with client expectations.
*   Flag stalled projects in the CRM when no communication activity is detected for a predefined window (e.g., 5 business days).

**Data Hygiene & Reporting**
*   Standardize project naming conventions by automatically formatting inputs before they are pushed to the CRM.
*   Sync cross-platform project metadata to ensure reports in the CRM reflect the actual status of external delivery tools.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your project dashboard.
3. Connect your Capsule CRM account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives project status updates or client communication summaries.
*   **Agent**: Processes the input, extracts key project metrics, and determines the necessary CRM action.
*   **Composio Toolset**: Executes the API calls to Capsule CRM to update records or create new entries.
*   **Chat Output**: Confirms the successful synchronization and provides a summary of the CRM update.

### 3) Run the Flow
Use the Playground to test your sync logic with these prompts:
* `Update project 'Website Redesign' to status 'Completed' and log 'Client approved final mockups' in the notes.`
* `Check the status of the 'Q4 Marketing Campaign' project and update the delivery date to next Friday.`
* `Sync the latest client feedback from the email thread to the 'Enterprise Migration' project in Capsule.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that parses natural language into structured CRM commands.
*   Use a model capable of high-precision instruction following (e.g., GPT-4o or Claude 3.5 Sonnet).
*   System prompt should emphasize strict adherence to CRM field schemas.
*   Enable tool-calling capabilities to allow the agent to invoke the Composio Toolset dynamically.

### 2) Composio Toolset Node
*   **API Key**: Provide your Capsule CRM API key within the Composio configuration.
*   **Connection Scope**: Ensure the connection has read/write permissions for Projects, Contacts, and Notes.

### 3) Tool Availability
*   `capsule_crm_update_project`: Updates existing project status and metadata.
*   `capsule_crm_add_note`: Appends communication logs to project profiles.
*   `capsule_crm_search_project`: Locates project IDs based on project names provided in the chat.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize multi-platform CRM data with conflict resolution.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate data cleanup and formatting for CRM records.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage sales pipeline stages and automate follow-up tasks.
