# Document Compliance Monitor (Uplizd) - Automated permission auditing and document security

## Summary
The Document Compliance Monitor is an intelligent Uplizd workflow designed to automate the auditing of Google Drive document permissions. By leveraging the Composio Toolset to interface with Google Workspace, this solution identifies unauthorized access, enforces security policies, and ensures sensitive files remain compliant with organizational standards, significantly reducing the risk of data leakage and manual oversight.

---

## Demo
![Document Compliance Monitor dashboard showing permission audit results and security alerts](image.png)
**Alt text (SEO-ready):** Document Compliance Monitor dashboard showing permission audit results, security alerts, Google Drive integration, and Uplizd automated compliance workflow.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c51b720b-6996-5bae-af5a-f60dd6d8af6a)

---

## Category
**Primary category:** Data Governance
**Secondary tags:** google drive, compliance, security, audit, data hygiene, automation, composio, ai workflow.
This solution bridges the gap between raw document storage and enterprise-grade security compliance through automated monitoring.

---

## Who is this for?
This solution is designed for teams responsible for maintaining strict data security and regulatory adherence across cloud environments.

* **Compliance Officer**
    * Automates the audit trail for document access to satisfy internal and external regulatory requirements.
* **IT Security Manager**
    * Identifies and remediates over-exposed files or unauthorized external sharing settings in real-time.
* **Operations Lead**
    * Ensures that sensitive project documentation remains restricted to authorized personnel without manual intervention.
* **Data Privacy Analyst**
    * Monitors for potential data leakage by tracking permission changes across large-scale Google Drive directories.

---

## Features
- **Automated Permission Auditing**
  Scans Google Drive folders to detect public or overly permissive document sharing settings.
- **Real-time Security Alerts**
  Triggers notifications when sensitive files are shared with unauthorized domains or external users.
- **Policy Enforcement Engine**
  Automatically reverts unauthorized permission changes to maintain a secure document baseline.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely authenticate and execute commands within Google Workspace.
- **Compliance Reporting**
  Generates structured summaries of document access logs for periodic security reviews and audits.

---

## Use Cases
**Security & Access Control**
- Automatically revoke public access links on files containing restricted keywords or metadata tags.
- Identify and flag files shared with personal email addresses that violate corporate data policies.

**Regulatory Compliance**
- Maintain a continuous audit log of document access for GDPR, HIPAA, or SOC2 compliance reporting.
- Perform bulk audits of folder permissions to ensure adherence to internal data classification standards.

**Operational Hygiene**
- Clean up legacy document permissions by identifying files that haven't been accessed by authorized users in over 90 days.
- Standardize access levels across departmental folders to prevent "permission creep" as teams evolve.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Document Compliance Monitor template from the solution library.
3. Connect your Google Drive account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the trigger command or manual audit request.
* **Agent**: Processes security logic and evaluates file permission metadata.
* **Composio Toolset**: Executes API calls to fetch and update Google Drive file permissions.
* **Chat Output**: Returns the audit summary and confirmation of any security actions taken.

### 3) Run the Flow
Use the Playground to test your compliance monitor with these prompts:
`"Scan my 'Finance' folder for any files shared with users outside the organization."`
`"List all documents that currently have public link sharing enabled."`
`"Revoke all external edit permissions for files in the 'Q4 Strategy' folder."`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security auditor, interpreting file metadata and applying governance rules.
* Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
* Instruction: "You are a security auditor. Analyze file permissions, identify violations based on provided policy, and execute remediation only when confirmed."
* Ensure the agent is configured to output clear, human-readable audit reports.

### 2) Composio Toolset Node
* Requires a valid Google Drive API key/OAuth connection configured within Composio.
* Ensure the connection scope includes `drive.metadata.readonly` and `drive.file` permissions to perform audits and updates.

### 3) Tool Availability
* `google_drive_list_files`: To scan directory contents.
* `google_drive_get_permissions`: To retrieve current access levels for specific files.
* `google_drive_update_permissions`: To revoke or modify access as required by the security policy.

---

## Related Solutions
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Automated monitoring of account health and security compliance.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Auditing user permissions and administrative access levels.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitoring the operational status and health of automated workflows.
