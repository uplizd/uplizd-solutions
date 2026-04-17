# Lead Validation Agent (Uplizd) - Real-time email verification for lead hygiene

## Summary
The Lead Validation Agent is an automated Uplizd workflow that ensures high-quality data entry by verifying email addresses in real-time using NeverBounce. By integrating directly into your lead capture pipeline, this solution eliminates bounce rates, improves sender reputation, and ensures that your sales and marketing teams are only engaging with valid, reachable prospects.

---

## Demo
![Lead Validation Agent workflow diagram showing Chat Input, Agent, NeverBounce toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Lead Validation Agent (Uplizd) workflow diagram for real-time email verification, CRM data hygiene, and automated lead qualification using NeverBounce and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=appveyor)](https://uplizd.ai/solutions/fab4855d-0bb7-5f9b-b0c7-80530d9a139e)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** crm, lead generation, data hygiene, email verification, neverbounce, sales operations, composio, ai workflow  
This solution bridges the gap between raw lead capture and actionable CRM data by automating the validation process.

---

## Who is this for?
This agent is designed for teams focused on maintaining high-quality lead databases and maximizing outreach efficiency.

*   **Sales Operations Manager**
    *   Ensures CRM data integrity by preventing invalid email addresses from entering the sales pipeline.
*   **Demand Generation Specialist**
    *   Protects sender domain reputation by ensuring all inbound leads are verified before triggering automated nurture sequences.
*   **BDR/SDR Lead**
    *   Increases outbound productivity by ensuring time is spent only on verified, reachable prospects.
*   **CRM Administrator**
    *   Automates the cleanup of contact records, reducing manual data entry and maintenance overhead.

---

## Features
- **Real-Time Verification**
  Instantly checks the validity of email addresses at the moment of capture, preventing bad data from ever reaching your database.
- **NeverBounce Integration**
  Leverages the industry-leading NeverBounce API via the Composio Toolset to provide accurate, reliable verification results.
- **Automated Hygiene Pipeline**
  Seamlessly integrates into existing workflows to flag or reject invalid leads based on custom validation logic.
- **Reduced Bounce Rates**
  Significantly lowers email bounce rates, protecting your domain from being blacklisted by major email service providers.
- **Actionable Output**
  Provides clear status updates (Valid, Invalid, Disposable, or Unknown) to trigger downstream actions like CRM updates or manual review alerts.

---

## Use Cases
**Lead Capture Optimization**
*   Automatically validate leads submitted via web forms before they are synced to your CRM.
*   Flag invalid email entries for immediate correction by the sales team during the onboarding process.

**Outreach Campaign Protection**
*   Filter out disposable or catch-all email addresses before adding leads to high-volume cold outreach sequences.
*   Maintain a healthy sender reputation by ensuring only verified contacts receive marketing communications.

**CRM Data Maintenance**
*   Run bulk validation checks on existing lead lists to identify and remove decayed or incorrect contact information.
*   Sync validation status back to custom CRM fields to keep lead scoring models accurate and up-to-date.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import" to load the workflow into your builder.
3. Connect your NeverBounce account through the Composio integration settings.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all API credentials.

### 2) Setup the Nodes
*   **Chat Input**: Receives the lead email address or contact object from your trigger source.
*   **Agent**: Processes the request and determines the validation requirement based on the provided email.
*   **Composio Toolset**: Executes the NeverBounce API call to verify the email status.
*   **Chat Output**: Returns the validation result and triggers the next step in your CRM or notification system.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Validate the email address: john.doe@example.com`
* `Check if the lead email 'marketing@disposable-service.com' is valid for outreach.`
* `Verify the contact list provided in the input and return only the valid email addresses.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for the validation logic.
*   **Instruction Pattern:**
    *   "You are a lead validation assistant; always prioritize accuracy when checking email status."
    *   "If the NeverBounce tool returns 'invalid', flag the lead for immediate removal or correction."
    *   "Provide a concise summary of the validation result to the user or downstream system."

### 2) Composio Toolset Node
*   **API Key:** Ensure your NeverBounce API key is active within the Composio dashboard.
*   **Connection Scope:** Grant the agent permission to access the NeverBounce verification endpoints.

### 3) Tool Availability
*   `NeverBounce_Verify`: Core tool for checking email validity.
*   `NeverBounce_GetAccountBalance`: Optional tool for monitoring API credit usage.
*   `NeverBounce_BulkVerification`: Tool for processing lists of leads in a single batch.

---

## Related Solutions
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automates the cleanup and formatting of CRM contact records.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes lead data across multiple platforms and CRM instances.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enriches lead profiles with professional data and company insights.
