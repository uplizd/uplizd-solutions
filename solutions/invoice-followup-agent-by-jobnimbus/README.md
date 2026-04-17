# Invoice Follow-up Agent (Uplizd) - Automate overdue invoice tracking and client communications

## Summary
The Invoice Follow-up Agent is an intelligent Uplizd workflow designed to streamline accounts receivable by automating the identification of overdue invoices and the orchestration of personalized client follow-ups. By integrating directly with JobNimbus, this solution reduces manual administrative overhead, accelerates cash flow, and ensures consistent communication hygiene, providing a single source of truth for your billing pipeline.

---

## Demo
![Invoice Follow-up Agent workflow diagram showing JobNimbus integration for automated billing reminders](image.png)

**Alt text (SEO-ready):** Invoice Follow-up Agent workflow for JobNimbus, automating overdue invoice tracking, client communication, and billing pipeline management via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/23595797-c46c-5ea7-aaca-69a4781d9534)

---

## Category
- **Primary category:** Finance
- **Secondary tags:** jobnimbus, accounts receivable, billing, invoice tracking, automation, composio, ai workflow, cash flow
- This solution bridges the gap between financial data in JobNimbus and proactive client engagement to improve collection efficiency.

---

## Who is this for?
This solution is designed for finance and operations teams looking to reclaim time spent on manual collections.

- **Finance Manager**
    - Automates the identification of high-risk overdue accounts to prioritize collection efforts.
- **Operations Coordinator**
    - Standardizes communication templates to ensure professional and timely follow-ups across all clients.
- **Account Executive**
    - Maintains visibility into client billing status without needing to manually check the CRM.
- **Business Owner**
    - Improves overall cash flow velocity by reducing the time between invoice due dates and final payment.

---

## Features
- **Automated Invoice Scanning**
    - Continuously monitors JobNimbus for invoices that have passed their due date.
- **Intelligent Communication Drafting**
    - Uses AI to generate personalized, empathetic follow-up messages based on the specific delay duration.
- **Composio-Powered CRM Integration**
    - Leverages the Composio Toolset to securely read invoice data and update client records in real-time.
- **Customizable Escalation Logic**
    - Allows for tiered follow-up strategies, from friendly reminders to formal overdue notices.
- **Centralized Activity Logging**
    - Automatically logs all sent communications back into the JobNimbus client activity feed for auditability.

---

## Use Cases
**Proactive Billing Management**
- Automatically trigger a "friendly reminder" email 3 days before an invoice is due.
- Identify invoices that are 30+ days past due and flag them for immediate manual review.

**Client Relationship Preservation**
- Tailor follow-up tone based on the client's historical payment performance and project status.
- Ensure that automated messages are paused if a client has already initiated a support ticket regarding the invoice.

**Operational Efficiency**
- Sync payment status updates from external gateways back to JobNimbus without manual data entry.
- Generate weekly summaries of outstanding receivables for the finance department.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Authenticate your JobNimbus connection via the Composio Toolset node.
4. Ensure nodes are correctly mapped and all API credentials are saved in your environment variables.

### 2) Setup the Nodes
- **Chat Input:** Receives the trigger signal or manual request to scan for overdue invoices.
- **Agent:** Processes invoice data and determines the appropriate follow-up action based on the delay.
- **Composio Toolset:** Executes read/write operations within JobNimbus to fetch invoice details and send messages.
- **Chat Output:** Confirms the completion of the follow-up process and summarizes actions taken.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Scan for all invoices overdue by more than 15 days and draft follow-up emails.`
- `Check the status of invoice #INV-9928 and update the client record if payment is pending.`
- `Generate a summary report of all outstanding invoices for the current month.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial communications assistant that maintains a professional and firm tone.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a billing assistant. Always verify the invoice status in JobNimbus before drafting a message."
- Instruction: "Maintain a helpful tone for early reminders and a formal tone for overdue notices."

### 2) Composio Toolset Node
- Provide your JobNimbus API key within the Composio configuration.
- Ensure the connection scope includes `read:invoices` and `write:communications`.

### 3) Tool Availability
- `jobnimbus_get_invoices`: Fetches current billing data.
- `jobnimbus_update_client_note`: Logs follow-up actions.
- `jobnimbus_send_email`: Dispatches the drafted communication.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for JobNimbus workflows.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Streamline financial matching and reconciliation tasks.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track client engagement and health metrics.
