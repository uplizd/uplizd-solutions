# Lead Qualification Agent (Uplizd) - Automated lead scoring and routing for ActiveCampaign

## Summary
The Lead Qualification Agent by ActiveCampaign streamlines your sales pipeline by automatically evaluating incoming leads against your ideal customer profile. By leveraging real-time engagement data and profile attributes, this Uplizd workflow ensures that high-intent prospects are prioritized for immediate outreach, significantly increasing conversion rates and reducing manual data entry for your sales team.

---

## Demo
![Lead Qualification Agent workflow showing ActiveCampaign integration and automated routing logic](image.png)
**Alt text (SEO-ready):** Lead Qualification Agent workflow in Uplizd, demonstrating automated lead scoring, ActiveCampaign integration, and CRM routing for sales pipeline optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/836cde42-35e2-53d4-9fe1-effcfb5bb1a8)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** activecampaign, lead qualification, crm, sales pipeline, lead scoring, automation, composio, ai workflow
- This solution bridges the gap between marketing engagement and sales action by automating the qualification process within your CRM ecosystem.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to eliminate manual lead triage and focus on high-value opportunities.

- **Sales Development Representative (SDR)**
    - Receives only pre-qualified leads, allowing for faster response times and higher discovery call booking rates.
- **Marketing Operations Manager**
    - Ensures that marketing-generated leads are accurately scored and routed, maintaining data hygiene and pipeline velocity.
- **Account Executive (AE)**
    - Gains immediate visibility into lead intent signals, enabling personalized outreach that resonates with the prospect's current journey.
- **Revenue Operations (RevOps) Lead**
    - Standardizes the qualification criteria across the organization to ensure consistent lead handling and improved forecast accuracy.

---

## Features
- **Automated Lead Scoring**
    - Dynamically assigns scores to leads based on engagement metrics and profile fit, ensuring your team focuses on the most promising prospects.
- **Real-time CRM Routing**
    - Instantly updates lead status and assigns owners in ActiveCampaign as soon as qualification thresholds are met.
- **Intelligent Data Enrichment**
    - Uses the Composio Toolset to fetch and append missing contact information, providing a complete view of the lead before outreach.
- **Customizable Qualification Logic**
    - Easily adjust thresholds and criteria within the Agent node to align with your specific product-market fit and sales strategy.
- **Seamless Integration Workflow**
    - Connects directly with ActiveCampaign via the Composio Toolset to ensure all changes are reflected in real-time across your sales stack.

---

## Use Cases
**Lead Prioritization**
- Automatically flag leads that have visited your pricing page multiple times for immediate SDR follow-up.
- Filter out low-intent signups to prevent sales teams from wasting time on unqualified traffic.

**Pipeline Velocity**
- Trigger automated email sequences in ActiveCampaign based on the qualification status assigned by the agent.
- Reduce the time-to-first-contact by routing qualified leads to the appropriate account owner within minutes of submission.

**Data Hygiene & Enrichment**
- Automatically verify contact information and update lead fields in ActiveCampaign to ensure accurate reporting.
- Segment leads into specific nurture campaigns based on their qualification score and industry attributes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Configure your ActiveCampaign API credentials in the integration settings.
4. Ensure nodes are correctly connected from Chat Input to Agent, then to the Composio Toolset, and finally to Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the lead data or trigger event.
- **Agent**: Processes the lead against your defined qualification criteria.
- **Composio Toolset**: Executes the API calls to read/write lead data in ActiveCampaign.
- **Chat Output**: Returns the qualification result and action taken to the dashboard.

### 3) Run the Flow
Use the Playground to test your qualification logic:
- `Qualify the latest leads from the 'Webinar' list in ActiveCampaign.`
- `Score the lead with email user@example.com and update their status to 'Qualified'.`
- `Find all leads in ActiveCampaign with a score above 80 and assign them to the Sales team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your automated sales assistant, interpreting lead data and applying business rules.
- Analyze lead engagement patterns against the provided ideal customer profile.
- Execute conditional logic to determine if a lead meets the "Qualified" threshold.
- Format output clearly to confirm the action taken in the CRM.

### 2) Composio Toolset Node
- **API Key**: Ensure your ActiveCampaign API key is active within the Composio dashboard.
- **Connection Scope**: Grant the agent read/write access to your Contacts, Deals, and Lists to enable full automation.

### 3) Tool Availability
- **Lead Search**: Locate contacts by email or ID.
- **Field Update**: Modify custom fields and lead status in real-time.
- **List Management**: Add or remove leads from specific nurture sequences.
- **Deal Creation**: Automatically create new opportunities for highly qualified leads.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple CRM platforms.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage deal stages and follow-up cadences for your sales team.
- [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Clean and standardize your CRM contact data automatically.
