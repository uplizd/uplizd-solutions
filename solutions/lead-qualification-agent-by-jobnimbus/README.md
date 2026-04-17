# Lead Qualification Agent (Uplizd) - Automate lead scoring and routing for JobNimbus

## Summary
The Lead Qualification Agent by Uplizd streamlines your sales pipeline by automatically evaluating incoming leads against your specific project criteria. By integrating directly with JobNimbus, this AI workflow ensures that high-intent prospects are prioritized and routed to the correct team members, eliminating manual data entry and reducing response times for your sales organization.

---

## Demo
![Lead Qualification Agent workflow diagram showing Chat Input, Agent, JobNimbus integration, and Chat Output](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow for JobNimbus, automating sales pipeline management, lead scoring, and CRM routing via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-12683c65--af45--509a--9031--2da8ab082b2e-blue)](https://uplizd.ai/solutions/12683c65-af45-509a-9031-2da8ab082b2e)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** `crm`, `jobnimbus`, `lead qualification`, `sales pipeline`, `automation`, `composio`, `ai workflow`

This solution bridges the gap between raw lead intake and actionable CRM data, ensuring your sales team focuses only on qualified opportunities.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to scale their lead intake process without increasing headcount.

* **Sales Managers**
    * Maintain consistent qualification standards across the entire team.
* **BDRs/SDRs**
    * Eliminate time spent on manual lead research and initial data entry.
* **RevOps Specialists**
    * Ensure pipeline hygiene by enforcing strict data requirements for new opportunities.
* **JobNimbus Administrators**
    * Automate the routing of leads to specific project owners based on territory or service type.

---

## Features
- **Automated Lead Scoring**
    Instantly evaluate incoming leads based on project size, location, and service requirements.
- **JobNimbus CRM Integration**
    Seamlessly create or update records in JobNimbus using the Composio Toolset.
- **Intelligent Routing**
    Automatically assign qualified leads to the appropriate sales representative or project manager.
- **Real-time Data Validation**
    Verify lead contact information and project details before pushing data into your CRM.
- **Customizable Qualification Logic**
    Easily adjust the agent's instructions to match your evolving business criteria and sales thresholds.

---

## Use Cases
**Pipeline Acceleration**
* Automatically move qualified leads from "New" to "Discovery" status in JobNimbus.
* Trigger immediate follow-up notifications for high-priority leads identified by the agent.

**Data Hygiene & Accuracy**
* Standardize lead formatting and project descriptions before they enter the CRM database.
* Remove duplicate entries by checking existing JobNimbus records during the qualification process.

**Sales Efficiency**
* Filter out unqualified prospects based on budget or project scope, saving your team valuable time.
* Summarize lead requirements into a concise note for the assigned sales representative.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Agent template using the solution ID.
3. Connect your JobNimbus account via the Composio integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives raw lead data or inquiry text from your website or email.
* **Agent:** Analyzes the input against your qualification criteria and decides on the next action.
* **Composio Toolset:** Executes the necessary API calls to create or update records in JobNimbus.
* **Chat Output:** Confirms the lead status and provides a summary of the action taken.

### 3) Run the Flow
Use the Playground to test your agent with various lead scenarios:
* `Qualify this lead: John Doe, interested in a roof replacement, budget $15k, located in Austin.`
* `Check if this lead meets our minimum project size requirements for a full kitchen remodel.`
* `Route this inquiry to the residential sales team and update the lead status in JobNimbus.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your digital sales assistant, responsible for interpreting lead intent and enforcing business rules.
* **Instruction Pattern:**
    * Define the specific criteria that constitute a "qualified" lead for your business.
    * Instruct the agent to extract key entities (Name, Budget, Project Type) from the input.
    * Set the tone for the confirmation message returned to the user or internal team.

### 2) Composio Toolset Node
* **API Key:** Provide your JobNimbus API credentials within the Composio connection manager.
* **Connection Scope:** Ensure the agent has "Write" permissions for Leads and Projects to enable full automation.

### 3) Tool Availability
* **Lead Creation:** Ability to generate new records in JobNimbus.
* **Data Lookup:** Ability to query existing records to prevent duplicates.
* **Status Update:** Ability to transition lead stages based on qualification results.

---

## Related Solutions
* [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) — Automate general business processes and task management.
* [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) — Streamline new account creation and onboarding workflows.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and contact data across multiple platforms.
