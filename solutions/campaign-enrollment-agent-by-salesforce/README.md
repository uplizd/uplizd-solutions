# Campaign Enrollment Agent (Uplizd) - Automate lead nurturing and campaign synchronization

## Summary
The Campaign Enrollment Agent is an intelligent automation workflow designed to streamline the process of adding contacts and leads to targeted marketing campaigns. By leveraging the Composio Toolset to interface directly with Salesforce, this solution eliminates manual data entry, ensures consistent lead nurturing, and improves pipeline velocity by triggering enrollment based on real-time CRM signals.

---

## Demo
![Campaign Enrollment Agent workflow diagram showing CRM integration and automated lead routing](image.png)
**Alt text (SEO-ready):** Campaign Enrollment Agent workflow diagram showing Salesforce CRM integration, automated lead routing, and Uplizd AI pipeline management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/2d11f2d0-0c3a-5643-9aa7-f552a0bcf565)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** salesforce, crm, lead nurturing, campaign management, workflow automation, composio, pipeline, ai agent
- This solution bridges the gap between CRM data and marketing execution, ensuring every lead is enrolled in the right campaign at the right time.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to scale their outreach without increasing manual overhead.

- **Sales Development Rep (SDR)**
    - Automatically enrolls qualified leads into nurture sequences immediately after discovery calls.
- **Marketing Operations Manager**
    - Ensures campaign list hygiene by automating the addition of new contacts from CRM triggers.
- **Account Executive (AE)**
    - Maintains momentum on stalled opportunities by triggering re-engagement campaigns directly from the CRM.
- **Revenue Operations (RevOps) Lead**
    - Standardizes the enrollment process across the organization to ensure consistent lead handling and attribution.

---

## Features
- **Automated CRM Sync**
    - Seamlessly pushes contact status updates to Salesforce, ensuring your marketing campaigns reflect the latest CRM data.
- **Intelligent Lead Routing**
    - Uses AI to evaluate lead attributes and automatically map them to the most relevant campaign based on industry, role, or intent.
- **Real-time Triggering**
    - Executes enrollment actions instantly when specific criteria are met, reducing the latency between lead capture and outreach.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely execute complex API calls to Salesforce without writing custom middleware.
- **Error Handling & Logging**
    - Provides visibility into enrollment success rates, flagging failed syncs for manual review to maintain data integrity.

---

## Use Cases
**Lead Nurturing**
- Automatically enroll new inbound leads into a "Welcome" drip campaign based on their lead source.
- Add prospects who have attended a webinar to a specific follow-up sequence in Salesforce.

**Pipeline Acceleration**
- Enroll stalled opportunities into a specialized "Re-engagement" campaign to revive interest.
- Trigger enrollment for leads that have reached a specific "Marketing Qualified" score.

**Data Hygiene & Segmentation**
- Move contacts between campaigns based on their engagement level or recent activity in the CRM.
- Sync contact preferences across platforms to ensure compliance and accurate campaign targeting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project destination.
3. Configure your Salesforce credentials within the Composio connection settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger signal or manual request to enroll a specific contact.
- **Agent**: Analyzes the request and determines the correct campaign ID and contact parameters.
- **Composio Toolset**: Executes the API calls to Salesforce to perform the enrollment action.
- **Chat Output**: Confirms the successful enrollment or reports any errors back to the user.

### 3) Run the Flow
Use the Uplizd Playground to test your automation with prompts like:
- `Enroll contact john.doe@example.com into the Q4 Enterprise Nurture campaign.`
- `Add all leads from the 'Tech Conference 2023' list to the follow-up sequence.`
- `Check the status of lead ID 003xx000004 and enroll them in the current outreach campaign.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for CRM interactions.
- Use a model capable of structured output (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a CRM automation assistant. Extract contact IDs and campaign names from the input and use the Composio tools to perform the enrollment."
- Ensure the agent has access to the full Salesforce schema for accurate field mapping.

### 2) Composio Toolset Node
- Provide your Salesforce API key or OAuth token via the Composio dashboard.
- Set the connection scope to include `read` and `write` permissions for Leads, Contacts, and Campaigns.

### 3) Tool Availability
- `salesforce_add_contact_to_campaign`: Adds a specific contact to a campaign.
- `salesforce_search_campaign`: Retrieves campaign IDs based on name or status.
- `salesforce_get_lead_details`: Fetches current lead status for validation.

---

## Related Solutions
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates the creation and configuration of new accounts in Salesforce.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes data across multiple platforms to maintain a single source of truth.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Manages pipeline stages and automates follow-ups for stalled deals.
