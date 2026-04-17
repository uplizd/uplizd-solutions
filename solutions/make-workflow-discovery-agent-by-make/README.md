# Make Workflow Discovery Agent (Uplizd) - Automated workflow mapping and operation discovery

## Summary
The Make Workflow Discovery Agent is an intelligent automation solution designed to streamline the exploration and documentation of available operations within your Make (formerly Integromat) environment. By leveraging the Composio Toolset, this agent identifies, maps, and categorizes workflow triggers and actions, providing RevOps and automation engineers with a single source of truth for their integration architecture and reducing the time spent on manual pipeline discovery.

---

## Demo
![Make Workflow Discovery Agent interface showing automated operation mapping and workflow documentation](image.png)
**Alt text (SEO-ready):** Make Workflow Discovery Agent interface showing automated operation mapping, workflow documentation, and integration discovery using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4f868dca-787f-5fd0-bbe6-e4b2f782881d)

---

## Category
**Primary category:** Operations automation
**Secondary tags:** make, integromat, workflow discovery, automation mapping, integration, composio, ai agent, pipeline hygiene.
This solution bridges the gap between complex automation platforms and human-readable documentation, ensuring your Make workflows remain transparent and scalable.

---

## Who is this for?
This agent is built for technical teams looking to maintain visibility over their automation stack.

* **Automation Engineer**
    * Rapidly audit existing Make scenarios to identify bottlenecks or redundant operations.
* **RevOps Manager**
    * Maintain a clear inventory of data-sync workflows across the organization's tech stack.
* **Systems Architect**
    * Map complex cross-platform integrations to ensure compliance and data integrity.
* **Technical Product Manager**
    * Quickly generate documentation for new workflow deployments without manual mapping.

---

## Features
- **Automated Operation Mapping**
  Instantly scan and index available triggers and actions within your Make account.
- **Workflow Dependency Tracking**
  Visualize how data flows between different modules and third-party applications.
- **Intelligent Documentation Generation**
  Automatically create structured summaries of workflow logic and integration points.
- **Real-time Integration Sync**
  Leverage the Composio Toolset to fetch the latest API capabilities and module updates.
- **Pipeline Hygiene Reporting**
  Identify inactive or broken workflows that require maintenance or optimization.

---

## Use Cases
**Workflow Audit & Compliance**
* Perform quarterly audits of all active Make scenarios to ensure data privacy standards.
* Generate documentation for internal stakeholders regarding how data moves between CRM and marketing tools.

**Integration Discovery**
* Discover hidden automation opportunities by identifying manual tasks that have available Make modules.
* Map out the dependencies of a new integration before deploying it to production.

**System Optimization**
* Identify and consolidate redundant workflow steps to reduce execution costs and increase pipeline velocity.
* Monitor the health of critical data syncs by tracking successful operation patterns.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Make Workflow Discovery Agent template from the marketplace.
3. Connect your Make API credentials via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives your natural language request to discover or map specific workflows.
* **Agent**: Processes the request and determines which Make operations to query via the toolset.
* **Composio Toolset**: Executes the API calls to fetch real-time data from your Make account.
* **Chat Output**: Delivers the structured discovery report or workflow map back to the user.

### 3) Run the Flow
Use the Playground to test your agent with prompts like:
* `List all active workflows that involve Salesforce and HubSpot.`
* `Map the dependencies for the 'Lead Enrichment' scenario.`
* `Find any inactive workflows that haven't been triggered in the last 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical analyst, translating user queries into API-compatible search parameters.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruct the agent to prioritize accuracy when mapping module connections.
* Ensure the agent maintains a professional, technical tone in its output reports.

### 2) Composio Toolset Node
* Provide your Make API Key within the Composio configuration panel.
* Set the connection scope to include read-only access for scenarios and modules to ensure security.

### 3) Tool Availability
* **Scenario Discovery**: Fetch lists of all scenarios and their current status.
* **Module Inspection**: Retrieve detailed configurations for specific workflow steps.
* **Log Analysis**: Query execution history to identify performance trends.

---

## Related Solutions
* [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) — Automate task management and workflow triggers within JobNimbus.
* [Workflow Health Monitor (DailyBot)](../workflow-health-monitor-by-dailybot/README.md) — Track the operational health and status of your daily automation workflows.
* [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Synchronize data across platforms with conflict resolution and real-time updates.
