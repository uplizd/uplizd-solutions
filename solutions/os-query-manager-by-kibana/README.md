# OSQuery Manager (Uplizd) - Intelligent endpoint security query lifecycle automation

## Summary
The OSQuery Manager (Uplizd) is an AI-driven workflow designed to streamline the lifecycle of endpoint security queries. By automating the creation, execution, and analysis of OSQuery commands across distributed infrastructure, this solution provides security teams with a single source of truth for fleet visibility, significantly reducing the time spent on manual threat hunting and system auditing.

---

## Demo
![OSQuery Manager workflow interface showing query orchestration and endpoint data analysis](image.png)
**Alt text (SEO-ready):** Uplizd OSQuery Manager workflow interface for automated endpoint security queries, real-time threat hunting, and infrastructure auditing using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/014a8a1e-952d-5646-b581-81a6367665c2)

---

## Category
- **Primary category:** Security Operations
- **Secondary tags:** osquery, endpoint security, threat hunting, infrastructure, automation, composio, security auditing, fleet management
- This solution bridges the gap between raw endpoint telemetry and actionable security intelligence through automated query orchestration.

---

## Who is this for?
This solution is designed for security and IT teams managing complex, distributed infrastructure who need to maintain visibility without manual overhead.

- **Security Analyst**
    - Automates the execution of complex threat hunting queries across thousands of endpoints simultaneously.
- **System Administrator**
    - Simplifies the deployment and lifecycle management of saved queries for routine system health checks.
- **Compliance Officer**
    - Ensures consistent auditing of system configurations and security patches across the entire fleet.
- **DevOps Engineer**
    - Integrates endpoint telemetry directly into existing CI/CD or incident response pipelines for faster remediation.

---

## Features
- **Automated Query Lifecycle**
    - Manage the entire process from query drafting and validation to deployment and archival within a unified interface.
- **Cross-Platform Fleet Visibility**
    - Execute OSQuery commands across diverse operating systems and cloud environments using the Composio Toolset.
- **Real-Time Threat Detection**
    - Trigger automated scans based on security alerts to identify indicators of compromise (IoCs) instantly.
- **Intelligent Result Parsing**
    - Utilize the Agent node to interpret complex JSON output from OSQuery into human-readable security insights.
- **Audit Trail & Reporting**
    - Maintain a historical record of all executed queries and their findings for compliance and forensic analysis.

---

## Use Cases
**Threat Hunting & Incident Response**
- Execute immediate forensic queries across the fleet when a new vulnerability or IoC is reported.
- Correlate endpoint process data with network logs to identify lateral movement during an active incident.

**System Hardening & Compliance**
- Automatically verify that security configurations (e.g., firewall status, disk encryption) match organizational policies.
- Generate periodic compliance reports by scheduling automated audits of system settings across all managed nodes.

**Fleet Performance Monitoring**
- Identify resource-heavy processes or unauthorized software installations that deviate from the baseline.
- Monitor system uptime and patch levels to ensure all endpoints are running the latest security updates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the OSQuery Manager template from the solution library.
3. Connect your preferred OSQuery-compatible infrastructure via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language security queries or audit requests.
- **Agent**: Processes the intent, selects the appropriate OSQuery command, and analyzes the returned data.
- **Composio Toolset**: Executes the validated queries against your connected infrastructure.
- **Chat Output**: Delivers a summarized report or actionable insight back to the user.

### 3) Run the Flow
Use the Playground to test your queries:
- `Run a check for unauthorized SSH keys on all Linux endpoints.`
- `List all active processes consuming more than 50% CPU on the production fleet.`
- `Verify if the latest security patch is installed on all Windows servers.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your security queries.
- Use a model with strong reasoning capabilities for parsing technical telemetry.
- **Recommended instruction pattern:**
    - "You are a security expert; translate natural language requests into precise OSQuery syntax."
    - "Always validate the scope of the query to prevent performance degradation on endpoints."
    - "Summarize findings clearly, highlighting any anomalies or security risks found."

### 2) Composio Toolset Node
- Provide your API key to authenticate the connection to your endpoint management platform.
- Ensure the connection scope includes read/write permissions for query execution and fleet management.

### 3) Tool Availability
- **Query Execution**: Capability to push and run OSQuery commands.
- **Fleet Discovery**: Capability to list and filter active endpoints.
- **Data Export**: Capability to retrieve and format query results for analysis.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automated security auditing and account configuration monitoring.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Streamlined tracking and auditing of administrative user permissions.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Real-time monitoring and alerting for automated workflow performance.
