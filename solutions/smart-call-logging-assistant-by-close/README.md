# Smart Call Logging Assistant (Uplizd) - Automated CRM call summarization and categorization

## Summary
The Smart Call Logging Assistant is an intelligent Uplizd workflow designed to eliminate manual data entry by automatically transcribing, summarizing, and logging sales call insights directly into your CRM. By leveraging AI to extract key action items, sentiment, and deal-relevant data, this solution ensures your CRM remains a single source of truth, significantly improving pipeline velocity and sales team hygiene.

---

## Demo
![Smart Call Logging Assistant workflow dashboard showing automated transcription and CRM update nodes](image.png)
**Alt text (SEO-ready):** Smart Call Logging Assistant Uplizd workflow for automated CRM data entry, call summarization, and sales pipeline synchronization via Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AIFDRE6m4559QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFAwAAAKAAAHV9/8AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/9b27e85e-6c65-5153-8117-777873eb2046)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, close, sales, call logging, ai workflow, data hygiene, pipeline, composio
This solution bridges the gap between voice communication and CRM record-keeping, ensuring every customer interaction is captured accurately and efficiently.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce administrative overhead and improve data accuracy.

*   **Sales Representatives**
    *   Eliminate post-call manual entry, allowing more time for active selling and relationship building.
*   **Sales Operations Managers**
    *   Maintain high-quality CRM data hygiene by ensuring every call interaction is standardized and categorized.
*   **Revenue Leaders**
    *   Gain real-time visibility into deal health and sentiment through automated, consistent call summaries.
*   **Customer Success Managers**
    *   Quickly reference historical call notes and action items to provide personalized, informed support.

---

## Features
- **Automated Transcription Processing**
    Processes raw audio transcripts into structured, readable summaries using advanced LLM reasoning.
- **CRM Integration via Composio**
    Seamlessly connects with Close and other CRM platforms to push updates without manual intervention.
- **Intelligent Entity Extraction**
    Automatically identifies and tags key information such as budget, timeline, and decision-maker sentiment.
- **Action Item Prioritization**
    Extracts follow-up tasks from call transcripts and maps them to the appropriate CRM activity fields.
- **Real-Time Data Sync**
    Ensures that call logs are updated in the CRM immediately after the workflow execution, maintaining data freshness.

---

## Use Cases
**Sales Pipeline Management**
*   Automatically log call outcomes to move deals through defined pipeline stages.
*   Update deal probability scores based on sentiment analysis extracted during the call.

**Data Hygiene & Compliance**
*   Standardize call note formatting across the entire sales organization for better reporting.
*   Ensure all customer interactions are logged for audit trails and compliance requirements.

**Follow-up Automation**
*   Generate personalized follow-up email drafts based on the specific action items identified in the call.
*   Create task reminders in the CRM for account managers based on promised delivery dates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your CRM account (e.g., Close) through the Composio integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw call transcript or meeting notes.
*   **Agent**: Analyzes the text to extract sentiment, action items, and summary data.
*   **Composio Toolset**: Executes the API calls to update the CRM record.
*   **Chat Output**: Confirms the successful log entry and displays the generated summary.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
* `Log this call: "The prospect mentioned they have budget approval but need a demo for the CTO next week."`
* `Summarize this transcript and update the deal status to 'Negotiation' in Close.`
* `Extract action items from this meeting note and create follow-up tasks for the sales team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that transforms unstructured conversation into structured CRM data.
*   Maintain a neutral, professional tone for all generated summaries.
*   Strictly follow the schema for CRM field mapping (e.g., status, next_step, sentiment).
*   Prioritize the extraction of dates and specific commitments made during the call.

### 2) Composio Toolset Node
Requires a valid API key for your CRM (e.g., Close). Ensure the connection scope includes `write` permissions for activities, leads, and opportunities to allow the agent to perform updates.

### 3) Tool Availability
*   **CRM Search**: Locate lead or deal IDs based on email or company name.
*   **Activity Creation**: Log the summary as a new call activity.
*   **Field Update**: Modify specific deal attributes like stage, probability, or custom fields.
*   **Task Management**: Create follow-up tasks linked to the specific lead.

---

## Related Solutions
* [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Automates gathering intelligence on target accounts.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages pipeline stages and stalled deal follow-ups.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Cleans and standardizes CRM data for better reporting.
