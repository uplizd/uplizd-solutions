# Account Expansion Identifier (Uplizd) - Automate upsell discovery through growth pattern analysis

## Summary
The Account Expansion Identifier is an intelligent Uplizd workflow that monitors customer data and usage signals to pinpoint high-value upsell and cross-sell opportunities. By leveraging Crustdata’s real-time intelligence, this solution empowers RevOps and Sales teams to proactively identify accounts ready for expansion, ensuring no revenue-generating signal goes unnoticed in your pipeline.

---

## Demo
![Account Expansion Identifier workflow showing data ingestion from Crustdata to identify upsell opportunities](../image.png)
**Alt text (SEO-ready):** Account Expansion Identifier Uplizd workflow, automated upsell discovery, Crustdata CRM integration, sales pipeline growth, and revenue intelligence.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6e42a25d-99e6-59a9-8a20-cfe32a394f90)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, crustdata, account expansion, upsell, revenue intelligence, sales pipeline, data sync, ai workflow
- This solution bridges the gap between raw company growth data and actionable sales insights to drive account expansion.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to automate the identification of growth signals within their existing customer base.

- **Account Executives**
    - Receive automated alerts when assigned accounts show significant growth indicators or hiring spikes.
- **Sales Operations Managers**
    - Standardize the process of identifying expansion candidates across the entire CRM database.
- **Customer Success Managers**
    - Proactively identify accounts that have outgrown their current tier based on real-time organizational data.
- **Growth Marketers**
    - Align targeted expansion campaigns with accounts that demonstrate high-intent growth patterns.

---

## Features
- **Real-time Growth Tracking**
    - Utilizes Crustdata to monitor company headcount, funding, and technology stack changes as they happen.
- **Automated Opportunity Scoring**
    - Applies intelligent logic to rank accounts based on expansion potential, prioritizing the most promising leads.
- **CRM Integration**
    - Seamlessly pushes identified expansion signals directly into your CRM to update deal status or create new tasks.
- **Customizable Thresholds**
    - Define specific growth triggers—such as employee growth percentages—that define an "expansion-ready" account.
- **Actionable Insights**
    - Generates summarized briefings for sales teams, explaining exactly why an account was flagged for expansion.

---

## Use Cases
**Proactive Upsell Identification**
- Automatically flag accounts that have increased their headcount by 20% or more in a single quarter.
- Trigger a "Review for Expansion" task in your CRM when a target account announces a new funding round.

**Account Health Monitoring**
- Identify dormant accounts that are showing signs of renewed activity or organizational restructuring.
- Sync growth signals to Customer Success dashboards to prepare for upcoming contract renewal discussions.

**Market Expansion Research**
- Analyze existing customer segments to find similar companies that match the growth profiles of your most successful accounts.
- Generate weekly reports of "High Growth" prospects within your current CRM database for targeted outreach.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and click **Import Flow**.
3. Authenticate your Crustdata and CRM connections within the integration settings.
4. Ensure nodes are correctly mapped to your specific CRM objects and Crustdata API credentials.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to scan for expansion opportunities.
- **Agent**: Processes growth data against your defined expansion criteria to filter high-value leads.
- **Composio Toolset**: Executes the data retrieval from Crustdata and writes the resulting insights to your CRM.
- **Chat Output**: Delivers a summary report of identified expansion opportunities to the user or team channel.

### 3) Run the Flow
Use the Playground to test your expansion logic with these prompts:
- `Scan all accounts in the 'Enterprise' segment for headcount growth over 15% this month.`
- `Identify any accounts that have recently raised Series B funding and update their CRM status.`
- `Create a summary list of top 5 accounts showing the strongest growth signals for my review.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting growth data to make business decisions.
- **Role:** Act as a Revenue Intelligence Analyst.
- **Instruction Pattern:** 
    - Focus on identifying positive growth signals (hiring, funding, expansion).
    - Ignore noise and prioritize accounts with the highest revenue potential.
    - Format output as clear, actionable CRM update instructions.

### 2) Composio Toolset Node
- **API Key:** Ensure your Crustdata API key is active and has read-access to company growth endpoints.
- **Connection Scope:** Grant the toolset permission to read company data and write/update records in your CRM (e.g., Salesforce or HubSpot).

### 3) Tool Availability
- **Crustdata API:** Provides real-time organizational growth and firmographic data.
- **CRM Connector:** Enables reading account lists and writing expansion-related tasks or deal updates.
- **Data Processor:** Handles the logic for filtering and scoring account signals.

---

## Related Solutions
- [../crm-data-sync-manager/README.md](CRM Data Sync Manager) - Orchestrates complex data synchronization across multiple CRM platforms.
- [../deal-pipeline-manager/README.md](Deal Pipeline Manager) - Manages deal stages and follow-up cadences for sales teams.
- [../deal-oppotunity-tracker/README.md](Deal Opportunity Tracker) - Identifies and scores new sales opportunities based on lead signals.
- [../crm-data-quality-agent/README.md](CRM Data Quality Agent) - Maintains high-standard data hygiene within your CRM records.
