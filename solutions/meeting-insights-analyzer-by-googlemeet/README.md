# Meeting Insights Analyzer (Uplizd) - Extract actionable intelligence from Google Meet transcripts

## Summary
The Meeting Insights Analyzer is an automated Uplizd workflow that processes Google Meet transcripts to extract key discussion points, action items, and sentiment analysis. By leveraging the Composio Toolset to interface with meeting data, this solution eliminates manual note-taking, ensures consistent documentation, and accelerates pipeline velocity by surfacing follow-up tasks immediately after calls.

---

## Demo
![Meeting Insights Analyzer dashboard showing transcript summarization and action item extraction](image.png)
**Alt text (SEO-ready):** Meeting Insights Analyzer workflow by Uplizd for automated Google Meet transcript summarization, action item extraction, and CRM data synchronization.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAyY180LwAAAAlwSFlzAAALEgAACxIB0t1+/AAAAAd0SU1FB+gDCw02N3v5DA4AAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBkLmUHAAAAIklEQVR42mP8z8AABJgYGBgYGBgYGBgYGBgYGBgYGBgYGAAT+QG92w55VAAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/50272879-b9a1-537a-b70e-025d1fad618b)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** meetings, google meet, transcript analysis, ai workflow, productivity, composio, action items, sales operations
- This solution bridges the gap between raw meeting audio and structured business intelligence, serving as a central hub for meeting data hygiene.

---

## Who is this for?
This solution is designed for teams looking to standardize their post-meeting workflows and improve information retention.

- **Sales Managers**
    - Ensure all discovery calls are logged consistently with identified pain points and next steps.
- **Project Managers**
    - Automatically track project blockers and assign action items to the correct stakeholders without manual entry.
- **Customer Success Leads**
    - Monitor client sentiment trends and identify churn risks early based on meeting transcript analysis.
- **Operations Specialists**
    - Maintain a single source of truth for meeting outcomes across the organization’s CRM and project management tools.

---

## Features
- **Automated Transcription Processing**
    - Leverages AI to ingest raw Google Meet transcripts and convert them into structured, readable summaries.
- **Action Item Extraction**
    - Automatically identifies tasks, owners, and deadlines mentioned during the conversation using advanced NLP.
- **CRM Integration**
    - Seamlessly pushes meeting summaries and follow-up tasks into your CRM via the Composio Toolset.
- **Sentiment Analysis**
    - Evaluates the tone of the meeting to provide a health score for client or prospect relationships.
- **Real-time Pipeline Updates**
    - Triggers immediate updates to deal stages or project statuses based on the meeting outcome.

---

## Use Cases
**Sales Pipeline Management**
- Automatically log discovery call summaries directly to the associated opportunity in your CRM.
- Update deal stages based on positive or negative sentiment detected during the meeting.

**Project Collaboration**
- Extract technical requirements from stakeholder meetings and push them into project management boards.
- Assign follow-up tasks to team members automatically based on the meeting transcript.

**Customer Relationship Hygiene**
- Generate a concise "Meeting Recap" email draft for the account manager to send to the client.
- Flag high-priority concerns or support requests mentioned during meetings for immediate triage.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Insights Analyzer template from the marketplace.
3. Connect your Google Meet and CRM accounts via the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw transcript text or meeting recording link.
- **Agent**: Analyzes the input to extract summaries, sentiment, and action items.
- **Composio Toolset**: Executes API calls to push data to your CRM or project management tools.
- **Chat Output**: Returns the final summary and confirmation of data sync to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Summarize the meeting transcript provided below and identify all action items.`
- `Analyze the sentiment of this sales call and suggest a follow-up strategy.`
- `Extract the key technical requirements from this transcript and create tasks in our project management tool.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized meeting analyst.
- **Recommended instruction pattern:**
    - "Act as an expert meeting assistant that prioritizes accuracy and brevity."
    - "Extract action items only when a clear owner and deadline are implied."
    - "Maintain a professional tone when summarizing client-facing conversations."

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable secure tool execution.
- **Connection Scope:** Ensure the toolset has read/write access to your CRM and Google Workspace.

### 3) Tool Availability
- **CRM Connector:** For updating deal stages and contact records.
- **Project Management Tool:** For creating and assigning tasks.
- **Email/Communication Tool:** For drafting follow-up summaries.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](CRM Data Sync Agent) - Synchronize data across platforms to maintain a single source of truth.
- [../deal-pipeline-manager/README.md](Deal Pipeline Manager) - Manage sales stages and follow-ups to keep your pipeline moving.
- [../crm-data-hygiene-manager/README.md](CRM Data Hygiene Manager) - Clean and format your CRM data to ensure high-quality reporting.
- [../account-research-assistant-by-zoominfo/README.md](Account Research Assistant) - Gather deep intelligence on prospects before your meetings.
