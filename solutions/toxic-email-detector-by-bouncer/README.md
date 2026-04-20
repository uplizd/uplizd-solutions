# Toxic Email Detector (Uplizd) - Protect sender reputation by identifying and filtering toxic email addresses

## Summary
The Toxic Email Detector by Bouncer is an automated Uplizd workflow designed to scan, validate, and flag harmful or invalid email addresses before they enter your CRM or marketing pipeline. By leveraging real-time email verification, this solution ensures your communication channels remain clean, preventing bounce rates and protecting your domain's sender reputation.

---

## Demo
![Toxic Email Detector workflow showing email validation via Bouncer integration](image.png)
**Alt text (SEO-ready):** Toxic Email Detector workflow by Bouncer, demonstrating automated email validation, hygiene, and CRM data cleansing on the Uplizd platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a54d71ef-c9bb-5ffc-abb6-cd51fec135a8)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** email validation, bouncer, crm, data quality, sender reputation, bounce prevention, composio, ai workflow
- This solution integrates directly with Bouncer to provide real-time email verification, ensuring only high-quality, deliverable contacts reach your sales and marketing systems.

---

## Who is this for?
This solution is designed for teams focused on maintaining high deliverability and clean contact databases.

- **Email Marketers**
    - Ensure high open rates by preventing campaigns from being sent to invalid or toxic addresses.
- **Sales Operations Managers**
    - Maintain CRM data integrity by automatically filtering out low-quality leads during the ingestion process.
- **Deliverability Specialists**
    - Protect domain reputation by identifying and blacklisting high-risk, disposable, or toxic email domains.
- **Growth Leads**
    - Optimize lead nurturing pipelines by ensuring every contact in the system is verified and reachable.

---

## Features
- **Real-time Verification**
    - Instant validation of email addresses using Bouncer’s high-accuracy API to determine deliverability status.
- **Toxic Domain Detection**
    - Automated identification of disposable, temporary, or known malicious email providers that threaten sender health.
- **Composio-Powered Integration**
    - Seamlessly connects the Uplizd agent with Bouncer and your CRM to automate the cleanup of incoming lead data.
- **Customizable Thresholds**
    - Define specific risk levels to determine which emails should be blocked, flagged for review, or allowed into your database.
- **Automated Reporting**
    - Generates summary logs of filtered addresses, providing visibility into the quality of your incoming lead sources.

---

## Use Cases
**Lead Ingestion Hygiene**
- Automatically verify new leads captured via web forms before they are synced to your CRM.
- Flag "toxic" or "disposable" email addresses for manual review by the sales team.

**Marketing List Scrubbing**
- Batch-process existing contact lists to remove decayed or invalid entries before launching a major campaign.
- Identify and remove high-risk email addresses to prevent domain blacklisting.

**CRM Data Maintenance**
- Trigger periodic cleanup workflows to re-verify existing contact records that have not been engaged for over 90 days.
- Update lead status fields in your CRM based on the verification results provided by the Bouncer toolset.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Bouncer and CRM accounts within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the email address or lead data batch for processing.
- **Agent**: Analyzes the input and triggers the verification tool based on defined logic.
- **Composio Toolset**: Executes the Bouncer API calls to validate the email status.
- **Chat Output**: Returns the verification result and the action taken on the lead record.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
- `Verify the email address: test-user@example.com and update the CRM status.`
- `Check if the following list of emails contains any toxic or disposable addresses: [email1, email2, email3].`
- `Run a validation check on all new leads added to the CRM in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your data input and the Bouncer verification engine.
- Use a model capable of structured data extraction (e.g., GPT-4o).
- Instruction: "Extract email addresses from the input, call the Bouncer verification tool, and categorize the result as 'Valid', 'Risky', or 'Toxic'."
- Instruction: "If an email is 'Toxic', flag it in the CRM with a 'Do Not Contact' tag."

### 2) Composio Toolset Node
- Provide your Bouncer API key within the Composio connection settings.
- Ensure the scope allows for `email.verify` and `email.batch_verify` operations.

### 3) Tool Availability
- `bouncer_verify_email`: Validates a single email address.
- `bouncer_batch_verify`: Processes multiple email addresses for bulk cleanup.
- `crm_update_lead`: Updates the lead status field based on the verification outcome.

---

## Related Solutions
- [../crm-data-hygiene-manager/README.md](CRM Data Hygiene Manager) — Comprehensive tools for maintaining database health and record standardization.
- [../crm-data-sync-agent/README.md](CRM Data Sync Agent) — Synchronize contact data across multiple platforms with conflict resolution.
- [../account-intelligence-gatherer-by-dropcontact/README.md](Account Intelligence Gatherer) — Enrich contact records with professional data and firmographic insights.
