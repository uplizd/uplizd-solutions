# Lead Capture Agent (Uplizd) - Automated email parsing and lead enrichment

## Summary
The Lead Capture Agent by Parseur is an intelligent workflow designed to automate the extraction of lead data from incoming emails and contact forms. By leveraging the Composio Toolset, this solution transforms unstructured inquiry data into structured records, ensuring your sales pipeline is populated instantly and accurately without manual entry.

---

## Demo
![Lead Capture Agent workflow diagram showing email parsing, data extraction, and CRM synchronization](image.png)
**Alt text (SEO-ready):** Lead Capture Agent workflow diagram showing email parsing, data extraction, and CRM synchronization via Uplizd and Parseur.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/804feca1-d863-5aab-b72b-8926f50f58d2)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** lead generation, parseur, crm, data extraction, email automation, sales pipeline, lead qualification, composio

This solution bridges the gap between raw inbound communication and actionable CRM data, streamlining the lead lifecycle.

---

## Who is this for?
This agent is built for revenue-focused teams looking to eliminate manual data entry and accelerate response times.

* **Sales Development Representative (SDR)**
    * Reduces time spent manually copying lead details from email notifications into the CRM.
* **Marketing Operations Manager**
    * Ensures that every lead generated from web forms is captured and attributed correctly in the database.
* **Revenue Operations (RevOps) Lead**
    * Maintains high data hygiene by standardizing lead information before it hits the sales pipeline.
* **Small Business Owner**
    * Automates the initial lead intake process, allowing for faster follow-up and improved conversion rates.

---

## Features
- **Automated Email Parsing**
    Extracts key fields like name, email, phone number, and intent directly from incoming lead notifications.
- **Intelligent Data Enrichment**
    Uses the Composio Toolset to cross-reference extracted data with external databases for complete lead profiles.
- **Real-time CRM Sync**
    Pushes standardized lead objects into your preferred CRM platform immediately upon extraction.
- **Customizable Logic**
    Allows for conditional routing based on lead score, source, or specific inquiry keywords.
- **Error Handling & Logging**
    Provides visibility into parsing failures, ensuring no lead is lost due to unexpected email formatting.

---

## Use Cases
**Inbound Lead Management**
* Automating the creation of new lead records from website "Contact Us" email notifications.
* Routing high-intent leads to specific account managers based on extracted company size or industry.

**Data Hygiene & Enrichment**
* Standardizing phone number formats and address fields before syncing to the CRM.
* Appending missing company information to leads captured via simplified contact forms.

**Sales Pipeline Velocity**
* Triggering automated welcome email sequences the moment a lead is parsed and saved.
* Updating existing lead records with new inquiry details to maintain a single source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Lead Capture Agent.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Parseur account and CRM instance via the integration settings.
4. Ensure nodes are correctly mapped and all API credentials are authenticated.

### 2) Setup the Nodes
* **Chat Input**: Receives raw email content or form submission payloads.
* **Agent**: Analyzes the text and extracts structured lead entities.
* **Composio Toolset**: Executes the API calls to format and push data to your CRM.
* **Chat Output**: Confirms successful lead creation or logs parsing errors.

### 3) Run the Flow
Use the Playground to test the agent with sample data:
- `Extract lead details from this email: "Hi, I'm John Doe from Acme Corp, interested in your enterprise plan. Reach me at 555-0199."`
- `Parse this inquiry and update the CRM lead status to 'New Lead'.`
- `Identify the company domain from this email body and enrich the lead record.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data extraction specialist, focusing on accuracy and field mapping.
* Instruction: "Extract name, email, company, and intent from the input text."
* Instruction: "Normalize all phone numbers to E.164 format."
* Instruction: "If a field is missing, flag the lead for manual review rather than guessing."

### 2) Composio Toolset Node
Requires an active API key for your CRM (e.g., Salesforce, HubSpot) and the Parseur integration. Ensure the scope includes read/write access to lead and contact objects.

### 3) Tool Availability
* **Parseur API**: For parsing email templates and raw text.
* **CRM Connector**: For creating, updating, and searching lead records.
* **Data Enrichment Tool**: For verifying email validity and company details.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich lead profiles with deep company data.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistency across multiple CRM platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage lead progression through your sales stages.
