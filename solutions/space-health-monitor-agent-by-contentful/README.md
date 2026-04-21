# Space Health Monitor Agent (Uplizd) - Automated Contentful infrastructure integrity and performance tracking

## Summary
The Space Health Monitor Agent by Uplizd provides automated, real-time oversight of your Contentful environments, ensuring content delivery stability and infrastructure hygiene. By continuously scanning for configuration drift, asset errors, and delivery bottlenecks, this workflow empowers teams to resolve potential content delivery issues before they impact end-users, serving as a single source of truth for your digital content health.

---

## Demo
![Space Health Monitor Agent workflow dashboard showing Contentful integration and health status alerts](image.png)
**Alt text (SEO-ready):** Space Health Monitor Agent for Contentful, automated infrastructure health dashboard, Uplizd AI workflow, content delivery monitoring, and Composio integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4a8aa083-070b-5c50-8e0e-c4dbbdac7cc1)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** contentful, cms, data hygiene, infrastructure monitoring, automation, composio, ai workflow, content delivery
- This solution bridges the gap between technical infrastructure monitoring and marketing content operations to ensure seamless digital experiences.

---

## Who is this for?
This agent is designed for teams managing high-scale content operations who need proactive visibility into their CMS environment.

- **Content Operations Manager**
    - Ensures content delivery pipelines remain uninterrupted and error-free.
- **Technical SEO Specialist**
    - Monitors for broken assets or configuration issues that could negatively impact search rankings.
- **CMS Administrator**
    - Automates routine health checks to reduce manual auditing time across multiple spaces.
- **Developer/DevOps Engineer**
    - Receives real-time alerts on infrastructure drift or API rate limit warnings within Contentful.

---

## Features
- **Automated Health Audits**
    - Scheduled, real-time scans of Contentful spaces to detect configuration drift and broken references.
- **Content Delivery Monitoring**
    - Proactive identification of delivery API bottlenecks that could slow down front-end performance.
- **Composio-Powered Integration**
    - Seamless connectivity with Contentful via Composio, allowing the agent to execute deep-level environment checks.
- **Proactive Alerting**
    - Instant notifications regarding critical health status changes or potential content delivery failures.
- **Infrastructure Hygiene Reporting**
    - Comprehensive summaries of space health, providing actionable insights for maintenance and cleanup.

---

## Use Cases
**Content Infrastructure Maintenance**
- Automatically scan for orphaned content entries or broken media links that degrade site performance.
- Validate environment settings against best-practice configurations to prevent deployment errors.

**Performance & Delivery Optimization**
- Monitor Contentful Delivery API response times to identify latency spikes before they affect users.
- Track asset usage patterns to optimize storage and delivery costs across global CDN nodes.

**Compliance & Governance**
- Audit content schemas to ensure all entries adhere to mandatory field requirements and naming conventions.
- Maintain a consistent audit trail of all automated health checks for internal compliance reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Authenticate your Contentful account via the Composio connection prompt.
4. Ensure nodes are correctly mapped and the API credentials are active in the settings panel.

### 2) Setup the Nodes
- **Chat Input**: Receives manual health check triggers or scheduled monitoring commands.
- **Agent**: Analyzes the Contentful environment and interprets health data using the configured logic.
- **Composio Toolset**: Executes API calls to fetch space metadata, audit logs, and delivery performance metrics.
- **Chat Output**: Returns a summary report of the space health status and any recommended remediation steps.

### 3) Run the Flow
Use the Playground to test your agent with these prompts:
- `Run a full health audit on the production space and list any broken references.`
- `Check the current delivery API performance and report any latency issues.`
- `Identify any content entries that are missing required metadata fields.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent is configured to act as a technical auditor, prioritizing accuracy and clear, actionable reporting.
- Use a high-reasoning model to interpret complex API logs.
- Instruct the agent to prioritize "Critical" and "High" severity issues in its summary.
- Maintain a professional, technical tone suitable for DevOps and ContentOps documentation.

### 2) Composio Toolset Node
- Provide your Contentful API Key and Space ID within the Composio connection settings.
- Ensure the connection scope includes read-only access to Content Management and Delivery APIs for security.

### 3) Tool Availability
- **Contentful Space Auditor**: Scans for configuration errors and schema inconsistencies.
- **API Performance Tracker**: Monitors latency and request success rates.
- **Asset Link Validator**: Checks for broken image or file references across all entries.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track account usage metrics and health indicators.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor the operational health of your automated workflows.
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform deep-level security and configuration audits on your accounts.
