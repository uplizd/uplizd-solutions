# Space Governance Agent (Uplizd) - Automate Contentful space structure and naming standards

## Summary
The Space Governance Agent is an intelligent workflow designed to enforce organizational naming conventions and maintain structural integrity across your Contentful environment. By automating the audit and cleanup of content spaces, this solution ensures your digital asset management remains scalable, compliant, and easy to navigate for cross-functional teams, reducing manual oversight and preventing configuration drift.

---

## Demo
![Space Governance Agent workflow diagram showing Contentful integration for automated naming compliance and space auditing.](image.png)
**Alt text (SEO-ready):** Space Governance Agent for Contentful, automated naming standards enforcement, Uplizd workflow, Contentful API integration, and digital asset management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ab79a24d-14f6-53a8-8d1d-785b3ce16eb8)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** contentful, governance, data hygiene, automation, cms, digital asset management, composio, ai workflow.
This solution bridges the gap between creative content production and technical infrastructure management by automating governance policies within Contentful.

---

## Who is this for?
This agent is built for teams managing complex content architectures who need to maintain consistency at scale.

- **Content Operations Manager**
    - Ensures all new spaces adhere to strict naming conventions and organizational hierarchies.
- **CMS Administrator**
    - Automates the identification and remediation of non-compliant space configurations.
- **Digital Asset Lead**
    - Maintains a single source of truth for asset organization, improving retrieval and collaboration.
- **IT Compliance Officer**
    - Monitors space settings to ensure they meet internal security and structural governance standards.

---

## Features
- **Automated Naming Enforcement**
    - Automatically flags or renames spaces that deviate from established organizational naming patterns.
- **Structural Integrity Audits**
    - Performs real-time scans of Contentful spaces to verify that required settings and metadata fields are present.
- **Cross-Platform Sync**
    - Uses the Composio Toolset to bridge Contentful data with other operational tools for unified reporting.
- **Proactive Drift Detection**
    - Identifies unauthorized changes to space configurations immediately, allowing for rapid remediation.
- **Custom Governance Rules**
    - Allows users to define specific logic for what constitutes a "compliant" space, tailored to unique business needs.

---

## Use Cases
**Standardization & Compliance**
- Automatically rename new spaces to match the corporate `Project-Region-Type` naming schema.
- Flag spaces that lack mandatory description tags or owner metadata for immediate review.

**Operational Efficiency**
- Audit hundreds of existing spaces in minutes to identify legacy structures that need updating.
- Sync space status updates to internal dashboards to keep stakeholders informed of infrastructure health.

**Scalability & Maintenance**
- Prevent the creation of duplicate or "shadow" spaces by validating requests against existing records.
- Automate the archival process for spaces that have exceeded their project lifecycle duration.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the template in your workspace.
2. Connect your Contentful API credentials within the integration settings.
3. Configure the trigger settings to define how often the governance scan should run.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the governance trigger or manual audit request.
- **Agent**: Processes instructions to evaluate space compliance against defined rules.
- **Composio Toolset**: Executes API calls to Contentful to fetch, update, or audit space metadata.
- **Chat Output**: Returns a summary report of findings and any automated actions taken.

### 3) Run the Flow
Use the Playground to test your governance rules:
- `Audit all spaces and report any that do not follow the naming convention.`
- `Find all spaces created in the last 30 days and verify they have the required owner tags.`
- `List all spaces that are currently missing a description and suggest a standard format.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the governance engine, interpreting your compliance policies.
- Focus on strict adherence to the provided naming schema.
- Prioritize clear, actionable reporting for any identified non-compliant spaces.
- Maintain a neutral, professional tone when suggesting structural changes.

### 2) Composio Toolset Node
- Provide your Contentful API Key and ensure the connection scope includes `Space Management` and `Content Read/Write` permissions.

### 3) Tool Availability
- **Space Discovery**: List and retrieve metadata for all spaces in the organization.
- **Metadata Update**: Modify space names, descriptions, and tags.
- **Audit Logging**: Export findings to a structured format for external review.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Monitor and audit account-level configurations across your infrastructure.
- [Accessibility Audit Assistant](../accessibility-audit-assistant-by-figma/README.md) — Ensure design and content assets meet compliance standards.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the operational status and efficiency of your automated processes.
