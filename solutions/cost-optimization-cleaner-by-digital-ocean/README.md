# Cost Optimization Cleaner (Uplizd) - Automated cloud resource lifecycle management

## Summary
The Cost Optimization Cleaner is an intelligent Uplizd workflow designed to identify, flag, and decommission unused cloud resources within your DigitalOcean infrastructure. By automating the detection of idle droplets, unattached volumes, and stale snapshots, this solution helps DevOps teams and cloud administrators reduce monthly spend, maintain infrastructure hygiene, and prevent resource sprawl without manual intervention.

---

## Demo
![Cost Optimization Cleaner workflow identifying and deleting unused DigitalOcean droplets](image.png)
**Alt text (SEO-ready):** Cost Optimization Cleaner Uplizd workflow for DigitalOcean resource management, cloud cost reduction, and automated infrastructure cleanup.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/29cb39de-f6cd-5158-8685-d2004812e68d)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** cloud, devops, digitalocean, cost-optimization, infrastructure, automation, composio, ai-workflow
- This solution bridges the gap between cloud monitoring and automated cost governance, ensuring your infrastructure remains lean and cost-efficient.

---

## Who is this for?
This solution is designed for technical teams looking to regain control over their cloud expenditure through automated oversight.

- **Cloud Infrastructure Engineer**
    - Automates the identification of zombie resources that inflate monthly cloud bills.
- **FinOps Analyst**
    - Provides a programmatic way to enforce tagging policies and cleanup schedules across production environments.
- **DevOps Manager**
    - Reduces the manual burden of auditing infrastructure, allowing the team to focus on deployment velocity.
- **CTO / Startup Founder**
    - Ensures cloud spend is strictly aligned with active development and production requirements.

---

## Features
- **Intelligent Resource Scanning**
    - Automatically queries your DigitalOcean account to detect idle droplets and unattached storage volumes.
- **Automated Cleanup Logic**
    - Safely triggers deletion or suspension workflows for resources that meet defined inactivity thresholds.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to execute secure, authenticated API calls directly to DigitalOcean.
- **Real-time Reporting**
    - Delivers summary reports via the Chat Output node, detailing exactly which resources were flagged or removed.
- **Customizable Thresholds**
    - Allows users to define specific "inactivity" parameters to prevent accidental deletion of critical development environments.

---

## Use Cases
**Cloud Cost Governance**
- Automatically identify and terminate droplets that have had zero CPU usage for over 14 days.
- Flag unattached block storage volumes that are incurring costs without providing value to active servers.

**Infrastructure Hygiene**
- Clean up stale snapshots and backups that exceed your organization's retention policy.
- Audit and remove unused floating IPs that are no longer associated with active load balancers or droplets.

**Operational Efficiency**
- Generate weekly "Cost Savings" reports that summarize potential savings from identified idle resources.
- Trigger alerts to Slack or email when high-cost resources are detected as idle, requiring manual approval before deletion.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Connect your DigitalOcean API credentials within the integration settings.
3. Configure your preferred inactivity thresholds in the Agent node instructions.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or schedule signal to initiate the audit.
- **Agent**: Analyzes infrastructure data against your defined cost-optimization rules.
- **Composio Toolset**: Executes the specific API actions to fetch resource lists and perform cleanup.
- **Chat Output**: Returns a summary of the audit findings and actions taken to the user.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Run a full audit of all droplets and list any that have been idle for more than 30 days.`
- `Identify all unattached block storage volumes and prepare a report for deletion.`
- `Perform a cleanup of all snapshots older than 90 days to optimize storage costs.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for your infrastructure cleanup.
- **Instruction Pattern:**
    - "You are a cloud infrastructure assistant; prioritize safety by verifying resource activity before suggesting deletion."
    - "Always cross-reference resource tags to ensure critical production assets are never flagged for cleanup."
    - "Provide clear, concise summaries of all actions taken, including resource IDs and estimated cost savings."

### 2) Composio Toolset Node
- **API Key**: Ensure your DigitalOcean API token has `read` and `write` scopes enabled.
- **Connection Scope**: Limit the toolset to the specific projects or regions you wish to manage.

### 3) Tool Availability
- **Resource Discovery**: Capability to list droplets, volumes, and snapshots.
- **Usage Metrics**: Access to CPU and network utilization data.
- **Lifecycle Management**: Capability to delete, power off, or snapshot resources.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Comprehensive security and configuration auditing for cloud accounts.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor and maintain the operational status of your automated workflows.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich and manage account data for better organizational oversight.
