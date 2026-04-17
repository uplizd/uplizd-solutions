# Proposal Housekeeping Agent (Uplizd) - Automate proposal lifecycle management and data hygiene

## Summary
The Proposal Housekeeping Agent is an intelligent Uplizd workflow designed to automate the maintenance of client proposals within Bidsketch. By identifying stale documents, archiving outdated records, and ensuring consistent status tracking, this solution eliminates manual administrative overhead, improves pipeline hygiene, and provides a single source of truth for your sales documentation.

---

## Demo
![Proposal Housekeeping Agent workflow interface showing Bidsketch integration nodes](image.png)
**Alt text (SEO-ready):** Uplizd Proposal Housekeeping Agent workflow for Bidsketch, featuring automated proposal cleanup, status synchronization, and data hygiene management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d3b7887f-e59d-59b4-b78f-328cb9ccced7)

---

## Category
**Primary category:** Sales operations
**Secondary tags:** bidsketch, proposal management, data hygiene, sales automation, workflow automation, document tracking, composio, ai workflow

This solution streamlines sales operations by automating the routine maintenance of proposal data, ensuring your CRM and document platforms remain accurate and clutter-free.

---

## Who is this for?
This agent is designed for teams looking to reclaim hours spent on manual document management and improve the accuracy of their sales reporting.

*   **Sales Operations Manager**
    *   Maintains high-quality data hygiene across the entire proposal lifecycle without manual intervention.
*   **Account Executive**
    *   Reduces time spent on administrative cleanup, allowing more focus on closing active opportunities.
*   **Sales Enablement Lead**
    *   Ensures that proposal templates and client records are consistently archived and organized.
*   **Revenue Operations (RevOps) Analyst**
    *   Improves the reliability of pipeline reporting by removing stalled or obsolete proposal data.

---

## Features
- **Automated Stale Proposal Detection**
    - Identifies proposals that have remained in a specific status for too long using real-time Bidsketch data.
- **Intelligent Archiving Logic**
    - Automatically moves outdated or rejected proposals to archive folders to keep the active workspace clean.
- **Status Synchronization**
    - Updates proposal statuses across connected platforms to ensure alignment between Bidsketch and your CRM.
- **Customizable Cleanup Rules**
    - Allows users to define specific time windows and status triggers for automated housekeeping actions.
- **Composio-Powered Execution**
    - Leverages the Composio Toolset to securely interact with Bidsketch APIs for reliable, authenticated document operations.

---

## Use Cases
**Pipeline Hygiene**
*   Automatically archive proposals that have been in "Sent" status for more than 60 days without a response.
*   Flag proposals that have reached a "Draft" limit to prevent workspace clutter.

**Sales Administration**
*   Bulk update proposal statuses based on client feedback received via email or CRM triggers.
*   Generate weekly reports of archived documents to maintain an audit trail for management.

**Data Integrity**
*   Sync proposal metadata with CRM fields to ensure accurate reporting on conversion rates.
*   Clean up duplicate proposal entries created during the sales cycle to maintain a single source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Connect your Bidsketch account within the Composio Toolset node.
4. Ensure nodes are correctly mapped and all API credentials are saved before triggering the first run.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or manual request to initiate the housekeeping cycle.
*   **Agent**: Processes the logic to evaluate proposal dates and statuses against your defined cleanup rules.
*   **Composio Toolset**: Executes the API calls to Bidsketch to fetch, update, or archive proposals.
*   **Chat Output**: Returns a summary report of all proposals processed, archived, or updated during the run.

### 3) Run the Flow
Use the Uplizd Playground to test your agent with the following prompts:
* `Run the housekeeping agent to archive all proposals sent over 90 days ago.`
* `Check for draft proposals older than 30 days and provide a summary list.`
* `Sync all Bidsketch proposal statuses with my current CRM records.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your document lifecycle.
*   Instruction: "Analyze the list of proposals retrieved from Bidsketch and identify those meeting the 'stale' criteria."
*   Instruction: "Execute the archiving action only for proposals that have not been modified in the last 60 days."
*   Instruction: "Format the final output as a clear table showing the proposal name, original status, and action taken."

### 2) Composio Toolset Node
*   **API Key**: Ensure your Bidsketch API key is active and stored in your Uplizd environment variables.
*   **Connection Scope**: Grant the agent read/write permissions for proposal management and status updates.

### 3) Tool Availability
*   `bidsketch_list_proposals`: Retrieve current proposal data.
*   `bidsketch_update_proposal`: Modify status or move to archive.
*   `bidsketch_get_proposal_details`: Fetch specific metadata for decision-making.

---

## Related Solutions
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automate new client onboarding and CRM record creation.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Maintain organized task lists and resolve stale action items.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Comprehensive tools for cleaning and formatting CRM contact data.
