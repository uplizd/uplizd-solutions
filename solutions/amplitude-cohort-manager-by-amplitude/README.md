# Amplitude Cohort Manager (Uplizd) - Automated user cohort creation and behavioral analysis

## Summary
The Amplitude Cohort Manager is an intelligent Uplizd workflow designed to automate the creation, synchronization, and management of user cohorts within Amplitude. By leveraging the Composio Toolset, this solution enables product managers and data analysts to maintain precise audience segments, ensuring that marketing campaigns and product experiments are always targeted at the right user base without manual data entry.

---

## Demo
![Amplitude Cohort Manager workflow showing user segment ingestion and Amplitude API synchronization](image.png)
**Alt text (SEO-ready):** Amplitude Cohort Manager workflow in Uplizd for automated user segmentation, behavioral cohort syncing, and product analytics optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/0f22a35b-5d1a-5651-af2d-9013a2e9785d)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** amplitude, cohort management, user segmentation, product analytics, data sync, behavioral analysis, composio, ai workflow
- This solution bridges the gap between raw user behavioral data and actionable product segments through automated API orchestration.

---

## Who is this for?
This workflow is designed for teams looking to eliminate manual data management in their analytics stack.

- **Product Managers**
    - Rapidly iterate on user segments to test new feature adoption and retention strategies.
- **Data Analysts**
    - Automate the maintenance of complex behavioral cohorts, reducing time spent on repetitive data entry.
- **Growth Marketers**
    - Ensure that personalized messaging campaigns are triggered based on the most current and accurate user cohorts.
- **RevOps Specialists**
    - Maintain a single source of truth for user data across the analytics pipeline to improve reporting hygiene.

---

## Features
- **Automated Cohort Sync**
    - Synchronize user segments between your data warehouse and Amplitude in real-time using the Composio Toolset.
- **Behavioral Triggering**
    - Automatically update cohorts based on specific user actions or inactivity thresholds defined in your logic.
- **Dynamic Segment Updates**
    - Adjust cohort membership criteria dynamically as user behavior evolves, ensuring high-relevance targeting.
- **Error Handling & Logging**
    - Monitor synchronization status with built-in logging to ensure data integrity across your analytics platforms.
- **Seamless API Integration**
    - Connect directly to Amplitude’s API to push and pull cohort data without writing custom middleware.

---

## Use Cases
**Lifecycle Marketing**
- Automatically move users into "At-Risk" cohorts based on a 30-day inactivity window.
- Sync "High-Value" user segments to ad platforms for lookalike audience targeting.

**Product Experimentation**
- Create cohorts of users who have completed specific onboarding steps to measure feature adoption.
- Segment users by their interaction frequency with new UI elements to gather targeted feedback.

**Data Hygiene & Maintenance**
- Periodically clean up stale cohorts that no longer meet active engagement criteria.
- Standardize naming conventions for cohorts across different product environments and workspaces.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd solution library and select the Amplitude Cohort Manager.
2. Click "Import" to load the workflow into your workspace.
3. Configure your environment variables, including your Amplitude API keys.
4. Ensure nodes are correctly connected in the builder (Chat Input → Agent → Composio Toolset → Chat Output).

### 2) Setup the Nodes
- **Chat Input**: Receives natural language requests for cohort creation or updates.
- **Agent**: Interprets user intent and maps it to specific Amplitude API calls.
- **Composio Toolset**: Executes the authenticated requests to the Amplitude platform.
- **Chat Output**: Returns the confirmation of the cohort update or a summary of the current segment status.

### 3) Run the Flow
Use the Playground to test your cohort management logic:
- `Create a new cohort for users who signed up in the last 7 days and have not completed onboarding.`
- `List all active cohorts and identify which ones have not been updated in the last month.`
- `Move users who have reached the 'Power User' milestone into the 'VIP Retention' cohort.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your analytics data.
- Use a model capable of structured JSON output for reliable API parameter mapping.
- **Recommended instruction pattern:**
    - "You are an expert Amplitude data analyst assistant."
    - "Always verify the cohort ID before performing update or delete operations."
    - "If a requested segment is ambiguous, ask the user for clarification on the behavioral criteria."

### 2) Composio Toolset Node
- Provide your Amplitude API Key and Secret in the Composio configuration.
- Set the connection scope to include `cohort:write` and `cohort:read` permissions.

### 3) Tool Availability
- **Cohort Management**: Create, update, and delete user segments.
- **User Lookup**: Query user properties to validate cohort inclusion.
- **Analytics Reporting**: Fetch current cohort size and engagement metrics.

---

## Related Solutions
- [../ab-test-optimizer-by-mixpanel/README.md](../ab-test-optimizer-by-mixpanel/README.md) - Optimize A/B test workflows and user segmentation.
- [../account-intelligence-reporter-by-leadfeeder/README.md](../account-intelligence-reporter-by-leadfeeder/README.md) - Generate detailed account intelligence reports.
- [../workflow-health-monitor-by-dailybot/README.md](../workflow-health-monitor-by-dailybot/README.md) - Monitor the health and efficiency of your automated workflows.
