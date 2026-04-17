# Product Launch Campaign Orchestrator (Uplizd) - Automate campaign workflows and asset synchronization

## Summary
The Product Launch Campaign Orchestrator is an intelligent Uplizd workflow designed to streamline go-to-market execution by automating list creation, field mapping, and asset synchronization across your marketing stack. By centralizing campaign data and automating repetitive setup tasks, this solution eliminates manual configuration errors, accelerates time-to-market for new product releases, and ensures a single source of truth for campaign performance metrics.

---

## Demo
![Product Launch Campaign Orchestrator workflow showing automated list creation and field mapping nodes](image.png)
**Alt text (SEO-ready):** Product Launch Campaign Orchestrator Uplizd workflow for automated marketing list creation, field mapping, and campaign synchronization using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b57c1b28-fe6f-5805-9afd-ad1dcf72d31b)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** marketing, campaign management, automation, sendlane, data sync, go-to-market, composio, ai workflow
- This solution bridges the gap between strategic campaign planning and technical execution by automating the underlying data infrastructure required for successful product launches.

---

## Who is this for?
This workflow is designed for teams managing complex product rollouts who need to maintain consistency across multiple marketing channels.

- **Marketing Operations Manager**
    - Automates the tedious setup of campaign lists and field configurations to ensure data hygiene.
- **Product Marketing Manager**
    - Ensures that campaign assets and audience segments are deployed accurately without manual intervention.
- **Growth Lead**
    - Accelerates the speed of experimentation by rapidly spinning up new campaign environments.
- **Campaign Coordinator**
    - Reduces the risk of human error during high-stakes product launches through standardized, automated workflows.

---

## Features
- **Automated List Creation**
    - Dynamically generates and populates target audience lists based on predefined campaign criteria.
- **Unified Field Mapping**
    - Synchronizes custom fields across your marketing platforms to ensure consistent data reporting.
- **Cross-Platform Integration**
    - Leverages the Composio Toolset to bridge Sendlane and other marketing tools for seamless data flow.
- **Real-time Configuration**
    - Updates campaign parameters instantly, allowing for agile adjustments during the launch window.
- **Workflow Standardization**
    - Enforces consistent naming conventions and setup procedures for every new product launch campaign.

---

## Use Cases
**Campaign Setup Automation**
- Automatically create new segments in Sendlane when a product launch is initialized in your project management tool.
- Map custom lead attributes from your CRM to campaign-specific fields to ensure personalized messaging.

**Launch Asset Synchronization**
- Sync campaign-specific email templates and assets across multiple sub-accounts to maintain brand consistency.
- Trigger automated data validation checks to ensure all required fields are populated before a campaign goes live.

**Performance Data Hygiene**
- Cleanse and normalize lead data before importing it into a new launch campaign to prevent duplicate entries.
- Archive outdated campaign lists automatically once a product launch cycle concludes to maintain a lean marketing database.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Product Launch Campaign Orchestrator template JSON.
3. Connect your required API credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the campaign parameters and product details from the user.
- **Agent**: Processes the request and determines the necessary actions for list and field setup.
- **Composio Toolset**: Executes the API calls to Sendlane and other integrated marketing platforms.
- **Chat Output**: Confirms the successful creation of the campaign and provides a summary of the actions taken.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Create a new campaign list for the 'Summer Product Launch' and map the 'Lead Source' field.`
- `Sync all active leads from the 'Beta Testers' segment into the new 'Global Launch' campaign.`
- `Verify that all custom fields for the upcoming product release are correctly mapped in Sendlane.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your marketing operations, interpreting intent and executing technical tasks.
- Use a high-reasoning model to ensure accurate field mapping.
- Provide clear instructions on the naming conventions for your campaigns.
- Enable tool-calling capabilities to allow the agent to interact with your marketing stack.

### 2) Composio Toolset Node
- Provide your Composio API key to enable secure connectivity.
- Define the scope to include only the necessary marketing platforms (e.g., Sendlane, CRM) to maintain the principle of least privilege.

### 3) Tool Availability
- **Sendlane API**: For managing lists, segments, and campaign data.
- **CRM Connector**: For fetching lead attributes and contact information.
- **Data Validator**: For ensuring field formats match your internal standards.

---

## Related Solutions
- [../abandoned-cart-recovery-agent-by-klaviyo/README.md](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automate recovery sequences for lost sales.
- [../whats-app-lead-nurturing-agent-by-spoki/README.md](../whats-app-lead-nurturing-agent-by-spoki/README.md) — Engage leads through automated messaging channels.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) — Maintain data consistency across your primary CRM and marketing tools.
