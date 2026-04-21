# Supabase Security Monitor (Uplizd) - Automated security auditing and API key management

## Summary
The Supabase Security Monitor is an intelligent Uplizd workflow designed to automate the oversight of your database security posture. By leveraging the Composio Toolset to interface directly with Supabase, this solution provides real-time monitoring of API keys, row-level security (RLS) configurations, and access logs, ensuring your backend infrastructure remains hardened against unauthorized access and configuration drift.

---

## Demo
![Supabase Security Monitor workflow showing automated API key auditing and RLS policy verification](image.png)
**Alt text (SEO-ready):** Supabase Security Monitor workflow for automated API key auditing, RLS policy verification, and security alerting using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ff9cc5df-5062-5658-b73e-84ada0238056)

---

## Category
**Primary category:** Engineering
**Secondary tags:** supabase, security, api management, rls, database, cloud infrastructure, composio, ai workflow
This solution bridges the gap between manual security audits and automated infrastructure oversight for modern backend development.

---

## Who is this for?
This solution is designed for technical teams looking to maintain a secure and compliant database environment without manual overhead.

- **DevOps Engineer**
    - Automates the detection of exposed API keys and insecure database configurations.
- **Security Analyst**
    - Provides continuous monitoring of RLS policies to ensure data privacy standards are met.
- **Backend Developer**
    - Simplifies the management of environment variables and service role keys across multiple projects.
- **Engineering Manager**
    - Ensures consistent security hygiene across all team projects through automated reporting.

---

## Features
- **Automated API Key Auditing**
    - Scans your Supabase projects to identify active API keys and flag those with excessive permissions.
- **RLS Policy Verification**
    - Automatically checks your database tables to ensure Row Level Security is enabled and correctly configured.
- **Real-time Security Alerts**
    - Triggers notifications when unauthorized configuration changes or potential security vulnerabilities are detected.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely execute administrative commands within the Supabase API environment.
- **Compliance Reporting**
    - Generates summary reports of your security posture, making it easier to maintain audit trails for compliance requirements.

---

## Use Cases
**Proactive Security Auditing**
- Scanning production databases for missing or misconfigured Row Level Security policies.
- Identifying service role keys that have been improperly exposed in client-side code.

**Infrastructure Hygiene**
- Automating the rotation or revocation of legacy API keys that are no longer in use.
- Maintaining a clean environment by auditing project settings against security best practices.

**Incident Response**
- Rapidly assessing the impact of a potential credential leak by checking all active project keys.
- Providing immediate visibility into recent administrative changes within the Supabase dashboard.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in your workspace.
2. Connect your Supabase account via the Composio integration settings.
3. Configure your environment variables to target the specific Supabase project IDs you wish to monitor.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives security audit commands or scheduling triggers.
- **Agent**: Processes security logic and interprets Supabase configuration data.
- **Composio Toolset**: Executes secure API calls to fetch project metadata and security logs.
- **Chat Output**: Delivers actionable audit reports and security alerts to your preferred channel.

### 3) Run the Flow
Use the Playground to test the agent with these prompts:
- `Run a full security audit on my production Supabase project.`
- `List all tables that currently have Row Level Security disabled.`
- `Identify any API keys that have been active for more than 90 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security auditor, prioritizing accuracy and clear reporting.
- Use a model with strong reasoning capabilities to interpret complex database policies.
- Set the system instruction to prioritize "Security First" and "Least Privilege" principles.
- Configure the agent to provide remediation steps alongside any identified vulnerabilities.

### 2) Composio Toolset Node
- Provide your Supabase API key with the necessary read-only permissions for security monitoring.
- Define the connection scope to include project metadata and RLS configuration endpoints.

### 3) Tool Availability
- `supabase_list_projects`: Retrieves all projects linked to the account.
- `supabase_get_rls_policies`: Fetches current RLS configurations for specific tables.
- `supabase_list_api_keys`: Audits active keys and their associated permission scopes.

---

## Related Solutions
- [Account Audit Agent (Cloudflare)](../account-audit-agent-by-cloudflare/README.md) - Automate security and configuration audits for your Cloudflare infrastructure.
- [Admin User Access Auditor (Storeganise)](../admin-user-access-auditor-by-storeganise/README.md) - Monitor and audit administrative access levels across your workspace.
- [Workflow Health Monitor (Dailybot)](../workflow-health-monitor-by-dailybot/README.md) - Track the operational health and status of your automated workflows.
