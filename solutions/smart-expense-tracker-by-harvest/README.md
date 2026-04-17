# Smart Expense Tracker (Uplizd) - Automated project expense logging and categorization

## Summary
The Smart Expense Tracker is an intelligent Uplizd AI workflow designed to automate the ingestion, categorization, and logging of project-related expenses from receipts and invoices. By leveraging the Composio Toolset to interface with Harvest, this solution eliminates manual data entry, ensures accurate financial tracking, and provides real-time visibility into project budgets for finance teams and project managers.

---

## Demo
![Smart Expense Tracker workflow diagram showing receipt processing, categorization, and Harvest logging](image.png)
**Alt text (SEO-ready):** Smart Expense Tracker Uplizd workflow for automated receipt processing, expense categorization, and Harvest integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/20f8c842-20a5-5d75-a0de-bcdd84dc1f6c)

---

## Category
- **Primary category:** Finance operations
- **Secondary tags:** expense management, harvest, automation, data entry, project finance, ai workflow, composio, financial reporting
- This solution streamlines financial hygiene by bridging the gap between raw expense documentation and project accounting systems.

---

## Who is this for?
This solution is built for teams looking to reduce administrative overhead and improve the accuracy of project-based financial reporting.

- **Project Managers**
    - Gain real-time visibility into project spend without waiting for manual expense reports.
- **Finance Operations**
    - Eliminate data entry errors and accelerate the month-end reconciliation process.
- **Freelancers & Consultants**
    - Automate the tedious task of logging billable expenses against specific client projects.
- **Accounting Leads**
    - Ensure consistent categorization of expenses across multiple projects and team members.

---

## Features
- **Automated Receipt Parsing**
    - Uses AI to extract key financial data like merchant, date, and total amount from unstructured receipt images or PDFs.
- **Smart Categorization**
    - Automatically maps expenses to the correct project codes and expense categories based on historical patterns.
- **Harvest Integration**
    - Seamlessly pushes verified expense data directly into Harvest using the Composio Toolset for instant record creation.
- **Real-time Validation**
    - Checks incoming expenses against project budgets to flag potential overages before they are logged.
- **Audit-Ready Logging**
    - Maintains a structured digital trail of all processed expenses, ensuring compliance and easy retrieval for audits.

---

## Use Cases
**Expense Management**
- Automatically log travel-related expenses to specific client projects immediately after a trip.
- Sync recurring software subscriptions to project budgets to maintain accurate overhead tracking.

**Project Financials**
- Flag expenses that exceed pre-set project budget thresholds for immediate manager review.
- Consolidate multi-currency receipts into a single base currency for unified project reporting.

**Data Hygiene**
- Standardize expense descriptions and categories to ensure clean, reportable data in Harvest.
- Automatically archive processed receipt files to designated cloud storage folders after successful logging.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Expense Tracker template file provided in this repository.
3. Connect your Harvest account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the receipt image or invoice text data.
- **Agent**: Analyzes the input, extracts financial metadata, and determines the correct project mapping.
- **Composio Toolset**: Executes the API calls to log the expense directly into your Harvest account.
- **Chat Output**: Confirms successful logging or requests clarification if data is missing.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Log a $45.50 expense for 'Office Supplies' to the 'Q3 Marketing' project.`
- `Process this receipt image and add it to the 'Website Redesign' project under 'Software' category.`
- `Extract the total from this invoice and log it as a billable expense for the 'Client X' project.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the financial analyst, ensuring data accuracy and correct categorization.
- **Instruction Pattern:**
    - Extract merchant, date, amount, and category from the provided input.
    - Map the expense to the correct project ID found in the Harvest environment.
    - Request human intervention only if the project or category cannot be determined with high confidence.

### 2) Composio Toolset Node
- Requires a valid Harvest API Key and Workspace ID.
- Ensure the connection scope includes `expenses:write` and `projects:read` permissions.

### 3) Tool Availability
- **Harvest Expense API**: For creating and updating expense entries.
- **Harvest Project API**: For fetching active project lists and IDs.
- **Data Parser**: For OCR and structured data extraction from images.

---

## Related Solutions
- [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) — Automate bank reconciliation and ledger updates.
- [../workspace-setup-optimizer-by-clockify/README.md](../workspace-setup-optimizer-by-clockify/README.md) — Manage time tracking and project resource allocation.
- [../account-health-usage-monitor-by-jotform/README.md](../account-health-usage-monitor-by-jotform/README.md) — Monitor usage metrics and form-based financial inputs.
