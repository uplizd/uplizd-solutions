# Smart Lead Segmentation Agent (Uplizd) - Automated CRM contact categorization and list management

## Summary
The Smart Lead Segmentation Agent leverages Uplizd AI to analyze contact attributes and behavioral data within SendFox, automatically organizing leads into high-conversion segments. By streamlining list hygiene and targeting, this workflow ensures marketing teams deliver personalized content to the right audience, significantly increasing pipeline velocity and campaign engagement.

---

## Demo
![Smart Lead Segmentation Agent workflow interface showing SendFox integration nodes and AI categorization logic](image.png)
**Alt text (SEO-ready):** Smart Lead Segmentation Agent Uplizd workflow for SendFox CRM data hygiene and automated contact list management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/3b041da0-2898-5242-9069-7898f3d5bdf4)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** crm, sendfox, lead segmentation, data hygiene, email marketing, pipeline, composio, ai workflow
- This solution bridges the gap between raw contact data and actionable marketing segments by automating the classification process.

---

## Who is this for?
This agent is designed for teams looking to optimize their email marketing efficiency and lead conversion rates.

- **Marketing Manager**
    - Automates the tedious process of manual list sorting to focus on high-level campaign strategy.
- **Sales Operations Specialist**
    - Ensures CRM data hygiene by maintaining clean, segmented lists that reflect current lead status.
- **Growth Marketer**
    - Increases email open and click-through rates by delivering hyper-targeted content to specific segments.
- **Email Specialist**
    - Reduces churn by ensuring subscribers receive relevant communications based on their behavioral triggers.

---

## Features
- **Automated Behavioral Tagging**
    - Dynamically assigns tags to contacts based on real-time engagement data synced from SendFox.
- **Intelligent List Routing**
    - Automatically moves contacts between lists based on predefined conversion criteria or interaction history.
- **Composio-Powered CRM Integration**
    - Uses the Composio Toolset to execute secure, real-time read/write operations across your SendFox account.
- **Dynamic Data Hygiene**
    - Identifies and flags inactive or low-intent leads to maintain high deliverability and list health.
- **Customizable Segmentation Logic**
    - Easily adjust the AI instruction set to define new segments based on custom fields or specific lead attributes.

---

## Use Cases
**Targeted Email Campaigns**
- Segment leads based on specific product interests to trigger personalized nurture sequences.
- Filter contacts by engagement level to re-target inactive subscribers with win-back offers.

**Sales Pipeline Optimization**
- Automatically move high-intent leads into a "Sales Ready" list for immediate outreach.
- Categorize leads by source to track which channels provide the highest quality prospects.

**List Maintenance & Hygiene**
- Identify and remove duplicate or incomplete contact profiles to optimize SendFox storage.
- Periodically refresh segments based on the latest contact activity to ensure campaign relevance.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template.
2. Connect your SendFox account via the Composio Toolset node.
3. Configure your target list IDs within the agent instructions.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives triggers or manual requests to initiate segmentation.
- **Agent**: Processes contact data and applies logic to determine segment placement.
- **Composio Toolset**: Executes the API calls to update contact tags and list memberships in SendFox.
- **Chat Output**: Returns a summary report of the contacts processed and segments updated.

### 3) Run the Flow
Use the Playground to test your segmentation logic:
- `Segment all contacts who clicked the last newsletter into the 'High Intent' list.`
- `Move inactive leads from the last 90 days to the 'Archive' list.`
- `Analyze the 'New Leads' list and tag them based on their industry attribute.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a data analyst that interprets CRM attributes and maps them to your marketing strategy.
- Focus on identifying patterns in user behavior.
- Strictly adhere to the list naming conventions defined in your SendFox account.
- Prioritize accuracy when updating contact tags to avoid duplicate entries.

### 2) Composio Toolset Node
- **API Key**: Ensure your SendFox API key is active within the Composio dashboard.
- **Connection Scope**: Grant read/write permissions for lists, contacts, and tags to allow the agent to perform full segmentation tasks.

### 3) Tool Availability
- `sendfox_get_contacts`: Retrieve contact profiles and current metadata.
- `sendfox_update_contact`: Apply new tags or update contact attributes.
- `sendfox_add_to_list`: Move contacts into specific target segments.
- `sendfox_remove_from_list`: Clean up lists by removing contacts that no longer fit the criteria.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Recovers lost revenue through automated email triggers.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Gathers insights on account activity to inform sales outreach.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronizes contact data across multiple platforms for a single source of truth.
