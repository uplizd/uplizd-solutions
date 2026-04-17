# Smart Contact List Manager (Uplizd) - Automated CRM list hygiene and engagement segmentation

## Summary
The Smart Contact List Manager is an intelligent Uplizd AI workflow designed to automate the organization, cleaning, and segmentation of your CRM contact lists. By leveraging real-time engagement patterns, this solution ensures your marketing and sales teams maintain a single source of truth, significantly increasing pipeline velocity and data hygiene by removing stale entries and categorizing active leads automatically.

---

## Demo
![Smart Contact List Manager workflow showing CRM data ingestion, AI-driven segmentation, and automated list updates](image.png)

**Alt text (SEO-ready):** Smart Contact List Manager Uplizd workflow for CRM data hygiene, contact segmentation, and automated list synchronization using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2ef53c31-4141-5709-bdb9-5c6342acdf51)

---

## Category
- **Primary category:** CRM data hygiene
- **Secondary tags:** crm, contact management, data sync, sales automation, lead segmentation, composio, ai workflow, data quality
- This solution bridges the gap between raw CRM data and actionable marketing lists by applying AI-driven logic to maintain high-quality contact records.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual data entry and improve outreach precision.

- **Sales Operations Manager**
    - Automates the removal of duplicate or decayed contacts to ensure clean reporting.
- **Marketing Lead**
    - Segments contact lists based on real-time engagement data for higher conversion rates.
- **Account Executive**
    - Receives prioritized, high-intent contact lists directly in their CRM workflow.
- **RevOps Specialist**
    - Maintains data integrity across multiple platforms through automated synchronization and validation.

---

## Features
- **Intelligent Segmentation**
    - Automatically categorizes contacts into tiers based on interaction history and lead scoring.
- **Automated Data Hygiene**
    - Identifies and flags stale or incomplete contact records to prevent CRM bloat.
- **Real-time CRM Sync**
    - Uses the Composio Toolset to push updates instantly to your connected CRM platforms.
- **Engagement-Based Filtering**
    - Filters lists based on specific user behaviors, such as email opens or recent meeting activity.
- **Customizable Logic Nodes**
    - Allows for bespoke rules to define what constitutes a "qualified" contact for your specific business model.

---

## Use Cases
**Lead Qualification**
- Automatically move contacts to a "Hot Lead" list after three positive engagement signals.
- Filter out contacts that have not interacted with marketing materials in over 90 days.

**Data Maintenance**
- Standardize contact formatting (e.g., phone numbers, job titles) across disparate CRM entries.
- Merge duplicate contact records identified by the agent during the synchronization process.

**Campaign Preparation**
- Generate targeted lists for specific email campaigns based on industry or recent activity.
- Exclude unsubscribed or opted-out contacts from new outreach efforts to ensure compliance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Contact List Manager template from the marketplace.
3. Connect your CRM credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked from **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or manual request to refresh contact lists.
- **Agent**: Processes the logic for segmentation and identifies data anomalies.
- **Composio Toolset**: Executes the API calls to read, update, or delete records in your CRM.
- **Chat Output**: Confirms the number of contacts processed and provides a summary of changes.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Refresh my 'Active Leads' list by removing contacts with no activity in 6 months.`
- `Segment all contacts from the 'Tech' industry into a new 'Tech Outreach' list.`
- `Identify and merge duplicate contact entries for 'Acme Corp' in my CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine that evaluates contact data against your business rules.
- Set the system prompt to prioritize data accuracy and strict segmentation criteria.
- Enable tool-calling capabilities to allow the agent to query your CRM database.
- Configure the agent to output a summary report of all modifications made during the run.

### 2) Composio Toolset Node
- Provide your CRM API key to enable secure read/write access.
- Define the connection scope to include only the necessary modules (e.g., Contacts, Leads, Accounts).

### 3) Tool Availability
- **CRM Read/Write**: Access to fetch and update contact fields.
- **Data Validation**: Logic to check for missing or malformed contact information.
- **List Management**: Ability to create, update, or delete CRM list groupings.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich contact records with professional data.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize contact data across multiple platforms.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Perform bulk cleanup and formatting on CRM databases.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate deep-dive research on target accounts.
