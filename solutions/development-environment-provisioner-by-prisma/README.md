# Development Environment Provisioner (Uplizd) - Automated database setup for engineering teams

## Summary
The Development Environment Provisioner (Uplizd) automates the lifecycle of database provisioning, allowing engineering teams to spin up isolated, ready-to-code environments instantly. By integrating directly with Prisma and cloud infrastructure, this workflow eliminates manual configuration bottlenecks, ensures environment consistency across the team, and accelerates pipeline velocity for new feature development.

---

## Demo
![Development Environment Provisioner workflow showing automated database schema deployment and environment configuration](image.png)
**Alt text (SEO-ready):** Development Environment Provisioner workflow in Uplizd showing automated database schema deployment, Prisma integration, and cloud environment configuration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b6435ba8-4090-5200-8856-e88c5dc0bf00)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** devops, prisma, database, environment provisioning, automation, infrastructure as code, composio, ai workflow
- This solution streamlines technical operations by automating the complex task of database and environment setup for developers.

---

## Who is this for?
This solution is designed for technical teams looking to reduce environment setup friction and maintain infrastructure parity.

- **Software Engineer**
  - Reduces time spent on local environment configuration and database migrations.
- **DevOps Engineer**
  - Ensures consistent environment standards across the entire development lifecycle.
- **Engineering Manager**
  - Increases team velocity by eliminating wait times for environment provisioning.
- **QA Specialist**
  - Provides clean, isolated database instances for reliable and repeatable testing.

---

## Features
- **Automated Schema Deployment**
  - Leverages Prisma to automatically push database schemas to new environments, ensuring structural integrity.
- **Isolated Environment Creation**
  - Provisions dedicated, sandboxed database instances to prevent cross-environment data contamination.
- **Composio-Powered Orchestration**
  - Utilizes the Composio Toolset to bridge the gap between AI intent and cloud infrastructure APIs.
- **Real-time Configuration Sync**
  - Automatically updates environment variables and connection strings for seamless application integration.
- **Infrastructure Consistency**
  - Enforces standardized environment configurations, reducing "it works on my machine" issues.

---

## Use Cases
**New Feature Development**
- Automatically provision a fresh database instance when a new feature branch is created.
- Sync the latest schema changes to the development database without manual intervention.

**Automated Testing Pipelines**
- Spin up ephemeral database environments for CI/CD pipelines to run integration tests.
- Tear down temporary environments after test completion to optimize cloud resource usage.

**Onboarding and Training**
- Provide new team members with a pre-configured environment in minutes rather than hours.
- Standardize the development setup process for all incoming engineering talent.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution template.
2. Select "Import" to add the Development Environment Provisioner to your Uplizd workspace.
3. Connect your cloud provider and Prisma credentials within the integration settings.
4. Ensure nodes are correctly linked from the Chat Input through the Agent and Composio Toolset to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the environment provisioning request and project specifications.
- **Agent**: Interprets the request and determines the necessary infrastructure actions.
- **Composio Toolset**: Executes the specific API calls to provision databases and update configurations.
- **Chat Output**: Confirms successful environment setup and provides connection details to the user.

### 3) Run the Flow
Use the Playground to test your provisioning workflow:
- `Provision a new staging database for the 'user-auth' service using the latest schema.`
- `Setup a development environment for the 'billing-api' project with PostgreSQL.`
- `Update the environment variables for the 'frontend-app' to point to the new database instance.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for infrastructure tasks.
- Use a model with strong reasoning capabilities to parse complex environment requirements.
- Instruct the agent to prioritize security and environment isolation in its provisioning logic.
- Maintain a strict mapping between user-requested services and infrastructure resource tags.

### 2) Composio Toolset Node
- Provide a valid API key with permissions to manage your cloud infrastructure and database services.
- Configure the connection scope to include only the necessary resources for environment provisioning.

### 3) Tool Availability
- **Cloud Infrastructure API**: For creating and managing database instances.
- **Prisma CLI/API**: For schema migration and database structural updates.
- **Environment Manager**: For injecting credentials and connection strings into application services.

---

## Related Solutions
- [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automates CRM account creation and configuration.
- [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Streamlines business process automation and task management.
- [Workspace Setup Optimizer by Clockify](../workspace-setup-optimizer-by-clockify/README.md) - Configures team workspaces for improved time tracking and productivity.
