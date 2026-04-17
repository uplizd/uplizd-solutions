# LinkedIn Company Intelligence Agent (Uplizd) - Automate firmographic research and competitive monitoring

## Summary
The LinkedIn Company Intelligence Agent is an automated Uplizd workflow designed to streamline corporate research by extracting, synthesizing, and reporting on company activities directly from LinkedIn. By leveraging the Composio Toolset, this agent eliminates manual data entry and browser-based research, providing RevOps and Sales teams with a single source of truth for competitive intelligence, account mapping, and lead qualification, ultimately increasing pipeline velocity and data hygiene.

---

## Demo
![LinkedIn Company Intelligence Agent workflow dashboard showing automated data extraction from LinkedIn profiles to CRM records](image.png)
**Alt text (SEO-ready):** LinkedIn Company Intelligence Agent workflow by Uplizd, automated firmographic research, LinkedIn data extraction, and CRM integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAHAAABAAABAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEA1v8HAA==)](https://uplizd.ai/solutions/e28ec740-ed13-5872-bc33-06a43027d11f)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** linkedin, company intelligence, crm, salesforce, lead qualification, competitive analysis, data enrichment, composio, ai workflow
- This solution bridges the gap between public professional network data and internal CRM systems to automate account research.

---

## Who is this for?
This agent is built for professionals who need to maintain high-quality account data without the manual burden of platform-hopping.

- **Sales Development Representatives (SDRs)**
  - Accelerate lead qualification by instantly pulling firmographic data into the sales pipeline.
- **Account Executives (AEs)**
  - Gain competitive intelligence on target accounts before high-stakes discovery calls.
- **Revenue Operations (RevOps) Managers**
  - Ensure CRM data hygiene by automating the synchronization of verified company details.
- **Market Researchers**
  - Monitor industry trends and company growth signals across the LinkedIn ecosystem at scale.

---

## Features
- **Automated Profile Extraction**
  - Uses the Composio Toolset to fetch real-time company data, employee counts, and recent posts from LinkedIn.
- **CRM Synchronization**
  - Seamlessly maps extracted intelligence to fields in Salesforce, HubSpot, or Dynamics 365.
- **Competitive Signal Monitoring**
  - Detects changes in company leadership, funding rounds, or hiring patterns to trigger sales alerts.
- **Intelligent Data Formatting**
  - Cleans and standardizes raw LinkedIn data into structured formats suitable for CRM ingestion.
- **Real-time Alerting**
  - Configures automated notifications when target accounts meet specific growth or activity criteria.

---

## Use Cases
**Competitive Intelligence**
- Monitor competitor product launches and market positioning by tracking official company page updates.
- Aggregate recent company news to build a "pre-call" briefing document for sales teams.

**Account Enrichment**
- Automatically populate empty CRM fields like "Company Size," "Industry," and "Headquarters" using LinkedIn data.
- Identify key stakeholders and decision-makers within a target account based on current role listings.

**Lead Qualification**
- Score incoming leads based on firmographic fit against ideal customer profile (ICP) parameters.
- Filter out unqualified prospects by verifying company status and activity levels before routing to the sales team.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the LinkedIn Company Intelligence Agent.
2. Click "Import" to add the workflow to your private workspace.
3. Connect your LinkedIn and CRM credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company URL or name from the user.
- **Agent**: Processes the request, determines the necessary search parameters, and formulates the data extraction logic.
- **Composio Toolset**: Executes the authenticated LinkedIn API calls to retrieve company intelligence.
- **Chat Output**: Returns the structured summary and confirms the update to the CRM.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Research the recent activity and growth signals for [Company Name].`
- `Extract the latest company updates for this profile: [LinkedIn URL] and update my CRM.`
- `Find the key leadership changes for [Company Name] and summarize them for my sales team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a research analyst. Use the following instruction pattern:
- Focus on extracting firmographic data and key business signals.
- Maintain a professional, concise tone for all summaries.
- Prioritize data accuracy by cross-referencing LinkedIn fields with CRM requirements.

### 2) Composio Toolset Node
- Provide a valid LinkedIn API key within the Composio dashboard.
- Set the connection scope to "Read-Only" for company pages to ensure compliance and data security.

### 3) Tool Availability
- **LinkedIn Search**: For locating company profiles and public page data.
- **CRM Write/Update**: For pushing enriched data into your specific CRM instance.
- **Data Parser**: For cleaning and normalizing text strings extracted from social feeds.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data using external intelligence sources.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep-dive research and contact discovery for sales teams.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize and resolve data conflicts across multiple CRM platforms.
- [Deal Opportunity Tracker](../deal-opportunity-tracker/README.md) — Identify and score high-value sales opportunities.
