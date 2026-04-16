# Automated Expense Tracker (Uplizd) - Streamline business finance and receipt categorization

## Summary
The Automated Expense Tracker (Uplizd) is an intelligent AI workflow designed to automate the ingestion, categorization, and logging of business expenses directly into Google Sheets. By leveraging the Composio Toolset to bridge receipt data with spreadsheet management, this solution eliminates manual data entry, reduces human error in financial reporting, and ensures your team maintains a single source of truth for all operational expenditures.

---

## Demo
![Automated Expense Tracker workflow showing receipt ingestion, AI categorization, and Google Sheets logging](image.png)

**Alt text (SEO-ready):** Automated Expense Tracker workflow using Uplizd, AI-driven receipt categorization, Google Sheets integration, and Composio toolset for financial data management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/1fb9f31d-fa13-552a-952c-054d3beb258b)

---

## Category
- **Primary category:** Finance automation
- **Secondary tags:** google sheets, expense tracking, data entry, automation, finance, ai workflow, composio, receipt management
- This solution bridges the gap between raw financial documents and structured accounting data, providing a scalable way to handle business expenses.

---

## Who is this for?
This solution is designed for teams looking to reclaim time spent on manual bookkeeping and financial reconciliation.

- **Finance Managers**
    - Automate the validation of expense reports to ensure compliance with company spending policies.
- **Operations Leads**
    - Maintain real-time visibility into departmental burn rates without waiting for end-of-month reports.
- **Small Business Owners**
    - Eliminate the administrative burden of manual data entry for daily business receipts and invoices.
- **Remote Team Leads**
    - Simplify the reimbursement process by allowing team members to submit expenses directly into a centralized tracker.

---

## Features
- **Intelligent Categorization**
    - Uses AI to automatically assign expenses to predefined categories like Travel, Software, or Office Supplies based on receipt content.
- **Google Sheets Integration**
    - Seamlessly appends new expense rows to your master ledger, ensuring data is always available for reporting.
- **Real-time Data Sync**
    - Processes inputs immediately upon submission, providing instant updates to your financial dashboard.
- **Composio-Powered Connectivity**
    - Utilizes the Composio Toolset to securely authenticate and interact with Google Sheets APIs without writing custom code.
- **Error Reduction**
    - Minimizes manual keying errors by extracting values directly from receipt text using advanced OCR and parsing.

---

## Use Cases
**Expense Reporting**
- Automatically log travel and meal expenses during business trips.
- Sync recurring monthly software subscriptions to your primary tracking sheet.

**Financial Auditing**
- Flag duplicate expense entries or missing receipt information for manual review.
- Generate monthly summaries of spending by category for budget variance analysis.

**Operational Efficiency**
- Streamline the reimbursement workflow for remote employees submitting digital receipts.
- Maintain a clean, audit-ready database of all company expenditures in one location.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Automated Expense Tracker" template.
2. Click "Import" to load the workflow into your workspace.
3. Connect your Google Sheets account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw receipt text or expense details from the user.
- **Agent**: Analyzes the input, extracts key fields (date, amount, vendor, category), and formats the data.
- **Composio Toolset**: Executes the API call to write the structured data into the designated Google Sheet.
- **Chat Output**: Confirms the successful logging of the expense to the user.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Log a $45.00 expense for 'Office Supplies' at 'Amazon' on 2023-10-27.`
- `Add a new travel expense: $120.00 for 'Hotel Stay' at 'Marriott' dated today.`
- `Record a software subscription payment of $29.99 for 'Slack' under 'Software' category.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the financial clerk, parsing unstructured text into structured JSON.
- Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5).
- Ensure the system prompt defines the required schema (Date, Vendor, Amount, Category).
- Instruct the agent to normalize currency formats before passing data to the toolset.

### 2) Composio Toolset Node
- Provide your Google Sheets API credentials within the Composio dashboard.
- Set the connection scope to allow 'Read/Write' access to the specific spreadsheet used for tracking.

### 3) Tool Availability
- `google_sheets_append_row`: For adding new expense entries.
- `google_sheets_get_sheet_metadata`: To verify sheet headers before writing.
- `google_sheets_search_rows`: To check for potential duplicate entries.

---

## Related Solutions
- [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) — Automate the matching of transactions and bank statements.
- [../account-health-usage-monitor-by-jotform/README.md](../account-health-usage-monitor-by-jotform/README.md) — Track account usage and operational metrics via form submissions.
- [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) — Manage complex business workflows and task automation.
