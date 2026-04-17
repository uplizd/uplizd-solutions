# Customer Case Manager (Uplizd) - Automated support ticket routing and prioritization

## Summary
The Customer Case Manager (Uplizd) workflow streamlines your support operations by automatically ingesting, categorizing, and routing customer inquiries to the appropriate internal teams. By leveraging the Composio Toolset to interface with Dynamics 365, this solution ensures that high-priority issues are addressed immediately, reducing response times and maintaining a single source of truth for all customer interactions.

---

## Demo
![Customer Case Manager workflow diagram showing intake, AI routing, and Dynamics 365 integration](image.png)
**Alt text (SEO-ready):** Customer Case Manager workflow diagram showing AI-powered support ticket intake, automated routing, and Dynamics 365 CRM integration on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-6fe71e3d-blue)](https://uplizd.ai/solutions/6fe71e3d-ce3c-532d-bd43-ac77ff89c62f)

---

## Category
- **Primary category:** Support automation
- **Secondary tags:** crm, dynamics365, support, ticketing, ai workflow, composio, case management, customer service
- This solution bridges the gap between raw customer feedback and structured CRM data to improve support team efficiency.

---

## Who is this for?
This solution is designed for support teams and operations managers looking to eliminate manual ticket triage.

- **Support Manager**
    - Automates the distribution of incoming tickets to balance team workload effectively.
- **Customer Success Lead**
    - Ensures high-value accounts receive priority attention through automated sentiment-based routing.
- **CRM Administrator**
    - Maintains data hygiene by ensuring all support cases are correctly logged and categorized in Dynamics 365.
- **Support Agent**
    - Reduces time spent on manual data entry and ticket classification, allowing for faster resolution times.

---

## Features
- **Intelligent Ticket Routing**
    - Automatically assigns incoming cases to the correct department based on issue type and urgency.
- **Dynamics 365 Integration**
    - Seamlessly creates and updates records in your CRM using the robust Composio Toolset.
- **Real-time Priority Scoring**
    - Analyzes incoming text to detect sentiment and urgency, escalating critical issues instantly.
- **Automated Data Enrichment**
    - Pulls relevant account history from Dynamics 365 to provide agents with full context upon ticket creation.
- **Workflow Transparency**
    - Provides a clear audit trail of every ticket from initial ingestion to final resolution.

---

## Use Cases
**Support Triage**
- Automatically route technical bugs to the engineering queue while directing billing inquiries to the finance team.
- Flag tickets containing negative sentiment for immediate review by a senior support lead.

**CRM Data Management**
- Sync email inquiries directly into Dynamics 365 as new Case entities with pre-filled subject lines.
- Update existing customer records with recent interaction summaries to keep the account history current.

**Efficiency Optimization**
- Reduce manual ticket tagging by using AI to categorize issues based on predefined product categories.
- Trigger automated follow-up tasks for agents when a case remains in a "Pending" state for over 24 hours.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import" option.
2. Upload the `customer-case-manager-by-dynamics365` workflow file.
3. Connect your Dynamics 365 account via the Composio integration settings.
4. Ensure nodes are correctly linked from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw customer inquiry text.
- **Agent**: Analyzes intent, extracts priority, and formats data for the CRM.
- **Composio Toolset**: Executes the creation or update of cases within Dynamics 365.
- **Chat Output**: Confirms the ticket creation and provides a summary to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Create a new high-priority case for customer 'Acme Corp' regarding a login failure.`
- `Analyze this email: 'I am unable to access my dashboard, please help' and create a support ticket.`
- `Update the status of case #12345 to 'In Progress' and assign it to the technical support team.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the operation, interpreting natural language and mapping it to CRM actions.
- **Instruction Pattern:**
    - Always extract the customer name, issue description, and urgency level from the input.
    - Use the Dynamics 365 toolset to verify if the customer exists before creating a case.
    - Maintain a professional and helpful tone in the final Chat Output confirmation.

### 2) Composio Toolset Node
- Requires a valid Dynamics 365 API key configured within the Composio platform.
- Ensure the connection scope includes read/write access to the `Cases` and `Accounts` entities.

### 3) Tool Availability
- `dynamics365_create_case`: Generates a new support ticket record.
- `dynamics365_get_account`: Retrieves account details for context enrichment.
- `dynamics365_update_case`: Modifies existing ticket status or priority.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) — General purpose AI support assistant for 24/7 coverage.
- [account-setup-agent-by-salesforce](../account-setup-agent-by-salesforce/README.md) — Automates account creation and onboarding workflows in Salesforce.
- [whats-app-support-ticket-manager-by-spoki](../whats-app-support-ticket-manager-by-spoki/README.md) — Manages support tickets specifically via WhatsApp channels.
