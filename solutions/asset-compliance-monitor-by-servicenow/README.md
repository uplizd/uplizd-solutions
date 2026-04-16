# Asset Compliance Monitor (Uplizd) - Automated IT asset auditing and regulatory adherence

## Summary
The Asset Compliance Monitor is an intelligent Uplizd workflow that automates the tracking, verification, and reporting of IT assets against organizational and regulatory standards. By leveraging the ServiceNow integration, this solution ensures continuous compliance, reduces manual audit overhead, and maintains a single source of truth for all hardware and software inventory, ultimately driving operational hygiene and minimizing security risks.

---

## Demo
![Asset Compliance Monitor workflow dashboard showing real-time ServiceNow asset status and compliance alerts](../image.png)
**Alt text (SEO-ready):** Asset Compliance Monitor Uplizd workflow for ServiceNow IT asset management, regulatory compliance tracking, and automated audit reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6056f757-fb43-5d3d-b403-0d94d709dc62)

---

## Category
- **Primary category:** IT Operations & Compliance
- **Secondary tags:** servicenow, asset management, compliance, it audit, data hygiene, automated reporting, risk mitigation, composio
- This solution bridges the gap between raw IT asset data and regulatory requirements by automating the monitoring and validation process.

---

## Who is this for?
This solution is designed for IT and security teams responsible for maintaining infrastructure integrity and audit readiness.

- **IT Asset Manager**
    - Automates the reconciliation of hardware and software inventory against procurement records.
- **Compliance Officer**
    - Generates real-time audit reports to ensure adherence to internal and external regulatory frameworks.
- **Security Operations Analyst**
    - Identifies non-compliant assets that pose potential security vulnerabilities or policy violations.
- **System Administrator**
    - Reduces manual ticket creation by automating the identification and flagging of out-of-compliance assets.

---

## Features
- **Real-time ServiceNow Integration**
    - Seamlessly connects with ServiceNow to pull and update asset data in real-time via the Composio Toolset.
- **Automated Compliance Auditing**
    - Continuously scans asset metadata against defined policy rules to detect drift or unauthorized changes.
- **Intelligent Alerting**
    - Triggers proactive notifications when assets fall out of compliance, allowing for immediate remediation.
- **Centralized Reporting**
    - Consolidates audit findings into actionable summaries, providing a clear view of organizational risk.
- **Policy-Driven Remediation**
    - Enables the agent to suggest or execute corrective actions based on predefined organizational compliance standards.

---

## Use Cases
**Asset Lifecycle Management**
- Automatically flag assets that have exceeded their expected lifecycle or warranty period.
- Verify that all newly provisioned hardware is correctly tagged and assigned to the appropriate cost center.

**Regulatory Audit Preparation**
- Generate comprehensive compliance reports for internal and external auditors with a single prompt.
- Identify missing documentation or configuration settings required for SOC2 or ISO compliance.

**Security & Risk Mitigation**
- Detect unauthorized software installations that violate corporate security policies.
- Monitor for missing security patches on critical assets to prevent potential vulnerabilities.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Asset Compliance Monitor template from the solution library.
3. Connect your ServiceNow instance via the Composio Toolset integration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding asset status or compliance reports.
- **Agent**: Processes instructions and evaluates asset data against compliance rules.
- **Composio Toolset**: Executes API calls to ServiceNow to fetch asset details and update records.
- **Chat Output**: Delivers clear, formatted compliance summaries and remediation recommendations.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Check the compliance status of all assets assigned to the Engineering department.`
- `List all assets that have missing security tags or are overdue for an audit.`
- `Generate a summary report of non-compliant assets and suggest remediation steps.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary logic engine for interpreting compliance policies and ServiceNow data.
- Use a high-reasoning model to ensure accurate interpretation of complex audit logs.
- Set the system prompt to prioritize security-first language and strict adherence to compliance standards.
- Enable tool-calling capabilities to allow the agent to query ServiceNow dynamically.

### 2) Composio Toolset Node
- Provide your ServiceNow API credentials within the Composio dashboard.
- Ensure the connection scope includes read/write access to the `cmdb_ci` (Configuration Item) tables.

### 3) Tool Availability
- `servicenow_get_asset_details`: Fetches specific hardware/software metadata.
- `servicenow_list_non_compliant_assets`: Filters assets based on compliance flags.
- `servicenow_update_asset_record`: Applies remediation actions or status updates.
- `servicenow_generate_audit_log`: Compiles activity history for reporting purposes.

---

## Related Solutions
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Ensures account data remains compliant and healthy.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Audits user permissions and access rights across systems.
- [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) - Monitors and alerts on organizational risk factors.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) - Automates the matching and reconciliation of financial records.
