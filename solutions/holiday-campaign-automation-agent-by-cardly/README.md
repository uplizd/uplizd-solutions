# Holiday Campaign Automation Agent (Uplizd) - Streamline seasonal physical card outreach

## Summary
The Holiday Campaign Automation Agent leverages Uplizd and the Composio Toolset to orchestrate personalized physical card campaigns for key prospects and customers. By automating the transition from CRM lead data to physical fulfillment, marketing teams can significantly increase engagement, maintain brand presence during peak seasons, and eliminate manual data entry in the gifting pipeline.

---

## Demo
![Holiday Campaign Automation Agent workflow showing CRM data integration and Cardly fulfillment](image.png)
**Alt text (SEO-ready):** Holiday Campaign Automation Agent workflow using Uplizd, CRM data, and Cardly for automated physical card gifting and seasonal marketing.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAACXBIWXMAAAsTAAALEwEAmpwYAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAA)](https://uplizd.ai/solutions/holiday-campaign-automation-agent-by-cardly)

---

## Category
**Primary category:** Marketing operations  
**Secondary tags:** crm, cardly, seasonal marketing, gifting, automation, lead nurturing, composio, ai workflow  
This solution bridges the gap between digital CRM records and physical brand touchpoints to ensure no high-value lead is missed during the holiday season.

---

## Who is this for?
This workflow is designed for teams looking to scale personalized outreach without increasing operational overhead.

* **Marketing Manager**
    * Automate high-touch seasonal gifting to improve customer retention and brand loyalty.
* **Sales Operations Lead**
    * Sync CRM lead status with physical fulfillment triggers to ensure timely delivery.
* **Customer Success Manager**
    * Identify key accounts for holiday appreciation campaigns based on usage and tenure.
* **Growth Marketer**
    * Leverage physical mailers as a high-conversion channel to re-engage stalled leads.

---

## Features
- **CRM Data Integration**
    Connects directly to your CRM to pull verified mailing addresses and contact details for targeted campaigns.
- **Automated Fulfillment Triggers**
    Automatically dispatches card requests to Cardly when specific lead criteria or lifecycle stages are met.
- **Personalized Messaging Engine**
    Uses AI to generate unique, context-aware messages for each recipient, ensuring a human touch at scale.
- **Campaign Status Tracking**
    Monitors the lifecycle of each card from generation to delivery, updating CRM notes automatically.
- **Seasonal Scheduling**
    Allows for bulk processing or drip-campaign scheduling to ensure cards arrive during the optimal holiday window.

---

## Use Cases
**High-Value Account Nurturing**
* Trigger a personalized holiday card for all accounts with an open opportunity value exceeding $50,000.
* Automatically send appreciation cards to long-term customers who have renewed their contracts in Q4.

**Lead Re-engagement**
* Identify "stalled" leads from the last 6 months and send a physical card to spark a conversation.
* Send holiday greetings to prospects who attended a recent webinar but haven't booked a demo.

**Customer Loyalty Programs**
* Automate the "Thank You" card process for customers who have reached a specific milestone or usage tier.
* Send seasonal gifts to primary stakeholders at enterprise accounts to strengthen executive relationships.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Holiday Campaign Automation template from the library.
3. Connect your CRM and Cardly accounts via the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger criteria (e.g., "Send holiday cards to all closed-won customers from Q3").
* **Agent**: Analyzes the request, filters the CRM data, and prepares the personalized card content.
* **Composio Toolset**: Executes the API calls to fetch CRM data and trigger the Cardly fulfillment service.
* **Chat Output**: Confirms the number of cards sent and provides a summary of the campaign status.

### 3) Run the Flow
Use the Playground to test your campaign triggers:
* `Send a holiday card to all customers in the 'VIP' segment with a personalized message about their success this year.`
* `Find all leads in the 'Negotiation' stage and send them a holiday greeting card via Cardly.`
* `List all recipients for the current holiday campaign and confirm the status of their card delivery.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the campaign coordinator, ensuring data accuracy and tone consistency.
* Set the system prompt to prioritize professional yet warm holiday messaging.
* Configure the agent to cross-reference CRM fields (Name, Company, Last Interaction) for personalization.
* Define a strict output format for the Cardly API payload to prevent fulfillment errors.

### 2) Composio Toolset Node
* Provide your API keys for both your CRM (e.g., Salesforce, HubSpot) and Cardly.
* Ensure the connection scope includes read access for contacts and write access for activity/notes.

### 3) Tool Availability
* **CRM Connector**: For querying lead lists and updating campaign status fields.
* **Cardly API**: For submitting card orders, selecting templates, and tracking shipment status.
* **Data Parser**: For cleaning and formatting address strings to meet postal requirements.

---

## Related Solutions
* [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize lead data across multiple platforms to ensure accurate mailing lists.
* [../deal-pipeline-manager/README.md](../deal-pipeline-manager/README.md) - Manage deal stages to identify which prospects are eligible for high-touch campaigns.
* [../crm-data-hygiene-manager/README.md](../crm-data-hygiene-manager/README.md) - Clean and validate CRM address data before launching physical mailer campaigns.
