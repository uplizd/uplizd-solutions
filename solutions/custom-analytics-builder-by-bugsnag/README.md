# Custom Analytics Builder (Uplizd) - Tailored error tracking and stakeholder reporting

## Summary
The Custom Analytics Builder is an intelligent Uplizd workflow designed to automate the generation of tailored error tracking views and performance metrics. By leveraging the Bugsnag API via the Composio Toolset, this solution enables engineering leads and product managers to extract, filter, and visualize critical application health data, ensuring that technical debt and stability issues are prioritized based on stakeholder-specific requirements.

---

## Demo
![Custom Analytics Builder workflow dashboard showing Bugsnag data integration and automated reporting nodes](image.png)
**Alt text (SEO-ready):** Custom Analytics Builder (Uplizd) workflow for automated Bugsnag error tracking, data integration, and stakeholder analytics reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/767517dd-1fa7-5eb9-821f-c12bcda43dfa)

---

## Category
- **Primary category:** Data Analytics
- **Secondary tags:** bugsnag, error tracking, data integration, analytics, engineering operations, reporting, composio, ai workflow
- This solution bridges the gap between raw technical error logs and actionable business intelligence through automated data synthesis.

---

## Who is this for?
This solution is designed for technical teams looking to streamline their observability and reporting processes.

- **Engineering Managers**
    - Gain high-level visibility into application stability trends without manual dashboard configuration.
- **Product Managers**
    - Receive automated, context-aware reports on feature-specific bug rates to inform sprint prioritization.
- **DevOps Engineers**
    - Automate the extraction of error metadata to feed into incident response and post-mortem workflows.
- **QA Leads**
    - Identify regression patterns early by generating custom analytics views for new release cycles.

---

## Features
- **Automated Data Extraction**
    - Seamlessly pulls real-time error data from Bugsnag using the Composio Toolset to ensure reports are always current.
- **Stakeholder-Specific Filtering**
    - Applies intelligent logic to segment error reports by environment, severity, or specific application modules.
- **Custom Metric Synthesis**
    - Transforms raw error counts into meaningful KPIs, such as "Error-Free Session Rate" or "Mean Time to Acknowledge."
- **Scheduled Reporting Integration**
    - Triggers automated summaries that can be pushed to communication channels or project management tools.
- **Intelligent Trend Analysis**
    - Uses the Agent node to identify anomalous spikes in error frequency, providing proactive alerts before users report issues.

---

## Use Cases
**Engineering Performance Monitoring**
- Aggregate daily error counts by service to track stability against SLOs.
- Identify top-impacting bugs across production environments for rapid triage.

**Product Stability Reporting**
- Generate weekly summaries of error impact on specific user workflows or features.
- Correlate deployment timestamps with error spikes to identify unstable releases.

**Operational Data Hygiene**
- Automatically archive or categorize resolved errors to keep the analytics dashboard clean.
- Map Bugsnag error metadata to internal project tracking IDs for better cross-team visibility.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd dashboard and select "Create New Flow."
2. Import the Custom Analytics Builder template from the solution library.
3. Authenticate your Bugsnag account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the specific query or reporting parameters from the user.
- **Agent**: Processes the request, interprets the data requirements, and orchestrates the tool calls.
- **Composio Toolset**: Executes secure API requests to Bugsnag to fetch and filter the requested error data.
- **Chat Output**: Formats the retrieved data into a clear, readable report for the end user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Generate a report of the top 5 most frequent errors in the production environment from the last 24 hours.`
- `Compare error rates between the current release and the previous release for the checkout service.`
- `Create a summary of all critical unhandled exceptions that occurred during the weekend.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, translating natural language requests into structured API queries.
- Set the system prompt to prioritize technical accuracy and concise reporting.
- Enable "Tool Use" mode to allow the agent to dynamically select Bugsnag endpoints.
- Configure the response format to output structured markdown tables for better readability.

### 2) Composio Toolset Node
- Provide your Bugsnag API Key and Organization ID to establish the connection.
- Define the scope to include read-only access to error groups, events, and project metrics.

### 3) Tool Availability
- **Bugsnag List Errors**: Retrieve filtered lists of application errors.
- **Bugsnag Get Event Details**: Fetch specific stack traces and metadata for deep-dive analysis.
- **Bugsnag Project Metrics**: Query high-level stability scores and error trends.

---

## Related Solutions
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Automate business intelligence gathering and reporting.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and report on the operational health of your automated pipelines.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitor and analyze user engagement and account health metrics.
