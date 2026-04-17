# Meeting Notes Processor (Uplizd) - Automate CRM updates from meeting transcripts

## Summary
The Meeting Notes Processor by Uplizd streamlines your post-meeting workflow by automatically extracting key action items, sentiment, and summary data from transcripts and syncing them directly into Attio. This AI-driven solution eliminates manual data entry, ensures your CRM remains the single source of truth, and significantly increases pipeline velocity by keeping deal records current without administrative overhead.

---

## Demo
![Meeting Notes Processor workflow diagram showing transcript input, AI analysis, and CRM update](image.png)
**Alt text (SEO-ready):** Uplizd Meeting Notes Processor workflow for automated CRM data entry, transcript analysis, and Attio integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ca242ea4-f171-5844-a7de-178b13cb7f5c)

---

## Category
**Primary category:** CRM data integration  
**Secondary tags:** crm, attio, meeting notes, sales automation, data hygiene, ai workflow, composio, pipeline management  
This solution bridges the gap between unstructured conversation data and structured CRM records to maintain high-quality pipeline hygiene.

---

## Who is this for?
This solution is designed for revenue-focused teams who need to reduce manual logging and improve data accuracy across their sales cycle.

*   **Sales Representatives**
    *   Eliminate post-call manual entry by automatically pushing notes and action items to Attio.
*   **Sales Operations Managers**
    *   Ensure consistent data hygiene and standardized note-taking formats across the entire sales organization.
*   **Account Executives**
    *   Focus on relationship building while the AI captures critical deal intelligence and follow-up requirements.
*   **Customer Success Managers**
    *   Maintain detailed records of client feedback and evolving needs without interrupting the flow of customer conversations.

---

## Features
- **Automated Transcript Parsing**
  Extracts key insights, action items, and sentiment from raw meeting transcripts using advanced LLM analysis.
- **Attio CRM Integration**
  Leverages the Composio Toolset to perform real-time updates to contact and deal objects within Attio.
- **Structured Data Mapping**
  Automatically maps extracted meeting highlights to specific CRM fields, ensuring consistent data formatting.
- **Action Item Tracking**
  Identifies and logs follow-up tasks directly into the CRM, preventing missed opportunities and stalled deals.
- **Real-time Sync**
  Processes meeting data immediately after the call, ensuring the CRM is always updated with the latest intelligence.

---

## Use Cases
**Pipeline Management**
*   Automatically update deal stages based on meeting sentiment and progress indicators.
*   Log key competitive intelligence gathered during discovery calls directly into the deal record.

**Data Hygiene**
*   Standardize the format of meeting notes across the team to ensure reporting accuracy.
*   Clean up unstructured transcript data into concise, actionable summaries before saving to the CRM.

**Sales Productivity**
*   Create follow-up tasks for the sales team based on commitments made during the meeting.
*   Sync meeting summaries to the CRM to provide context for future account reviews and handoffs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Meeting Notes Processor.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Attio account within the Composio Toolset node.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input:** Receives the raw meeting transcript text.
*   **Agent:** Processes the text to extract structured insights and action items.
*   **Composio Toolset:** Executes the API calls to update the relevant Attio CRM records.
*   **Chat Output:** Confirms the successful update and displays the summary of logged data.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
* `Process this transcript: [Paste Transcript] and update the deal record for Acme Corp.`
* `Extract action items from the following meeting notes and log them in Attio: [Paste Notes]`
* `Summarize the sentiment of this call and update the 'Last Meeting Note' field in Attio.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the intelligence layer, transforming unstructured text into structured CRM updates.
*   Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate extraction.
*   Provide a clear system prompt defining the expected output schema (e.g., JSON format for CRM fields).
*   Ensure the agent is instructed to ignore irrelevant small talk and focus on business-critical insights.

### 2) Composio Toolset Node
*   **API Key:** Ensure your Attio API key is configured in the Composio dashboard.
*   **Connection Scope:** Grant the toolset read/write access to your Attio `deals` and `tasks` objects.

### 3) Tool Availability
*   **Attio Search:** Locate specific deal or contact IDs by name.
*   **Attio Update:** Modify fields such as `notes`, `next_steps`, or `stage`.
*   **Attio Task Creation:** Generate new follow-up tasks linked to the specific deal.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across multiple platforms with conflict resolution.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage pipeline stages and track stalled deals effectively.
* [Account Intelligence Gatherer](../account-intelligence-gatherer/README.md) — Enrich account records with external data and insights.
