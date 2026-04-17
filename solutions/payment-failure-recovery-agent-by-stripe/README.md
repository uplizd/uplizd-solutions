# Payment Failure Recovery Agent (Uplizd) - Automated Stripe payment recovery and churn reduction

## Summary
The Payment Failure Recovery Agent is an intelligent Uplizd workflow designed to minimize revenue leakage by automating the recovery of failed transactions. By integrating directly with Stripe via the Composio Toolset, the agent identifies declined payments, proactively notifies customers, and guides them through secure payment method updates, ensuring higher subscription retention and improved pipeline velocity for finance and operations teams.

---

## Demo
![Payment Failure Recovery Agent workflow diagram showing Stripe integration and customer notification flow](image.png)
**Alt text (SEO-ready):** Payment Failure Recovery Agent (Uplizd) workflow diagram showing automated Stripe payment retry logic and customer communication integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9c2e7b73-3968-5a13-9b3c-92bf10045eeb)

---

## Category
- **Primary category:** Finance operations
- **Secondary tags:** stripe, payment recovery, churn reduction, revenue operations, automated billing, composio, ai workflow, dunning management
- This solution streamlines the dunning process by automating the bridge between failed payment events and successful customer resolution.

---

## Who is this for?
This workflow is designed for teams focused on maintaining recurring revenue and optimizing customer billing lifecycles.

- **Finance Manager**
    - Reduces manual dunning efforts and minimizes revenue loss from expired or declined cards.
- **Customer Success Lead**
    - Proactively resolves billing friction to prevent unnecessary churn and maintain positive account relationships.
- **RevOps Specialist**
    - Ensures data hygiene across payment platforms by automating the synchronization of payment status updates.
- **Billing Administrator**
    - Gains real-time visibility into payment failure patterns and accelerates the resolution of high-value account issues.

---

## Features
- **Automated Failure Detection**
    - Instantly identifies failed Stripe transactions and triggers recovery workflows without manual intervention.
- **Intelligent Retry Logic**
    - Executes smart retry attempts based on failure codes to maximize recovery rates while respecting payment gateway limits.
- **Customer Communication Automation**
    - Generates and sends personalized, secure links to customers for updating payment methods, reducing friction in the recovery process.
- **Real-time Sync**
    - Updates account statuses across your CRM and billing systems immediately upon successful payment resolution.
- **Audit-Ready Reporting**
    - Maintains a detailed log of all recovery attempts, communications, and successful updates for financial compliance.

---

## Use Cases
**Proactive Dunning Management**
- Automatically trigger email sequences for customers with expired credit cards 7 days before subscription renewal.
- Escalate high-value account payment failures to a dedicated account manager for manual outreach.

**Revenue Recovery Optimization**
- Analyze common failure codes to identify and resolve systemic billing issues or regional payment gateway blocks.
- Sync successful payment recoveries back to the CRM to update account health scores and pipeline forecasting.

**Customer Experience Enhancement**
- Provide self-service payment update portals to customers via automated chat or email notifications.
- Reduce support ticket volume by resolving routine payment failures through autonomous agent intervention.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your workspace.
2. Connect your Stripe account via the Composio Toolset integration.
3. Configure your notification channels (e.g., Email or Slack) to alert customers.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event from Stripe or manual request.
- **Agent**: Analyzes the failure reason and determines the appropriate recovery action.
- **Composio Toolset**: Executes API calls to Stripe to update payment records or verify status.
- **Chat Output**: Confirms the recovery action taken or logs the outcome for the user.

### 3) Run the Flow
Use the Playground to test the recovery agent with these prompts:
- `Check for failed payments in the last 24 hours and initiate recovery for high-value accounts.`
- `List all customers with expired payment methods and send a reminder to update their billing info.`
- `Verify the status of the latest payment attempt for customer_id_12345 and retry if the error is transient.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial operations assistant, prioritizing accuracy and security.
- Use a model capable of structured data extraction (e.g., GPT-4o).
- Instruction: "You are a payment recovery expert. Always verify the error code before suggesting a retry."
- Instruction: "Maintain a professional, helpful tone when drafting customer communications."

### 2) Composio Toolset Node
- Provide your Stripe API Key with `read_write` access to `subscriptions` and `customers`.
- Ensure the connection scope includes `payment_intents` and `invoices` to allow the agent to perform updates.

### 3) Tool Availability
- **Stripe List Invoices**: Retrieve pending or failed invoice data.
- **Stripe Update Payment Method**: Securely update customer billing details.
- **Stripe Retry Payment**: Trigger a new attempt for failed payment intents.
- **CRM Update**: Sync recovery status back to your primary customer database.

---

## Related Solutions
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automate ledger balancing and financial data matching.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track customer engagement to predict and prevent churn.
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Recover lost sales through automated marketing and outreach.
