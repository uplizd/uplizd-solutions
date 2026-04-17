# Relationship Mapping Agent (Uplizd) - Automated CRM connection visualization and network intelligence

## Summary
The Relationship Mapping Agent is an intelligent Uplizd workflow designed to automatically map and visualize professional connections between contacts and companies within Folk CRM. By leveraging AI to analyze interaction history and organizational data, this solution helps sales and operations teams identify key stakeholders, uncover hidden network paths, and accelerate pipeline velocity through improved relationship intelligence.

---

## Demo
![Relationship Mapping Agent workflow visualizing connections between contacts and companies in Folk CRM](image.png)
**Alt text (SEO-ready):** Relationship mapping agent for Folk CRM, Uplizd AI workflow, automated network visualization, and sales intelligence integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/relationship-mapping-agent-by-folk)

---

## Category
**Primary category**: Sales automation  
**Secondary tags**: crm, folk, relationship mapping, network intelligence, sales operations, pipeline velocity, data enrichment, ai workflow  
This solution bridges the gap between raw CRM data and actionable network insights, empowering teams to visualize complex stakeholder relationships.

---

## Who is this for?
This solution is built for revenue-focused teams looking to turn static contact lists into dynamic relationship maps.

- **Account Executives**
    - Identifies key decision-makers and influencers within a target account to shorten sales cycles.
- **Sales Operations Managers**
    - Automates the maintenance of relationship data, ensuring the CRM remains a reliable source of truth.
- **Business Development Representatives**
    - Uncovers warm introduction paths by analyzing existing connections between current clients and prospects.
- **Customer Success Managers**
    - Monitors account health by mapping the depth and breadth of relationships across key client organizations.

---

## Features
- **Automated Network Discovery**
    - Uses AI to scan Folk CRM interaction logs and identify previously unmapped connections between entities.
- **Stakeholder Visualization**
    - Generates clear, hierarchical maps of professional relationships to simplify complex account structures.
- **Real-time Data Sync**
    - Ensures that relationship maps are updated instantly as new communications or meetings are logged in the CRM.
- **Composio-Powered CRM Integration**
    - Leverages the Composio Toolset to securely read and write relationship data directly to Folk CRM.
- **Actionable Intelligence Scoring**
    - Ranks connections based on interaction frequency and recency to highlight the strongest paths to a prospect.

---

## Use Cases
**Strategic Account Planning**
- Mapping the organizational chart of a target enterprise to identify the primary champion and potential blockers.
- Visualizing the history of touchpoints across a buying committee to ensure balanced engagement.

**Pipeline Acceleration**
- Identifying "warm" paths to a new lead by finding mutual connections within the existing client base.
- Highlighting stalled opportunities that lack sufficient relationship depth, prompting immediate outreach.

**Data Hygiene & Enrichment**
- Automatically cleaning up duplicate or orphaned contact records by linking them to the correct parent company.
- Enriching contact profiles with relationship metadata to provide a 360-degree view of account activity.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Relationship Mapping Agent.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Folk CRM account via the Composio integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the target company or contact name for mapping.
- **Agent**: Analyzes the request and queries the CRM for relevant relationship data.
- **Composio Toolset**: Executes API calls to fetch and structure interaction data from Folk.
- **Chat Output**: Displays the visualized relationship map or summary of network intelligence.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Map all stakeholders for [Company Name] and identify the strongest connection path.`
- `Which contacts at [Company Name] have we engaged with in the last 30 days?`
- `Analyze the relationship strength between our team and the decision-makers at [Company Name].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a CRM intelligence analyst.
- **Instruction Pattern**:
    - Focus on identifying high-value connections based on interaction frequency.
    - Maintain strict data privacy by only accessing authorized CRM records.
    - Prioritize recent engagement data when calculating relationship strength.

### 2) Composio Toolset Node
- **API Key**: Ensure your Folk CRM API key is active within the Composio dashboard.
- **Connection Scope**: Grant read/write access to contacts, companies, and interaction logs.

### 3) Tool Availability
- **CRM Read**: Fetch contact, company, and interaction history.
- **Relationship Analyzer**: Process interaction frequency and recency.
- **Data Mapper**: Structure and format the output for visualization.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates deep-dive research into target accounts and prospect profiles.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Synchronizes relationship data across Dynamics 365 environments.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Tracks and manages sales stages to improve overall pipeline health.
