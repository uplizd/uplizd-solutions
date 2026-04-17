# Form Submission Validator (Uplizd) - Real-time email verification and lead data hygiene

## Summary
The Form Submission Validator (Uplizd) automates the real-time verification of email addresses captured through web forms, ensuring high-quality lead data and reducing bounce rates. By integrating NeverBounce directly into your ingestion pipeline, this workflow acts as a single source of truth for lead hygiene, preventing invalid or disposable emails from entering your CRM and improving overall pipeline velocity.

---

## Demo
![Form Submission Validator workflow showing Chat Input, NeverBounce verification node, and CRM update](image.png)
**Alt text (SEO-ready):** Uplizd workflow for real-time email validation using NeverBounce, CRM data hygiene, and automated lead qualification.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/415f4809-b307-5f85-b83a-d85fef74db04)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** email verification, lead qualification, crm, neverbounce, data integrity, pipeline, composio, ai workflow
- This solution ensures your incoming lead data is clean, actionable, and ready for sales outreach by automating verification at the point of entry.

---

## Who is this for?
This workflow is designed for teams managing high-volume lead pipelines who need to maintain data integrity without manual intervention.

- **RevOps Manager**
    - Ensures only high-quality, deliverable leads reach the sales team to maintain CRM hygiene.
- **Marketing Operations Specialist**
    - Reduces bounce rates on email marketing campaigns by validating addresses at the source.
- **Sales Development Representative (SDR)**
    - Spends less time on invalid leads and focuses outreach efforts on verified, high-intent prospects.
- **Data Engineer**
    - Automates the validation layer in the ingestion pipeline, reducing the need for custom middleware.

---

## Features
- **Real-time Verification**
    - Instantly checks email validity against the NeverBounce database the moment a form is submitted.
- **Automated Filtering**
    - Automatically flags or rejects disposable, invalid, or risky email addresses before they reach your database.
- **Composio Toolset Integration**
    - Seamlessly connects your form ingestion layer with verification tools and CRM platforms via the Composio Toolset.
- **Customizable Thresholds**
    - Set specific rules for how the agent should handle "catch-all" or "unknown" email statuses.
- **CRM Sync Readiness**
    - Ensures that only verified contact records are pushed to your CRM, maintaining a pristine database.

---

## Use Cases
**Lead Ingestion Hygiene**
- Automatically verify leads coming from landing pages before triggering an automated welcome sequence.
- Prevent junk data from polluting your CRM during high-traffic marketing campaigns.

**Sales Outreach Optimization**
- Ensure SDRs only receive notifications for leads that have passed a rigorous email deliverability check.
- Reduce the cost of CRM storage by preventing the accumulation of invalid or duplicate contact records.

**Compliance and Security**
- Filter out known disposable email providers that are often used for bot-driven form spam.
- Maintain a healthy sender reputation by ensuring your outbound communications only target verified, active mailboxes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Form Submission Validator template from the solution library.
3. Connect your NeverBounce API key and CRM credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw form submission data (email, name, source).
- **Agent**: Analyzes the input and triggers the verification request.
- **Composio Toolset**: Executes the NeverBounce API call to validate the email address.
- **Chat Output**: Confirms the validation status and updates the CRM or notifies the team.

### 3) Run the Flow
Use the Playground to test your validation logic with these prompts:
- `Validate this email address: test-user@example.com`
- `Check the deliverability of the email captured in the latest form submission.`
- `Verify the email address provided and update the lead status in Salesforce if valid.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for the validation logic.
- **Instruction Pattern:**
    - "Always prioritize the NeverBounce verification result before proceeding to CRM updates."
    - "If the email status is 'invalid', flag the record and notify the marketing team."
    - "Maintain a log of all verification attempts for audit purposes."

### 2) Composio Toolset Node
- **API Key:** Provide your NeverBounce API key in the toolset configuration.
- **Connection Scope:** Ensure the agent has read/write access to your CRM and the NeverBounce verification endpoint.

### 3) Tool Availability
- **NeverBounce API**: For real-time email verification and status reporting.
- **CRM Connector**: For updating lead fields based on verification results.
- **Notification Service**: For alerting teams when invalid leads are detected.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich company data for verified leads.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain long-term database health and compliance.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep dive into verified accounts for personalized outreach.
