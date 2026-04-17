# New Connection Qualifier (Uplizd) - Automate lead qualification and pipeline prioritization

## Summary
The New Connection Qualifier by Leadoku is an intelligent Uplizd workflow designed to streamline your sales outreach by automatically vetting incoming connections. By leveraging AI to analyze prospect data in real-time, this solution helps sales teams focus their energy on high-intent leads, ensuring pipeline velocity and improved data hygiene across your CRM.

---

## Demo
![New Connection Qualifier workflow interface showing lead data processing and qualification status](image.png)
**Alt text (SEO-ready):** New Connection Qualifier workflow in Uplizd for automated lead vetting, CRM data enrichment, and sales pipeline optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/969b77b7-a032-5bcc-a698-2e263036b842)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead qualification, crm, leadoku, sales pipeline, lead scoring, data enrichment, composio, ai workflow
- This solution bridges the gap between raw lead acquisition and actionable sales intelligence by automating the qualification process.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to eliminate manual lead vetting and accelerate their sales cycle.

- **Sales Development Representative (SDR)**
    - Automates the initial research phase, allowing for faster outreach to qualified prospects.
- **Revenue Operations Manager**
    - Ensures consistent lead scoring criteria and maintains high data quality within the CRM.
- **Growth Marketer**
    - Provides immediate feedback on campaign lead quality, enabling rapid iteration on targeting strategies.
- **Account Executive**
    - Focuses time exclusively on high-probability opportunities that meet specific qualification thresholds.

---

## Features
- **Automated Lead Scoring**
    - Instantly evaluates incoming connections against your ideal customer profile using AI-driven logic.
- **Real-time CRM Enrichment**
    - Automatically updates lead records with verified contact details and professional insights via the Composio Toolset.
- **Intelligent Routing**
    - Routes high-intent leads directly to the appropriate sales representative based on territory or industry.
- **Custom Qualification Logic**
    - Easily configure specific business rules and triggers to define what constitutes a "qualified" lead for your team.
- **Seamless Integration**
    - Connects directly with your existing CRM ecosystem to ensure a unified source of truth for all lead data.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads that match specific job titles or company sizes for immediate follow-up.
- Filter out low-intent connections to prevent sales teams from wasting time on unqualified prospects.

**CRM Data Hygiene**
- Standardize lead entry formats across your database to ensure clean, searchable records.
- Automatically append missing professional data points to new connections to improve outreach personalization.

**Pipeline Velocity**
- Trigger automated notifications to the sales team the moment a high-value lead is qualified.
- Reduce the time-to-first-contact by automating the initial qualification and data gathering steps.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and project destination.
3. Authenticate your CRM and Leadoku credentials within the workflow builder.
4. Ensure nodes are correctly mapped to your specific CRM fields and qualification criteria.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw lead data or trigger event from your growth campaign.
- **Agent**: Analyzes the input data against your defined qualification rules and scoring logic.
- **Composio Toolset**: Executes the necessary API calls to enrich data and update your CRM records.
- **Chat Output**: Delivers a summary of the qualification results and any actions taken to the user.

### 3) Run the Flow
Use the Playground to test the workflow with sample lead data:
- `Qualify this new lead: [Lead Name], [Company], [Job Title]`
- `Check if this connection meets our enterprise criteria and update the CRM`
- `Analyze the recent batch of connections and prioritize the top 5 leads`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine that interprets lead signals and applies your business logic.
- **Role**: Act as a senior sales operations analyst.
- **Instruction Pattern**:
    - Evaluate the prospect based on the provided Ideal Customer Profile (ICP).
    - Determine qualification status based on pre-defined scoring thresholds.
    - Format the output for seamless CRM entry.

### 2) Composio Toolset Node
- **API Key**: Ensure your Leadoku and CRM API keys are securely stored in the environment variables.
- **Connection Scope**: Grant read/write access to your CRM's lead and contact objects to enable automated updates.

### 3) Tool Availability
- **CRM Connector**: For reading lead data and writing qualification status updates.
- **Lead Enrichment API**: For gathering professional insights and verifying contact information.
- **Notification Service**: For alerting sales reps when high-value leads are identified.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data and professional insights.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage and track deal stages through the sales funnel.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms.
