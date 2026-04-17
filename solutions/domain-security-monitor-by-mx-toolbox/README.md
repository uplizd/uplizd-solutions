# Domain Security Monitor (Uplizd) - Automated DNS health and security surveillance

## Summary
The Domain Security Monitor is an intelligent Uplizd workflow that provides continuous surveillance of domain infrastructure and DNS health. By leveraging the Composio Toolset to interface with MX Toolbox, this solution enables security teams and system administrators to proactively identify configuration vulnerabilities, monitor blacklists, and ensure domain integrity, ultimately reducing the risk of service disruption and phishing exposure.

---

## Demo
![Domain Security Monitor workflow dashboard showing automated DNS lookup and security alert triggers](image.png)
**Alt text (SEO-ready):** Domain Security Monitor Uplizd workflow, automated DNS health check, MX Toolbox integration, and security vulnerability alerting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1c2eae70-7dc3-56cc-b27f-4af4cae4b5a4)

---

## Category
**Primary category:** Engineering
**Secondary tags:** domain security, dns health, mx toolbox, security monitoring, infrastructure, automation, composio, ai workflow.
This solution automates the technical oversight of domain assets to ensure robust security posture and continuous uptime.

---

## Who is this for?
This solution is designed for technical teams responsible for maintaining secure and reliable web infrastructure.

* **Security Engineer**
    * Automates the detection of DNS misconfigurations and potential security threats before they impact production.
* **System Administrator**
    * Receives real-time alerts on domain health, reducing manual lookup time across multiple platforms.
* **DevOps Lead**
    * Ensures consistent security compliance across a portfolio of managed domains through automated reporting.
* **IT Operations Manager**
    * Maintains a single source of truth for domain reputation and blacklist status to prevent email deliverability issues.

---

## Features
- **Automated DNS Auditing**
    * Performs recurring checks on DNS records to identify propagation issues or unauthorized changes.
- **Real-time Blacklist Monitoring**
    * Automatically queries global blacklists to ensure your domain reputation remains intact.
- **Composio-Powered Integration**
    * Seamlessly connects with the MX Toolbox API to fetch deep technical insights without manual intervention.
- **Proactive Alerting**
    * Triggers notifications via the Chat Output node when security anomalies or critical health drops are detected.
- **Centralized Dashboard**
    * Consolidates complex technical data into actionable insights for rapid incident response.

---

## Use Cases
**Infrastructure Security**
* Monitoring DNSSEC status to prevent cache poisoning and man-in-the-middle attacks.
* Auditing SPF, DKIM, and DMARC records to ensure email authentication integrity.

**Operational Health**
* Tracking domain expiration dates and registrar status to prevent accidental service outages.
* Validating MX record configurations to ensure uninterrupted inbound email flow.

**Reputation Management**
* Detecting if a domain has been flagged by major spam filters or security vendors.
* Generating periodic health reports to document compliance with internal security policies.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Domain Security Monitor template file provided in this repository.
3. Authenticate your MX Toolbox credentials within the integration settings.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
* **Chat Input**: Receives the domain name or list of domains to be audited.
* **Agent**: Analyzes the input and determines the necessary security checks to perform.
* **Composio Toolset**: Executes the specific MX Toolbox API calls to retrieve DNS and security data.
* **Chat Output**: Formats the technical findings into a human-readable security summary.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
* `Check the DNS health and blacklist status for example-domain.com`
* `Perform a full security audit on my primary domain and report any missing DMARC records`
* `Are there any critical security vulnerabilities currently associated with my domain infrastructure?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a security analyst, interpreting raw API data into actionable advice.
* Use a model with strong reasoning capabilities to parse technical DNS output.
* Instruct the agent to prioritize high-risk vulnerabilities (e.g., blacklisting).
* Maintain a professional, concise tone for all security reporting.

### 2) Composio Toolset Node
* Provide your valid MX Toolbox API key in the configuration panel.
* Set the connection scope to include read-only access to DNS and blacklist lookup tools.

### 3) Tool Availability
* `mx_toolbox_dns_lookup`: Fetches current A, MX, and TXT records.
* `mx_toolbox_blacklist_check`: Queries domain against global spam and security blacklists.
* `mx_toolbox_dmarc_validator`: Verifies the presence and configuration of email authentication protocols.

---

## Related Solutions
* [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automates security audits for Cloudflare-managed infrastructure.
* [Zone Provisioning Agent by Cloudflare](../zone-provisioning-agent-by-cloudflare/README.md) - Manages and automates the provisioning of new security zones.
* [Account Health Compliance Monitor by Brevo](../account-health-compliance-monitor-by-brevo/README.md) - Monitors account-level compliance and health metrics.
