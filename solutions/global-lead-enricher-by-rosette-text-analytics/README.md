# Global Lead Enricher (Uplizd) - Automated international lead data standardization and enrichment

## Summary
The Global Lead Enricher is an intelligent Uplizd workflow designed to automate the processing of international sales leads. By leveraging advanced text analytics to detect language and standardize entity information, this solution ensures your CRM maintains high-quality, actionable data regardless of the lead's origin. It eliminates manual data entry, reduces lead decay, and accelerates pipeline velocity by providing a single source of truth for global prospect information.

---

## Demo
![Global Lead Enricher workflow dashboard showing language detection and entity extraction nodes](image.png)
**Alt text (SEO-ready):** Global Lead Enricher Uplizd workflow dashboard showing language detection, entity extraction, and CRM data enrichment integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ddb0f0b3-7ea5-596c-afe1-48a559206244)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead enrichment, data hygiene, international sales, entity extraction, composio, ai workflow, data sync
- This solution bridges the gap between raw international lead inputs and structured CRM records through automated linguistic and entity analysis.

---

## Who is this for?
This solution is designed for revenue-focused teams managing diverse, global lead pipelines.

- **Sales Operations Manager**
    - Automates data standardization across regions to ensure consistent reporting and territory management.
- **BDR/SDR Lead**
    - Increases outreach efficiency by ensuring lead contact information is accurately parsed and enriched before engagement.
- **Revenue Operations (RevOps) Analyst**
    - Maintains high data hygiene standards by automatically validating and formatting international lead entities.
- **Global Sales Director**
    - Gains visibility into international market performance through cleaner, more reliable lead data in the CRM.

---

## Features
- **Automated Language Detection**
    - Instantly identifies the source language of incoming leads to route them to the appropriate regional sales workflows.
- **Entity Extraction Engine**
    - Uses Rosette text analytics to pull key information like organization names, locations, and titles from unstructured lead text.
- **CRM Data Synchronization**
    - Seamlessly pushes enriched data into your CRM using the Composio Toolset to update existing records or create new ones.
- **Real-time Data Hygiene**
    - Cleans and standardizes lead formats automatically, preventing duplicate entries and formatting errors in your database.
- **Scalable Pipeline Integration**
    - Connects directly to your existing sales stack, ensuring that enriched data flows instantly to the teams that need it most.

---

## Use Cases
**International Lead Processing**
- Automatically parse contact details from leads submitted in non-English languages.
- Standardize address and company entity formats for global territory assignment.

**CRM Data Enrichment**
- Populate missing fields in Salesforce or HubSpot by extracting data from unstructured lead notes.
- Update lead status based on enriched entity information to prioritize high-value international prospects.

**Sales Pipeline Optimization**
- Reduce the time spent on manual lead research by automating the initial enrichment phase.
- Improve lead routing accuracy by ensuring all international leads are tagged with correct regional and entity metadata.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your CRM and Rosette API credentials within the workflow settings.
4. Ensure nodes are correctly connected from the Chat Input through the Agent and Composio Toolset to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or text snippets from your lead capture forms.
- **Agent**: Processes the input, triggers language detection, and extracts entity data.
- **Composio Toolset**: Executes the API calls to sync the cleaned data into your CRM.
- **Chat Output**: Returns a confirmation message detailing the enriched lead information.

### 3) Run the Flow
Use the Uplizd Playground to test the enrichment capabilities:
- `Enrich this lead: "Jean-Pierre Dupont, Directeur chez TechSolutions, basé à Paris."`
- `Process this international lead: "Maria Garcia, Gerente de Ventas en Soluciones Globales, Madrid."`
- `Standardize and sync this lead: "Hiroshi Tanaka, Lead Engineer at Nippon Systems, Tokyo."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for linguistic analysis and CRM logic.
- Use a model capable of high-precision entity extraction (e.g., GPT-4o or Claude 3.5).
- Instruction pattern:
    - Detect the language of the provided input text.
    - Extract entities including Name, Job Title, Company, and Location.
    - Format the output into a JSON structure compatible with your CRM's API.

### 2) Composio Toolset Node
- Provide your API key to enable secure communication between the agent and your CRM.
- Set the connection scope to allow read/write access to lead and contact objects.

### 3) Tool Availability
- **CRM Connector**: For updating lead records (Salesforce, HubSpot, or Dynamics 365).
- **Text Analytics API**: For language detection and entity extraction.
- **Data Formatter**: For standardizing phone numbers, addresses, and date formats.

---

## Related Solutions
- [../account-intelligence-gatherer-by-dropcontact/README.md](../account-intelligence-gatherer-by-dropcontact/README.md) - Automate account intelligence gathering for enriched sales prospecting.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms with automated conflict resolution.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Maintain clean CRM records through automated data decay and formatting cleanup.
