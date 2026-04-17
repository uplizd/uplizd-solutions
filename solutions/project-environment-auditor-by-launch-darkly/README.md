# Project Environment Auditor (Uplizd) - Automated LaunchDarkly configuration and compliance monitoring

## Summary
The Project Environment Auditor is an intelligent Uplizd workflow designed to scan, audit, and report on LaunchDarkly project configurations across multiple environments. By leveraging the Composio Toolset to interface with LaunchDarkly APIs, this solution ensures environment consistency, identifies drift in feature flag settings, and maintains high-velocity deployment hygiene for engineering and DevOps teams.

---

## Demo
![Project Environment Auditor dashboard showing feature flag drift analysis and environment configuration report](image.png)
**Alt text (SEO-ready):** Project Environment Auditor dashboard showing feature flag drift analysis and environment configuration report for LaunchDarkly, Uplizd AI workflow, and automated DevOps compliance.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c4f46804-99e5-5ac7-ac8d-4dd698c6ae4f)

---

## Category
**Primary category:** DevOps automation  
**Secondary tags:** launchdarkly, feature flags, compliance, environment audit, drift detection, devops, composio, ai workflow  
This solution streamlines infrastructure governance by automating the verification of feature flag states and project settings across complex development environments.

---

## Who is this for?
This solution is designed for technical teams managing large-scale feature flag deployments who need to maintain strict environment parity.

- **DevOps Engineer**
    - Automates the detection of configuration drift between staging and production environments to prevent deployment failures.
- **Engineering Manager**
    - Gains visibility into feature flag usage and project health without manual dashboard navigation.
- **Security Compliance Officer**
    - Ensures that all feature flag configurations adhere to internal security policies and access controls.
- **QA Lead**
    - Verifies that environment-specific flag overrides are correctly applied before triggering automated test suites.

---

## Features
- **Automated Environment Scanning**
  Real-time retrieval of project configurations across all defined LaunchDarkly environments.
- **Drift Detection Engine**
  Intelligent comparison logic that highlights discrepancies in flag settings between target environments.
- **Compliance Reporting**
  Generates structured summaries of flag states, ensuring adherence to organizational deployment standards.
- **Composio-Powered Integration**
  Seamless API connectivity to LaunchDarkly, enabling secure and authenticated read/write operations.
- **Actionable Insights**
  Provides clear, natural language recommendations for remediating configuration inconsistencies.

---

## Use Cases
**Environment Parity Audits**
- Automatically compare feature flag states between 'Production' and 'Staging' to identify missing configurations.
- Generate a delta report of flag variations to ensure consistent behavior across global deployment regions.

**Compliance and Governance**
- Audit flag access levels to ensure only authorized service accounts have modification permissions.
- Maintain a historical log of configuration changes for internal security and audit requirements.

**Deployment Hygiene**
- Identify stale or unused feature flags that have remained in a specific state for extended periods.
- Validate that mandatory environment-level overrides are correctly configured for new feature releases.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Project Environment Auditor template from the solution library.
3. Connect your LaunchDarkly API credentials within the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's audit request or environment scope.
- **Agent**: Processes the request and determines which LaunchDarkly API endpoints to query.
- **Composio Toolset**: Executes secure API calls to fetch project, environment, and flag data.
- **Chat Output**: Formats the audit findings into a readable, actionable report.

### 3) Run the Flow
Use the Playground to test your auditor with these prompts:
- `Audit the 'Production' environment and list all flags that differ from 'Staging'.`
- `Generate a compliance report for the 'Mobile-App' project.`
- `Identify any stale feature flags in the 'Development' environment that haven't been updated in 30 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a technical auditor capable of interpreting API JSON responses.
- **Recommended instruction pattern:**
    - "You are a DevOps auditor; analyze the provided LaunchDarkly configuration data for inconsistencies."
    - "Always prioritize identifying environment drift and flag state mismatches."
    - "Format all outputs as clear, bulleted reports with actionable remediation steps."

### 2) Composio Toolset Node
- **API Key**: Ensure your LaunchDarkly Personal Access Token (PAT) is configured with read-only or read-write permissions as required.
- **Connection Scope**: Limit the scope to the specific projects and environments you intend to audit.

### 3) Tool Availability
- **List Projects**: Retrieve all available projects in the account.
- **Get Environment Flags**: Fetch the current status of flags within a specific environment.
- **Compare Environments**: Execute cross-environment analysis for drift detection.

---

## Related Solutions
- [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automates security and configuration audits for Cloudflare infrastructure.
- [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Tracks and reports on the operational status of automated team workflows.
- [Admin User Access Auditor by Storeganise](../admin-user-access-auditor-by-storeganise/README.md) - Audits user permissions and access levels across administrative platforms.
