# Friendly Payment Reminder Agent (Uplizd) - Automate overdue payment collections and improve cash flow

## Summary
The Friendly Payment Reminder Agent is an intelligent Uplizd workflow designed to automate the outreach process for outstanding invoices. By integrating directly with your accounting and communication platforms, this agent identifies overdue accounts, drafts personalized, empathetic payment reminders, and triggers delivery, helping finance teams reduce Days Sales Outstanding (DSO) while maintaining positive client relationships.

---

## Demo
![Friendly Payment Reminder Agent workflow interface showing invoice data processing and automated email dispatch](image.png)
**Alt text (SEO-ready):** Friendly Payment Reminder Agent workflow interface showing invoice data processing and automated email dispatch via Uplizd, CRM integrations, and Composio toolsets.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/2a35d20e-3a83-5265-914a-c3ef17a506d7)

---

## Category
**Primary category:** Finance
**Secondary tags:** crm, accounting, payment automation, dso reduction, customer success, collections, composio, ai workflow
This solution streamlines the accounts receivable process by bridging the gap between financial data and client communication channels.

---

## Who is this for?
This agent is built for finance and operations teams looking to reclaim time spent on manual collections.

*   **Accounts Receivable Specialist**
    *   Automates the repetitive task of identifying and emailing clients with overdue balances.
*   **Finance Manager**
    *   Ensures consistent follow-up cadences to improve cash flow and reduce bad debt.
*   **Customer Success Manager**
    *   Maintains healthy client relationships by sending polite, branded reminders rather than aggressive notices.
*   **Operations Lead**
    *   Integrates payment tracking directly into existing CRM and communication workflows for full visibility.

---

## Features
- **Automated Invoice Scanning**
    Real-time monitoring of accounting software to identify invoices that have passed their due date.
- **Personalized Outreach**
    Generates context-aware, empathetic email templates that reference specific invoice numbers and amounts.
- **Multi-Channel Delivery**
    Seamlessly routes reminders through email or messaging platforms like WhatsApp or Slack using the Composio Toolset.
- **Escalation Logic**
    Automatically adjusts the tone and frequency of reminders based on the number of days an invoice is past due.
- **Audit Trail Logging**
    Records every interaction and reminder sent, providing a clear history for internal reporting and compliance.

---

## Use Cases
**Proactive Collections**
*   Send a "friendly nudge" email 3 days before an invoice is due to ensure the client has the necessary documentation.
*   Trigger an automated follow-up immediately upon the first day of delinquency to prevent further delays.

**Relationship Management**
*   Draft personalized messages that acknowledge the client's history and offer assistance if they are experiencing payment issues.
*   Pause automated reminders if a client has an active support ticket or a pre-arranged payment plan in the CRM.

**Operational Efficiency**
*   Sync overdue status across your CRM and accounting platforms to ensure all stakeholders have a single source of truth.
*   Generate weekly summaries of collection performance to identify trends in payment behavior across different client segments.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Friendly Payment Reminder Agent.
2. Click "Import" to add the workflow to your workspace.
3. Connect your required accounting and communication accounts via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific CRM and email provider credentials.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal from your accounting software or a manual request.
*   **Agent**: Processes the invoice data and determines the appropriate tone and message content.
*   **Composio Toolset**: Executes the retrieval of invoice details and the dispatch of the communication.
*   **Chat Output**: Confirms the successful delivery of the reminder and logs the action.

### 3) Run the Flow
*   `Check for all invoices overdue by more than 30 days and send a polite reminder to the primary contact.`
*   `Draft a follow-up email for client ID 8842 regarding invoice INV-2023-001.`
*   `Summarize all payment reminders sent this week and update the status in the CRM.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a professional, empathetic financial assistant.
*   Maintain a polite, helpful, and firm tone.
*   Always include the specific invoice number, due date, and outstanding balance.
*   Provide clear instructions on how the client can make a payment or contact support.

### 2) Composio Toolset Node
Requires an active API key with read/write access to your accounting platform (e.g., QuickBooks, Xero) and your communication platform (e.g., Gmail, Outlook, WhatsApp).

### 3) Tool Availability
*   **Accounting Fetcher**: Retrieve invoice status and client contact details.
*   **Email/Messaging Sender**: Dispatch communications to the identified client.
*   **CRM Updater**: Log the interaction history and update the payment status field.

---

## Related Solutions
*   [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate the matching of payments to open invoices.
*   [Affiliate Payment Automation Agent](../affiliate-payment-automation-agent-by-tapfiliate/README.md) - Streamline payouts for affiliate partners.
*   [WhatsApp Order Status Agent](../whats-app-order-status-agent-by-whatsapp/README.md) - Provide real-time updates on order and payment status via WhatsApp.
