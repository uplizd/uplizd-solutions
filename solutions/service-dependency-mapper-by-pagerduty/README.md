# Service Dependency Mapper (Uplizd) - Automated incident impact assessment and service topology mapping

## Summary
The Service Dependency Mapper by PagerDuty is an intelligent Uplizd workflow that automatically discovers, maps, and visualizes complex service relationships. By leveraging real-time data from PagerDuty, this solution empowers DevOps and SRE teams to instantly assess the blast radius of incidents, reduce mean time to resolution (MTTR), and maintain a clean, accurate source of truth for infrastructure dependencies.

---

## Demo
![Service Dependency Mapper workflow showing PagerDuty incident integration and dependency mapping nodes](image.png)
**Alt text (SEO-ready):** Service Dependency Mapper workflow by PagerDuty for automated incident impact assessment, infrastructure topology mapping, and Uplizd AI-driven DevOps automation.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/49d8514d-f5dc-5424-816e-0e0b110b1629)

---

## Category
**Primary category:** Operations
**Secondary tags:** pagerduty, devops, sre, incident management, service mapping, infrastructure, automation, composio, ai workflow.
This solution bridges the gap between raw incident alerts and actionable infrastructure topology, enabling faster root cause analysis.

---

## Who is this for?
This solution is designed for technical teams managing complex distributed systems who need to minimize downtime and improve operational clarity.

*   **Site Reliability Engineers (SREs)**
    *   Instantly visualize service dependencies to identify the root cause of cascading failures during high-pressure incidents.
*   **DevOps Engineers**
    *   Automate the maintenance of service topology maps, ensuring documentation stays synced with real-world infrastructure changes.
*   **Incident Commanders**
    *   Rapidly assess the blast radius of an active incident to determine which downstream services and stakeholders are impacted.
*   **Engineering Managers**
    *   Gain high-level visibility into service health and interdependencies to prioritize technical debt and architectural improvements.

---

## Features
- **Real-time Dependency Discovery**
  Automatically syncs with PagerDuty to map service relationships as they evolve in your production environment.
- **Automated Impact Analysis**
  Uses AI to correlate incident alerts with specific service dependencies, highlighting affected components instantly.
- **Composio-Powered Integration**
  Seamlessly connects with your existing PagerDuty toolset to fetch service metadata and incident logs without manual configuration.
- **Dynamic Topology Visualization**
  Generates clear, actionable insights into how a single service failure propagates across your microservices architecture.
- **Incident Response Acceleration**
  Reduces the time spent manually tracing dependencies, allowing teams to focus on remediation and service restoration.

---

## Use Cases
**Incident Impact Assessment**
*   Automatically identify all downstream services affected by a primary service outage.
*   Generate a summary of impacted dependencies to share with stakeholders during incident post-mortems.

**Infrastructure Documentation**
*   Maintain an up-to-date map of service interdependencies without the need for manual diagramming.
*   Identify "orphan" services or undocumented connections that pose a risk to system stability.

**Change Management**
*   Analyze the potential impact of a planned service deployment on existing infrastructure before execution.
*   Verify that new service additions are correctly mapped within the existing dependency graph.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Authenticate your PagerDuty account within the Composio Toolset node.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the incident ID or service name from the user.
*   **Agent**: Processes the request and queries the PagerDuty API for dependency data.
*   **Composio Toolset**: Executes the specific PagerDuty functions to retrieve service topology.
*   **Chat Output**: Returns a structured report of the service dependencies and potential impact.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
*   `Map the dependencies for the 'Checkout-Service' and identify potential failure points.`
*   `What is the blast radius of the current incident ID PD-9928?`
*   `List all downstream services that depend on the 'Payment-Gateway' service.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an SRE assistant, translating natural language queries into API calls.
*   Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
*   Instruction: "You are an expert SRE assistant. Use the provided PagerDuty tools to map service dependencies."
*   Instruction: "Always prioritize identifying critical path dependencies that could cause cascading failures."

### 2) Composio Toolset Node
*   **API Key**: Provide your PagerDuty API key in the node settings.
*   **Connection Scope**: Ensure the token has read-only access to services, incidents, and dependency mapping endpoints.

### 3) Tool Availability
*   `pagerduty_get_service_dependencies`: Retrieves the list of upstream and downstream services.
*   `pagerduty_get_incident_details`: Fetches metadata for specific active incidents.
*   `pagerduty_list_services`: Provides a comprehensive overview of your service catalog.

---

## Related Solutions
*   [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Automate the prioritization of incident-related tasks.
*   [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the operational health of your automated workflows.
*   [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform security and configuration audits across your infrastructure.
