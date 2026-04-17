# Performance Dashboard Generator (Uplizd) - Automated observability and metric visualization

## Summary
The Performance Dashboard Generator (Uplizd) is an intelligent workflow that automates the creation of custom observability dashboards by analyzing service architecture and infrastructure metrics. By leveraging the Composio Toolset to interface with Datadog, this solution eliminates manual configuration overhead, ensuring DevOps and SRE teams maintain a single source of truth for system health and pipeline velocity.

---

## Demo
![Performance Dashboard Generator workflow diagram showing Datadog integration](image.png)
**Alt text (SEO-ready):** Performance Dashboard Generator (Uplizd) workflow showing automated Datadog dashboard creation, observability metrics, and infrastructure monitoring integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3dae0dfa-ecae-55c4-afa3-ff21d054736c)

---

## Category
**Primary category:** Data integration
**Secondary tags:** datadog, observability, dashboarding, devops, sre, infrastructure, monitoring, composio, ai workflow.
This solution bridges the gap between raw infrastructure data and actionable visual insights, streamlining the deployment of monitoring environments.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining high-availability systems and clear visibility into service performance.

* **Site Reliability Engineer (SRE)**
    * Reduces mean time to resolution (MTTR) by instantly deploying standard dashboards for new microservices.
* **DevOps Engineer**
    * Automates the provisioning of monitoring infrastructure, ensuring consistency across staging and production environments.
* **Engineering Manager**
    * Gains high-level visibility into system performance trends and resource utilization without manual reporting.
* **Cloud Architect**
    * Ensures that infrastructure deployments are automatically coupled with the necessary observability hooks and visual metrics.

---

## Features
- **Automated Dashboard Provisioning**
  Instantly generates Datadog dashboards based on service metadata, reducing manual setup time.
- **Dynamic Metric Mapping**
  Intelligently maps infrastructure components to relevant performance widgets using the Composio Toolset.
- **Real-time Health Monitoring**
  Configures real-time alerts and status indicators directly within the generated dashboard views.
- **Cross-Service Correlation**
  Aggregates data across multiple services to provide a unified view of complex distributed architectures.
- **Template-Driven Configuration**
  Uses standardized templates to ensure all dashboards adhere to organizational observability best practices.

---

## Use Cases
**Infrastructure Observability**
* Automatically generating dashboards for newly deployed Kubernetes clusters or microservices.
* Mapping CPU, memory, and latency metrics to visual widgets during service scaling events.

**Incident Response Preparation**
* Creating specialized "war room" dashboards during active outages to track critical service dependencies.
* Consolidating error logs and throughput metrics into a single view for rapid root-cause analysis.

**Capacity Planning**
* Visualizing historical resource utilization trends to inform infrastructure rightsizing decisions.
* Tracking performance degradation over time to proactively identify potential system bottlenecks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the builder.
2. Connect your Datadog account via the Composio Toolset node.
3. Configure the input parameters to define your service architecture scope.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Accepts service names, environment tags, and dashboard requirements.
* **Agent**: Processes requirements and maps them to Datadog API dashboard specifications.
* **Composio Toolset**: Executes the API calls to provision dashboards in your Datadog instance.
* **Chat Output**: Returns the dashboard URL and a summary of the configured widgets.

### 3) Run the Flow
Use the Playground to test the flow with these prompts:
* `Create a performance dashboard for the 'payment-gateway' service in the production environment.`
* `Generate a high-level observability dashboard for all microservices in the 'us-east-1' region.`
* `Build a latency-focused dashboard for the 'user-auth' service including error rate widgets.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer, translating natural language requests into structured API configurations.
* Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "Analyze the user's request, identify the relevant service metrics, and map them to standard Datadog dashboard widgets."
* Ensure the agent is instructed to validate service names against existing infrastructure metadata.

### 2) Composio Toolset Node
* Requires a valid Datadog API key and Application key provided via the Composio connection.
* Scope the connection to allow `dashboard:write` and `dashboard:read` permissions.

### 3) Tool Availability
* **Dashboard Management**: Create, update, and delete dashboard definitions.
* **Metric Querying**: Fetch current metric availability for specific service tags.
* **Widget Configuration**: Apply standard visualization templates (timeseries, query values, heatmaps).

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and execution health of automated workflows.
* [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Analyzes user engagement and account usage metrics for proactive health monitoring.
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Performs comprehensive security and configuration audits on cloud infrastructure.
