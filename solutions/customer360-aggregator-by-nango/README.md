# Customer 360 Aggregator (Uplizd) - Unified customer intelligence across fragmented business systems

## Summary
The Customer 360 Aggregator is an intelligent Uplizd workflow that synchronizes disparate data points from multiple business platforms into a single, comprehensive customer profile. By leveraging the Composio Toolset to query and normalize data from various CRM and support systems, this solution eliminates data silos, providing teams with a real-time, 360-degree view of customer interactions, history, and health to drive informed decision-making.

---

## Demo
![Customer 360 Aggregator workflow showing data flow from CRM and support tools into a unified profile](image.png)
**Alt text (SEO-ready):** Customer 360 Aggregator Uplizd workflow for CRM data synchronization, multi-platform data integration, and unified customer profile management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f04ad16a-2600-5b06-9aed-71ac9a2f90b5)

---

## Category
**Primary category:** CRM data integration
**Secondary tags:** crm, data sync, customer 360, composio, data hygiene, unified profile, business intelligence, salesops
This solution bridges the gap between disconnected business applications to ensure a consistent, high-fidelity view of customer data across the enterprise.

---

## Who is this for?
This solution is designed for operations and support teams managing complex customer lifecycles across multiple platforms.

* **RevOps Manager**
    * Ensures data consistency across the tech stack to improve reporting accuracy and pipeline visibility.
* **Customer Success Lead**
    * Accesses a holistic view of account health and interaction history to proactively manage renewals and churn.
* **Sales Operations Analyst**
    * Automates the aggregation of lead and account data to reduce manual research time for the sales team.
* **Support Manager**
    * Provides agents with immediate context from CRM and billing systems to resolve tickets faster and more effectively.

---

## Features
- **Cross-Platform Data Normalization**
    Standardizes inconsistent data formats from various sources into a unified schema for reliable reporting.
- **Real-Time Intelligence Retrieval**
    Uses the Composio Toolset to fetch live data from connected CRMs and support platforms on demand.
- **Unified Profile Synthesis**
    Automatically merges interaction logs, support tickets, and account metadata into a single, readable summary.
- **Automated Sync Logic**
    Ensures that the aggregated profile remains updated by triggering refreshes based on specific event signals.
- **Context-Aware Agent Logic**
    Employs an intelligent agent to identify missing data points and proactively query relevant tools to fill gaps.

---

## Use Cases
**Customer Health Monitoring**
* Aggregating support ticket volume and recent CRM notes to calculate an automated account health score.
* Identifying at-risk customers by correlating usage drops with recent negative support interactions.

**Sales Intelligence Enrichment**
* Pulling recent communication history from multiple channels to prepare detailed account briefings for sales reps.
* Mapping cross-sell opportunities by analyzing product usage data against current contract status in the CRM.

**Support Efficiency**
* Providing support agents with a summary of the customer's entire relationship history within the ticket interface.
* Automating the identification of high-priority accounts based on aggregated revenue and support tier data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and project destination.
3. Configure your API credentials for the connected CRM and support platforms.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the customer identifier (e.g., email or account ID) from the user.
* **Agent**: Processes the request, determines which tools to call, and synthesizes the final profile.
* **Composio Toolset**: Executes secure API calls to fetch data from your integrated business systems.
* **Chat Output**: Displays the consolidated 360-degree customer profile to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
* `Get a 360-degree summary for customer: john.doe@example.com`
* `What is the current account health and recent support history for Acme Corp?`
* `Aggregate all open opportunities and recent ticket activity for account ID 98765.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer for data retrieval and synthesis.
* Use a model with high reasoning capabilities to handle multi-step tool calls.
* Instruct the agent to prioritize data accuracy and cite sources when possible.
* Configure the system prompt to enforce a specific output format (e.g., Markdown table or structured list).

### 2) Composio Toolset Node
* Connect your specific CRM (e.g., Salesforce, HubSpot) and support tool (e.g., Zendesk, Intercom) via the Composio dashboard.
* Ensure the agent has "Read" access to the necessary objects: Accounts, Contacts, Tickets, and Opportunities.

### 3) Tool Availability
* **CRM Connector**: Fetch account details, contact info, and deal status.
* **Support Connector**: Retrieve ticket history, status, and priority levels.
* **Data Transformer**: Normalize dates, currency, and string formats across systems.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes records between platforms to maintain data integrity.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Cleans and formats CRM data to prevent decay and duplication.
* [Account Research Assistant](../account-research-assistant/README.md) - Automates deep-dive research on prospects and accounts.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Tracks and manages sales pipeline stages and deal velocity.
