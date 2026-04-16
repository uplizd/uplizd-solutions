# Build Capacity Optimizer (Uplizd) - CI/CD Infrastructure Cost and Utilization Management

## Summary
The Build Capacity Optimizer (Uplizd) is an intelligent workflow designed to monitor and optimize CI/CD infrastructure by analyzing agent utilization patterns. By integrating directly with Buildkite, this solution provides engineering teams with actionable insights to reduce idle compute costs, improve pipeline velocity, and ensure optimal resource allocation across distributed build environments.

---

## Demo
![Build Capacity Optimizer dashboard showing agent utilization metrics and cost-saving recommendations](image.png)
**Alt text (SEO-ready):** Build Capacity Optimizer dashboard showing agent utilization metrics, CI/CD cost-saving recommendations, and Buildkite infrastructure analytics on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/d9ec7a4e-57e6-5d17-a1e6-e9510b9e1b4c)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** ci/cd, buildkite, infrastructure, cost optimization, devops, pipeline, automation, composio
- This solution bridges the gap between raw CI/CD telemetry and infrastructure efficiency, enabling automated resource rightsizing.

---

## Who is this for?
This solution is designed for engineering and infrastructure teams looking to maintain high-performance build pipelines while controlling cloud expenditure.

- **DevOps Engineer**
    - Automate the scaling of build agents based on real-time queue depth and historical load.
- **Engineering Manager**
    - Gain visibility into CI/CD spend and identify underutilized build capacity.
- **Platform Architect**
    - Standardize infrastructure cleanup policies to prevent "zombie" agents from consuming budget.
- **SRE (Site Reliability Engineer)**
    - Monitor build pipeline health and receive alerts when agent saturation impacts deployment latency.

---

## Features
- **Real-time Utilization Tracking**
    - Continuously ingest agent metrics to identify bottlenecks and idle periods in your CI/CD pipeline.
- **Automated Scaling Logic**
    - Trigger dynamic adjustments to agent pools using the Composio Toolset to match current build demand.
- **Cost-Efficiency Analytics**
    - Generate automated reports that correlate build volume with infrastructure spend for better budget forecasting.
- **Intelligent Alerting**
    - Receive proactive notifications when agent capacity is consistently over-provisioned or hitting critical limits.
- **Seamless Buildkite Integration**
    - Leverage native API connectors to manage agent states and queue configurations without manual intervention.

---

## Use Cases
**Infrastructure Cost Reduction**
- Automatically terminate idle build agents during off-peak hours to minimize cloud compute expenses.
- Right-size agent instance types based on historical build duration and resource consumption patterns.

**Pipeline Performance Optimization**
- Dynamically burst agent capacity during high-traffic deployment windows to reduce developer wait times.
- Identify and resolve stalled build jobs caused by insufficient agent availability or configuration drift.

**Operational Hygiene**
- Audit agent configurations to ensure compliance with security and resource tagging standards.
- Automate the decommissioning of legacy or orphaned build agents to maintain a clean CI environment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Buildkite account within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input:** Receives the trigger signal or manual request for capacity analysis.
- **Agent:** Processes the infrastructure data and applies optimization logic.
- **Composio Toolset:** Executes API calls to Buildkite to fetch metrics and manage agents.
- **Chat Output:** Delivers the summary report and optimization recommendations to the user.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Analyze my Buildkite agent utilization for the last 7 days and suggest cost-saving actions.`
- `Identify any idle agents that have been running for more than 2 hours.`
- `Scale down the agent pool for the 'frontend-build' queue to save costs during the weekend.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an infrastructure analyst.
- Focus on identifying patterns in agent uptime versus build completion times.
- Prioritize cost-saving recommendations that do not negatively impact build latency.
- Maintain a professional, data-driven tone when reporting findings.

### 2) Composio Toolset Node
- **API Key:** Provide your Buildkite API token with read/write access to agent and pipeline settings.
- **Connection Scope:** Ensure the toolset has permissions to list agents, inspect queue status, and update agent configurations.

### 3) Tool Availability
- `list_agents`: Retrieve current status and uptime of all build agents.
- `get_queue_metrics`: Analyze throughput and wait times for specific pipelines.
- `update_agent_state`: Modify agent status or terminate underutilized instances.

---

## Related Solutions
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and optimize overall team workflow performance.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Perform comprehensive security and configuration audits.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamline administrative setup and resource provisioning.
