# Network Inventory Manager (Uplizd) - Automated device discovery and network asset tracking

## Summary
The Network Inventory Manager by Uplizd automates the discovery, cataloging, and monitoring of network assets to ensure a single source of truth for IT infrastructure. By leveraging the Composio Toolset to interface with network security and management platforms like DNSFilter, this workflow eliminates manual data entry, reduces shadow IT risks, and provides real-time visibility into your connected device ecosystem.

---

## Demo
![Network Inventory Manager workflow dashboard showing automated device discovery and asset synchronization nodes](image.png)
**Alt text (SEO-ready):** Network Inventory Manager Uplizd workflow showing automated device discovery, asset tracking, and DNSFilter integration for IT operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d6999cc8-44b5-5903-8c82-eb54c20ce6f5)

---

## Category
- **Primary category:** IT Operations
- **Secondary tags:** network inventory, asset management, dnsfilter, it infrastructure, device discovery, automation, composio, ai workflow
- This solution streamlines IT asset management by automating the synchronization of network device data into a centralized inventory system.

---

## Who is this for?
This solution is designed for IT professionals and security teams who need to maintain accurate records of their network environment.

- **Network Administrator**
    - Automates the identification of new devices to prevent unauthorized network access.
- **IT Security Analyst**
    - Ensures all connected assets are accounted for and compliant with security policies.
- **Operations Manager**
    - Reduces manual auditing time by maintaining a real-time, accurate hardware inventory.
- **Compliance Officer**
    - Provides detailed logs and reports for regulatory audits regarding network infrastructure.

---

## Features
- **Automated Device Discovery**
    - Continuously scans network segments to identify and register new hardware assets in real-time.
- **DNSFilter Integration**
    - Leverages the Composio Toolset to pull granular security and traffic data directly from DNSFilter.
- **Centralized Asset Registry**
    - Aggregates disparate device data into a unified dashboard, eliminating data silos across the organization.
- **Shadow IT Detection**
    - Flags unrecognized or unauthorized devices attempting to connect to the network for immediate review.
- **Dynamic Reporting**
    - Generates automated status reports on inventory health, device uptime, and security posture.

---

## Use Cases
**Network Security Audits**
- Automatically flag non-compliant devices that lack required security software or firmware updates.
- Generate weekly reports identifying all active endpoints connected to the corporate network.

**Asset Lifecycle Management**
- Track the deployment and decommissioning of network hardware to optimize procurement cycles.
- Sync device metadata with internal databases to ensure accurate depreciation and maintenance tracking.

**Operational Efficiency**
- Reduce the time spent on manual network documentation by 80% through automated discovery workflows.
- Trigger alerts for IT staff when critical network infrastructure nodes go offline or exhibit anomalous traffic.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Network Inventory Manager template from the marketplace.
3. Configure your API credentials for DNSFilter and your internal database.
4. Ensure nodes are correctly connected from the Chat Input through the Agent and Composio Toolset to the Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives manual triggers or scheduled scan requests from the user.
*   **Agent**: Processes network data and determines the necessary inventory updates.
*   **Composio Toolset**: Executes secure API calls to DNSFilter to fetch and verify device information.
*   **Chat Output**: Delivers a summary of discovered devices and any flagged security anomalies.

### 3) Run the Flow
Use the Playground to test your inventory workflow with these prompts:
- `Run a full network discovery scan and update the asset registry.`
- `List all unauthorized devices detected by DNSFilter in the last 24 hours.`
- `Generate a summary report of all active network assets and their current security status.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for network data interpretation.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate data parsing.
- Set the system instruction to prioritize security-first reporting.
- Ensure the agent is configured to handle structured JSON outputs for database integration.

### 2) Composio Toolset Node
- Provide your DNSFilter API key within the secure credential manager.
- Define the connection scope to include read-only access for device discovery and reporting.

### 3) Tool Availability
- **DNSFilter API**: For fetching domain, device, and security policy data.
- **Inventory Database Connector**: For updating asset records.
- **Notification Service**: For alerting admins of new or suspicious device connections.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automates security auditing and compliance monitoring for cloud accounts.
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) - Streamlines the setup and management of network zones and security configurations.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks the operational status and performance of automated business workflows.
