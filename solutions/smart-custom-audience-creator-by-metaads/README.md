# Smart Custom Audience Creator (Uplizd) - Automate targeted ad audience segmentation

## Summary
The Smart Custom Audience Creator is an intelligent Uplizd workflow that transforms raw customer data and behavioral insights into high-performing Meta Ads custom audiences. By automating the segmentation process, marketing teams can ensure their ad spend is directed toward the most relevant prospects, significantly improving pipeline velocity and campaign ROI through data-driven precision.

---

## Demo
![Smart Custom Audience Creator workflow diagram showing data ingestion, audience segmentation, and Meta Ads synchronization](image.png)
**Alt text (SEO-ready):** Smart Custom Audience Creator Uplizd workflow for Meta Ads audience segmentation, CRM data integration, and automated marketing pipeline optimization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/87b99e86-210d-540a-8804-e2be3edd1f12)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** meta ads, audience segmentation, crm, ad targeting, marketing automation, composio, data sync, growth marketing.
This solution bridges the gap between raw CRM customer intelligence and live advertising platforms to maximize ad relevance.

---

## Who is this for?
This solution is designed for growth-focused teams looking to eliminate manual list management and improve ad performance.

*   **Growth Marketer**
    *   Automates the creation of lookalike and custom audiences based on real-time conversion data.
*   **Paid Media Manager**
    *   Reduces manual CSV uploads by syncing CRM segments directly to Meta Ads Manager.
*   **RevOps Specialist**
    *   Ensures data hygiene by maintaining consistent audience definitions across the marketing stack.
*   **CRM Administrator**
    *   Streamlines the flow of high-intent customer segments from the database to ad platforms.

---

## Features
- **Automated Audience Sync**
    Directly push segmented customer lists to Meta Ads Manager without manual exports.
- **Behavioral Segmentation**
    Leverage CRM activity data to group users by purchase history, engagement levels, or intent signals.
- **Real-time Data Updates**
    Keep custom audiences fresh by triggering updates based on specific CRM events or time-based intervals.
- **Composio-Powered Integration**
    Utilize the Composio Toolset to securely authenticate and interact with Meta Ads and CRM APIs.
- **Performance-Driven Logic**
    Apply AI-driven filters to exclude existing customers or focus exclusively on high-LTV prospects.

---

## Use Cases
**Ad Targeting Optimization**
*   Sync high-intent leads from your CRM to Meta Ads for immediate retargeting campaigns.
*   Exclude existing customers from top-of-funnel awareness campaigns to optimize ad spend.

**Customer Lifecycle Marketing**
*   Create custom audiences for lapsed customers based on their last purchase date in the CRM.
*   Build lookalike audiences based on your top 10% most profitable customers identified via data analysis.

**Data-Driven Campaign Management**
*   Automatically refresh audience segments based on recent webinar attendance or whitepaper downloads.
*   Sync event-based segments to Meta Ads to trigger time-sensitive promotional offers.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your Meta Ads and CRM accounts within the integration settings.
4. Ensure nodes are correctly mapped to your specific API credentials and environment variables.

### 2) Setup the Nodes
*   **Chat Input**: Receives natural language requests for audience criteria or segment updates.
*   **Agent**: Interprets marketing requirements and translates them into API calls for audience management.
*   **Composio Toolset**: Executes the secure connection to Meta Ads and CRM platforms to push audience data.
*   **Chat Output**: Confirms the successful creation or update of the audience segment in the ad platform.

### 3) Run the Flow
*   `Create a custom audience in Meta Ads for all leads who signed up in the last 30 days.`
*   `Update the 'High LTV' audience segment by syncing the latest customer data from Salesforce.`
*   `Exclude users who have already purchased from the 'Summer Sale' ad campaign audience.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between your CRM data and ad platform APIs.
*   Focus on mapping natural language intent to specific audience criteria.
*   Ensure the agent has access to the latest schema definitions for your CRM fields.
*   Use clear, concise instructions to prevent over-segmentation or data duplication.

### 2) Composio Toolset Node
*   Requires a valid Meta Ads API key and appropriate scope permissions (e.g., `ads_management`, `ads_read`).
*   Ensure the CRM connector is configured to allow read access to customer contact and activity objects.

### 3) Tool Availability
*   **Meta Ads API**: For creating, updating, and managing custom audience lists.
*   **CRM Connector**: For querying customer lists, filtering by attributes, and exporting data.
*   **Data Transformation Utility**: For formatting CRM data into the structure required by the Meta Ads API.

---

## Related Solutions
*   [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automate recovery workflows for lost revenue.
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich account data for better targeting.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep customer data consistent across platforms.
