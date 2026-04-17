# Data Compliance Auditor (Uplizd) - Automated data retention and regulatory compliance monitoring

## Summary
The Data Compliance Auditor is an intelligent Uplizd workflow designed to automate the enforcement of data retention policies and regulatory standards. By continuously scanning your databases for records that have exceeded their lifecycle or violate privacy mandates, this solution ensures your organization maintains strict data hygiene, reduces storage overhead, and minimizes legal risk through automated, audit-ready cleanup processes.

---

## Demo
![Data Compliance Auditor dashboard showing automated retention policy enforcement and record deletion logs](image.png)
**Alt text (SEO-ready):** Data Compliance Auditor dashboard showing automated retention policy enforcement, record deletion logs, and Uplizd workflow compliance monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9c779999-46b7-586f-9607-b42c9285bcf6)

---

## Category
**Primary category:** Data Governance
**Secondary tags:** compliance, data retention, gdpr, data hygiene, audit, automation, ninox, composio, ai workflow

This solution bridges the gap between complex regulatory requirements and operational data management by providing an automated, AI-driven audit layer for your business systems.

---

## Who is this for?
This solution is designed for teams responsible for maintaining data integrity and meeting strict regulatory obligations.

* **Data Protection Officer (DPO)**
    * Ensures organizational adherence to GDPR, CCPA, and internal data retention policies without manual oversight.
* **Compliance Manager**
    * Maintains an audit-ready state by automating the identification and purging of expired or non-compliant records.
* **Database Administrator**
    * Offloads the burden of routine data cleanup tasks to an intelligent agent, improving system performance and storage efficiency.
* **Legal Operations Lead**
    * Reduces corporate liability by ensuring sensitive information is not retained longer than legally permitted.

---

## Features
- **Automated Policy Enforcement**
    Automatically triggers cleanup workflows based on pre-defined retention schedules and data age thresholds.
- **Regulatory Compliance Mapping**
    Aligns data deletion actions with specific regulatory frameworks like GDPR or HIPAA to ensure legal defensibility.
- **Intelligent Record Identification**
    Uses advanced logic to scan and flag records that violate privacy policies or have reached their end-of-life status.
- **Audit Trail Generation**
    Maintains detailed logs of all compliance actions, providing a transparent record for internal and external audits.
- **Seamless Integration**
    Leverages the Composio Toolset to connect directly with your existing databases and CRM platforms for real-time data management.

---

## Use Cases
**Data Lifecycle Management**
* Automating the deletion of customer records that have been inactive for more than seven years.
* Purging temporary user data files after the completion of a project or service contract.

**Regulatory Privacy Compliance**
* Identifying and removing PII (Personally Identifiable Information) that lacks explicit user consent for long-term storage.
* Ensuring that "Right to be Forgotten" requests are processed across all connected data silos automatically.

**Storage and Performance Optimization**
* Archiving or deleting legacy logs and outdated transaction history to optimize database query performance.
* Reducing cloud storage costs by systematically removing redundant, obsolete, or trivial (ROT) data.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Flow" to add the Data Compliance Auditor template to your workspace.
3. Connect your database credentials within the configuration panel to allow the agent access.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the compliance audit trigger or manual scan request.
* **Agent**: Analyzes the request against defined retention policies and determines the necessary cleanup actions.
* **Composio Toolset**: Executes the specific API calls to query, flag, or delete records in your connected systems.
* **Chat Output**: Provides a summary report of the audit findings and actions taken.

### 3) Run the Flow
Use the Playground to test your compliance workflows:
* `Run a full audit on the customer database for records older than 5 years.`
* `Identify all PII records that lack a consent flag and generate a summary report.`
* `Purge expired project files from the last fiscal year and log the deletion in the audit trail.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the compliance engine, interpreting policy rules and executing data management logic.
* Set the system prompt to prioritize data security and accuracy.
* Use a model capable of structured data reasoning (e.g., GPT-4o or Claude 3.5).
* Configure the instruction pattern to: 1) Analyze input, 2) Verify against policy, 3) Execute cleanup.

### 2) Composio Toolset Node
* Provide your API keys for the target database or CRM (e.g., Ninox, Salesforce).
* Ensure the connection scope includes read/write permissions for the specific tables requiring audit.

### 3) Tool Availability
* **Database Query Tools**: For scanning and retrieving record timestamps.
* **Data Deletion/Archive Tools**: For executing the removal or migration of non-compliant records.
* **Logging/Reporting Tools**: For documenting audit actions into your compliance dashboard.

---

## Related Solutions
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Monitor account status and compliance metrics.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) - Automate the removal of stale or resolved action items.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean and accurate CRM data through automated formatting and deduplication.
