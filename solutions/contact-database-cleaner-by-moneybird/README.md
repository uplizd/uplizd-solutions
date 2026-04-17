# Contact Database Cleaner (Uplizd) - Automated CRM hygiene and contact list optimization

## Summary
The Contact Database Cleaner (Uplizd) is an intelligent automation workflow designed to maintain pristine CRM data by identifying, flagging, and cleaning inactive or duplicate records. By leveraging the Composio Toolset to interface with Moneybird and other CRM platforms, this solution helps RevOps and sales teams reduce data decay, improve pipeline accuracy, and ensure that outreach efforts are focused on high-quality, verified contacts.

---

## Demo
![Contact Database Cleaner workflow showing data ingestion, validation, and cleanup nodes](image.png)
**Alt text (SEO-ready):** Contact Database Cleaner workflow for Uplizd, automating CRM data hygiene, contact list deduplication, and record maintenance via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c99fccdd-31c5-5755-9d4a-aa374cf4df09)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** crm, moneybird, data sync, contact management, automation, composio, ai workflow, data quality
- This solution bridges the gap between raw contact storage and actionable data by automating the identification of stale or redundant entries.

---

## Who is this for?
This solution is designed for teams managing high-volume contact databases who need to maintain data integrity without manual intervention.

- **Sales Operations Manager**
    - Automates the removal of stale leads to keep CRM storage costs low and focus metrics accurate.
- **CRM Administrator**
    - Ensures consistent data formatting and prevents duplicate record creation across integrated platforms.
- **Growth Marketer**
    - Increases email deliverability and campaign performance by ensuring outreach lists are clean and up-to-date.
- **Account Executive**
    - Spends less time manually verifying contact details and more time engaging with active, qualified prospects.

---

## Features
- **Automated Data Scanning**
    - Continuously monitors your contact database for outdated records or missing information fields.
- **Intelligent Deduplication**
    - Uses AI to identify and merge duplicate contacts based on email addresses, names, and company identifiers.
- **Composio-Powered Integration**
    - Seamlessly connects with Moneybird and other CRM tools to perform real-time read/write operations.
- **Customizable Cleanup Rules**
    - Allows users to define specific criteria for what constitutes an "inactive" contact, such as last interaction date.
- **Audit Logging**
    - Provides a clear trail of all modifications made to the database for compliance and reporting purposes.

---

## Use Cases
**Database Maintenance**
- Automatically flag contacts that have not had an interaction in over 180 days.
- Bulk-archive contacts that have opted out or are marked as invalid in the CRM.

**Data Standardization**
- Normalize phone number formats and address fields across the entire contact database.
- Identify and merge duplicate entries created by multiple lead sources or manual imports.

**Pipeline Hygiene**
- Remove test accounts or dummy contacts from active sales lists to prevent skewed reporting.
- Sync updated contact statuses back to Moneybird to ensure cross-platform data consistency.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Contact Database Cleaner template from the solution library.
3. Authenticate your Moneybird and CRM credentials within the Composio connection manager.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or schedule signal to begin the cleanup process.
- **Agent**: Processes the logic to evaluate contact records against your defined hygiene rules.
- **Composio Toolset**: Executes the API calls to fetch, update, or delete records in Moneybird.
- **Chat Output**: Returns a summary report of the cleanup actions performed during the run.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Scan all contacts in Moneybird and flag those inactive for more than 6 months.`
- `Identify and merge duplicate contact records based on email address.`
- `Run a full database cleanup and provide a summary of removed records.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for your data hygiene policy.
- Use a model capable of high-precision reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a data hygiene expert. Analyze contact records provided by the toolset and apply cleanup rules strictly."
- Instruction: "If a record is ambiguous, flag it for manual review rather than deleting it."

### 2) Composio Toolset Node
- Provide your unique API key to enable secure communication with your CRM.
- Set the connection scope to allow read/write access to contacts and account objects.

### 3) Tool Availability
- **List Contacts**: Retrieve current database state.
- **Update Contact**: Modify fields or status flags.
- **Delete/Archive Record**: Remove stale data based on logic.
- **Search Records**: Locate duplicates or specific contact patterns.

---

## Related Solutions
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Comprehensive tools for maintaining overall CRM data health.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize contact data across multiple platforms and tools.
- [Account Research Assistant](../account-research-assistant/README.md) - Enrich contact profiles with external intelligence.
