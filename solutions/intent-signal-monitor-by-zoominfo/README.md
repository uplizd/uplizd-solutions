# Intent Signal Monitor (Uplizd) - Real-time buying intent tracking and sales pipeline acceleration

## Summary
The Intent Signal Monitor is an automated Uplizd workflow that tracks high-value buying intent signals from ZoomInfo and instantly alerts sales teams to hot prospects. By bridging the gap between raw market intelligence and CRM action, this solution ensures your team never misses a conversion opportunity, significantly increasing pipeline velocity and lead prioritization accuracy.

---

## Demo
![Intent Signal Monitor workflow showing ZoomInfo data ingestion, AI analysis, and CRM alert dispatch](image.png)
**Alt text (SEO-ready):** Intent Signal Monitor workflow for Uplizd, automating ZoomInfo data ingestion, sales lead scoring, and CRM pipeline alerts.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/81d50ade-2898-52b0-b025-dee00b154949)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales intelligence, zoominfo, lead scoring, pipeline, intent data, crm, salesops, ai workflow
- This solution transforms raw market signals into actionable sales tasks, streamlining the transition from prospect identification to active engagement.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate the identification of high-intent leads and reduce manual research time.

- **Sales Development Reps (SDRs)**
  - Receive automated notifications for prospects showing active buying intent, allowing for timely outreach.
- **Revenue Operations (RevOps)**
  - Standardize the flow of intent data into the CRM to ensure consistent lead scoring and data hygiene.
- **Sales Managers**
  - Monitor real-time pipeline growth and ensure that high-priority accounts are being addressed by the team.
- **Account Executives**
  - Focus on warm, qualified opportunities rather than cold outreach, increasing overall closing rates.

---

## Features
- **Real-time Signal Ingestion**
  - Automatically pulls intent data from ZoomInfo to identify accounts actively researching your solution space.
- **AI-Powered Lead Scoring**
  - Uses an Agent node to evaluate signal strength and prioritize leads based on your specific ICP (Ideal Customer Profile).
- **Seamless CRM Integration**
  - Leverages the Composio Toolset to push qualified leads directly into your CRM with context-rich notes.
- **Automated Alerting**
  - Triggers instant notifications via Slack or email when a high-intent signal is detected and validated.
- **Customizable Thresholds**
  - Easily adjust the sensitivity of intent signals to filter out noise and focus only on high-conversion prospects.

---

## Use Cases
**Proactive Lead Outreach**
- Trigger an immediate follow-up task for an SDR when a target account hits a specific intent score threshold.
- Populate CRM fields with recent intent activity to provide AEs with talking points for discovery calls.

**Pipeline Acceleration**
- Identify stalled opportunities that show renewed research activity, prompting a "re-engagement" campaign.
- Automatically update lead status in the CRM based on the intensity of the signals gathered from ZoomInfo.

**Market Intelligence**
- Aggregate intent signals over a 30-day window to identify emerging trends in your target market.
- Route high-intent leads to specific account owners based on territory or industry mapping.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Connect your ZoomInfo and CRM accounts within the integration settings.
3. Configure the trigger frequency to match your desired monitoring cadence.
4. Ensure nodes are correctly linked from the Chat Input through the Agent and Composio Toolset to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the signal trigger or manual request to scan for intent.
- **Agent**: Analyzes the ZoomInfo data against your scoring logic and determines the next action.
- **Composio Toolset**: Executes the API calls to update the CRM or push alerts to communication channels.
- **Chat Output**: Confirms the successful processing of the signal and logs the action taken.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Scan for high-intent signals in the tech sector for the last 24 hours.`
- `Identify accounts with an intent score above 80 and update their status in Salesforce.`
- `Summarize the recent buying activity for [Company Name] and create a task for the account owner.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets raw intent data.
- **Instruction Pattern:**
  - "Analyze the provided ZoomInfo data and assign a priority score from 1-100 based on the defined ICP."
  - "If the score exceeds the threshold, format the data for CRM entry and trigger the notification tool."
  - "Maintain a professional tone when summarizing the intent context for the sales team."

### 2) Composio Toolset Node
- **API Key:** Ensure your ZoomInfo and CRM API keys are active in the Composio dashboard.
- **Connection Scope:** Grant read access to ZoomInfo intent data and write access to your CRM's Lead/Opportunity objects.

### 3) Tool Availability
- **ZoomInfo API:** For fetching intent signals and company research.
- **CRM Connector (Salesforce/HubSpot):** For updating lead records and creating tasks.
- **Notification Service (Slack/Email):** For real-time alerts to the sales team.

---

## Related Solutions
- [Account Research Assistant (ZoomInfo)](../account-research-assistant-by-zoominfo/README.md) — Deep-dive research and data enrichment for target accounts.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage deal stages and follow-up cadences for active opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain data consistency across multiple CRM and marketing platforms.
