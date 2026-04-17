# Seasonal Campaign List Manager (Uplizd) - Automate targeted customer segmentation for seasonal marketing

## Summary
The Seasonal Campaign List Manager is an intelligent Uplizd workflow designed to automate the creation and refinement of customer segments for seasonal marketing initiatives. By leveraging the Composio Toolset to interface with your CRM and email platforms, this solution identifies high-intent leads and organizes them into targeted lists, ensuring your promotional messaging reaches the right audience at the peak of their engagement cycle.

---

## Demo
![Seasonal Campaign List Manager workflow showing CRM data integration and automated list segmentation](image.png)
**Alt text (SEO-ready):** Seasonal Campaign List Manager workflow for automated CRM segmentation, Uplizd marketing automation, and Sendlane list building.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a0a15b9b-7de0-5247-a2dc-e24ace72c613)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** crm, sendlane, marketing automation, customer segmentation, list management, email marketing, composio, ai workflow

This solution streamlines seasonal marketing by automating the data-heavy process of list curation and audience targeting.

---

## Who is this for?
This solution is designed for marketing teams and revenue operations professionals looking to reduce manual list preparation time.

- **Marketing Manager**
    - Automates the creation of seasonal segments to ensure timely campaign launches.
- **Email Marketing Specialist**
    - Increases campaign ROI by targeting highly relevant customer cohorts based on historical behavior.
- **RevOps Analyst**
    - Maintains data hygiene by syncing clean, segmented lists across CRM and email platforms.
- **Growth Lead**
    - Scales seasonal promotional efforts without increasing manual administrative overhead.

---

## Features
- **Automated Segmentation**
    - Dynamically filters CRM contacts based on seasonal purchase history and engagement metrics.
- **Cross-Platform Sync**
    - Seamlessly pushes curated lists from your CRM to Sendlane using the Composio Toolset.
- **Real-Time Data Enrichment**
    - Pulls the latest contact activity to ensure lists are current before campaign deployment.
- **Customizable Logic**
    - Adjusts filtering criteria based on specific seasonal themes like holiday sales or back-to-school events.
- **Error Handling & Validation**
    - Automatically flags incomplete contact profiles to prevent delivery failures during high-volume campaigns.

---

## Use Cases
**Holiday Campaign Preparation**
- Automatically segment customers who made purchases during the previous year's holiday season.
- Sync high-value VIP lists to Sendlane for early-access promotional emails.

**Seasonal Product Launches**
- Identify users interested in specific categories to create targeted pre-launch notification lists.
- Filter out inactive subscribers to maintain high email deliverability rates during peak seasons.

**Performance-Based Retargeting**
- Create lists of customers who abandoned carts during seasonal peaks for automated recovery workflows.
- Segment users based on their engagement with previous seasonal newsletters to refine future targeting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace and project environment.
3. Authenticate your CRM and Sendlane accounts within the integration settings.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input:** Receives the seasonal campaign parameters and target criteria.
- **Agent:** Analyzes the request and determines the necessary segmentation logic.
- **Composio Toolset:** Executes the API calls to fetch CRM data and update Sendlane lists.
- **Chat Output:** Confirms the list creation and provides a summary of the processed contacts.

### 3) Run the Flow
Use the Playground to test your segmentation logic with prompts like:
- `Create a list of all customers who purchased in Q4 last year and add them to the 'Holiday VIP' segment in Sendlane.`
- `Find all users who engaged with our summer collection emails and create a new segment for the upcoming fall launch.`
- `Identify inactive leads from the last 6 months and move them to a 'Re-engagement' list in Sendlane.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for data retrieval and list management.
- Use a high-reasoning model to ensure accurate interpretation of complex segmentation queries.
- Provide clear instructions on mapping CRM fields to Sendlane list attributes.
- Ensure the agent is instructed to verify list existence before attempting to add contacts.

### 2) Composio Toolset Node
- Provide your API keys for both your CRM and Sendlane accounts.
- Set the connection scope to allow read access for contact data and write access for list management.

### 3) Tool Availability
- **CRM Connector:** For querying contact history, purchase data, and engagement tags.
- **Sendlane API:** For creating new lists, adding subscribers, and updating segment tags.
- **Data Processor:** For formatting and cleaning contact information before sync.

---

## Related Solutions
- [../abandoned-cart-recovery-agent-by-klaviyo/README.md](Abandoned Cart Recovery Agent) - Automate recovery workflows for seasonal shoppers.
- [../whats-app-lead-nurturing-agent-by-spoki/README.md](WhatsApp Lead Nurturing Agent) - Extend seasonal campaigns to mobile messaging channels.
- [../account-intelligence-reporter-by-leadfeeder/README.md](Account Intelligence Reporter) - Gather deeper insights for high-value seasonal targeting.
