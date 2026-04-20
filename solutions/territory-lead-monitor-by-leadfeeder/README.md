# Territory Lead Monitor (Uplizd) - Automated lead routing and territory management

## Summary
The Territory Lead Monitor is an intelligent Uplizd AI workflow that automates the identification and assignment of incoming leads based on geographic and firmographic data. By leveraging real-time data from Leadfeeder, this solution ensures that sales representatives receive qualified prospects within their designated territories, eliminating manual triage bottlenecks, reducing response times, and maintaining a single source of truth for pipeline distribution.

---

## Demo
![Territory Lead Monitor workflow showing Leadfeeder data ingestion, territory mapping, and CRM assignment](image.png)
**Alt text (SEO-ready):** Territory Lead Monitor Uplizd workflow, automated lead routing, Leadfeeder CRM integration, sales territory management, and AI-driven lead assignment.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c77235bf-a517-584e-a0e7-2d44f5ee6c88)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** leadfeeder, crm, territory management, lead routing, sales operations, pipeline velocity, composio, ai workflow
- This solution streamlines the sales funnel by connecting intent-based lead data directly to regional sales workflows.

---

## Who is this for?
This workflow is designed for revenue teams looking to optimize lead distribution and ensure high-value prospects are handled by the correct regional experts.

- **Sales Operations Manager**
    - Ensures equitable lead distribution and reduces manual administrative overhead in territory assignment.
- **Account Executive**
    - Receives qualified, territory-specific leads directly in their pipeline, allowing for faster outreach and higher conversion.
- **Revenue Operations (RevOps) Lead**
    - Maintains data hygiene and pipeline velocity by automating the handoff between intent signals and sales action.
- **BDR/SDR Team Lead**
    - Improves team productivity by ensuring reps only focus on leads that match their assigned geographic or vertical focus.

---

## Features
- **Intelligent Territory Mapping**
    - Automatically matches incoming lead signals from Leadfeeder against predefined geographic or industry-based territory rules.
- **Real-Time Lead Enrichment**
    - Uses the Composio Toolset to pull firmographic context, ensuring the agent has full visibility into the lead's company size and industry before routing.
- **Automated CRM Assignment**
    - Seamlessly updates lead ownership in your connected CRM, ensuring the right rep is notified the moment a lead is identified.
- **Customizable Routing Logic**
    - Easily adjust assignment thresholds or territory boundaries within the Agent node to adapt to changing team structures.
- **Pipeline Velocity Tracking**
    - Reduces the "time-to-first-touch" by removing manual triage steps from the lead qualification process.

---

## Use Cases
**Regional Sales Optimization**
- Automatically route leads from specific countries or states to the corresponding regional sales representative.
- Reassign stalled leads to different territories if the primary representative is unavailable or at capacity.

**Firmographic Lead Qualification**
- Filter incoming Leadfeeder signals by company revenue or employee count before triggering a territory assignment.
- Prioritize high-intent leads that match specific industry verticals for immediate outreach by specialized account teams.

**Pipeline Hygiene and Management**
- Sync lead status updates between Leadfeeder and your CRM to ensure no lead is left unassigned or duplicated.
- Generate automated reports on lead distribution volume across different territories to identify coverage gaps.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Connect your Leadfeeder and CRM accounts via the Composio Toolset.
3. Configure your territory mapping rules within the Agent node instructions.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data or trigger signals from the Leadfeeder integration.
- **Agent**: Processes lead information, evaluates territory criteria, and determines the appropriate sales owner.
- **Composio Toolset**: Executes the API calls to update CRM records and fetch additional lead context.
- **Chat Output**: Confirms the successful routing and assignment of the lead to the sales representative.

### 3) Run the Flow
Use the Playground to test your routing logic with these prompts:
- `Route all incoming leads from the DACH region to the EMEA sales team.`
- `Check the latest Leadfeeder signals and assign companies with over 500 employees to the Enterprise account team.`
- `Verify the current territory assignment for the lead associated with company ID 98765.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central decision-maker for lead routing.
- Define clear geographic boundaries and territory rules in the system prompt.
- Set the agent to prioritize high-intent leads based on Leadfeeder signal scores.
- Instruct the agent to handle exceptions by routing unmapped leads to a general sales queue.

### 2) Composio Toolset Node
- Provide your API keys for Leadfeeder and your primary CRM (e.g., Salesforce, HubSpot).
- Ensure the connection scope includes read/write permissions for lead objects and user assignment fields.

### 3) Tool Availability
- **Leadfeeder API**: For fetching real-time visitor and company intent data.
- **CRM Connector**: For updating lead ownership, status, and custom territory fields.
- **Data Parser**: For normalizing lead address and location data before territory matching.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed firmographic reports for your target accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent lead and contact data across multiple platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up cadences for your sales team.
