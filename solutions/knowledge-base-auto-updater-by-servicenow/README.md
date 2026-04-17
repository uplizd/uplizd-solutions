# Knowledge Base Auto-Updater (Uplizd) - Automate documentation updates from resolved incidents

## Summary
The Knowledge Base Auto-Updater is an intelligent Uplizd workflow that bridges the gap between IT support and documentation by automatically synthesizing resolved incident data into actionable knowledge base articles. By leveraging AI to extract key resolutions and update your ServiceNow repository in real-time, this solution eliminates manual documentation bottlenecks, ensures your support team has access to the latest troubleshooting steps, and maintains a single source of truth for organizational knowledge.

---

## Demo
![Knowledge Base Auto-Updater workflow showing incident resolution data flowing into a ServiceNow knowledge article update](image.png)
**Alt text (SEO-ready):** Knowledge Base Auto-Updater workflow for ServiceNow, featuring automated incident-to-article conversion, Uplizd AI integration, and Composio toolset synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/db6acbd6-a5a8-5b07-b1a9-97e63fdc2463)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** servicenow, knowledge management, incident response, automation, ai workflow, documentation, composio, data sync
- This solution streamlines IT operations by transforming reactive incident resolution into proactive knowledge base maintenance.

---

## Who is this for?
This solution is designed for IT and Support teams looking to reduce documentation debt and improve self-service resolution rates.

- **Knowledge Manager**
    - Ensures that the knowledge base remains current without requiring manual intervention from support engineers.
- **IT Support Lead**
    - Reduces the time spent on repetitive tickets by surfacing proven resolutions directly in the knowledge portal.
- **Service Desk Analyst**
    - Focuses on solving complex issues while the AI handles the administrative burden of documenting the solution.
- **Operations Manager**
    - Improves overall team velocity and documentation hygiene across the entire IT service management lifecycle.

---

## Features
- **Automated Incident Parsing**
    - Uses AI to extract the root cause and resolution steps from closed ServiceNow incident tickets.
- **Intelligent Article Drafting**
    - Generates structured, professional knowledge base content formatted for immediate publication.
- **Composio-Powered ServiceNow Integration**
    - Seamlessly connects with ServiceNow to read incident data and write updates to the knowledge base.
- **Real-time Sync**
    - Triggers updates immediately upon incident resolution, ensuring documentation never lags behind operations.
- **Quality Assurance Layer**
    - Configurable agent instructions ensure that generated articles meet internal style and compliance standards.

---

## Use Cases
**Incident Resolution Documentation**
- Automatically draft a "How-to" article when a specific error code is resolved.
- Update existing articles with new troubleshooting steps derived from recent high-frequency tickets.

**Knowledge Base Maintenance**
- Identify outdated articles that conflict with recent incident resolutions and flag them for review.
- Consolidate multiple incident resolutions into a single comprehensive FAQ entry.

**Support Efficiency**
- Reduce ticket deflection rates by surfacing newly generated articles to end-users in the self-service portal.
- Standardize the format of technical documentation across different support tiers.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Knowledge Base Auto-Updater template file.
3. Connect your ServiceNow instance via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the incident ID or resolution summary trigger.
- **Agent**: Processes the incident text and drafts the knowledge article content.
- **Composio Toolset**: Executes the API calls to update or create the article in ServiceNow.
- **Chat Output**: Confirms the successful creation or update of the knowledge article.

### 3) Run the Flow
Use the Playground to test the workflow with these prompts:
- `Update the knowledge base with the resolution steps for incident INC-99281.`
- `Draft a new article based on the recent fix for the VPN connection failure incident.`
- `Review the last 5 resolved incidents and suggest updates for the 'Network Troubleshooting' category.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical writer and documentation specialist.
- Focus on extracting technical steps while removing PII or sensitive customer data.
- Maintain a consistent professional tone suitable for internal and external knowledge bases.
- Prioritize clarity and conciseness in the generated troubleshooting procedures.

### 2) Composio Toolset Node
- Requires a valid ServiceNow API key with read/write permissions for the Knowledge Base module.
- Connection scope should be limited to the specific knowledge base instances you wish to automate.

### 3) Tool Availability
- `servicenow_get_incident`: Fetches ticket details and resolution notes.
- `servicenow_create_article`: Publishes the drafted content to the knowledge base.
- `servicenow_update_article`: Modifies existing articles with new resolution insights.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md) - AI-driven assistant for managing customer support inquiries.
- [account-relationship-builder-by-dynamics365](../account-relationship-builder-by-dynamics365/README.md) - Automate CRM relationship tracking and data enrichment.
- [workflow-automation-agent-by-jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline business processes and task management.
