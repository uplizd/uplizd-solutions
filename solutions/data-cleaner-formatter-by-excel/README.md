# Data Cleaner and Formatter (Uplizd) - Automated Excel data normalization and structural cleanup

## Summary
The Data Cleaner and Formatter (Uplizd) is an intelligent AI workflow designed to transform unstructured, messy datasets into clean, analysis-ready Excel tables. By leveraging advanced LLM parsing and the Composio Toolset, this solution automates the tedious process of data normalization, deduplication, and formatting, ensuring high-quality data hygiene for analysts, operations teams, and data-driven organizations.

---

## Demo
![Data Cleaner and Formatter workflow interface showing automated Excel file processing and cleanup nodes](image.png)
**Alt text (SEO-ready):** Data Cleaner and Formatter workflow in Uplizd, showing automated Excel data normalization, CSV cleaning, and AI-driven table formatting integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data)](https://uplizd.ai/solutions/1a9dfe99-c7e0-5743-8e8a-a2d9016cc3ba)

---

## Category
**Primary category:** Data integration
**Secondary tags:** excel, data hygiene, data cleaning, automation, csv, formatting, ai workflow, composio
This solution streamlines data operations by bridging the gap between raw, inconsistent inputs and structured, professional-grade spreadsheets.

---

## Who is this for?
This workflow is designed for professionals who manage large datasets and require consistent, error-free reporting.

*   **Data Analysts**
    *   Reduces manual cleaning time by automatically fixing formatting inconsistencies and structural errors in raw exports.
*   **Operations Managers**
    *   Ensures that CRM and operational reports are standardized and ready for executive-level review without manual intervention.
*   **Sales Operations**
    *   Maintains high data hygiene standards across lead lists and opportunity logs, preventing duplicate or malformed entries.
*   **Finance Professionals**
    *   Automates the reconciliation of disparate data sources into clean, uniform Excel templates for financial reporting.

---

## Features
- **Intelligent Data Parsing**
  Uses AI to interpret and normalize inconsistent date formats, currency symbols, and text strings across disparate data sources.
- **Automated Deduplication**
  Identifies and removes redundant records based on custom logic, ensuring your master Excel files remain lean and accurate.
- **Structural Standardization**
  Automatically maps raw data fields to your preferred header structure, ensuring every export follows your organization's naming conventions.
- **Error Detection & Flagging**
  Highlights potential data anomalies or missing values in real-time, allowing for proactive correction before final analysis.
- **Seamless Excel Integration**
  Leverages the Composio Toolset to directly interact with Excel files, enabling automated read/write operations without leaving the Uplizd environment.

---

## Use Cases
**Data Migration & Consolidation**
*   Merging multiple CSV exports from different departments into a single, unified master Excel file.
*   Standardizing address, phone number, and email formats during bulk data imports.

**Reporting & Analytics Prep**
*   Converting raw, unstructured survey responses into categorized, quantitative Excel tables.
*   Cleaning historical sales data to ensure accurate trend forecasting and pipeline visualization.

**Operational Data Hygiene**
*   Automating the removal of "junk" characters and whitespace from exported CRM contact lists.
*   Validating and formatting product SKU lists to match inventory management system requirements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your required Excel or storage integration within the settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw data or file path from the user.
*   **Agent**: Processes the data using specific instructions to clean, format, and structure the input.
*   **Composio Toolset**: Executes the necessary API calls to read, modify, and save the Excel file.
*   **Chat Output**: Returns the confirmation of the cleaned file or a preview of the formatted data.

### 3) Run the Flow
Use the Playground to test your data processing:
*   `"Clean the attached customer list, fix the date formats to YYYY-MM-DD, and remove all duplicate email entries."`
*   `"Standardize the column headers in this sales export to match our master template and highlight any missing values."`
*   `"Format this raw survey data into a clean table and calculate the average response score for each category."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the data transformation engine.
*   **Instruction Pattern:**
    *   "Act as a data engineer; identify and correct formatting inconsistencies in the provided dataset."
    *   "Strictly follow the schema requirements: ensure all date fields are ISO 8601 and currency fields are numeric."
    *   "If data is missing, flag the row for review rather than guessing the value."

### 2) Composio Toolset Node
*   **API Key:** Ensure your Composio API key is configured with access to your file storage and Excel integration.
*   **Connection Scope:** Grant read/write permissions to the specific folders containing your raw data files.

### 3) Tool Availability
*   **File Read/Write:** Ability to open, parse, and save Excel/CSV files.
*   **Data Transformation:** Logic for string manipulation, regex matching, and type conversion.
*   **Validation:** Tools to check for duplicates and schema compliance.

---

## Related Solutions
*   [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Automates the cleanup of stale or decaying CRM records.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronizes data across multiple platforms with conflict resolution.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manages sales stages and pipeline velocity for improved forecasting.
