# Product Health Monitor (Uplizd) - Automated real-time product metric tracking and alerting

## Summary
The Product Health Monitor (Uplizd) is an intelligent automation workflow designed to track, analyze, and report on critical product performance metrics using PostHog data. By integrating real-time analytics with proactive alerting, this solution helps product teams maintain a single source of truth, improve pipeline velocity, and ensure data hygiene across their digital product ecosystem.

---

## Demo
![Product Health Monitor dashboard showing real-time metric tracking and automated alert triggers](image.png)
**Alt text (SEO-ready):** Product Health Monitor dashboard showing real-time metric tracking, automated alert triggers, Uplizd workflow, and PostHog integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9f70dc79-26c4-52b4-8719-02e2d0acb82c)

---

## Category
**Primary category:** Product Operations
**Secondary tags:** posthog, product analytics, data monitoring, automation, product health, metrics, composio, ai workflow.
This solution bridges the gap between raw product analytics and actionable operational insights to keep teams informed of product performance.

---

## Who is this for?
This workflow is designed for product-led teams looking to automate their monitoring and reporting cycles.

*   **Product Managers**
    *   Receive instant notifications on feature adoption drops or critical user journey bottlenecks.
*   **Data Analysts**
    *   Automate the extraction of complex PostHog queries to reduce manual reporting overhead.
*   **Growth Leads**
    *   Identify high-performing cohorts and trigger automated follow-up workflows based on usage spikes.
*   **Engineering Managers**
    *   Monitor system health and user-reported friction points to prioritize technical debt and bug fixes.

---

## Features
- **Real-time Metric Tracking**
  Continuous polling of PostHog events to ensure your product dashboards reflect the latest user behavior.
- **Intelligent Alerting**
  Customizable threshold triggers that notify stakeholders via Slack or email when product health metrics deviate from the norm.
- **Composio-Powered Integration**
  Seamlessly connects PostHog data with your existing tech stack, enabling cross-platform data synchronization.
- **Automated Trend Analysis**
  Uses the Agent node to interpret raw data patterns and provide human-readable summaries of product performance.
- **Data Hygiene & Cleanup**
  Automatically flags stale or inconsistent event data, ensuring your analytics remain accurate and reliable.

---

## Use Cases
**Proactive Performance Monitoring**
*   Trigger alerts when daily active users (DAU) drop below a predefined baseline.
*   Monitor conversion rates across specific funnels and notify the team of sudden performance degradation.

**Feature Adoption Tracking**
*   Analyze usage patterns for newly launched features to determine if adoption targets are being met.
*   Identify user segments that are not engaging with core features and trigger automated re-engagement campaigns.

**Operational Reporting**
*   Generate weekly product health summaries that aggregate key performance indicators (KPIs) from PostHog.
*   Automate the creation of Jira tickets when specific error events are detected in the product logs.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Authenticate your PostHog and notification provider (e.g., Slack/Email) via the Composio Toolset.
3. Configure the trigger frequency for your monitoring cycle.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual request to run a health check.
*   **Agent**: Processes the data, applies logic to identify anomalies, and drafts the summary.
*   **Composio Toolset**: Executes API calls to PostHog to fetch metrics and perform external actions.
*   **Chat Output**: Delivers the final report or alert to the designated communication channel.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Check the current conversion rate for the onboarding funnel and alert if it drops below 20%.`
* `Summarize the top 5 most used features from the last 7 days.`
* `Identify any anomalies in user sign-up patterns for the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain, interpreting raw event data into actionable insights.
*   Focus on identifying statistical deviations from historical averages.
*   Maintain a professional, objective tone for all generated alerts.
*   Prioritize clarity by highlighting the "why" behind every metric change.

### 2) Composio Toolset Node
Requires a valid PostHog API key and appropriate read permissions for your project. Ensure the connection scope includes `event_read` and `insight_read` capabilities.

### 3) Tool Availability
*   **PostHog Query API**: For fetching event counts and funnel data.
*   **Notification Connectors**: For sending alerts via Slack, Microsoft Teams, or Email.
*   **Data Transformation Tools**: For formatting JSON payloads into readable reports.

---

## Related Solutions
* [AB Test Optimizer by Mixpanel](../ab-test-optimizer-by-mixpanel/README.md) - Optimize experiment results using behavioral data.
* [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Track and report on team workflow efficiency.
* [Account Health Usage Monitor by Jotform](../account-health-usage-monitor-by-jotform/README.md) - Monitor customer usage metrics to prevent churn.
