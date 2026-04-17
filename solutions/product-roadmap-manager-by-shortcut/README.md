# Product Roadmap Manager (Uplizd) - Automated feature request organization and epic mapping

## Summary
The Product Roadmap Manager is an intelligent Uplizd workflow that transforms unstructured feature requests into organized product roadmaps. By leveraging the Composio Toolset to interface with project management platforms like Shortcut, this solution automatically categorizes incoming feedback, creates actionable epics, and assigns user stories, ensuring product teams maintain high pipeline velocity and a single source of truth for their development lifecycle.

---

## Demo
![Product Roadmap Manager workflow showing feature request ingestion, epic creation, and roadmap synchronization in Shortcut](image.png)
**Alt text (SEO-ready):** Product Roadmap Manager workflow on Uplizd, automating feature request categorization, epic creation, and roadmap synchronization with Shortcut and project management tools.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/33463b42-66d0-523c-a685-4e716bc6b43c)

---

## Category
- **Primary category:** Product Operations
- **Secondary tags:** product management, roadmap, shortcut, feature requests, agile, epics, user stories, automation
- This solution bridges the gap between customer feedback and engineering execution by automating the administrative overhead of roadmap maintenance.

---

## Who is this for?
This solution is designed for product teams looking to reduce manual ticket management and improve alignment between stakeholders and engineering.

- **Product Managers**
    - Streamline the conversion of customer feedback into structured development tasks without manual data entry.
- **Engineering Leads**
    - Ensure that incoming feature requests are properly scoped and mapped to existing epics for better sprint planning.
- **Customer Success Managers**
    - Gain visibility into the status of requested features by automatically syncing feedback to the product roadmap.
- **Operations Specialists**
    - Maintain data hygiene across the product backlog by enforcing consistent labeling and categorization of new stories.

---

## Features
- **Automated Request Ingestion**
  Real-time processing of incoming feature requests from various channels into a unified backlog.
- **Intelligent Epic Mapping**
  Uses AI to analyze request intent and automatically associate new stories with the correct parent epics.
- **Shortcut Integration**
  Seamlessly creates and updates tasks within Shortcut using the Composio Toolset for reliable API interaction.
- **Priority Scoring**
  Automatically assigns priority levels to new items based on predefined business logic and customer impact signals.
- **Status Synchronization**
  Keeps stakeholders informed by updating roadmap statuses as development progresses from backlog to completion.

---

## Use Cases
**Backlog Grooming**
- Automatically convert raw customer emails into structured user stories with detailed acceptance criteria.
- Batch-process weekly feedback logs to identify trends and create new epics based on recurring requests.

**Sprint Planning**
- Map high-priority feature requests directly to upcoming sprint cycles to ensure alignment with quarterly goals.
- Generate summary reports of roadmap changes to share with cross-functional stakeholders before sprint kickoff.

**Stakeholder Alignment**
- Sync roadmap updates back to CRM or communication tools to notify account managers of feature progress.
- Maintain a clean, searchable product backlog by archiving stale requests and merging duplicate feature submissions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Product Roadmap Manager" template.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Shortcut account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw feature request text or structured feedback data.
- **Agent**: Analyzes the request, determines the epic, and drafts the user story.
- **Composio Toolset**: Executes API calls to create or update items in Shortcut.
- **Chat Output**: Confirms the successful creation of the ticket and provides a summary link.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Create a new user story for the 'Mobile Offline Mode' epic based on this feedback: 'Users are struggling to access reports while on flights.'`
- `Analyze the last 5 feedback items and suggest which ones should be added to the Q3 Roadmap.`
- `Update the 'API Rate Limiting' epic with the new requirements submitted by the Enterprise support team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the product analyst, interpreting user intent and mapping it to technical requirements.
- Instruct the agent to prioritize clarity and adherence to existing epic naming conventions.
- Use a structured JSON output format to ensure the Composio Toolset receives clean data.
- Configure the agent to ask for clarification if a feature request lacks sufficient detail.

### 2) Composio Toolset Node
- Provide your Shortcut API key within the Composio configuration.
- Set the connection scope to allow read/write access to your primary workspace and project boards.

### 3) Tool Availability
- `shortcut_create_story`: For generating new tickets in the backlog.
- `shortcut_update_epic`: For modifying existing epics with new stories.
- `shortcut_search_items`: For checking existing requests to prevent duplicates.

---

## Related Solutions
- [../account-research-agent-by-onepage/README.md](../account-research-agent-by-onepage/README.md) - Gather intelligence on accounts to inform product strategy.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) - Extend automation capabilities to broader operational workflows.
- [../account-relationship-builder-by-dynamics365/README.md](../account-relationship-builder-by-dynamics365/README.md) - Manage stakeholder relationships to better prioritize roadmap items.
