# Development Environment Orchestrator (Uplizd) - Streamline ngrok tunnel management for dev teams

## Summary
The Development Environment Orchestrator is an intelligent Uplizd workflow designed to automate the lifecycle of ngrok tunnels across distributed development teams. By centralizing tunnel management, this solution eliminates manual configuration overhead, ensures consistent environment exposure, and provides a single source of truth for active development endpoints, significantly increasing pipeline velocity and reducing infrastructure friction.

---

## Demo
![Development Environment Orchestrator workflow diagram showing ngrok tunnel provisioning and management](image.png)
**Alt text (SEO-ready):** Development Environment Orchestrator workflow for ngrok tunnel management, Uplizd automation, and developer environment synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2035e10d-8495-5170-b5f9-3c67735fc7d4)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** ngrok, devops, infrastructure, automation, tunnel management, developer experience, composio, api orchestration
- This solution bridges the gap between local development environments and external accessibility through automated ngrok tunnel orchestration.

---

## Who is this for?
This solution is designed for engineering teams looking to standardize how local services are exposed for testing and collaboration.

- **DevOps Engineer**
    - Automates the provisioning of secure tunnels to ensure consistent environment access across staging and development.
- **Backend Developer**
    - Eliminates manual CLI configuration by programmatically managing ngrok endpoints for real-time API testing.
- **QA Automation Lead**
    - Enables seamless integration of local services into automated testing pipelines by providing stable, reachable endpoints.
- **Engineering Manager**
    - Reduces onboarding friction and infrastructure downtime by centralizing visibility into active development tunnels.

---

## Features
- **Automated Tunnel Lifecycle**
    - Automatically provisions, monitors, and tears down ngrok tunnels based on active development sessions.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely interface with ngrok APIs and internal infrastructure management tools.
- **Real-time Endpoint Sync**
    - Maintains an up-to-date registry of active tunnels, ensuring team members always have access to the correct development environments.
- **Configurable Security Policies**
    - Enforces standardized security headers and tunnel constraints across all orchestrated development endpoints.
- **Centralized Orchestration Dashboard**
    - Provides a unified view of all active tunnels, allowing for rapid troubleshooting and environment cleanup.

---

## Use Cases
**Collaborative Debugging**
- Automatically generate temporary public URLs for local webhooks when testing integrations with third-party services.
- Share active development environments with remote team members for real-time pair programming and troubleshooting.

**Automated CI/CD Testing**
- Spin up ephemeral ngrok tunnels during automated integration test suites to expose local services to external test runners.
- Automatically terminate tunnels upon test completion to maintain environment hygiene and security.

**Client Demonstrations**
- Quickly expose local prototypes to stakeholders via secure, temporary tunnels without modifying firewall settings.
- Manage multiple concurrent tunnels for different features or branches during client review sessions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Development Environment Orchestrator template from the solution library.
3. Connect your ngrok API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives commands to start, stop, or list active ngrok tunnels.
- **Agent**: Interprets user intent and determines the necessary tunnel management actions.
- **Composio Toolset**: Executes API calls to ngrok to manage tunnel states securely.
- **Chat Output**: Returns status updates, tunnel URLs, or error logs to the user.

### 3) Run the Flow
Use the Uplizd Playground to test your orchestration:
- `Start a new ngrok tunnel for port 8080 and name it 'feature-branch-test'`
- `List all currently active development tunnels and their status`
- `Terminate the tunnel associated with the 'feature-branch-test' session`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for all tunnel management tasks.
- Instruction: You are an expert DevOps assistant specialized in ngrok tunnel management.
- Instruction: Always verify the status of a tunnel before attempting to terminate or modify it.
- Instruction: Provide clear, actionable feedback including the public URL and expiration status for every tunnel created.

### 2) Composio Toolset Node
- **API Key**: Provide your ngrok API key to enable tunnel management capabilities.
- **Connection Scope**: Limit the agent's access to specific tunnel regions and port ranges as required by your security policy.

### 3) Tool Availability
- **Tunnel Provisioning**: Capability to create new tunnels on specified local ports.
- **Tunnel Inspection**: Capability to list, query, and monitor existing tunnel health.
- **Tunnel Termination**: Capability to safely close active tunnels and release resources.

---

## Related Solutions
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Monitor the health and status of your automated development workflows.
- [../account-audit-agent-by-cloudflare/README.md](../account-audit-agent-by-cloudflare/README.md) - Audit and secure your network infrastructure and edge configurations.
- [../admin-user-onboarding-assistant-by-storeganise/README.md](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamline the onboarding process for new developers and administrative users.
