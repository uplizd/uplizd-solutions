# Intent Signal Scorer (Uplizd) - Automate lead prioritization based on real-time buying intent

## Summary
The Intent Signal Scorer is an automated Uplizd workflow that ingests visitor data from Leadfeeder to rank and score prospects based on their specific buying intent signals. By surfacing high-intent accounts directly to your sales team, this solution eliminates manual lead research, reduces response latency, and ensures your pipeline is focused on the prospects most likely to convert.

---

## Demo
![Intent Signal Scorer workflow dashboard showing lead ranking and intent scoring metrics](image.png)
**Alt text (SEO-ready):** Intent Signal Scorer dashboard showing automated lead ranking, buying intent signals, and CRM integration for sales pipeline optimization on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/c07e3a1d-50f3-5419-8f2e-526c5d8dac54)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** leadfeeder, intent data, lead scoring, sales pipeline, crm, revenue operations, ai workflow, composio
- This solution bridges the gap between raw website visitor intelligence and actionable sales outreach by automating the qualification process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to prioritize high-value engagement over manual lead filtering.

- **Sales Development Representative (SDR)**
    - Receives prioritized lists of accounts showing active buying intent to focus daily outreach efforts.
- **Revenue Operations Manager**
    - Standardizes lead scoring criteria across the organization to ensure consistent pipeline hygiene.
- **Sales Manager**
    - Monitors real-time intent signals to allocate resources toward high-probability deals.
- **Marketing Operations Lead**
    - Connects top-of-funnel website traffic data with bottom-of-funnel sales actions for better attribution.

---

## Features
- **Automated Intent Scoring**
  Calculates lead scores dynamically based on visitor behavior, page depth, and frequency of site visits.
- **Leadfeeder Integration**
  Seamlessly pulls firmographic and behavioral data from Leadfeeder to enrich your existing lead profiles.
- **Real-Time Alerting**
  Triggers immediate notifications to sales channels when a high-intent account crosses a specific scoring threshold.
- **CRM Syncing**
  Automatically updates lead status and intent scores in your CRM via the Composio Toolset to keep data centralized.
- **Customizable Thresholds**
  Allows users to define specific scoring logic that aligns with your unique ideal customer profile (ICP).

---

## Use Cases
**Lead Prioritization**
- Automatically flag accounts that visit pricing or demo pages more than three times in a week.
- Rank incoming leads based on company size and industry relevance to ensure SDRs contact the best fit first.

**Sales Outreach Optimization**
- Trigger a personalized outreach sequence in your CRM the moment a high-intent score is registered.
- Provide sales reps with a summary of the specific pages a prospect visited before they make a discovery call.

**Pipeline Hygiene**
- Automatically archive or deprioritize leads that show low intent signals over a 30-day period.
- Ensure all Leadfeeder data is mapped correctly to CRM fields to prevent duplicate lead creation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Leadfeeder and CRM accounts via the Composio Toolset node.
3. Configure your scoring parameters in the Agent node to match your ICP.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal from Leadfeeder or manual request.
- **Agent**: Analyzes visitor data and applies the scoring logic to rank the lead.
- **Composio Toolset**: Executes the API calls to update lead scores in your CRM.
- **Chat Output**: Returns a confirmation summary of the lead score and action taken.

### 3) Run the Flow
Use the Playground to test your scoring logic with these prompts:
- `Score the latest batch of visitors from Leadfeeder and update the CRM.`
- `Identify all accounts with an intent score above 80 and notify the sales team.`
- `List the top 5 most active companies currently visiting our pricing page.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets raw visitor data into a prioritized score.
- **Recommended instruction pattern:**
    - "Analyze the provided Leadfeeder visitor data and compare it against our defined ICP criteria."
    - "Assign a numerical intent score (0-100) based on page engagement and visit frequency."
    - "Format the output to update the CRM field 'Intent_Score' and 'Last_Intent_Update'."

### 2) Composio Toolset Node
- Requires a valid API key for your CRM (e.g., Salesforce, HubSpot) and Leadfeeder.
- Ensure the connection scope includes read/write access to Lead/Account objects.

### 3) Tool Availability
- **Leadfeeder API**: For fetching visitor behavior and firmographic data.
- **CRM API**: For updating lead records and triggering sales notifications.
- **Notification Service**: For alerting the sales team via Slack or Email.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate comprehensive reports on account activity and firmographic data.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent data across multiple platforms with automated conflict resolution.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Identify and score new sales opportunities based on lead signals.
