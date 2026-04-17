# Roommate Expense Tracker (Uplizd) - Automate shared household expense management

## Summary
The Roommate Expense Tracker by Uplizd is an intelligent AI workflow that automates the logging, categorization, and reconciliation of shared household expenses. By integrating with Splitwise, this solution eliminates manual spreadsheet tracking, reduces friction in roommate financial disputes, and ensures a single source of truth for all recurring and one-time household costs.

---

## Demo
![Uplizd AI workflow dashboard showing automated expense logging and Splitwise integration](image.png)
**Alt text (SEO-ready):** Uplizd Roommate Expense Tracker workflow dashboard showing automated expense logging, Splitwise integration, and financial reconciliation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/53c9c2f2-94e2-53d6-a8b6-e4f534820ee9)

---

## Category
**Primary category:** Finance
**Secondary tags:** personal finance, splitwise, expense tracking, household management, automation, ai workflow, composio, budget management.
This solution streamlines personal finance operations by bridging the gap between daily household spending and automated ledger updates.

---

## Who is this for?
This workflow is designed for individuals and groups looking to remove the administrative burden of shared living expenses.

* **Roommates**
    * Automatically split utility bills and rent without manual calculations.
* **Household Managers**
    * Maintain a transparent record of shared purchases to ensure equitable cost distribution.
* **Budget-Conscious Individuals**
    * Track personal spending patterns alongside shared obligations for better financial health.
* **Busy Professionals**
    * Reduce time spent on financial reconciliation through automated expense logging.

---

## Features
- **Automated Expense Logging**
  Instantly record new expenses via natural language input, which the agent parses and pushes directly to your Splitwise account.
- **Smart Categorization**
  Utilizes AI to automatically assign expenses to relevant categories like 'Utilities', 'Groceries', or 'Rent' based on transaction descriptions.
- **Real-time Reconciliation**
  Syncs with Splitwise to provide up-to-date balances, ensuring all roommates know exactly who owes what at any given moment.
- **Recurring Payment Handling**
  Configures automated reminders for recurring monthly bills, preventing missed payments and late fees.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely connect with the Splitwise API, ensuring reliable and authenticated data transfers.

---

## Use Cases
**Shared Utility Management**
* Automatically log monthly electricity and water bills as soon as the invoice arrives in your email.
* Split recurring internet and streaming service subscriptions equally among all household members.

**Grocery and Supply Tracking**
* Log individual grocery runs and attribute costs to specific roommates based on shared shopping lists.
* Generate monthly summaries of household supply spending to identify potential cost-saving opportunities.

**One-time Expense Reconciliation**
* Quickly log shared purchases like furniture or cleaning supplies to ensure immediate reimbursement.
* Resolve disputes by providing a clear, timestamped audit trail of all logged expenses within the workflow.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import Flow" to add the Roommate Expense Tracker to your Uplizd workspace.
3. Authenticate your Splitwise account via the Composio connection prompt.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input:** Receives the expense details or query from the user.
* **Agent:** Processes the natural language input to extract amount, category, and payee.
* **Composio Toolset:** Executes the API calls to update the Splitwise ledger.
* **Chat Output:** Confirms the successful logging of the expense or provides the requested balance summary.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Log a new expense of $45 for electricity under the Utilities category.`
* `What is the current balance I owe to my roommates?`
* `Show me the total household spending for the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the financial assistant responsible for interpreting user intent and structuring data for the API.
* Use a model capable of high-precision entity extraction (e.g., GPT-4o).
* Instruction: "You are a helpful financial assistant. Extract the amount, category, and description from the user input."
* Instruction: "Always confirm the details with the user before finalizing the transaction in Splitwise."

### 2) Composio Toolset Node
* Provide your Splitwise API key within the Composio dashboard.
* Ensure the connection scope includes read/write access to expenses and group balances.

### 3) Tool Availability
* `splitwise_create_expense`: Adds new line items to the ledger.
* `splitwise_get_balances`: Retrieves current debt/credit status for the user.
* `splitwise_list_expenses`: Fetches historical data for reporting and analysis.

---

## Related Solutions
* [Account Reconciliation Helper by QuickBooks](../account-reconciliation-helper-by-quickbooks/README.md) — Automate financial ledger reconciliation and bank feed management.
* [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline complex operational workflows and task management.
* [Workspace Usage Analyzer by Baserow](../workspace-usage-analyzer-by-baserow/README.md) — Track and analyze resource allocation and usage metrics.
