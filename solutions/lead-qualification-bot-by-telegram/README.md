# Lead Qualification Bot (Uplizd) - Automate lead scoring and qualification via Telegram

## Summary
The Lead Qualification Bot (Uplizd) streamlines your sales pipeline by automating the initial engagement and scoring of incoming leads directly through Telegram. By leveraging AI-driven conversational workflows, this solution ensures that only high-intent prospects reach your sales team, significantly reducing manual data entry and increasing pipeline velocity.

---

## Demo
![Lead Qualification Bot workflow diagram showing Telegram input, AI agent scoring, and CRM update](image.png)
**Alt text (SEO-ready):** Uplizd lead qualification workflow using Telegram, AI agent scoring, and automated CRM synchronization for sales teams.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6b852b5f-6254-5dd6-9dca-7067a4dcd770)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** telegram, lead qualification, crm, sales pipeline, ai workflow, lead scoring, composio, automation
- This solution bridges the gap between instant messaging and CRM management, providing a scalable way to qualify leads in real-time.

---

## Who is this for?
This solution is designed for revenue-focused teams looking to optimize their lead intake process.

- **Sales Development Representatives (SDRs)**
  - Focuses energy on high-intent leads that have already passed initial qualification criteria.
- **Revenue Operations Managers**
  - Ensures consistent data hygiene and standardized scoring metrics across all incoming lead channels.
- **Growth Marketers**
  - Reduces friction in the conversion funnel by providing immediate responses to potential customers.
- **Small Business Owners**
  - Manages lead intake and initial triage without the need for a dedicated 24/7 support staff.

---

## Features
- **Conversational Qualification**
  - Uses AI to ask targeted discovery questions, ensuring leads meet your specific business requirements before reaching a human.
- **Automated Lead Scoring**
  - Assigns dynamic scores to prospects based on their responses, allowing for intelligent prioritization in your CRM.
- **Telegram Integration**
  - Provides a familiar, high-engagement interface for prospects to interact with your brand instantly.
- **CRM Synchronization**
  - Automatically pushes qualified lead data into your CRM, keeping your pipeline updated without manual intervention.
- **Real-time Alerting**
  - Notifies your sales team immediately when a high-value lead is identified, enabling rapid follow-up.

---

## Use Cases
**Lead Triage and Routing**
- Automatically route high-scoring leads to the appropriate account executive based on industry or company size.
- Flag low-intent leads for automated nurturing sequences instead of direct sales outreach.

**Data Enrichment and Hygiene**
- Capture and validate contact information directly within the Telegram chat to ensure CRM accuracy.
- Standardize lead responses into structured data fields for better reporting and analytics.

**Pipeline Velocity Optimization**
- Eliminate the "waiting period" between initial interest and human contact by providing instant AI-driven engagement.
- Reduce administrative overhead by automating the initial discovery call process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to initialize the workflow.
3. Connect your Telegram bot token and CRM API credentials in the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives incoming messages from Telegram prospects.
- **Agent**: Analyzes intent, asks qualification questions, and calculates lead scores.
- **Composio Toolset**: Executes CRM updates and data enrichment tasks.
- **Chat Output**: Delivers the final response or confirmation to the user on Telegram.

### 3) Run the Flow
Test the workflow in the Uplizd Playground:
- `Can you tell me more about your enterprise pricing plans?`
- `I am interested in a demo for my team of 50 people.`
- `What are the primary features of your software compared to competitors?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a professional sales assistant.
- **Instruction Pattern:**
  - Maintain a helpful, professional, and concise tone.
  - Follow the qualification script strictly to ensure consistent scoring.
  - Escalate to a human representative only when specific high-intent triggers are met.

### 2) Composio Toolset Node
- Requires a valid API key for your CRM (e.g., Salesforce, HubSpot).
- Connection scope should include read/write access to "Leads" and "Contacts" objects.

### 3) Tool Availability
- **Lead Lookup**: Search for existing records to prevent duplicates.
- **Lead Creation**: Add new qualified prospects to the CRM.
- **Field Update**: Modify lead status and score based on conversation outcomes.

---

## Related Solutions
- [../whats-app-lead-qualifier-by-wati/README.md](../whats-app-lead-qualifier-by-wati/README.md) - Similar lead qualification logic adapted for WhatsApp.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple CRM platforms.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage and track deal stages after lead qualification.
