# Call Log Analyzer (Uplizd) - Automate CRM insights from voice recordings

## Summary
The Call Log Analyzer is an intelligent Uplizd workflow that processes raw call recordings and transcripts to extract actionable intelligence directly into Pipedrive. By automating the transcription analysis and CRM update process, this solution eliminates manual data entry, ensures consistent lead qualification, and provides sales teams with a single source of truth for every customer interaction.

---

## Demo
![Call Log Analyzer workflow showing transcription processing and Pipedrive CRM update nodes](../image.png)
**Alt text (SEO-ready):** Uplizd Call Log Analyzer workflow for Pipedrive, automating CRM data entry, sales call transcription, and lead qualification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a755f73a-6023-5754-b74c-a764bd43ce76)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, pipedrive, call logs, transcription, sales intelligence, data sync, ai workflow, composio  
This solution bridges the gap between unstructured voice conversations and structured CRM data, enabling automated pipeline management.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to turn call data into measurable pipeline growth.

*   **Sales Managers**
    *   Gain visibility into team performance and common objection patterns without manual review.
*   **Account Executives**
    *   Automatically populate Pipedrive fields with meeting summaries and action items to save time.
*   **Revenue Operations (RevOps)**
    *   Maintain high data hygiene standards by ensuring every call results in updated CRM records.
*   **Sales Development Reps (SDRs)**
    *   Identify lead signals and follow-up opportunities faster by leveraging AI-driven call analysis.

---

## Features
- **Automated Transcription Processing**
  Seamlessly ingest audio files or transcripts and convert them into structured text for analysis.
- **Pipedrive CRM Integration**
  Utilize the Composio Toolset to push summaries, sentiment scores, and action items directly into specific Pipedrive deals.
- **Intelligent Insight Extraction**
  Identify key topics, customer pain points, and buying signals using advanced LLM reasoning.
- **Real-time Action Item Tracking**
  Automatically extract follow-up tasks and sync them to your CRM or task management system.
- **Sentiment & Tone Analysis**
  Evaluate call quality and customer sentiment to help coach sales reps and improve conversion rates.

---

## Use Cases
**Pipeline Management**
*   Automatically update deal stages in Pipedrive based on the outcome of a discovery call.
*   Flag stalled deals that require immediate follow-up based on negative sentiment detected in the latest call.

**Sales Coaching**
*   Generate concise summaries of sales calls for managers to review during weekly 1:1 sessions.
*   Extract common customer objections to build a centralized knowledge base for team training.

**Data Hygiene**
*   Ensure all call notes are standardized and logged in the correct Pipedrive fields automatically.
*   Sync contact information updates discovered during conversations back to the CRM record.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Call Log Analyzer template from the marketplace.
3. Connect your Pipedrive account via the Composio integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw transcript or audio file link.
*   **Agent**: Analyzes text to extract key insights, sentiment, and action items.
*   **Composio Toolset**: Executes API calls to update the relevant Pipedrive deal.
*   **Chat Output**: Confirms the successful update and displays the extracted summary.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Analyze the transcript for deal ID 123 and update the Pipedrive notes with the summary.`
* `Extract all action items from this call and create a follow-up task in Pipedrive.`
* `Evaluate the sentiment of this call and update the deal probability score accordingly.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary intelligence layer, parsing unstructured conversation data.
*   Focus on extracting specific CRM fields (e.g., "Next Step," "Budget," "Timeline").
*   Maintain a neutral, professional tone for all CRM note entries.
*   Prioritize identifying explicit customer requests or objections.

### 2) Composio Toolset Node
Requires a valid Pipedrive API key. Ensure the connection scope includes `deals.write`, `notes.write`, and `activities.write` permissions to allow the agent to perform full updates.

### 3) Tool Availability
*   **Pipedrive Search**: Locate deals by name or ID.
*   **Pipedrive Update**: Modify deal fields and statuses.
*   **Pipedrive Note Creation**: Append summaries to the deal timeline.
*   **Pipedrive Activity Manager**: Create follow-up tasks based on call outcomes.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across platforms to maintain a single source of truth.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and automate follow-ups for stalled deals.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Clean up and standardize CRM data to prevent decay.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new opportunities based on lead signals.
