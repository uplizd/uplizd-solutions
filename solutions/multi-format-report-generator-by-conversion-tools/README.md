# Multi-Format Report Generator (Uplizd) - Automated data transformation and document conversion

## Summary
The Multi-Format Report Generator is an intelligent Uplizd AI workflow designed to automate the conversion of complex Excel datasets into web-ready HTML and structured CSV formats. By leveraging the Composio Toolset to interface with file management and data processing APIs, this solution eliminates manual reformatting tasks, ensuring data consistency and accelerating reporting velocity for data-driven teams.

---

## Demo
![Multi-Format Report Generator workflow showing Excel input, data processing via Composio, and multi-format output](image.png)
**Alt text (SEO-ready):** Multi-Format Report Generator Uplizd workflow, Excel to HTML and CSV data conversion, automated document processing with Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/e47d1a3a-db89-57c7-ab3c-876eaad90361)

---

## Category
**Primary category:** Data integration
**Secondary tags:** excel, csv, html, data transformation, automation, reporting, composio, ai workflow
This solution streamlines data hygiene and distribution by automating the conversion of raw spreadsheets into standardized, accessible formats.

---

## Who is this for?
This solution is designed for professionals who manage high-volume data reporting and need to maintain cross-platform compatibility.

* **Data Analysts**
  * Automate the tedious conversion of raw Excel exports into clean, web-ready formats for stakeholder dashboards.
* **Operations Managers**
  * Ensure consistent data formatting across internal systems by standardizing output files automatically.
* **Marketing Coordinators**
  * Quickly transform campaign performance spreadsheets into HTML snippets for email templates or web reports.
* **Finance Specialists**
  * Maintain audit-ready CSV logs by programmatically converting and archiving complex financial workbooks.

---

## Features
- **Intelligent File Parsing**
  Automatically detects and interprets complex Excel structures, including nested headers and multi-sheet workbooks.
- **Multi-Format Export**
  Generates clean HTML tables for web display and standardized CSV files for database ingestion simultaneously.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely interact with file storage and data processing services in real-time.
- **Automated Data Hygiene**
  Applies predefined cleaning rules during the conversion process to remove null values and standardize date formats.
- **Workflow Scalability**
  Handles large datasets efficiently, allowing for batch processing of reports without manual intervention.

---

## Use Cases
**Automated Web Reporting**
* Converting monthly sales performance Excel sheets into HTML tables for company intranet publication.
* Updating public-facing product inventory lists by syncing internal Excel logs to web-ready formats.

**Data Migration & Sync**
* Preparing legacy Excel data for import into CRM systems by converting them into clean, standardized CSV files.
* Normalizing data fields across multiple department spreadsheets to ensure compatibility with downstream analytics tools.

**Operational Efficiency**
* Generating daily status reports in multiple formats to satisfy different stakeholder requirements automatically.
* Reducing manual data entry errors by automating the transformation of raw inputs into structured output files.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Multi-Format Report Generator template from the solution library.
3. Connect your preferred file storage service within the Composio configuration.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** to **Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the file path or raw data trigger from the user.
* **Agent:** Analyzes the input data and determines the required transformation logic.
* **Composio Toolset:** Executes the file conversion and formatting operations.
* **Chat Output:** Delivers the converted HTML and CSV files back to the user.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
* `Convert the latest sales-report.xlsx into an HTML table for the web team.`
* `Take the data from the Q3-financials.xlsx and export it as a clean CSV file.`
* `Process the inventory-update.xlsx and provide both HTML and CSV versions.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary orchestrator for data transformation logic.
* Use a model with strong reasoning capabilities for handling complex Excel schemas.
* Set the system prompt to prioritize data integrity and formatting accuracy.
* Ensure the agent is instructed to validate file headers before initiating conversion.

### 2) Composio Toolset Node
* Provide your Composio API key to enable secure access to file processing tools.
* Configure the connection scope to allow read/write access to your designated cloud storage folders.

### 3) Tool Availability
* **File Reader:** For parsing Excel workbooks and extracting raw data.
* **Data Transformer:** For mapping fields and applying formatting rules.
* **Format Converter:** For generating HTML and CSV output streams.

---

## Related Solutions
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms with automated conflict resolution.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain high-quality data by automating cleanup and deduplication.
* [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and pipeline velocity with AI-driven insights.
