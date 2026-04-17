# Lead Qualification Engine (Uplizd) - Automate lead scoring and categorization for high-velocity sales

## Summary
The Lead Qualification Engine by Acculynx is an intelligent Uplizd workflow designed to streamline the sales funnel by automatically scoring, categorizing, and prioritizing incoming leads. By leveraging AI-driven analysis, this solution ensures that sales teams focus their efforts on high-intent prospects, reducing manual data entry and significantly increasing pipeline velocity.

---

## Demo
![Lead Qualification Engine workflow diagram showing automated lead scoring and CRM routing](image.png)
**Alt text (SEO-ready):** Lead Qualification Engine workflow diagram showing automated lead scoring, CRM routing, and AI-driven prospect categorization on Uplizd.

---

## 🚀 Run on Uplizd
[Launch Lead Qualification Engine](https://uplizd.ai/solutions/6d0c641c-98b6-5dc8-be16-6c095a7ea2af)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, lead scoring, sales pipeline, lead qualification, ai workflow, composio, data hygiene, revenue operations
- This solution bridges the gap between raw lead ingestion and actionable sales intelligence, ensuring your CRM remains a source of truth for high-quality opportunities.

---

## Who is this for?
This workflow is designed for revenue-focused teams looking to eliminate manual lead triage and improve conversion rates.

- **Sales Development Representative (SDR)**
    - Automatically receives qualified leads with pre-filled context, allowing for faster outreach.
- **Revenue Operations Manager**
    - Ensures consistent lead scoring criteria across the entire organization to maintain pipeline hygiene.
- **Sales Manager**
    - Gains visibility into lead quality trends and team performance through automated categorization.
- **Marketing Operations Lead**
    - Closes the feedback loop between lead generation efforts and actual sales conversion outcomes.

---

## Features
- **Automated Lead Scoring**
    - Assigns dynamic scores to incoming leads based on predefined business rules and behavioral signals.
- **Intelligent Categorization**
    - Uses AI to classify leads into segments (e.g., Hot, Warm, Cold) for targeted follow-up strategies.
- **CRM Integration**
    - Seamlessly syncs qualified lead data into your CRM using the Composio Toolset for real-time updates.
- **Contextual Enrichment**
    - Automatically pulls firmographic data to provide sales teams with a complete view of the prospect.
- **Real-time Routing**
    - Triggers instant notifications or task assignments to the appropriate account owner based on lead score.

---

## Use Cases
**Lead Prioritization**
- Automatically flag high-intent leads for immediate outreach within 5 minutes of form submission.
- Re-score existing leads based on recent website activity or engagement with marketing content.

**Data Hygiene & Enrichment**
- Standardize lead contact information and job titles before pushing them into the CRM.
- Identify and flag duplicate lead entries to prevent sales team overlap and data fragmentation.

**Pipeline Velocity Optimization**
- Route qualified opportunities directly to the correct sales territory based on company size and industry.
- Generate automated follow-up tasks for stalled leads that have not been contacted within 48 hours.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Lead Qualification Engine template using the provided solution URL.
3. Connect your CRM and AI provider credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw lead data from webhooks or form submissions.
- **Agent**: Analyzes lead data against your qualification criteria and assigns a score.
- **Composio Toolset**: Executes CRM updates and fetches additional prospect intelligence.
- **Chat Output**: Confirms the lead has been qualified and routed to the appropriate CRM queue.

### 3) Run the Flow
Test your workflow in the Uplizd Playground with these example prompts:
- `Qualify the latest lead from the web form and assign a priority score.`
- `Check if the new lead 'John Doe' exists in the CRM and update his lead status.`
- `Categorize the incoming lead list based on company revenue and industry fit.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary decision-maker for lead scoring logic.
- Instruct the model to prioritize leads based on specific firmographic markers.
- Define clear thresholds for "Hot" vs "Cold" lead classification.
- Ensure the agent maintains a neutral, objective tone when summarizing lead data for the sales team.

### 2) Composio Toolset Node
- Provide your API key to enable secure communication with your CRM platform.
- Set the connection scope to allow read/write access for lead objects and contact records.

### 3) Tool Availability
- **CRM Search**: Locate existing records to prevent duplicates.
- **Lead Update**: Modify lead fields and status tags.
- **Data Enrichment**: Fetch external company details to supplement lead profiles.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich prospect data for better qualification.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Manage the full lifecycle of qualified opportunities.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain consistent data across multiple platforms.
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) — Deep-dive into target accounts for high-value outreach.
