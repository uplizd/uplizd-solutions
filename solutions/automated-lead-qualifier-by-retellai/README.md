# Automated Lead Qualifier (Uplizd) - Intelligent voice-based lead qualification and routing

## Summary
The Automated Lead Qualifier by Retell AI is an intelligent voice workflow that engages inbound leads in real-time conversations to assess intent and fit. By leveraging Retell AI for natural language voice interaction and the Composio Toolset for CRM integration, this solution ensures that only high-intent prospects reach your sales team, significantly reducing manual discovery time and improving pipeline velocity.

---

## Demo
![Automated Lead Qualifier workflow diagram showing Retell AI voice interaction and CRM data sync](image.png)
**Alt text (SEO-ready):** Automated Lead Qualifier workflow by Uplizd, featuring Retell AI voice integration, CRM lead scoring, and automated sales pipeline routing.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/0ec13ba6-fe43-5ebc-90e5-4108cdaf8feb)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** lead qualification, retell ai, voice agent, crm, sales pipeline, lead scoring, composio, ai workflow
- This solution bridges the gap between initial lead capture and sales readiness by automating the discovery process through conversational AI.

---

## Who is this for?
This solution is designed for revenue teams looking to scale their lead qualification efforts without adding headcount.

- **Sales Development Reps (SDRs)**
    - Focuses energy on high-intent prospects that have already passed initial qualification criteria.
- **RevOps Managers**
    - Standardizes the qualification process across all inbound channels to ensure consistent data hygiene.
- **Growth Marketers**
    - Increases conversion rates by providing immediate engagement to leads while their interest is at its peak.
- **Sales Leaders**
    - Reduces the cost per acquisition by filtering out unqualified leads before they enter the expensive human-touch stages of the pipeline.

---

## Features
- **Real-time Voice Interaction**
    - Utilizes Retell AI to conduct natural, human-like discovery calls that capture lead intent instantly.
- **Automated CRM Sync**
    - Seamlessly updates lead status, notes, and qualification scores in your CRM via the Composio Toolset.
- **Intelligent Lead Scoring**
    - Dynamically assigns scores based on conversation responses, ensuring only qualified leads are prioritized.
- **Instant Handoff Logic**
    - Automatically triggers calendar invites or Slack notifications for sales reps when a lead meets pre-defined criteria.
- **Customizable Qualification Scripts**
    - Easily adjust the Agent node instructions to match your specific product-market fit and discovery questions.

---

## Use Cases
**Inbound Lead Discovery**
- Automatically call new web-form leads within seconds to confirm interest and budget.
- Capture key discovery data like "Number of employees" or "Current tech stack" directly into CRM fields.

**Pipeline Prioritization**
- Filter out "window shoppers" by identifying leads that do not meet your minimum qualification threshold.
- Flag high-value prospects for immediate follow-up by senior account executives.

**Data Hygiene & Enrichment**
- Update existing CRM records with fresh conversation insights without manual data entry.
- Standardize lead formatting and contact information during the initial qualification call.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the workflow.
3. Connect your Retell AI and CRM accounts within the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming lead trigger events from your web form or CRM.
- **Agent**: Processes the lead data and executes the qualification script via Retell AI.
- **Composio Toolset**: Executes CRM updates and lead routing actions based on agent findings.
- **Chat Output**: Confirms the qualification status and logs the interaction summary.

### 3) Run the Flow
Use the Playground to test your qualification logic:
- `Qualify a new inbound lead from the contact form with a budget of $50k.`
- `Check if the lead is a decision-maker and update the CRM status to 'Qualified'.`
- `Trigger a follow-up email for a lead that failed the qualification criteria.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the voice of your brand, using the following instruction pattern:
- Define the persona as a professional SDR conducting a brief discovery call.
- List the 3–5 mandatory discovery questions the agent must ask.
- Set the logic for determining a "Qualified" vs "Unqualified" lead status.

### 2) Composio Toolset Node
- Provide your CRM API key (e.g., Salesforce, HubSpot) within the Composio configuration.
- Set the connection scope to allow read/write access to lead and opportunity objects.

### 3) Tool Availability
- **CRM Search**: Locate existing records to prevent duplicate lead creation.
- **Lead Update**: Modify lead fields based on conversation outcomes.
- **Calendar/Scheduling**: Book discovery meetings for qualified prospects.
- **Notification Service**: Alert sales team members via Slack or Email.

---

## Related Solutions
- [../whats-app-lead-qualifier-by-wati/README.md](../whats-app-lead-qualifier-by-wati/README.md) - Automated lead qualification via WhatsApp.
- [../account-research-assistant-by-zoominfo/README.md](../account-research-assistant-by-zoominfo/README.md) - Deep account intelligence and research automation.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage and track sales pipeline stages effectively.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize data across multiple CRM platforms.
