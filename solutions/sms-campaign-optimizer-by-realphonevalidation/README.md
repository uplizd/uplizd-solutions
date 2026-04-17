# SMS Campaign Optimizer (Uplizd) - Enhance SMS deliverability and campaign ROI through real-time number validation

## Summary
The SMS Campaign Optimizer is an automated Uplizd workflow designed to maximize marketing reach and reduce costs by filtering out invalid or non-mobile numbers before deployment. By integrating real-time validation, this solution ensures your SMS campaigns reach active, reachable devices, significantly improving engagement rates and protecting your sender reputation.

---

## Demo
![SMS Campaign Optimizer workflow showing data input, validation node, and filtered output](image.png)
**Alt text (SEO-ready):** Uplizd SMS Campaign Optimizer workflow for mobile number validation, CRM data hygiene, and automated marketing campaign optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/77f00b6c-af8c-59e8-9f3e-ca814e8b86c2)

---

## Category
* **Primary category:** Marketing operations
* **Secondary tags:** sms, mobile marketing, data hygiene, lead validation, campaign optimization, composio, ai workflow
* This solution bridges the gap between raw contact lists and high-performing SMS campaigns by automating the technical verification of mobile phone data.

---

## Who is this for?
This solution is designed for teams managing high-volume mobile outreach who need to ensure data accuracy and compliance.

* **Marketing Manager**
    * Reduces wasted spend on inactive numbers and improves overall campaign ROI.
* **SMS Campaign Specialist**
    * Automates the list-scrubbing process to ensure only valid, reachable numbers enter the send queue.
* **RevOps Lead**
    * Maintains high-quality CRM data hygiene by flagging and removing dead or landline contacts.
* **Growth Marketer**
    * Increases deliverability rates and engagement by targeting verified mobile users exclusively.

---

## Features
- **Real-time Number Validation**
  Instantly verify if a contact number is a valid mobile device capable of receiving SMS.
- **Automated List Scrubbing**
  Automatically filter out landlines, disconnected numbers, and invalid formats before your campaign launches.
- **Composio Toolset Integration**
  Seamlessly connects your CRM and SMS platforms to the validation engine for end-to-end automation.
- **Data Hygiene Reporting**
  Generate insights on the quality of your contact lists to identify trends in data decay.
- **Customizable Thresholds**
  Set specific validation rules to handle edge cases like international numbers or carrier-specific restrictions.

---

## Use Cases
**Campaign Pre-Flight Checks**
* Validate entire contact segments against the RealPhoneValidation database before triggering an SMS blast.
* Automatically flag contacts that fail validation for manual review or removal from the active marketing list.

**CRM Data Enrichment**
* Update CRM contact fields with validation status and carrier information for better segmentation.
* Sync cleaned data back to your primary marketing platform to ensure future campaigns start with high-quality lists.

**Lead Qualification**
* Verify mobile numbers during the lead capture process to ensure immediate outreach is possible.
* Prioritize leads that have confirmed, active mobile numbers for faster follow-up by the sales team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your preferred CRM and the RealPhoneValidation API via the Composio Toolset.
3. Configure the input source (e.g., a CSV upload or a CRM list view).
4. Ensure nodes are correctly mapped and the API keys are authorized for production access.

### 2) Setup the Nodes
* **Chat Input**: Receives the list of phone numbers or CRM contact IDs to be processed.
* **Agent**: Analyzes the input and triggers the validation logic based on your campaign requirements.
* **Composio Toolset**: Executes the API calls to validate mobile connectivity and carrier status.
* **Chat Output**: Provides a summary report of validated numbers and a list of contacts to be excluded.

### 3) Run the Flow
Use the Playground to test your validation logic:
* `Validate the following list of numbers for my upcoming SMS campaign: [Insert Numbers]`
* `Filter my CRM list 'Q3_Promotion' and remove all landlines and invalid mobile numbers.`
* `Check the status of these contacts and update the 'SMS_Ready' field in my CRM to true if valid.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for data flow and validation logic.
* Use a system prompt that prioritizes data accuracy and strict adherence to the validation API schema.
* Instruct the agent to categorize results into "Valid," "Invalid," and "Review Required."
* Ensure the agent is configured to handle batch processing for large contact lists efficiently.

### 2) Composio Toolset Node
* Provide your API keys for both your CRM (e.g., HubSpot or Salesforce) and the RealPhoneValidation service.
* Set the connection scope to allow read/write access to contact phone fields.

### 3) Tool Availability
* **Phone Validation API**: Performs the core connectivity and mobile-type checks.
* **CRM Connector**: Enables reading contact lists and updating validation status fields.
* **Data Parser**: Formats raw input data into the structure required by the validation service.

---

## Related Solutions
* [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automate follow-ups for users who left items in their cart.
* [WhatsApp Lead Qualification Agent](../whats-app-lead-qualification-agent-by-whatsapp/README.md) - Qualify leads directly through automated WhatsApp messaging.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain overall database health through automated cleanup and formatting.
