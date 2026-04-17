# Invoice Payment Tracker (Uplizd) - Automate overdue invoice monitoring and collection

## Summary
The Invoice Payment Tracker by Uplizd is an intelligent automation workflow designed to monitor financial records, identify overdue payments, and trigger proactive follow-up communications. By integrating directly with Zoho Invoice via the Composio Toolset, this solution eliminates manual tracking, reduces Days Sales Outstanding (DSO), and ensures consistent cash flow management for finance and operations teams.

---

## Demo
![Invoice Payment Tracker workflow dashboard showing automated overdue invoice detection and follow-up triggers](image.png)
**Alt text (SEO-ready):** Uplizd Invoice Payment Tracker workflow for Zoho Invoice, automating overdue payment detection, financial data synchronization, and automated collection outreach.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8d3bc26a-c75c-5b34-b37e-1e4cc948276f)

---

## Category
*   **Primary category:** Finance
*   **Secondary tags:** zoho invoice, accounts receivable, payment tracking, dso reduction, finance automation, cash flow, composio, ai workflow
*   This solution streamlines the accounts receivable lifecycle by bridging the gap between financial data platforms and automated communication channels.

---

## Who is this for?
This solution is designed for finance professionals and operations managers who need to maintain healthy cash flow without manual intervention.

*   **Accounts Receivable Specialist**
    *   Automates the identification of delinquent accounts to prioritize collection efforts.
*   **Finance Manager**
    *   Provides real-time visibility into payment status and reduces manual reporting overhead.
*   **Small Business Owner**
    *   Ensures consistent follow-up with clients to improve overall business liquidity.
*   **Operations Coordinator**
    *   Syncs payment status updates across internal systems to maintain a single source of truth.

---

## Features
- **Automated Overdue Detection**
  Real-time monitoring of invoice due dates to instantly flag payments that have passed their grace period.
- **Zoho Invoice Integration**
  Seamless connectivity via the Composio Toolset to fetch, update, and manage invoice records directly within the workflow.
- **Proactive Collection Logic**
  Intelligent triggers that initiate follow-up actions based on the severity of the payment delay.
- **Customizable Communication Templates**
  Dynamic generation of professional payment reminders tailored to the specific client and invoice context.
- **Audit-Ready Reporting**
  Maintains a clean log of all payment status changes and follow-up attempts for financial compliance.

---

## Use Cases
**Accounts Receivable Management**
*   Automatically flagging invoices that are 30+ days overdue for immediate review.
*   Syncing payment status updates from Zoho Invoice to internal CRM dashboards.

**Client Communication**
*   Sending automated, personalized email reminders to clients with outstanding balances.
*   Escalating high-value overdue invoices to human account managers for personalized outreach.

**Financial Reporting**
*   Generating weekly summaries of total outstanding receivables to assist in cash flow forecasting.
*   Reconciling partial payments against total invoice amounts to ensure accurate balance tracking.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Invoice Payment Tracker template using the provided solution link.
3. Authenticate your Zoho Invoice account within the Composio Toolset configuration.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger command or schedule signal to initiate the invoice scan.
*   **Agent**: Processes the invoice data and determines the appropriate follow-up action based on payment status.
*   **Composio Toolset**: Executes API calls to Zoho Invoice to retrieve invoice details and update payment records.
*   **Chat Output**: Delivers a summary report of the scan results and actions taken to the user.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
* `Check for all invoices overdue by more than 15 days and list them.`
* `Identify high-value overdue invoices and draft a polite follow-up email for each.`
* `Sync the latest payment status from Zoho Invoice and update the dashboard.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the financial logic engine, interpreting invoice data and determining the next best action.
*   Prioritize accuracy in identifying due dates and client contact information.
*   Maintain a professional and firm tone for all generated collection communications.
*   Ensure all data updates are mapped correctly to the corresponding invoice IDs.

### 2) Composio Toolset Node
*   **API Key**: Provide your Zoho Invoice API credentials within the secure configuration tab.
*   **Connection Scope**: Ensure the toolset has read/write permissions for "Invoices," "Contacts," and "Payments."

### 3) Tool Availability
*   `get_invoice_details`: Fetches specific invoice data including due date and balance.
*   `list_overdue_invoices`: Filters and retrieves a list of all unpaid invoices past their due date.
*   `update_invoice_status`: Marks invoices as 'Followed Up' or 'Paid' based on agent logic.
*   `send_email_reminder`: Dispatches automated collection emails to the client contact.

---

## Related Solutions
* [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate the matching of bank transactions to internal ledger entries.
* [Affiliate Payment Automation Agent](../affiliate-payment-automation-agent-by-tapfiliate/README.md) - Streamline the calculation and disbursement of affiliate commissions.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track customer usage metrics to prevent churn and identify upsell opportunities.
