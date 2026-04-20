# User Journey Event Tracker (Uplizd) - Behavioral analytics and automated user property synchronization

## Summary
The User Journey Event Tracker is an automated Uplizd workflow that monitors behavioral milestones within Amplitude and synchronizes them with your CRM or data warehouse. By transforming raw event data into actionable user properties, this solution ensures your marketing and product teams maintain a single source of truth, increasing pipeline velocity and improving data hygiene across your entire stack.

---

## Demo
![User Journey Event Tracker workflow diagram showing Amplitude event ingestion, agent processing, and CRM property updates](image.png)
**Alt text (SEO-ready):** User Journey Event Tracker workflow diagram showing Amplitude event ingestion, agent processing, and CRM property updates in Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/62bf824b-8954-5026-9e3b-ce78c68524bf)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** amplitude, crm, user journey, behavioral analytics, data sync, event tracking, composio, ai workflow
This solution bridges the gap between behavioral event data and operational systems to drive personalized user engagement.

---

## Who is this for?
This workflow is designed for teams looking to bridge the gap between product usage and customer relationship management.

- **Growth Marketer**
    - Automate personalized email triggers based on specific feature adoption milestones.
- **Product Manager**
    - Identify high-intent user segments by syncing behavioral data directly into the CRM.
- **RevOps Specialist**
    - Maintain data hygiene by ensuring user properties reflect real-time engagement status.
- **Customer Success Manager**
    - Proactively reach out to users who have hit specific usage thresholds or dropped off.

---

## Features
- **Real-time Event Ingestion**
    - Automatically capture behavioral triggers from Amplitude as they occur.
- **Intelligent Property Mapping**
    - Use AI to map complex event sequences to simple, actionable user profile attributes.
- **Composio-Powered Sync**
    - Seamlessly push updated user properties to your CRM using the Composio Toolset.
- **Automated Data Hygiene**
    - Prevent data decay by continuously reconciling event-based properties with your source of truth.
- **Customizable Logic**
    - Easily adjust the agent's decision-making criteria to match your unique user journey stages.

---

## Use Cases
**Behavioral Lead Scoring**
- Automatically increment a lead score when a user completes a key onboarding event.
- Sync "Power User" status to the CRM when a user hits a specific session frequency.

**Churn Prevention**
- Flag accounts for the success team when usage drops below a defined threshold.
- Trigger automated re-engagement workflows when a user stops performing core platform actions.

**Feature Adoption Tracking**
- Update user properties to reflect the specific features a customer has activated.
- Map trial-to-paid conversion events to update account status in real-time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the builder.
3. Authenticate your Amplitude and CRM accounts within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw event payload or trigger signal from Amplitude.
- **Agent**: Analyzes the event data and determines the appropriate property update.
- **Composio Toolset**: Executes the API calls to update user records in your CRM.
- **Chat Output**: Confirms the successful synchronization and logs the update status.

### 3) Run the Flow
Use the Playground to test your configuration with these example prompts:
- `Process the latest 'Feature Activated' event for user_id: 12345 and update their CRM status.`
- `Check if user_id: 98765 has completed the onboarding milestone and update the 'Onboarding_Complete' property to true.`
- `Sync the recent session frequency data for account_id: 555 to the CRM 'Usage_Score' field.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine that parses event data and maps it to CRM fields.
- Use a model capable of structured data extraction (e.g., GPT-4o).
- Instruction: "Extract the user_id and event type from the input, then map the event to the corresponding CRM property update."
- Instruction: "If the event is unrecognized, log a warning and skip the update to maintain data integrity."

### 2) Composio Toolset Node
- Provide your API key to enable secure connections to your CRM and Amplitude.
- Set the connection scope to allow read access for Amplitude and write access for your CRM user objects.

### 3) Tool Availability
- **Amplitude API**: For fetching detailed user event history.
- **CRM Connector**: For updating user properties and custom fields.
- **Data Transformer**: For formatting event timestamps and property values.

---

## Related Solutions
- [AB Test Optimizer by Mixpanel](../ab-test-optimizer-by-mixpanel/README.md) - Optimize your A/B testing strategy using behavioral data.
- [Account Intelligence Reporter by Leadfeeder](../account-intelligence-reporter-by-leadfeeder/README.md) - Enrich your CRM with account-level intelligence.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across platforms for a unified view.
