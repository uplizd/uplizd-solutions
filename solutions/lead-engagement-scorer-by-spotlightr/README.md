# Lead Engagement Scorer (Uplizd) - Automate lead prioritization based on video interaction data

## Summary
The Lead Engagement Scorer (Uplizd) is an intelligent automation workflow that analyzes viewer behavior on video content to score and prioritize sales leads. By leveraging real-time engagement data, this solution helps sales teams focus their outreach on high-intent prospects, increasing pipeline velocity and ensuring that marketing-qualified leads are acted upon when their interest is at its peak.

---

## Demo
![Lead Engagement Scorer workflow showing video analytics data flowing into a scoring agent](image.png)
**Alt text (SEO-ready):** Uplizd lead engagement scorer workflow, video analytics integration, sales lead prioritization, automated CRM scoring, and lead qualification pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cd9c2207-ed6c-5a20-a334-9e1a338d34ef)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead scoring, video analytics, spotlightr, sales pipeline, lead qualification, composio, ai workflow
- This solution bridges the gap between video consumption metrics and CRM lead management to ensure data-driven sales prioritization.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to turn passive video views into active sales conversations.

- **Sales Development Representative (SDR)**
    - Quickly identify which prospects have watched key product demos to prioritize daily outreach.
- **Growth Marketing Manager**
    - Measure the ROI of video content by tracking which assets successfully drive lead engagement.
- **Revenue Operations (RevOps) Lead**
    - Standardize lead scoring criteria across the organization by integrating behavioral data into the CRM.
- **Account Executive (AE)**
    - Receive real-time alerts when high-value accounts interact with personalized video content.

---

## Features
- **Behavioral Scoring Engine**
    - Automatically assigns numerical values to leads based on video completion rates and re-watch frequency.
- **CRM Integration**
    - Seamlessly syncs engagement scores directly into your CRM fields using the Composio Toolset.
- **Real-time Alerting**
    - Triggers instant notifications to sales channels when a lead crosses a high-intent engagement threshold.
- **Video Analytics Aggregation**
    - Consolidates raw data from video platforms into actionable insights for the sales team.
- **Automated Lead Routing**
    - Dynamically updates lead status or owner based on the calculated engagement score.

---

## Use Cases
**Pipeline Prioritization**
- Automatically move leads to the "Hot" category in your CRM when they watch >80% of a pricing video.
- Flag stalled deals for follow-up if the contact engages with a new product update video.

**Sales Outreach Optimization**
- Provide AEs with a summary of which video segments a prospect watched before a discovery call.
- Trigger personalized email sequences based on specific video interaction triggers.

**Content Performance Tracking**
- Identify which video assets are most effective at converting viewers into qualified opportunities.
- Correlate video engagement spikes with overall account health and renewal probability.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Engagement Scorer template from the marketplace.
3. Connect your video platform (e.g., Spotlightr) and CRM credentials via the Composio Toolset.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event from the video platform containing viewer metadata.
- **Agent**: Analyzes the engagement metrics against your defined scoring logic.
- **Composio Toolset**: Executes the API calls to update the lead record in your CRM.
- **Chat Output**: Confirms the update and logs the engagement score for the user.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Score lead [email] based on their recent engagement with the 'Q3 Product Demo' video.`
- `Fetch all leads who watched more than 50% of the latest webinar and update their CRM score.`
- `Identify high-intent leads from the last 24 hours and post a summary to the sales-alerts Slack channel.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic layer for interpreting engagement data and applying business rules.
- Instruction: "Analyze the provided video engagement data and calculate a score from 1-100 based on watch time and interaction frequency."
- Instruction: "Map the calculated score to the 'Lead Score' field in the CRM."
- Instruction: "If the score exceeds 80, flag the lead as 'High Intent' and notify the assigned account owner."

### 2) Composio Toolset Node
- **API Key**: Ensure your CRM and video platform API keys are configured within the Composio dashboard.
- **Connection Scope**: Grant read access to video analytics and write access to CRM lead objects.

### 3) Tool Availability
- **Video Analytics API**: Retrieves watch time, completion percentage, and viewer identity.
- **CRM Connector**: Updates lead fields, modifies lead status, and creates activity notes.
- **Notification Service**: Sends alerts to email or messaging platforms based on scoring thresholds.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Enrich account profiles with external web traffic and firmographic data.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain consistent lead and contact information across multiple platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker-by-salesforce/README.md) — Identify and score new sales opportunities based on lead behavior.
