# Release Performance Monitor (Uplizd) - Automated release tracking and error correlation

## Summary
The Release Performance Monitor (Uplizd) is an intelligent automation workflow designed to bridge the gap between deployment cycles and production stability. By integrating directly with Sentry, this solution automatically correlates new software releases with error spikes, providing engineering teams with a single source of truth for release health. It reduces mean time to detection (MTTD) by surfacing critical regressions immediately after deployment, ensuring pipeline velocity remains high without compromising system reliability.

---

## Demo
![Release Performance Monitor dashboard showing error correlation metrics and deployment impact analysis](image.png)
**Alt text (SEO-ready):** Release Performance Monitor dashboard showing error correlation metrics, Sentry integration, and deployment impact analysis for Uplizd AI workflows.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4803b4ae-cdf4-51e7-b9bc-48d3831aa421)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** sentry, release management, error tracking, devops, incident response, observability, composio, ai workflow
- This solution streamlines the feedback loop between deployment and production monitoring, enabling proactive release management.

---

## Who is this for?
This workflow is designed for engineering and operations teams focused on maintaining high-availability systems.

- **DevOps Engineer**
    - Automates the correlation of deployment events with error logs to identify root causes faster.
- **Software Engineering Manager**
    - Gains visibility into release stability to make data-driven decisions on deployment frequency.
- **Site Reliability Engineer (SRE)**
    - Reduces alert fatigue by filtering noise and focusing on errors tied to specific release versions.
- **Full-Stack Developer**
    - Receives immediate feedback on code performance, allowing for rapid hotfixes post-deployment.

---

## Features
- **Automated Release Correlation**
    - Automatically maps incoming Sentry error events to the most recent release tags in your environment.
- **Real-Time Error Triage**
    - Uses the Composio Toolset to query Sentry data and prioritize issues based on impact and frequency.
- **Deployment Impact Analysis**
    - Generates concise summaries comparing pre-release and post-release error rates to validate stability.
- **Proactive Notification System**
    - Triggers alerts via the Chat Output node when a release exceeds predefined error thresholds.
- **Seamless Sentry Integration**
    - Leverages the Composio Sentry connector to pull live diagnostic data without manual API configuration.

---

## Use Cases
**Post-Deployment Health Checks**
- Automatically verify that a new release hasn't introduced critical regressions in core services.
- Compare error counts 30 minutes before and after a deployment window to ensure stability.

**Incident Response Automation**
- Quickly identify which recent code change triggered a spike in production exceptions.
- Aggregate error logs from Sentry to provide context-rich reports to on-call engineers.

**Release Quality Reporting**
- Generate weekly summaries of release performance to identify recurring stability patterns.
- Track the "Time to Fix" for errors introduced in specific release versions to improve development processes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Release Performance Monitor template from the solution library.
3. Connect your Sentry account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the release version or monitoring interval from the user.
- **Agent**: Analyzes the input and determines which Sentry metrics to retrieve.
- **Composio Toolset**: Executes API calls to fetch release-specific error data from Sentry.
- **Chat Output**: Delivers a human-readable summary of the release performance and error status.

### 3) Run the Flow
Use the Playground to test your monitor with these prompts:
- `Check the error impact for release v2.4.1 in the production project.`
- `Compare error rates for the last two deployments in the web-frontend project.`
- `Are there any new critical issues introduced since the last deployment?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as an observability analyst that interprets raw error data into actionable insights.
- Focus on identifying correlations between deployment timestamps and error spikes.
- Maintain a professional, concise tone when reporting stability metrics.
- Prioritize critical and high-severity errors in the final summary.

### 2) Composio Toolset Node
- Requires a valid Sentry API key with read-access to your organization's projects.
- Ensure the connection scope includes `project:read` and `event:read` permissions.

### 3) Tool Availability
- **Sentry Fetcher**: Retrieves error counts, event logs, and release metadata.
- **Metric Aggregator**: Calculates percentage changes in error frequency.
- **Alert Dispatcher**: Formats data for notification channels.

---

## Related Solutions
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Monitor overall workflow health and operational bottlenecks.
- [../account-audit-agent-by-cloudflare/README.md](../account-audit-agent-by-cloudflare/README.md) - Perform security and configuration audits on your infrastructure.
- [../action-item-prioritizer-by-rootly/README.md](../action-item-prioritizer-by-rootly/README.md) - Prioritize incident action items and follow-ups effectively.
