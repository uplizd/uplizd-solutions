# Deal Pipeline Monitor (Uplizd) - Real-time deal flow tracking and pipeline health alerts

## Summary
The Deal Pipeline Monitor is an intelligent Uplizd workflow designed to provide real-time visibility into your sales pipeline, ensuring that deal velocity remains high and potential bottlenecks are identified before they impact revenue. By integrating directly with your CRM, this solution automates the tracking of deal stages, flags stalled opportunities, and alerts sales teams to critical updates, serving as a single source of truth for RevOps and account managers to maintain pipeline hygiene and accelerate closing cycles.

---

## Demo
![Deal Pipeline Monitor dashboard showing real-time opportunity tracking and stage progression alerts](image.png)
**Alt text (SEO-ready):** Deal Pipeline Monitor dashboard showing real-time opportunity tracking, sales pipeline health alerts, and CRM integration workflows on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b722f91b-a450-5643-8a69-9d131ab26544)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, salesforce, hubspot, pipeline, deal tracking, revenue operations, sales velocity, ai workflow
- This solution bridges the gap between raw CRM data and actionable sales intelligence, enabling teams to optimize their pipeline management through automated oversight.

---

## Who is this for?
This solution is designed for sales and operations professionals who need to maintain a high-velocity pipeline and ensure no opportunity falls through the cracks.

- **Sales Managers**
    - Gain immediate visibility into team performance and identify stalled deals that require intervention.
- **Account Executives**
    - Receive automated notifications on deal stage changes and upcoming follow-up requirements.
- **RevOps Specialists**
    - Standardize pipeline hygiene and ensure data consistency across the entire sales lifecycle.
- **Sales Development Reps (SDRs)**
    - Prioritize outreach based on real-time opportunity scoring and recent activity signals.

---

## Features
- **Real-time Pipeline Sync**
    - Automatically pulls deal data from your CRM to provide an up-to-the-minute view of your sales funnel.
- **Stalled Deal Detection**
    - Uses intelligent logic to flag opportunities that have remained in a single stage beyond the defined threshold.
- **Automated Alerting**
    - Triggers proactive notifications via email or Slack when high-value deals reach critical milestones.
- **Composio-Powered CRM Integration**
    - Leverages the Composio Toolset to execute read/write operations across major CRM platforms like Salesforce and HubSpot.
- **Pipeline Velocity Analytics**
    - Calculates the time spent in each stage to help teams identify and resolve process bottlenecks.

---

## Use Cases
**Pipeline Health Monitoring**
- Automatically flag deals that have not been updated in the last 14 days.
- Generate weekly summaries of pipeline movement for leadership review.

**Opportunity Prioritization**
- Rank incoming leads based on deal size and historical conversion probability.
- Alert the sales team when a high-value opportunity enters the "Negotiation" stage.

**Sales Process Compliance**
- Ensure all mandatory fields are populated before a deal can advance to the "Closed-Won" stage.
- Notify managers when a deal is moved backward in the pipeline without a valid reason.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and click "Import" to load the workflow canvas.
3. Connect your CRM credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your natural language request for pipeline status or specific deal updates.
*   **Agent**: Processes the request, interprets CRM data, and determines the necessary actions.
*   **Composio Toolset**: Executes secure API calls to fetch or update deal records in your CRM.
*   **Chat Output**: Delivers a concise, human-readable summary of the pipeline status or requested deal information.

### 3) Run the Flow
Use the Uplizd Playground to test your pipeline monitor:
- `Show me all deals that have been stalled in the 'Discovery' stage for more than 10 days.`
- `List all high-value opportunities that are currently in the 'Negotiation' phase.`
- `Provide a summary of pipeline health for the current quarter.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your sales operations analyst.
- Use a model capable of complex reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a sales operations assistant. Use the provided tools to query the CRM, identify stalled opportunities, and summarize pipeline health."
- Ensure the agent is instructed to prioritize high-value deals and maintain professional, actionable tone.

### 2) Composio Toolset Node
- Provide your API key to authenticate the connection to your CRM.
- Set the connection scope to allow read/write access to 'Deals', 'Opportunities', and 'Accounts' objects.

### 3) Tool Availability
- `crm_get_deals`: Fetch active opportunities with filtering capabilities.
- `crm_update_deal`: Modify deal stages or update custom fields.
- `crm_list_tasks`: Retrieve pending follow-ups associated with specific deals.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Comprehensive management of sales stages and follow-up workflows.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Automated multi-platform synchronization for consistent CRM data.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automated cleanup and maintenance of CRM records.
