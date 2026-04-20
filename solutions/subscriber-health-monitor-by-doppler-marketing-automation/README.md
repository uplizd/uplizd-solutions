# Subscriber Health Monitor (Uplizd) - Automated email list hygiene and engagement optimization

## Summary
The Subscriber Health Monitor (Uplizd) is an automated AI workflow designed to maintain high email deliverability and list quality. By leveraging the Composio Toolset to interface with marketing platforms, the agent identifies inactive subscribers, flags bounce-prone addresses, and triggers re-engagement campaigns. This solution provides a single source of truth for list health, ensuring marketing operations teams can maintain pipeline velocity and sender reputation without manual data scrubbing.

---

## Demo
![Subscriber Health Monitor dashboard showing automated list cleanup and engagement metrics](image.png)
**Alt text (SEO-ready):** Subscriber Health Monitor dashboard showing automated list cleanup, email engagement metrics, and Uplizd workflow automation for marketing operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/250bfe6d-e6ac-59e0-a38c-b551115cb24e)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, list hygiene, subscriber retention, data sync, marketing automation, composio, ai workflow, crm
- This solution bridges the gap between raw subscriber data and actionable marketing intelligence to prevent list decay.

---

## Who is this for?
This solution is built for teams focused on maintaining high-performing email channels and maximizing campaign ROI.

- **Email Marketing Manager**
    - Automates the identification of cold leads to improve overall open rates and sender reputation.
- **RevOps Specialist**
    - Ensures consistent data hygiene across marketing platforms and CRM systems through automated syncs.
- **Growth Marketer**
    - Triggers personalized re-engagement sequences based on real-time subscriber activity signals.
- **Deliverability Analyst**
    - Monitors bounce rates and unsubscribes to proactively mitigate domain blacklisting risks.

---

## Features
- **Automated List Auditing**
    - Periodically scans subscriber lists for inactivity thresholds and bounce patterns using integrated marketing tools.
- **Intelligent Segmentation**
    - Dynamically categorizes subscribers into "Active," "At-Risk," and "Churned" segments for targeted communication.
- **Real-time Hygiene Sync**
    - Automatically updates CRM and ESP records when invalid or suppressed email addresses are detected.
- **Engagement Triggering**
    - Seamlessly connects with email service providers to initiate re-engagement workflows for at-risk segments.
- **Performance Reporting**
    - Generates summary reports on list health trends, providing visibility into the impact of automated cleanup efforts.

---

## Use Cases
**List Hygiene & Compliance**
- Automatically suppress hard-bounce email addresses to maintain domain sender reputation.
- Identify and remove duplicate or malformed contact entries across multiple marketing platforms.

**Subscriber Retention**
- Trigger automated "We miss you" email sequences for subscribers who have been inactive for over 90 days.
- Analyze engagement trends to adjust content frequency for high-value subscriber segments.

**Cross-Platform Data Sync**
- Synchronize subscriber status updates between your CRM and email marketing tools in real-time.
- Consolidate engagement data from disparate sources into a unified health score for every contact.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Subscriber Health Monitor template from the solution library.
3. Authenticate your required marketing and CRM integrations via the Composio Toolset.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all API connections are active.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled cron inputs to initiate the health scan.
- **Agent**: Processes subscriber data, evaluates engagement scores, and determines the necessary cleanup actions.
- **Composio Toolset**: Executes API calls to fetch subscriber lists and perform bulk updates in your marketing platform.
- **Chat Output**: Returns a summary report of the cleanup operation and a list of actions taken.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Run a full audit on the main newsletter list and generate a report of all inactive subscribers.`
- `Identify all subscribers with a bounce rate above 5% and move them to the suppression list.`
- `Trigger a re-engagement campaign for the 'At-Risk' segment identified in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for list analysis and decision-making.
- **Instruction Pattern:**
    - Analyze incoming subscriber data against defined engagement thresholds.
    - Prioritize actions based on list health impact (e.g., suppression before re-engagement).
    - Maintain a neutral, data-driven tone when reporting audit results.

### 2) Composio Toolset Node
- **API Key:** Provide your marketing platform's API key (e.g., HubSpot, Mailchimp, or Brevo).
- **Connection Scope:** Ensure the agent has read/write access to contact lists, suppression lists, and email campaign analytics.

### 3) Tool Availability
- **List Retrieval Tools**: Fetch subscriber status and engagement history.
- **Data Modification Tools**: Update contact properties and manage suppression status.
- **Campaign Trigger Tools**: Initiate automated email sequences or workflow triggers.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automates recovery sequences for lost sales.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Cleans and standardizes CRM contact data.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks customer usage to identify churn risks.
