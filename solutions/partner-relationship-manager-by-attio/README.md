# Partner Relationship Manager (Uplizd) - Automate partner onboarding and relationship tracking

## Summary
The Partner Relationship Manager by Attio is an intelligent Uplizd workflow designed to streamline partner lifecycle management, from initial onboarding to ongoing engagement tracking. By leveraging the Composio Toolset to interface directly with your CRM, this solution ensures a single source of truth for partner data, reduces manual administrative overhead, and accelerates pipeline velocity by automating routine communication and status updates.

---

## Demo
![Partner Relationship Manager workflow screenshot showing Attio CRM integration nodes](image.png)
**Alt text (SEO-ready):** Uplizd Partner Relationship Manager workflow showing Attio CRM integration, automated partner onboarding, and relationship tracking pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7bcaeac6-8c92-5d48-8824-df453878112f)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** crm, attio, partner management, onboarding, automation, pipeline, workflow, composio
- This solution optimizes partner operations by synchronizing relationship data and automating administrative tasks within your CRM ecosystem.

---

## Who is this for?
This solution is designed for professionals managing complex partner ecosystems who need to maintain data hygiene and consistent engagement.

- **Partner Operations Manager**
    - Automates repetitive onboarding tasks to focus on strategic partner growth.
- **Sales Operations Lead**
    - Ensures partner data is consistently updated across the CRM for accurate reporting.
- **Channel Sales Representative**
    - Receives automated alerts and summaries for partner health and follow-up opportunities.
- **Business Development Manager**
    - Maintains a clear view of partner relationship status and pending action items.

---

## Features
- **Automated Onboarding**
    - Triggers standardized workflows when a new partner is added to Attio, ensuring consistent setup.
- **Real-time Data Sync**
    - Uses the Composio Toolset to push and pull partner information between Uplizd and Attio instantly.
- **Relationship Health Tracking**
    - Monitors interaction frequency and updates partner status fields based on engagement metrics.
- **Action Item Prioritization**
    - Automatically identifies and flags stalled partner relationships that require immediate human intervention.
- **Centralized Communication Log**
    - Aggregates partner interactions into a single source of truth within the CRM for team-wide visibility.

---

## Use Cases
**Partner Onboarding**
- Automatically create and assign tasks in Attio when a new partner is marked as "Signed."
- Send welcome documentation and setup instructions based on the partner's specific tier or region.

**Relationship Maintenance**
- Trigger a follow-up reminder if no interaction has been logged with a partner in the last 30 days.
- Update partner engagement scores based on recent activity volume and meeting frequency.

**Performance Reporting**
- Generate weekly summaries of partner activity and pipeline contribution for executive review.
- Sync partner performance metrics from external tools back into the CRM for unified reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in your workspace.
2. Connect your Attio account within the Composio Toolset configuration.
3. Map your preferred CRM fields to the corresponding workflow variables.
4. Ensure nodes are correctly linked from Chat Input through to the Agent and final Output.

### 2) Setup the Nodes
- **Chat Input**: Receives commands or triggers for partner updates.
- **Agent**: Processes instructions and determines the necessary CRM actions.
- **Composio Toolset**: Executes read/write operations within Attio.
- **Chat Output**: Returns the confirmation or summary of the completed action.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `List all partners currently in the 'Onboarding' stage.`
- `Update the status of Partner X to 'Active' and create a follow-up task for next week.`
- `Summarize the last 3 interactions with our top-tier partners.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your CRM interactions.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Instruct the agent to prioritize data accuracy when updating CRM records.
- Ensure the agent is configured to handle missing information by requesting clarification.

### 2) Composio Toolset Node
- Provide your valid Attio API key within the Composio integration settings.
- Define the connection scope to allow read/write access to partner and task objects.

### 3) Tool Availability
- **Attio Search**: Locate partner profiles and records.
- **Attio Update**: Modify partner status and custom fields.
- **Task Creation**: Generate follow-up items for the partner management team.
- **Data Retrieval**: Fetch interaction history and engagement logs.

---

## Related Solutions
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Manage complex account hierarchies and relationships.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into prospect accounts.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms and tools.
