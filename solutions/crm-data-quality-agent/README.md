# CRM Data Quality Agent (Uplizd) - Automate CRM Data Validation, Enrichment, and Hygiene

## Summary
The CRM Data Quality Agent is a specialized Uplizd AI workflow that automates the validation, standardization, and enrichment of customer records. By leveraging the Composio Toolset, it enables teams to maintain a single source of truth, eliminate manual data entry errors, and ensure high-quality pipeline hygiene across CRM platforms like Salesforce and HubSpot.

---

## Demo

![Uplizd CRM Data Quality Agent workflow showing Chat Input, Agent node, Composio Toolset, and Chat Output](image.png)

**Alt text (SEO-ready):** Uplizd CRM Data Quality Agent workflow integrating Composio toolset for automated CRM data validation, cleaning, and record enrichment.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/RUN%20ON%20UPLIZD-blue?style=for-the-badge&logo=lightning)](https://uplizd.ai/solutions/crm-data-quality-agent/)

---

## Category

**Primary category:** CRM data hygiene

**Secondary tags:** crm, salesforce, hubspot, data validation, data enrichment, pipeline hygiene, composio, ai workflow

This solution bridges the gap between raw customer input and structured CRM records by automating the cleaning and verification process.

---

## Who is this for?

This workflow is designed for teams managing high-volume lead and customer data who need to maintain pristine database integrity:

- **Sales Operations (SalesOps)**
    - Ensure sales reps spend time on validated leads rather than fixing formatting errors or duplicate entries.
- **Marketing Managers**
    - Improve campaign deliverability and segmentation accuracy by standardizing contact information at the point of entry.
- **CRM Administrators**
    - Reduce the burden of manual data cleanup tasks and enforce consistent data entry standards across the organization.
- **RevOps Professionals**
    - Maintain a reliable "Single Source of Truth" to drive accurate forecasting and reporting across the revenue funnel.

---

## Features

- **Intelligent Data Validation**
    - Automatically checks email formats, phone number lengths, and required fields against CRM schemas.
- **Automated Record Standardization**
    - Normalizes company names, job titles, and location data to ensure consistent reporting and searchability.
- **Composio-Powered Tool Execution**
    - Seamlessly triggers CRM API actions to update, fetch, or verify records in real-time.
- **Deduplication Logic**
    - Identifies and flags potential duplicate records based on fuzzy matching of email, name, or domain.
- **Flexible Agentic Routing**
    - Uses an LLM agent to interpret user intent and decide whether to enrich, validate, or update a specific record.

---

## Use Cases

**Data Hygiene & Cleanup**
- Bulk-standardize state and country fields to match ISO formats.
- Remove redundant whitespace and fix casing issues in contact names.

**Lead Validation & Enrichment**
- Verify email deliverability status before adding a lead to a sales sequence.
- Enrich incomplete lead profiles with company industry and size data via external APIs.

**CRM Maintenance Operations**
- Automatically flag records missing critical data points for manual review.
- Trigger status updates based on data quality scores to keep the pipeline healthy.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. Select your target workspace to clone the solution.
3. Configure your CRM credentials within the Composio Toolset node.
4. Ensure nodes are connected in the sequence: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests or raw data strings.
- **Agent**: Analyzes the input and determines the necessary validation or enrichment steps.
- **Composio Toolset**: Executes the specific CRM API calls (e.g., `update_contact`, `search_lead`).
- **Chat Output**: Returns the processed, cleaned, or validated result to the user.

### 3) Run the Flow
1. Open the **Playground** in your Uplizd workspace.
2. Use one of the following prompts to test the agent:
   - `"Validate the email address for john.doe@example.co.uk and check if it exists in Salesforce."`
   - `"Standardize the company name for record ID 12345 and format the phone number."`
   - `"Check for duplicate leads matching the domain 'acme-corp.com' and flag them for review."`

---

## Configuration

### 1) Language Model (Agent Node)
The Agent node acts as the brain of the operation.
- **Recommended instruction pattern:**
    - Act as a CRM Data Quality expert.
    - Prioritize data integrity and schema compliance.
    - Only call tools when necessary to resolve the user's intent.

### 2) Composio Toolset Node
- **API Key**: Ensure your Composio API key is active and has permissions for your CRM (Salesforce/HubSpot).
- **Connection Scope**: Limit the toolset scope to only the CRM objects required for your specific cleanup tasks.

### 3) Tool Availability
- **CRM Search/Lookup**: For identifying existing records.
- **Update/Patch Tools**: For fixing formatting or missing fields.
- **Validation Services**: For verifying email/phone/address formats.

---

## Related Solutions

- **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.
- **[CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md)**  
  Continuous maintenance to ensure your CRM stays clean, organized, and free of data rot.
- **[CRM Address Data Cleanup Agent](../crm-address-data-cleanup-agent/README.md)**  
  Specialized verification and standardization of physical address and location data.
- **[Deal Pipeline Manager](../deal-pipeline-manager/README.md)**  
  Automatically update deal progress and create follow-up tasks for your sales team.
