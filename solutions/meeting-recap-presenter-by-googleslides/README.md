# Meeting Recap Presenter (Uplizd) - Automated meeting-to-slide workflow for executive summaries

## Summary
The Meeting Recap Presenter is an intelligent Uplizd workflow that automatically transforms raw meeting transcripts and notes into structured, professional slide decks. By leveraging AI to synthesize key takeaways and action items, this solution accelerates communication velocity, ensuring stakeholders receive concise, actionable summaries without the manual overhead of slide creation.

---

## Demo
![Meeting Recap Presenter workflow screenshot showing transcript processing into Google Slides](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Recap Presenter workflow automating transcript analysis and Google Slides presentation generation for business meetings.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/acc6c80d-19cc-516b-abbe-a22a952518b5)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** google slides, meeting notes, automation, productivity, ai workflow, composio, presentation, documentation
- This solution streamlines the transition from verbal collaboration to visual documentation, bridging the gap between meeting insights and executive reporting.

---

## Who is this for?
This solution is designed for professionals who need to maintain high-quality documentation while minimizing time spent on administrative slide design.

- **Project Managers**
    - Quickly convert complex meeting discussions into clear, visual progress updates for stakeholders.
- **Sales Leads**
    - Generate professional post-call summaries and account review decks immediately after client interactions.
- **Executive Assistants**
    - Automate the creation of board-ready presentation slides from raw meeting transcripts and notes.
- **Team Leads**
    - Standardize the format of weekly sync recaps to ensure consistent information flow across the department.

---

## Features
- **Automated Synthesis**
    - Uses advanced LLMs to distill long-form transcripts into high-impact bullet points and key takeaways.
- **Google Slides Integration**
    - Leverages the Composio Toolset to programmatically create and populate slide decks directly in your Google Drive.
- **Smart Formatting**
    - Automatically applies professional layouts and structures to ensure your recaps are visually consistent and readable.
- **Action Item Extraction**
    - Identifies and highlights specific tasks, owners, and deadlines mentioned during the meeting for immediate follow-up.
- **Real-Time Processing**
    - Enables rapid turnaround from meeting conclusion to presentation delivery, keeping teams aligned and informed.

---

## Use Cases
**Executive Reporting**
- Convert quarterly business review (QBR) transcripts into high-level performance summary slides.
- Transform project steering committee meeting notes into status update presentations for leadership.

**Sales & Account Management**
- Generate post-discovery call decks that summarize client pain points and proposed solutions.
- Create account health update presentations for internal review sessions based on recent client feedback.

**Internal Team Alignment**
- Summarize weekly sprint planning meetings into visual roadmaps for cross-functional visibility.
- Document brainstorming session outcomes into structured presentation formats for future reference.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Meeting Recap Presenter template from the solution library.
3. Connect your Google account within the Composio Toolset node to grant slide creation permissions.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input:** Receives the raw meeting transcript or summary notes.
- **Agent:** Analyzes the input to extract key themes, action items, and slide content.
- **Composio Toolset:** Executes the API calls to generate and format the Google Slides deck.
- **Chat Output:** Confirms successful slide generation and provides a direct link to the presentation.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Create a summary presentation from this transcript: [Paste Transcript Here]`
- `Generate a 5-slide recap of the QBR meeting notes provided in the input.`
- `Extract action items from the meeting and create a follow-up slide deck for the team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a professional summarizer and presentation architect.
- Use a high-reasoning model to ensure accurate extraction of action items.
- Instruct the agent to prioritize clarity, brevity, and professional tone.
- Configure the system prompt to map specific transcript sections to slide titles and body content.

### 2) Composio Toolset Node
- Provide your Google Workspace API credentials to authorize the agent.
- Set the connection scope to allow 'Slides' and 'Drive' write access.

### 3) Tool Availability
- **Google Slides API:** For creating, updating, and formatting presentation slides.
- **Google Drive API:** For managing file permissions and organizing generated decks.
- **Text Analysis Tools:** For parsing transcripts and identifying key meeting segments.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automates the tracking and resolution of meeting action items.
- [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Ranks and assigns meeting tasks based on urgency and impact.
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) — Manages and deploys visual collaboration templates for team sessions.
