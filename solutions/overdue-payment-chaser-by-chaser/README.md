# Overdue Payment Chaser (Uplizd) - Automated AR recovery and personalized payment follow-ups

## Summary
The Overdue Payment Chaser by Uplizd is an intelligent AI workflow designed to automate the accounts receivable process by identifying outstanding invoices and triggering personalized, empathetic follow-up communications. By leveraging the Composio Toolset to integrate with your financial platforms, this solution reduces manual outreach, improves cash flow velocity, and maintains professional client relationships through timely, data-driven reminders.

---

## Demo
![Overdue Payment Chaser workflow diagram showing invoice identification, status check, and automated communication steps](image.png)
**Alt text (SEO-ready):** Uplizd Overdue Payment Chaser workflow automation, CRM and accounting integration, automated accounts receivable follow-ups, and payment recovery AI agent.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b94941b3-4f74-5789-9f84-3964abf78fe6)

---

## Category
- **Primary category:** Finance
- **Secondary tags:** accounts receivable, payment recovery, automation, crm, financial operations, debt collection, composio, ai workflow
- This solution streamlines financial operations by bridging the gap between accounting data and client communication channels.

---

## Who is this for?
This solution is designed for finance and operations teams looking to minimize manual collection efforts while maintaining high customer satisfaction.

- **Accounts Receivable Manager**
    - Automates the identification of overdue accounts to ensure no invoice is missed.
- **Finance Operations Lead**
    - Reduces the time spent on manual dunning processes and status reporting.
- **Customer Success Manager**
    - Ensures payment reminders are personalized and empathetic to preserve client relationships.
- **Small Business Owner**
    - Improves cash flow predictability without needing a dedicated collections department.

---

## Features
- **Automated Invoice Monitoring**
    - Real-time scanning of accounting platforms to detect invoices past their due date.
- **Personalized Communication Engine**
    - Generates context-aware, professional follow-up messages based on the specific client history.
- **Multi-Channel Integration**
    - Seamlessly connects with email and messaging platforms via the Composio Toolset to deliver reminders.
- **Escalation Logic**
    - Configurable triggers that adjust the tone and frequency of follow-ups based on the duration of the delay.
- **Audit Trail Logging**
    - Maintains a comprehensive record of all sent communications and payment status updates for compliance.

---

## Use Cases
**Proactive Payment Reminders**
- Send automated "friendly reminders" three days before an invoice is due to ensure timely processing.
- Trigger immediate notifications for invoices that have crossed the 30-day overdue threshold.

**Client Relationship Management**
- Filter out high-value or sensitive accounts from automated flows to allow for manual, high-touch intervention.
- Adjust communication tone based on the client's past payment behavior and current account health.

**Operational Efficiency**
- Sync overdue status updates directly back to your CRM to keep sales and support teams informed.
- Generate weekly summary reports of recovered payments and outstanding balances for management review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your dashboard.
2. Connect your preferred accounting and communication tools via the Composio Toolset.
3. Configure your specific invoice threshold settings and notification templates.
4. Ensure nodes are correctly mapped and all API credentials are authenticated before activating.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled batch requests for invoice checks.
- **Agent**: Analyzes invoice data and determines the appropriate follow-up action.
- **Composio Toolset**: Executes the retrieval of invoice data and the dispatch of messages.
- **Chat Output**: Confirms the status of the outreach and logs the action taken.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Check for all invoices overdue by more than 15 days and draft a reminder email for each.`
- `List all clients with outstanding payments over $5,000 and notify the finance team.`
- `Send a final notice to client ID 9928 and update the status in the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial communications assistant, prioritizing clarity and professionalism.
- Use a model with strong reasoning capabilities to interpret invoice aging reports.
- Instruction: Maintain a professional, firm, yet helpful tone in all communications.
- Instruction: Always verify the invoice amount and due date against the source data before sending.

### 2) Composio Toolset Node
- Provide your API key for the relevant accounting software (e.g., QuickBooks, Xero).
- Ensure the connection scope includes read access for invoices and write access for communication channels.

### 3) Tool Availability
- **Accounting API**: For fetching invoice status, client contact details, and balance information.
- **Email/Messaging API**: For drafting and sending payment reminders.
- **CRM Connector**: For updating client records with interaction history.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automate the matching of payments to invoices.
- [Affiliate Payment Automation Agent](../affiliate-payment-automation-agent-by-tapfiliate/README.md) — Manage and automate outgoing affiliate payouts.
- [Work Order Status Tracker](../work-order-status-tracker-by-maintainx/README.md) — Monitor and update status-based financial workflows.
