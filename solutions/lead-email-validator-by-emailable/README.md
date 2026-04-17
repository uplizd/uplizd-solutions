# Lead Email Validator (Uplizd) - Automate email verification and improve CRM deliverability

## Summary
The Lead Email Validator (Uplizd) is an automated AI workflow designed to maintain high-quality contact lists by verifying email addresses in real-time. By integrating with the Emailable API, this solution helps sales and marketing teams reduce bounce rates, protect sender reputation, and ensure that critical outreach reaches the intended inbox, serving as a single source of truth for lead data hygiene.

---

## Demo
![Lead Email Validator workflow showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Lead Email Validator workflow on Uplizd for automated CRM data hygiene, email verification, and sales pipeline optimization using Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/21e1068f-538b-5fa0-8c3f-2a5f107439bf)

---

## Category
*   **Primary category:** Sales automation
*   **Secondary tags:** crm, emailable, data hygiene, lead qualification, sales operations, email deliverability, composio, ai workflow
*   This solution streamlines lead management by automating the validation process, ensuring your CRM remains populated with accurate, high-intent contact data.

---

## Who is this for?
This solution is designed for teams focused on maintaining pristine lead databases and maximizing outreach efficiency.

*   **Sales Operations Manager**
    *   Automates data cleaning processes to prevent lead decay and improve overall pipeline accuracy.
*   **Email Marketing Specialist**
    *   Protects sender reputation by filtering out invalid or risky email addresses before campaign deployment.
*   **Business Development Representative (BDR)**
    *   Ensures that time is spent only on reachable prospects, increasing conversion rates and outreach velocity.
*   **CRM Administrator**
    *   Maintains high data hygiene standards across the organization by integrating real-time validation into existing workflows.

---

## Features
- **Real-time Email Verification**
  Instantly validate email addresses against the Emailable database to confirm deliverability status.
- **Automated CRM Hygiene**
  Automatically flag or update contact records in your CRM based on verification results, reducing manual data entry.
- **Risk Scoring Integration**
  Receive detailed insights on email quality, including risk levels, to make informed decisions on lead prioritization.
- **Seamless Composio Connectivity**
  Leverage the Composio Toolset to bridge the gap between your AI agent and external CRM/Email platforms.
- **Proactive Bounce Prevention**
  Identify and remove invalid syntax or non-existent domains before they impact your email marketing performance.

---

## Use Cases
**Lead Qualification**
*   Verify new inbound leads immediately upon entry to ensure only valid contacts enter the sales sequence.
*   Score leads based on email deliverability to prioritize high-value, reachable prospects.

**Data Maintenance**
*   Run bulk validation checks on existing CRM lists to identify and purge decayed or inactive contact records.
*   Sync validation status back to custom CRM fields to keep sales teams informed of lead health.

**Outreach Optimization**
*   Filter out high-risk "catch-all" or disposable email addresses to maintain a healthy sender reputation.
*   Automate the re-verification of stale leads before launching large-scale re-engagement campaigns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Email Validator template from the solution library.
3. Connect your preferred CRM and Emailable API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the email address or lead record to be validated.
*   **Agent**: Analyzes the request and triggers the appropriate verification tool.
*   **Composio Toolset**: Executes the API call to Emailable to perform the validation.
*   **Chat Output**: Returns the validation status and quality score to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
* `Validate the email address: contact@example.com`
* `Check the deliverability status for the lead in my CRM with email john.doe@company.com`
* `Run a verification check on the latest leads added to my CRM today`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for data validation tasks.
*   Use a model capable of structured data extraction (e.g., GPT-4o).
*   Instruction: "You are a data hygiene assistant. Extract email addresses from the input, verify them using the provided tools, and report the deliverability status clearly."
*   Instruction: "If an email is invalid, suggest the next steps for the user to update the record."

### 2) Composio Toolset Node
*   Ensure your Emailable API key is stored securely in the Composio connection settings.
*   Grant the agent scope to read/write contact information from your connected CRM.

### 3) Tool Availability
*   `emailable_verify`: Performs the core email validation check.
*   `crm_get_contact`: Retrieves lead details for verification.
*   `crm_update_contact`: Updates the record with the validation result.

---

## Related Solutions
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data and verify contact details.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Maintain overall CRM data quality and remove duplicates.
*   [Lead Qualification Agent](../whats-app-lead-qualification-agent-by-whatsapp/README.md) — Qualify leads across messaging channels.
