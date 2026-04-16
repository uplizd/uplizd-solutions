# Asset Privacy Guardian (Uplizd) - Automated Data Discovery and Privacy Risk Assessment

## Summary
The Asset Privacy Guardian is an automated Uplizd workflow designed to scan, identify, and assess privacy risks across your digital infrastructure. By leveraging the Borneo integration, this solution provides security teams and data privacy officers with real-time visibility into sensitive data assets, ensuring compliance and minimizing exposure through proactive risk monitoring.

---

## Demo
![Asset Privacy Guardian workflow showing data discovery, risk scanning, and privacy report generation](image.png)
**Alt text (SEO-ready):** Asset Privacy Guardian Uplizd workflow for automated data discovery, privacy risk assessment, and security compliance monitoring using Borneo.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8111edad-0492-540a-97dc-10a77790d317)

---

## Category
- **Primary category:** Data Privacy & Security
- **Secondary tags:** borneo, data discovery, privacy compliance, risk assessment, security automation, data hygiene, composio, ai workflow
- This solution streamlines the complex process of identifying sensitive data assets and assessing their privacy posture to maintain organizational compliance.

---

## Who is this for?
This solution is designed for privacy-conscious organizations looking to automate their security posture and data governance.

- **Data Privacy Officer**
  - Automate the identification of PII and sensitive data across distributed systems to ensure regulatory compliance.
- **Security Engineer**
  - Gain real-time visibility into data assets and prioritize remediation efforts based on automated risk scoring.
- **Compliance Manager**
  - Generate consistent, audit-ready reports on data privacy status without manual scanning overhead.
- **IT Operations Lead**
  - Reduce the risk of data exposure by integrating automated privacy checks into existing infrastructure workflows.

---

## Features
- **Automated Asset Discovery**
  - Continuously scan and map data assets across your environment to maintain an up-to-date inventory of sensitive information.
- **Privacy Risk Scoring**
  - Automatically evaluate the risk level of discovered assets based on data sensitivity and exposure potential.
- **Borneo Integration**
  - Utilize the powerful Borneo API via the Composio Toolset to execute deep-packet inspection and privacy analysis.
- **Compliance Reporting**
  - Generate automated summaries of privacy risks, providing actionable insights for immediate remediation.
- **Real-time Monitoring**
  - Trigger alerts and assessments the moment new data assets are detected, ensuring no shadow data goes unmonitored.

---

## Use Cases
**Data Governance & Compliance**
- Automatically scan new cloud storage buckets for PII to ensure adherence to GDPR and CCPA requirements.
- Generate monthly privacy risk reports for stakeholders to demonstrate ongoing data protection efforts.

**Security Operations**
- Identify and isolate high-risk data assets that are improperly exposed to public or unauthorized internal access.
- Integrate privacy scanning into the CI/CD pipeline to prevent sensitive data from being committed to non-compliant environments.

**Data Hygiene & Cleanup**
- Locate redundant, obsolete, or trivial (ROT) data that contains sensitive information for secure archival or deletion.
- Map data lineage to understand how sensitive information flows through your organization’s internal services.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd builder and select "Create New Flow."
2. Import the Asset Privacy Guardian template from the Uplizd marketplace.
3. Connect your Borneo API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the scan command or specific asset scope from the user.
- **Agent**: Orchestrates the privacy analysis logic and interprets the results from the toolset.
- **Composio Toolset**: Executes the Borneo API calls to perform discovery and risk assessment.
- **Chat Output**: Delivers the final privacy report and risk summary back to the user.

### 3) Run the Flow
Use the Playground to test your privacy scans with prompts like:
- `Run a full privacy scan on the production database and summarize high-risk assets.`
- `Identify all PII-containing assets in the marketing cloud storage bucket.`
- `Generate a risk assessment report for the latest data discovery scan.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a privacy analyst, interpreting raw scan data into human-readable reports.
- Set the system prompt to prioritize security-first language and risk-based prioritization.
- Ensure the agent is configured to handle large JSON outputs from the Borneo API.
- Use a high-reasoning model to accurately categorize data types (e.g., PII, PHI, Financial).

### 2) Composio Toolset Node
- Provide your Borneo API key to authenticate the toolset.
- Define the connection scope to include read-only access to your cloud storage and database environments.

### 3) Tool Availability
- `discovery_scan`: Initiates the automated search for data assets.
- `risk_assessment`: Analyzes identified assets for privacy vulnerabilities.
- `report_generator`: Compiles findings into a structured summary.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automated auditing of cloud account configurations and security settings.
- [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Monitor and audit user access levels to maintain internal security compliance.
- [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) - Proactive identification of organizational risks and compliance gaps.
