# Donor Engagement Tracker (Uplizd) - Automated donor insights and relationship management

## Summary
The Donor Engagement Tracker is an intelligent Uplizd AI workflow designed to streamline non-profit operations by monitoring donor interactions and campaign performance in real-time. By connecting Givebutter data to an automated agent, this solution provides a single source of truth for engagement metrics, ensuring pipeline velocity for fundraising efforts and maintaining high-quality donor data hygiene.

---

## Demo
![Donor Engagement Tracker workflow dashboard showing Givebutter integration and automated donor follow-up triggers](image.png)

**Alt text (SEO-ready):** Donor Engagement Tracker Uplizd workflow showing Givebutter integration, automated donor follow-up, and fundraising analytics.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/62d0cb5f-973a-5c1a-bcab-dfac020978ac)

---

## Category
- **Primary category:** Non-profit operations
- **Secondary tags:** givebutter, donor management, fundraising, crm, engagement tracking, data sync, ai workflow, composio
- This solution bridges the gap between donor activity and actionable outreach, enabling organizations to optimize their fundraising impact through automated intelligence.

---

## Who is this for?
This solution is designed for mission-driven teams looking to scale their outreach without sacrificing personalization.

- **Development Director**
    - Gains high-level visibility into campaign performance and donor retention trends.
- **Fundraising Coordinator**
    - Automates the tracking of donor interactions to ensure no follow-up opportunity is missed.
- **Non-profit Operations Manager**
    - Maintains clean donor data by syncing engagement signals directly from Givebutter.
- **Community Engagement Lead**
    - Identifies high-potential donors based on real-time engagement patterns and interaction history.

---

## Features
- **Automated Donor Sync**
    - Seamlessly pulls engagement data from Givebutter into your central tracking system using the Composio Toolset.
- **Real-time Interaction Monitoring**
    - Triggers instant updates whenever a new donation or engagement event is detected, keeping your records current.
- **Engagement Scoring**
    - Uses the Agent node to evaluate donor activity levels, helping prioritize outreach efforts for high-value supporters.
- **Customized Follow-up Logic**
    - Automatically maps donor actions to specific follow-up workflows, reducing manual administrative overhead.
- **Unified Reporting Dashboard**
    - Consolidates fragmented donor data into a single, readable output for better strategic decision-making.

---

## Use Cases
**Campaign Performance Analysis**
- Track conversion rates for specific fundraising campaigns by monitoring donor response times.
- Identify top-performing donation tiers to refine future outreach strategies.

**Donor Relationship Management**
- Automatically log donor touchpoints to ensure a consistent communication history across the team.
- Flag inactive donors who haven't engaged with recent campaigns for targeted re-engagement efforts.

**Operational Data Hygiene**
- Standardize donor contact information and interaction notes to prevent data decay.
- Sync Givebutter transaction statuses with internal CRM records to ensure financial reporting accuracy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to add the Donor Engagement Tracker template to your workspace.
3. Authenticate your Givebutter account via the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled polling requests for donor data.
- **Agent**: Processes engagement signals and determines the appropriate outreach or logging action.
- **Composio Toolset**: Executes API calls to Givebutter to fetch, update, or sync donor records.
- **Chat Output**: Returns a summary of the processed donor interactions and any flagged follow-up tasks.

### 3) Run the Flow
Use the Playground to test your integration with the following prompts:
- `Fetch all donor engagement events from the last 24 hours.`
- `Identify donors who have contributed to the 'Spring Gala' campaign but haven't received a thank-you note.`
- `Sync the latest donation records from Givebutter and update the donor engagement status.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your primary analyst for donor behavior.
- Use a model capable of structured data reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on how to interpret "engagement" based on your organization's specific KPIs.
- Set the system prompt to prioritize accuracy in donor identification and categorization.

### 2) Composio Toolset Node
- Ensure your Givebutter API key is securely stored in the Composio connection settings.
- Scope the connection to allow read/write access to donor profiles and transaction history.

### 3) Tool Availability
- **Givebutter Search**: Locate donor profiles by email or ID.
- **Transaction Fetcher**: Retrieve detailed logs of recent donations.
- **Engagement Logger**: Update custom fields or notes within the donor record.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research into donor and account profiles.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Ensure multi-platform data consistency across your fundraising stack.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Extend your operational automation beyond donor management.
