# Account Audit Agent (Uplizd) - Automated Cloudflare security and compliance auditing

## Summary
The Account Audit Agent is an intelligent Uplizd workflow designed to automate the security posture assessment and compliance monitoring of Cloudflare accounts. By leveraging the Composio Toolset to interface directly with Cloudflare APIs, this agent identifies misconfigurations, detects potential vulnerabilities, and generates actionable security reports, significantly reducing manual overhead for security teams and ensuring continuous infrastructure hygiene.

---

## Demo
![Account Audit Agent workflow showing automated security scanning and compliance reporting](image.png)
**Alt text (SEO-ready):** Account Audit Agent workflow for Cloudflare security scanning, compliance monitoring, and automated infrastructure auditing on Uplizd.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/6266e7fe-1e59-595e-9d7d-342b2f1cd375)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** cloudflare, security, compliance, audit, infrastructure, automation, composio, ai workflow
- This solution bridges the gap between complex cloud infrastructure management and automated security compliance through intelligent agentic workflows.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining secure and compliant cloud environments.

- **Security Engineers**
    - Automate the discovery of misconfigured security headers and firewall rules across global zones.
- **DevOps Leads**
    - Ensure infrastructure as code deployments adhere to internal security benchmarks and compliance standards.
- **Compliance Officers**
    - Generate real-time audit logs and security posture reports for regulatory requirements.
- **Cloud Architects**
    - Maintain consistent security policies across multi-zone Cloudflare deployments with minimal manual intervention.

---

## Features
- **Automated Security Scanning**
    - Continuously inspects Cloudflare zone settings for common vulnerabilities and security gaps.
- **Compliance Reporting**
    - Aggregates audit data into structured summaries to verify adherence to industry security frameworks.
- **Intelligent Remediation Suggestions**
    - Provides context-aware recommendations for fixing identified misconfigurations based on best practices.
- **Real-time API Integration**
    - Utilizes the Composio Toolset to perform secure, authenticated read/write operations against Cloudflare endpoints.
- **Customizable Audit Rules**
    - Allows users to define specific security thresholds and monitoring parameters tailored to organizational needs.

---

## Use Cases
**Security Posture Management**
- Automatically audit SSL/TLS settings to ensure all zones meet minimum encryption standards.
- Detect and flag unauthorized changes to WAF (Web Application Firewall) rulesets.

**Compliance and Governance**
- Perform periodic bulk audits of account-wide settings to satisfy SOC2 or ISO27001 evidence requirements.
- Monitor for "drift" in security configurations across production and staging environments.

**Infrastructure Hygiene**
- Identify unused or legacy DNS records that pose potential security risks.
- Audit rate-limiting configurations to ensure protection against DDoS and brute-force attacks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project to initialize the workflow.
3. Authenticate your Cloudflare account via the Composio connection prompt.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the specific audit request or scope (e.g., "Audit all zones").
- **Agent**: Orchestrates the logic, interprets audit results, and formats the final report.
- **Composio Toolset**: Executes the specific Cloudflare API calls required for data retrieval.
- **Chat Output**: Delivers the final security audit findings and recommendations to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Perform a full security audit of all active zones in my Cloudflare account.`
- `Check if any zones are missing strict SSL/TLS settings and list them.`
- `Generate a compliance report for the current WAF configuration.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security analyst, prioritizing clarity and actionable insights.
- Instruct the agent to prioritize high-severity findings first.
- Ensure the agent maintains a professional, technical tone in all reports.
- Configure the agent to provide specific API-based remediation steps where applicable.

### 2) Composio Toolset Node
- Provide a valid Cloudflare API Token with `Zone.Read` and `Account.Read` permissions.
- Ensure the connection scope is limited to the specific account IDs you wish to audit.

### 3) Tool Availability
- **Zone Discovery**: Lists all available domains and zones.
- **Security Settings Inspector**: Retrieves current SSL, WAF, and Firewall configurations.
- **Audit Log Fetcher**: Retrieves recent account-level changes for compliance review.

---

## Related Solutions
- [CRM System Health Monitor](../crm-system-health-monitor/README.md) - Monitor and maintain data integrity across your CRM ecosystem.
- [AI Compliance Monitor](../ai-compliance-monitor-by-apipie-ai/README.md) - Automated monitoring for regulatory compliance and policy adherence.
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) - Streamline the creation and setup of new Cloudflare zones.
- [CRM Permissions Analyzer](../crm-permissions-analyzer/README.md) - Audit and manage user access levels within your CRM.
