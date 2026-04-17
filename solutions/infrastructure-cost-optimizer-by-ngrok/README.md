# Infrastructure Cost Optimizer (Uplizd) - Automated ngrok usage monitoring and infrastructure spend reduction

## Summary
The Infrastructure Cost Optimizer (Uplizd) is an intelligent AI workflow designed to monitor ngrok tunnel activity, identify idle or redundant endpoints, and provide actionable insights to reduce infrastructure overhead. By automating the analysis of network traffic and tunnel configurations, this solution enables DevOps and engineering teams to maintain optimal performance while ensuring cost-efficient resource allocation across their development environments.

---

## Demo
![Infrastructure Cost Optimizer dashboard showing ngrok tunnel usage metrics and cost-saving recommendations](image.png)
**Alt text (SEO-ready):** Infrastructure Cost Optimizer dashboard showing ngrok tunnel usage metrics and cost-saving recommendations for Uplizd AI workflow and cloud infrastructure management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/72ef855c-9105-5b31-bb71-0bd0e9518466)

---

## Category
**Primary category:** Operations  
**Secondary tags:** infrastructure, ngrok, cost optimization, cloud ops, devops, resource management, composio, ai workflow  
This solution bridges the gap between raw network telemetry and financial efficiency by automating the identification of underutilized infrastructure assets.

---

## Who is this for?
This solution is designed for technical teams looking to gain granular control over their development infrastructure spend.

* **DevOps Engineer**
    * Automates the cleanup of stale tunnels to prevent unnecessary resource consumption.
* **Engineering Manager**
    * Provides clear visibility into infrastructure costs associated with remote development tools.
* **Cloud Architect**
    * Ensures that ngrok configurations align with organizational security and budget policies.
* **System Administrator**
    * Monitors real-time tunnel activity to identify potential bottlenecks or misconfigured endpoints.

---

## Features
- **Real-time Tunnel Monitoring**
  Tracks active ngrok tunnels via the Composio Toolset to provide live status updates.
- **Automated Idle Detection**
  Uses AI logic to flag tunnels that have been inactive for extended periods, reducing waste.
- **Cost-Efficiency Reporting**
  Generates summaries of potential savings based on current tunnel usage patterns.
- **Integration-Ready Architecture**
  Connects seamlessly with your existing infrastructure stack to pull telemetry data.
- **Proactive Alerting**
  Notifies stakeholders when infrastructure usage exceeds defined cost thresholds.

---

## Use Cases
**Infrastructure Cleanup**
* Automatically terminate tunnels that have been idle for more than 24 hours.
* Identify and remove duplicate endpoints created by automated CI/CD pipelines.

**Cost Analysis & Reporting**
* Generate weekly reports detailing the correlation between tunnel uptime and project spend.
* Flag high-traffic tunnels that may require a transition to permanent infrastructure.

**Operational Governance**
* Enforce naming conventions and lifecycle policies for all developer-created tunnels.
* Audit tunnel access logs to ensure compliance with internal security standards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Infrastructure Cost Optimizer.
2. Click "Import" to add the workflow to your workspace.
3. Connect your ngrok API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives user queries regarding tunnel status or cost reports.
* **Agent**: Processes infrastructure data and applies optimization logic.
* **Composio Toolset**: Executes API calls to fetch and manage ngrok tunnel configurations.
* **Chat Output**: Delivers actionable insights and optimization recommendations to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
* `Analyze my current ngrok tunnels and list any that have been idle for over 48 hours.`
* `How much could we save if we terminated all non-essential tunnels in the staging environment?`
* `Generate a summary report of our infrastructure usage for the last 7 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as an infrastructure analyst, translating raw API data into human-readable insights.
* Focus on identifying patterns of inactivity.
* Prioritize cost-saving recommendations based on usage frequency.
* Maintain a professional, data-driven tone for all generated reports.

### 2) Composio Toolset Node
Requires a valid ngrok API key with read/write permissions to manage tunnel endpoints and retrieve telemetry data.

### 3) Tool Availability
* **Tunnel List**: Retrieve all active and inactive tunnels.
* **Tunnel Detail**: Fetch metadata and traffic statistics for specific endpoints.
* **Tunnel Management**: Ability to stop or delete tunnels identified as redundant.

---

## Related Solutions
* [Account Audit Agent (Cloudflare)](../account-audit-agent-by-cloudflare/README.md) — Monitor and audit account-level infrastructure security and settings.
* [Workflow Health Monitor (Dailybot)](../workflow-health-monitor-by-dailybot/README.md) — Track the operational health and efficiency of your team's automated workflows.
* [Zone Provisioning Agent (Cloudflare)](../zone-provisioning-agent-by-cloudflare/README.md) — Automate the provisioning and management of network zones.
