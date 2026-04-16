# Campaign Email List Cleaner (Uplizd) - Automate email verification and improve deliverability

## Summary
The Campaign Email List Cleaner (Uplizd) is an automated workflow designed to sanitize and validate your marketing contact lists before deployment. By integrating real-time verification services with your email marketing platform, this solution ensures high sender reputation, reduces bounce rates, and maximizes campaign ROI by maintaining a single source of truth for your clean, high-intent audience data.

---

## Demo
![Campaign Email List Cleaner workflow diagram showing email input, verification agent, and cleaned output](image.png)
**Alt text (SEO-ready):** Campaign Email List Cleaner workflow for Uplizd, automating email verification, marketing list hygiene, and bounce rate reduction using the Composio Toolset.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgMTJoM3Y5aDZ2LTdoMnY3aDZ2LTloM0wxMiAyeiIvPjwvc3ZnPg==)](https://uplizd.ai/solutions/e76bf586-c1a1-53c1-a714-ecb21a6ce453)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, data hygiene, list cleaning, deliverability, emaillistverify, composio, ai workflow, marketing automation
- This solution bridges the gap between raw contact acquisition and high-performance email delivery by automating the validation lifecycle.

---

## Who is this for?
This solution is built for marketing and growth teams focused on maintaining pristine contact data and high-performing outreach campaigns.

- **Email Marketer**
    - Ensures higher inbox placement rates by removing invalid or risky email addresses before sending.
- **Growth Operations Manager**
    - Automates the data hygiene pipeline to reduce manual list scrubbing and improve lead quality.
- **CRM Administrator**
    - Maintains database integrity by syncing verified contact statuses back to the source of truth.
- **Demand Generation Specialist**
    - Maximizes campaign ROI by ensuring marketing spend is only directed toward reachable, verified prospects.

---

## Features
- **Automated List Validation**
    - Instantly triggers verification checks for new or existing contact lists via the EmailListVerify API.
- **Real-time Bounce Prevention**
    - Identifies and flags invalid, disposable, or catch-all email addresses before they enter your active marketing funnel.
- **Composio-Powered Integrations**
    - Leverages the Composio Toolset to seamlessly connect your email verification service with CRMs and marketing platforms.
- **Data Hygiene Reporting**
    - Generates summary reports on list health, highlighting the percentage of clean vs. risky contacts.
- **Seamless Workflow Orchestration**
    - Automates the hand-off between data input, verification processing, and final list segmentation.

---

## Use Cases
**Marketing Campaign Preparation**
- Automatically scrub lead lists imported from trade shows or webinars before adding them to a nurture sequence.
- Filter out high-risk domains that could trigger spam filters and damage your domain reputation.

**CRM Data Maintenance**
- Periodically verify existing CRM contact records to ensure long-term data accuracy and reduce storage costs.
- Update contact status fields automatically based on verification results (e.g., "Verified," "Invalid," "Risky").

**Lead Qualification Pipelines**
- Integrate verification steps directly into your lead intake forms to ensure only valid emails reach your sales team.
- Route "Risky" or "Catch-all" emails to a secondary manual review queue instead of the primary sales pipeline.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Campaign Email List Cleaner template from the solution library.
3. Connect your preferred email verification API and CRM credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the list of email addresses or trigger event from your marketing platform.
- **Agent**: Analyzes the input and orchestrates the verification logic.
- **Composio Toolset**: Executes the API calls to verify email validity and update CRM records.
- **Chat Output**: Returns the verification results and a summary of the cleaned list.

### 3) Run the Flow
Use the Playground to test your workflow with the following prompts:
- `Verify the following list of emails for our upcoming Q3 newsletter: [email1, email2, email3].`
- `Check the validity of all new contacts added to the 'Webinar Leads' list in our CRM.`
- `Clean our primary marketing list and remove any addresses that return a 'Hard Bounce' or 'Invalid' status.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the workflow coordinator, interpreting verification results and deciding on the next action.
- Use a high-reasoning model to ensure accurate parsing of API responses.
- Instruct the agent to prioritize "Verified" status updates in the CRM.
- Configure the agent to summarize errors for any failed verification attempts.

### 2) Composio Toolset Node
- Provide your **EmailListVerify API Key** and relevant CRM credentials (e.g., HubSpot, Salesforce) within the Composio configuration.
- Set the connection scope to allow read/write access to contact objects and email fields.

### 3) Tool Availability
- **Email Verification API**: For bulk and single address validation.
- **CRM Connector**: For updating contact properties and status fields.
- **Data Transformation Tool**: For formatting list outputs into CSV or JSON formats.

---

## Related Solutions
- [../abandoned-cart-recovery-agent-by-klaviyo/README.md](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automate recovery emails for lost sales.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Maintain overall database health and data quality.
- [../whats-app-lead-nurturing-agent-by-spoki/README.md](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Engage leads through multi-channel nurturing.
