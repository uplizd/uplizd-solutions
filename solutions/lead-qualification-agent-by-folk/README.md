# Lead Qualification Agent (Uplizd) - Automate lead scoring and enrichment in Folk CRM

## Summary
The Lead Qualification Agent is an intelligent Uplizd workflow designed to streamline your sales pipeline by automatically qualifying and enriching incoming leads within Folk CRM. By leveraging AI to analyze lead data and cross-reference it with external intelligence, this solution eliminates manual data entry, ensures your sales team focuses only on high-intent prospects, and maintains a clean, actionable CRM database.

---

## Demo
![Lead Qualification Agent workflow showing Chat Input, AI Agent, Folk CRM integration, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow in Uplizd integrating with Folk CRM for automated lead scoring, data enrichment, and sales pipeline optimization.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a9118ffe-b2f7-55ba-91f7-09d6a936680e)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** folk, crm, lead qualification, sales pipeline, data enrichment, ai workflow, composio, revenue operations
- This solution bridges the gap between raw lead intake and sales readiness by automating the qualification process within your existing CRM ecosystem.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to maximize pipeline velocity and lead conversion rates.

- **Sales Development Representative (SDR)**
    - Spend less time researching prospects and more time engaging with qualified leads.
- **Revenue Operations Manager**
    - Ensure CRM data hygiene by enforcing standardized qualification criteria across all incoming leads.
- **Growth Marketer**
    - Gain immediate feedback on lead quality to optimize top-of-funnel acquisition strategies.
- **Account Executive (AE)**
    - Receive pre-qualified opportunities with enriched context, allowing for more personalized outreach.

---

## Features
- **Automated Lead Scoring**
    - Instantly evaluate lead quality based on custom business logic and firmographic data.
- **Real-time Data Enrichment**
    - Automatically pull missing contact details and company insights using the Composio Toolset.
- **Folk CRM Integration**
    - Seamlessly update lead statuses, add tags, and sync notes directly into your Folk workspace.
- **Intelligent Routing**
    - Categorize leads by intent and assign them to the appropriate sales queue based on qualification tier.
- **Customizable Logic**
    - Easily adjust the Agent's qualification criteria to match your evolving ideal customer profile (ICP).

---

## Use Cases
**Pipeline Acceleration**
- Automatically flag high-intent leads for immediate outreach by the sales team.
- Move qualified leads through pipeline stages without manual intervention.

**Data Hygiene & Enrichment**
- Populate empty fields in Folk CRM with verified company size, industry, and social profiles.
- Standardize lead formatting to prevent duplicate entries and maintain a clean database.

**Sales Performance Optimization**
- Filter out low-quality leads to prevent SDRs from wasting time on dead-end prospects.
- Generate summary reports of qualification trends to identify high-performing lead sources.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Folk CRM account within the Composio Toolset node.
4. Ensure nodes are connected in the sequence: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives raw lead data or trigger events from your lead capture forms.
*   **Agent**: Processes the lead information against your defined qualification criteria.
*   **Composio Toolset**: Executes API calls to Folk CRM to fetch, update, or enrich lead records.
*   **Chat Output**: Returns the qualification status and summary of actions taken to the user.

### 3) Run the Flow
Use the Uplizd Playground to test your agent with these example prompts:
* `Qualify the new lead added to Folk CRM with email contact@example.com.`
* `Enrich the profile for the lead 'Acme Corp' and update their status to 'Qualified'.`
* `Check if the latest lead in Folk meets our B2B SaaS qualification criteria.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your lead qualification process.
* **Instruction Pattern:**
    * Define your specific ICP (Ideal Customer Profile) and lead scoring thresholds clearly.
    * Instruct the agent to prioritize data accuracy when performing enrichment lookups.
    * Set strict output formatting rules for CRM field updates to ensure data consistency.

### 2) Composio Toolset Node
* Requires a valid Folk CRM API key provided via the Composio dashboard.
* Ensure the connection scope includes read/write permissions for Leads, Contacts, and Organizations.

### 3) Tool Availability
* **Lead Search**: Locate existing records by email or company name.
* **Data Enrichment**: Fetch external firmographic data to fill CRM gaps.
* **Record Update**: Modify lead status, priority, and custom fields in Folk.
* **Note Creation**: Log qualification summaries directly onto the lead profile.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data with deep firmographic insights.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automate research tasks for target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain synchronization across multiple CRM platforms.
