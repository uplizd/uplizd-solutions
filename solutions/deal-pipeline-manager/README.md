
# Deal Pipeline Manager (Uplizd) - Automatically Update Progress & Follow-ups

## Summary
A Uplizd AI workflow that monitors deal stages, updates progress, and automatically creates follow-up tasks to ensure your sales pipeline never stalls.

---

## Demo

![Uplizd Deal Pipeline Manager flow monitoring deal stages and creating follow-up tasks automatically](../image.png)

**Alt text (SEO-ready):** Uplizd Deal Pipeline Manager integrating CRM toolsets to automate deal stage progress and follow-up task creation.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0b7bdce2-561f-5bff-8c70-562b1b0ed531)

---
## Category

- **Primary:** Sales pipeline automation
- **Tags:** `crm`, `sales`, `pipeline`, `deal stages`, `follow-ups`, `salesforce`, `hubspot`, `pipedrive`, `composio`, `uplizd`, `revops`, `sales operations`
- Keeps deal progression and follow-up tasks aligned so revenue teams sell more and manually update CRM less.

---
## Who is this for?
This workflow is built for sales teams who want to maintain an active, accurate pipeline without the manual overhead:

- Sales Managers (SalesOps)
    - Maintain a bird's-eye view of all deals and ensure they move through the pipeline smoothly.

- Account Executives (AEs)
    - Automate the tedious task of updating deal stages and setting reminders for follow-ups.

- CRM Administrators
    - Standardize deal progression logic and task creation across the entire sales organization.

- Startup Founders
    - Focus on closing deals rather than managing pipeline hygiene manually.

---

## Features

- **Automated Stage Progression**  
  Intelligently updates deal stages based on activity and predefined triggers.

- **Smart Follow-up Creation**  
  Automatically generates tasks for the next best action, ensuring no deal "goes cold."

- **Pipeline Monitoring**  
  Continuously watches for stalled deals and flags them for immediate attention.

- **CRM Integration via Composio**  
  Seamlessly connects with your CRM (Salesforce, HubSpot, Pipedrive) to sync deal data.

- **Modular Uplizd Architecture**  
  Easily customize deal stages, task priorities, and notification settings.

---

## Use Cases

- **Move Deals Forward Automatically**
  - Update status from "Discovery" to "Proposal Sent" when a document is delivered.
  - Flag deals that haven't had activity in 48 hours.

- **Standardize Follow-up Tasks**
  - Create a "Send Thank You" task immediately after a demo is logged.
  - Schedule a "Check-in" task 3 days after a proposal is sent.

- **Deal Value Monitoring**
  - Alert managers when high-value deals enter critical stages.
  - Automatically calculate expected close dates based on historical velocity.

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all nodes are connected correctly:
   - **Chat Input**
   - **Composio Toolset**
   - **Agent**
   - **Chat Output**

### 2) Setup the Nodes
Verify the workflow structure:

- **Chat Input** → sends deal-related requests into the system.
- **Agent** → interprets the pipeline status and decides on updates/task creation.
- **Composio Toolset** → provides callable tools for CRM deal and task management.
- **Chat Output** → displays confirmation of updates and new tasks.

### 3) Run the Flow
1. Click **Playground** to open Chat Interface.
2. Enter a request such as:
   - `"Update deal [Deal Name] to Negotiation stage"`
   - `"What are my next actions for the [Client Name] deal?"`
   - `"Identify any stalled deals in my pipeline"`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is configured to act as a sales operations assistant focused on pipeline velocity.

Recommended instruction pattern:
- Focus on deal progression
- Prioritize high-value follow-ups
- Maintain consistent CRM data standards

### 2) Composio Toolset Node
Requires your **Composio API Key** and a connection to your CRM of choice.

### 3) Tool Availability
The agent can call tools for:
- Deal stage updates
- Task/Activity creation
- Contact and Company lookup
- Pipeline reporting

---

## Related Solutions

* **[CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md)**  
  Continuous maintenance to ensure your CRM stays clean, organized, and free of data rot.

* **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.

* **[Deal Opportunity Tracker](../deal-oppotunity-tracker/README.md)**  
  Identify and track new sales opportunities in real time from your data streams.

* **[CRM Address Data Cleanup Agent](../crm-address-data-cleanup-agent/README.md)**  
  Specialized verification and standardization of physical address and location data.
