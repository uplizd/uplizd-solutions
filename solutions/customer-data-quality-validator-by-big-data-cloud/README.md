# Customer Data Quality Validator (Uplizd) - Automated CRM contact enrichment and hygiene

## Summary
The Customer Data Quality Validator is an intelligent Uplizd workflow designed to maintain a single source of truth by automatically auditing, validating, and enriching customer contact records. By leveraging the Composio Toolset to interface with your CRM, this solution eliminates manual data entry errors, reduces record decay, and ensures your sales and marketing teams are always working with high-fidelity, actionable lead information.

---

## Demo
![Customer Data Quality Validator workflow showing automated validation and enrichment steps](image.png)
**Alt text (SEO-ready):** Customer Data Quality Validator Uplizd workflow for CRM data hygiene, contact validation, and automated record enrichment using Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0iI2ZmZiI+PHBhdGggZD0iTTEyIDJMMiAxMnYxMGgyMFYxMkwxMiAyeiIvPjwvc3ZnPg==)](https://uplizd.ai/solutions/6c7d0b74-bd15-5416-9371-d6ca6e11676a)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** crm, data validation, contact enrichment, data quality, sales operations, composio, ai workflow
- This solution bridges the gap between raw, messy CRM inputs and high-quality, reliable customer intelligence.

---

## Who is this for?
This solution is designed for teams managing high-volume customer data who need to ensure accuracy across their tech stack.

- **Sales Operations Manager**
    - Automates the cleanup of lead databases to ensure sales reps spend time on verified, reachable prospects.
- **Data Analyst**
    - Reduces the time spent on manual data scrubbing and normalization tasks, allowing for faster reporting cycles.
- **CRM Administrator**
    - Maintains strict data governance standards by automatically flagging and fixing incomplete or malformed contact entries.
- **Growth Marketer**
    - Increases campaign deliverability by ensuring contact lists are accurate and enriched with the latest professional data.

---

## Features
- **Automated Validation**
    - Real-time verification of email formats, phone numbers, and physical addresses against global standards.
- **Intelligent Enrichment**
    - Automatically pulls missing firmographic or contact details to complete sparse CRM profiles.
- **Composio Toolset Integration**
    - Seamlessly connects to major CRM platforms to read, update, and sync contact records without manual intervention.
- **Conflict Resolution**
    - Identifies and merges duplicate records based on configurable logic to maintain a clean database.
- **Compliance Monitoring**
    - Ensures that all contact data updates adhere to regional privacy regulations and internal data policies.

---

## Use Cases
**Lead Management**
- Automatically validate new inbound leads from web forms before they reach the CRM.
- Enrich existing lead records with job titles and company sizes to improve lead scoring accuracy.

**Data Hygiene Maintenance**
- Run scheduled audits on the entire contact database to identify and flag stale or decayed information.
- Standardize naming conventions and formatting across all contact fields for consistent reporting.

**Sales Pipeline Optimization**
- Verify contact details for high-value accounts to ensure sales outreach reaches the correct decision-makers.
- Update contact status fields based on validation results to prioritize active, reachable leads.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your CRM credentials within the Composio Toolset node.
3. Configure the trigger settings to define which contact records should be audited.
4. Ensure nodes are correctly mapped from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to validate specific contact records.
- **Agent**: Analyzes the input data, performs logic checks, and determines the necessary enrichment steps.
- **Composio Toolset**: Executes API calls to your CRM to fetch, validate, and update contact fields.
- **Chat Output**: Returns a summary report of the validation results and any updates applied to the CRM.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Validate all new leads created in the last 24 hours.`
- `Check the contact record for john.doe@example.com and enrich missing fields.`
- `Run a full audit on the 'Prospects' list and flag records with invalid email formats.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic controller for data validation and enrichment decisions.
- Use a high-reasoning model to ensure accurate interpretation of CRM data fields.
- Instruct the agent to prioritize data integrity and flag any records that require human review.
- Define specific mapping rules for how the agent should handle missing or conflicting contact information.

### 2) Composio Toolset Node
- Provide your CRM API key and ensure the connection scope includes read/write access to Contacts and Leads objects.
- Configure the toolset to handle rate limits and batch processing for large datasets.

### 3) Tool Availability
- **CRM Read/Write**: Access to fetch and update contact objects.
- **Data Validation API**: Capability to verify email and phone number syntax.
- **Enrichment Service**: Ability to query external databases for missing contact attributes.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate the collection of firmographic data for target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with conflict resolution.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Comprehensive tools for bulk data cleanup and formatting.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Deep-dive research assistant for sales prospecting.
