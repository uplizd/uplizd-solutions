# LinkedIn Prospect Qualification Assistant (Uplizd) - Automate Lead Scoring and Enrichment

## Summary
The LinkedIn Prospect Qualification Assistant is an intelligent Uplizd workflow designed to streamline sales prospecting by automating the enrichment and scoring of LinkedIn leads. By integrating real-time profile data with your CRM, this solution eliminates manual research, ensures high-quality pipeline hygiene, and empowers sales teams to focus their outreach efforts on the most qualified prospects.

---

## Demo
![LinkedIn Prospect Qualification Assistant workflow dashboard showing profile enrichment and lead scoring nodes](image.png)
**Alt text (SEO-ready):** LinkedIn Prospect Qualification Assistant workflow in Uplizd for automated lead enrichment, sales prospecting, and CRM data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/51878a33-78a9-5ff0-99dd-5676d2756913)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** linkedin, lead qualification, sales prospecting, crm, lead scoring, data enrichment, composio, ai workflow
- This solution bridges the gap between raw LinkedIn profile data and actionable CRM insights to accelerate your sales cycle.

---

## Who is this for?
This assistant is built for revenue-focused teams looking to reduce manual data entry and improve lead conversion rates.

- **Sales Development Representatives (SDRs)**
    - Automate the initial research phase to identify high-intent leads faster.
- **Account Executives (AEs)**
    - Receive pre-qualified prospect summaries directly in your workflow to prepare for discovery calls.
- **RevOps Managers**
    - Standardize lead scoring criteria across the organization to maintain clean CRM data.
- **Growth Marketers**
    - Sync enriched lead signals to marketing platforms for targeted outreach campaigns.

---

## Features
- **Automated Profile Enrichment**
    - Leverages the AeroLeads integration to pull real-time professional data from LinkedIn profiles.
- **Intelligent Lead Scoring**
    - Applies custom logic to rank prospects based on job title, company size, and industry fit.
- **CRM Synchronization**
    - Automatically pushes qualified lead data into your CRM, ensuring a single source of truth.
- **Real-time Data Validation**
    - Cleans and formats incoming prospect data to prevent duplicate entries and maintain hygiene.
- **Customizable Qualification Logic**
    - Easily adjust scoring thresholds within the Agent node to match your specific Ideal Customer Profile (ICP).

---

## Use Cases
**Lead Prioritization**
- Automatically flag prospects that match your target persona for immediate follow-up.
- Filter out unqualified leads based on company size or industry to save time.

**Sales Pipeline Acceleration**
- Sync enriched contact details directly to your CRM to reduce manual data entry for the sales team.
- Trigger automated outreach sequences for prospects who meet the high-intent scoring threshold.

**Data Hygiene & Enrichment**
- Update existing CRM records with the latest professional information retrieved from LinkedIn.
- Standardize job titles and company names to ensure consistent reporting across your sales stack.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project to import the workflow.
3. Authenticate your LinkedIn and CRM integrations via the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the LinkedIn profile URL or prospect name.
- **Agent**: Processes the data, performs the lookup, and calculates the lead score.
- **Composio Toolset**: Executes the AeroLeads and CRM API calls to fetch and push data.
- **Chat Output**: Returns the enriched profile summary and qualification status.

### 3) Run the Flow
Use the Playground to test the assistant with these prompts:
- `Qualify this prospect: [LinkedIn Profile URL]`
- `Enrich and score this lead: [Prospect Name] at [Company Name]`
- `Check if this profile meets our ICP and update the CRM`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the operation, interpreting LinkedIn data and applying your business rules.
- Focus on extracting key professional attributes from the raw data.
- Apply the scoring rubric based on your specific ICP requirements.
- Format the final output for seamless CRM integration.

### 2) Composio Toolset Node
- Provide your API keys for AeroLeads and your CRM (e.g., Salesforce or HubSpot).
- Set the connection scope to allow read access to LinkedIn data and write access to your CRM contacts.

### 3) Tool Availability
- **AeroLeads API**: For retrieving professional profile details.
- **CRM Connector**: For creating or updating lead records.
- **Data Transformer**: For normalizing and cleaning input strings.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and identify key decision-makers.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep-dive research into target accounts using ZoomInfo.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) - Monitor and score deal opportunities within your pipeline.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple platforms to maintain consistency.
