# Source Organization Assistant (Uplizd) - Intelligent monitoring and log management

## Summary
The Source Organization Assistant is an AI-powered workflow designed to streamline the management of monitoring sources and log data. By leveraging the Composio Toolset, this solution enables teams to automate the categorization, tagging, and health monitoring of infrastructure logs, ensuring a single source of truth for system reliability and reducing manual overhead in incident response.

---

## Demo
![Source Organization Assistant dashboard showing automated log categorization and monitoring source health status](image.png)
**Alt text (SEO-ready):** Source Organization Assistant Uplizd workflow for automated log management, monitoring source categorization, and infrastructure health tracking via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9340a040-398b-57b7-bc7f-aded67a87b71)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** log management, infrastructure monitoring, data organization, automation, composio, ai workflow, system reliability, devops
- This solution bridges the gap between raw log data and actionable infrastructure insights through intelligent automated organization.

---

## Who is this for?
This solution is designed for technical teams looking to reduce noise and improve visibility across their monitoring stack.

- **Site Reliability Engineers (SREs)**
    - Automates the triage of log sources to reduce mean time to resolution (MTTR) during outages.
- **DevOps Engineers**
    - Maintains clean, organized monitoring configurations across complex cloud environments.
- **System Administrators**
    - Ensures consistent tagging and categorization of logs for improved compliance and auditability.
- **Infrastructure Managers**
    - Provides high-level visibility into monitoring coverage and source health across the organization.

---

## Features
- **Automated Source Categorization**
    - Intelligently identifies and labels incoming log streams based on service type and environment.
- **Real-time Health Monitoring**
    - Continuously evaluates the status of connected monitoring sources to detect ingestion gaps.
- **Composio-Powered Integrations**
    - Seamlessly connects with monitoring tools and log aggregators to execute management tasks via natural language.
- **Intelligent Alert Routing**
    - Maps specific log patterns to the appropriate notification channels, reducing alert fatigue.
- **Configuration Hygiene**
    - Automatically identifies and flags duplicate or orphaned monitoring sources to keep infrastructure clean.

---

## Use Cases
**Log Management Optimization**
- Automatically archive or rotate logs based on age and service criticality.
- Standardize naming conventions across all monitoring sources to ensure uniform reporting.

**Infrastructure Health Audits**
- Perform scheduled scans of monitoring sources to verify data ingestion connectivity.
- Generate summary reports on log source activity to identify underutilized monitoring assets.

**Incident Response Acceleration**
- Quickly query and organize logs related to specific service failures during an active incident.
- Automate the creation of temporary log dashboards for specific troubleshooting sessions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Source Organization Assistant template from the library.
3. Connect your required monitoring tool accounts within the Composio integration settings.
4. Ensure nodes are correctly linked from the Chat Input to the Agent and finally to the Composio Toolset.

### 2) Setup the Nodes
*   **Chat Input**: Receives user requests regarding log sources or monitoring status.
*   **Agent**: Processes natural language instructions and determines the necessary management actions.
*   **Composio Toolset**: Executes API calls to monitoring platforms to update, categorize, or audit sources.
*   **Chat Output**: Delivers the summary, confirmation, or status report back to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
`"Categorize all unlabelled log sources from the production environment."`
`"Check the health status of all monitoring sources connected to the primary database cluster."`
`"Find and flag any orphaned log sources that haven't received data in the last 24 hours."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your natural language intent and the monitoring API.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system instruction to prioritize accuracy in resource identification.
- Ensure the agent has access to the full list of available tool functions for log management.

### 2) Composio Toolset Node
- Provide your API key for the specific monitoring platform (e.g., Better Stack, Datadog).
- Ensure the connection scope includes read/write permissions for source configuration and metadata.

### 3) Tool Availability
- **Source Discovery**: Scan and list active monitoring endpoints.
- **Metadata Update**: Modify tags, categories, and descriptions for log sources.
- **Health Check**: Verify connectivity and recent data ingestion timestamps.
- **Cleanup Utility**: Delete or archive inactive or redundant monitoring sources.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Tracks the operational status and health of automated workflows.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Performs comprehensive audits of account configurations and security settings.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automates the organization and resolution of pending action items and tasks.
