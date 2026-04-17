# Network Intelligence Analyst (Uplizd) - Automated BGP and ASN infrastructure monitoring

## Summary
The Network Intelligence Analyst is an automated Uplizd AI workflow designed to streamline BGP and ASN monitoring for network operations teams. By leveraging real-time data ingestion and intelligent analysis, this solution provides a single source of truth for network health, reducing incident response times and ensuring pipeline velocity for critical infrastructure updates.

---

## Demo
![Network Intelligence Analyst dashboard showing real-time BGP routing updates and ASN health metrics](image.png)
**Alt text (SEO-ready):** Network Intelligence Analyst dashboard showing real-time BGP routing updates, ASN health metrics, Uplizd workflow, and network infrastructure monitoring integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/886997fe-45c2-55f5-9296-a680689abb2e)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** network operations, bgp, asn, infrastructure monitoring, data sync, ai workflow, composio, cloudflare
- This solution bridges the gap between raw network telemetry and actionable insights, enabling automated infrastructure oversight.

---

## Who is this for?
This solution is designed for technical teams managing complex network topologies and global routing infrastructure.

- **Network Engineer**
    - Automates the detection of BGP route leaks and prefix hijacking attempts.
- **Site Reliability Engineer (SRE)**
    - Monitors ASN health metrics to proactively prevent service outages.
- **Cloud Infrastructure Manager**
    - Synchronizes network configuration changes across multi-cloud environments.
- **Security Operations Analyst**
    - Identifies anomalous traffic patterns originating from suspicious autonomous systems.

---

## Features
- **Real-time BGP Monitoring**
    - Tracks routing table changes and prefix updates to ensure global network stability.
- **ASN Health Analytics**
    - Aggregates performance data from autonomous systems to identify latency or connectivity bottlenecks.
- **Automated Incident Triage**
    - Uses the Composio Toolset to trigger alerts and diagnostic workflows when network anomalies are detected.
- **Cross-Platform Data Sync**
    - Integrates with Cloudflare and other network providers to maintain a unified state of network configurations.
- **Intelligent Alerting**
    - Filters noise from network logs, surfacing only high-priority routing events to the operations team.

---

## Use Cases
**Proactive Network Defense**
- Detecting unauthorized BGP prefix advertisements before they impact global traffic.
- Automating the rollback of routing configurations when latency thresholds are exceeded.

**Infrastructure Compliance**
- Auditing ASN registration data against internal security policies to ensure compliance.
- Generating automated reports on network uptime and routing efficiency for stakeholders.

**Operational Efficiency**
- Streamlining the onboarding of new network segments by automating verification checks.
- Reducing manual log analysis time by using AI to correlate routing events with system performance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Network Intelligence Analyst template from the marketplace.
3. Configure your API credentials for your network provider (e.g., Cloudflare).
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives network queries or automated trigger events.
- **Agent**: Analyzes routing data and determines the appropriate diagnostic action.
- **Composio Toolset**: Executes commands to fetch BGP/ASN data and perform network audits.
- **Chat Output**: Delivers summarized insights and incident reports to the dashboard.

### 3) Run the Flow
Use the Playground to test your network analysis:
- `Analyze the current BGP routing table for any unauthorized prefix advertisements.`
- `Check the health status of ASN 13335 and report any latency spikes.`
- `Summarize the last 24 hours of network configuration changes.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized network analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system prompt to prioritize security and uptime metrics.
- Configure the agent to output structured JSON for downstream integration.

### 2) Composio Toolset Node
- Provide your API key for the relevant network infrastructure provider.
- Set the connection scope to read-only for monitoring, or read-write for automated remediation.

### 3) Tool Availability
- **BGP Fetcher**: Retrieves real-time routing information.
- **ASN Validator**: Cross-references autonomous system data against global databases.
- **Alert Dispatcher**: Sends notifications to Slack or PagerDuty upon anomaly detection.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md): Automated auditing for cloud account security and configuration.
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md): Streamlined management of network zones and DNS settings.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md): Monitoring the operational status of automated business workflows.
