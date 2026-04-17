# Customer Success Tracker (Uplizd) - Automate health monitoring and success milestones

## Summary
The Customer Success Tracker by Attio is an intelligent Uplizd workflow designed to streamline account management by monitoring customer health signals and automating key success milestones. By integrating real-time data from Attio, this solution empowers Customer Success Managers (CSMs) to proactively identify at-risk accounts, track engagement metrics, and ensure consistent follow-up, ultimately driving higher retention rates and pipeline velocity.

---

## Demo
![Customer Success Tracker workflow showing Attio integration and health monitoring logic](image.png)
**Alt text (SEO-ready):** Customer Success Tracker Uplizd workflow for Attio CRM data synchronization, health monitoring, and automated success milestone tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/5ca38d53-657b-5e8e-9f61-9000f5efbcf9)

---

## Category
**Primary category:** Customer Success
**Secondary tags:** crm, attio, customer health, retention, account management, success milestones, data sync, ai workflow.
This solution bridges the gap between raw CRM data and actionable customer success insights to maintain long-term account health.

---

## Who is this for?
This solution is designed for teams focused on maintaining high-value client relationships and reducing churn through data-driven intervention.

- **Customer Success Manager**
    - Automates the tracking of health scores and identifies accounts requiring immediate attention.
- **Account Executive**
    - Gains visibility into post-sale engagement to identify upsell and expansion opportunities.
- **RevOps Lead**
    - Standardizes the definition of "customer health" across the organization using unified CRM data.
- **Support Operations Manager**
    - Ensures that support tickets and usage patterns are reflected in the overall account health status.

---

## Features
- **Real-time Health Scoring**
    - Automatically calculates and updates account health scores based on usage data and interaction frequency.
- **Milestone Automation**
    - Triggers notifications and task creation when specific customer success milestones are reached or missed.
- **Attio CRM Integration**
    - Leverages the Composio Toolset to read and update account records directly within Attio.
- **Proactive Risk Alerts**
    - Identifies stalled accounts or declining engagement trends before they lead to churn.
- **Unified Data Sync**
    - Consolidates interaction history and usage metrics into a single source of truth for the entire success team.

---

## Use Cases
**Proactive Churn Prevention**
- Automatically flag accounts with declining login frequency over a 30-day window.
- Create high-priority tasks for CSMs when an account's health score drops below a critical threshold.

**Success Milestone Tracking**
- Track onboarding completion rates and trigger celebratory or follow-up communications.
- Update account status fields in Attio automatically once a renewal or expansion milestone is achieved.

**Account Engagement Optimization**
- Sync support ticket volume with account records to provide a holistic view of the customer experience.
- Generate weekly summaries of account activity for leadership review based on real-time CRM data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the workflow.
3. Authenticate your Attio account within the Composio Toolset node.
4. Ensure nodes are connected correctly: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers or manual queries regarding account status.
- **Agent**: Processes health data and determines the necessary action based on current account metrics.
- **Composio Toolset**: Executes read/write operations within Attio to update records or fetch engagement logs.
- **Chat Output**: Delivers the final summary or confirmation of the action taken to the user.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Check the health score for Acme Corp and list any pending success milestones.`
- `Identify all accounts with declining engagement in the last 14 days and create a follow-up task.`
- `Update the renewal status for all accounts due in the next 30 days based on current usage data.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the analytical engine for your customer data.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data interpretation.
- Provide clear instructions on how to calculate "health" based on your specific business KPIs.
- Ensure the agent is instructed to prioritize high-risk accounts in its output summaries.

### 2) Composio Toolset Node
- Provide your Attio API key within the Composio configuration.
- Ensure the connection scope includes read/write access to `Accounts`, `Tasks`, and `Custom Objects`.

### 3) Tool Availability
- **Attio Search**: Locate specific account IDs and metadata.
- **Attio Record Update**: Modify health scores and status fields.
- **Task Creation**: Generate follow-up items for the success team.
- **Data Aggregation**: Fetch interaction logs and support ticket summaries.

---

## Related Solutions
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage complex account hierarchies and relationship mapping.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on prospective and existing accounts.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track usage metrics and form-based feedback for account health.
