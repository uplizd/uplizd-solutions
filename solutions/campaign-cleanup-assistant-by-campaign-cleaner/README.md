# Campaign Cleanup Assistant (Uplizd) - Automated marketing campaign hygiene and performance optimization

## Summary
The Campaign Cleanup Assistant is an intelligent Uplizd workflow designed to maintain marketing pipeline health by automatically identifying and archiving outdated, underperforming, or redundant email campaigns. By leveraging the Composio Toolset to interface with your marketing automation platforms, this solution ensures your workspace remains clutter-free, improving reporting accuracy and team focus.

---

## Demo
![Campaign Cleanup Assistant workflow interface showing automated campaign filtering and archival logic](../image.png)
**Alt text (SEO-ready):** Campaign Cleanup Assistant Uplizd workflow for automated marketing campaign hygiene, data synchronization, and performance optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d0e88924-d7da-58e5-ad68-7c9d3a8babf5)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** marketing, automation, data hygiene, campaign management, email marketing, workflow, composio, pipeline optimization
- This solution streamlines marketing operations by enforcing data hygiene standards across your campaign management platforms.

---

## Who is this for?
This solution is designed for marketing teams looking to reduce manual overhead and maintain high-quality data standards.

- **Marketing Operations Manager**
    - Automates the removal of stale campaign assets to ensure reporting reflects only active initiatives.
- **Email Marketing Specialist**
    - Frees up time spent manually auditing campaign folders by automating the identification of low-engagement assets.
- **Growth Marketer**
    - Maintains a clean, organized campaign environment that allows for faster A/B testing and iteration.
- **Data Analyst**
    - Ensures the integrity of marketing performance data by preventing outdated campaigns from skewing historical metrics.

---

## Features
- **Automated Audit Cycles**
    - Schedules recurring scans of your marketing platform to flag campaigns that meet specific inactivity criteria.
- **Intelligent Performance Filtering**
    - Uses AI to analyze engagement metrics and identify campaigns that fall below your defined success thresholds.
- **Safe Archival Logic**
    - Moves identified campaigns to an archive state via the Composio Toolset, ensuring data is preserved but removed from active views.
- **Real-time Notification Alerts**
    - Sends summary reports to your team via Slack or email whenever a cleanup cycle is completed.
- **Customizable Cleanup Rules**
    - Allows you to define specific time windows and performance KPIs that trigger the cleanup process.

---

## Use Cases
**Marketing Asset Hygiene**
- Automatically archive email campaigns that have been inactive for more than 90 days.
- Identify and flag duplicate campaign drafts that clutter the marketing dashboard.

**Performance-Based Optimization**
- Flag campaigns with an open rate below 5% for manual review or automated archival.
- Remove test campaigns that were created during development phases but never launched.

**Reporting Accuracy**
- Clean up expired seasonal promotions to ensure current monthly performance reports are accurate.
- Standardize campaign naming conventions by identifying and archiving assets that don't match the current taxonomy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Campaign Cleanup Assistant template from the solution library.
3. Connect your marketing platform credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or schedule signal to initiate the cleanup.
- **Agent**: Processes the logic to evaluate campaign performance against your defined criteria.
- **Composio Toolset**: Executes the API calls to fetch, filter, and archive campaigns in your CRM or marketing tool.
- **Chat Output**: Returns a summary report detailing which campaigns were archived or flagged.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Find and archive all email campaigns created over 6 months ago with zero sends.`
- `List all campaigns with an open rate below 2% for my review.`
- `Run the cleanup process for the 'Q3-Promotions' folder and notify the team on Slack.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making engine for your marketing hygiene.
- Use a model capable of structured data reasoning (e.g., GPT-4o or Claude 3.5).
- Instruct the agent to prioritize safety by flagging high-value campaigns for manual approval.
- Maintain a strict mapping between performance metrics and archival actions.

### 2) Composio Toolset Node
- Provide your API key for the target marketing platform (e.g., HubSpot, Mailchimp).
- Ensure the connection scope includes `read` and `write` permissions for campaign objects.

### 3) Tool Availability
- **Campaign Fetcher**: Retrieves campaign lists, metadata, and performance statistics.
- **Status Updater**: Performs the archival or status change operations.
- **Notification Service**: Sends alerts to communication channels upon completion.

---

## Related Solutions
- [../abandoned-cart-recovery-agent-by-klaviyo/README.md](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Recover lost revenue through automated abandoned cart workflows.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Maintain clean CRM records by identifying and merging duplicate entries.
- [../ab-test-optimizer-by-mixpanel/README.md](../ab-test-optimizer-by-mixpanel/README.md) - Optimize marketing experiments based on real-time performance data.
