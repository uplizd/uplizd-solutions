# Transaction Merchant Identifier (Uplizd) - Enrich payment data with brand intelligence

## Summary
The Transaction Merchant Identifier workflow automates the enrichment of raw, often cryptic transaction strings into clear, recognizable merchant identities. By leveraging the Brandfetch integration, this Uplizd AI workflow helps finance and operations teams eliminate manual data reconciliation, improve financial reporting accuracy, and provide a single source of truth for transaction categorization.

---

## Demo
![Transaction Merchant Identifier workflow interface showing raw transaction strings being mapped to verified brand logos and names via the Composio Toolset.](image.png)
**Alt text (SEO-ready):** Uplizd Transaction Merchant Identifier workflow showing automated brand enrichment, payment data cleaning, and merchant logo mapping using Composio and Brandfetch.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/30614fea-d40f-5e8b-b471-679e404be41e)

---

## Category
**Primary category:** Data integration
**Secondary tags:** finance, merchant data, brand enrichment, data hygiene, composio, brandfetch, reconciliation, payment processing.
This solution bridges the gap between raw financial logs and actionable business intelligence by normalizing merchant data at scale.

---

## Who is this for?
This workflow is designed for teams managing high-volume transaction data who need to maintain clean, readable financial records.

* **Financial Analyst**
    * Reduces time spent manually researching and categorizing ambiguous merchant descriptors in ledger exports.
* **Operations Manager**
    * Ensures consistent merchant naming conventions across disparate payment gateways and internal databases.
* **Accounting Lead**
    * Improves the speed and accuracy of month-end reconciliation by providing verified brand context for every transaction.
* **Product Manager**
    * Enables better user-facing transaction history displays by providing clean brand names and logos for customer portals.

---

## Features
- **Automated Brand Mapping**
  Instantly matches cryptic payment strings to official merchant names and brand assets using the Brandfetch API.
- **Real-time Data Normalization**
  Standardizes transaction descriptions into a clean, uniform format suitable for database ingestion or reporting.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely connect the Uplizd agent to external brand intelligence services.
- **High-Volume Processing**
  Designed to handle bulk transaction lists, allowing for efficient cleanup of thousands of records in a single workflow execution.
- **Contextual Enrichment**
  Goes beyond simple naming by retrieving brand-specific metadata, including official logos and website URLs, to enhance financial dashboards.

---

## Use Cases
**Financial Reconciliation**
* Automatically mapping bank statement descriptors to internal vendor IDs for faster ledger matching.
* Identifying duplicate transactions across different payment processors by normalizing merchant names.

**Customer Experience Enhancement**
* Displaying verified brand logos in user transaction history feeds to reduce support tickets regarding unrecognized charges.
* Providing clear, human-readable merchant names in mobile banking or subscription management interfaces.

**Operational Data Hygiene**
* Cleaning up legacy transaction databases to prepare for migration to new ERP or accounting software.
* Flagging high-risk or unknown merchant descriptors that require manual review by the fraud prevention team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in the builder.
2. Connect your Brandfetch API credentials within the Composio integration settings.
3. Map your transaction data source (CSV, API, or Database) to the input node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the raw transaction string or batch list.
* **Agent**: Processes the input, queries the toolset, and formats the output.
* **Composio Toolset**: Executes the brand lookup and data retrieval functions.
* **Chat Output**: Returns the enriched merchant data, including name, logo, and category.

### 3) Run the Flow
Use the Playground to test your data:
* `Identify the merchant for this transaction string: "AMZN MKTP US*123456789"`
* `Process this list of raw payment descriptors and return a JSON table with brand names and logos.`
* `Clean the following transaction record and provide the official website for the identified merchant: "STRIPE *TECH_SERVICES_INC"`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine that parses raw strings and interprets tool responses.
* Set the system prompt to prioritize accuracy in brand matching.
* Enable "JSON Mode" if you require structured output for downstream database integration.
* Configure the temperature to 0.1 to ensure consistent, deterministic merchant identification.

### 2) Composio Toolset Node
* Provide your valid Brandfetch API key in the connection settings.
* Ensure the scope is set to allow read-only access to brand metadata.

### 3) Tool Availability
* **Brand Search**: Retrieves official brand names based on search queries.
* **Logo Retrieval**: Fetches high-resolution brand assets for UI integration.
* **Metadata Lookup**: Extracts website URLs and industry categories for enriched reporting.

---

## Related Solutions
* [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Automates the matching of bank transactions with internal ledger entries.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Cleans and standardizes CRM records to prevent data decay.
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enriches account profiles with verified contact and company data.
