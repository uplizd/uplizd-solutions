# CRM Data Hygienist (Uplizd) - Expert Contact & Company Data Enrichment

## Summary
A Uplizd AI workflow that functions as a dedicated data specialist, focusing on the deep enrichment and surgical cleaning of contact and company records to ensure your sales and marketing teams have the best possible intelligence.

---

## Demo

![Uplizd CRM Data Hygienist flow performing deep contact and company data enrichment in CRM](../image.png)

**Alt text (SEO-ready):** Uplizd CRM Data Hygienist using specialized tools to enrich and clean CRM records for maximum sales and marketing effectiveness.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/da6576a5-97e4-5a49-9939-459021561deb)

---
## Who is this for?
This workflow is designed for organizations that want to go beyond simple cleaning and truly enrich their customer data with professional insights:

- Sales Development Representatives (SDRs)
    - Automatically find direct-dial phone numbers and verified work emails for your target prospects.

- Marketing Operations (MOps)
    - Enrich company records with industry, revenue, and employee count for more precise audience segmentation.

- CRM Data Managers
    - Consolidate and standardize data from multiple sources into a single, high-quality record.

- Founders & Business Owners
    - Build a high-value database of potential partners and customers with minimal manual effort.

---

## Features

- **Deep Contact Enrichment**  
  Finds missing job titles, LinkedIn profiles, and verified professional email addresses.

- **Company Intelligence Gathering**  
  Appends critical firmographic data (Industry, Size, HQ Location, Website) to company records.

- **Automated Data Normalization**  
  Standardizes disparate data points into a clean, unified format that fits your CRM's specific schema.

- **Real-time Record Updates**  
  Instantly updates your CRM as new information is discovered, ensuring your database never falls behind.

- **Specialized Dropcontact Integration**  
  Uses the power of Dropcontact's algorithms to provide high-accuracy B2B data enrichment without the need for manual research.

---

## Use Cases

- **Prospection List Enrichment**
  - Take a list of company names and website URLs and return a fully enriched list with key decision-makers and their contact details.
  - Automatically identify the "Best" email to use for outreach based on deliverability scores.

- **CRM Record Refresh**
  - Regularly scan your "Lost Deals" or "Inactive Customers" to see if stakeholders have changed roles or companies.
  - Update stale company firmographics (e.g., if a company has been acquired or has grown significantly).

- **Data Inbound Standardization**
  - Automatically clean and enrich leads as they flow in from your website or third-party lead providers.
  - Fix typos and fill in missing fields (like "City" or "Industry") based on the company's domain.

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
5. Ensure all nodes are connected correctly:
   - **Chat Input**
   - **Composio Toolset**
   - **Agent**
   - **Chat Output**

### 2) Setup the Nodes
Verify the workflow structure:

- **Chat Input** → receives the records or lists that need enrichment.
- **Agent** → orchestrates the enrichment process using available tools.
- **Composio Toolset** → provides the connection to Dropcontact and your CRM.
- **Chat Output** → summary of the enriched data and records updated.

### 3) Run the Flow
1. Click **Playground** to open Chat Interface.
2. Enter a request such as:
   - `"Enrich this contact [Name/Email] with their current title and company info"`
   - `"Find and append the employee count and industry for [Company Name]"`
   - `"Verify and clean the contact details for our 'Strategic Accounts' segment"`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is focused on B2B intelligence and data synthesis.

Recommended instruction pattern:
- Prioritize accuracy and verified data sources
- Maintain a focus on professional B2B context
- Log exactly which fields were updated and what the original values were

### 2) Composio Toolset Node
Requires your **Composio API Key** and a connection to **Dropcontact** and your primary CRM.

### 3) Tool Availability
The agent can call tools for:
- Contact enrichment (Email, Phone, Title)
- Company enrichment (Firmographics)
- Data normalization and formatting
- CRM record creation and update

---

## Related Solutions

* **[CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md)**  
  Continuous maintenance to ensure your CRM stays clean, organized, and free of data rot.

* **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.

* **[Deal Pipeline Manager](../deal-pipeline-manager/README.md)**  
  Automatically update deal progress and create follow-up tasks for your sales team.

* **[CRM Address Data Cleanup Agent](../crm-address-data-cleanup-agent/README.md)**  
  Specialized verification and standardization of physical address and location data.
