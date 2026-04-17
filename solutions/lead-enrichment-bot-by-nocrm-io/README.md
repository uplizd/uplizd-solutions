# Lead Enrichment Bot (Uplizd) - Automate lead profile enhancement with real-time data

## Summary
The Lead Enrichment Bot is an intelligent Uplizd workflow designed to automatically augment raw lead data with deep contextual insights. By leveraging the Composio Toolset to query external databases and CRM platforms, this solution eliminates manual research, ensures your sales team has a single source of truth for every prospect, and significantly accelerates pipeline velocity by prioritizing high-intent leads.

---

## Demo
![Lead Enrichment Bot workflow diagram showing data flow from input to CRM update](image.png)
**Alt text (SEO-ready):** Lead Enrichment Bot Uplizd workflow diagram, automated CRM data enrichment, sales lead qualification, and Composio integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AQLDTAQo0r/5QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDZ4AAAA+SURBVEjHY2AYBaNgFAwAAAPAAAE=)](https://uplizd.ai/solutions/e1fe9ddf-57b2-5cae-97b5-622d6a437a28)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, lead enrichment, nocrm, sales intelligence, data hygiene, pipeline, composio, ai workflow

This solution integrates directly into your sales stack to transform fragmented contact information into comprehensive, actionable lead profiles.

---

## Who is this for?
This solution is built for revenue-focused teams looking to optimize their outreach and data quality.

*   **Sales Development Representatives (SDRs)**
    *   Reduces time spent on manual research by instantly populating lead profiles with company size, industry, and funding data.
*   **Revenue Operations (RevOps) Managers**
    *   Maintains data hygiene by ensuring all lead records are standardized and enriched with consistent, verified information.
*   **Account Executives (AEs)**
    *   Provides deeper context for discovery calls, allowing for personalized pitches based on real-time prospect intelligence.
*   **Growth Marketers**
    *   Improves lead scoring accuracy by injecting enriched firmographic data into the qualification pipeline.

---

## Features
- **Automated Data Retrieval**
  Connects to external intelligence providers via the Composio Toolset to fetch missing contact details in real-time.
- **CRM Synchronization**
  Automatically pushes enriched data back into your CRM, ensuring your system of record is always up-to-date.
- **Intelligent Contextualization**
  Uses the Agent node to synthesize raw data into a concise summary of the lead's professional background and company relevance.
- **Customizable Enrichment Logic**
  Define specific fields to target, such as job title, company revenue, or social media presence, to match your unique sales strategy.
- **Real-time Pipeline Updates**
  Triggers immediate updates to lead status or priority levels based on the newly gathered enrichment insights.

---

## Use Cases
**Lead Qualification**
*   Automatically flag leads that match your Ideal Customer Profile (ICP) based on enriched company size and industry data.
*   Route high-value leads to senior account executives immediately upon enrichment completion.

**Sales Outreach Optimization**
*   Generate personalized ice-breakers for email campaigns using the latest company news or funding announcements retrieved by the agent.
*   Update CRM fields to reflect the most recent contact information, reducing bounce rates during outreach.

**Data Hygiene & Maintenance**
*   Periodically scan existing CRM records to identify and fill gaps in contact data, such as missing email addresses or phone numbers.
*   Standardize job titles and company names across your database to ensure clean reporting and analytics.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the Uplizd builder.
2. Connect your preferred CRM and data intelligence tool accounts via the Composio Toolset.
3. Configure the input trigger to listen for new lead creation events.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw lead data or trigger event from your CRM.
*   **Agent**: Processes the lead information and determines which enrichment data is required.
*   **Composio Toolset**: Executes the API calls to fetch external intelligence and update CRM fields.
*   **Chat Output**: Returns a confirmation summary of the enriched data to the user or logs the success.

### 3) Run the Flow
Use the Playground to test the enrichment process with these example prompts:
* `Enrich the lead record for john.doe@example.com with current company details.`
* `Find the latest funding information for the company associated with this lead.`
* `Update the CRM profile for the latest lead in the 'New' stage with LinkedIn and industry data.`

---

## Configuration

### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for data extraction and mapping.
*   Instruction: "Act as a sales intelligence assistant; identify missing fields in the lead profile and use the provided tools to fetch accurate data."
*   Instruction: "Prioritize data accuracy and ensure all updates follow the CRM's required formatting standards."
*   Instruction: "If data cannot be found, provide a clear summary of the missing information rather than hallucinating values."

### 2) Composio Toolset Node
*   **API Key**: Provide your Composio API key to enable secure connectivity to your CRM and enrichment providers.
*   **Connection Scope**: Ensure the toolset has read/write permissions for your CRM's Lead and Contact objects.

### 3) Tool Availability
*   **CRM Connectors**: Read/Write access to Lead, Contact, and Account objects.
*   **Data Intelligence APIs**: Capability to query firmographic and contact databases.
*   **Validation Tools**: Logic to verify email formats and company website URLs.

---

## Related Solutions
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Generate comprehensive reports on account activities and engagement.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize lead and contact data across multiple platforms seamlessly.
* [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score new sales opportunities based on lead signals.
