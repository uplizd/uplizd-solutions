# Network Troubleshooter (Uplizd) - Automated connectivity and performance diagnostics

## Summary
The Network Troubleshooter (Uplizd) is an intelligent automation workflow designed to streamline infrastructure diagnostics and connectivity testing. By leveraging the Composio Toolset, this agent performs real-time network analysis, identifies latency bottlenecks, and validates endpoint availability, providing IT teams with a single source of truth for network health and reducing mean time to resolution (MTTR).

---

## Demo
![Network Troubleshooter workflow dashboard showing real-time connectivity diagnostics and latency analysis results](image.png)
**Alt text (SEO-ready):** Network Troubleshooter dashboard by Uplizd, showing automated connectivity diagnostics, latency analysis, and network performance monitoring workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3c5d9ee2-fb9d-5159-9c36-8f1c4ff98370)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** network, diagnostics, infrastructure, latency, connectivity, monitoring, automation, composio
- This solution bridges the gap between raw network telemetry and actionable insights, enabling rapid troubleshooting for complex distributed systems.

---

## Who is this for?
This workflow is designed for technical teams responsible for maintaining robust and performant network environments.

- **Network Engineers**
    - Automate routine connectivity checks and baseline performance testing across distributed endpoints.
- **Site Reliability Engineers (SREs)**
    - Accelerate incident response by instantly identifying network-level bottlenecks during service outages.
- **IT Operations Managers**
    - Maintain high availability standards through proactive monitoring and automated diagnostic reporting.
- **System Administrators**
    - Simplify the validation of firewall rules and routing configurations with automated verification scripts.

---

## Features
- **Automated Connectivity Testing**
    - Executes real-time ping and traceroute commands to validate path integrity between critical infrastructure nodes.
- **Latency Bottleneck Identification**
    - Analyzes response times across network hops to pinpoint specific segments causing performance degradation.
- **Endpoint Availability Validation**
    - Continuously monitors service endpoints to ensure uptime and immediate alerting on connection failures.
- **Composio-Powered Tool Integration**
    - Seamlessly connects with network diagnostic tools to execute commands and retrieve structured diagnostic data.
- **Actionable Diagnostic Reporting**
    - Translates technical network logs into human-readable summaries for faster decision-making and incident documentation.

---

## Use Cases
**Infrastructure Health Monitoring**
- Automatically verify connectivity between cloud-hosted microservices and on-premises databases.
- Generate daily health reports for critical network gateways and VPN tunnels.

**Incident Response & Triage**
- Trigger diagnostic scans immediately upon receiving a high-latency alert from monitoring systems.
- Isolate network-level issues from application-level errors during service degradation events.

**Configuration Verification**
- Validate firewall and security group settings by testing reachability to restricted internal resources.
- Confirm route propagation across multi-region VPCs following infrastructure updates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Network Troubleshooter template from the library.
3. Configure your environment variables for the target network infrastructure.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target IP, URL, or diagnostic request from the user.
- **Agent**: Processes the request, determines the necessary diagnostic steps, and formulates the query.
- **Composio Toolset**: Executes the specific network diagnostic commands (e.g., ping, traceroute, curl) via authorized integrations.
- **Chat Output**: Delivers a clear, summarized report of the connectivity findings back to the user.

### 3) Run the Flow
Use the Playground to test your network diagnostics:
- `Check connectivity to production-api.internal and report any latency spikes.`
- `Run a traceroute to the primary database cluster and identify the slowest hop.`
- `Verify if the staging environment is reachable from the current network segment.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a network diagnostic expert, interpreting raw output into actionable advice.
- Use a model capable of structured data reasoning (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize identifying the "first point of failure" in network paths.
- Ensure the agent is configured to provide concise summaries followed by detailed technical logs.

### 2) Composio Toolset Node
- Provide the necessary API keys for your network diagnostic tools or CLI access providers.
- Set the connection scope to include read-only access to network telemetry and diagnostic execution permissions.

### 3) Tool Availability
- **Connectivity Tools**: Ping, Traceroute, MTR.
- **HTTP/API Validators**: Curl, Head requests, SSL certificate status checks.
- **Reporting Tools**: Log formatting and summary generation utilities.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Automated security and configuration auditing for cloud infrastructure.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Proactive monitoring for automated business process performance.
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) — Automated management and deployment of network zones and security settings.
