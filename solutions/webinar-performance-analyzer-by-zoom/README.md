# Webinar Performance Analyzer (Uplizd) - Optimize engagement and track webinar metrics

## Summary
The Webinar Performance Analyzer (Uplizd) is an automated workflow designed to ingest, process, and evaluate webinar performance data from Zoom. By leveraging AI-driven analytics, this solution helps marketing and event teams transform raw attendance and engagement metrics into actionable insights, ensuring higher pipeline velocity and improved ROI for every virtual event.

---

## Demo
![Webinar Performance Analyzer dashboard showing attendee engagement metrics and AI-generated insights](image.png)
**Alt text (SEO-ready):** Webinar Performance Analyzer dashboard showing attendee engagement metrics and AI-generated insights integrated with Uplizd and Zoom.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f928b5d9-581a-533a-8262-d2fae846575c)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** webinar, zoom, analytics, engagement, marketing, data sync, ai workflow, composio
This solution bridges the gap between raw webinar attendance data and strategic marketing intelligence.

---

## Who is this for?
This workflow is designed for teams looking to quantify the impact of their virtual events and streamline post-webinar follow-up processes.

*   **Marketing Manager**
    *   Automates the reporting process to quickly identify high-performing content topics.
*   **Event Coordinator**
    *   Reduces manual data entry by syncing attendee lists directly into the CRM.
*   **Sales Operations Lead**
    *   Prioritizes leads based on real-time engagement scores captured during the session.
*   **Demand Generation Specialist**
    *   Optimizes future webinar strategy by analyzing attendee drop-off points and participation rates.

---

## Features
- **Automated Data Ingestion**
    Connects directly to Zoom to pull attendee logs, poll responses, and Q&A transcripts in real-time.
- **Engagement Scoring**
    Calculates an engagement index for each attendee based on session duration, interaction frequency, and poll participation.
- **AI-Driven Insight Generation**
    Uses the Agent node to summarize key themes from Q&A sessions and identify common audience pain points.
- **CRM Synchronization**
    Seamlessly pushes qualified leads and engagement data into your existing sales stack via the Composio Toolset.
- **Performance Reporting**
    Generates structured summaries that highlight conversion opportunities and areas for webinar improvement.

---

## Use Cases
**Post-Event Lead Qualification**
*   Automatically flag attendees who stayed for the entire duration for immediate sales outreach.
*   Sync high-intent questions from the Q&A log directly into the CRM as follow-up tasks.

**Content Strategy Optimization**
*   Analyze poll results to determine which topics resonated most with the target audience.
*   Identify specific timestamps where attendee drop-off spiked to refine future presentation pacing.

**Operational Efficiency**
*   Eliminate manual spreadsheet exports by automating the transfer of Zoom data to your data warehouse.
*   Trigger automated "Thank You" emails based on specific engagement thresholds reached during the event.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Authenticate your Zoom account within the Uplizd environment.
3. Configure your destination CRM or database connection via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are saved in the environment settings.

### 2) Setup the Nodes
*   **Chat Input**: Receives the webinar ID or date range for the analysis.
*   **Agent**: Processes the raw Zoom data and applies logic to score engagement.
*   **Composio Toolset**: Executes API calls to fetch Zoom data and update CRM records.
*   **Chat Output**: Delivers the final performance summary and actionable lead list.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Analyze the performance of the webinar with ID 123456789 and list the top 10 most engaged attendees.`
* `Summarize the Q&A from the latest webinar and identify the top 3 recurring questions.`
* `Generate a report on attendee drop-off rates and suggest improvements for our next session.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary analytical engine, interpreting webinar transcripts and engagement data.
*   Focus on identifying patterns in audience behavior and sentiment.
*   Maintain a professional, data-driven tone for all generated reports.
*   Prioritize actionable insights that link directly to sales or marketing outcomes.

### 2) Composio Toolset Node
Requires a valid Zoom API key and appropriate scopes (e.g., `meeting:read`, `report:read`) to pull session data. Ensure your CRM integration is authorized to create or update lead records.

### 3) Tool Availability
*   **Zoom API**: Fetching meeting participants, poll results, and Q&A transcripts.
*   **CRM Integration**: Updating lead status, adding notes, and creating follow-up tasks.
*   **Data Formatting**: Converting raw JSON responses into human-readable summary tables.

---

## Related Solutions
* [Zoom Usage Intelligence Agent](../zoom-usage-intelligence-agent/README.md) - Monitor and optimize overall Zoom account usage and meeting patterns.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent data across your sales and marketing platforms.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score new sales opportunities based on engagement signals.
