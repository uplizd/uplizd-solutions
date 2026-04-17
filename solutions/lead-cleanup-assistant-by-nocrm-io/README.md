# Lead Cleanup Assistant (Uplizd) - Automated CRM data hygiene and lead database optimization

## Summary
The Lead Cleanup Assistant is an intelligent Uplizd workflow designed to automate the maintenance of your lead database by identifying duplicates, correcting formatting errors, and standardizing contact information. By leveraging the Composio Toolset to interface directly with your CRM, this solution ensures high-quality data hygiene, reduces manual administrative overhead, and improves pipeline velocity for sales and marketing teams.

---

## Demo
![Lead Cleanup Assistant workflow interface showing automated data deduplication and formatting nodes](image.png)
**Alt text (SEO-ready):** Lead Cleanup Assistant Uplizd workflow for CRM data hygiene, automated lead deduplication, and contact database optimization using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/ba4ae51b-3e0c-5b75-b522-bcb3b4b4060e)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, lead management, data hygiene, data cleaning, sales operations, composio, ai workflow, database optimization.
This solution streamlines CRM data management by automating the identification and correction of lead records to maintain a single source of truth.

---

## Who is this for?
This solution is built for revenue-focused teams looking to eliminate manual data entry and improve lead quality across their tech stack.

*   **Sales Operations Manager**
    *   Automates routine data scrubbing tasks to ensure clean reporting and accurate forecasting.
*   **Account Executive**
    *   Reduces time spent researching contact details by ensuring lead records are standardized and enriched.
*   **Marketing Operations Specialist**
    *   Maintains list integrity for outbound campaigns by preventing duplicate entries and formatting errors.
*   **CRM Administrator**
    *   Enforces data governance policies automatically, reducing the risk of "dirty" data polluting the pipeline.

---

## Features
- **Automated Deduplication**
    Detects and merges duplicate lead records based on email, phone number, or company domain to maintain a clean database.
- **Data Standardization**
    Automatically formats phone numbers, job titles, and address fields to match your organization's specific naming conventions.
- **Intelligent Error Correction**
    Identifies and flags incomplete or invalid contact entries, prompting for updates or performing auto-corrections where possible.
- **Composio-Powered CRM Sync**
    Utilizes the Composio Toolset to perform real-time read/write operations across major CRM platforms like Salesforce and HubSpot.
- **Customizable Hygiene Rules**
    Allows users to define specific logic for what constitutes a "clean" lead, ensuring the agent acts according to your business requirements.

---

## Use Cases
**Lead Database Maintenance**
*   Running weekly batch jobs to identify and merge duplicate leads created by multiple marketing channels.
*   Standardizing lead source naming conventions to ensure consistent attribution reporting.

**Outbound Campaign Preparation**
*   Validating contact information before syncing leads to an email automation tool to reduce bounce rates.
*   Cleaning up job title fields to enable precise segmentation for targeted sales outreach.

**CRM Data Governance**
*   Flagging leads with missing critical fields (e.g., industry, company size) for manual review by the sales team.
*   Automating the removal of test accounts or inactive leads that clutter the sales pipeline.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the Lead Cleanup Assistant workflow.
3. Connect your CRM credentials via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or manual request to initiate a cleanup task.
*   **Agent**: Processes the cleanup logic, evaluates data against defined rules, and decides on necessary actions.
*   **Composio Toolset**: Executes the API calls to fetch, update, or delete records within your connected CRM.
*   **Chat Output**: Returns a summary report of the cleanup operation, including records merged or corrected.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
* `Clean up the lead database by merging duplicates found in the last 24 hours.`
* `Standardize all phone number formats in the 'New Leads' view.`
* `Identify and flag any leads missing a company domain for manual review.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for data validation and record management.
*   **Instruction Pattern:**
    *   "You are a data hygiene expert; prioritize data integrity and follow strict deduplication rules."
    *   "When an error is detected, attempt to auto-correct based on standard formats before flagging for human review."
    *   "Always provide a summary of changes made to the CRM after every execution."

### 2) Composio Toolset Node
*   **API Key:** Ensure your CRM API key is securely stored in the Composio connection settings.
*   **Connection Scope:** Grant read/write permissions for the specific CRM objects (Leads, Contacts, Accounts) required for your cleanup tasks.

### 3) Tool Availability
*   **CRM Search:** Capability to query records based on specific criteria.
*   **Record Update:** Ability to modify fields or merge records.
*   **Data Validation:** Logic to check for field completeness and formatting accuracy.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Comprehensive data decay and compliance-aware cleanup.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up automation.
* [Account Intelligence Gatherer](../account-intelligence-gatherer/README.md) - Enrich account records with external intelligence.
