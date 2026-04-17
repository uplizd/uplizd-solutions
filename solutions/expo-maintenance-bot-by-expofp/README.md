# Expo Maintenance Bot (Uplizd) - Automated floor plan category optimization

## Summary
The Expo Maintenance Bot is an intelligent Uplizd workflow designed to automate the categorization and hygiene of expo floor plans. By leveraging AI to analyze and update exhibitor data in real-time, this solution ensures your event floor plans remain accurate, organized, and optimized for attendee navigation, ultimately reducing manual administrative overhead and improving event operational velocity.

---

## Demo
![Expo Maintenance Bot interface showing automated category mapping and floor plan updates](image.png)
**Alt text (SEO-ready):** Expo Maintenance Bot dashboard showing automated floor plan category mapping, exhibitor data synchronization, and Uplizd AI workflow integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b4614360-ccd2-5a6f-9b84-92d2d879dabf)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** expo, floor plan, data hygiene, event management, automation, expofp, ai workflow, composio
- This solution streamlines event operations by automating the classification of exhibitor spaces and maintaining data integrity within your floor plan management system.

---

## Who is this for?
This solution is designed for event professionals and operations teams looking to scale their floor plan management without increasing manual labor.

- **Event Operations Manager**
    - Automates repetitive categorization tasks to focus on strategic floor plan layout and exhibitor placement.
- **Exhibitor Success Lead**
    - Ensures exhibitor profiles are correctly mapped to floor categories, improving visibility and attendee experience.
- **Data Analyst**
    - Maintains high-quality, clean data across all event infrastructure by eliminating manual entry errors.
- **Technical Event Coordinator**
    - Integrates floor plan management tools with AI workflows to achieve real-time updates and synchronization.

---

## Features
- **Automated Categorization**
    - Uses AI to intelligently assign exhibitor categories based on company descriptions and industry tags.
- **Real-time Data Hygiene**
    - Continuously scans for outdated or mislabeled floor plan entries to ensure a single source of truth.
- **Composio-Powered Integration**
    - Seamlessly connects with ExpoFP and other event management platforms to execute updates directly.
- **Workflow Velocity**
    - Reduces the time required to update large-scale floor plans from hours of manual work to minutes of automated processing.
- **Intelligent Error Detection**
    - Identifies and flags conflicting or missing information in exhibitor records for human review.

---

## Use Cases
**Floor Plan Optimization**
- Automatically re-categorize exhibitors based on updated booth requirements or industry shifts.
- Sync floor plan updates across multiple event platforms to ensure consistency for attendees and staff.

**Exhibitor Data Management**
- Standardize exhibitor category naming conventions to match your internal taxonomy.
- Bulk-update exhibitor metadata to reflect recent changes in sponsorship or booth tiering.

**Operational Efficiency**
- Trigger automated cleanup routines whenever a new batch of exhibitors is imported into the system.
- Generate summary reports of floor plan changes to keep stakeholders informed of layout modifications.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Expo Maintenance Bot template from the solution library.
3. Connect your ExpoFP API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or manual request to audit floor plan categories.
- **Agent**: Analyzes the current floor plan data against the defined taxonomy and determines necessary updates.
- **Composio Toolset**: Executes the API calls to update exhibitor categories and booth metadata in ExpoFP.
- **Chat Output**: Provides a summary report of all changes made during the maintenance run.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Audit the current floor plan and update all uncategorized exhibitors.`
- `Re-map all 'Tech' exhibitors to the new 'Software Solutions' category.`
- `Check for data inconsistencies in the floor plan and generate a cleanup report.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine for data classification and hygiene.
- Use a high-reasoning model (e.g., GPT-4o) for accurate category mapping.
- Maintain a strict system prompt that enforces your specific floor plan taxonomy.
- Enable tool-calling capabilities to allow the agent to interact with the Composio Toolset.

### 2) Composio Toolset Node
- Provide your ExpoFP API key to grant the agent permission to read and write exhibitor data.
- Set the connection scope to include read/write access for booth and exhibitor objects.

### 3) Tool Availability
- `list_exhibitors`: Retrieve current floor plan data for analysis.
- `update_exhibitor_category`: Apply the AI-determined category to specific booth entries.
- `get_floor_plan_metadata`: Fetch current layout constraints and category definitions.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automated auditing for account configurations and compliance.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Real-time tracking of workflow performance and operational status.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamlined onboarding and setup for new accounts and entities.
