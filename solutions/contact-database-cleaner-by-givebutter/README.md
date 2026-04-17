# Contact Database Cleaner (Uplizd) - Automated donor data hygiene and contact management

## Summary
The Contact Database Cleaner by Givebutter is an intelligent Uplizd AI workflow designed to maintain high-quality donor and contact records. By automating the identification of duplicates, formatting inconsistencies, and outdated information, this solution ensures your CRM remains a single source of truth, significantly improving pipeline velocity and data hygiene for non-profits and fundraising teams.

---

## Demo
![Contact Database Cleaner workflow interface showing automated data scrubbing and Givebutter integration nodes](image.png)
**Alt text (SEO-ready):** Contact Database Cleaner Uplizd workflow, automated CRM data hygiene, Givebutter donor management, AI-powered contact deduplication.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ed58deb0-b163-5e0e-8e46-7aeacf73c4be)

---

## Category
**Primary category:** Data integration
**Secondary tags:** crm, givebutter, data hygiene, contact management, donor database, ai workflow, composio, data sync.
This solution bridges the gap between raw donor input and clean, actionable CRM data through automated validation and cleanup routines.

---

## Who is this for?
This solution is built for teams managing high-volume donor relationships who need to maintain pristine records without manual intervention.

- **Development Director**
    - Ensures donor outreach is based on accurate, deduplicated contact information.
- **Database Administrator**
    - Reduces the manual burden of cleaning records and fixing formatting errors.
- **Fundraising Operations Manager**
    - Maintains high data integrity for segmented marketing and donor retention campaigns.
- **Non-profit Program Coordinator**
    - Automates the verification of contact details to prevent communication bounce-backs.

---

## Features
- **Automated Deduplication**
    - Detects and merges duplicate contact profiles based on email, phone, or name patterns.
- **Real-time Data Formatting**
    - Standardizes address, phone number, and name casing across the entire Givebutter database.
- **Intelligent Validation**
    - Uses AI to flag incomplete or suspicious contact entries for manual review or automated enrichment.
- **Composio-Powered CRM Sync**
    - Leverages the Composio Toolset to execute secure, authenticated updates directly within your Givebutter environment.
- **Customizable Cleanup Rules**
    - Allows users to define specific logic for what constitutes "dirty" data, ensuring compliance with internal standards.

---

## Use Cases
**Donor Data Maintenance**
- Automatically flagging and merging duplicate donor profiles created during high-traffic fundraising events.
- Standardizing donor contact fields to ensure consistent reporting and segmentation.

**Communication Hygiene**
- Identifying and removing invalid email addresses or malformed phone numbers before launching mass outreach.
- Updating donor records with missing information by cross-referencing recent engagement data.

**Compliance and Reporting**
- Ensuring all donor records meet internal data quality standards for annual audit readiness.
- Cleaning up legacy data imports to improve the accuracy of donor lifetime value calculations.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Contact Database Cleaner solution.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Givebutter account via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or manual request to initiate a database scan.
*   **Agent**: Processes the data using LLM instructions to identify inconsistencies and duplicates.
*   **Composio Toolset**: Executes the API calls to read, update, or delete records in Givebutter.
*   **Chat Output**: Returns a summary report of all changes made to the contact database.

### 3) Run the Flow
Access the Playground to test the agent's cleanup capabilities:
- `Clean all duplicate contacts in my Givebutter database.`
- `Standardize the address formatting for all donors added in the last 30 days.`
- `Identify and flag any donor records missing phone numbers or email addresses.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for data evaluation.
- Instruct the agent to prioritize data accuracy and record integrity.
- Define specific thresholds for what constitutes a "duplicate" (e.g., matching email vs. matching name/address).
- Configure the agent to provide a detailed log of all actions taken during the cleanup process.

### 2) Composio Toolset Node
- Provide your Givebutter API key within the Composio connection settings.
- Ensure the connection scope includes read/write permissions for Contacts and Donor profiles.

### 3) Tool Availability
- **Contact Search**: Locate existing records by name or email.
- **Record Update**: Modify fields to correct formatting or merge data.
- **Bulk Delete**: Remove confirmed duplicate or junk entries.
- **Data Validation**: Verify the structure of contact fields against standard formats.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automates financial record matching and reconciliation.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — General-purpose toolkit for maintaining CRM data quality.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enriches contact records with verified professional data.
