# Contact Database Optimizer (Uplizd) - Automated CRM hygiene and enrichment for Brevo

## Summary
The Contact Database Optimizer by Uplizd is an intelligent AI workflow designed to maintain high-quality contact records within your Brevo ecosystem. By automating the identification of stale data, correcting formatting inconsistencies, and enriching missing fields, this solution ensures your marketing campaigns reach the right audience with accuracy, ultimately boosting deliverability and pipeline velocity.

---

## Demo
![Contact Database Optimizer workflow showing data flow from Brevo to the AI agent for cleaning and enrichment](image.png)
**Alt text (SEO-ready):** Contact Database Optimizer workflow for Brevo, featuring Uplizd AI-driven data hygiene, CRM contact enrichment, and automated record synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7b6e3c3f-95c3-5868-8694-d5bca742c7c7)

---

## Category
**Primary category:** CRM data hygiene
**Secondary tags:** brevo, crm, data enrichment, data cleaning, marketing operations, pipeline, composio, ai workflow

This solution bridges the gap between raw contact lists and actionable marketing data by leveraging intelligent automation to maintain a pristine CRM environment.

---

## Who is this for?
This workflow is designed for teams looking to eliminate manual data entry and improve the reliability of their customer communications.

*   **Marketing Operations Manager**
    *   Ensures that email lists are free of duplicates and formatting errors to maximize campaign ROI.
*   **CRM Administrator**
    *   Maintains data integrity across the Brevo database by automating routine cleanup tasks.
*   **Sales Development Representative**
    *   Receives enriched, verified contact profiles that allow for more personalized outreach.
*   **Growth Lead**
    *   Reduces bounce rates and improves sender reputation through consistent, automated data validation.

---

## Features
- **Automated Data Sanitization**
    Standardizes contact fields like phone numbers, job titles, and company names to ensure consistent formatting across your database.
- **Intelligent Enrichment**
    Uses the Composio Toolset to fetch missing professional details, turning sparse contact entries into comprehensive profiles.
- **Duplicate Detection**
    Identifies and flags redundant records within Brevo, providing a clear path to merging or archiving outdated entries.
- **Real-time Syncing**
    Updates your Brevo CRM in real-time, ensuring that your marketing automation tools always have access to the latest, most accurate data.
- **Compliance-Aware Cleanup**
    Applies logic to filter out inactive or non-compliant contacts, helping your organization maintain high deliverability standards.

---

## Use Cases
**Data Hygiene and Maintenance**
*   Automatically formatting phone numbers and email addresses to match global standards.
*   Identifying and merging duplicate contact records created during multi-channel lead generation.

**Lead Enrichment and Qualification**
*   Automatically appending missing industry and company size data to new leads in Brevo.
*   Updating contact job titles to reflect recent career changes for better segmentation.

**Campaign Performance Optimization**
*   Cleaning lists prior to major email blasts to reduce bounce rates and improve engagement.
*   Segmenting contacts based on the completeness of their profile data for targeted re-engagement.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Brevo account via the Integrations menu.
3. Configure the trigger settings to define which contact lists should be monitored.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual request to audit specific contact records.
*   **Agent**: Processes the data, applies cleaning logic, and determines which enrichment tools to invoke.
*   **Composio Toolset**: Executes API calls to Brevo to fetch, update, or delete contact records.
*   **Chat Output**: Confirms the completion of the cleanup process and summarizes the changes made.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Audit the 'New Leads' list in Brevo and format all phone numbers to E.164 standard.`
* `Find and merge duplicate contacts in the 'Newsletter' list based on email address.`
* `Enrich all contacts in the 'Q3 Prospects' list with missing company industry information.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data steward, interpreting CRM records and applying business rules.
*   Focus on identifying patterns of data decay.
*   Prioritize accuracy when merging records to prevent data loss.
*   Maintain a neutral, professional tone when reporting audit results.

### 2) Composio Toolset Node
Requires a valid Brevo API key with read/write permissions for the Contacts and Lists modules. Ensure the connection scope includes `contacts.read`, `contacts.write`, and `lists.read`.

### 3) Tool Availability
*   **Brevo Contact Search**: Locate specific records by email or ID.
*   **Brevo Update Contact**: Apply standardized formatting and enriched data.
*   **Brevo List Management**: Move or remove contacts based on hygiene criteria.

---

## Related Solutions
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) — Monitor and maintain account health standards within Brevo.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize contact data across multiple CRM platforms.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Comprehensive data cleanup and decay prevention for CRM systems.
