# Multi-Currency Expense Tracker (Uplizd) - Automated real-time currency conversion and expense logging

## Summary
The Multi-Currency Expense Tracker is an intelligent Uplizd AI workflow designed to streamline global financial reporting by automatically converting international expenses into a base currency. By leveraging the Fixer API via the Composio Toolset, this solution eliminates manual calculation errors, ensures consistent exchange rate application, and provides finance teams with a single source of truth for multi-currency operational costs.

---

## Demo
![Multi-Currency Expense Tracker workflow interface showing currency conversion nodes and expense logging](image.png)
**Alt text (SEO-ready):** Multi-Currency Expense Tracker Uplizd workflow, automated currency conversion, finance data integration, Fixer API automation, and expense management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/042f6837-f563-5aee-a57d-6df03c66c1d8)

---

## Category
- **Primary category:** Finance
- **Secondary tags:** finance, currency conversion, fixer, expense tracking, data sync, automation, ai workflow, composio
- This solution bridges the gap between global spending and local accounting by automating real-time currency normalization.

---

## Who is this for?
This solution is built for finance professionals and operations teams managing international budgets.

- **Finance Manager**
    - Ensures accurate monthly reporting by standardizing multi-currency expense data into a single base currency.
- **Operations Lead**
    - Reduces administrative overhead by automating the manual lookup and calculation of daily exchange rates.
- **Global Accountant**
    - Maintains audit-ready financial records with consistent, timestamped currency conversion logs.
- **Travel Coordinator**
    - Simplifies reimbursement processes by providing instant conversion estimates for international travel expenses.

---

## Features
- **Real-time Conversion**
    - Fetches the most accurate, up-to-date exchange rates via the Fixer API to ensure financial precision.
- **Automated Data Normalization**
    - Converts diverse currency inputs into your organization's preferred base currency automatically.
- **Composio Toolset Integration**
    - Seamlessly connects the AI agent to external financial data sources for reliable, secure information retrieval.
- **Error-Free Calculation**
    - Eliminates human error in manual currency math, ensuring compliance with internal financial policies.
- **Unified Expense Logging**
    - Centralizes converted expense data into your existing CRM or accounting software for streamlined tracking.

---

## Use Cases
**International Travel Reimbursement**
- Automatically convert hotel and meal receipts from foreign currencies to the company's home currency.
- Flag expenses that exceed specific budget thresholds after currency conversion.

**Global Vendor Payments**
- Standardize invoice amounts from international contractors to ensure accurate accounts payable processing.
- Generate monthly summaries of vendor spending across multiple geographic regions.

**Multi-Currency Budget Audits**
- Reconcile credit card statements containing mixed-currency transactions against internal project budgets.
- Identify discrepancies between transaction-date exchange rates and current market values.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Solution."
2. Upload the `multi-currency-expense-tracker-by-fixer` configuration file.
3. Connect your Fixer API credentials within the Composio Toolset settings.
4. Ensure nodes are correctly linked from Chat Input to Agent, and Agent to Composio Toolset and Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw expense amount, original currency, and target currency.
- **Agent**: Processes the request and triggers the currency conversion logic.
- **Composio Toolset**: Executes the Fixer API call to retrieve current exchange rates.
- **Chat Output**: Returns the converted amount and the exchange rate used for the calculation.

### 3) Run the Flow
Use the Playground to test the following prompts:
- `Convert 500 EUR to USD and log the expense.`
- `What is the current exchange rate for 1000 JPY to GBP?`
- `Calculate the total cost in EUR for a 50 USD lunch and a 200 CAD hotel stay.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a financial assistant, interpreting natural language requests to perform accurate currency conversions.
- Use a clear, instruction-based prompt to define the base currency.
- Configure the agent to always provide the exchange rate used for transparency.
- Set the agent to request missing information (e.g., target currency) if not provided by the user.

### 2) Composio Toolset Node
- Provide your **Fixer API Key** in the node configuration to enable real-time rate fetching.
- Set the connection scope to include read-only access to currency exchange endpoints.

### 3) Tool Availability
- **Fixer Currency Converter**: Retrieves live market rates for over 170 currencies.
- **Historical Rate Lookup**: Allows the agent to fetch rates for specific past dates for audit purposes.
- **Currency Validator**: Ensures that input currency codes are valid and supported by the API.

---

## Related Solutions
- [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) - Automates the matching of bank transactions and ledger entries.
- [../account-health-usage-monitor-by-jotform/README.md](../account-health-usage-monitor-by-jotform/README.md) - Tracks account usage and health metrics across platforms.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronizes customer data across multiple CRM and financial systems.
