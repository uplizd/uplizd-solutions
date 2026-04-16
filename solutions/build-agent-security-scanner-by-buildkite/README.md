# Build Agent Security Scanner (Uplizd) - Automated CI/CD vulnerability and compliance monitoring

## Summary
The Build Agent Security Scanner is an automated Uplizd workflow designed to secure your CI/CD pipeline by continuously auditing build agents for vulnerabilities and configuration drift. By leveraging the Composio Toolset to interface with infrastructure providers, this solution ensures that your build environment remains compliant, reducing the risk of supply chain attacks and unauthorized access through real-time security posture reporting.

---

## Demo
![Build Agent Security Scanner dashboard showing real-time vulnerability alerts and agent compliance status](../image.png)
**Alt text (SEO-ready):** Build Agent Security Scanner dashboard displaying Uplizd workflow automation, CI/CD vulnerability tracking, and infrastructure compliance monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a8977cdc-c724-5b00-a877-df16c266e7f7)

---

## Category
**Primary category:** Engineering  
**Secondary tags:** devops, security, ci/cd, buildkite, vulnerability management, compliance, automation, composio  
This solution bridges the gap between infrastructure security and developer velocity by automating the audit lifecycle of your build environment.

---

## Who is this for?
This solution is designed for engineering and security teams responsible for maintaining a hardened CI/CD infrastructure.

*   **DevOps Engineer**
    *   Automate routine security audits of build agents to prevent configuration drift.
*   **Security Analyst**
    *   Gain real-time visibility into vulnerabilities across ephemeral build environments.
*   **Engineering Manager**
    *   Ensure pipeline compliance with internal security standards without manual oversight.
*   **Site Reliability Engineer (SRE)**
    *   Minimize downtime caused by compromised build agents through proactive threat detection.

---

## Features
- **Automated Vulnerability Scanning**
  Continuous assessment of build agent images and runtime environments against known CVE databases.
- **Configuration Drift Detection**
  Real-time monitoring of agent settings to ensure they match approved security baselines.
- **Composio-Powered Remediation**
  Seamless integration with cloud infrastructure tools to isolate or patch compromised agents automatically.
- **Centralized Security Reporting**
  Consolidated logs and alerts delivered directly to your team’s communication channels.
- **Ephemeral Environment Hardening**
  Automated cleanup and verification of build agents post-execution to maintain a zero-trust posture.

---

## Use Cases
**Infrastructure Hardening**
*   Automatically rotate or terminate build agents that fail security compliance checks.
*   Verify that all active build agents are running the latest patched versions of container runtimes.

**Compliance & Auditing**
*   Generate automated audit trails for build agent access logs to satisfy SOC2 or ISO27001 requirements.
*   Flag unauthorized changes to build agent environment variables or installed software packages.

**Incident Response**
*   Trigger immediate alerts when a build agent exhibits anomalous network behavior during a job.
*   Isolate build agents suspected of being compromised to prevent lateral movement within the CI/CD network.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Build Agent Security Scanner template from the library.
3. Connect your CI/CD provider (e.g., Buildkite) and security scanning tools via the Composio Toolset.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives manual triggers or scheduled scan requests from your engineering team.
*   **Agent**: Processes security policies and evaluates scan results against defined compliance rules.
*   **Composio Toolset**: Executes API calls to infrastructure providers to fetch agent status and apply remediation actions.
*   **Chat Output**: Delivers a summary report of findings and actions taken to your preferred notification channel.

### 3) Run the Flow
Use the Playground to test the scanner with these prompts:
* `Run a full security audit on all active build agents in the production queue.`
* `Check for configuration drift on the latest build agent image and report any discrepancies.`
* `Isolate any build agent that has failed the last three vulnerability scans.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the security orchestrator, interpreting scan data and deciding on remediation steps.
*   Prioritize security-first logic when evaluating scan results.
*   Maintain a neutral, objective tone in all generated security reports.
*   Follow strict escalation protocols when high-severity vulnerabilities are detected.

### 2) Composio Toolset Node
Configure the node with your CI/CD platform API key and ensure the connection scope includes read/write permissions for agent management and infrastructure monitoring.

### 3) Tool Availability
*   **CI/CD Provider API**: For fetching agent lists and job status.
*   **Vulnerability Scanner API**: For querying CVE databases and agent scan results.
*   **Infrastructure Management API**: For isolating or updating build agent resources.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Comprehensive security auditing for cloud infrastructure accounts.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Real-time monitoring of team workflow and pipeline health.
* [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Automated auditing of user permissions and access logs.
