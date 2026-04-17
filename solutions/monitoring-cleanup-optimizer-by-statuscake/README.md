# Monitoring Cleanup Optimizer (Uplizd) - Automated infrastructure hygiene and alert management

## Summary
The Monitoring Cleanup Optimizer is an intelligent Uplizd workflow designed to automate the lifecycle management of monitoring tests and contact configurations. By integrating with StatusCake, this solution identifies stale, redundant, or failing monitoring endpoints and performs automated cleanup, ensuring your infrastructure monitoring remains accurate, cost-effective, and free of alert fatigue for DevOps and SRE teams.

---

## Demo
![Monitoring Cleanup Optimizer workflow dashboard showing automated StatusCake test deletion and contact list pruning](image.png)
**Alt text (SEO-ready):** Monitoring Cleanup Optimizer Uplizd workflow for automated StatusCake monitoring test cleanup, alert hygiene, and infrastructure data management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d54f0322-f916-55be-856b-95fd44a29e74)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** monitoring, statuscake, infrastructure, devops, cleanup, automation, alert-fatigue, composio
- This solution streamlines technical operations by automating the maintenance of monitoring configurations to prevent alert noise and resource bloat.

---

## Who is this for?
This workflow is designed for technical teams managing large-scale infrastructure monitoring who need to maintain high signal-to-noise ratios.

- **Site Reliability Engineer (SRE)**
    - Automates the removal of legacy monitoring tests to reduce infrastructure clutter and maintenance overhead.
- **DevOps Manager**
    - Ensures monitoring compliance by automatically pruning outdated contact groups and notification channels.
- **System Administrator**
    - Reduces alert fatigue by identifying and decommissioning monitoring probes for deprecated services.
- **Cloud Infrastructure Lead**
    - Maintains accurate monitoring dashboards by syncing active service lists with current StatusCake configurations.

---

## Features
- **Automated Stale Test Detection**
    - Uses the Composio Toolset to scan StatusCake for monitoring tests that have been inactive or failing for extended periods.
- **Intelligent Contact Pruning**
    - Automatically identifies and removes orphaned contact groups that are no longer associated with active monitoring alerts.
- **Bulk Cleanup Operations**
    - Executes safe, batch-processed deletions of identified redundant tests to maintain a clean monitoring environment.
- **Real-time Alert Hygiene**
    - Filters out noise by dynamically updating notification thresholds based on current service uptime requirements.
- **Audit Logging**
    - Generates a comprehensive summary of all cleanup actions performed, providing full visibility into infrastructure changes.

---

## Use Cases
**Infrastructure Maintenance**
- Automatically decommission monitoring tests for services that have been retired or migrated to new environments.
- Regularly audit and remove duplicate monitoring probes that cause redundant alert notifications.

**Alert Fatigue Reduction**
- Identify and disable "flapping" tests that trigger false positives, allowing teams to focus on genuine service outages.
- Consolidate notification contacts to ensure alerts are routed only to currently active on-call engineers.

**Compliance & Reporting**
- Generate weekly reports on monitoring coverage to ensure all production endpoints are correctly instrumented.
- Maintain a clean state for monitoring configurations to meet internal infrastructure documentation standards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Connect your StatusCake API credentials via the Composio Toolset node.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language commands to initiate a cleanup scan.
- **Agent**: Processes instructions and determines which monitoring tests or contacts require attention.
- **Composio Toolset**: Executes API calls to StatusCake to fetch, verify, and delete monitoring resources.
- **Chat Output**: Returns a summary report of the cleanup actions taken or a list of items flagged for review.

### 3) Run the Flow
Open the Uplizd Playground and try these prompts:
- `Find and delete all monitoring tests that have been failing for more than 30 days.`
- `List all contact groups that are not currently assigned to any active monitoring tests.`
- `Perform a full cleanup of orphaned StatusCake contacts and provide a summary report.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for infrastructure cleanup.
- Use a model with strong reasoning capabilities to accurately identify "stale" vs "active" tests.
- **Recommended instruction pattern:**
    - "Act as an SRE assistant; prioritize safety by flagging items for confirmation before deletion."
    - "Analyze the provided StatusCake data to identify tests with zero uptime in the last 7 days."
    - "Maintain a professional tone and provide clear, actionable summaries of all modifications."

### 2) Composio Toolset Node
- Requires a valid StatusCake API Key with read/write permissions.
- Ensure the connection scope includes `tests:read`, `tests:delete`, and `contacts:read`.

### 3) Tool Availability
- **Test Management**: List, Get, and Delete monitoring tests.
- **Contact Management**: Fetch and remove contact groups.
- **Status Reporting**: Retrieve uptime and failure metrics for specific endpoints.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor and maintain the health of your automated workflows.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform security and configuration audits on your infrastructure.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Audit and clean up user access permissions across your systems.
