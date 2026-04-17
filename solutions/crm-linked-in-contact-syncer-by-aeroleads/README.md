# CRM LinkedIn Contact Syncer (Uplizd) - Automate professional profile enrichment and CRM synchronization

## Summary
The CRM LinkedIn Contact Syncer is an intelligent Uplizd workflow that bridges the gap between professional networking data and your CRM. By leveraging the Composio Toolset to interface with LinkedIn and your CRM platform, this solution automates the enrichment of contact records, ensuring your sales team has access to real-time professional insights, updated job titles, and verified contact information without manual data entry.

---

## Demo
![Uplizd CRM LinkedIn Contact Syncer workflow diagram showing data flow from LinkedIn to CRM](image.png)
**Alt text (SEO-ready):** Uplizd CRM LinkedIn Contact Syncer workflow diagram showing data flow from LinkedIn to CRM for automated contact enrichment and sales pipeline hygiene.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/6f9b03d5-4f06-54fe-8b18-c98f4e1087fd)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, linkedin, data enrichment, salesforce, hubspot, lead qualification, data hygiene, composio
- This solution streamlines the integration between professional social networks and CRM systems to maintain high-quality, actionable lead data.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual research and improve data accuracy.

- **Sales Development Representatives (SDRs)**
    - Reduces time spent manually researching prospect backgrounds and updating CRM fields.
- **RevOps Managers**
    - Ensures CRM data hygiene by automatically syncing verified professional details across the pipeline.
- **Account Executives (AEs)**
    - Provides instant access to the latest prospect information, enabling more personalized outreach.
- **Growth Marketers**
    - Improves lead scoring accuracy by enriching contact profiles with current job titles and company data.

---

## Features
- **Automated Profile Enrichment**
    - Automatically pulls current job titles, company affiliations, and professional summaries from LinkedIn profiles.
- **Real-time CRM Sync**
    - Updates existing contact records in your CRM instantly, ensuring the single source of truth remains current.
- **Intelligent Data Mapping**
    - Uses the Composio Toolset to intelligently map LinkedIn data points to the correct CRM fields.
- **Conflict Resolution**
    - Prevents data overwriting by applying logic to prioritize verified LinkedIn data over outdated CRM entries.
- **Pipeline Hygiene Monitoring**
    - Flags incomplete contact records for automated enrichment, keeping your sales funnel clean and actionable.

---

## Use Cases
**Lead Qualification**
- Automatically enrich incoming leads with LinkedIn data to verify seniority and company fit.
- Update lead status based on professional profile changes detected during the sync process.

**Sales Outreach Preparation**
- Populate CRM notes with recent LinkedIn activity to help AEs craft personalized conversation starters.
- Sync professional summaries to the CRM to assist in better account mapping and territory planning.

**Data Maintenance**
- Run bulk enrichment cycles to update stale contact records with the latest professional information.
- Standardize job title formatting across the CRM by pulling verified data directly from LinkedIn profiles.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your dashboard.
3. Connect your CRM and LinkedIn accounts via the Composio integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the contact name or LinkedIn URL to trigger the search.
- **Agent**: Orchestrates the logic, interpreting the request and deciding which tool to invoke.
- **Composio Toolset**: Executes the API calls to fetch LinkedIn data and perform CRM updates.
- **Chat Output**: Returns a confirmation summary of the enriched data and the updated CRM record status.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Enrich the contact record for John Doe at Acme Corp using his LinkedIn profile.`
- `Find the latest job title for the contact with email john.doe@example.com and update the CRM.`
- `Sync LinkedIn profile details for all leads in the 'New' status within the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that parses contact information and manages the tool-calling sequence.
- **Role**: Data Orchestrator and CRM Liaison.
- **Recommended instruction pattern**:
    - Identify the target contact from the input provided by the user.
    - Invoke the LinkedIn search tool to retrieve the most recent professional profile data.
    - Map the retrieved data to the corresponding CRM fields and confirm the update.

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and authorized for LinkedIn and your specific CRM (e.g., Salesforce or HubSpot).
- **Connection Scope**: Grant read access for LinkedIn and write/update access for your CRM contact objects.

### 3) Tool Availability
- **LinkedIn Search**: Capability to fetch profile summaries, current roles, and company data.
- **CRM Update**: Capability to write enriched data to specific contact fields.
- **Data Validation**: Capability to check for existing records before performing updates.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Automates the collection of deep account-level insights.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Manages multi-platform data synchronization and conflict resolution.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Provides detailed firmographic and contact research for sales teams.
