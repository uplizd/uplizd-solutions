# Multi-Tenant Email Orchestrator (Uplizd) - Automated cross-tenant email infrastructure management

## Summary
The Multi-Tenant Email Orchestrator by SendGrid is an intelligent Uplizd workflow designed to automate the provisioning, domain assignment, and IP management for complex multi-tenant email environments. By leveraging the Composio Toolset to interface directly with SendGrid’s API, this solution eliminates manual configuration overhead, ensures strict domain isolation, and provides real-time visibility into email infrastructure health, ultimately accelerating onboarding velocity for SaaS providers and agencies.

---

## Demo
![Multi-Tenant Email Orchestrator workflow showing SendGrid API integration for subuser management](image.png)
**Alt text (SEO-ready):** Multi-tenant email orchestration workflow in Uplizd showing automated SendGrid domain and IP assignment for scalable infrastructure management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4ccc7cca-dfae-5802-a417-3acf29bbb9ac)

---

## Category
**Primary category:** Operations
**Secondary tags:** email infrastructure, sendgrid, multi-tenant, saas, automation, domain management, ip warm-up, composio
This solution streamlines the complex task of managing email deliverability and subuser accounts across diverse client environments.

---

## Who is this for?
This solution is designed for technical operations teams and platform engineers who need to scale email infrastructure without manual intervention.

*   **Platform Engineer**
    *   Automates the provisioning of new subusers and domain verification processes.
*   **Email Deliverability Specialist**
    *   Monitors IP health and ensures consistent domain reputation across multiple tenants.
*   **SaaS Operations Manager**
    *   Reduces onboarding time for new clients by standardizing email infrastructure setups.
*   **DevOps Lead**
    *   Maintains strict compliance and isolation between tenant email configurations via API-driven workflows.

---

## Features
- **Automated Subuser Provisioning**
    Create and configure new subuser accounts instantly, ensuring consistent settings across your entire platform.
- **Dynamic Domain Assignment**
    Automatically link verified domains to specific subusers, reducing the manual effort required for DNS and setup.
- **IP Pool Management**
    Assign dedicated or shared IP pools to tenants based on volume requirements and reputation needs.
- **Real-time Infrastructure Monitoring**
    Track the health and status of email domains and subuser accounts directly through the agent interface.
- **Composio-Powered Integration**
    Utilize the Composio Toolset to execute complex SendGrid API calls securely without writing custom backend code.

---

## Use Cases
**Infrastructure Scaling**
*   Automatically provision subuser accounts when a new customer signs up for your platform.
*   Batch update domain settings across hundreds of tenants during infrastructure migrations.

**Deliverability & Compliance**
*   Monitor domain authentication status (SPF/DKIM) and alert the team if a tenant's configuration drifts.
*   Segregate high-volume senders into dedicated IP pools to protect your primary domain reputation.

**Operational Efficiency**
*   Generate automated reports on subuser email volume and engagement metrics for internal stakeholders.
*   Revoke access or rotate credentials for compromised subuser accounts through a simple chat command.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Multi-Tenant Email Orchestrator template from the solution library.
3. Connect your SendGrid API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives natural language requests for infrastructure changes.
*   **Agent**: Processes intent and maps requests to specific SendGrid API actions.
*   **Composio Toolset**: Executes the authenticated API calls to manage SendGrid resources.
*   **Chat Output**: Returns the confirmation or status report of the requested operation.

### 3) Run the Flow
Use the Playground to test your orchestration:
*   `Provision a new subuser named 'client-alpha' and assign it to the 'marketing-pool' IP group.`
*   `Check the SPF and DKIM status for all domains associated with subuser 'client-beta'.`
*   `List all active subusers and report their current email sending volume for the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an infrastructure orchestrator.
*   Maintain a neutral, technical tone for all status updates.
*   Always verify the existence of a subuser before attempting to modify domain settings.
*   Prioritize security by confirming destructive actions (e.g., deleting a subuser) before execution.

### 2) Composio Toolset Node
*   **API Key**: Provide your SendGrid API Key with sufficient permissions for subuser and domain management.
*   **Connection Scope**: Ensure the scope includes `subuser.manage`, `domain.read`, and `ip.manage` permissions.

### 3) Tool Availability
*   `sendgrid_create_subuser`: Creates new tenant accounts.
*   `sendgrid_get_domain_auth`: Retrieves DNS and authentication status.
*   `sendgrid_assign_ip_pool`: Manages IP pool allocation for specific tenants.
*   `sendgrid_list_subusers`: Provides an overview of active infrastructure.

---

## Related Solutions
*   [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) - Automates CRM account creation and onboarding workflows.
*   [Workflow Automation Agent (JobNimbus)](../workflow-automation-agent-by-jobnimbus/README.md) - Streamlines business process automation for service-based operations.
*   [Account Health Usage Monitor (Jotform)](../account-health-usage-monitor-by-jotform/README.md) - Tracks customer usage metrics and identifies account health risks.
