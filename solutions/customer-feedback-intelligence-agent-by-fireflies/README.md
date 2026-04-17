# Customer Feedback Intelligence Agent (Uplizd) - Automated sentiment analysis and actionable insights

## Summary
The Customer Feedback Intelligence Agent leverages Uplizd and Fireflies to automatically ingest, transcribe, and analyze customer feedback from voice and video interactions. By centralizing qualitative data into a single source of truth, teams can identify recurring pain points, track sentiment trends, and accelerate product roadmap decisions without manual note-taking or spreadsheet consolidation.

---

## Demo
![Customer Feedback Intelligence Agent workflow dashboard showing Fireflies transcription and sentiment analysis nodes](image.png)
**Alt text (SEO-ready):** Customer Feedback Intelligence Agent workflow on Uplizd, featuring Fireflies integration for automated sentiment analysis and voice-to-text feedback processing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6c378b6c-0d6b-5dfd-b79c-38b4c45a98f0)

---

## Category
**Primary category:** Customer Support
**Secondary tags:** feedback, fireflies, sentiment analysis, voice intelligence, customer success, product management, composio, ai workflow.
This solution bridges the gap between raw conversation data and structured business intelligence for customer-facing teams.

---

## Who is this for?
This agent is designed for teams that need to turn high-volume voice interactions into structured data.

*   **Product Managers**
    *   Identify feature requests and usability friction points directly from user calls.
*   **Customer Success Managers**
    *   Monitor account sentiment and proactively address churn risks before they escalate.
*   **Support Leads**
    *   Automate the categorization of support tickets based on recurring feedback themes.
*   **Sales Operations**
    *   Extract competitive intelligence and objection patterns from discovery and demo calls.

---

## Features
- **Automated Transcription**
  Seamlessly pull meeting transcripts from Fireflies to eliminate manual documentation.
- **Sentiment Scoring**
  Apply real-time NLP to categorize feedback as positive, neutral, or negative.
- **Theme Extraction**
  Automatically tag conversations with keywords like "pricing," "UI/UX," or "feature request."
- **Actionable Summaries**
  Generate concise executive summaries of long-form customer calls using the Agent node.
- **Composio Integration**
  Connect feedback insights directly to your CRM or project management tools for immediate follow-up.

---

## Use Cases
**Product Roadmap Prioritization**
*   Aggregate feature requests across all customer calls to rank development priorities.
*   Identify the most frequently mentioned "missing" features in the last 30 days.

**Customer Churn Prevention**
*   Flag accounts showing a downward trend in sentiment scores during recent check-ins.
*   Automate alerts for support teams when specific "cancellation" keywords appear in transcripts.

**Quality Assurance & Training**
*   Analyze support call transcripts to ensure team adherence to company messaging.
*   Extract successful objection-handling techniques from top-performing sales calls.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Customer Feedback Intelligence template from the library.
3. Authenticate your Fireflies and CRM accounts via the Composio connection manager.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the meeting ID or transcript trigger.
*   **Agent**: Processes the text, performs sentiment analysis, and identifies key themes.
*   **Composio Toolset**: Executes actions to push insights into your connected CRM or Slack.
*   **Chat Output**: Delivers the final summary report to the user or a designated channel.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
* `Analyze the sentiment of the last 5 customer calls and list the top 3 recurring complaints.`
* `Summarize the feedback regarding our new dashboard update from this week's meetings.`
* `Create a Jira ticket for the engineering team based on the technical issues mentioned in the recent sales call.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized analyst for qualitative data.
*   Focus on objective extraction rather than subjective interpretation.
*   Use a structured JSON output format for downstream tool compatibility.
*   Maintain a consistent tone when summarizing feedback for stakeholders.

### 2) Composio Toolset Node
*   Requires a valid Fireflies API key and CRM (e.g., Salesforce/HubSpot) connection.
*   Scope should be limited to "Read" access for transcripts and "Write" access for tickets/notes.

### 3) Tool Availability
*   **Fireflies API**: Retrieve transcripts, meeting summaries, and speaker metadata.
*   **CRM Connector**: Update account records, create tasks, or log feedback notes.
*   **Slack/Email API**: Send automated alerts to the product or success teams.

---

## Related Solutions
* [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - General purpose support automation.
* [whats-app-feedback-collection-agent-by-wati](../whats-app-feedback-collection-agent-by-wati/README.md) - Collect feedback via WhatsApp channels.
* [account-intelligence-reporter-by-leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregate account insights for sales teams.
