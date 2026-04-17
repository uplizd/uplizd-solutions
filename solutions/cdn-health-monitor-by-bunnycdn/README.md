# CDN Health Monitor (Uplizd) - Proactive infrastructure performance and availability management

## Summary
The CDN Health Monitor is an automated Uplizd AI workflow designed to provide real-time visibility into your content delivery network's performance. By leveraging the Composio Toolset to interface with BunnyCDN, this solution continuously tracks latency, error rates, and cache hit ratios, ensuring high availability and optimal delivery speeds for your global web assets.

---

## Demo
![CDN Health Monitor dashboard showing real-time latency and cache hit ratio metrics](image.png)
**Alt text (SEO-ready):** CDN Health Monitor dashboard showing real-time latency, error rates, and cache hit ratio metrics for Uplizd AI infrastructure workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/86a863f4-4321-535a-942c-43ceea901e82)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** cdn, bunnycdn, infrastructure, monitoring, performance, uptime, composio, ai workflow
- This solution bridges the gap between raw CDN telemetry and actionable infrastructure insights for DevOps teams.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining high-performance web delivery and minimizing downtime.

- **Site Reliability Engineer (SRE)**
    - Automates incident detection and reduces mean time to resolution (MTTR) for CDN-related outages.
- **DevOps Manager**
    - Ensures infrastructure compliance and performance SLAs are met through continuous automated auditing.
- **Web Performance Architect**
    - Identifies bottlenecks in content delivery paths to optimize global user experience.
- **Cloud Infrastructure Admin**
    - Simplifies the monitoring of complex multi-region CDN configurations without manual dashboard fatigue.

---

## Features
- **Real-time Performance Tracking**
  Monitors latency and throughput metrics directly from your CDN provider to ensure consistent delivery speeds.
- **Automated Error Detection**
  Instantly identifies spikes in 4xx or 5xx error codes, triggering alerts before they impact end-users.
- **Cache Efficiency Analysis**
  Evaluates cache hit ratios to identify under-performing assets and optimize origin server load.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely execute API calls and retrieve granular CDN health data.
- **Actionable Insight Generation**
  Translates complex technical logs into plain-language summaries for rapid decision-making.

---

## Use Cases
**Infrastructure Reliability**
- Automatically verify CDN uptime status across multiple global regions every 15 minutes.
- Detect and report sudden increases in origin request latency during peak traffic periods.

**Performance Optimization**
- Identify specific assets or URL patterns that are frequently missing the cache.
- Generate weekly reports on CDN performance trends to inform infrastructure scaling decisions.

**Incident Response**
- Trigger automated notifications when error rates exceed defined thresholds for specific zones.
- Quickly query historical health data to troubleshoot intermittent connectivity issues reported by users.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the CDN Health Monitor workflow.
3. Authenticate your BunnyCDN account via the Composio connection prompt.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries or scheduled trigger signals.
- **Agent**: Processes health data and interprets infrastructure metrics.
- **Composio Toolset**: Executes API requests to fetch real-time CDN status.
- **Chat Output**: Delivers formatted health reports and incident summaries.

### 3) Run the Flow
Use the Playground to test the agent's monitoring capabilities:
- `Check the current health status and latency for my primary CDN zone.`
- `Are there any unusual error rate spikes in the last hour?`
- `Provide a summary of the cache hit ratio for the static assets zone.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an infrastructure analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize identifying anomalies over standard operational data.
- Ensure the agent is configured to output clear, actionable recommendations for any detected issues.

### 2) Composio Toolset Node
- Provide your BunnyCDN API key within the Composio dashboard.
- Limit the connection scope to read-only access for monitoring purposes to maintain security best practices.

### 3) Tool Availability
- **Zone Metrics Fetcher**: Retrieves latency, bandwidth, and request counts.
- **Error Log Analyzer**: Parses recent HTTP response codes for anomaly detection.
- **Cache Status Reporter**: Queries cache hit/miss ratios for specific zones.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Comprehensive audit and security monitoring for cloud infrastructure.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Automated tracking of internal workflow performance and team productivity.
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) — Automates the setup and configuration of new CDN zones and security policies.
