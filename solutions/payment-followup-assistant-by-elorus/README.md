# Payment Follow-up Assistant (Uplizd) - Automated invoice tracking and professional payment reminders

## Summary
The Payment Follow-up Assistant is an intelligent Uplizd workflow designed to streamline accounts receivable by automatically identifying overdue invoices and drafting professional, empathetic payment reminders. By integrating directly with your accounting platform via the Composio Toolset, this solution eliminates manual tracking, reduces DSO (Days Sales Outstanding), and maintains healthy client relationships through timely, automated communication.

---

## Demo
![Payment Follow-up Assistant workflow dashboard showing invoice tracking and automated email triggers](image.png)
**Alt text (SEO-ready):** Payment Follow-up Assistant (Uplizd) workflow dashboard showing automated invoice tracking, overdue payment detection, and email reminder triggers using the Composio Toolset.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1eeb402a-6206-5252-8fde-8357fd34f50c)

---

## Category
**Primary category:** Finance
**Secondary tags:** `accounts receivable`, `invoicing`, `payment reminders`, `automation`, `elorus`, `composio`, `ai workflow`, `cash flow`
This solution bridges the gap between accounting data and client communication to optimize cash flow management.

---

## Who is this for?
This solution is built for finance teams and business owners looking to automate the tedious process of chasing late payments.

*   **Finance Managers**
    *   Gain real-time visibility into overdue accounts and reduce manual reconciliation time.
*   **Small Business Owners**
    *   Maintain professional client relationships without needing a dedicated collections department.
*   **Accountants**
    *   Ensure consistent follow-up cadences across all client invoices to improve overall cash flow.
*   **Operations Leads**
    *   Standardize communication templates to ensure brand consistency and compliance in payment requests.

---

## Features
- **Automated Overdue Detection**
    Real-time monitoring of invoice statuses to trigger follow-ups the moment a payment deadline passes.
- **Intelligent Reminder Drafting**
    AI-generated, context-aware email drafts that adjust tone based on the severity of the delay.
- **Seamless Accounting Integration**
    Direct connectivity with Elorus and other accounting platforms via the Composio Toolset for instant data retrieval.
- **Customizable Follow-up Cadence**
    Flexible scheduling logic that allows for tiered reminders, from friendly nudges to formal notices.
- **Audit Trail Logging**
    Comprehensive tracking of all sent reminders and client interactions within the workflow history.

---

## Use Cases
**Proactive Cash Flow Management**
*   Automatically flag invoices that are 1–7 days past due for a gentle reminder.
*   Sync payment status updates back to your CRM to keep sales teams informed of client account health.

**Client Relationship Preservation**
*   Use AI to soften the tone of early-stage reminders to maintain positive long-term partnerships.
*   Personalize email content by pulling specific project or invoice line-item details into the message body.

**Operational Efficiency**
*   Reduce the time spent manually checking accounting dashboards by receiving daily summaries of pending payments.
*   Automate the escalation path for invoices that remain unpaid after multiple automated attempts.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace to import the pre-configured workflow nodes.
3. Authenticate your accounting platform (e.g., Elorus) within the Composio Toolset.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual request to scan for overdue invoices.
*   **Agent**: Processes invoice data and determines the appropriate follow-up action.
*   **Composio Toolset**: Executes API calls to fetch invoice details and send communication.
*   **Chat Output**: Delivers the summary of actions taken or drafts for final review.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
*   `"Check for all invoices overdue by more than 15 days and draft a formal reminder."`
*   `"List all pending payments for client 'Acme Corp' and identify if any are past due."`
*   `"Send a friendly follow-up email for invoice #INV-1024 that is currently 3 days late."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for identifying payment status and drafting communications.
*   Instruct the agent to prioritize professional, non-confrontational language.
*   Ensure the agent is configured to extract invoice numbers, client names, and due dates accurately.
*   Set a temperature of 0.2 to maintain consistency in financial reporting and email generation.

### 2) Composio Toolset Node
*   **API Key**: Provide your Elorus or accounting platform API key in the secure credential manager.
*   **Connection Scope**: Ensure the toolset has read access to 'Invoices' and write access to 'Email/Messaging' services.

### 3) Tool Availability
*   `get_overdue_invoices`: Fetches a list of invoices past their due date.
*   `get_client_contact_info`: Retrieves email addresses associated with specific client accounts.
*   `send_email_reminder`: Dispatches the AI-generated follow-up message.

---

## Related Solutions
*   [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate the matching of bank transactions to invoices.
*   [Affiliate Payment Automation Agent](../affiliate-payment-automation-agent-by-tapfiliate/README.md) - Streamline outgoing payments to partners and affiliates.
*   [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for managing business process lifecycles.
