# Bitcoin Payment Request Manager (Uplizd) - Automated Crypto Invoice Generation and Tracking

## Summary
The Bitcoin Payment Request Manager is an intelligent Uplizd workflow that automates the creation, issuance, and status tracking of Bitcoin invoices via BTCPay Server. By integrating directly with your payment infrastructure, this solution eliminates manual billing errors, ensures real-time payment verification, and provides a single source of truth for financial operations, significantly increasing pipeline velocity for crypto-native businesses.

---

## Demo
![Bitcoin Payment Request Manager workflow interface showing invoice creation and status tracking nodes](image.png)
**Alt text (SEO-ready):** Bitcoin Payment Request Manager Uplizd workflow, automated crypto billing, BTCPay Server invoice generation, and real-time payment tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e9dc0cc8-360d-58eb-9057-923f743b7ce3)

---

## Category
**Primary category:** Finance
**Secondary tags:** bitcoin, btcpay server, crypto payments, invoice automation, financial operations, payment tracking, composio, ai workflow.
This solution streamlines financial operations by automating the lifecycle of Bitcoin payment requests through secure API integrations.

---

## Who is this for?
This solution is designed for finance and operations teams looking to modernize their crypto-payment infrastructure.

*   **Finance Manager**
    *   Automate reconciliation processes and reduce manual entry errors for incoming crypto payments.
*   **E-commerce Operations Lead**
    *   Enable seamless checkout experiences by generating instant, verifiable payment requests for customers.
*   **Developer/Systems Architect**
    *   Integrate complex BTCPay Server functionality into business workflows without building custom middleware.
*   **Sales Operations Specialist**
    *   Track deal payment status in real-time to trigger automated follow-ups or service provisioning.

---

## Features
- **Automated Invoice Generation**
    Create precise Bitcoin payment requests instantly based on order details or customer inputs.
- **Real-time Payment Verification**
    Automatically monitor the blockchain via BTCPay Server to confirm transaction status without manual polling.
- **Unified Payment Dashboard**
    Centralize all payment request data within your existing business logic for easier reporting and auditing.
- **Error-Free Billing**
    Eliminate human error in address generation and amount calculation by leveraging programmatic API calls.
- **Seamless Composio Integration**
    Utilize the Composio Toolset to securely connect the AI agent to your BTCPay Server instance with granular scope control.

---

## Use Cases
**Payment Processing**
*   Automatically generate unique Bitcoin invoices for new customer orders.
*   Trigger service activation immediately upon receipt of a confirmed transaction.

**Financial Reconciliation**
*   Sync payment status updates directly to your internal ledger or CRM.
*   Generate daily reports on pending versus completed crypto transactions.

**Customer Support & Billing**
*   Provide customers with instant payment links via automated chat responses.
*   Resolve billing inquiries by fetching real-time invoice status from the BTCPay Server API.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your BTCPay Server connection via the Composio Toolset.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input:** Receives the customer order details or payment request parameters.
*   **Agent:** Processes the intent and determines the necessary BTCPay Server action.
*   **Composio Toolset:** Executes the API calls to create or fetch invoice data.
*   **Chat Output:** Returns the payment link or status update to the user.

### 3) Run the Flow
Use the Playground to test your integration with these prompts:
* `Create a new Bitcoin invoice for 0.05 BTC for order #12345.`
* `Check the payment status of invoice ID: BTC-INV-9988.`
* `List all pending Bitcoin payment requests from the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between user intent and the payment gateway.
*   Use a high-reasoning model (e.g., GPT-4o) for accurate API parameter extraction.
*   Ensure the system prompt explicitly defines the required invoice fields (amount, currency, order ID).
*   Enable tool-calling capabilities to allow the agent to invoke Composio functions dynamically.

### 2) Composio Toolset Node
*   Connect your BTCPay Server API key within the Composio dashboard.
*   Set the connection scope to include `invoices:create` and `invoices:read` permissions.

### 3) Tool Availability
*   `create_invoice`: Generates a new payment request.
*   `get_invoice_status`: Retrieves real-time confirmation status.
*   `list_invoices`: Fetches historical payment data for reporting.

---

## Related Solutions
* [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automate financial ledger updates and account balancing.
* [Affiliate Payment Automation Agent](../affiliate-payment-automation-agent-by-tapfiliate/README.md) - Streamline commission payouts and payment tracking.
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Connect business processes with automated task management.
