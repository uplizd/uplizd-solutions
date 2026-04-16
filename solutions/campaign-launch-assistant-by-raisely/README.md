# Campaign Launch Assistant (Uplizd) - Streamline fundraising campaign setup and validation

## Summary
The Campaign Launch Assistant by Raisely is an intelligent AI workflow designed to automate the configuration, validation, and deployment of fundraising campaigns. By leveraging the Composio Toolset to interface directly with Raisely’s platform, this solution eliminates manual data entry errors, ensures campaign compliance, and accelerates time-to-market for non-profit and social impact initiatives.

---

## Demo
![Campaign Launch Assistant workflow interface showing automated Raisely configuration nodes](image.png)

**Alt text (SEO-ready):** Campaign Launch Assistant Uplizd workflow for automated fundraising campaign setup, Raisely integration, and campaign validation.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dbf5aafc-c613-5d78-be41-e1ac8dcc0e35)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** raisely, fundraising, campaign management, automation, non-profit, data validation, composio, ai workflow
- This solution optimizes the lifecycle of fundraising campaigns by automating repetitive setup tasks and ensuring data integrity across the Raisely ecosystem.

---

## Who is this for?
This solution is designed for teams managing high-volume fundraising efforts who need to maintain consistency and speed.

- **Campaign Manager**
    - Automates the creation of campaign pages and donation forms to reduce manual overhead.
- **Non-Profit Director**
    - Ensures all launched campaigns meet organizational branding and compliance standards automatically.
- **Digital Marketing Specialist**
    - Syncs campaign metadata and tracking parameters across platforms without manual configuration.
- **Operations Lead**
    - Validates campaign settings and goal configurations to prevent launch-day errors.

---

## Features
- **Automated Campaign Creation**
    - Instantly initialize new fundraising pages using pre-defined templates and organizational settings.
- **Real-time Validation**
    - Automatically check campaign goals, end dates, and donation tiers against internal requirements before deployment.
- **Composio-Powered Integration**
    - Seamlessly connect with Raisely APIs to push updates and pull status reports in real-time.
- **Dynamic Content Mapping**
    - Map donor impact stories and campaign descriptions directly from your knowledge base to the Raisely editor.
- **Error Mitigation**
    - Identify and flag configuration mismatches, such as broken links or invalid payment gateway settings, before the campaign goes live.

---

## Use Cases
**Campaign Lifecycle Management**
- Automatically generate a new fundraising landing page based on a standardized project brief.
- Sync campaign status updates from Raisely back to your internal project management dashboard.

**Data Hygiene and Compliance**
- Audit active campaigns to ensure all donation tiers are correctly mapped to the intended impact funds.
- Verify that all campaign metadata, including UTM parameters, is correctly formatted for analytics tracking.

**Rapid Scaling**
- Clone successful campaign structures for seasonal fundraising events with a single prompt.
- Bulk-update campaign end dates and goal targets across multiple active fundraising initiatives.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Campaign Launch Assistant JSON configuration file.
3. Connect your Raisely API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives campaign details, goals, and target audience data from the user.
- **Agent**: Processes instructions, validates campaign constraints, and determines the necessary API actions.
- **Composio Toolset**: Executes the specific Raisely API calls to create or update campaign resources.
- **Chat Output**: Returns a confirmation summary, including the live campaign URL and a status report of the configuration.

### 3) Run the Flow
Use the Playground to test your campaign setup:
- `Create a new fundraising campaign for the 'Spring Gala' with a goal of $50,000.`
- `Validate the settings for the 'Summer Relief' campaign and ensure the donation tier is set to $100.`
- `List all active campaigns in Raisely and check if any are missing a description.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the campaign architect, ensuring all inputs align with organizational standards.
- Use a model capable of structured data output (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a Raisely expert. Always validate that the campaign goal is a positive integer and the end date is in the future."
- Instruction: "If a required field is missing from the user input, ask for clarification before calling the Composio Toolset."

### 2) Composio Toolset Node
- Provide your Raisely API Key to enable secure communication.
- Set the connection scope to include `campaigns:write` and `campaigns:read` permissions.

### 3) Tool Availability
- `raisely_create_campaign`: Initializes a new campaign entity.
- `raisely_update_campaign`: Modifies existing campaign settings or goals.
- `raisely_get_campaign_details`: Fetches current configuration for validation.
- `raisely_list_campaigns`: Retrieves a summary of all existing initiatives.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Recover lost donations and donor interest.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich donor and account data for better targeting.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Extend automation capabilities across your operational stack.
