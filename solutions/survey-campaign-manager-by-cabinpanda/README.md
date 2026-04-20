# Survey Campaign Manager (Uplizd) - Automated multi-stage survey lifecycle and response orchestration

## Summary
The Survey Campaign Manager by CabinPanda is an intelligent Uplizd AI workflow designed to automate the end-to-end lifecycle of survey campaigns. By integrating directly with your survey platforms and CRM, it streamlines distribution, tracks completion rates, and triggers follow-up actions based on participant feedback, ensuring higher engagement and actionable data hygiene for marketing and customer success teams.

---

## Demo
![Survey Campaign Manager workflow showing automated distribution, tracking, and response analysis nodes](image.png)
**Alt text (SEO-ready):** Survey Campaign Manager Uplizd workflow automation for marketing survey distribution, response tracking, and CRM data integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a4ad52c4-d6bf-53b3-958c-b1919a66516c)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** survey, campaign management, customer feedback, marketing automation, data sync, composio, ai workflow, lead nurturing
- This solution bridges the gap between raw survey data and actionable marketing insights by automating the feedback loop.

---

## Who is this for?
This workflow is designed for teams looking to eliminate manual survey administration and improve response-driven decision-making.

- **Marketing Manager**
    - Automates large-scale survey distribution and tracks campaign performance in real-time.
- **Customer Success Lead**
    - Triggers personalized follow-up actions based on specific survey sentiment scores.
- **RevOps Specialist**
    - Ensures survey response data is synced accurately to CRM profiles for unified customer intelligence.
- **Product Researcher**
    - Accelerates the collection and synthesis of user feedback to inform product roadmap prioritization.

---

## Features
- **Automated Distribution**
    - Schedules and sends survey links across multiple channels to maximize reach and participation.
- **Real-time Response Tracking**
    - Monitors survey completion status and updates participant records automatically via the Composio Toolset.
- **Sentiment-Driven Logic**
    - Analyzes incoming feedback and categorizes responses to trigger immediate internal notifications or CRM updates.
- **CRM Integration**
    - Syncs survey metadata and participant status directly with your CRM, maintaining a single source of truth.
- **Lifecycle Management**
    - Manages the entire campaign lifecycle from initial invitation to final data aggregation and reporting.

---

## Use Cases
**Campaign Execution**
- Automatically trigger survey invitations to customers immediately following a support ticket resolution.
- Batch distribute quarterly NPS surveys to segmented contact lists based on recent product usage data.

**Data Enrichment**
- Update CRM lead fields with survey-provided preferences to enable more targeted marketing automation.
- Flag high-churn-risk accounts based on negative survey feedback for immediate account manager intervention.

**Performance Analysis**
- Generate summary reports of campaign response rates to identify the most effective distribution channels.
- Aggregate qualitative feedback into actionable insights for weekly product development meetings.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Select your workspace and import the Survey Campaign Manager flow.
3. Authenticate your survey and CRM platforms within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives campaign parameters or manual trigger commands.
- **Agent**: Processes logic, interprets survey data, and decides on follow-up actions.
- **Composio Toolset**: Executes API calls to your survey and CRM platforms to perform read/write operations.
- **Chat Output**: Returns the summary of the campaign status or confirmation of automated actions.

### 3) Run the Flow
Use the Playground to test your campaign logic with these prompts:
- `Launch the Q3 Customer Satisfaction survey to the 'Active Users' segment in HubSpot.`
- `Check the current response rate for the 'Product Feedback' campaign and notify the team if it falls below 20%.`
- `Sync all survey responses from the last 24 hours to the CRM and tag participants based on their sentiment score.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for survey logic and data mapping.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate sentiment analysis.
- Provide clear instructions on how to handle missing data or incomplete survey responses.
- Define specific triggers for CRM updates to prevent data clutter.

### 2) Composio Toolset Node
- Provide your API keys for your survey platform (e.g., Typeform, SurveyMonkey) and CRM (e.g., Salesforce, HubSpot).
- Ensure the connection scope includes read/write permissions for contacts and survey response objects.

### 3) Tool Availability
- **Survey API**: Fetching survey links, response status, and raw feedback data.
- **CRM Connector**: Updating contact properties, creating tasks, and logging survey activities.
- **Notification Service**: Sending alerts to Slack or Email when critical feedback is received.

---

## Related Solutions
- [WhatsApp Lead Qualification Agent](../whats-app-lead-qualification-agent-by-whatsapp/README.md) - Automates lead screening and qualification via messaging.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Ensures consistent data flow and hygiene across integrated platforms.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Tracks and optimizes sales opportunities through the funnel.
