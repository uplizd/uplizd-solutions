# Sales Prospect Email Validator (Uplizd) - Ensure deliverability and maximize outreach ROI

## Summary
The Sales Prospect Email Validator (Uplizd) automates the verification of prospect email addresses, ensuring your outreach campaigns reach real inboxes rather than bouncing. By integrating real-time validation via Bouncer, this workflow improves sender reputation, reduces bounce rates, and ensures your sales team focuses their efforts on high-quality, reachable leads.

---

## Demo
![Sales Prospect Email Validator workflow showing email input, Bouncer validation, and status output](image.png)
**Alt text (SEO-ready):** Sales Prospect Email Validator workflow in Uplizd using Bouncer for real-time email verification, CRM data hygiene, and outreach optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/9858130d-8237-5b5c-b551-1c9d2cb4dee6)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** email validation, bouncer, lead hygiene, sales outreach, crm, data quality, composio, ai workflow
- This solution bridges the gap between raw lead lists and high-performance sales outreach by automating the critical step of email verification.

---

## Who is this for?
This workflow is designed for revenue teams looking to maintain pristine contact data and improve campaign performance.

- **Sales Development Reps (SDRs)**
    - Eliminate time wasted on manual verification and focus exclusively on reachable prospects.
- **RevOps Managers**
    - Maintain high data hygiene standards across the CRM to prevent domain blacklisting.
- **Marketing Operations Specialists**
    - Ensure email marketing lists are clean, improving overall deliverability and sender score.
- **Account Executives**
    - Increase meeting booking rates by ensuring outreach sequences reach the intended decision-makers.

---

## Features
- **Real-time Email Verification**
    - Instantly check email validity against Bouncer’s global database to identify risky or invalid addresses.
- **Automated Bounce Prevention**
    - Filter out "catch-all" or "disposable" emails before they enter your active sales sequence.
- **Seamless CRM Integration**
    - Use the Composio Toolset to push validation statuses directly back into your CRM fields.
- **Bulk Processing Capability**
    - Handle large lists of prospect data efficiently through the automated agent pipeline.
- **Actionable Output Reporting**
    - Receive clear, categorized feedback on every email address processed by the agent.

---

## Use Cases
**Lead List Hygiene**
- Automatically scrub imported CSV lists of prospects before adding them to a CRM campaign.
- Flag invalid email addresses for manual review or removal to protect your domain reputation.

**Outreach Campaign Preparation**
- Validate prospect contact information immediately before triggering automated email sequences.
- Ensure high-value account outreach is directed only to verified, active professional addresses.

**CRM Data Enrichment**
- Update existing CRM records with verified status tags to keep historical data accurate.
- Sync validation results across multiple platforms using the Composio Toolset to maintain a single source of truth.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Import the workflow into your active Uplizd workspace.
3. Connect your Bouncer API credentials and CRM integrations within the settings.
4. Ensure nodes are correctly mapped and all API connections are authorized.

### 2) Setup the Nodes
- **Chat Input:** Accepts the prospect email address or list of addresses to be validated.
- **Agent:** Analyzes the request and coordinates the validation logic using the Bouncer toolset.
- **Composio Toolset:** Executes the actual verification API calls and updates CRM records.
- **Chat Output:** Returns the validation status (Valid, Invalid, or Risky) to the user.

### 3) Run the Flow
Use the Playground to test your validation logic:
- `Validate this email: john.doe@example.com`
- `Check the validity of the following list: [email1, email2, email3]`
- `Verify prospect email and update the status in Salesforce if valid.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your data validation logic.
- Instruct the agent to prioritize accuracy and handle "risky" emails with caution.
- Define clear output formats for validation results (e.g., JSON or summary tables).
- Ensure the agent follows strict error-handling protocols if the Bouncer API is unreachable.

### 2) Composio Toolset Node
- Provide your Bouncer API key to enable deep integration with email verification services.
- Configure the connection scope to allow the agent to read/write to your CRM's contact objects.

### 3) Tool Availability
- **Bouncer API:** For real-time email syntax and deliverability checks.
- **CRM Connector:** For updating contact fields based on validation results.
- **Data Parser:** For extracting email addresses from unstructured input strings.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich prospect data with professional contact details.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain overall CRM data quality and remove duplicates.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather deep insights on target accounts before outreach.
