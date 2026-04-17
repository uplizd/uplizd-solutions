# Event Follow-Up Card Agent (Uplizd) - Automated post-event networking and relationship management

## Summary
The Event Follow-Up Card Agent streamlines post-event engagement by automatically triggering personalized follow-up cards for trade show and conference contacts. By integrating event lead data with physical or digital card delivery services, this Uplizd AI workflow ensures timely, memorable outreach that increases conversion rates and strengthens professional relationships without manual administrative overhead.

---

## Demo
![Event Follow-Up Card Agent workflow showing lead data processing and card dispatch](image.png)
**Alt text (SEO-ready):** Event Follow-Up Card Agent workflow for Uplizd, automating trade show lead outreach, CRM data integration, and personalized follow-up card delivery.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/badge/run-on-uplizd.svg)](https://uplizd.ai/solutions/40c6c688-c51f-523f-9267-40f3a60acb07)

---

## Category
**Primary category:** Sales automation
**Secondary tags:** crm, event management, lead nurturing, cardly, sales operations, relationship building, automation, composio

This solution bridges the gap between physical event networking and digital CRM workflows to ensure no lead is left behind.

---

## Who is this for?
This agent is designed for teams looking to turn high-touch event interactions into long-term business opportunities.

- **Sales Development Representative (SDR)**
    - Automates the tedious process of sending thank-you notes to hundreds of booth visitors.
- **Event Manager**
    - Ensures consistent brand messaging and follow-up quality across all trade show appearances.
- **Account Executive (AE)**
    - Keeps prospects warm with personalized physical touchpoints that stand out in a digital-first world.
- **Marketing Operations Lead**
    - Maintains data hygiene by syncing event lead status directly with CRM follow-up activities.

---

## Features
- **Automated Triggering**
    - Instantly initiates follow-up sequences as soon as new event leads are captured or imported into your CRM.
- **Personalized Messaging**
    - Uses AI to draft unique, context-aware messages based on notes taken during the event interaction.
- **Composio Toolset Integration**
    - Seamlessly connects with Cardly and major CRM platforms to handle data extraction and physical mail dispatch.
- **Real-time Status Tracking**
    - Monitors the progress of each follow-up card, providing updates directly within your workflow dashboard.
- **Scalable Outreach**
    - Handles bulk processing of event contacts, allowing your team to manage thousands of leads with the same effort as ten.

---

## Use Cases
**Trade Show Lead Nurturing**
- Automatically send a branded thank-you card to every prospect who scanned their badge at your booth.
- Trigger a follow-up sequence based on the specific product interest tagged during the event conversation.

**Executive Relationship Building**
- Send high-value, personalized cards to VIP prospects identified during networking sessions.
- Coordinate physical gift or card delivery for key accounts to ensure your brand remains top-of-mind post-event.

**CRM Data Hygiene & Sync**
- Update lead status in your CRM to "Follow-up Sent" once the card dispatch is confirmed by the agent.
- Log interaction history automatically to ensure the entire sales team has visibility into the lead's engagement timeline.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template in the builder.
2. Connect your preferred CRM and Cardly accounts via the Composio Toolset.
3. Configure your trigger settings to point to your event lead source or CSV import.
4. Ensure nodes are correctly linked from the Chat Input to the Agent, Toolset, and Output.

### 2) Setup the Nodes
- **Chat Input**: Receives event lead data or manual trigger commands.
- **Agent**: Processes lead context and drafts personalized follow-up content.
- **Composio Toolset**: Executes the API calls to Cardly and updates CRM records.
- **Chat Output**: Confirms successful dispatch and provides a summary of sent items.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Send a follow-up card to John Doe from the Tech Expo with a note about our new API features.`
- `Process all new leads from the 'Q3 Trade Show' list and send them the standard follow-up card.`
- `Check the status of the follow-up cards sent to the leads from yesterday's event.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a professional communication assistant.
- Use a concise, warm, and professional tone for all outgoing cards.
- Reference specific event details provided in the lead input to ensure personalization.
- Maintain a clear call-to-action (CTA) for the next meeting or demo.

### 2) Composio Toolset Node
- Provide your Cardly API key and CRM credentials within the Composio configuration panel.
- Ensure the connection scope includes read/write access to your lead objects and mailing services.

### 3) Tool Availability
- **CRM Connector**: For retrieving lead details and updating interaction status.
- **Cardly API**: For selecting templates, generating physical cards, and managing delivery addresses.
- **Notification Service**: For alerting the sales team once the mailing process is complete.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather deep intelligence on prospects before sending follow-ups.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Keep your lead data consistent across multiple platforms during event cycles.
- [Deal Pipeline Manager](../deal-pipeline-manager/README.md) - Move leads through your sales funnel after the initial follow-up is sent.
