# CDN Infrastructure Manager (Uplizd) - Automated content delivery and edge configuration

## Summary
The CDN Infrastructure Manager (Uplizd) automates the provisioning, configuration, and maintenance of your content delivery network settings via BunnyCDN. By leveraging AI-driven orchestration, this solution eliminates manual edge configuration errors, ensures global cache consistency, and accelerates deployment velocity for DevOps and infrastructure teams.

---

## Demo
![CDN Infrastructure Manager dashboard showing automated edge rule deployment and cache status monitoring](image.png)
**Alt text (SEO-ready):** CDN Infrastructure Manager dashboard showing automated edge rule deployment and cache status monitoring for Uplizd AI workflows and BunnyCDN integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7217e11c-ac37-5189-8a74-df77f27c780b)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** cdn, bunnycdn, infrastructure, devops, edge computing, automation, cloud management, composio
- This solution streamlines infrastructure operations by connecting AI agents directly to your CDN provider for real-time configuration management.

---

## Who is this for?
This solution is designed for technical teams managing high-traffic web assets who need to maintain performance without manual intervention.

- **DevOps Engineer**
    - Automates edge rule deployments and purges to maintain high availability during traffic spikes.
- **Site Reliability Engineer (SRE)**
    - Monitors CDN health and triggers automated remediation for cache-related latency issues.
- **Web Infrastructure Manager**
    - Ensures global compliance and security settings are consistently applied across all CDN zones.
- **Full-Stack Developer**
    - Simplifies the integration of asset delivery pipelines with automated environment-specific CDN updates.

---

## Features
- **Automated Zone Provisioning**
    - Instantly create and configure new CDN zones via the Composio Toolset to reduce setup time for new environments.
- **Real-time Cache Management**
    - Execute targeted cache purges and invalidations directly through natural language commands to ensure content freshness.
- **Edge Rule Orchestration**
    - Dynamically update edge rules, security headers, and redirect logic without manual dashboard navigation.
- **Infrastructure Health Monitoring**
    - Query real-time CDN performance metrics and status codes to proactively identify and resolve delivery bottlenecks.
- **Cross-Environment Synchronization**
    - Maintain parity between staging and production CDN configurations to prevent environment-specific delivery failures.

---

## Use Cases
**Automated Deployment Pipelines**
- Trigger CDN cache invalidation automatically following a successful CI/CD build deployment.
- Provision new CDN zones for temporary feature-branch environments via automated infrastructure-as-code workflows.

**Incident Response & Optimization**
- Rapidly update security headers or block malicious IP ranges during a detected DDoS or traffic anomaly.
- Adjust cache TTL (Time to Live) settings dynamically based on real-time traffic patterns and content volatility.

**Global Content Management**
- Synchronize edge configuration settings across multiple geographic regions to ensure consistent user experiences.
- Automate the rotation of SSL certificates and edge security policies to maintain compliance standards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the CDN Infrastructure Manager template from the marketplace.
3. Connect your BunnyCDN API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language commands for infrastructure tasks.
- **Agent**: Interprets intent and maps requests to specific CDN management actions.
- **Composio Toolset**: Executes authenticated API calls to the BunnyCDN platform.
- **Chat Output**: Returns confirmation of configuration changes or performance status reports.

### 3) Run the Flow
Use the Playground to test your infrastructure automation:
- `Purge all cache for the production zone immediately.`
- `Create a new CDN zone named 'staging-app-v2' with standard security headers.`
- `List all active edge rules for the main website zone and report any missing security policies.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an infrastructure orchestrator.
- Maintain a formal, technical tone for all infrastructure operations.
- Prioritize safety by requiring confirmation for destructive actions like zone deletion.
- Use structured JSON outputs for logging configuration changes.

### 2) Composio Toolset Node
- Provide a valid BunnyCDN API key with "Zone Read/Write" permissions.
- Ensure the connection scope is limited to the specific zones required for the workflow.

### 3) Tool Availability
- **Zone Management**: Create, delete, and list CDN zones.
- **Cache Control**: Purge individual files or entire zones.
- **Edge Rules**: Read, update, and deploy edge rule configurations.
- **Security**: Manage SSL certificates and access control lists.

---

## Related Solutions
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) - Automate infrastructure provisioning using Cloudflare.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Perform comprehensive security and configuration audits.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for complex operational tasks.
