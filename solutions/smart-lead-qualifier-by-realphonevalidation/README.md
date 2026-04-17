# Smart Lead Qualifier (Uplizd) - Automated lead validation and contact quality scoring

## Summary
The Smart Lead Qualifier (Uplizd) is an automated AI workflow that integrates real-time phone validation to ensure your CRM data remains accurate and actionable. By leveraging the RealPhoneValidation API, this solution automatically verifies lead contact information, filters out invalid entries, and scores lead quality, significantly reducing manual data entry and improving pipeline velocity for sales and marketing teams.

---

## Demo
![Smart Lead Qualifier workflow showing Chat Input, Agent, RealPhoneValidation tool, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Smart Lead Qualifier Uplizd workflow, automated CRM lead validation, RealPhoneValidation integration, sales data hygiene, and AI-driven lead scoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/017d656b-5897-5d71-9ef5-45b44f5ffd03)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead qualification, data hygiene, realphonevalidation, sales operations, data sync, composio, ai workflow
- This solution streamlines the lead qualification process by automating the verification of contact data directly within your existing sales stack.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate bad data and prioritize high-intent prospects.

- **Sales Development Representative (SDR)**
    - Instantly identifies valid phone numbers to prioritize outreach and reduce time spent on disconnected lines.
- **RevOps Manager**
    - Maintains pristine CRM data hygiene by automatically flagging or updating invalid contact records.
- **Marketing Operations Specialist**
    - Increases campaign ROI by ensuring lead nurturing efforts are directed toward verified, reachable contacts.
- **Sales Manager**
    - Gains visibility into lead quality metrics to forecast more accurately based on verified prospect data.

---

## Features
- **Real-time Phone Validation**
    - Instantly verifies the status, carrier, and line type of phone numbers using the RealPhoneValidation API.
- **Automated Lead Scoring**
    - Assigns quality scores to leads based on contact validity, allowing agents to focus on high-probability opportunities.
- **CRM Integration**
    - Seamlessly syncs validation results back to your CRM, ensuring your single source of truth is always up-to-date.
- **Intelligent Error Handling**
    - Automatically flags invalid entries for manual review or removal, preventing data decay in your pipeline.
- **Composio-Powered Execution**
    - Utilizes the Composio Toolset to bridge the gap between AI reasoning and external validation services.

---

## Use Cases
**Lead Pipeline Optimization**
- Automatically filter out invalid phone numbers from incoming web forms before they reach the sales team.
- Update lead status in the CRM based on validation results to trigger specific follow-up sequences.

**Data Hygiene Maintenance**
- Run bulk validation checks on existing CRM databases to identify and clean up stale or incorrect contact information.
- Standardize phone number formatting across global lead lists to ensure consistent communication.

**Sales Efficiency Gains**
- Reduce "dead-end" calls by providing SDRs with a pre-verified list of reachable prospects.
- Improve lead routing logic by prioritizing contacts with verified mobile numbers over landlines or invalid entries.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Smart Lead Qualifier template from the solution library.
3. Connect your CRM and RealPhoneValidation API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead contact details and phone number for processing.
- **Agent**: Analyzes the input and triggers the validation request.
- **Composio Toolset**: Executes the phone validation lookup via the RealPhoneValidation API.
- **Chat Output**: Returns the validation status and quality score to the user or CRM.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Validate the phone number +1-555-0199 for lead ID 8842.`
- `Check the contact quality for the list of leads provided in the attached CSV.`
- `Verify if the phone number for John Doe is a valid mobile line.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for data verification.
- **Recommended instruction pattern:**
    - "You are a lead qualification assistant. Your goal is to verify contact data accuracy."
    - "Always use the RealPhoneValidation tool to check the status of provided phone numbers."
    - "Summarize the validation results clearly, highlighting any invalid numbers for immediate action."

### 2) Composio Toolset Node
- **API Key**: Ensure your RealPhoneValidation API key is securely stored in the Composio configuration.
- **Connection Scope**: Grant the toolset read/write access to your CRM to allow for automated field updates.

### 3) Tool Availability
- **Phone Validator**: Performs real-time lookup of phone number status.
- **CRM Connector**: Updates lead records with validation metadata.
- **Data Formatter**: Ensures phone numbers are normalized to E.164 format before validation.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with verified contact details.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automate bulk data cleanup and formatting.
- [WhatsApp Lead Qualifier](../whats-app-lead-qualifier-by-wati/README.md) — Qualify leads directly through WhatsApp messaging.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Track and score sales opportunities for better pipeline management.
