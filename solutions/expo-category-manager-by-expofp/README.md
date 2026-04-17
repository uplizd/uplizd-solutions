# Expo Category Manager (Uplizd) - Automate event floor plan organization and category mapping

## Summary
The Expo Category Manager by ExpoFP is an intelligent Uplizd workflow designed to automate the classification and organization of event floor plan categories. By leveraging AI-driven mapping, this solution eliminates manual data entry, ensures consistent taxonomy across large-scale event layouts, and significantly reduces the time required for floor plan maintenance, providing event organizers with a single source of truth for exhibitor placement and category hygiene.

---

## Demo
![Expo Category Manager workflow interface showing automated category mapping and floor plan synchronization](image.png)
**Alt text (SEO-ready):** Expo Category Manager Uplizd workflow for automated floor plan category mapping, event data synchronization, and ExpoFP integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMJFR0W+7/35QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxK04AAAAiSURBVEjHY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwChgBAAAGAAH5314AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/594bd510-b507-5729-99f6-cd7af277e8c1)

---

## Category
**Primary category:** Event operations  
**Secondary tags:** `expofp`, `floor plan`, `data mapping`, `event management`, `taxonomy`, `automation`, `composio`, `ai workflow`  
This solution streamlines event floor plan management by automating the categorization of exhibitors and booth placements through intelligent data synchronization.

---

## Who is this for?
This workflow is designed for event professionals and operations teams managing complex floor plans.

- **Event Planners**
    - Automate the assignment of exhibitors to specific floor plan categories to save hours of manual sorting.
- **Operations Managers**
    - Ensure data hygiene across event layouts by maintaining a consistent and error-free category taxonomy.
- **Exhibitor Success Leads**
    - Improve exhibitor visibility by ensuring accurate placement and categorization on digital floor plans.
- **Data Analysts**
    - Generate cleaner event reports by standardizing category labels and mapping data directly from the floor plan source.

---

## Features
- **Automated Category Mapping**
    - Uses AI to intelligently match exhibitor data with predefined floor plan categories, reducing manual oversight.
- **Real-time Sync**
    - Connects directly with ExpoFP to ensure that any changes in exhibitor status are reflected immediately on the floor plan.
- **Taxonomy Standardization**
    - Enforces a consistent naming convention across all event categories to prevent data fragmentation.
- **Bulk Update Capability**
    - Processes large lists of exhibitors and categories in a single workflow execution, ideal for massive trade shows.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to bridge the gap between AI logic and the ExpoFP API for seamless execution.

---

## Use Cases
**Event Floor Plan Optimization**
- Automatically re-categorize exhibitors based on updated booth requirements or sponsorship tiers.
- Sync floor plan updates across multiple event instances to maintain operational consistency.

**Exhibitor Data Hygiene**
- Identify and merge duplicate category labels to clean up the event database.
- Validate exhibitor category assignments against the master event taxonomy to ensure compliance.

**Operational Efficiency**
- Reduce the time spent on manual floor plan adjustments during the final weeks before an event.
- Generate automated status reports on floor plan coverage and category distribution for stakeholders.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Expo Category Manager template from the solution library.
3. Connect your ExpoFP API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives instructions or triggers for category updates.
- **Agent**: Processes the logic to map exhibitors to categories based on provided metadata.
- **Composio Toolset**: Executes API calls to update the ExpoFP floor plan data.
- **Chat Output**: Confirms the successful mapping and provides a summary of changes.

### 3) Run the Flow
Use the Playground to test your mapping logic:
- `Map all unassigned exhibitors in the 'Tech Expo 2024' floor plan to the 'Software' category.`
- `Clean up category naming conventions for the current floor plan to match the master taxonomy.`
- `Sync the latest exhibitor list with the floor plan and flag any missing category assignments.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the logic engine for classifying exhibitor data.
- Use a clear, instruction-based prompt to define category rules.
- Enable structured output to ensure the agent returns data in the format required by the API.
- Provide a list of allowed categories to prevent the agent from creating unauthorized labels.

### 2) Composio Toolset Node
- Authenticate using your ExpoFP API key to grant the agent permission to modify floor plan data.
- Set the connection scope to allow read/write access to exhibitor and category endpoints.

### 3) Tool Availability
- **Exhibitor Fetcher**: Retrieves current list of exhibitors and their existing metadata.
- **Category Updater**: Pushes updated category assignments back to the ExpoFP platform.
- **Validation Utility**: Checks for mapping conflicts before finalizing updates.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate account intelligence gathering for better exhibitor targeting.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline general operational tasks and data synchronization.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Manage CRM-based account onboarding and data mapping.
