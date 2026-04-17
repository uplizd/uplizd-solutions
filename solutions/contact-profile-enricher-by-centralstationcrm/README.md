# Contact Profile Enricher (Uplizd) - Automated CRM data enrichment and intelligence

## Summary
The Contact Profile Enricher is an intelligent Uplizd workflow designed to automate the gathering and synchronization of professional contact data. By leveraging the Composio Toolset to query external intelligence providers, this solution ensures your CRM records remain accurate and comprehensive, eliminating manual research and maintaining a single source of truth for your sales and marketing teams.

---

## Demo
![Contact Profile Enricher workflow showing automated data flow from CRM to enrichment tools](image.png)
**Alt text (SEO-ready):** Uplizd Contact Profile Enricher workflow automating CRM data synchronization and professional profile intelligence gathering.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue?logo=uplizd)](https://uplizd.ai/solutions/f908eb17-0d91-5ce6-aa87-234b32b6fa57)

---

## Category
**Primary category:** CRM data enrichment
**Secondary tags:** crm, centralstationcrm, data enrichment, sales automation, lead intelligence, data hygiene, composio, ai workflow
This solution streamlines the enrichment of contact records by integrating real-time intelligence directly into your CRM environment.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to reduce manual data entry and improve lead quality.

* **Sales Development Representatives (SDRs)**
    * Spend less time researching prospect details and more time engaging with high-quality, verified leads.
* **CRM Administrators**
    * Maintain high data hygiene standards by ensuring every contact profile is populated with up-to-date professional information.
* **Marketing Operations Managers**
    * Improve segmentation accuracy by enriching contact profiles with firmographic and professional data points.
* **Account Executives**
    * Access comprehensive prospect insights directly within the CRM to personalize outreach and increase conversion rates.

---

## Features
- **Automated Data Retrieval**
  Seamlessly fetches professional details from external databases using the Composio Toolset to populate empty CRM fields.
- **Real-time CRM Sync**
  Ensures that enriched data is pushed back to your CRM instantly, maintaining consistency across your entire sales stack.
- **Intelligent Field Mapping**
  Automatically maps retrieved intelligence to the correct CRM fields, reducing the risk of manual entry errors.
- **Proactive Data Hygiene**
  Identifies and updates outdated contact information, preventing data decay within your CentralStationCRM instance.
- **Context-Aware Enrichment**
  Uses AI to prioritize the most relevant professional data points based on your specific sales qualification criteria.

---

## Use Cases
**Lead Qualification**
* Automatically append job titles and company size to new leads to prioritize high-value prospects.
* Flag incomplete contact profiles for enrichment before they enter the active sales pipeline.

**Sales Outreach Optimization**
* Gather professional background information to craft highly personalized email sequences.
* Sync updated contact details to ensure automated outreach tools always have the correct recipient data.

**CRM Maintenance**
* Perform bulk enrichment of existing contact lists to refresh stale data and improve database health.
* Standardize formatting for contact locations and company names to ensure clean, searchable CRM records.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Contact Profile Enricher template from the solution library.
3. Connect your CentralStationCRM account and required enrichment tool credentials via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the contact identifier or email address to trigger the enrichment process.
* **Agent**: Orchestrates the logic, deciding which data points are missing and which tools to query.
* **Composio Toolset**: Executes the API calls to fetch external contact intelligence.
* **Chat Output**: Returns the enriched profile summary and confirms the update status in the CRM.

### 3) Run the Flow
Use the Playground to test your enrichment logic with the following prompts:
* `Enrich the profile for john.doe@example.com in CentralStationCRM.`
* `Find and update the job title and company details for the contact with ID 5501.`
* `Check if the contact profile for Sarah Jenkins is complete; if not, fetch the latest professional data.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making layer, parsing input and determining the necessary enrichment steps.
* Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are an expert CRM data assistant. Analyze the contact profile provided, identify missing fields, and use the Composio Toolset to find the required information."
* Instruction: "Always verify the accuracy of the retrieved data before initiating an update to the CRM."

### 2) Composio Toolset Node
* Provide your API key within the Uplizd integration settings.
* Ensure the connection scope includes read/write permissions for your CRM and relevant enrichment APIs.

### 3) Tool Availability
* **CRM Connector**: For reading existing contact data and writing enriched updates.
* **Intelligence API**: For querying professional profiles, company firmographics, and contact verification services.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Specialized tool for deep-dive account research and lead intelligence.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Robust solution for multi-platform data synchronization and conflict resolution.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automated cleanup and formatting for maintaining CRM database health.
