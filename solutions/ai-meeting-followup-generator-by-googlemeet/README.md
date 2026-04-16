# AI Meeting Follow-up Generator (Uplizd) - Automated action item extraction and communication

## Summary
The AI Meeting Follow-up Generator is an intelligent Uplizd workflow designed to streamline post-meeting productivity by automatically parsing transcripts to extract key decisions, action items, and drafting personalized follow-up emails. By leveraging the Composio Toolset, this solution eliminates manual note-taking and ensures that stakeholders remain aligned, significantly reducing the administrative burden on project managers and sales teams.

---

## Demo
![AI Meeting Follow-up Generator workflow diagram showing transcript processing and email drafting](image.png)
**Alt text (SEO-ready):** AI Meeting Follow-up Generator workflow diagram showing transcript processing, action item extraction, and email drafting using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVHgB7dExAQAAAMKg9U9tCj+gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOCtAQUAAAE=)](https://uplizd.ai/solutions/5a817e11-589a-5afd-978d-2f436b227a08)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** meetings, transcript analysis, email automation, productivity, ai workflow, composio, action items, communication
- This solution bridges the gap between spoken meeting content and actionable documentation, serving as a vital tool for RevOps and project management efficiency.

---

## Who is this for?
This solution is designed for professionals who manage high volumes of meetings and need to maintain rigorous follow-up standards.

- **Project Managers**
    - Automate the distribution of meeting minutes and task assignments to team members immediately after a call.
- **Sales Representatives**
    - Ensure no prospect request is missed by generating personalized follow-up emails based on specific meeting discussions.
- **Executive Assistants**
    - Reduce time spent on manual documentation by using AI to summarize complex discussions into concise action items.
- **Customer Success Managers**
    - Track client requirements and commitments accurately to improve long-term account health and satisfaction.

---

## Features
- **Automated Transcript Parsing**
    - Uses advanced LLM processing to identify speaker intent and extract critical information from raw meeting transcripts.
- **Action Item Extraction**
    - Automatically categorizes and assigns tasks based on the meeting context, ensuring accountability across the team.
- **Personalized Email Drafting**
    - Generates professional, context-aware follow-up communications that reflect the specific tone and outcomes of the meeting.
- **Composio Toolset Integration**
    - Seamlessly connects with your existing email and project management platforms to execute follow-ups without switching tabs.
- **Real-time Workflow Execution**
    - Processes meeting data instantly, allowing for rapid deployment of follow-up materials while the conversation is still fresh.

---

## Use Cases
**Meeting Documentation**
- Converting raw Google Meet transcripts into structured meeting minutes.
- Archiving key decisions and action items directly into project management tools.

**Sales & Client Relations**
- Drafting immediate follow-up emails for prospects based on specific pain points discussed.
- Tracking commitments made during discovery calls to ensure timely delivery of requested information.

**Internal Team Alignment**
- Distributing concise summaries to stakeholders who were unable to attend the live session.
- Standardizing the follow-up process across departments to ensure consistent communication quality.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the AI Meeting Follow-up Generator template from the solution library.
3. Authenticate your required integrations (Google Meet, Email, CRM) within the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw meeting transcript text.
- **Agent**: Analyzes the transcript to identify action items and draft follow-up content.
- **Composio Toolset**: Executes the delivery of emails and updates to project management boards.
- **Chat Output**: Displays the generated summary and confirmation of sent communications.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Summarize the meeting transcript provided and draft a follow-up email to the client highlighting the three key action items.`
- `Extract all assigned tasks from this transcript and format them into a table for the project management team.`
- `Create a professional follow-up email based on the discussion, ensuring the tone is supportive and addresses the prospect's concerns about pricing.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the intelligence layer for parsing and drafting.
- **Instruction Pattern:**
    - "Act as an expert meeting assistant; prioritize clarity and professional tone."
    - "Identify all explicit action items, assignees, and deadlines mentioned in the transcript."
    - "Draft follow-up emails that reference specific meeting topics to increase engagement."

### 2) Composio Toolset Node
- Requires an active API key for your chosen email and project management connectors.
- Ensure the connection scope allows for "Read" access to transcripts and "Write" access to email/task management tools.

### 3) Tool Availability
- **Email Client**: For sending drafted follow-ups directly to participants.
- **Project Management API**: For creating tasks or updating tickets based on extracted action items.
- **Transcript Parser**: For structured data extraction from unstructured text.

---

## Related Solutions
- [../action-item-cleanup-agent-by-rootly/README.md](Action Item Cleanup Agent) - Automates the removal and organization of stale action items.
- [../action-item-prioritizer-by-rootly/README.md](Action Item Prioritizer) - Ranks and manages task urgency for project teams.
- [../247-customer-support-assistant-by-ai-ml-api/README.md](Customer Support Assistant) - Provides 24/7 automated support and inquiry handling.
