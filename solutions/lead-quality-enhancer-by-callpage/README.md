# Lead Quality Enhancer (Uplizd) - Automate lead qualification and routing via CallPage

## Summary
The Lead Quality Enhancer (Uplizd) streamlines your sales pipeline by automating the qualification and routing of incoming leads from CallPage. By leveraging AI-driven analysis, this workflow ensures that high-intent leads are instantly assigned to the appropriate account managers, reducing response times and increasing conversion rates through improved data hygiene and pipeline velocity.

---

## Demo
![Lead Quality Enhancer workflow diagram showing CallPage integration with AI agent routing](image.png)
**Alt text (SEO-ready):** Lead Quality Enhancer workflow diagram showing CallPage integration with AI agent routing and automated CRM lead assignment for Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2bec6f19-6220-5eeb-95f7-fc6da06c0a4d)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** callpage, lead qualification, crm, sales operations, lead routing, pipeline management, composio, ai workflow.
This solution bridges the gap between real-time lead capture and CRM data integrity to ensure your sales team focuses on the most valuable opportunities.

---

## Who is this for?
This solution is designed for revenue teams looking to eliminate manual lead triage and improve response consistency.

* **Sales Operations Manager**
    * Automates lead distribution logic to ensure balanced workloads across the team.
* **Account Executive**
    * Receives pre-qualified leads directly in the CRM, allowing for faster outreach.
* **Marketing Manager**
    * Gains visibility into lead quality metrics originating from CallPage campaigns.
* **RevOps Lead**
    * Maintains a clean, synchronized database by enforcing qualification standards at the point of entry.

---

## Features
- **Real-time Lead Scoring**
  Automatically evaluates lead intent and quality as soon as they arrive from CallPage.
- **Intelligent Routing**
  Assigns leads to specific account managers based on predefined territory or industry rules.
- **CRM Data Synchronization**
  Updates lead records in your CRM instantly, ensuring the sales team has the latest context.
- **Automated Follow-up Triggers**
  Initiates personalized outreach sequences based on the lead's specific qualification score.
- **Composio Toolset Integration**
  Uses advanced toolsets to bridge CallPage data with your existing sales stack seamlessly.

---

## Use Cases
**Lead Qualification & Triage**
* Automatically filtering out low-intent leads to prioritize high-value prospects.
* Scoring leads based on custom fields captured during the CallPage interaction.

**Sales Pipeline Optimization**
* Reducing the time-to-first-response by automating the assignment process.
* Ensuring all leads are correctly tagged in the CRM for accurate pipeline reporting.

**Data Hygiene & Management**
* Standardizing lead contact information formats before they enter the CRM database.
* Detecting and merging duplicate lead entries to maintain a single source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Lead Quality Enhancer template using the provided solution link.
3. Connect your CallPage and CRM accounts within the integration settings.
4. Ensure nodes are correctly linked and all API credentials are authenticated.

### 2) Setup the Nodes
* **Chat Input**: Receives raw lead data payload from CallPage.
* **Agent**: Analyzes lead intent and determines qualification status.
* **Composio Toolset**: Executes CRM updates and routing logic based on agent analysis.
* **Chat Output**: Confirms successful routing and logs the lead status.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Qualify the latest lead from CallPage and assign it to the Enterprise Sales team.`
* `Check the current lead score for the most recent entry and update the CRM status.`
* `Summarize the last 5 incoming leads and verify if they meet the high-intent criteria.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for lead triage.
* Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
* Instruction: "Analyze the lead data, assign a score from 1-10, and map to the correct sales representative."
* Instruction: "If the lead is missing critical contact info, flag it for manual review instead of routing."

### 2) Composio Toolset Node
* Ensure your CRM API key is active within the Composio dashboard.
* Scope the connection to allow read/write access to 'Leads' and 'Contacts' objects.

### 3) Tool Availability
* **CRM Connector**: For updating lead status and owner fields.
* **CallPage API**: For fetching real-time lead metadata.
* **Data Validator**: For checking email and phone number formats.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages effectively.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean and maintain your CRM data quality.
