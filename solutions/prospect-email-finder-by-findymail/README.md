# Prospect Email Finder (Uplizd) - Automated lead contact discovery and verification

## Summary
The Prospect Email Finder is an intelligent Uplizd AI workflow designed to streamline sales outreach by automatically identifying and verifying professional email addresses for your prospects. By leveraging the Findymail integration, this solution eliminates manual research, ensures high deliverability rates, and accelerates your pipeline velocity by providing a single source of truth for lead contact data.

---

## Demo
![Prospect Email Finder workflow showing automated lead enrichment and email verification](image.png)
**Alt text (SEO-ready):** Uplizd Prospect Email Finder workflow, automated lead enrichment, email verification using Findymail, sales automation, and CRM data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f722364c-cd71-5cc5-bd98-5404000ab26e)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** sales, lead generation, email enrichment, findymail, crm, data hygiene, composio, ai workflow
- This solution bridges the gap between raw lead lists and actionable contact data, ensuring your sales team spends more time selling and less time searching.

---

## Who is this for?
This solution is built for revenue-focused teams looking to scale their outbound efforts with precision and speed.

- **Sales Development Representative (SDR)**
    - Reduces time spent on manual prospecting, allowing for higher daily outreach volume.
- **Account Executive (AE)**
    - Ensures accurate contact information for key stakeholders during high-value deal cycles.
- **RevOps Manager**
    - Maintains high-quality CRM data hygiene by automating the enrichment of lead records.
- **Growth Marketer**
    - Increases campaign conversion rates by ensuring email communications reach verified, active inboxes.

---

## Features
- **Automated Email Discovery**
    - Leverages Findymail to scan professional databases and return verified email addresses for your target leads.
- **Real-Time Verification**
    - Performs instant validation checks to ensure the discovered emails are active and deliverable, reducing bounce rates.
- **Composio-Powered Integration**
    - Seamlessly connects your AI agent to the Findymail API, enabling secure and reliable data retrieval.
- **CRM Data Sync**
    - Automatically maps discovered contact information back to your CRM, keeping your lead profiles up-to-date.
- **Intelligent Error Handling**
    - Provides clear feedback when an email cannot be found or verified, allowing for manual intervention or alternative lead prioritization.

---

## Use Cases
**Lead List Enrichment**
- Automatically populate missing email fields in your CRM for newly imported lead lists.
- Enrich cold outreach campaigns with verified contact details to improve open and response rates.

**Outbound Sales Preparation**
- Quickly find the primary contact email for decision-makers at target accounts before initiating outreach.
- Validate existing lead data to ensure your sales sequences are targeting active and reachable prospects.

**Data Hygiene Maintenance**
- Periodically scan your lead database to identify and update outdated or invalid contact information.
- Ensure compliance with email marketing standards by filtering out unverified or potentially risky addresses.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Prospect Email Finder template from the solution library.
3. Connect your Findymail API credentials within the integration settings.
4. Ensure nodes are correctly mapped from Chat Input to the Agent and finally to the Composio Toolset.

### 2) Setup the Nodes
- **Chat Input**: Accepts the prospect's name and company domain.
- **Agent**: Processes the request and triggers the email search logic.
- **Composio Toolset**: Executes the Findymail API calls to fetch and verify data.
- **Chat Output**: Returns the verified email address or a status message if no email is found.

### 3) Run the Flow
Use the Playground to test your workflow with the following prompts:
- `Find the professional email address for John Doe at acme-corp.com`
- `Verify the contact email for Sarah Jenkins at tech-innovations.io`
- `Look up and validate the email for the CEO of global-logistics.com`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your data enrichment tasks.
- Use a model capable of structured data extraction.
- Instruct the agent to prioritize high-confidence email matches.
- Configure the agent to handle "not found" scenarios gracefully by informing the user.

### 2) Composio Toolset Node
- Provide your Findymail API key in the configuration panel.
- Set the connection scope to allow read-only access to email discovery endpoints.

### 3) Tool Availability
- **Findymail Search**: Primary tool for locating contact emails.
- **Email Validator**: Secondary tool for verifying the deliverability of discovered addresses.
- **Data Mapper**: Utility for formatting the output into your preferred CRM structure.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account profiles with deep firmographic data.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into target prospect accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
