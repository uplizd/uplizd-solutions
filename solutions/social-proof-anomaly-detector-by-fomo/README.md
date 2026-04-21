# Social Proof Anomaly Detector (Uplizd) - Real-time monitoring for conversion event irregularities

## Summary
The Social Proof Anomaly Detector is an automated Uplizd workflow that monitors social proof events—such as recent purchases or sign-ups—to identify statistical outliers and unusual activity patterns. By leveraging real-time data analysis, this solution helps marketing and growth teams maintain brand integrity, detect potential bot traffic, and ensure that displayed social proof remains authentic and trustworthy.

---

## Demo
![Social Proof Anomaly Detector workflow visualizing event stream analysis and alert triggers](image.png)
**Alt text (SEO-ready):** Social Proof Anomaly Detector workflow in Uplizd, monitoring conversion events and social proof data for anomalies using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/21e04033-4f2f-56ca-ae3f-1a068e4337cf)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** social proof, anomaly detection, conversion tracking, data hygiene, growth marketing, fomo, composio, ai workflow
- This solution bridges the gap between raw conversion data and actionable marketing insights by automating the detection of irregular social proof patterns.

---

## Who is this for?
This workflow is designed for teams managing high-traffic conversion funnels who need to ensure data accuracy and trust.

- **Growth Marketer**
    - Identifies spikes in conversion data that may indicate bot activity or tracking errors.
- **Marketing Operations Manager**
    - Maintains the integrity of social proof widgets by filtering out anomalous or fraudulent event data.
- **E-commerce Manager**
    - Ensures that displayed customer activity is genuine, protecting brand reputation and consumer trust.
- **Data Analyst**
    - Automates the monitoring of event streams to reduce manual auditing time for conversion anomalies.

---

## Features
- **Real-time Event Monitoring**
    - Continuously scans incoming social proof events for deviations from established baseline conversion rates.
- **Automated Anomaly Detection**
    - Uses AI-driven logic to distinguish between legitimate viral growth and potential system errors or bot attacks.
- **Composio-Powered Integrations**
    - Seamlessly connects with your existing marketing stack to pull event logs and push alerts to communication channels.
- **Configurable Alert Thresholds**
    - Allows users to define sensitivity levels for what constitutes an "anomaly," reducing noise and false positives.
- **Actionable Insight Reporting**
    - Generates summary reports of detected irregularities, providing context for immediate investigation.

---

## Use Cases
**Conversion Integrity**
- Flagging sudden bursts of "purchases" that originate from a single IP address or geographic region.
- Identifying gaps in event reporting that suggest a tracking pixel or integration failure.

**Bot & Fraud Prevention**
- Detecting automated script activity that artificially inflates social proof numbers on landing pages.
- Monitoring for "event flooding" that could degrade the performance of your social proof display widgets.

**Marketing Performance Auditing**
- Correlating social proof anomalies with specific marketing campaigns to identify successful vs. suspicious traffic.
- Validating that event data flowing into your CRM matches the activity displayed on your storefront.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project to initialize the workflow.
3. Authenticate the required integrations within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives parameters for the monitoring window and alert sensitivity.
- **Agent**: Analyzes the event stream against historical data to identify statistical outliers.
- **Composio Toolset**: Executes data retrieval and alert dispatching via connected marketing APIs.
- **Chat Output**: Delivers a summary of findings and specific anomaly alerts to the user.

### 3) Run the Flow
Use the Playground to test the detector with these prompts:
- `Check for anomalies in the last 24 hours of conversion events.`
- `Run a deep scan on social proof data from the 'Summer Sale' campaign.`
- `Identify any suspicious spikes in sign-ups occurring between 2 AM and 4 AM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain of the workflow.
- Set the system prompt to prioritize statistical variance analysis.
- Configure the model to output alerts in a structured JSON format for downstream processing.
- Enable "Tool Use" mode to allow the agent to query event logs dynamically.

### 2) Composio Toolset Node
- Provide your API keys for the relevant marketing or analytics platforms.
- Set the connection scope to "Read-Only" for event logs to maintain data security.

### 3) Tool Availability
- **Event Log Fetcher**: Retrieves raw conversion event data.
- **Statistical Analyzer**: Performs variance calculations on event timestamps.
- **Alert Dispatcher**: Sends notifications via Slack, Email, or Webhook when anomalies are detected.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automates follow-ups for high-intent users who leave the site.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Tracks user engagement metrics to identify at-risk accounts.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Keeps your automated processes running smoothly by monitoring for execution errors.
