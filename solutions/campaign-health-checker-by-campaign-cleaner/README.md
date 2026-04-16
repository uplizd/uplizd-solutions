# Campaign Health Checker (Uplizd) - Proactive email campaign monitoring and performance optimization

## Summary
The Campaign Health Checker is an automated Uplizd AI workflow designed to monitor email marketing performance, identify delivery bottlenecks, and flag engagement anomalies in real-time. By connecting directly to your marketing automation stack, this solution ensures your campaigns maintain high deliverability and reach, providing a single source of truth for campaign health and pipeline velocity.

---

## Demo
![Campaign Health Checker workflow interface showing automated monitoring of email metrics and alert triggers](image.png)
**Alt text (SEO-ready):** Campaign Health Checker Uplizd workflow, email marketing automation, campaign performance monitoring, and real-time alert integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/4c4986ed-e396-5e9d-91b8-b896a8cf35b9)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, campaign management, data hygiene, marketing automation, performance monitoring, composio, ai workflow
- This solution streamlines marketing operations by automating the detection of campaign decay and performance dips.

---

## Who is this for?
This solution is built for marketing teams looking to maintain high engagement rates and operational efficiency.

- **Marketing Manager**
    - Automates the identification of underperforming campaigns to prevent budget waste.
- **Email Marketing Specialist**
    - Monitors delivery metrics and bounce rates to ensure list health and sender reputation.
- **Marketing Operations Lead**
    - Maintains a consistent feedback loop between campaign performance and CRM data.
- **Growth Marketer**
    - Rapidly iterates on campaign strategies based on real-time health alerts and data signals.

---

## Features
- **Real-time Performance Monitoring**
    - Tracks key email metrics continuously to detect anomalies as they occur.
- **Automated Anomaly Detection**
    - Uses AI to flag sudden drops in open rates or spikes in unsubscribe counts.
- **Integrated Alerting System**
    - Pushes health notifications directly to your team's preferred communication channels.
- **Composio-Powered CRM Sync**
    - Seamlessly connects with marketing platforms to pull data and push corrective actions.
- **Campaign Hygiene Reporting**
    - Generates actionable insights to clean up lists and improve future campaign targeting.

---

## Use Cases
**Proactive Issue Resolution**
- Automatically pause campaigns showing high bounce rates to protect sender reputation.
- Trigger alerts when open rates fall below a predefined threshold for specific segments.

**Performance Optimization**
- Analyze A/B test results to identify the highest-performing subject lines and content blocks.
- Sync campaign engagement data back to the CRM to refine lead scoring models.

**List and Data Hygiene**
- Identify inactive subscribers based on long-term campaign disengagement patterns.
- Flag duplicate or malformed contact entries that impact campaign delivery success.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Campaign Health Checker template from the solution library.
3. Connect your required marketing and CRM accounts via the Composio integration panel.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled health check requests.
- **Agent**: Analyzes campaign data and determines if performance metrics are within acceptable ranges.
- **Composio Toolset**: Executes API calls to fetch campaign stats and update CRM records.
- **Chat Output**: Delivers a summary report or specific alerts regarding campaign health.

### 3) Run the Flow
Use the Playground to test your setup with these prompts:
- `Check the health status of the 'Q3 Newsletter' campaign and report any delivery issues.`
- `Identify all campaigns with an open rate lower than 15% from the last 7 days.`
- `Run a full audit on the current email list and flag inactive contacts for removal.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as a specialized marketing analyst.
- Use a model capable of logical reasoning and data interpretation.
- **Instruction Pattern:**
    - "Act as a marketing operations analyst monitoring campaign performance."
    - "Analyze the provided data for anomalies in delivery, open, and click-through rates."
    - "Format all alerts clearly, highlighting the campaign name and the specific issue identified."

### 2) Composio Toolset Node
- Provide your API key to authorize the connection to your marketing automation platform.
- Ensure the connection scope includes read access to campaign analytics and write access for list management.

### 3) Tool Availability
- **Campaign Analytics API**: For fetching real-time performance data.
- **CRM Connector**: For updating contact status and lead scores.
- **Notification Service**: For sending alerts to Slack, Email, or internal dashboards.

---

## Related Solutions
- [../abandoned-cart-recovery-agent-by-klaviyo/README.md](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automate recovery workflows for lost sales.
- [../account-health-compliance-monitor-by-brevo/README.md](../account-health-compliance-monitor-by-brevo/README.md) - Monitor account compliance and health metrics.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Maintain clean and actionable CRM data.
