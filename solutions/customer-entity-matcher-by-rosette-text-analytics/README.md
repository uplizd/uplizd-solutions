# Customer Entity Matcher (Uplizd) - Intelligent deduplication and entity resolution for CRM records

## Summary
The Customer Entity Matcher (Uplizd) leverages Rosette Text Analytics to identify, match, and deduplicate customer records across disparate data sources. By normalizing entity names and addresses, this workflow ensures a single source of truth for your customer database, eliminating redundant entries and improving data hygiene for downstream sales and support operations.

---

## Demo
![Customer Entity Matcher workflow showing Rosette Text Analytics processing CRM records for deduplication](image.png)
**Alt text (SEO-ready):** Customer Entity Matcher workflow in Uplizd using Rosette Text Analytics for CRM data deduplication and entity resolution.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/35213144-1cf6-545f-aa8a-5e49ddfdbe52)

---

## Category
**Data integration**
- `crm`, `deduplication`, `rosette`, `data hygiene`, `entity resolution`, `data sync`, `composio`, `ai workflow`
This solution bridges the gap between raw customer data and actionable intelligence by automating the complex process of entity matching.

---

## Who is this for?
This solution is designed for data-driven teams looking to maintain pristine records and eliminate manual data cleanup tasks.

- **Data Operations Manager**
    - Automates the identification of duplicate records to maintain high-quality data standards across the organization.
- **CRM Administrator**
    - Reduces manual oversight by implementing automated entity resolution logic within the existing CRM ecosystem.
- **Sales Operations Lead**
    - Ensures sales representatives have a unified view of accounts, preventing cross-territory conflicts and redundant outreach.
- **Customer Success Manager**
    - Provides a consolidated history of customer interactions by merging fragmented profiles into a single, accurate entity.

---

## Features
- **Advanced Entity Resolution**
    - Uses Rosette Text Analytics to perform deep linguistic analysis, identifying matches even when names or addresses are formatted differently.
- **Automated Data Normalization**
    - Standardizes inconsistent input formats into a unified schema, ensuring compatibility across your entire tech stack.
- **Real-time Deduplication Pipeline**
    - Processes incoming records instantly via the Composio Toolset to prevent duplicate entries from ever reaching your primary database.
- **Intelligent Conflict Resolution**
    - Employs configurable logic to determine which record attributes take precedence during the merge process.
- **Seamless CRM Integration**
    - Connects directly to your CRM via Composio to push cleaned, matched entities back into your production environment.

---

## Use Cases
**Data Hygiene & Cleanup**
- Identifying and merging duplicate customer profiles created by manual entry errors.
- Standardizing address formats across global customer records to ensure accurate territory mapping.

**Sales Pipeline Optimization**
- Consolidating lead data from multiple marketing campaigns to provide a clear view of account engagement.
- Preventing duplicate outreach by ensuring sales teams are targeting unique, verified entities.

**Support Operations**
- Aggregating support tickets from the same customer across different communication channels.
- Maintaining a consistent customer profile to provide personalized, context-aware support experiences.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Customer Entity Matcher template using the provided solution link.
3. Authenticate your CRM and Rosette Text Analytics credentials within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw customer record data or search queries.
- **Agent**: Analyzes input and orchestrates the matching logic using Rosette.
- **Composio Toolset**: Executes the API calls to fetch and update CRM records.
- **Chat Output**: Returns the status of the match, including merged record IDs or deduplication reports.

### 3) Run the Flow
Use the Playground to test your entity matching logic with these prompts:
- `Find and merge duplicate records for 'Acme Corp' in our Salesforce instance.`
- `Check for address inconsistencies in the latest batch of imported leads.`
- `Identify any potential duplicate entities for 'John Doe' and merge them into the primary record.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making layer for entity resolution.
- Configure the agent to prioritize accuracy over speed for high-stakes account data.
- Use system instructions to define the threshold for a "match" versus a "potential duplicate."
- Enable logging to track every merge action performed by the agent.

### 2) Composio Toolset Node
- Provide your API key for the relevant CRM (e.g., Salesforce, HubSpot).
- Set the connection scope to allow read/write access to lead and contact objects.

### 3) Tool Availability
- **Entity Search**: Capability to query the CRM for existing records.
- **Data Normalization**: Access to Rosette endpoints for string and address cleanup.
- **Record Update/Merge**: Ability to perform bulk updates or merge operations on identified duplicates.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with verified contact details.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain overall CRM health through automated cleanup.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospective accounts.
