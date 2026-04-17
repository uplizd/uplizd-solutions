# Email List Cleaner Agent (Uplizd) - Automated email validation and list hygiene for high-deliverability campaigns

## Summary
The Email List Cleaner Agent is an intelligent Uplizd workflow designed to automate the validation, scoring, and hygiene of email marketing lists. By leveraging real-time verification tools, this agent identifies invalid, risky, or inactive addresses, ensuring your sender reputation remains high and your marketing automation pipelines maintain optimal deliverability.

---

## Demo
![Email List Cleaner Agent workflow interface showing input validation, email scoring, and list export nodes in Uplizd](image.png)
**Alt text (SEO-ready):** Email List Cleaner Agent workflow in Uplizd for automated email validation, list hygiene, and marketing data cleanup.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d06f58a5-4d62-5759-8cc8-a9823eba966a)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** email marketing, data hygiene, list cleaning, deliverability, crm, composio, ai workflow, lead management  
This solution streamlines marketing operations by ensuring only high-quality, verified contact data enters your outreach pipeline.

---

## Who is this for?
This agent is built for teams looking to eliminate bounce rates and improve campaign performance through automated data maintenance.

*   **Email Marketer**
    *   Reduces bounce rates by proactively scrubbing lists before campaign deployment.
*   **RevOps Manager**
    *   Maintains CRM data integrity by syncing verified contact statuses across platforms.
*   **Lead Generation Specialist**
    *   Ensures outbound efforts are directed toward valid, reachable prospects.
*   **Marketing Operations Lead**
    *   Automates the tedious process of list auditing to save hours of manual data entry.

---

## Features
- **Real-time Email Validation**
  Instantly verify email syntax, domain existence, and mailbox availability using integrated verification tools.
- **Risk Scoring Engine**
  Assigns a quality score to each email address, allowing you to filter out high-risk or disposable addresses automatically.
- **CRM Data Synchronization**
  Seamlessly updates contact records in your CRM with the latest validation status via the Composio Toolset.
- **Automated List Segmentation**
  Automatically sorts cleaned contacts into "Ready to Send," "Review Required," and "Invalid" buckets.
- **Compliance-Aware Cleanup**
  Ensures that list maintenance adheres to data privacy standards by flagging contacts that require re-permissioning.

---

## Use Cases
**Campaign Deliverability**
*   Scrubbing large lead lists before launching a high-volume cold outreach sequence.
*   Identifying and removing "catch-all" or risky domains that threaten sender reputation.

**CRM Data Maintenance**
*   Periodic auditing of existing CRM contacts to remove decayed or inactive email addresses.
*   Updating lead status fields based on real-time validation results to trigger follow-up workflows.

**Lead Qualification**
*   Verifying new sign-ups from web forms to ensure only valid business emails enter the sales funnel.
*   Prioritizing high-quality leads for immediate outreach based on verified email domain authority.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Email List Cleaner Agent template from the solution library.
3. Connect your preferred email validation provider via the Composio Toolset.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw email list or individual contact record.
*   **Agent**: Analyzes the input and determines the necessary validation steps.
*   **Composio Toolset**: Executes the API calls to verify the email address and update the CRM.
*   **Chat Output**: Returns the validation report and the cleaned contact status.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
* `Validate the following email list: [email1@example.com, email2@test.co] and update the status in my CRM.`
* `Check the quality score for this lead: [contact@company.com] and flag it if it's a disposable address.`
* `Audit my recent lead import and move all invalid emails to the 'Do Not Contact' list.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for validation logic and CRM communication.
*   Prioritize accuracy in identifying "risky" vs. "invalid" email statuses.
*   Maintain a neutral, analytical tone when reporting list health metrics.
*   Always confirm the specific CRM field being updated before executing a bulk change.

### 2) Composio Toolset Node
Requires an active API key for your chosen email validation service (e.g., ZeroBounce, NeverBounce) and your CRM integration (e.g., Salesforce, HubSpot). Ensure the connection scope includes read/write access to contact objects.

### 3) Tool Availability
*   **Email Verification API**: Performs syntax checks and SMTP handshake validation.
*   **CRM Connector**: Updates contact records with validation metadata.
*   **Data Parser**: Extracts email addresses from unstructured text or CSV-like inputs.

---

## Related Solutions
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automates the cleanup of duplicate and decayed CRM records.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes contact data across multiple platforms to ensure consistency.
* [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Targets verified contacts with automated recovery sequences.
