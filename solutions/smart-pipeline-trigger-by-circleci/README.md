# Smart Pipeline Trigger (Uplizd) - Automated CI/CD orchestration based on code and business logic

## Summary
The Smart Pipeline Trigger (Uplizd) solution automates CI/CD workflows by intelligently monitoring code changes and applying business-defined rules to initiate deployments. This workflow eliminates manual intervention in the release process, ensuring that pipeline velocity is maintained while enforcing strict deployment hygiene and reducing human error in complex software delivery environments.

---

## Demo
![Smart Pipeline Trigger workflow diagram showing code change detection and CircleCI integration](image.png)
**Alt text (SEO-ready):** Smart Pipeline Trigger (Uplizd) workflow for automated CI/CD orchestration, code change monitoring, and CircleCI pipeline integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/0205f7bb-5ac8-5375-b1e7-00ee357161a3)

---

## Category
*   **Primary category:** DevOps automation
*   **Secondary tags:** ci/cd, circleci, workflow automation, deployment, pipeline, devops, software delivery, composio
*   This solution bridges the gap between code repository events and CI/CD execution, providing a smart layer for intelligent deployment management.

---

## Who is this for?
This solution is designed for technical teams looking to optimize their release cycles and maintain high-quality deployment standards.

*   **DevOps Engineer**
    *   Automates repetitive pipeline triggers to focus on infrastructure stability and scaling.
*   **Software Architect**
    *   Ensures deployment logic adheres to organizational standards and release governance.
*   **Engineering Manager**
    *   Increases team velocity by reducing the time spent on manual deployment coordination.
*   **QA Lead**
    *   Ensures that automated tests are triggered consistently based on specific code change criteria.

---

## Features
- **Intelligent Change Detection**
  Analyzes incoming code commits or pull requests to determine if a pipeline trigger is necessary based on defined business logic.
- **CircleCI Integration**
  Leverages the Composio Toolset to securely communicate with CircleCI, enabling real-time pipeline initiation and status tracking.
- **Customizable Trigger Rules**
  Allows users to define specific conditions (e.g., branch names, file paths, or commit messages) that must be met before a deployment starts.
- **Automated Workflow Orchestration**
  Connects the Chat Input to the Agent, which evaluates the context and executes the appropriate CI/CD tool commands.
- **Real-time Execution Feedback**
  Provides immediate status updates and logs through the Chat Output node, keeping the team informed of deployment progress.

---

## Use Cases
**Automated Environment Deployment**
*   Trigger staging deployments automatically when code is merged into the `develop` branch.
*   Initiate production hotfix pipelines based on specific commit tag patterns.

**Conditional Testing Workflows**
*   Run full integration test suites only when core service files are modified.
*   Skip resource-heavy pipelines if changes are limited to documentation or non-functional assets.

**Release Governance**
*   Enforce manual approval gates within the pipeline trigger logic for sensitive production releases.
*   Sync deployment status updates back to project management tools for full visibility.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Pipeline Trigger template from the marketplace.
3. Configure your environment variables for CircleCI and your VCS provider.
4. Ensure nodes are correctly wired: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the trigger event or manual command to start the pipeline.
*   **Agent**: Processes the logic and determines if the CI/CD criteria are satisfied.
*   **Composio Toolset**: Executes the authenticated API calls to CircleCI.
*   **Chat Output**: Returns the deployment status or error logs to the user.

### 3) Run the Flow
Use the Playground to test your triggers:
*   `Trigger pipeline for branch feature/login-fix`
*   `Check status of the latest build for project-alpha`
*   `Run production deployment for commit hash a1b2c3d`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine that interprets trigger requests.
*   Use a model with strong reasoning capabilities (e.g., GPT-4o).
*   Provide clear instructions on the hierarchy of deployment rules.
*   Ensure the agent has access to the latest repository metadata.

### 2) Composio Toolset Node
*   Provide your CircleCI API key within the Composio configuration.
*   Set the connection scope to include read/write access for pipeline triggering.

### 3) Tool Availability
*   **CircleCI Actions**: Trigger pipeline, Get build status, List recent workflows.
*   **VCS Connectors**: Fetch commit details, Validate branch status.

---

## Related Solutions
*   [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor the operational health of your automated workflows.
*   [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) — Automate administrative tasks and user provisioning.
*   [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Perform security audits and compliance checks on your infrastructure.
