# Contact Database Cleaner (Uplizd) - Automated phone validation and data hygiene

## Summary
The Contact Database Cleaner is an intelligent Uplizd workflow designed to maintain high-quality contact records by automatically verifying phone numbers via RealPhoneValidation. By integrating real-time validation into your CRM pipeline, this solution eliminates invalid entries, reduces bounce rates, and ensures your sales and marketing teams are reaching out to active, reachable leads.

---

## Demo
![Contact Database Cleaner workflow showing phone validation logic](image.png)
**Alt text (SEO-ready):** Contact Database Cleaner workflow in Uplizd, featuring RealPhoneValidation integration for automated CRM data hygiene and lead verification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e3fac6a8-aea2-52fc-834c-43a65cf41a41)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** crm, data validation, phone verification, lead quality, sales operations, realphonevalidation, composio, ai workflow
- This solution streamlines CRM data management by automating the verification of contact information to ensure pipeline accuracy.

---

## Who is this for?
This workflow is designed for teams focused on maintaining pristine lead data and improving outreach efficiency.

- **Sales Operations Managers**
    - Ensure that lead lists are clean and actionable before they reach the sales floor.
- **Growth Marketers**
    - Improve campaign ROI by ensuring SMS and voice outreach targets valid, active numbers.
- **CRM Administrators**
    - Automate the removal of stale or incorrect contact data to maintain database health.
- **BDRs/SDRs**
    - Spend less time dialing disconnected numbers and more time engaging with qualified prospects.

---

## Features
- **Real-Time Validation**
    - Instantly verify phone number status, line type, and carrier information using the RealPhoneValidation API.
- **Automated CRM Cleanup**
    - Automatically flag or remove invalid contacts from your CRM based on validation results.
- **Intelligent Routing**
    - Route verified leads to high-priority sales queues while isolating invalid records for review.
- **Composio-Powered Integration**
    - Seamlessly connect your CRM and validation tools through the Composio Toolset for unified data flow.
- **Customizable Thresholds**
    - Configure the agent to handle specific validation errors, such as disconnected lines or invalid formats, according to your business logic.

---

## Use Cases
**Lead Qualification**
- Automatically validate phone numbers for new inbound leads captured via web forms.
- Score leads based on the validity of their contact information before assigning them to reps.

**Database Maintenance**
- Run bulk cleanup jobs on existing CRM contact lists to identify and purge decayed records.
- Standardize phone number formatting across your entire database for consistent outreach.

**Outreach Optimization**
- Prevent wasted spend on invalid SMS or voice campaigns by pre-verifying contact lists.
- Reduce manual data entry errors by validating inputs at the point of ingestion.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project to import the workflow.
3. Authenticate your CRM and RealPhoneValidation credentials within the integration settings.
4. Ensure nodes are correctly mapped to your specific CRM objects and validation triggers.

### 2) Setup the Nodes
* **Chat Input**: Receives the contact data or trigger event from your CRM.
* **Agent**: Analyzes the contact record and determines the necessary validation steps.
* **Composio Toolset**: Executes the RealPhoneValidation API calls to verify the phone number.
* **Chat Output**: Updates the CRM record with the validation status and notifies the user of the result.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Validate the phone number for lead ID 5501 and update the status in Salesforce.`
- `Check if the phone number +1-555-010-9988 is active and valid.`
- `Scan the latest batch of imported contacts and flag any invalid numbers for manual review.`

---

## Configuration

### 1) Language Model (Agent Node)
The agent acts as the decision-making layer for your data hygiene process.
* Use a model capable of structured data extraction and logical reasoning.
* **Recommended instruction pattern:**
    * "You are a data hygiene assistant; extract the phone number from the input."
    * "Call the RealPhoneValidation tool to verify the number's status."
    * "Update the CRM record with the validation result and provide a summary of the action taken."

### 2) Composio Toolset Node
* Provide your API keys for both your CRM (e.g., Salesforce, HubSpot) and RealPhoneValidation.
* Ensure the connection scope includes read/write access to contact objects and phone fields.

### 3) Tool Availability
* **Phone Validation**: Capability to check line type, carrier, and reachability.
* **CRM Read/Write**: Ability to fetch contact details and update custom fields like `Validation_Status` or `Is_Valid`.
* **Logging**: Capability to record validation history for audit purposes.

---

## Related Solutions
- [Address Verification Agent](../address-verification-agent-by-addresszen/README.md) - Ensure physical address accuracy for shipping and billing.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Comprehensive tools for bulk data cleanup and deduplication.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data with verified contact details and firmographics.
