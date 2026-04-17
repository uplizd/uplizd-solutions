# Growth Insights Generator (Uplizd) - Automated user behavior analysis and cohort growth intelligence

## Summary
The Growth Insights Generator is an intelligent Uplizd workflow that bridges the gap between raw Amplitude event data and actionable business strategy. By automating the extraction of user behavior patterns and cohort performance metrics, this solution empowers teams to identify growth levers, reduce churn, and optimize product adoption without manual data crunching.

---

## Demo
![Growth Insights Generator dashboard showing cohort analysis and behavioral trends](image.png)
**Alt text (SEO-ready):** Growth Insights Generator dashboard showing cohort analysis, user behavior trends, and Uplizd AI workflow integration with Amplitude.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f65a0967-4fb6-53aa-9747-0735430970b7)

---

## Category
- **Primary category:** Growth Operations
- **Secondary tags:** amplitude, product analytics, user behavior, cohort analysis, growth strategy, data insights, composio, ai workflow
- This solution transforms complex product analytics into a streamlined pipeline for data-driven growth decision-making.

---

## Who is this for?
This workflow is designed for teams looking to turn product usage data into a competitive advantage.

- **Product Managers**
    - Identify high-value user cohorts and feature adoption bottlenecks to prioritize the product roadmap.
- **Growth Marketers**
    - Pinpoint specific behavioral triggers that lead to conversion, allowing for more targeted acquisition campaigns.
- **Data Analysts**
    - Automate the repetitive extraction of behavioral insights, freeing up time for deep-dive strategic research.
- **Customer Success Leads**
    - Monitor account health through usage patterns to proactively address churn risks before they escalate.

---

## Features
- **Automated Cohort Analysis**
    - Leverages Composio to query Amplitude cohorts, identifying trends in user retention and engagement automatically.
- **Behavioral Pattern Recognition**
    - Uses advanced LLM processing to detect anomalies or spikes in user activity that signal new growth opportunities.
- **Real-time Insight Synthesis**
    - Aggregates disparate data points into a single, human-readable summary for immediate stakeholder review.
- **Cross-Platform Integration**
    - Connects seamlessly with your existing tech stack via the Composio Toolset to trigger follow-up actions based on insights.
- **Customizable Reporting Logic**
    - Allows for tailored prompt engineering to focus on specific KPIs like activation rate, feature stickiness, or churn velocity.

---

## Use Cases
**Product Roadmap Optimization**
- Analyze feature usage frequency to sunset underperforming tools and double down on high-value workflows.
- Correlate user onboarding steps with long-term retention to refine the "Aha!" moment for new signups.

**Growth & Acquisition Strategy**
- Identify the behavioral characteristics of your most profitable customer segments to optimize lookalike audience targeting.
- Detect early-stage adoption trends in new markets to adjust regional marketing spend in real-time.

**Churn Mitigation & Account Health**
- Monitor drops in key engagement events to trigger automated alerts for the Customer Success team.
- Analyze the behavior of churned vs. retained users to identify specific friction points in the user journey.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Growth Insights Generator template file provided in this repository.
3. Authenticate your Amplitude account and any secondary CRM tools via the Composio connection manager.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your specific query regarding user behavior or cohort performance.
- **Agent**: Processes the data using the configured LLM to synthesize growth insights.
- **Composio Toolset**: Executes API calls to fetch real-time metrics from Amplitude.
- **Chat Output**: Delivers the final, actionable growth report to your workspace.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Analyze the retention rate of the 'Q3 Signups' cohort compared to 'Q2 Signups'.`
- `What are the top 3 behavioral patterns of users who converted to a paid plan this week?`
- `Identify any significant drops in feature usage for the 'Dashboard' module over the last 14 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your data strategist, interpreting complex analytics into business language.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system instruction to prioritize "actionable growth levers" over raw data reporting.
- Ensure the agent has access to the current date to provide time-bound analysis.

### 2) Composio Toolset Node
- Provide your Amplitude API Key and Project ID within the Composio connection settings.
- Ensure the connection scope includes read-only access to cohort and event data for security.

### 3) Tool Availability
- **Amplitude Query Tool**: Fetches raw event counts and cohort membership data.
- **Data Summarizer**: Compresses large JSON responses into concise executive summaries.
- **Notification Connector**: Optionally routes insights to Slack or Email via Composio.

---

## Related Solutions
- [AB Test Optimizer by Mixpanel](../ab-test-optimizer-by-mixpanel/README.md) - Optimize product experiments with data-driven insights.
- [Account Intelligence Reporter by Leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed account intelligence reports.
- [Account Health Usage Monitor by Jotform](../account-health-usage-monitor-by-jotform/README.md) - Track and monitor customer account health metrics.
