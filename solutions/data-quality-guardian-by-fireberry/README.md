# Data Quality Guardian (Uplizd) - Automated CRM Data Standardization and Hygiene

## Summary
The Data Quality Guardian is an intelligent Uplizd workflow designed to maintain pristine CRM data integrity by automatically identifying, cleaning, and standardizing records. By leveraging the Composio Toolset to interface with your CRM, this solution eliminates manual data entry errors, reduces data decay, and ensures your sales and marketing teams operate from a single source of truth, ultimately increasing pipeline velocity and operational efficiency.

---

## Demo
![Data Quality Guardian workflow showing automated CRM record cleaning and standardization](image.png)
**Alt text (SEO-ready):** Data Quality Guardian Uplizd workflow for automated CRM data hygiene, record standardization, and data integration using Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue?logo=uplizd)](https://uplizd.ai/solutions/30fbfa57-e03b-5f7b-a322-82fe4d5d638f)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** crm, fireberry, data quality, automation, composio, data sync, sales operations, record management
- This solution bridges the gap between raw, inconsistent CRM inputs and high-quality, actionable business intelligence through automated validation logic.

---

## Who is this for?
This solution is designed for teams managing high-volume customer data who need to enforce strict formatting and accuracy standards.

- **RevOps Manager**
    - Ensures consistent data architecture across the entire sales funnel for accurate reporting.
- **CRM Administrator**
    - Automates the tedious process of deduplication and field-level cleanup to reduce technical debt.
- **Sales Operations Lead**
    - Increases team productivity by ensuring lead and account data is always formatted correctly for outreach.
- **Data Analyst**
    - Relies on cleaner, standardized datasets to generate reliable performance insights and forecasting.

---

## Features
- **Automated Data Normalization**
    - Automatically formats phone numbers, addresses, and naming conventions to match your organization's specific standards.
- **Real-time Validation Engine**
    - Triggers immediate checks upon record creation or update to catch errors before they propagate through your systems.
- **Intelligent Deduplication**
    - Identifies and flags potential duplicate records based on email, company domain, or unique identifiers using Composio-integrated CRM tools.
- **Compliance-Aware Cleanup**
    - Ensures that data modification processes respect privacy regulations and internal data governance policies.
- **Seamless CRM Integration**
    - Connects directly to your CRM (e.g., Fireberry) to perform bulk updates and field corrections without manual intervention.

---

## Use Cases
**Data Standardization**
- Automatically convert all incoming lead names to Title Case and standardize state/country abbreviations.
- Normalize phone number formats to E.164 standards to ensure compatibility with global dialing tools.

**CRM Hygiene Maintenance**
- Identify and merge duplicate account records that share the same website domain or primary contact email.
- Periodically scan for missing mandatory fields and trigger alerts or auto-fill actions based on available metadata.

**Sales Pipeline Accuracy**
- Ensure that all opportunity stages are mapped to valid, standardized CRM picklist values to prevent reporting gaps.
- Clean up outdated contact information by verifying email deliverability status against CRM records.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the Data Quality Guardian workflow.
3. Connect your CRM account (e.g., Fireberry) via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to initiate a data audit.
- **Agent**: Processes the data, applies formatting logic, and determines necessary cleanup actions.
- **Composio Toolset**: Executes read/write operations to your CRM to update records.
- **Chat Output**: Returns a summary report of the records cleaned, updated, or flagged for review.

### 3) Run the Flow
Use the Playground to test your data cleanup:
- `Clean all lead records created in the last 24 hours.`
- `Standardize the phone number format for all contacts in the 'New' stage.`
- `Identify and merge duplicate accounts for the domain 'example.com'.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic layer for identifying data anomalies.
- Use a high-reasoning model (e.g., GPT-4o) to ensure accurate field mapping.
- Set the system prompt to prioritize data integrity and strict adherence to formatting rules.
- Enable tool-calling capabilities to allow the agent to interact with the CRM API.

### 2) Composio Toolset Node
- Provide your API key within the Composio node settings.
- Ensure the connection scope includes read/write permissions for the specific CRM modules (Leads, Accounts, Contacts) you intend to manage.

### 3) Tool Availability
- **CRM Read/Search**: To fetch current record states and identify inconsistencies.
- **CRM Update/Patch**: To apply standardized values and formatting fixes.
- **CRM Merge**: To consolidate duplicate records identified by the agent.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research into target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes data across multiple platforms to ensure consistency.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages pipeline stages and identifies stalled opportunities.
