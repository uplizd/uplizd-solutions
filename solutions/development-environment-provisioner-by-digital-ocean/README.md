# Development Environment Provisioner (Uplizd) - Automated infrastructure setup for engineering teams

## Summary
The Development Environment Provisioner (Uplizd) automates the creation, configuration, and teardown of isolated development environments using DigitalOcean. By leveraging AI-driven workflows, engineering teams can eliminate manual infrastructure provisioning, ensure environment consistency across the development lifecycle, and significantly accelerate pipeline velocity.

---

## Demo
![Development Environment Provisioner workflow showing automated DigitalOcean droplet creation and configuration](image.png)
**Alt text (SEO-ready):** Development Environment Provisioner workflow in Uplizd, automating DigitalOcean infrastructure setup, cloud resource management, and developer environment provisioning.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/75285b5c-fba9-57e9-a2af-8f5ceb575ba5)

---

## Category
**Primary category:** Operations
**Secondary tags:** devops, digitalocean, infrastructure, cloud, automation, provisioning, composio, ai workflow.
This solution streamlines cloud infrastructure management by integrating AI agents with DigitalOcean APIs to automate environment lifecycle tasks.

---

## Who is this for?
This solution is designed for technical teams looking to reduce infrastructure overhead and standardize developer workspaces.

*   **DevOps Engineer**
    *   Automates repetitive server provisioning tasks to focus on high-level architecture.
*   **Engineering Manager**
    *   Ensures consistent development environments across the team to reduce "it works on my machine" issues.
*   **Full-Stack Developer**
    *   Spins up isolated sandboxes instantly for testing new features without waiting for IT tickets.
*   **QA Lead**
    *   Provisions clean, ephemeral environments for automated testing and bug reproduction.

---

## Features
- **Automated Droplet Provisioning**
  Rapidly deploy DigitalOcean droplets via AI-driven commands, reducing setup time from hours to seconds.
- **Environment Isolation**
  Create clean, sandbox-ready environments for every feature branch or experiment to prevent cross-project interference.
- **Composio Toolset Integration**
  Utilizes the Composio Toolset to securely bridge the Uplizd agent with DigitalOcean’s robust cloud infrastructure APIs.
- **Configurable Resource Allocation**
  Dynamically define CPU, memory, and region requirements through natural language prompts.
- **Lifecycle Management**
  Automate the teardown of development environments to optimize cloud spend and maintain resource hygiene.

---

## Use Cases
**Infrastructure Automation**
*   Provision a new Ubuntu droplet with specific SSH keys and firewall rules for a new project.
*   Scale up development server resources during high-intensity load testing phases.

**Developer Productivity**
*   Create a temporary staging environment to demonstrate a feature to stakeholders.
*   Automate the destruction of expired development environments to clean up unused cloud resources.

**Compliance & Governance**
*   Ensure all provisioned environments follow standard naming conventions and security tagging.
*   Audit environment creation logs to maintain visibility into cloud infrastructure usage.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and project destination.
3. Configure the DigitalOcean API credentials in the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives natural language requests for environment provisioning.
*   **Agent**: Interprets infrastructure requirements and orchestrates the DigitalOcean API calls.
*   **Composio Toolset**: Executes the specific cloud commands to manage droplets and networking.
*   **Chat Output**: Returns the status, IP address, and access details of the provisioned environment.

### 3) Run the Flow
Use the Playground to test your provisioning agent with these prompts:
* `Create a new 2GB RAM Ubuntu droplet in the NYC1 region for project-alpha.`
* `List all active development droplets and identify which ones have been running for more than 48 hours.`
* `Destroy the development environment associated with the feature-login-fix branch.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an infrastructure orchestrator.
*   Maintain a professional, technical tone focused on resource efficiency.
*   Always confirm resource parameters (region, size, image) before executing creation commands.
*   Provide clear, actionable error messages if API requests fail due to rate limits or permission issues.

### 2) Composio Toolset Node
*   Requires a valid DigitalOcean API Token with read/write permissions.
*   Scope the connection to specific projects or tags to ensure the agent operates within defined boundaries.

### 3) Tool Availability
*   **Droplet Management**: Create, list, and delete server instances.
*   **Network Configuration**: Manage firewall rules and floating IPs.
*   **Resource Monitoring**: Query current droplet status and uptime metrics.

---

## Related Solutions
* [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automates security and configuration audits for cloud accounts.
* [Workflow Health Monitor by DailyBot](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and health of automated workflows.
* [Zone Provisioning Agent by Cloudflare](../zone-provisioning-agent-by-cloudflare/README.md) - Manages DNS zone provisioning and configuration at scale.
