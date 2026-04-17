# Dynamic Lead Scoring Engine (Uplizd) - Real-time lead prioritization and engagement analytics

## Summary
The Dynamic Lead Scoring Engine is an intelligent Uplizd workflow that automates the qualification of inbound leads by analyzing engagement data, behavioral signals, and historical conversion patterns. By leveraging the Composio Toolset to integrate with your CRM and marketing platforms, this solution ensures your sales team focuses on high-intent prospects, drastically reducing manual triage time and increasing pipeline velocity.

---

## Demo
![Dynamic Lead Scoring Engine workflow showing CRM data ingestion, AI scoring agent, and automated lead routing](image.png)
**Alt text (SEO-ready):** Dynamic Lead Scoring Engine workflow in Uplizd, showing automated CRM lead qualification, behavioral analysis, and sales pipeline prioritization using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/06249cf7-3cc5-520b-883c-d0217f802f38)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead scoring, sales pipeline, lead qualification, omnisend, data sync, ai workflow, composio
- This solution bridges the gap between raw marketing engagement and actionable sales intelligence by automating the lead scoring lifecycle.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual lead sorting and improve conversion rates.

- **Sales Development Representative (SDR)**
    - Receives prioritized lead lists daily, allowing for immediate outreach to high-intent prospects.
- **Revenue Operations Manager**
    - Standardizes lead scoring criteria across the organization to ensure consistent data hygiene and pipeline reporting.
- **Marketing Manager**
    - Gains visibility into which campaigns drive the highest quality leads, enabling better budget allocation.
- **Sales Director**
    - Monitors aggregate lead quality trends to forecast revenue more accurately based on real-time engagement data.

---

## Features
- **Behavioral Scoring Engine**
    - Automatically assigns point values to leads based on specific actions like email opens, link clicks, and website visits.
- **Real-time CRM Integration**
    - Uses the Composio Toolset to push updated scores directly into your CRM, ensuring sales reps always see the latest data.
- **Dynamic Threshold Alerts**
    - Triggers instant notifications for sales teams when a lead crosses a high-intent threshold, facilitating "hot" lead follow-up.
- **Historical Data Analysis**
    - Learns from past conversion patterns to refine scoring logic, ensuring the model evolves with your business.
- **Automated Lead Routing**
    - Assigns leads to the appropriate account owner based on score and territory, removing manual assignment bottlenecks.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads that have engaged with pricing pages or high-value content within the last 24 hours.
- Rank incoming leads by combining demographic data with real-time behavioral signals from your marketing stack.

**Sales Pipeline Optimization**
- Identify "stalled" leads that have high scores but haven't been contacted, triggering a reminder for the assigned rep.
- Clean up lead databases by archiving or re-nurturing leads that consistently fail to meet minimum engagement scores.

**Marketing & Sales Alignment**
- Sync lead quality feedback from sales reps back into marketing platforms to improve future lead generation targeting.
- Generate weekly reports on lead quality trends to identify which marketing channels are producing the most sales-ready prospects.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Configure your CRM and Marketing platform credentials within the connection manager.
4. Ensure nodes are correctly mapped to your specific CRM fields and scoring thresholds.

### 2) Setup the Nodes
- **Chat Input**: Accepts lead data triggers or manual requests for lead score updates.
- **Agent**: Analyzes engagement data against defined scoring rules to determine lead priority.
- **Composio Toolset**: Executes read/write operations to your CRM (e.g., updating lead status, adding notes).
- **Chat Output**: Returns the final score and a summary of the lead's recent activity to the user.

### 3) Run the Flow
- `Score all leads from the last 24 hours and update their status in Salesforce.`
- `Identify high-intent leads that have visited the pricing page more than three times.`
- `Generate a summary report of the top 10 leads currently in the pipeline.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that interprets engagement data and applies your scoring business rules.
- Instruction: "Analyze the provided lead engagement data and assign a score based on the defined activity weights."
- Instruction: "Compare current lead score against historical conversion benchmarks to determine if the lead is 'Hot', 'Warm', or 'Cold'."
- Instruction: "Format the output as a structured JSON object for the CRM update tool."

### 2) Composio Toolset Node
- Requires an active API key for your CRM (e.g., Salesforce, HubSpot, or Omnisend).
- Ensure the connection scope includes read/write permissions for Lead and Contact objects.

### 3) Tool Availability
- **CRM Search**: Locate existing lead records by email or ID.
- **Lead Update**: Modify field values such as `Lead_Score__c` or `Lead_Status`.
- **Activity Log**: Retrieve recent engagement history from marketing platforms.
- **Notification Service**: Send alerts to Slack or Email when a lead reaches a critical score.

---

## Related Solutions
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage pipeline stages and stalled deal follow-ups.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
- [Account Intelligence Reporter](../account-intelligence-reporter/README.md) - Gather and report on account-level insights for sales teams.
