# Meeting Knowledge Base Builder (Uplizd) - Automate meeting insights into searchable organizational intelligence

## Summary
The Meeting Knowledge Base Builder is an automated Uplizd workflow that ingests raw meeting transcripts from Fireflies.ai, extracts key insights, and indexes them into a centralized knowledge repository. By bridging the gap between spoken conversation and structured documentation, this solution ensures that critical decisions, action items, and strategic discussions are instantly retrievable, eliminating knowledge silos and accelerating team alignment.

---

## Demo
![Meeting Knowledge Base Builder workflow diagram showing transcript ingestion from Fireflies.ai into a searchable knowledge base](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Knowledge Base Builder workflow, Fireflies.ai transcript processing, automated knowledge management, and AI-driven insights extraction.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue?logo=uplizd)](https://uplizd.ai/solutions/238f75f3-fc17-5b88-84c2-70ce371f6edc)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** knowledge management, fireflies, ai workflow, transcript analysis, documentation, composio, enterprise search, productivity
- This solution streamlines organizational intelligence by converting unstructured meeting data into a structured, searchable knowledge base for high-velocity teams.

---

## Who is this for?
This solution is designed for teams looking to capture institutional memory and reduce time spent searching for information.

- **Operations Managers**
    - Centralize meeting outcomes to ensure team-wide visibility and process consistency.
- **Product Managers**
    - Quickly retrieve user feedback and feature requests discussed across multiple customer calls.
- **Sales Leaders**
    - Analyze recurring objections and competitive mentions to refine sales playbooks.
- **Engineering Leads**
    - Track technical decisions and architectural discussions without re-listening to long recordings.

---

## Features
- **Automated Transcript Ingestion**
    - Seamlessly pulls raw meeting data from Fireflies.ai as soon as a meeting concludes.
- **Intelligent Insight Extraction**
    - Uses the Agent node to identify action items, key decisions, and sentiment from transcripts.
- **Structured Knowledge Indexing**
    - Organizes extracted data into a standardized format for easy integration with your documentation tools.
- **Real-time Searchability**
    - Enables teams to query past meetings using natural language to find specific project updates.
- **Composio-Powered Connectivity**
    - Leverages the Composio Toolset to push summarized insights directly into your preferred knowledge management platforms.

---

## Use Cases
**Meeting Documentation**
- Automatically generate meeting minutes and summaries for recurring syncs.
- Archive key decisions in a central repository to maintain a historical record.

**Strategic Intelligence**
- Aggregate customer feedback from discovery calls to inform product roadmaps.
- Identify recurring pain points across sales calls to improve customer success strategies.

**Team Alignment**
- Sync action items directly to project management tools to ensure accountability.
- Provide new team members with a searchable history of project-related discussions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Knowledge Base Builder template from the solution library.
3. Connect your Fireflies.ai and destination tool credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to process a specific meeting.
- **Agent**: Analyzes the transcript text and extracts structured insights based on your instructions.
- **Composio Toolset**: Executes the API calls to store the processed data in your knowledge base.
- **Chat Output**: Confirms the successful indexing and provides a summary of the extracted data.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Process the latest meeting transcript from Fireflies and extract all action items.`
- `Summarize the key decisions made in the Q3 product planning meeting.`
- `Find all mentions of 'pricing' in the last five customer discovery calls.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your meeting data.
- **Instruction Pattern:**
    - Focus on extracting actionable insights, decisions, and follow-up tasks.
    - Maintain a consistent summary format for every meeting processed.
    - Prioritize clarity and brevity to ensure the knowledge base remains readable.

### 2) Composio Toolset Node
- **API Key:** Provide your unique Composio API key to enable secure tool execution.
- **Connection Scope:** Ensure the toolset has read access to Fireflies.ai and write access to your chosen knowledge management platform.

### 3) Tool Availability
- **Fireflies.ai API:** For retrieving transcripts and meeting metadata.
- **Knowledge Management Connectors:** (e.g., Notion, Confluence, or Google Docs) for storing processed insights.
- **Data Formatting Tools:** For converting raw text into structured Markdown or JSON.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Automatically rank and assign tasks extracted from meetings.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Enrich your meeting context with external account intelligence.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Trigger downstream tasks based on meeting outcomes.
