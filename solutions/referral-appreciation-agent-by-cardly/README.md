# Referral Appreciation Agent (Uplizd) - Automate physical thank you cards for successful referrals

## Summary
The Referral Appreciation Agent is an automated workflow designed to strengthen professional relationships by triggering physical thank you cards via Cardly whenever a new referral is successfully converted. By integrating CRM data with physical mail services, this solution ensures high-touch engagement without manual effort, increasing referral velocity and partner loyalty.

---

## Demo
![Referral Appreciation Agent workflow showing CRM trigger to Cardly dispatch](image.png)
**Alt text (SEO-ready):** Referral Appreciation Agent workflow in Uplizd, automating physical thank you cards via Cardly for CRM referral conversions.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhL7dExDQAgEAMw+B+9h8M4gIAJkE5yE12ySgAAwJ+79wAAgD937wAAgD937wAAgD937wAAgD937wAAgD937wAAgD8X2gE5+w1eAAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/1b21ad9b-80ed-58ae-9321-242922479b85)

---

## Category
**Primary category:** Sales automation  
**Secondary tags:** referral, cardly, crm, customer loyalty, automation, sales operations, partner management, composio  
This solution bridges the gap between digital CRM milestones and physical relationship-building touchpoints.

---

## Who is this for?
This agent is designed for teams looking to humanize their digital outreach and reward high-value partners.

- **Sales Managers**
    - Automate the recognition process to ensure no referral goes unacknowledged.
- **Partner Success Leads**
    - Maintain high engagement levels with referral sources through personalized physical mail.
- **RevOps Specialists**
    - Standardize the post-conversion workflow to include physical touchpoints without manual intervention.
- **Customer Success Managers**
    - Strengthen long-term relationships by adding a tangible, thoughtful element to the referral lifecycle.

---

## Features
- **Automated Triggering**
    - Instantly detects new referral conversions in your CRM to initiate the appreciation workflow.
- **Personalized Messaging**
    - Uses the Agent node to draft warm, context-aware thank you notes based on referral data.
- **Cardly Integration**
    - Seamlessly dispatches physical cards via the Composio Toolset to the referrer's mailing address.
- **Real-time Sync**
    - Ensures that the status of the appreciation card is updated back into your CRM for full visibility.
- **Customizable Templates**
    - Allows for dynamic insertion of referral details, such as the referred client's name or project scope.

---

## Use Cases
**Referral Milestone Recognition**
- Automatically send a "Thank You" card when a referral reaches the "Closed-Won" stage.
- Include a personalized note referencing the specific client referred to build deeper rapport.

**Partner Loyalty Programs**
- Trigger a branded appreciation card after a partner hits a specific threshold of successful referrals.
- Send automated quarterly appreciation cards to top-tier referral sources to maintain top-of-mind awareness.

**High-Value Account Nurturing**
- Identify high-value referrals and trigger a premium physical card to ensure the partner feels valued.
- Coordinate physical mailings with digital follow-up emails to create a multi-channel appreciation strategy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your CRM and Cardly accounts via the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the referral conversion event data from your CRM.
- **Agent**: Processes the referral details and drafts a personalized thank you message.
- **Composio Toolset**: Executes the API call to Cardly to generate and mail the physical card.
- **Chat Output**: Confirms the card dispatch status and logs the action in your CRM.

### 3) Run the Flow
Test the workflow in the Playground:
- `Send a thank you card to John Doe for the referral of Acme Corp.`
- `Draft a note for Sarah Smith thanking her for the recent referral and trigger a Cardly dispatch.`
- `Verify the status of the last referral appreciation card sent to our top partner.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the communication layer, transforming raw CRM data into professional, human-like correspondence.
- Instruction: "You are a professional relationship manager tasked with drafting personalized thank you notes for referrals."
- Instruction: "Always extract the referrer's name, address, and the referred company name from the input."
- Instruction: "Maintain a warm, appreciative tone while ensuring the message is concise and professional."

### 2) Composio Toolset Node
- **API Key**: Ensure your Cardly API key is active within the Composio dashboard.
- **Connection Scope**: Grant the toolset permission to create and send mailings on your behalf.

### 3) Tool Availability
- **Cardly Create Campaign**: Ability to initiate new card mailings.
- **CRM Update**: Ability to log the "Card Sent" status back to the lead or contact record.
- **Data Fetcher**: Ability to retrieve partner contact details from your CRM.

---

## Related Solutions
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize and clean CRM data across multiple platforms.
- [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage deal stages and automate follow-up cadences.
- [../account-relationship-builder-by-dynamics365/README.md](../account-relationship-builder-by-dynamics365/README.md) - Strengthen account relationships using Dynamics 365 insights.
