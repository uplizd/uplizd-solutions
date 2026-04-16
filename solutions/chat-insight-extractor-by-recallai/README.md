# Chat Insight Extractor (Uplizd) - Automated meeting intelligence and action item generation

## Summary
The Chat Insight Extractor is an intelligent Uplizd workflow designed to process meeting transcripts and chat logs, automatically distilling complex conversations into actionable business insights. By leveraging the Composio Toolset to interface with communication platforms, this solution helps teams eliminate manual note-taking, ensure critical follow-ups are captured, and maintain a single source of truth for project decisions.

---

## Demo
![Chat Insight Extractor workflow diagram showing transcript input, AI analysis, and action item output](image.png)
**Alt text (SEO-ready):** Chat Insight Extractor Uplizd workflow diagram for automated meeting analysis, transcript processing, and action item extraction using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/b167580d-d79f-5811-955a-9b896b3bde05)

---

## Category
**Primary category:** Data integration
**Secondary tags:** chat, meeting intelligence, transcription, action items, productivity, ai workflow, composio, data hygiene.
This solution bridges the gap between raw meeting communication and structured project management data.

---

## Who is this for?
This workflow is designed for teams that need to convert high-velocity meeting discussions into structured, trackable tasks.

* **Project Managers**
    * Automate the creation of Jira or Asana tickets directly from meeting chat logs.
* **Sales Representatives**
    * Capture prospect pain points and follow-up requirements without manual data entry.
* **Customer Success Managers**
    * Identify churn risks and feature requests discussed during client syncs.
* **Operations Leads**
    * Maintain consistent documentation of meeting outcomes across distributed teams.

---

## Features
- **Automated Transcript Parsing**
    Processes raw chat logs to filter noise and focus on high-value decision points.
- **Action Item Extraction**
    Identifies specific commitments and tasks assigned to team members during discussions.
- **Composio-Powered Integrations**
    Seamlessly pushes extracted insights into your existing CRM or project management stack.
- **Context-Aware Summarization**
    Generates concise executive summaries that capture the "who, what, and when" of every meeting.
- **Real-Time Data Sync**
    Ensures that extracted insights are updated immediately following the conclusion of a meeting.

---

## Use Cases
**Meeting Documentation**
* Automatically generate meeting minutes from long-form chat transcripts.
* Archive key decisions in a centralized database for future reference.

**Task Management**
* Convert verbal commitments into actionable tasks in your project management tool.
* Assign follow-up items to the correct team members based on conversation context.

**Customer Intelligence**
* Extract recurring feature requests from customer support or sales meetings.
* Flag urgent client concerns for immediate escalation to the appropriate department.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Chat Insight Extractor template from the library.
3. Connect your preferred communication and project management accounts via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the raw meeting transcript or chat log text.
* **Agent:** Analyzes the text to identify insights, owners, and deadlines.
* **Composio Toolset:** Executes the API calls to push data to your external tools.
* **Chat Output:** Returns a confirmation summary of the extracted and synced items.

### 3) Run the Flow
Use the Playground to test the extraction logic with these example prompts:
* `Extract all action items from this transcript and create tasks in Asana.`
* `Summarize the key decisions made in this meeting and email them to the project lead.`
* `Identify any urgent customer requests from this chat log and add them to the priority queue.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent requires a model capable of high-fidelity summarization and entity extraction.
* Set the temperature to 0.2 for consistent, factual output.
* Use a system prompt that defines the output schema for tasks (Title, Assignee, Due Date).
* Enable function calling to allow the agent to trigger Composio tools automatically.

### 2) Composio Toolset Node
* Provide your Composio API key to authenticate the connection.
* Define the scope of access to your project management and CRM platforms.

### 3) Tool Availability
* **Task Creation Tools:** For pushing items to Jira, Asana, or Trello.
* **Communication Tools:** For sending summaries via Slack or Email.
* **Data Retrieval Tools:** For fetching existing project context to improve extraction accuracy.

---

## Related Solutions
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organize and rank tasks extracted from meeting logs.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize extracted meeting data across your CRM ecosystem.
* [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) - Automate support ticket triage using similar transcript analysis.
