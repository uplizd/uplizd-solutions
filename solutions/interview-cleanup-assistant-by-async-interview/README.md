# Interview Cleanup Assistant (Uplizd) - Automated recruitment data hygiene and pipeline maintenance

## Summary
The Interview Cleanup Assistant is an intelligent Uplizd workflow designed to automate the maintenance of your recruitment database. By leveraging AI to identify stale, duplicate, or incomplete candidate records, this solution ensures your hiring pipeline remains accurate and actionable, significantly reducing manual data entry and improving recruiter productivity.

---

## Demo
![Interview Cleanup Assistant dashboard showing automated candidate record deduplication and status updates](image.png)
**Alt text (SEO-ready):** Interview Cleanup Assistant dashboard showing automated candidate record deduplication, recruitment data hygiene, and Uplizd workflow integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/3d6dcb00-af2e-5380-9abe-b978ef2a4529)

---

## Category
**Primary category:** Recruiting operations
**Secondary tags:** crm, recruitment, data hygiene, candidate management, pipeline, ai workflow, composio, automation.
This solution streamlines recruitment operations by ensuring candidate data integrity through automated cleanup and synchronization.

---

## Who is this for?
This solution is built for talent acquisition teams and HR departments looking to eliminate manual data maintenance.

*   **Recruiting Managers**
    *   Maintain high-quality candidate pipelines with automated data validation and deduplication.
*   **HR Operations Specialists**
    *   Reduce administrative overhead by automating the cleanup of legacy candidate records.
*   **Talent Acquisition Leads**
    *   Ensure accurate reporting metrics by maintaining a single source of truth for all interview stages.
*   **Technical Recruiters**
    *   Focus on candidate engagement rather than manual database updates and record reconciliation.

---

## Features
- **Automated Deduplication**
    Detects and merges duplicate candidate profiles across your ATS or CRM to prevent fragmented hiring histories.
- **Data Hygiene Enforcement**
    Automatically flags and corrects incomplete candidate records, ensuring all mandatory fields are populated correctly.
- **Stale Record Archiving**
    Identifies candidates who have been inactive for extended periods and moves them to appropriate archive stages.
- **Real-time Sync**
    Utilizes the Composio Toolset to push updates directly to your integrated CRM, ensuring instant visibility across the team.
- **Intelligent Formatting**
    Standardizes contact information and interview notes, providing a consistent and professional look for all candidate data.

---

## Use Cases
**Candidate Data Maintenance**
*   Automatically identifying and merging duplicate profiles created by multiple recruiter entries.
*   Standardizing phone number and email formatting across the entire candidate database.

**Pipeline Optimization**
*   Moving candidates who have not progressed in over 30 days to a "Nurture" or "Archived" status.
*   Flagging incomplete interview feedback forms to ensure recruiters provide necessary documentation.

**Compliance & Reporting**
*   Ensuring all candidate records contain required GDPR or EEO data fields before moving to the offer stage.
*   Generating clean data sets for monthly hiring velocity and source-of-hire reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in the Uplizd builder.
2. Connect your preferred CRM or ATS via the Composio Toolset node.
3. Configure your API credentials to allow the agent read/write access to candidate records.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives manual triggers or scheduled cleanup requests from the user.
*   **Agent**: Processes natural language instructions to identify and clean target candidate records.
*   **Composio Toolset**: Executes precise API calls to update, merge, or archive records in your CRM.
*   **Chat Output**: Delivers a summary report of all actions taken during the cleanup process.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
* `Find all duplicate candidate records created in the last 30 days and merge them.`
* `Identify candidates with missing contact information and flag them for review.`
* `Archive all candidates who have been in the 'Initial Screening' stage for more than 60 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data steward, interpreting cleanup rules and executing them via tools.
*   Prioritize data integrity and strict adherence to defined record-merging logic.
*   Maintain a neutral, professional tone when reporting cleanup results to the user.
*   Always verify record IDs before performing destructive actions like merging or deleting.

### 2) Composio Toolset Node
Requires an active API key for your CRM (e.g., Salesforce, Greenhouse, or Lever). Ensure the connection scope includes `read` and `write` permissions for candidate and contact objects.

### 3) Tool Availability
*   **Search/Fetch**: Retrieve candidate lists based on specific status or date filters.
*   **Update/Patch**: Modify candidate fields to correct formatting or status.
*   **Merge**: Combine duplicate records into a primary profile.
*   **Archive/Delete**: Safely transition stale records to inactive states.

---

## Related Solutions
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates the configuration of new accounts in your CRM.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - General-purpose data cleanup for broader CRM environments.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages sales pipeline stages and stalled deal follow-ups.
