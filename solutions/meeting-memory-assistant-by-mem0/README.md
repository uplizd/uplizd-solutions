# Meeting Memory Assistant (Uplizd) - Automate meeting recall and context retention

## Summary
The Meeting Memory Assistant leverages the Mem0 AI layer to transform unstructured meeting transcripts into a persistent, searchable knowledge base. By automatically extracting action items, decisions, and key context, this workflow ensures that teams maintain a single source of truth across recurring syncs, significantly reducing context switching and improving pipeline velocity.

---

## Demo
![Meeting Memory Assistant workflow showing transcript ingestion, Mem0 memory storage, and automated action item extraction](image.png)
**Alt text (SEO-ready):** Meeting Memory Assistant by Uplizd, an AI workflow for automated transcript processing, Mem0 memory integration, and actionable meeting intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/08f24840-cfa3-53ea-9f29-607d00d25146)

---

## Category
**Primary category:** Operations
**Secondary tags:** meetings, mem0, knowledge management, ai workflow, productivity, composio, transcript analysis, data retention.
This solution bridges the gap between ephemeral meeting conversations and long-term organizational memory.

---

## Who is this for?
This solution is designed for professionals who manage high-volume communication and need to maintain continuity across complex projects.

*   **Project Managers**
    *   Track evolving requirements and decisions across weekly stakeholder syncs.
*   **Sales Representatives**
    *   Recall specific prospect pain points and preferences from previous discovery calls.
*   **Engineering Leads**
    *   Maintain a persistent record of technical constraints and architectural choices.
*   **Executive Assistants**
    *   Ensure follow-up tasks are captured and assigned immediately after leadership meetings.

---

## Features
- **Persistent Memory Layer**
  Utilizes Mem0 to store and retrieve context across multiple sessions, ensuring the agent learns user preferences over time.
- **Automated Transcript Parsing**
  Intelligently processes raw meeting transcripts to filter out filler text and highlight high-value information.
- **Action Item Extraction**
  Automatically identifies tasks, owners, and deadlines, pushing them directly into your existing project management tools via the Composio Toolset.
- **Contextual Search & Retrieval**
  Allows users to query the agent for specific decisions or topics discussed in past meetings without manual searching.
- **Seamless Integration**
  Connects with popular meeting platforms and CRM tools to ensure that meeting memory is always accessible where work happens.

---

## Use Cases
**Meeting Intelligence**
*   Summarize key decisions from a 60-minute discovery call into a 3-bullet executive brief.
*   Identify and extract all action items assigned to specific team members during a project sprint planning session.

**Relationship Management**
*   Retrieve the specific technical requirements mentioned by a client in a meeting three months ago.
*   Update the "Client Preferences" profile in your CRM based on feedback provided during a recent quarterly business review.

**Workflow Continuity**
*   Generate a "pre-meeting prep" document based on the memory of the last three meetings with a specific stakeholder.
*   Sync meeting-derived action items directly into your task management system to ensure nothing falls through the cracks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Memory Assistant template from the library.
3. Authenticate your Mem0 and Composio connections within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw meeting transcript or user query.
*   **Agent**: Processes the text, queries Mem0 for historical context, and determines necessary actions.
*   **Composio Toolset**: Executes external API calls to update CRMs or task trackers based on agent instructions.
*   **Chat Output**: Delivers the summarized insights or confirmation of action items to the user.

### 3) Run the Flow
Use the Playground to test the assistant with these prompts:
* `Summarize the key decisions from the transcript provided and highlight any new action items.`
* `What were the main technical concerns raised by the client in our last three meetings?`
* `Update the project status in my task manager based on the notes from today's sync.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for transcript analysis and memory management.
*   Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate extraction.
*   Define system instructions to prioritize "Action Item" and "Decision" extraction.
*   Enable Mem0 memory access to allow the agent to reference past meeting history.

### 2) Composio Toolset Node
*   Requires a valid Composio API key to bridge the agent with external platforms.
*   Configure the connection scope to include read/write access for your specific CRM or task management tools.

### 3) Tool Availability
*   **Mem0 Memory API**: For reading and writing persistent user/meeting context.
*   **CRM Connectors**: For updating account intelligence and contact notes.
*   **Task Management APIs**: For creating and assigning action items.

---

## Related Solutions
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive intelligence gathering for sales accounts.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Intelligent sorting and management of project tasks.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Real-time synchronization of data across platforms.
