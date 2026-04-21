# Space Inventory Agent (Uplizd) - Real-time Contentful workspace tracking and usage analytics

## Summary
The Space Inventory Agent is an automated Uplizd workflow designed to provide a single source of truth for your Contentful ecosystem. By leveraging the Composio Toolset to interface with Contentful APIs, this agent continuously monitors workspace metadata, asset usage, and content distribution metrics, ensuring your team maintains optimal hygiene and pipeline velocity across all digital environments.

---

## Demo
![Space Inventory Agent dashboard showing real-time Contentful workspace usage metrics and asset distribution analytics](image.png)

**Alt text (SEO-ready):** Space Inventory Agent dashboard showing real-time Contentful workspace usage metrics and asset distribution analytics for Uplizd AI workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0c2091f0-6236-50f1-8ee3-69aa6feabf2b)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** contentful, inventory, data hygiene, cms, api integration, composio, ai workflow, workspace management

This solution streamlines Contentful administration by automating the discovery and reporting of workspace assets and usage patterns.

---

## Who is this for?
This solution is designed for technical teams and content managers who need granular visibility into their CMS infrastructure.

* **Content Operations Manager**
    * Gains immediate visibility into workspace sprawl and redundant content assets.
* **Technical Architect**
    * Monitors API usage and workspace limits to prevent service interruptions.
* **Digital Marketing Lead**
    * Tracks content distribution across multiple spaces to ensure brand consistency.
* **System Administrator**
    * Automates the audit process for user access and space configuration compliance.

---

## Features
- **Real-time Workspace Discovery**
  Automatically scans and indexes all active Contentful spaces to provide an up-to-date inventory list.
- **Usage Analytics Engine**
  Aggregates data on content entries, asset counts, and API calls to identify high-traffic workspaces.
- **Automated Hygiene Reporting**
  Flags inactive or duplicate spaces, helping teams optimize their CMS footprint and reduce clutter.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely execute read/write operations against the Contentful Management API.
- **Proactive Alerting**
  Triggers notifications when workspace usage approaches predefined thresholds or when new spaces are provisioned.

---

## Use Cases
**CMS Infrastructure Audits**
* Generate a comprehensive report of all Contentful spaces and their associated environment configurations.
* Identify orphaned or unused workspaces that contribute to unnecessary complexity in the content pipeline.

**Resource Optimization**
* Analyze asset distribution across spaces to identify opportunities for content consolidation.
* Monitor API request volumes to ensure workspace performance remains within established service limits.

**Compliance and Governance**
* Verify that all active spaces adhere to organizational naming conventions and security policies.
* Automate the documentation of workspace permissions to streamline periodic security reviews.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your Contentful account via the integration settings.
3. Configure the environment variables for your specific organization ID.
4. Ensure nodes are correctly connected in the builder: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the user request or scheduled trigger command.
* **Agent:** Processes the intent and determines which Contentful API calls are required.
* **Composio Toolset:** Executes the authenticated requests to fetch workspace data.
* **Chat Output:** Formats the retrieved inventory data into a readable summary for the user.

### 3) Run the Flow
Use the Playground to test your agent with the following prompts:
* `List all active Contentful spaces and their current entry counts.`
* `Identify any workspaces that have not been updated in the last 30 days.`
* `Generate a summary report of total asset usage across all production spaces.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for API interactions.
* Use a model capable of structured data reasoning (e.g., GPT-4o).
* Instruction: "You are a Contentful expert. Use the provided tools to fetch workspace metadata and summarize it clearly."
* Instruction: "Always prioritize accurate data retrieval over conversational filler."

### 2) Composio Toolset Node
* Requires a valid Contentful API key with `Content Management` scope.
* Ensure the connection is authorized for the specific organization you wish to audit.

### 3) Tool Availability
* `contentful_get_spaces`: Retrieves the list of all spaces.
* `contentful_get_space_usage`: Fetches metrics for a specific space ID.
* `contentful_list_assets`: Queries asset metadata for inventory reporting.

---

## Related Solutions
* [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automates security and configuration audits for network infrastructure.
* [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and efficiency of automated business processes.
* [Admin User Access Auditor by Storeganise](../admin-user-access-auditor-by-storeganise/README.md) - Monitors and reports on user permissions and access levels across platforms.
