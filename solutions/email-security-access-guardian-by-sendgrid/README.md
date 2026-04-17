# Email Security Access Guardian (Uplizd) - Automated IP Allowlisting and Access Control

## Summary
The Email Security Access Guardian (Uplizd) automates the lifecycle of email security configurations by streamlining IP allowlist management and access request approvals. Designed for security and IT teams, this AI-driven workflow eliminates manual bottlenecks in SendGrid security operations, ensuring that authorized traffic is processed instantly while maintaining strict compliance and audit trails.

---

## Demo
![Email Security Access Guardian workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Email Security Access Guardian workflow diagram showing Chat Input, Agent, Composio Toolset, and Chat Output nodes for automated SendGrid IP allowlisting and security management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/14748812-7217-59b2-a211-a8a29c2bb450)

---

## Category
- **Primary category:** Engineering
- **Secondary tags:** email security, sendgrid, access control, ip allowlist, automation, security operations, composio, ai workflow
- This solution bridges the gap between security policy requests and technical implementation within SendGrid, providing a secure, automated pipeline for infrastructure access.

---

## Who is this for?
This solution is designed for technical teams managing high-volume email infrastructure and security compliance.

- **Security Engineer**
    - Automates the validation and approval process for new IP addresses to reduce manual security overhead.
- **IT Operations Manager**
    - Ensures consistent application of security policies across email environments without manual configuration errors.
- **DevOps Lead**
    - Integrates access request workflows directly into existing communication channels for faster deployment cycles.
- **Compliance Officer**
    - Maintains a clear, automated audit log of all access requests and modifications made to the email security perimeter.

---

## Features
- **Automated IP Validation**
    - Automatically verifies incoming IP addresses against internal security standards before attempting to update the allowlist.
- **SendGrid Integration**
    - Leverages the Composio Toolset to securely interact with the SendGrid API for real-time allowlist modifications.
- **Approval Workflow**
    - Implements a structured request-response loop that requires verification before executing sensitive security changes.
- **Real-time Audit Logging**
    - Captures every interaction and configuration change, providing a transparent history of security access updates.
- **Error Handling & Alerts**
    - Provides immediate feedback if an API request fails or if an IP address is flagged as potentially malicious.

---

## Use Cases
**Infrastructure Access Management**
- Automatically add new office or VPN IP ranges to the SendGrid allowlist upon verified request.
- Remove stale or expired IP addresses to maintain a clean and secure email infrastructure.

**Security Incident Response**
- Quickly revoke access for compromised IP addresses during a security event to prevent unauthorized email relay.
- Temporarily whitelist specific IPs for emergency troubleshooting or third-party integration testing.

**Compliance & Reporting**
- Generate summary reports of all recent changes to the email security configuration for internal audits.
- Ensure all security modifications are tied to an authorized requester, providing accountability for every change.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow into your Uplizd dashboard.
3. Connect your SendGrid API credentials via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the security request or IP modification command from the user.
- **Agent**: Processes the request, validates the input, and determines the necessary SendGrid API action.
- **Composio Toolset**: Executes the authenticated API calls to update the email security allowlist.
- **Chat Output**: Returns the status of the operation and confirmation of the security change to the user.

### 3) Run the Flow
Use the Playground to test your security guardian with prompts like:
- `Add 192.168.1.1 to the SendGrid allowlist for the marketing team.`
- `List all currently allowed IP addresses in our SendGrid account.`
- `Remove IP 10.0.0.5 from the security allowlist immediately.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security gatekeeper, ensuring only valid requests are processed.
- Use a model with high reasoning capabilities to parse IP addresses and request intent.
- Instruct the agent to always verify the requester's identity before executing changes.
- Configure the agent to provide clear, concise confirmation messages upon successful API execution.

### 2) Composio Toolset Node
- Provide your SendGrid API key with the necessary scopes for managing IP access lists.
- Ensure the connection is scoped to the specific environment (e.g., production vs. staging) to prevent accidental configuration changes.

### 3) Tool Availability
- **IP Management**: Tools for adding, removing, and listing IP addresses in the allowlist.
- **Validation Tools**: Regex-based tools for verifying the format of IP addresses.
- **Logging Tools**: Capabilities to append request details to a secure audit log.

---

## Related Solutions
- [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automates security auditing and infrastructure monitoring.
- [Admin User Access Auditor by Storeganise](../admin-user-access-auditor-by-storeganise/README.md) - Manages and audits user access permissions across platforms.
- [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and health of automated workflows.
