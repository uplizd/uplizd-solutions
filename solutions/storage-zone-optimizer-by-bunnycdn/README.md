# Storage Zone Optimizer (Uplizd) - Automated CDN file distribution and storage efficiency

## Summary
The Storage Zone Optimizer is an intelligent Uplizd AI workflow designed to streamline file storage distribution across global BunnyCDN zones. By automating the monitoring and reallocation of assets, this solution helps infrastructure teams and DevOps engineers maintain optimal latency, reduce egress costs, and ensure high availability for global content delivery, acting as a single source of truth for storage hygiene.

---

## Demo
![Storage Zone Optimizer workflow showing automated file distribution and CDN zone management](image.png)
**Alt text (SEO-ready):** Storage Zone Optimizer workflow for automated CDN file distribution, Uplizd AI infrastructure management, and BunnyCDN storage optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/fba9d27a-82b9-5d04-9994-1c508bb507f6)

---

## Category
**Primary category:** Cloud Infrastructure Operations
**Secondary tags:** cdn, bunnycdn, storage optimization, infrastructure automation, latency reduction, data hygiene, composio, ai workflow.
This solution bridges the gap between raw storage management and intelligent, automated CDN distribution to improve global content delivery performance.

---

## Who is this for?
This solution is designed for technical teams managing high-traffic digital assets who need to automate complex storage routing.

*   **DevOps Engineer**
    *   Automates the manual burden of rebalancing assets across global CDN zones to maintain performance SLAs.
*   **Infrastructure Manager**
    *   Ensures cost-effective storage utilization by identifying and migrating under-optimized zones.
*   **Site Reliability Engineer (SRE)**
    *   Reduces latency for end-users by ensuring files are routed through the most efficient geographic storage zones.
*   **Cloud Architect**
    *   Maintains a clean, scalable storage architecture through automated policy-based distribution rules.

---

## Features
- **Automated Zone Balancing**
    Real-time monitoring of storage usage across BunnyCDN zones to trigger redistribution based on traffic patterns.
- **Intelligent Asset Routing**
    Uses AI logic to determine the optimal storage zone for new uploads based on geographic metadata and latency requirements.
- **Cost-Efficiency Analysis**
    Identifies redundant or infrequently accessed files that can be moved to lower-cost storage tiers without impacting delivery speeds.
- **Composio-Powered Integration**
    Leverages the Composio Toolset to securely execute API calls directly to your BunnyCDN account for seamless infrastructure updates.
- **Real-time Health Monitoring**
    Provides automated reporting on zone health and distribution status, ensuring your content delivery pipeline remains performant.

---

## Use Cases
**Global Traffic Optimization**
*   Automatically re-route assets to edge storage zones during peak traffic events to minimize latency.
*   Sync new media uploads to multiple regional zones to ensure high availability for global users.

**Storage Cost Management**
*   Identify and migrate stale assets from high-performance zones to cost-optimized storage buckets.
*   Automate the cleanup of orphaned files that no longer map to active CDN delivery paths.

**Infrastructure Compliance**
*   Ensure all new storage zones adhere to regional data residency requirements through automated validation.
*   Generate audit logs for every storage migration or zone configuration change performed by the agent.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Connect your BunnyCDN API credentials within the Composio integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives commands for storage optimization or zone status queries.
*   **Agent**: Processes infrastructure logic and decides which CDN zones require action.
*   **Composio Toolset**: Executes secure API requests to manage BunnyCDN storage zones and file paths.
*   **Chat Output**: Delivers a summary of actions taken or current storage distribution metrics.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Analyze current storage distribution and identify zones exceeding 80% capacity.`
* `Move assets from the North America zone to the Europe zone based on current traffic latency.`
* `Generate a report on storage usage and suggest optimizations for the current month.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your infrastructure orchestrator.
*   Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Instruction: "You are a CDN infrastructure expert. Analyze storage metrics and use the provided tools to optimize file distribution."
*   Instruction: "Always prioritize latency reduction and cost-efficiency when making storage migration decisions."

### 2) Composio Toolset Node
*   Provide your BunnyCDN API Key to the Composio Toolset node.
*   Ensure the connection scope includes `Storage.Read` and `Storage.Write` permissions to allow the agent to manage your zones.

### 3) Tool Availability
*   `list_storage_zones`: Fetch current zone configurations and usage stats.
*   `move_file_asset`: Transfer files between designated storage zones.
*   `get_zone_latency_metrics`: Retrieve performance data to inform migration decisions.
*   `delete_orphaned_assets`: Clean up unused files identified during the audit.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Automate security and configuration audits for cloud accounts.
* [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) — Streamline the creation and setup of new network zones.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track and maintain the operational status of automated infrastructure pipelines.
