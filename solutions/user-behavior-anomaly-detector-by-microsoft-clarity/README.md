# User Behavior Anomaly Detector (Uplizd) - Real-time monitoring and threat detection for user activity

## Summary
The User Behavior Anomaly Detector is an automated Uplizd workflow that monitors user interaction patterns via Microsoft Clarity to identify suspicious activity, performance bottlenecks, or unexpected navigation shifts. By leveraging AI-driven analysis, this solution provides security and product teams with actionable insights, ensuring data hygiene and proactive threat mitigation without manual log review.

---

## Demo
![User Behavior Anomaly Detector workflow showing data ingestion from Microsoft Clarity, AI analysis, and alert routing](image.png)
**Alt text (SEO-ready):** User Behavior Anomaly Detector workflow in Uplizd, featuring Microsoft Clarity integration for real-time user activity monitoring, anomaly detection, and automated alerting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0590fb9a-3684-5c09-9fc0-ce00b649c21f)

---

## Category
**Primary category:** Operations
**Secondary tags:** user behavior, microsoft clarity, anomaly detection, security, data hygiene, ai workflow, monitoring, composio
This solution bridges the gap between raw user interaction data and proactive operational intelligence.

---

## Who is this for?
This workflow is designed for teams responsible for maintaining platform integrity and optimizing user experience.

*   **Security Analyst**
    *   Detects unauthorized access patterns or bot-like behavior in real-time.
*   **Product Manager**
    *   Identifies friction points where users drop off or encounter unexpected UI errors.
*   **DevOps Engineer**
    *   Monitors for anomalous traffic spikes that may indicate performance degradation.
*   **Customer Success Lead**
    *   Proactively flags accounts experiencing technical difficulties before they report issues.

---

## Features
- **Real-time Data Ingestion**
  Connects directly to Microsoft Clarity to stream user session data into the Uplizd pipeline.
- **AI-Powered Anomaly Detection**
  Uses advanced LLM reasoning to distinguish between normal user navigation and suspicious or erratic behavior.
- **Automated Alerting**
  Triggers immediate notifications through integrated communication channels when high-risk anomalies are detected.
- **Composio Toolset Integration**
  Utilizes the Composio Toolset to execute complex queries and fetch granular session details for deeper investigation.
- **Contextual Reporting**
  Generates summarized reports that include session IDs, timestamps, and the specific nature of the detected anomaly.

---

## Use Cases
**Security & Threat Monitoring**
*   Identifying brute-force login attempts or credential stuffing patterns.
*   Flagging unusual geographical or device-based access shifts for specific user accounts.

**Product Experience Optimization**
*   Detecting "rage clicks" or dead-end navigation paths that indicate broken UI elements.
*   Analyzing session data to identify bottlenecks in complex user onboarding flows.

**Operational Data Hygiene**
*   Cleaning up noise by filtering out bot traffic from genuine user interaction logs.
*   Automating the categorization of user feedback based on session-specific performance metrics.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided JSON configuration file for the Anomaly Detector.
3. Authenticate your Microsoft Clarity and communication tool connections.
4. Ensure nodes are correctly mapped and all API keys are active in the settings panel.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger signal or manual request to scan for anomalies.
*   **Agent**: Processes session logs and applies logic to identify deviations from established user patterns.
*   **Composio Toolset**: Executes API calls to fetch detailed session metadata from Microsoft Clarity.
*   **Chat Output**: Delivers the final summary of detected anomalies and recommended actions.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
* `Analyze the last 24 hours of session data for any high-risk navigation anomalies.`
* `Check for rage clicks or UI errors in the recent user session logs.`
* `Generate a summary report of all detected anomalies from the last hour.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security and UX analyst, interpreting session data to provide actionable insights.
* Focus on identifying deviations from standard user journey benchmarks.
* Prioritize high-severity anomalies that impact platform security or usability.
* Maintain a concise, professional tone in all generated alerts and summaries.

### 2) Composio Toolset Node
Requires an active Microsoft Clarity API key. Ensure the connection scope allows for read-only access to session recordings and interaction logs.

### 3) Tool Availability
* `ClaritySessionFetcher`: Retrieves raw session interaction data.
* `AnomalyCategorizer`: Classifies findings into security, performance, or UX categories.
* `NotificationDispatcher`: Sends alerts to Slack, Email, or internal ticketing systems.

---

## Related Solutions
* [AB Test Performance Analyzer (Microsoft Clarity)](../ab-test-performance-analyzer-by-microsoft-clarity/README.md) - Analyze A/B test results using session data.
* [Account Health Usage Monitor (Jotform)](../account-health-usage-monitor-by-jotform/README.md) - Track user engagement and account health metrics.
* [Workflow Health Monitor (DailyBot)](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational health of automated business processes.
