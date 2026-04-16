# Client Portal Generator (Uplizd) - Automated creation of branded client hubs and project tracking

## Summary
The Client Portal Generator (Uplizd) is an automated workflow that streamlines the creation of personalized, branded client portals using Coda. By integrating document management with project tracking, this solution enables teams to deliver a professional, single source of truth for client interactions, reducing manual setup time and ensuring consistent project visibility.

---

## Demo
![Client Portal Generator workflow showing Coda integration for automated document and project tracking setup](image.png)
**Alt text (SEO-ready):** Client Portal Generator workflow by Uplizd, automating branded client hubs and project tracking via Coda and Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/3ec2cf27-31dc-5e21-9984-3811719e37b8)

---

## Category
**Primary category:** Operations
**Secondary tags:** coda, client portal, project management, document automation, workflow automation, crm, client success, composio.
This solution bridges the gap between client relationship management and project delivery by automating the instantiation of collaborative workspaces.

---

## Who is this for?
This solution is designed for teams looking to standardize their client onboarding and project communication processes.

- **Account Managers**
    - Automate the creation of personalized portals to keep clients updated without manual document drafting.
- **Project Managers**
    - Ensure project milestones and documentation are centralized in a single, accessible hub for every client.
- **Operations Leads**
    - Standardize the client experience across the organization by enforcing consistent portal templates.
- **Customer Success Managers**
    - Provide clients with real-time visibility into project health and deliverables, increasing transparency and retention.

---

## Features
- **Automated Portal Provisioning**
    - Instantly generate new Coda-based client portals from predefined templates, ensuring brand consistency.
- **Dynamic Content Sync**
    - Automatically populate portals with relevant project data, timelines, and documentation using the Composio Toolset.
- **Centralized Project Tracking**
    - Embed live project status trackers directly into the client-facing interface for real-time reporting.
- **Branded Documentation Hub**
    - Aggregate meeting notes, project briefs, and deliverables into a professional, easy-to-navigate portal structure.
- **Seamless CRM Integration**
    - Connect portal data directly to your CRM to maintain a unified view of client interactions and project history.

---

## Use Cases
**Client Onboarding**
- Automatically generate a "Welcome Portal" for new clients containing project scope, team contacts, and initial documentation.
- Sync onboarding checklists from your CRM to the new portal to track progress in real-time.

**Project Delivery**
- Create dedicated project hubs that update automatically as tasks are completed in your management software.
- Share milestone reports and status updates directly within the portal, eliminating the need for manual email status reports.

**Client Reporting**
- Provide a persistent link for clients to view historical project data, past deliverables, and future roadmap items.
- Automate the generation of summary reports for monthly business reviews, hosted directly within the portal.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Coda account via the Composio Toolset connection.
4. Ensure nodes are correctly mapped and the API triggers are active before deploying.

### 2) Setup the Nodes
- **Chat Input**: Receives client details and project requirements from the user.
- **Agent**: Interprets the request and orchestrates the portal creation logic.
- **Composio Toolset**: Executes the Coda API calls to build the portal and populate data.
- **Chat Output**: Confirms portal creation and provides the direct access link to the user.

### 3) Run the Flow
Use the Playground to test your portal generation:
- `Create a new client portal for 'Acme Corp' using the standard project template.`
- `Generate a client portal for 'Global Tech' and include the Q3 project roadmap.`
- `Setup a new portal for 'Beta Solutions' and link the existing project tracker.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for portal structure and data mapping.
- Use a clear, instruction-based prompt to define the portal template structure.
- Ensure the agent has access to the specific Coda document IDs required for templating.
- Configure the agent to validate input data (e.g., client name, project scope) before triggering creation.

### 2) Composio Toolset Node
- Provide your Coda API key within the Composio Toolset node configuration.
- Set the connection scope to allow the agent to read and write to your Coda workspaces.

### 3) Tool Availability
- **Coda API**: For document creation, table updates, and row insertion.
- **Data Mapper**: To ensure information from the Chat Input is correctly formatted for Coda fields.
- **Notification Service**: To alert the user once the portal is successfully generated.

---

## Related Solutions
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamlines the initial configuration of new client accounts in your CRM.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Automates complex operational tasks and project handoffs.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) - Tracks and manages deep-level client relationship data and touchpoints.
