# Lead Qualification Validator (Uplizd) - Real-time email verification and prospect scoring

## Summary
The Lead Qualification Validator is an automated Uplizd workflow designed to streamline sales operations by verifying prospect email addresses in real-time. By integrating directly with your CRM and email validation services, this solution ensures your pipeline remains populated with high-quality, reachable leads, significantly reducing bounce rates and improving overall sales development productivity.

---

## Demo
![Lead Qualification Validator workflow diagram showing email input, validation agent, and CRM update](image.png)
**Alt text (SEO-ready):** Uplizd Lead Qualification Validator workflow for real-time email verification, CRM data hygiene, and sales pipeline optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/0f0d4209-1b12-5ddd-b656-9253f85fcb13)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, email validation, lead qualification, sales operations, data hygiene, composio, ai workflow
- This solution bridges the gap between raw lead generation and CRM data integrity by automating the verification process.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to optimize their outreach efficiency and maintain clean prospect databases.

- **Sales Development Representative (SDR)**
    - Eliminates time wasted on invalid email addresses and bounced outreach campaigns.
- **RevOps Manager**
    - Ensures a single source of truth for lead quality metrics across the entire sales pipeline.
- **Marketing Operations Specialist**
    - Protects sender reputation by ensuring only verified, deliverable contacts enter the CRM.
- **Account Executive (AE)**
    - Increases focus on high-intent, qualified opportunities by filtering out junk data early.

---

## Features
- **Real-time Email Verification**
    - Instantly validates email syntax and deliverability status using the Composio Toolset before data reaches your CRM.
- **Automated CRM Enrichment**
    - Automatically updates lead status or adds verification tags in your CRM based on the validation results.
- **Intelligent Bounce Prevention**
    - Flags high-risk or disposable email addresses to prevent them from entering your active sales sequences.
- **Seamless Composio Integration**
    - Leverages powerful connectors to bridge your CRM and email validation APIs without writing custom middleware.
- **Customizable Qualification Logic**
    - Easily adjust the Agent instructions to define what constitutes a "qualified" lead based on your specific business rules.

---

## Use Cases
**Pipeline Hygiene**
- Automatically purge or flag invalid leads imported from bulk CSV uploads or web forms.
- Sync verification status across multiple CRM platforms to maintain consistent data quality.

**Outreach Optimization**
- Validate prospect contact information immediately after a lead is captured via landing page.
- Prioritize follow-up tasks for leads that pass verification, ensuring SDRs focus on reachable prospects.

**Sales Efficiency**
- Reduce manual data entry by automating the validation check during the lead creation process.
- Improve email deliverability rates by preventing high-bounce-risk addresses from entering automated sequences.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your dashboard.
3. Authenticate your CRM and Email Validation tool connections within the Composio settings.
4. Ensure nodes are correctly mapped and the Agent is configured with your specific validation criteria.

### 2) Setup the Nodes
- **Chat Input**: Receives the prospect email and lead metadata for processing.
- **Agent**: Analyzes the input and triggers the validation logic based on the provided instructions.
- **Composio Toolset**: Executes the API calls to verify the email and update the CRM record.
- **Chat Output**: Returns the validation status and confirmation of the CRM update to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Verify the email address john.doe@example.com and update his status in Salesforce if valid.`
- `Check if the lead 'marketing-lead-001' has a deliverable email address and flag it for review if invalid.`
- `Validate the contact info for the new lead from HubSpot and move them to the 'Qualified' pipeline stage.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for lead qualification.
- Use a model with strong reasoning capabilities to interpret validation API responses.
- Instruct the agent to prioritize "deliverable" status over "risky" or "unknown" results.
- Maintain a clear mapping between validation outcomes and CRM field updates.

### 2) Composio Toolset Node
- Provide your API keys for both your CRM (e.g., Salesforce, HubSpot) and your chosen Email Validation service.
- Ensure the connection scope includes read/write access to lead and contact objects.

### 3) Tool Availability
- **CRM Connector**: For reading lead data and updating qualification fields.
- **Email Validation API**: For real-time syntax and SMTP verification checks.
- **Logging Utility**: To track validation history and audit changes made to lead records.

---

## Related Solutions
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate bulk data cleanup and formatting.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple CRM platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up automation.
