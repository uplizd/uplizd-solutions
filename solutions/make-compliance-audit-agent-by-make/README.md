# Make Compliance Audit Agent (Uplizd) - Automated regulatory data handling and workflow validation

## Summary
The Make Compliance Audit Agent provides an automated governance layer for your Make.com workflows, ensuring that data handling, timezone configurations, and regional compliance standards are strictly maintained. By leveraging the Composio Toolset to inspect active scenarios, this solution helps RevOps and IT teams eliminate manual audit overhead, reduce the risk of data leakage, and maintain a single source of truth for organizational compliance.

---

## Demo
![Make Compliance Audit Agent workflow dashboard showing automated scenario inspection and regulatory validation logs](image.png)
**Alt text (SEO-ready):** Make Compliance Audit Agent dashboard for automated workflow regulatory validation, data handling, and Uplizd compliance monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bd140694-e980-515c-a787-41a75ae27c85)

---

## Category
- **Primary category:** Legal & Compliance
- **Secondary tags:** make, automation, data governance, compliance, workflow audit, risk management, composio, ai workflow
- This solution bridges the gap between technical workflow automation and corporate regulatory requirements through continuous, AI-driven monitoring.

---

## Who is this for?
This agent is designed for teams managing complex automation ecosystems who need to prove compliance without manual intervention.

- **Compliance Officer**
    - Ensures all automated data transfers meet regional privacy standards and internal policy requirements.
- **RevOps Manager**
    - Maintains clean, compliant data pipelines across CRM and marketing automation platforms.
- **IT Systems Administrator**
    - Automates the auditing of workflow configurations to identify and remediate security vulnerabilities.
- **Data Privacy Analyst**
    - Monitors data residency and handling practices to ensure adherence to GDPR, CCPA, or internal security frameworks.

---

## Features
- **Automated Scenario Scanning**
    - Continuously inspects active Make scenarios to detect non-compliant data routing or insecure connection configurations.
- **Regional Compliance Validation**
    - Cross-references workflow settings against defined regional data residency and timezone compliance rules.
- **Real-time Alerting**
    - Triggers immediate notifications when a workflow configuration drifts from established security or compliance baselines.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely interface with Make APIs for deep-dive inspection of scenario metadata.
- **Audit Trail Generation**
    - Automatically compiles comprehensive audit logs for every scan, providing a clear history of compliance status for stakeholders.

---

## Use Cases
**Data Residency Monitoring**
- Verify that customer data is only routed through approved regional servers.
- Flag workflows that inadvertently transmit sensitive PII across restricted geographic boundaries.

**Configuration Hygiene**
- Identify outdated or insecure API connections within Make scenarios that pose a security risk.
- Ensure all automated processes follow standardized naming and error-handling conventions.

**Regulatory Reporting**
- Generate periodic compliance reports to demonstrate adherence to internal data governance policies.
- Provide documentation for third-party audits by logging all automated configuration checks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Make Compliance Audit Agent template file.
3. Connect your Make.com account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the audit trigger or manual request for a compliance scan.
- **Agent**: Processes the request, interprets compliance rules, and decides which workflows to inspect.
- **Composio Toolset**: Executes API calls to retrieve and validate Make scenario configurations.
- **Chat Output**: Delivers the final audit report, highlighting compliant workflows and flagged issues.

### 3) Run the Flow
Use the Playground to test your audit agent with these prompts:
- `Scan all active scenarios in the 'Sales' folder for data residency compliance.`
- `List any Make workflows that have not been audited in the last 30 days.`
- `Check if the 'Lead Enrichment' scenario is configured to handle PII according to GDPR standards.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a governance expert. Use the following instruction pattern:
- Focus on identifying deviations from established compliance schemas.
- Prioritize clear, actionable remediation steps for every flagged workflow.
- Maintain a professional, objective tone suitable for audit documentation.

### 2) Composio Toolset Node
- Provide your Make API Key within the Composio connection settings.
- Ensure the connection scope includes read-access to scenario metadata and connection logs.

### 3) Tool Availability
- `list_scenarios`: Retrieve a list of all workflows in the connected Make account.
- `get_scenario_details`: Fetch specific configuration data for a chosen workflow.
- `log_audit_result`: Record the findings of the compliance check into your reporting system.

---

## Related Solutions
- [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Automated monitoring for web accessibility standards.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) — Audit and manage user permissions across administrative platforms.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the operational status and performance of your automated workflows.
