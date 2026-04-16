# Alerting Rule Curator (Uplizd) - Intelligent automation for monitoring and alert hygiene

## Summary
The Alerting Rule Curator is an automated Uplizd workflow designed to streamline the management, optimization, and maintenance of monitoring alerts. By leveraging AI-driven analysis, it ensures that your alerting infrastructure remains clean, actionable, and free from noise, ultimately improving incident response velocity and reducing alert fatigue for DevOps and SRE teams.

---

## Demo
![Alerting Rule Curator workflow showing automated rule analysis and cleanup](image.png)
**Alt text (SEO-ready):** Uplizd Alerting Rule Curator workflow for automated monitoring rule cleanup, noise reduction, and incident management integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/b6134d2c-11dd-52a9-9036-313fbc814ef8)

---

## Category
**Primary category:** Operations
**Secondary tags:** monitoring, alerting, devops, sre, noise reduction, data hygiene, automation, composio
This solution optimizes monitoring infrastructure by automating the lifecycle management of alerting rules to ensure high-signal incident reporting.

---

## Who is this for?
This solution is designed for technical teams looking to maintain a high-signal, low-noise monitoring environment.

* **Site Reliability Engineer (SRE)**
    * Reduces alert fatigue by identifying and pruning redundant or flapping alerting rules.
* **DevOps Manager**
    * Ensures consistent alerting standards across distributed infrastructure environments.
* **System Administrator**
    * Automates the documentation and categorization of complex monitoring thresholds.
* **Incident Response Lead**
    * Improves mean time to acknowledge (MTTA) by ensuring only critical, actionable alerts reach the team.

---

## Features
- **Automated Rule Discovery**
    Scan existing monitoring configurations to identify active, inactive, or duplicate alerting rules across your stack.
- **Noise Reduction Analysis**
    Use AI to evaluate rule trigger frequency and correlate them with historical incident data to flag "noisy" alerts.
- **Intelligent Threshold Tuning**
    Receive automated recommendations for adjusting alert thresholds based on current performance baselines and traffic patterns.
- **Composio-Powered Integration**
    Seamlessly connect with monitoring platforms and ticketing systems to execute rule updates and documentation tasks.
- **Compliance & Audit Logging**
    Maintain a clear audit trail of all rule modifications, deletions, or updates performed by the agent for regulatory compliance.

---

## Use Cases
**Alert Hygiene & Cleanup**
* Automatically disable stale alerting rules that have not triggered in over 90 days.
* Consolidate duplicate alerting rules across multiple environments into a single, unified policy.

**Incident Response Optimization**
* Prioritize critical alerts by dynamically updating severity levels based on real-time service impact.
* Auto-generate incident response documentation when specific high-priority alerting rules are triggered.

**Monitoring Infrastructure Scaling**
* Standardize naming conventions and metadata for new alerting rules during the provisioning process.
* Perform bulk updates to notification channels when team on-call rotations or escalation policies change.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace and project destination.
3. Configure your API credentials for the target monitoring platform.
4. Ensure nodes are correctly mapped and the Composio Toolset is authorized for read/write access.

### 2) Setup the Nodes
* **Chat Input**: Receives the request for rule analysis or specific cleanup commands.
* **Agent**: Analyzes the monitoring data and determines the necessary rule modifications.
* **Composio Toolset**: Executes the API calls to update, delete, or create monitoring rules.
* **Chat Output**: Provides a summary report of the actions taken and the current state of the alerting rules.

### 3) Run the Flow
* `Analyze all alerting rules for the production environment and identify those with high false-positive rates.`
* `Disable all monitoring rules associated with the legacy 'v1-api' service.`
* `Generate a report of all alerting rules modified in the last 30 days and their current status.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized SRE assistant.
* Use a model with strong logical reasoning capabilities to interpret monitoring thresholds.
* Provide clear instructions on the hierarchy of alert severity.
* Ensure the agent has access to the current incident history context.

### 2) Composio Toolset Node
* Provide your API key for the monitoring platform (e.g., Datadog, New Relic, or Prometheus).
* Ensure the connection scope includes `read_rules` and `write_rules` permissions.

### 3) Tool Availability
* **Rule Discovery**: Fetching current configurations.
* **Threshold Adjustment**: Updating trigger conditions.
* **Rule Lifecycle Management**: Enabling, disabling, or deleting rules.
* **Log & Audit**: Exporting change history to external storage.

---

## Related Solutions
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automates security and configuration audits for cloud infrastructure.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and performance of automated workflows.
* [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Manages and audits user permissions and access levels across systems.
