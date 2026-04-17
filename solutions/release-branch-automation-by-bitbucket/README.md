# Release Branch Automation (Uplizd) - Streamline CI/CD pipeline management

## Summary
The Release Branch Automation solution by Uplizd orchestrates the lifecycle of software release branches, enabling engineering teams to automate branch creation, synchronization, and cleanup. By integrating directly with Bitbucket, this workflow eliminates manual overhead, reduces human error in version control, and ensures that release pipelines remain clean and consistent, ultimately accelerating deployment velocity and improving team coordination.

---

## Demo
![Release Branch Automation workflow diagram showing Bitbucket integration and automated branch management](image.png)
**Alt text (SEO-ready):** Release Branch Automation workflow diagram showing Bitbucket integration, automated branch management, and CI/CD pipeline synchronization using Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3181acac-8cbe-5c73-871f-00d2f1627614)

---

## Category
**Primary category:** DevOps automation
**Secondary tags:** bitbucket, ci/cd, release management, git, workflow automation, software engineering, devops, composio
This solution bridges the gap between project management and version control, ensuring your release branches are always in sync with your development lifecycle.

---

## Who is this for?
This solution is designed for engineering and operations teams looking to standardize their release processes.

* **DevOps Engineer**
    * Automates repetitive branch creation and merging tasks to maintain pipeline health.
* **Release Manager**
    * Gains visibility into active release branches and ensures compliance with deployment schedules.
* **Software Developer**
    * Reduces context switching by automating the boilerplate setup of new feature or release branches.
* **Engineering Lead**
    * Enforces consistent branching strategies across the team to prevent integration conflicts.

---

## Features
- **Automated Branch Creation**
    Standardize the naming and initialization of release branches directly from your project requirements.
- **Bitbucket Integration**
    Leverage the Composio Toolset to execute secure, authenticated commands against your Bitbucket repositories.
- **Real-time Sync**
    Automatically update branch status and metadata to keep stakeholders informed of progress.
- **Cleanup Automation**
    Identify and prune stale or merged branches to maintain a clean and manageable repository structure.
- **Pipeline Triggering**
    Seamlessly initiate CI/CD build processes once a new release branch is successfully established.

---

## Use Cases
**Release Lifecycle Management**
* Automating the creation of `release/*` branches based on sprint planning tickets.
* Syncing branch protection rules automatically when a new major release cycle begins.

**Repository Hygiene**
* Identifying and deleting feature branches that have been merged into the main branch for over 30 days.
* Generating automated reports on branch age to prevent "branch sprawl" in large repositories.

**Deployment Coordination**
* Triggering automated notifications in Slack or Jira when a release branch is successfully cut.
* Validating that all required commits are present in the release branch before allowing a merge to production.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Release Branch Automation template from the marketplace.
3. Connect your Bitbucket account via the Composio integration settings.
4. Ensure nodes are correctly mapped (Chat Input → Agent → Composio Toolset → Chat Output) and verify all API credentials are active.

### 2) Setup the Nodes
* **Chat Input**: Receives the release version or branch name from the user.
* **Agent**: Processes the request, determines the necessary Bitbucket actions, and manages the logic flow.
* **Composio Toolset**: Executes the specific Bitbucket API calls to create, list, or delete branches.
* **Chat Output**: Returns the confirmation of the branch operation and the resulting branch URL.

### 3) Run the Flow
Use the Playground to test your automation with prompts like:
* `Create a new release branch named release/v2.4.0 from the develop branch.`
* `List all stale branches in the core-api repository that haven't been updated in 14 days.`
* `Delete the feature branch feature/login-fix-123 after verifying it is merged.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your version control tasks.
* Use a model with strong reasoning capabilities to parse complex branch naming conventions.
* Provide clear instructions on how to handle errors (e.g., if a branch already exists).
* Ensure the agent is instructed to confirm actions before executing destructive tasks like branch deletion.

### 2) Composio Toolset Node
* Provide your Bitbucket API key and ensure the connection scope includes `repository:write` and `pullrequest:write` permissions.

### 3) Tool Availability
* **Branch Management**: Create, delete, and list branches.
* **Repository Metadata**: Fetch repository information and branch status.
* **Commit History**: Retrieve latest commit SHAs for branch validation.

---

## Related Solutions
* [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for job-based workflows.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automated onboarding and configuration for CRM accounts.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) - Intelligent sorting and management of engineering action items.
