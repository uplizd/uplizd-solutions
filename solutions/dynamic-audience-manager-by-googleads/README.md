# Dynamic Audience Manager (Uplizd) - Automated customer segmentation and Google Ads list synchronization

## Summary
The Dynamic Audience Manager is an intelligent Uplizd workflow that synchronizes customer behavioral data with Google Ads to ensure real-time audience segmentation. By automating the flow of data between your CRM and advertising platforms, this solution eliminates manual list management, improves ad targeting precision, and maximizes return on ad spend (ROAS) by ensuring your campaigns always reach the most relevant segments.

---

## Demo
![Dynamic Audience Manager workflow showing CRM data flowing into Google Ads segmentation nodes](image.png)
**Alt text (SEO-ready):** Dynamic Audience Manager workflow for automated Google Ads customer list synchronization and CRM data segmentation using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b95f7cf4-4bdf-545a-8f8e-d67c1a78bc32)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** google ads, crm, audience segmentation, data sync, adtech, marketing automation, composio, ai workflow
- This solution bridges the gap between customer relationship management and digital advertising platforms to maintain high-performing, dynamic audience lists.

---

## Who is this for?
This solution is designed for marketing and growth teams looking to eliminate manual data entry and improve ad targeting accuracy.

- **Growth Marketer**
  - Automates the creation of high-intent audience lists based on real-time user behavior.
- **Paid Media Specialist**
  - Ensures ad spend is directed toward the most qualified segments by keeping lists updated.
- **Marketing Operations Manager**
  - Maintains data hygiene across advertising platforms without requiring manual CSV uploads.
- **CRM Administrator**
  - Syncs complex customer attributes directly to Google Ads to enable granular audience filtering.

---

## Features
- **Real-time Audience Sync**
  - Automatically pushes CRM updates to Google Ads, ensuring your audiences are always current.
- **Behavior-Based Segmentation**
  - Uses AI to categorize users based on specific actions, purchase history, or engagement levels.
- **Composio-Powered Integration**
  - Leverages the Composio Toolset to securely connect and communicate with Google Ads APIs.
- **Automated List Hygiene**
  - Removes inactive or unqualified leads from active campaigns to optimize budget allocation.
- **Custom Trigger Logic**
  - Allows for flexible configuration of the conditions that trigger an audience list update.

---

## Use Cases
**Campaign Optimization**
- Sync high-value leads from your CRM to Google Ads to create "Lookalike" audiences.
- Automatically exclude converted customers from top-of-funnel awareness campaigns.

**Lifecycle Marketing**
- Move users into "Re-engagement" lists based on inactivity signals detected in the CRM.
- Update "VIP" audience segments immediately after a user hits a specific lifetime value threshold.

**Data-Driven Targeting**
- Segment users by product interest or category to serve hyper-relevant ad creative.
- Sync regional or demographic data to Google Ads for localized campaign targeting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Connect your Google Ads and CRM accounts via the Composio dashboard.
3. Configure your specific segment criteria within the Agent node instructions.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or automated signals from your CRM webhook.
- **Agent**: Processes the data and determines the appropriate audience list for the user.
- **Composio Toolset**: Executes the API calls to add or remove users from Google Ads lists.
- **Chat Output**: Confirms the successful synchronization of the audience data.

### 3) Run the Flow
Use the Playground to test your audience logic:
- `Sync all users who purchased in the last 30 days to the 'Recent Buyers' list.`
- `Remove users with a 'Churned' status from the 'Active Prospects' audience.`
- `Update the 'High Value' segment with all leads having a score above 80.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine that translates CRM data into actionable audience updates.
- Use a model capable of structured data parsing (e.g., GPT-4o).
- Define clear mapping rules between CRM fields and Google Ads list identifiers.
- Instruct the agent to handle errors gracefully if a user is already present or missing from a list.

### 2) Composio Toolset Node
- Provide your Google Ads API credentials within the Composio connection settings.
- Ensure the connection scope includes `adwords` and `customer_match` permissions.

### 3) Tool Availability
- `google_ads_add_user_to_list`: Adds a specific email or ID to a target audience.
- `google_ads_remove_user_from_list`: Removes a user from a target audience.
- `crm_fetch_user_data`: Retrieves the latest attributes for a specific customer.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Gather deep intelligence on target accounts to inform your segmentation strategy.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Maintain consistent customer data across your entire tech stack.
- [Affiliate Program Analytics Agent](../affiliate-program-analytics-agent-by-tapfiliate/README.md) - Track and optimize performance for your affiliate-driven audience segments.
