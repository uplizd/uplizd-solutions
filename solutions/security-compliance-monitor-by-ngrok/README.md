# Security Compliance Monitor (Uplizd) - Automated ngrok tunnel auditing and policy enforcement

## Summary
The Security Compliance Monitor is an intelligent Uplizd workflow that automates the auditing of ngrok tunnels to ensure adherence to organizational security policies. By leveraging real-time tunnel inspection and automated policy enforcement, this solution helps security teams maintain a robust security posture, reduce the risk of unauthorized exposure, and ensure continuous compliance across all development and production environments.

---

## Demo
![Security Compliance Monitor workflow dashboard showing ngrok tunnel audit results and automated policy enforcement actions](image.png)
**Alt text (SEO-ready):** Security Compliance Monitor dashboard by Uplizd, showing automated ngrok tunnel audit, security policy enforcement, and real-time compliance reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7569dbfe-5a7f-50e7-9f2a-7a1117e008b8)

---

## Category
- **Primary category:** Security & Compliance
- **Secondary tags:** ngrok, security, compliance, audit, automation, devops, network security, composio
- This solution bridges the gap between infrastructure visibility and automated policy enforcement for secure network tunneling.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining secure infrastructure and network integrity.

- **Security Engineer**
    - Automates the detection of non-compliant ngrok tunnels to prevent unauthorized data exposure.
- **DevOps Manager**
    - Ensures that developer-initiated tunnels adhere to corporate security standards without manual oversight.
- **Compliance Officer**
    - Maintains an audit trail of all active tunnels and policy enforcement actions for regulatory reporting.
- **IT Administrator**
    - Reduces the attack surface by automatically closing or flagging insecure or misconfigured tunnel endpoints.

---

## Features
- **Automated Tunnel Auditing**
    - Continuously scans active ngrok tunnels to identify endpoints that violate security configurations.
- **Policy Enforcement Engine**
    - Automatically triggers remediation actions, such as tunnel termination or alert notification, based on defined security rules.
- **Real-time Compliance Reporting**
    - Provides instant visibility into the security status of all network tunnels via the Composio Toolset.
- **Integration with ngrok API**
    - Seamlessly connects to ngrok to fetch metadata, tunnel status, and configuration details for comprehensive analysis.
- **Customizable Alerting**
    - Configures specific thresholds and notification channels to keep security teams informed of potential risks.

---

## Use Cases
**Infrastructure Security**
- Automatically terminate tunnels that are exposed to the public internet without proper authentication.
- Audit tunnel metadata to ensure all active endpoints are tagged with the correct project and owner information.

**Compliance & Governance**
- Generate weekly compliance reports detailing all active tunnels and their adherence to internal security policies.
- Enforce time-to-live (TTL) policies on temporary development tunnels to prevent long-term security drift.

**Operational Efficiency**
- Streamline the onboarding process by verifying that new tunnels meet security requirements before they are approved for use.
- Reduce manual overhead by automating the cleanup of stale or unused ngrok tunnels across the organization.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Security Compliance Monitor template from the solution library.
3. Connect your ngrok API credentials within the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives manual audit triggers or scheduled scan requests.
- **Agent**: Processes security policies and evaluates tunnel data against compliance rules.
- **Composio Toolset**: Executes API commands to fetch tunnel data and perform remediation actions.
- **Chat Output**: Delivers audit summaries and status updates to the user.

### 3) Run the Flow
Use the Playground to test your security workflows:
- `Audit all active ngrok tunnels and report any non-compliant endpoints.`
- `List all tunnels created in the last 24 hours and flag those without authentication.`
- `Terminate all tunnels associated with the 'staging' environment that have been active for over 8 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the security policy interpreter.
- Focus on identifying deviations from established security baselines.
- Prioritize clear, actionable reporting for security incidents.
- Maintain a neutral, professional tone for all compliance notifications.

### 2) Composio Toolset Node
- Requires a valid ngrok API key with read/write permissions.
- Ensure the connection scope includes tunnel management and metadata retrieval.

### 3) Tool Availability
- **Tunnel Discovery**: Capability to list and filter active ngrok tunnels.
- **Metadata Inspection**: Ability to read tunnel configuration and environment tags.
- **Remediation Actions**: Capability to stop or delete tunnels violating security policies.

---

## Related Solutions
- [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automate infrastructure security audits and access reviews.
- [Admin User Access Auditor by Storeganise](../admin-user-access-auditor-by-storeganise/README.md) - Monitor and audit user access levels for compliance.
- [Workplace Risk Early Warning System by Faceup](../workplace-risk-early-warning-system-by-faceup/README.md) - Proactive risk identification and compliance monitoring.
