# Sales Lead Phone Enrichment Agent (Uplizd) - Real-time phone intelligence for lead qualification

## Summary
The Sales Lead Phone Enrichment Agent automates the verification and enrichment of lead contact data using CallerAPI, enabling sales teams to prioritize high-intent prospects with validated phone numbers. By integrating real-time intelligence directly into your CRM pipeline, this Uplizd workflow eliminates manual research, reduces bounce rates, and accelerates lead qualification velocity.

---

## Demo
![Sales Lead Phone Enrichment Agent workflow diagram showing lead input, CallerAPI enrichment, and CRM update](image.png)
**Alt text (SEO-ready):** Sales Lead Phone Enrichment Agent workflow using CallerAPI for CRM data hygiene, lead qualification, and automated contact verification on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0ea1e537-c00b-5491-bbfb-03e130b4a912)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, callerapi, lead enrichment, sales intelligence, data hygiene, composio, ai workflow, lead qualification
- This solution bridges the gap between raw lead capture and actionable sales intelligence by automating phone number validation and metadata enrichment.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to optimize their outbound efforts and improve data accuracy.

- **Sales Development Representative (SDR)**
    - Focuses on high-quality outreach by ensuring every lead has a verified and enriched phone number before calling.
- **Revenue Operations (RevOps) Manager**
    - Maintains CRM data hygiene by automating the enrichment process and reducing manual entry errors.
- **Sales Manager**
    - Increases team productivity by providing reps with enriched lead signals that prioritize the most promising opportunities.
- **Growth Marketer**
    - Improves lead-to-opportunity conversion rates by ensuring marketing-qualified leads are fully enriched for the sales team.

---

## Features
- **Real-time Phone Validation**
    - Instantly verifies phone number validity and carrier details via CallerAPI to ensure outreach efforts are directed at reachable prospects.
- **Automated Data Enrichment**
    - Automatically appends missing contact metadata to CRM records, providing sales reps with a complete view of their leads.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely connect the AI agent with your CRM and CallerAPI for seamless data flow.
- **Intelligent Lead Scoring**
    - Uses enriched phone data to help qualify leads based on location, carrier type, and line status, surfacing high-priority targets.
- **Pipeline Hygiene Automation**
    - Keeps CRM records clean and up-to-date by triggering enrichment workflows the moment a new lead enters the system.

---

## Use Cases
**Outbound Sales Optimization**
- Automatically enrich incoming web leads with phone intelligence to enable immediate, high-confidence follow-up calls.
- Filter out invalid or landline numbers from outbound calling lists to maximize SDR talk time and efficiency.

**CRM Data Management**
- Clean up legacy lead databases by running bulk enrichment jobs to identify and update outdated contact information.
- Standardize phone number formatting across global lead lists to ensure compatibility with automated dialers.

**Lead Qualification Strategy**
- Prioritize leads based on enriched carrier data, focusing sales efforts on prospects with verified mobile numbers.
- Flag leads with missing or suspicious contact data for manual review before they reach the high-priority sales queue.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Sales Lead Phone Enrichment template from the marketplace.
3. Connect your CRM and CallerAPI credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead record or phone number string to be processed.
- **Agent**: Analyzes the lead data and determines the necessary enrichment steps.
- **Composio Toolset**: Executes the CallerAPI lookups and updates the CRM fields.
- **Chat Output**: Returns the enriched lead profile and verification status to the user.

### 3) Run the Flow
Use the Playground to test your agent with the following prompts:
- `Enrich the lead record for +1-555-010-9988 and update the CRM.`
- `Verify the phone number for John Doe and add carrier details to the lead profile.`
- `Check if the phone number in lead ID 4567 is a valid mobile line.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer between your CRM and the enrichment service.
- Use a model capable of structured data extraction (e.g., GPT-4o).
- Instruct the agent to prioritize CallerAPI results over existing CRM data.
- Ensure the agent is configured to handle null values gracefully if a number cannot be enriched.

### 2) Composio Toolset Node
- Provide your CallerAPI and CRM API keys within the Composio configuration.
- Set the connection scope to allow read/write access to lead objects and phone fields.

### 3) Tool Availability
- **CallerAPI**: Phone validation, carrier lookup, and line type identification.
- **CRM Connector**: Search lead, update contact field, and fetch lead metadata.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account records with firmographic data and contact details.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Automate bulk cleanup and formatting of CRM contact records.
- [WhatsApp Lead Qualifier](../whats-app-lead-qualifier-by-whatsapp/README.md) - Qualify leads directly through automated WhatsApp messaging workflows.
