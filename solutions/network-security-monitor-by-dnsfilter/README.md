# Network Security Monitor (Uplizd) - Automated threat detection and network security oversight

## Summary
The Network Security Monitor by Uplizd provides an automated workflow for real-time threat detection and network infrastructure oversight. By integrating DNSFilter with intelligent AI agents, this solution enables security teams to proactively identify malicious domains, monitor traffic patterns, and maintain a robust security posture, reducing the time required to respond to potential network vulnerabilities.

---

## Demo
![Network Security Monitor dashboard showing real-time threat detection and DNS filtering logs](image.png)
**Alt text (SEO-ready):** Network Security Monitor dashboard showing real-time threat detection, DNS filtering logs, and automated security reporting within the Uplizd workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0ef97513-e42c-59a0-a347-ce9fa796f5f8)

---

## Category
**Primary category:** Engineering
**Secondary tags:** network security, dnsfilter, threat detection, cybersecurity, automation, real-time monitoring, composio, ai workflow
This solution bridges the gap between raw network logs and actionable security intelligence for modern IT operations.

---

## Who is this for?
This solution is designed for security professionals and IT administrators who need to maintain network integrity without manual oversight.

* **Security Operations Center (SOC) Analyst**
    * Automates the triage of suspicious network requests to focus on high-priority threats.
* **Network Administrator**
    * Gains real-time visibility into domain filtering status and infrastructure health.
* **DevOps Engineer**
    * Integrates security monitoring directly into existing CI/CD or infrastructure management pipelines.
* **IT Compliance Officer**
    * Generates automated reports on network traffic and blocked malicious activity for audit readiness.

---

## Features
- **Real-time Threat Detection**
  Continuous monitoring of network traffic to identify and flag malicious domains instantly.
- **Automated DNS Filtering**
  Seamless integration with DNSFilter to enforce security policies and block unauthorized access points.
- **Intelligent Alerting**
  Context-aware notifications that prioritize alerts based on threat severity and historical data.
- **Unified Security Dashboard**
  A centralized view of network health, integrating data from multiple security endpoints via the Composio Toolset.
- **Automated Incident Response**
  Trigger automated workflows to isolate compromised nodes or update firewall rules upon threat detection.

---

## Use Cases
**Proactive Threat Hunting**
* Automatically scan DNS query logs for patterns indicative of command-and-control (C2) server communication.
* Flag newly registered domains that exhibit suspicious traffic spikes within the corporate network.

**Compliance and Reporting**
* Generate weekly summaries of blocked threats and policy violations for executive stakeholders.
* Ensure all network endpoints adhere to organizational security policies by auditing DNSFilter configurations.

**Infrastructure Health Monitoring**
* Receive instant alerts when network throughput deviates from established baselines.
* Automate the reconciliation of active network devices against the authorized asset inventory.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Network Security Monitor template from the solution library.
3. Connect your DNSFilter API credentials to the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives security queries or automated trigger signals.
* **Agent**: Processes network logs and evaluates threat levels using LLM reasoning.
* **Composio Toolset**: Executes API calls to DNSFilter for real-time data retrieval and policy updates.
* **Chat Output**: Delivers actionable insights and security reports to the user or notification channel.

### 3) Run the Flow
Use the Playground to test your monitor with these prompts:
* `Check for any high-severity threats detected in the network logs over the last 24 hours.`
* `Generate a summary report of all blocked domains for the engineering department.`
* `Identify any anomalous traffic patterns originating from the internal server subnet.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security analyst, interpreting logs and determining the appropriate response.
* Focus on identifying patterns related to known threat signatures.
* Maintain a professional, concise tone for all security alerts.
* Prioritize actionable data over raw log output.

### 2) Composio Toolset Node
* Requires a valid DNSFilter API Key with read/write permissions.
* Connection scope should be limited to the specific network zones you intend to monitor.

### 3) Tool Availability
* `dnsfilter_get_logs`: Fetches recent DNS query and threat logs.
* `dnsfilter_update_policy`: Adjusts filtering rules based on detected threats.
* `dnsfilter_get_threat_intel`: Retrieves updated threat intelligence feeds.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automated auditing and security compliance checks for cloud infrastructure.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Real-time monitoring of automated workflow performance and status.
* [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Managing and auditing user permissions to ensure secure access control.
