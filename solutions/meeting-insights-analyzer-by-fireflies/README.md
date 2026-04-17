# Meeting Insights Analyzer (Uplizd) - Automate meeting intelligence and action item distribution

## Summary
The Meeting Insights Analyzer is an intelligent Uplizd workflow that processes meeting transcripts from Fireflies.ai to extract key discussion points, sentiment, and actionable tasks. By automating the synthesis of meeting data, this solution ensures that critical information is captured, organized, and distributed to stakeholders immediately, eliminating manual note-taking and ensuring team alignment across all projects.

---

## Demo
![Meeting Insights Analyzer workflow dashboard showing transcript ingestion and automated summary generation](image.png)
**Alt text (SEO-ready):** Meeting Insights Analyzer dashboard displaying automated Fireflies.ai transcript processing, sentiment analysis, and action item extraction within the Uplizd workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/baa17077-00ce-52b2-a563-9e2665be793e)

---

## Category
**Primary category:** Operations  
**Secondary tags:** meetings, fireflies, ai-transcription, productivity, automation, action-items, collaboration, composio  
This solution bridges the gap between raw meeting audio and structured operational data to improve organizational transparency.

---

## Who is this for?
This solution is designed for teams looking to reclaim time spent on administrative follow-up and documentation.

*   **Project Managers**
    *   Automatically track project milestones and blockers identified during stakeholder calls.
*   **Sales Representatives**
    *   Instantly capture prospect requirements and follow-up commitments without manual entry.
*   **Operations Leads**
    *   Maintain a centralized repository of meeting outcomes to ensure team-wide accountability.
*   **Executive Assistants**
    *   Streamline the creation of meeting minutes and distribution of summary emails to participants.

---

## Features
- **Automated Transcript Processing**
  Seamlessly pulls raw meeting data from Fireflies.ai for immediate analysis.
- **Action Item Extraction**
  Identifies and categorizes tasks, assigning them to the correct owners based on context.
- **Sentiment & Tone Analysis**
  Evaluates meeting dynamics to flag potential risks or high-priority client concerns.
- **Structured Summary Generation**
  Produces professional, concise meeting minutes formatted for instant sharing via email or Slack.
- **Composio-Powered Integrations**
  Leverages the Composio Toolset to push insights directly into your existing project management or CRM tools.

---

## Use Cases
**Meeting Documentation**
*   Automatically generate and archive meeting minutes in your internal knowledge base.
*   Format long-form transcripts into bulleted executive summaries for quick review.

**Task Management**
*   Extract action items from team syncs and sync them directly to your task tracking software.
*   Notify team members of their assigned responsibilities via automated follow-up messages.

**Strategic Intelligence**
*   Analyze recurring themes across customer calls to identify product feature requests.
*   Monitor sentiment trends in sales meetings to improve pitch performance and objection handling.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Authenticate your Fireflies.ai and relevant destination tool connections within the Composio dashboard.
4. Ensure nodes are correctly mapped and the API keys are active in the configuration panel.

### 2) Setup the Nodes
*   **Chat Input**: Receives the meeting ID or transcript trigger from the source.
*   **Agent**: Analyzes the text to identify key insights, sentiment, and tasks.
*   **Composio Toolset**: Executes the extraction and pushes data to your integrated apps.
*   **Chat Output**: Returns the final summary and confirmation of task creation.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Analyze the latest meeting transcript and extract all action items.`
* `Summarize the sentiment of the last sales call and identify top 3 customer pain points.`
* `Create a summary report for the project sync and email it to the team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your meeting data.
*   Focus on extracting objective facts and actionable commitments.
*   Maintain a neutral, professional tone for all generated summaries.
*   Prioritize clarity and brevity when formatting lists of action items.

### 2) Composio Toolset Node
*   **API Key**: Ensure your Composio API key is configured in the environment settings.
*   **Connection Scope**: Grant access to Fireflies.ai and your target project management or communication platforms.

### 3) Tool Availability
*   **Fireflies.ai**: Transcript retrieval and meeting metadata access.
*   **Task Management Tools**: Automated creation of tickets and tasks.
*   **Communication APIs**: Sending summaries to Slack, Microsoft Teams, or Email.

---

## Related Solutions
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Focuses on ranking and managing tasks across your stack.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks team productivity and operational bottlenecks.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregates account data for better meeting preparation.
