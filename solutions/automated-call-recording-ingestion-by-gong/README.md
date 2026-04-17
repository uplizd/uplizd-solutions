# Automated Call Recording Ingestion (Uplizd) - Streamline your Gong data pipeline

## Summary
The Automated Call Recording Ingestion workflow enables revenue teams to automatically sync external call recordings into Gong for centralized analysis and coaching. By eliminating manual uploads, this solution ensures that every customer interaction is captured, transcribed, and analyzed within your primary sales intelligence platform, significantly improving pipeline visibility and coaching velocity.

---

## Demo
![Automated Call Recording Ingestion workflow diagram showing file source to Gong integration](../image.png)
**Alt text (SEO-ready):** Automated Call Recording Ingestion workflow by Uplizd, syncing external media to Gong for sales intelligence and revenue operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cbdee46d-54c8-5de7-9cee-788c97b49e41)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** gong, sales intelligence, call recording, data ingestion, revenue operations, composio, ai workflow, sales coaching
- This solution bridges the gap between disparate communication channels and your revenue intelligence platform to ensure comprehensive data coverage.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to unify their customer conversation data.

- **Sales Managers**
    - Ensure 100% of team calls are available for performance reviews and coaching sessions.
- **Revenue Operations (RevOps)**
    - Automate the ingestion pipeline to maintain data hygiene and reduce manual administrative overhead.
- **Sales Enablement Specialists**
    - Gain immediate access to call transcripts and insights to refine training materials and sales playbooks.
- **Account Executives**
    - Spend less time on manual data entry and more time focusing on deal progression and customer engagement.

---

## Features
- **Automated Media Sync**
    - Automatically detect and push new call recordings from cloud storage to Gong without manual intervention.
- **Centralized Intelligence**
    - Consolidate all customer interactions into a single source of truth for better reporting and trend analysis.
- **Composio-Powered Integration**
    - Utilize the Composio Toolset to securely authenticate and manage API connections between your storage providers and Gong.
- **Real-time Processing**
    - Trigger ingestion workflows immediately upon file creation to ensure insights are available for timely follow-ups.
- **Scalable Data Pipeline**
    - Handle high volumes of call data efficiently, ensuring no customer conversation is missed during peak sales periods.

---

## Use Cases
**Sales Coaching & Performance**
- Automatically upload discovery calls to Gong to identify coaching opportunities for new hires.
- Sync demo recordings to analyze objection handling patterns across the sales organization.

**Revenue Operations Efficiency**
- Streamline the ingestion of cross-platform meeting recordings to maintain consistent CRM data hygiene.
- Reduce manual file management tasks by automating the transfer of recordings from external conferencing tools.

**Customer Insight Analysis**
- Capture feedback from support-led calls to identify recurring product pain points and feature requests.
- Aggregate competitor mentions from call recordings to inform strategic positioning and market intelligence.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the Uplizd builder.
2. Authenticate your Gong and cloud storage accounts via the Composio connection prompt.
3. Configure the trigger node to monitor your specific call recording folder.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the file metadata and trigger event from your storage provider.
- **Agent**: Orchestrates the logic, validating file formats and preparing the payload for Gong.
- **Composio Toolset**: Executes the secure API calls to upload and link the recording to the correct account.
- **Chat Output**: Confirms successful ingestion and provides a status summary of the processed recording.

### 3) Run the Flow
Use the Playground to test your ingestion pipeline with these prompts:
- `Ingest the latest call recording from the 'Q3-Discovery' folder to Gong.`
- `Check the status of the last 5 call uploads and report any failures.`
- `Sync all pending recordings from the 'Sales-Team-Recordings' bucket to the primary Gong workspace.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent controller for your data pipeline.
- Use a high-reasoning model to ensure accurate mapping of recording metadata to Gong fields.
- **Recommended instruction pattern:**
    - "Extract file metadata and verify compatibility with Gong's supported formats."
    - "Handle API rate limits by implementing a retry mechanism for failed uploads."
    - "Summarize the ingestion result and notify the user of any missing required fields."

### 2) Composio Toolset Node
- Provide your Gong API key and ensure the connection scope includes `write` access to recordings.
- Configure the toolset to handle authentication tokens securely via the Uplizd environment variables.

### 3) Tool Availability
- **Gong API**: For uploading media and updating call metadata.
- **Storage Connectors**: For monitoring and retrieving files from platforms like AWS S3, Google Drive, or Dropbox.
- **Logging Utility**: To track ingestion success rates and debug connectivity issues.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and track deal velocity.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize customer data across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score new sales opportunities.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean and accurate CRM records.
