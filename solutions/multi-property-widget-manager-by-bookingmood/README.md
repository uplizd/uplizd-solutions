# Multi-Property Widget Manager (Uplizd) - Centralized booking widget deployment and configuration

## Summary
The Multi-Property Widget Manager is an intelligent Uplizd workflow designed to streamline the deployment, updates, and synchronization of booking widgets across diverse property portfolios. By leveraging the Composio Toolset, this solution eliminates manual configuration errors, ensures consistent branding across all booking interfaces, and provides a single source of truth for property-specific widget settings, significantly reducing operational overhead for property managers and digital teams.

---

## Demo
![Multi-Property Widget Manager workflow showing automated deployment of booking widgets across multiple property dashboards](image.png)
**Alt text (SEO-ready):** Multi-Property Widget Manager (Uplizd) workflow for automated booking widget deployment, property management, and CRM integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1035478a-9773-5131-ab5e-1186ad08f34a)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** booking, widget management, property management, automation, multi-site, workflow, composio, scheduling
- This solution enables seamless, automated management of booking widgets across multiple properties to ensure consistent user experiences and efficient scheduling operations.

---

## Who is this for?
This solution is designed for teams managing multiple booking interfaces who need to maintain high standards of operational efficiency.

- **Property Managers**
    - Automate the deployment of booking widgets to new properties without manual configuration.
- **Operations Leads**
    - Maintain a centralized view of widget performance and settings across the entire portfolio.
- **Digital Marketing Managers**
    - Ensure consistent branding and conversion tracking across all booking touchpoints.
- **Support Specialists**
    - Quickly troubleshoot widget availability and booking issues for specific properties.

---

## Features
- **Centralized Deployment**
    - Push standardized widget configurations to multiple properties simultaneously via automated workflows.
- **Real-time Sync**
    - Ensure booking availability and widget settings are updated instantly across all connected platforms.
- **Intelligent Error Handling**
    - Automatically detect and report configuration mismatches or deployment failures across property dashboards.
- **Composio-Powered Integration**
    - Utilize robust toolsets to interface directly with booking platforms and property management systems.
- **Scalable Architecture**
    - Easily add or remove properties from the management pipeline without disrupting existing booking flows.

---

## Use Cases
**Portfolio Expansion**
- Automatically provision booking widgets for new properties added to the management system.
- Sync global branding updates to every property widget in a single click.

**Operational Maintenance**
- Audit current widget versions across all properties to ensure compliance with company standards.
- Re-sync booking availability windows for properties undergoing seasonal schedule changes.

**Performance Monitoring**
- Track widget interaction rates across different property locations to identify high-performing assets.
- Automate alerts for properties where the booking widget is detected as offline or misconfigured.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your required booking and property management platform connections.
4. Ensure nodes are correctly mapped to your specific property IDs and API endpoints.

### 2) Setup the Nodes
- **Chat Input**: Receives commands for widget updates or property-specific configuration requests.
- **Agent**: Processes intent, validates property data, and orchestrates the deployment logic.
- **Composio Toolset**: Executes the API calls to update or verify widget settings on external platforms.
- **Chat Output**: Returns a confirmation summary of the deployment status or highlights any errors encountered.

### 3) Run the Flow
Use the Playground to test your widget management:
- `Update the booking widget theme for all properties in the 'Coastal' portfolio to 'Summer-2024'.`
- `Check the status of booking widgets for property IDs 501, 502, and 503.`
- `Deploy the standard booking widget configuration to the new property added to the system.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central controller for all widget management tasks.
- **Recommended instruction pattern:**
    - Act as a property operations assistant focused on widget deployment and maintenance.
    - Always verify property IDs before executing configuration changes.
    - Provide clear, concise summaries of successful deployments and detailed logs for any failures.

### 2) Composio Toolset Node
- **API Key**: Ensure your platform-specific API keys are securely stored in the Composio environment.
- **Connection Scope**: Grant the agent read/write access to your booking platform's widget settings and property management APIs.

### 3) Tool Availability
- **Widget Update Tool**: Allows the agent to push new settings or themes to specific property widgets.
- **Property Query Tool**: Enables the agent to fetch current configuration states for audit purposes.
- **Status Reporting Tool**: Provides the agent with the ability to summarize deployment outcomes to the user.

---

## Related Solutions
- [Widget Experience Optimizer](../widget-experience-optimizer-by-productlane/README.md) — Enhance user engagement through data-driven widget adjustments.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Streamline general operations and task management across your business.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the onboarding and configuration of new accounts and properties.
