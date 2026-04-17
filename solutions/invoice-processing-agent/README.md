
# Invoice Processing Agent (Parseur) - Automate Accounts Payable & Data Extraction

## Summary
An Uplizd AI workflow for accounts payable automation that extracts and routes critical invoice data from emails and PDFs. It monitors incoming mailboxes, intelligently identifies vendors via template matching, and pushes structured data directly to accounting systems—dramatically reducing manual entry and flagging exceptions for human review.

---

## Demo

![Uplizd Invoice Processing Agent flow extracting PDF data and routing to accounting systems](../image.png)

**Alt text:** Uplizd Invoice Processing Agent integrating Parseur toolsets to automate financial document extraction and system synchronization.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/RUN%20ON%20UPLIZD-blue?style=for-the-badge&logo=lightning)](https://uplizd.ai/solutions/1ca8d196-496f-59e0-bf44-76513d8a9bd4/)

---
## Who is this for?
This workflow is built for finance operations and administrative teams looking to digitize their payables process:

- **Accounting & AP Teams**
    - Eliminate hours of manual data entry and "fat-finger" errors from vendor invoices.

- **Finance & Operations Managers**
    - Speed up the approval cycle and ensure early-payment discounts aren't missed due to processing delays.

- **Small Business Owners**
    - Professionally manage high volumes of vendor paperwork without hiring dedicated administrative staff.

- **Audit & Compliance Officers**
    - Maintain a consistent, digitally-logged audit trail of every financial document processed.

---

## Features

- **Continuous Mailbox Monitoring**  
  Automatically scans designated digital mailboxes for new invoice arrivals using `PARSEUR_LIST_MAILBOXES` and `PARSEUR_LIST_DOCUMENTS_IN_MAILBOX`.

- **Intelligent Template Matching**  
  Intelligently identifies the appropriate vendor template for each document to ensure maximum extraction accuracy via `PARSEUR_LIST_TEMPLATES`.

- **Deep Field Extraction**  
  Captures all critical accounting data including vendor names, total amounts, tax, due dates, invoice numbers, and specific line-item details.

- **Business Rule Validation**  
  Performs automated sanity checks for duplicate invoice numbers and verifies that due dates and payment terms align with standards.

- **Automated Routing & Webhooks**  
  Sends structured JSON data directly to your ERP, accounting software, or database using `PARSEUR_CREATE_WEBHOOK`.

- **Smart Exception Escalation**  
  Automatically flags invoices with low parsing confidence (<90%) or missing fields for manual review, ensuring only accurate data reaches your books.

---

## Use Cases

- **"Zero-Touch" Accounts Payable**
  - Connect your "invoices@" email alias to automatically populate your accounting software with new bills as they arrive.
  - Automatically flag and isolate invoices from new or unknown vendors for verification.

- **Batch PDF Processing**
  - Upload a bulk export of invoices and have them standardized, validated, and synchronized across your accounting systems in seconds.

- **Compliance & Spend Auditing**
  - Use the extracted data to run immediate reports on spend distribution across vendors without manual spreadsheet consolidation.

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all nodes are connected correctly:
   - **Chat Input**
   - **Parseur - PARSEUR_LIST_MAILBOXES**
   - **Parseur - PARSEUR_LIST_DOCUMENTS_IN_MAILBOX**
   - **Parseur - PARSEUR_LIST_TEMPLATES**
   - **Parseur - PARSEUR_CREATE_WEBHOOK**
   - **Agent**
   - **Chat Output**

### 2) Setup the Nodes
Verify the workflow structure:

- **Chat Input** → receives commands for manual processing runs or system status checks.
- **Agent** → coordinates the 6-step automation workflow (Monitoring -> Matching -> Extraction -> Validation -> Routing -> Exception Handling).
- **Parseur Toolset** → provides the underlying AI engine for document parsing and mailbox access.
- **Chat Output** → provides summaries of processed batches and flags items requiring human attention.

### 3) Run the Flow
1. Click **Playground** to open Chat Interface.
2. Enter a request such as:
   - `"Process all new invoices in the Main Mailbox for the last 24 hours"`
   - `"Parse the latest PDF from Vendor X and send the data to the accounting webhook"`
   - `"List any invoices from today that require manual review"`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is pre-configured with industry-standard accounting logic and a focus on financial data accuracy.

Recommended instruction pattern:
- Prioritize data accuracy over processing speed.
- Escalate any ambiguity to human review immediately.
- Ensure all monetary figures are consistently formatted for system entry.

### 2) Parseur Toolset Nodes
Requires your **Composio API Key** and a synchronized connection to your **Parseur** account with pre-defined templates for your common vendors.

### 3) Tool Availability
The agent can call tools for:
- Mailbox and document discovery
- Template management
- Webhook creation and data routing

---

## Related Solutions

* **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.

* **[Workforce Onboarding Automator](../workforce-onboarding-automator/README.md)**  
  Streamline new hire setup and group assignments for deskless workers on Connecteam.

* **[Meeting Room Coordinator](../meeting-room-coordinator/README.md)**  
  Automate office scheduling and resolve meeting room conflicts directly through Slack.

* **[Invoice Processing Agent](../invoice-processing-agent/README.md)**  
  Automate the extraction and routing of invoice data from emails and PDFs.
