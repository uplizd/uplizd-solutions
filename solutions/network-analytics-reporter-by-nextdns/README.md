# Network Analytics Reporter (Uplizd) - Automated DNS traffic insights and performance reporting

## Summary
The Network Analytics Reporter is an automated Uplizd AI workflow that streamlines the collection, analysis, and reporting of DNS traffic data from NextDNS. By leveraging the Composio Toolset to interface with network logs, this solution provides IT administrators and security teams with a single source of truth for traffic patterns, threat detection, and performance metrics, significantly reducing the time spent on manual log review and network hygiene.

---

## Demo
![Network Analytics Reporter dashboard showing DNS query trends and threat blocking statistics](image.png)
**Alt text (SEO-ready):** Network Analytics Reporter dashboard showing DNS query trends and threat blocking statistics for Uplizd AI network monitoring workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3cec318a-2ee7-52c4-a50e-f78417b271b4)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** network analytics, nextdns, dns logs, security monitoring, automated reporting, data hygiene, composio, ai workflow
- This solution bridges the gap between raw DNS log data and actionable security intelligence through automated AI-driven analysis.

---

## Who is this for?
The Network Analytics Reporter is designed for professionals managing network infrastructure and security posture.

- **IT Administrators**
    - Automate the generation of weekly network health reports without manual log parsing.
- **Security Analysts**
    - Identify anomalous traffic patterns and potential security threats in real-time.
- **DevOps Engineers**
    - Monitor DNS performance and latency to ensure optimal service connectivity.
- **Compliance Officers**
    - Maintain detailed records of network traffic for internal audits and security compliance.

---

## Features
- **Automated Log Retrieval**
    - Seamlessly pulls DNS query logs from NextDNS using the Composio Toolset for real-time data access.
- **Intelligent Traffic Analysis**
    - Uses advanced LLM reasoning to categorize traffic, identify top domains, and flag suspicious activity.
- **Customizable Reporting**
    - Generates structured summaries that highlight performance bottlenecks and security incidents.
- **Threat Detection Alerts**
    - Automatically filters and highlights blocked queries related to known malicious domains or trackers.
- **Unified Data Visualization**
    - Translates complex log data into human-readable insights, perfect for stakeholder presentations.

---

## Use Cases
**Network Security Auditing**
- Identify and report on high-frequency blocked requests that indicate potential malware or phishing attempts.
- Audit DNS configurations to ensure compliance with organizational security policies.

**Performance Optimization**
- Analyze query latency trends to pinpoint geographical or service-specific connectivity issues.
- Evaluate the impact of DNS filtering rules on overall network throughput and user experience.

**Operational Reporting**
- Generate recurring executive summaries of network usage patterns and top-visited domains.
- Create ad-hoc reports for troubleshooting specific service outages or unexpected traffic spikes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your project dashboard.
3. Connect your NextDNS API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language query or reporting schedule.
- **Agent**: Processes the request and orchestrates the data retrieval logic.
- **Composio Toolset**: Executes the API calls to fetch and filter DNS logs.
- **Chat Output**: Delivers the final, formatted analytics report to the user.

### 3) Run the Flow
Use the Playground to test your reporting capabilities:
- `Generate a summary of all blocked DNS requests from the last 24 hours.`
- `Which domains are consuming the most bandwidth in our network this week?`
- `Create a security report highlighting any suspicious traffic patterns detected today.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting raw logs into business intelligence.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate log parsing.
- Set the system instruction to prioritize security-focused insights and clear, concise summaries.
- Ensure the agent has access to the full scope of DNS log metadata for comprehensive analysis.

### 2) Composio Toolset Node
- Provide your NextDNS API Key to authorize the agent to read your account logs.
- Configure the connection scope to allow read-only access to query logs and analytics endpoints.

### 3) Tool Availability
- `fetch_dns_logs`: Retrieves raw query data for a specified time range.
- `get_security_events`: Isolates blocked or flagged requests from the log stream.
- `analyze_traffic_patterns`: Aggregates data to identify top domains and usage trends.

---

## Related Solutions
- [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automate security audits and configuration reviews for your cloud infrastructure.
- [Zone Provisioning Agent by Cloudflare](../zone-provisioning-agent-by-cloudflare/README.md) - Streamline the management and provisioning of network zones and security settings.
- [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Track the performance and reliability of your automated operational workflows.
