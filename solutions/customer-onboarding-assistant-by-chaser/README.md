# Customer Onboarding Assistant (Uplizd) - Automate and streamline new customer account setup

## Summary
The Customer Onboarding Assistant is an intelligent Uplizd workflow designed to automate the manual friction associated with new client setup. By integrating directly with your CRM and communication platforms via the Composio Toolset, this agent ensures that account provisioning, welcome documentation, and stakeholder notifications are handled instantly. This solution provides a single source of truth for onboarding status, significantly increasing pipeline velocity and ensuring consistent data hygiene from the moment a deal is closed.

---

## Demo
![Customer Onboarding Assistant workflow showing automated CRM account creation and welcome email triggers](image.png)
**Alt text (SEO-ready):** Uplizd Customer Onboarding Assistant workflow automating CRM account creation, data sync, and welcome email triggers via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-Launch%20Solution-blue)](https://uplizd.ai/solutions/6df95c38-0a84-57a8-81e7-c6aa0b46f07f)

---

## Category
**Primary category:** Customer Success Operations
**Secondary tags:** onboarding, crm, automation, customer success, data sync, composio, ai workflow, account provisioning.
This solution bridges the gap between sales closure and customer success, ensuring seamless transitions through automated data orchestration.

---

## Who is this for?
This solution is designed for teams looking to eliminate manual data entry and reduce time-to-value for new clients.

*   **Customer Success Managers**
    *   Automate the creation of client profiles and project folders to focus on relationship building.
*   **Sales Operations Leads**
    *   Ensure data consistency across platforms by syncing closed-won deal details into onboarding systems.
*   **Account Executives**
    *   Trigger automated welcome sequences immediately upon deal closure without manual intervention.
*   **Implementation Specialists**
    *   Standardize the onboarding checklist and initial communication touchpoints for every new account.

---

## Features
- **Automated Account Provisioning**
    Trigger account creation in your CRM or project management tools the moment a deal status changes to 'Closed-Won'.
- **Dynamic Welcome Sequences**
    Automatically draft and send personalized welcome emails and resource links based on the specific product tier or industry of the customer.
- **Cross-Platform Data Sync**
    Maintain data integrity by syncing customer contact information and deal metadata across your tech stack using the Composio Toolset.
- **Real-Time Status Tracking**
    Update internal dashboards and notify relevant stakeholders via Slack or email as onboarding milestones are completed.
- **Intelligent Error Handling**
    Identify and flag missing account data or configuration conflicts, allowing the agent to request missing information from the sales team.

---

## Use Cases
**Automated Account Setup**
*   Automatically create a new project workspace in your management tool when a deal is marked as won.
*   Populate client contact fields in your CRM based on the information provided during the sales process.

**Client Communication**
*   Send a personalized welcome email including onboarding documentation and scheduling links for the kickoff call.
*   Trigger internal notifications to the assigned account manager with a summary of the client's specific needs and pain points.

**Data Hygiene & Sync**
*   Map custom fields from your CRM to your onboarding platform to ensure consistent data across the entire customer lifecycle.
*   Archive outdated lead data once the onboarding process is successfully initiated to keep your pipeline clean.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Authenticate your required CRM and communication tool connections within the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are saved before activating the flow.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event (e.g., "New deal closed" or manual request).
*   **Agent**: Processes the customer data and determines the necessary onboarding steps.
*   **Composio Toolset**: Executes the API calls to create accounts, send emails, and update records.
*   **Chat Output**: Confirms successful onboarding initiation and logs any required follow-up actions.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these example prompts:
*   `Initiate onboarding for the new account 'Acme Corp' closed by John Doe.`
*   `Check if all required fields are present for the latest closed-won deal and trigger the welcome sequence.`
*   `Sync the contact details for the new onboarding project 'Beta Inc' to the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your onboarding logic.
*   Use a high-reasoning model to ensure accurate mapping of CRM fields.
*   Provide clear instructions on how to handle missing data (e.g., "If email is missing, notify the sales owner").
*   Define the tone for all automated client-facing communications.

### 2) Composio Toolset Node
*   Ensure your API keys for the CRM (e.g., Salesforce, HubSpot) and communication tools are active.
*   Set the connection scope to allow 'Read' and 'Write' access for account and contact objects.

### 3) Tool Availability
*   **CRM Connectors**: Create, Update, and Retrieve account/contact records.
*   **Email/Notification Tools**: Send automated welcome emails and internal alerts.
*   **Project Management Tools**: Create folders, projects, or tasks for new client onboarding.

---

## Related Solutions
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize customer data across multiple platforms to maintain a single source of truth.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and automate follow-ups for high-velocity sales teams.
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Clean up and standardize CRM data to ensure accurate reporting and onboarding.
