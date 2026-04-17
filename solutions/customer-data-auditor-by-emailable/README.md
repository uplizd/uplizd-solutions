# Customer Data Auditor (Uplizd) - Automated email hygiene and database validation

## Summary
The Customer Data Auditor by Emailable is an automated AI workflow designed to maintain high-quality customer databases by identifying invalid, risky, or outdated email addresses. By integrating real-time verification directly into your data pipeline, this solution ensures your communication channels remain clean, reducing bounce rates and improving deliverability for marketing and support teams.

---

## Demo
![Customer Data Auditor workflow showing email verification process](image.png)
**Alt text (SEO-ready):** Customer Data Auditor workflow in Uplizd, featuring automated email verification, data hygiene, and Emailable integration for CRM database management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5e2e7296-6ea6-5614-b438-03d408890cd8)

---

## Category
**Data Hygiene**
*Tags:* `email verification`, `emailable`, `crm`, `data quality`, `bounce reduction`, `sales operations`, `composio`, `ai workflow`

This solution serves as a critical automated layer for maintaining clean, actionable customer contact data across your enterprise systems.

---

## Who is this for?
This solution is designed for teams managing high-volume customer communications who need to ensure data accuracy and sender reputation.

* **Marketing Operations Manager**
    * Automates the removal of invalid leads from mailing lists to protect domain reputation.
* **Sales Operations Specialist**
    * Ensures CRM contact records are verified, saving SDRs time spent on unreachable prospects.
* **Customer Support Lead**
    * Validates user-provided emails during onboarding to ensure critical account notifications are delivered.
* **Data Analyst**
    * Maintains a single source of truth for customer contact health by auditing database integrity.

---

## Features
- **Real-time Email Verification**
  Instantly validate email addresses against the Emailable API to detect syntax errors and inactive domains.
- **Automated Data Hygiene**
  Automatically flag or remove records that fail verification, preventing "data decay" in your CRM.
- **Composio-Powered CRM Integration**
  Seamlessly connect to your CRM to pull contact lists and push verification statuses back to specific fields.
- **Risk Scoring**
  Assign risk levels to contacts based on deliverability metrics to prioritize high-value outreach.
- **Customizable Thresholds**
  Configure the agent to trigger specific actions based on verification results, such as moving "risky" emails to a re-engagement list.

---

## Use Cases
**Marketing List Optimization**
* Scrubbing bulk email lists before a major campaign launch to maximize open rates.
* Automating the suppression of hard-bounce addresses from active marketing automation workflows.

**CRM Data Maintenance**
* Running periodic audits on legacy CRM records to identify and clean up stale contact information.
* Validating new lead entries in real-time as they are added to the database via web forms.

**Support & Onboarding Hygiene**
* Verifying user email addresses during the sign-up process to prevent account creation with fake or temporary emails.
* Ensuring critical transactional emails reach the intended recipient by auditing contact data before dispatch.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Customer Data Auditor" template.
2. Click "Import" to load the workflow into your workspace.
3. Authenticate your Emailable and CRM accounts within the integration settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger signal or manual request to audit specific contact lists.
* **Agent**: Processes the data, interprets verification results, and decides on the necessary cleanup action.
* **Composio Toolset**: Executes the API calls to Emailable and updates the CRM fields accordingly.
* **Chat Output**: Returns a summary report of the audit, including total records processed and identified issues.

### 3) Run the Flow
Use the Playground to test your configuration:
* `Audit all contacts in the 'New Leads' list and flag invalid emails.`
* `Check the deliverability status of the email address user@example.com.`
* `Remove all contacts from the CRM that return a 'risky' verification status.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making layer for your data hygiene strategy.
* Follow a strict logic: Verify → Analyze → Act.
* Prioritize high-confidence verification results from the Emailable API.
* Maintain a detailed log of all changes made to CRM records for audit purposes.

### 2) Composio Toolset Node
Requires a valid Emailable API key and appropriate read/write permissions for your CRM (e.g., Salesforce, HubSpot). Ensure the connection scope includes access to contact objects and custom fields.

### 3) Tool Availability
* **Emailable Verification**: Capability to check email validity, domain status, and deliverability.
* **CRM Connector**: Capability to read contact records and update field values based on audit results.
* **Reporting Utility**: Capability to generate and format audit summaries for the end user.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enriches CRM records with firmographic data.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes contact data across multiple platforms.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - General-purpose cleanup for CRM database records.
