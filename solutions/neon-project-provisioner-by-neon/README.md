# Neon Project Provisioner (Uplizd) - Automated Postgres infrastructure and branch management

## Summary
The Neon Project Provisioner is an intelligent Uplizd workflow designed to automate the lifecycle of Postgres database environments. By leveraging the Composio Toolset to interface with Neon’s API, this solution enables developers and DevOps engineers to programmatically provision projects, manage database branches, and configure environment settings, significantly reducing manual overhead and ensuring consistent infrastructure deployment across development pipelines.

---

## Demo
![Neon Project Provisioner workflow showing automated Postgres branch creation and environment configuration via Composio](image.png)
**Alt text (SEO-ready):** Neon Project Provisioner workflow for automated Postgres database management, branch provisioning, and cloud infrastructure synchronization using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/46a8ef05-e943-5df0-abe6-4bed24fbfe75)

---

## Category
**Primary category:** Data infrastructure automation
**Secondary tags:** postgres, neon, database, devops, cloud infrastructure, automation, composio, api integration
This solution streamlines database lifecycle management, allowing teams to treat their Postgres infrastructure as code through automated provisioning workflows.

---

## Who is this for?
This solution is built for engineering teams looking to eliminate manual database configuration bottlenecks.

*   **DevOps Engineers**
    *   Automate the creation of ephemeral database environments for CI/CD pipelines.
*   **Backend Developers**
    *   Instantly provision isolated Postgres branches for feature testing and debugging.
*   **Engineering Managers**
    *   Standardize database environment setup to ensure consistency across development teams.
*   **Platform Architects**
    *   Integrate database lifecycle management directly into existing internal developer platforms.

---

## Features
- **Automated Project Provisioning**
  Seamlessly create new Neon Postgres projects via API, reducing setup time from minutes to seconds.
- **Dynamic Branch Management**
  Programmatically create, list, and delete database branches to support parallel feature development.
- **Environment Configuration**
  Apply custom settings and connection parameters during the provisioning process to match specific application requirements.
- **Composio-Powered Integration**
  Utilizes the robust Composio Toolset to securely authenticate and execute complex Neon API operations.
- **Real-time Status Monitoring**
  Receive immediate feedback on provisioned resources, ensuring infrastructure state is always synchronized with the workflow.

---

## Use Cases
**CI/CD Pipeline Integration**
*   Automatically spin up a fresh Postgres branch for every new pull request.
*   Tear down temporary database branches upon successful merge to optimize resource usage.

**Development Workflow Optimization**
*   Provision isolated database environments for local development testing without manual console interaction.
*   Sync schema changes across multiple development branches using automated provisioning scripts.

**Infrastructure-as-Code (IaC) Automation**
*   Trigger project creation based on external events or webhooks from your project management tools.
*   Maintain a standardized naming convention and configuration template for all new database projects.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Neon Project Provisioner template from the solutions library.
3. Connect your Neon API credentials within the Composio Toolset integration settings.
4. Ensure nodes are correctly wired: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the user request for project or branch creation.
*   **Agent**: Processes the intent and maps it to the appropriate Neon API call.
*   **Composio Toolset**: Executes the authenticated request against the Neon infrastructure.
*   **Chat Output**: Returns the connection string and project status to the user.

### 3) Run the Flow
Use the Playground to test your provisioning logic:
*   `Create a new Neon project named 'staging-db-v1' in the 'us-east-1' region.`
*   `Create a new database branch for project 'my-app' based on the 'main' branch.`
*   `List all active database branches for the project 'production-api' and provide their connection strings.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between user intent and API execution.
*   Use a model capable of structured JSON output for reliable API parameter mapping.
*   Ensure the system prompt emphasizes strict adherence to Neon API schema requirements.
*   Enable tool-calling capabilities to allow the agent to invoke the Composio Toolset dynamically.

### 2) Composio Toolset Node
*   Requires a valid Neon API Key provided via the Composio dashboard.
*   Scope the connection to allow project-level read/write permissions for secure operations.

### 3) Tool Availability
*   `neon_create_project`: Provision new Postgres instances.
*   `neon_create_branch`: Generate new branches from existing project snapshots.
*   `neon_list_branches`: Retrieve metadata and status for existing database branches.
*   `neon_delete_branch`: Clean up temporary environments to manage costs.

---

## Related Solutions
*   [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamline user and account onboarding processes.
*   [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Manage complex task sequences across multiple platforms.
*   [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) - Automate cloud infrastructure and network zone deployments.
