# Secure Customer Data Sharing Agent (Uplizd) - Automated anonymization for compliant cross-team collaboration

## Summary
The Secure Customer Data Sharing Agent by Anonyflow streamlines the process of sharing sensitive customer information across internal teams by applying real-time, automated anonymization. This workflow ensures that PII (Personally Identifiable Information) is redacted or masked before it reaches external or internal stakeholders, maintaining data hygiene and regulatory compliance without sacrificing operational velocity.

---

## Demo
![Secure Customer Data Sharing Agent workflow diagram showing data input, anonymization, and secure output](image.png)
**Alt text (SEO-ready):** Secure Customer Data Sharing Agent workflow for automated PII redaction, data privacy, and compliant information exchange using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fbc33399-e91a-5067-992c-bc201e4092fc)

---

## Category
**Primary category:** Data Privacy & Compliance
**Secondary tags:** crm, data hygiene, security, privacy, anonymization, compliance, composio, ai workflow.
This solution bridges the gap between data accessibility and security, ensuring teams can collaborate effectively while adhering to strict internal data governance policies.

---

## Who is this for?
This solution is designed for organizations that need to balance high-speed collaboration with stringent data protection requirements.

* **Data Protection Officer**
    * Ensures all shared customer records meet GDPR, CCPA, and internal security standards automatically.
* **Sales Operations Manager**
    * Facilitates safe lead hand-offs between departments without exposing sensitive contact details.
* **Customer Support Lead**
    * Enables support agents to share ticket context with engineering teams while masking private user identifiers.
* **IT Security Analyst**
    * Reduces the attack surface by minimizing the distribution of raw, unmasked customer data across internal communication channels.

---

## Features
- **Automated PII Detection**
    Identifies sensitive fields like email, phone numbers, and addresses in real-time using intelligent pattern recognition.
- **Configurable Masking Rules**
    Allows users to define specific redaction levels, from full masking to partial obfuscation, based on the recipient's role.
- **Composio-Powered Integration**
    Leverages the Composio Toolset to securely fetch data from CRMs and push sanitized versions to downstream platforms.
- **Audit-Ready Logging**
    Maintains a record of what data was shared and how it was anonymized, providing a clear trail for compliance audits.
- **Real-Time Data Sanitization**
    Processes data streams instantly, ensuring that information is protected the moment it is requested or moved.

---

## Use Cases
**Cross-Departmental Collaboration**
* Redacting PII from customer support tickets before escalating to the engineering or product development teams.
* Sharing lead summaries with external marketing agencies while keeping raw contact information strictly internal.

**Compliance & Data Governance**
* Automating the cleanup of legacy CRM records to ensure only authorized personnel have access to full customer profiles.
* Enforcing data masking policies during bulk exports for quarterly business reviews or external reporting.

**Secure Workflow Automation**
* Triggering a secure data share request via chat that automatically masks fields before posting to a team Slack or Teams channel.
* Validating data integrity during migration tasks to ensure no unmasked sensitive data is leaked into development environments.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the `secure-customer-data-sharing-agent-by-anonyflow` template from the marketplace.
3. Connect your required CRM and communication tool credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to the **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the request for customer data and the target recipient context.
* **Agent:** Analyzes the data payload and applies the configured anonymization logic.
* **Composio Toolset:** Executes the secure retrieval and transformation of data from the source system.
* **Chat Output:** Delivers the sanitized, safe-to-share data back to the user.

### 3) Run the Flow
Use the Uplizd Playground to test your anonymization rules:
* `Anonymize the contact details for customer ID 98234 and share with the engineering team.`
* `Fetch the latest support ticket for user 'John Doe' and mask all PII for the external report.`
* `Securely share the account summary for 'Acme Corp' with the sales team, redacting email and phone fields.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for identifying and redacting sensitive information.
* Use a model with high reasoning capabilities to ensure accurate PII detection.
* Instruction: "Identify all PII in the provided data, apply masking rules based on the recipient role, and ensure no raw sensitive data is passed to the output."
* Instruction: "If the data type is ambiguous, default to full redaction to maintain maximum security."

### 2) Composio Toolset Node
* Provide the necessary API keys for your CRM (e.g., Salesforce, HubSpot).
* Ensure the connection scope is limited to read-only access for data retrieval to minimize security risks.

### 3) Tool Availability
* **CRM Data Fetcher:** Retrieves raw customer records.
* **PII Redaction Engine:** Applies masking masks to specific data fields.
* **Communication Connector:** Sends the sanitized output to the designated channel.

---

## Related Solutions
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automates bulk data cleanup and formatting to maintain high-quality CRM records.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes customer data across multiple platforms with conflict resolution.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Tracks and manages sales opportunities through various pipeline stages.
