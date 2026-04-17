# Meeting Summary Agent (Uplizd) - Automated transcription and intelligent meeting insights

## Summary
The Meeting Summary Agent is an AI-powered workflow that streamlines post-meeting documentation by automatically transcribing audio, extracting key decisions, and generating actionable summaries. By integrating advanced speech-to-text and LLM capabilities, this solution eliminates manual note-taking, ensuring that project stakeholders remain aligned and informed without the administrative burden of traditional meeting recaps.

---

## Demo
![Meeting Summary Agent workflow interface showing transcription and summary generation](image.png)
**Alt text (SEO-ready):** Meeting Summary Agent workflow interface showing transcription and summary generation using Uplizd and AI-powered meeting analytics.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/138c4b3c-a8bc-5743-becd-dafacf710b69)

---

## Category
- **Primary category:** Productivity automation
- **Secondary tags:** meeting notes, transcription, ai summary, workflow automation, documentation, composio, meeting intelligence
- This solution bridges the gap between raw audio data and structured business intelligence, categorizing it as an essential tool for operational efficiency.

---

## Who is this for?
This solution is designed for professionals who need to convert spoken collaboration into structured, searchable documentation.

- **Project Managers**
    - Automatically capture project milestones and blockers without manual documentation.
- **Sales Representatives**
    - Quickly generate follow-up emails and capture client requirements immediately after discovery calls.
- **Executive Assistants**
    - Maintain accurate records of leadership decisions and delegated action items across multiple time zones.
- **Product Owners**
    - Synthesize user feedback and feature requests from stakeholder meetings into actionable product backlog items.

---

## Features
- **Automated Transcription**
    - Utilizes high-fidelity speech-to-text engines to convert audio files into accurate, timestamped text.
- **Intelligent Summarization**
    - Leverages LLMs to distill long-form discussions into concise executive summaries and bulleted highlights.
- **Action Item Extraction**
    - Automatically identifies and lists tasks, assignees, and deadlines mentioned during the conversation.
- **CRM Integration**
    - Seamlessly pushes meeting insights and summaries directly into your connected CRM platforms via the Composio Toolset.
- **Customizable Output Formats**
    - Configures the final output to match your team's preferred documentation style, whether for Slack, email, or internal wikis.

---

## Use Cases
**Meeting Documentation**
- Transcribing internal strategy sessions to ensure all team members have a single source of truth.
- Creating standardized meeting minutes for recurring client check-ins to track long-term progress.

**Sales and Revenue Operations**
- Capturing critical discovery call details to update opportunity records in real-time.
- Generating personalized follow-up templates based on specific pain points mentioned by prospects.

**Project Management**
- Tracking project blockers and technical debt identified during sprint planning or retrospective meetings.
- Mapping action items to specific team members to ensure accountability and project velocity.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Summary template file provided in this repository.
3. Connect your preferred LLM and transcription service credentials in the integration settings.
4. Ensure nodes are correctly linked from Chat Input to Agent, Composio Toolset, and finally Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Accepts audio files or raw transcript text for processing.
- **Agent**: Analyzes the input to extract key themes, decisions, and action items.
- **Composio Toolset**: Connects to external tools to save summaries or update project management boards.
- **Chat Output**: Delivers the formatted summary and task list to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Summarize this meeting transcript and highlight all action items assigned to the engineering team.`
- `Create a follow-up email draft based on the key pain points discussed in this sales call.`
- `Extract the top 3 decisions made during this project sync and format them for a Slack update.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node requires a model capable of high-context reasoning.
- Set the system prompt to prioritize "Action Item" and "Decision" extraction.
- Use a temperature setting of 0.2 to ensure factual accuracy and minimize hallucinations.
- Ensure the model has access to the full transcript context for consistent summary generation.

### 2) Composio Toolset Node
- Provide your API key to enable secure communication with your CRM and productivity tools.
- Define the connection scope to allow the agent to read/write to your specific project management or sales platforms.

### 3) Tool Availability
- **Transcription API**: For processing audio input.
- **CRM Connector**: For updating account notes and opportunity details.
- **Task Manager Connector**: For creating and assigning action items.
- **Communication Connector**: For drafting emails or sending summary notifications.

---

## Related Solutions
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Organize and rank tasks extracted from meeting notes.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Enrich your meeting context with deep account intelligence.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Automate downstream processes based on meeting outcomes.
