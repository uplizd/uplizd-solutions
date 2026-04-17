# Meeting Intelligence Agent (Uplizd) - Automate transcription, summarization, and action item extraction

## Summary
The Meeting Intelligence Agent by Deepgram is an automated workflow designed to convert raw audio recordings into structured, actionable business intelligence. By leveraging advanced speech-to-text processing and AI-driven analysis, this solution eliminates manual note-taking, ensuring that critical decisions, follow-up tasks, and key discussion points are captured accurately and synchronized directly into your project management or CRM systems.

---

## Demo
![Meeting Intelligence Agent workflow dashboard showing audio processing, transcription, and action item extraction nodes](image.png)
**Alt text (SEO-ready):** Meeting Intelligence Agent by Uplizd utilizing Deepgram for automated transcription, AI summarization, and CRM action item synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/05dfffb5-9285-51e0-88ca-3fee7bf98868)

---

## Category
**Primary category:** Operations
**Secondary tags:** meeting intelligence, deepgram, transcription, ai workflow, productivity, automation, action items, composio

This solution bridges the gap between spoken conversation and structured data, enabling teams to maintain a single source of truth for all meeting outcomes.

---

## Who is this for?
This agent is designed for professionals who need to scale their meeting output without increasing administrative overhead.

* **Sales Managers**
    * Automatically log key objections and buying signals from discovery calls into the CRM.
* **Project Managers**
    * Extract and assign action items to team members immediately following project syncs.
* **Customer Success Leads**
    * Identify churn risks and feature requests from support meetings to improve retention.
* **Executive Assistants**
    * Generate concise executive summaries and meeting minutes for stakeholders to review.

---

## Features
- **Real-time Transcription**
  High-accuracy speech-to-text processing powered by Deepgram for clear, verbatim records.
- **Automated Summarization**
  AI-driven synthesis of long-form audio into bulleted executive summaries and key takeaways.
- **Action Item Extraction**
  Intelligent identification of tasks, owners, and deadlines mentioned during the conversation.
- **CRM/Tool Integration**
  Seamlessly push meeting data to external platforms using the Composio Toolset.
- **Sentiment Analysis**
  Detects tone and engagement levels to provide context on the health of the meeting relationship.

---

## Use Cases
**Sales Pipeline Management**
* Sync discovery call transcripts to Salesforce or HubSpot to update opportunity notes.
* Automatically flag stalled deals based on negative sentiment detected in client meetings.

**Project Collaboration**
* Convert brainstorming session recordings into organized Jira tickets or Trello cards.
* Distribute meeting minutes via Slack or email to ensure all stakeholders are aligned.

**Quality Assurance & Training**
* Analyze support call recordings to identify common customer pain points and training gaps.
* Archive searchable meeting transcripts for compliance and historical reference.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Meeting Intelligence Agent template file provided in this repository.
3. Connect your Deepgram API key and preferred CRM/Project Management tool via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Accepts audio file URLs or raw text transcripts for processing.
* **Agent**: Orchestrates the transcription analysis and extracts structured insights.
* **Composio Toolset**: Connects to your ecosystem to push summaries and tasks to external apps.
* **Chat Output**: Returns the final summary and a list of identified action items to the user.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
* `Summarize this meeting and extract all action items assigned to the engineering team.`
* `Analyze the sentiment of this sales call and update the CRM opportunity record.`
* `Create a follow-up email draft based on the key decisions made in this transcript.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node requires a model capable of high-level reasoning and structured data extraction.
* Set the system prompt to prioritize concise, professional formatting.
* Enable JSON mode to ensure action items are parsed correctly for downstream tools.
* Configure the temperature to 0.3 for consistent, factual output.

### 2) Composio Toolset Node
* Provide your API key to authenticate with the Composio platform.
* Define the connection scope to include only the specific CRM or project tools required for your workflow.

### 3) Tool Availability
* **Transcription Service**: Deepgram API for audio processing.
* **CRM Connectors**: Salesforce, HubSpot, or Pipedrive for data logging.
* **Task Management**: Jira, Trello, or Asana for action item assignment.
* **Communication**: Slack or Email for summary distribution.

---

## Related Solutions
* [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospects before meetings.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Organize and rank tasks extracted from various sources.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex business processes across multiple platforms.
