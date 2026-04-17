# Lead Scoring & Qualification Agent (Uplizd) - Automate lead prioritization and data enrichment

## Summary
The Lead Scoring & Qualification Agent by Hunter is an intelligent automation workflow designed to streamline sales operations by analyzing incoming lead data in real-time. By leveraging Hunter’s email intelligence and company data, this agent automatically qualifies prospects, assigns scores based on predefined criteria, and updates your CRM, ensuring your sales team focuses their efforts on high-intent opportunities with maximum pipeline velocity.

---

## Demo
![Lead Scoring & Qualification Agent workflow diagram showing email input, Hunter data enrichment, and CRM scoring](image.png)
**Alt text (SEO-ready):** Lead Scoring and Qualification Agent by Uplizd, showing automated lead enrichment, CRM data sync, and sales pipeline prioritization workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b8757d03-6b06-5e09-bfb6-ae792a9aa936)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead scoring, crm, hunter, salesforce, data enrichment, pipeline, qualification, ai workflow
- This solution bridges the gap between raw lead intake and actionable sales intelligence by automating the qualification process.

---

## Who is this for?
This agent is designed for revenue-focused teams looking to eliminate manual data entry and prioritize high-value prospects.

- **Sales Development Representative (SDR)**
    - Reduces time spent researching lead validity, allowing for faster outreach to qualified prospects.
- **Revenue Operations (RevOps) Manager**
    - Ensures consistent lead scoring logic across the organization, improving overall data hygiene.
- **Account Executive (AE)**
    - Receives pre-qualified leads with enriched context, increasing the likelihood of successful discovery calls.
- **Marketing Operations Specialist**
    - Bridges the gap between lead generation campaigns and sales readiness by automating the handoff process.

---

## Features
- **Automated Email Verification**
    - Instantly validates lead contact information using Hunter’s API to ensure high deliverability and data accuracy.
- **Intelligent Lead Scoring**
    - Applies dynamic scoring logic based on company size, industry, and email patterns to rank leads by conversion potential.
- **CRM Data Synchronization**
    - Automatically pushes enriched data and qualification status to your CRM, maintaining a single source of truth.
- **Real-time Enrichment**
    - Fetches professional context and company details for every new lead, providing the sales team with immediate insights.
- **Customizable Qualification Rules**
    - Allows users to define specific thresholds for "Sales Ready" status, ensuring the agent aligns with unique business goals.

---

## Use Cases
**Lead Prioritization**
- Automatically flag high-intent leads that match your ideal customer profile (ICP) for immediate follow-up.
- Filter out low-quality or invalid email addresses to prevent wasted effort in the sales pipeline.

**CRM Data Hygiene**
- Update existing CRM records with the latest company intelligence gathered from Hunter.
- Standardize lead entry formats to ensure clean, searchable data for reporting and analytics.

**Sales Pipeline Acceleration**
- Trigger automated notifications to the assigned sales owner when a lead reaches a high-priority score.
- Reduce the time-to-contact window by automating the initial research and qualification steps.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the builder.
2. Connect your Hunter API key and CRM credentials within the integration settings.
3. Review the default scoring logic to ensure it aligns with your specific business requirements.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead data (email, company name, or landing page submission).
- **Agent**: Analyzes the lead, executes scoring logic, and determines qualification status.
- **Composio Toolset**: Connects to Hunter and your CRM to fetch data and push updates.
- **Chat Output**: Returns the final qualification status and lead score to the user or logs it in the CRM.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Score the lead: john.doe@example-company.com and update the CRM.`
- `Verify the contact details for this lead and provide a qualification score.`
- `Check if this lead meets our enterprise criteria based on their company data.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a sales intelligence analyst, prioritizing accuracy and data-driven decision-making.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a lead qualification expert. Use the provided tools to verify emails and score leads based on the defined ICP."
- Instruction: "Always prioritize data accuracy; if a lead cannot be verified, mark as 'Needs Manual Review'."

### 2) Composio Toolset Node
- Provide your Hunter API key to enable email and company data lookups.
- Ensure the CRM connection (e.g., Salesforce or HubSpot) has read/write permissions for Lead/Contact objects.

### 3) Tool Availability
- **Hunter API**: Email verification, domain search, and company profile lookup.
- **CRM Connector**: Search, update, and create lead records.
- **Data Processor**: Logic for calculating scores based on retrieved attributes.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and identify key decision-makers.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage sales stages and track deal velocity.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
