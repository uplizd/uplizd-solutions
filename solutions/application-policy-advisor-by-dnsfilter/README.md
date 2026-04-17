# Application Policy Advisor (Uplizd) - Intelligent application filtering and security policy management

## Summary
The Application Policy Advisor by DNSFilter is an AI-driven workflow designed to automate the evaluation, categorization, and enforcement of application security policies. By leveraging real-time threat intelligence and DNS-level filtering, this solution enables IT and security teams to maintain a robust security posture, reduce shadow IT risks, and ensure organizational compliance with minimal manual intervention.

---

## Demo
![Application Policy Advisor workflow dashboard showing DNSFilter integration and policy recommendation nodes](image.png)
**Alt text (SEO-ready):** Application Policy Advisor workflow dashboard showing DNSFilter integration, automated security policy recommendations, and Uplizd AI orchestration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/21c84f60-672f-5c5b-b27b-d4d2aa0d0e45)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** dnsfilter, security, policy management, compliance, shadow it, automation, composio, ai workflow
- This solution bridges the gap between raw network traffic data and actionable security governance through intelligent policy automation.

---

## Who is this for?
This solution is designed for security-conscious organizations looking to streamline their network governance and threat mitigation strategies.

- **IT Administrators**
    - Automate the classification of new applications to prevent unauthorized network access.
- **Security Analysts**
    - Receive real-time alerts and policy recommendations based on DNSFilter threat intelligence.
- **Compliance Officers**
    - Maintain audit-ready documentation of application access policies and security enforcement.
- **Network Engineers**
    - Reduce the overhead of manual blocklist updates by syncing policy changes directly to the network edge.

---

## Features
- **Automated Policy Assessment**
    - Instantly analyze application traffic patterns against defined security benchmarks to suggest policy updates.
- **DNSFilter Integration**
    - Seamlessly connect with DNSFilter via the Composio Toolset to fetch threat data and push policy changes.
- **Shadow IT Detection**
    - Identify and flag unauthorized applications attempting to connect to the corporate network.
- **Real-time Compliance Monitoring**
    - Continuously audit network traffic to ensure alignment with internal security and acceptable use policies.
- **Intelligent Alerting**
    - Route high-priority security findings to the appropriate team members with context-rich remediation steps.

---

## Use Cases
**Network Security Hardening**
- Automatically block domains associated with newly identified malicious applications.
- Enforce granular access policies for high-risk application categories during business hours.

**Shadow IT Mitigation**
- Discover unauthorized SaaS tools in use and generate policy enforcement recommendations.
- Notify department heads when employees attempt to access non-compliant application categories.

**Compliance and Reporting**
- Generate weekly summaries of policy enforcement actions for security audit requirements.
- Validate that all active network policies align with current organizational security standards.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Application Policy Advisor template from the solution library.
3. Connect your DNSFilter API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives security queries or policy update requests from the user.
- **Agent**: Processes input, interprets security context, and determines the necessary policy action.
- **Composio Toolset**: Executes authorized commands against the DNSFilter API to retrieve data or update policies.
- **Chat Output**: Returns the status of policy changes or detailed security recommendations to the user.

### 3) Run the Flow
Use the Playground to test the agent's decision-making capabilities:
- `Analyze current network traffic and identify any unauthorized SaaS applications.`
- `Create a new block policy for all domains associated with the 'gambling' category.`
- `Generate a summary of the most frequent policy violations from the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the central intelligence for policy interpretation and decision-making.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize security-first responses when ambiguity exists.
- Ensure the agent follows strict JSON output formats for API interactions.

### 2) Composio Toolset Node
- Provide a valid DNSFilter API key with "Read/Write" permissions.
- Scope the connection to allow the agent to manage domains, policies, and reporting endpoints.

### 3) Tool Availability
- **Domain Management**: Ability to add/remove domains from blocklists.
- **Policy Retrieval**: Access to current organizational policy configurations.
- **Threat Intelligence**: Querying DNSFilter's real-time threat database.
- **Reporting**: Fetching logs and violation summaries for audit purposes.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automated auditing of account configurations and security settings.
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) - Streamlined management of network zones and security provisioning.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitoring the operational health and status of automated workflows.
