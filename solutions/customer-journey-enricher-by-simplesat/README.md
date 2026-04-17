# Customer Journey Enricher (Uplizd) - Unified feedback and satisfaction data enrichment

## Summary
The Customer Journey Enricher by Simplesat is an automated Uplizd workflow that synthesizes customer feedback history and satisfaction trends into a single source of truth. By integrating real-time sentiment data into your CRM, this solution eliminates manual data entry, improves pipeline hygiene, and empowers teams to deliver proactive, data-driven customer experiences.

---

## Demo
![Customer Journey Enricher workflow dashboard showing feedback sentiment analysis and CRM data sync](image.png)
**Alt text (SEO-ready):** Customer Journey Enricher (Uplizd) workflow dashboard showing feedback sentiment analysis, Simplesat integration, and CRM data sync for improved customer insights.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b61eb478-9d0c-5e3b-8eaa-c5952d8ed829)

---

## Category
- **Primary category:** Customer Support
- **Secondary tags:** crm, simplesat, feedback, sentiment analysis, customer journey, data enrichment, support automation, composio
- This solution bridges the gap between raw customer feedback and actionable CRM data to optimize the end-to-end customer journey.

---

## Who is this for?
This solution is designed for teams looking to turn qualitative feedback into quantitative business intelligence.

- **Customer Success Managers**
    - Proactively identify at-risk accounts based on declining satisfaction trends.
- **Support Leads**
    - Automate the aggregation of feedback metrics to streamline performance reporting.
- **RevOps Professionals**
    - Maintain high-quality CRM data hygiene by syncing external feedback signals automatically.
- **Account Executives**
    - Gain immediate visibility into client sentiment before entering high-stakes renewal meetings.

---

## Features
- **Automated Feedback Sync**
    - Seamlessly pulls feedback data from Simplesat and maps it directly to relevant customer profiles in your CRM.
- **Sentiment Scoring Engine**
    - Uses the Agent node to analyze qualitative comments and assign a standardized sentiment score for easier tracking.
- **Real-time Alerting**
    - Triggers notifications in your communication channels when negative feedback thresholds are crossed.
- **Composio-Powered Integrations**
    - Leverages the Composio Toolset to securely connect with your CRM and support platforms without custom middleware.
- **Historical Trend Mapping**
    - Aggregates feedback over time to provide a longitudinal view of the customer relationship health.

---

## Use Cases
**Proactive Churn Prevention**
- Automatically flag accounts with a downward trend in NPS scores for immediate CS intervention.
- Sync negative feedback comments to the CRM "Notes" field so AEs have full context before outreach.

**Support Performance Optimization**
- Correlate individual support agent performance with customer satisfaction ratings to identify training needs.
- Generate weekly summaries of top-cited customer pain points to inform product roadmap prioritization.

**Data-Driven Account Management**
- Update CRM "Health Score" fields based on the latest feedback received via Simplesat.
- Trigger automated follow-up tasks for account managers when a customer provides a low-score survey response.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your Simplesat and CRM accounts within the integration settings.
3. Configure the trigger interval to match your desired sync frequency.
4. Ensure nodes are correctly mapped to your specific CRM custom fields and API endpoints.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger event or manual request to initiate the enrichment process.
- **Agent**: Processes feedback data, performs sentiment analysis, and determines the appropriate CRM update.
- **Composio Toolset**: Executes the API calls to fetch feedback and push updates to your CRM.
- **Chat Output**: Confirms successful data sync and logs any errors encountered during the process.

### 3) Run the Flow
Use the Playground to test the workflow with these example prompts:
- `Sync all feedback from the last 24 hours to the CRM.`
- `Analyze the sentiment of the latest feedback for account ID 12345.`
- `Generate a summary of recent negative feedback and update the account health status.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical brain, interpreting feedback and deciding on the necessary CRM actions.
- Use a high-reasoning model (e.g., GPT-4o) for accurate sentiment classification.
- Instruction: "Extract the sentiment score and key themes from the customer feedback."
- Instruction: "Map the feedback to the corresponding CRM account using the provided identifier."

### 2) Composio Toolset Node
- Provide your API key within the Composio configuration panel.
- Ensure the connection scope includes read access for Simplesat and write access for your CRM (e.g., Salesforce, HubSpot).

### 3) Tool Availability
- **Simplesat API**: Fetching survey responses and customer metadata.
- **CRM Connector**: Updating account fields, adding notes, and modifying health scores.
- **Notification Service**: Sending alerts to Slack or email when critical feedback is received.

---

## Related Solutions
- [247-customer-support-assistant-by-ai-ml-api](../247-customer-support-assistant-by-ai-ml-api/README.md): AI-driven support ticket management and resolution.
- [crm-data-sync-agent](../crm-data-sync-agent/README.md): Multi-platform CRM data synchronization and conflict resolution.
- [account-health-usage-monitor-by-jotform](../account-health-usage-monitor-by-jotform/README.md): Monitoring account health through usage and form data.
