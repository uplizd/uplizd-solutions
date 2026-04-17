# CRM Data Cleaner (Uplizd) - Precision Data scrubbing & Sanitization

## Summary
A Uplizd AI workflow designed for targeted data cleaning tasks, allowing you to quickly scrub specific datasets, fix bulk formatting errors, and sanitize your CRM records with surgical precision.

---

## Demo

![Uplizd CRM Data Cleaner flow performing targeted data scrubbing and sanitization on CRM records](../image.png)

**Alt text (SEO-ready):** Uplizd CRM Data Cleaner executing bulk data cleaning and sanitization rules to improve CRM data accuracy.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bc37bce1-5200-556d-a3a9-23d0f6079039)

---

## Category

**Primary category:** Data hygiene

**Secondary tags:** crm, data cleaning, sanitization, automation, composio, data quality, salesops, record management

This solution provides an automated framework for maintaining high-integrity CRM data through intelligent, AI-driven scrubbing and formatting.

---

## Who is this for?

This workflow is built for data-conscious teams who need a fast, reliable tool for ad-hoc or scheduled data cleaning projects:

- **Data Analysts**
    - Clean up raw data imports before they are merged into the main CRM database.
- **Sales Operations (SalesOps)**
    - Quickly fix formatting issues in lead lists purchased from external vendors.
- **CRM Administrators**
    - Execute specific "find and replace" or "standardization" rules across thousands of records instantly.
- **Marketing Specialists**
    - Scrub email lists to remove "junk" entries and ensure consistent field formatting for personalized campaigns.

---

## Features

- **Selective Data Scrubbing**
  Apply cleaning rules to specific fields, tags, or segments without affecting the rest of the database.

- **Advanced Pattern Matching**
  Uses regex and AI to identify and fix complex data patterns (e.g., separating "First Name" and "Last Name" from a full name field).

- **Bulk Format Standardization**
  Normalize dates, phone numbers, addresses, and currency fields across your entire dataset.

- **Junk & Placeholder Removal**
  Automatically identifies and removes placeholder data like "asdf", "test@test.com", or "N/A".

- **Pre-Clean Preview**
  The agent can provide a summary of proposed changes for review before committing the bulk update to the CRM.

---

## Use Cases

**Sanitize New Lead Imports**
- Fix common "fat-finger" errors in email addresses (e.g., "gmial.com" to "gmail.com").
- Remove special characters and emojis from company and contact names.

**Standardize International Data**
- Convert all phone numbers to E.164 format based on the country code.
- Standardize country names to ISO Alpha-2 or Alpha-3 codes.

**Field Merging & Splitting**
- Split "Address" fields into "Street", "City", "State", and "Zip" for better geolocation.
- Merge "First Name" and "Last Name" into a "Full Name" field for specific reporting needs.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all nodes are connected correctly: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input** → receives the cleaning instructions or the dataset to be processed.
- **Agent** → analyzes the data and applies the requested cleaning rules.
- **Composio Toolset** → provides the actions to read and write data back to your CRM or spreadsheet.
- **Chat Output** → summary of the cleaning results and records processed.

### 3) Run the Flow
1. Click **Playground** to open the Chat Interface.
2. Enter a request such as:
   - `"Scrub this list of leads and fix all invalid email formats"`
   - `"Standardize all phone numbers in the CRM to international format"`
   - `"Remove any records that contain 'test' in the company name"`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is focused on data accuracy and pattern recognition.
- Enforce strict data validation rules.
- Be precise with string manipulations.
- Always highlight any data that could not be cleaned automatically.

### 2) Composio Toolset Node
Requires your **Composio API Key** and a connection to your data source (CRM, Google Sheets, etc.).

### 3) Tool Availability
- Bulk updates and deletes
- Data validation and formatting
- Pattern matching (Regex)
- Field mapping and transformation

---

## Related Solutions

* **[CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md)**  
  Continuous maintenance to ensure your CRM stays clean, organized, and free of data rot.

* **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.

* **[CRM Address Data Cleanup Agent](../crm-address-data-cleanup-agent/README.md)**  
  Specialized verification and standardization of physical address and location data.
