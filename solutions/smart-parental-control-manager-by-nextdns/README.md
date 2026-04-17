# Smart Parental Control Manager (Uplizd) - Intelligent DNS filtering for family internet safety

## Summary
The Smart Parental Control Manager is an automated Uplizd AI workflow designed to provide real-time internet safety and content filtering for households. By integrating with NextDNS, this solution empowers parents and administrators to maintain a secure digital environment, ensuring family-friendly browsing, blocking malicious domains, and providing granular control over online activity through a centralized, automated pipeline.

---

## Demo
![Smart Parental Control Manager workflow dashboard showing DNS filtering rules and real-time activity logs](image.png)
**Alt text (SEO-ready):** Smart Parental Control Manager workflow dashboard showing DNS filtering rules and real-time activity logs for Uplizd AI-driven family internet safety and content filtering.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/17b300d0-03c8-5589-ad31-e8939d0bf92f)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** dns, internet safety, parental control, nextdns, content filtering, security, automation, ai workflow
- This solution streamlines digital safety by automating DNS-based content restrictions and security policies for home and small office networks.

---

## Who is this for?
This solution is designed for individuals and administrators who need to enforce digital boundaries and protect network users from harmful content.

- **Parents**
  - Automate the enforcement of age-appropriate content filters and screen time restrictions.
- **Home Network Administrators**
  - Manage security policies across multiple devices without manual configuration for each endpoint.
- **Small Business Owners**
  - Restrict access to distracting or non-work-related websites to maintain productivity.
- **Privacy Advocates**
  - Implement robust DNS-level blocking to prevent tracking and malicious domain access.

---

## Features
- **Automated DNS Filtering**
  - Instantly apply or update content blocklists via the NextDNS API to ensure consistent protection.
- **Real-time Activity Monitoring**
  - Receive automated summaries of blocked requests and potential security threats detected on the network.
- **Customizable Safety Profiles**
  - Define unique filtering rules for different users or device groups within the home or office.
- **Security Threat Mitigation**
  - Automatically block known phishing, malware, and botnet domains to harden network defenses.
- **Composio-Powered Integration**
  - Seamlessly connect the Uplizd Agent to the NextDNS ecosystem for reliable, low-latency policy management.

---

## Use Cases
**Family Safety Management**
- Automatically enable "Safe Search" and block adult content during school hours.
- Schedule internet downtime for specific devices to encourage healthy digital habits.

**Network Security Hardening**
- Block access to known malicious domains and phishing sites across all connected hardware.
- Monitor and alert on suspicious DNS query patterns that may indicate compromised devices.

**Productivity and Compliance**
- Restrict access to social media and streaming platforms during designated work or study periods.
- Enforce company-wide web usage policies for remote employees using home networks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the template in the Uplizd builder.
2. Connect your NextDNS account via the Composio Toolset node.
3. Configure your target DNS profiles and desired blocklist categories.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives natural language commands for policy updates or status checks.
- **Agent**: Interprets user requests and translates them into specific API calls for DNS management.
- **Composio Toolset**: Executes the requested changes directly within the NextDNS configuration.
- **Chat Output**: Provides confirmation of policy updates or reports on network activity.

### 3) Run the Flow
Use the Playground to test your automation with prompts like:
- `Block all gambling and adult content categories on the 'Kids' profile.`
- `Show me a summary of the top 5 blocked domains from the last 24 hours.`
- `Disable internet access for the 'Guest' device group until 6 PM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the intelligent interface between your commands and the network infrastructure.
- Use a model capable of structured output to ensure API parameters are parsed correctly.
- Instruct the agent to prioritize security-first settings when creating new rules.
- Maintain a neutral, informative tone for all status reports and confirmation messages.

### 2) Composio Toolset Node
- Provide your NextDNS API Key and Profile ID within the toolset configuration.
- Ensure the connection scope includes read and write permissions for DNS policy management.

### 3) Tool Availability
- **Profile Management**: Create, update, and delete filtering profiles.
- **Blocklist Configuration**: Toggle specific categories (e.g., malware, social media, gambling).
- **Log Retrieval**: Query DNS request logs for security auditing.

---

## Related Solutions
- [Account Audit Agent by Cloudflare](../account-audit-agent-by-cloudflare/README.md) - Automated security auditing for network and account infrastructure.
- [Zone Provisioning Agent by Cloudflare](../zone-provisioning-agent-by-cloudflare/README.md) - Streamlined management for DNS zones and network security settings.
- [Workflow Health Monitor by Dailybot](../workflow-health-monitor-by-dailybot/README.md) - Real-time monitoring and reporting for automated operational workflows.
