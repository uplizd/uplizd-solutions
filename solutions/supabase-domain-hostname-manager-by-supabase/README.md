# Supabase Domain & Hostname Manager (Uplizd) - Automate custom domain and vanity subdomain configuration

## Summary
The Supabase Domain & Hostname Manager is an intelligent Uplizd AI workflow designed to streamline the provisioning, verification, and management of custom domains for Supabase projects. By automating the interaction between your infrastructure and the Supabase API, this solution eliminates manual configuration errors, accelerates deployment velocity, and ensures your project's vanity subdomains remain compliant and active, providing a single source of truth for your infrastructure networking.

---

## Demo
![Supabase Domain & Hostname Manager workflow showing automated API calls to Supabase for custom domain provisioning](image.png)
**Alt text (SEO-ready):** Supabase Domain & Hostname Manager workflow in Uplizd, automating custom domain configuration, vanity subdomain setup, and API-driven infrastructure management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on%20Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/167dca40-0df5-58f8-a54a-40e738a5a78a)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** supabase, domain management, infrastructure, automation, api, networking, devops, composio
- This solution bridges the gap between infrastructure requirements and Supabase project settings, ensuring seamless domain integration for scalable applications.

---

## Who is this for?
This workflow is designed for technical teams managing multiple Supabase environments who need to maintain consistent networking configurations.

- **DevOps Engineer**
    - Automates the repetitive task of mapping custom domains across staging and production environments.
- **Backend Developer**
    - Ensures vanity subdomains are correctly linked to project APIs without manual dashboard intervention.
- **Infrastructure Manager**
    - Maintains a clean, audited record of all active hostnames and domain configurations within the Supabase ecosystem.
- **Technical Founder**
    - Accelerates time-to-market by removing infrastructure bottlenecks during the onboarding of new client projects.

---

## Features
- **Automated Domain Provisioning**
    - Programmatically trigger the creation and assignment of custom domains to specific Supabase projects via the Composio Toolset.
- **Real-time Hostname Verification**
    - Automatically check the status of DNS records and hostname propagation to ensure your services are live and reachable.
- **Vanity Subdomain Management**
    - Simplify the lifecycle of vanity subdomains, allowing for rapid creation, updates, or deprecation as project needs evolve.
- **Error-Resilient Configuration**
    - Built-in validation logic prevents misconfiguration by checking API responses before finalizing domain assignments.
- **Unified Infrastructure Dashboard**
    - Centralize all domain-related operations into a single, chat-driven interface that integrates directly with your existing Supabase stack.

---

## Use Cases
**Infrastructure Scaling**
- Provision custom domains for new client environments automatically upon project initialization.
- Sync domain configurations across multiple regional Supabase instances to maintain global consistency.

**Compliance & Hygiene**
- Identify and remove deprecated or unused vanity subdomains to maintain a clean infrastructure footprint.
- Audit domain verification status to ensure all production endpoints meet security and compliance standards.

**Deployment Automation**
- Integrate domain setup into your CI/CD pipeline, ensuring that every deployment is automatically mapped to the correct hostname.
- Rapidly swap or update domain pointers during maintenance windows without manual dashboard access.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your target workspace and project environment.
3. Connect your Supabase API credentials via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your domain management commands and project identifiers.
- **Agent**: Processes instructions and determines the necessary API calls for Supabase.
- **Composio Toolset**: Executes the specific domain and hostname configuration actions.
- **Chat Output**: Returns the status of the domain provisioning or verification process.

### 3) Run the Flow
Use the Playground to test your configuration with these prompts:
- `Check the current status of the custom domain for project 'my-app-production'.`
- `Provision a new vanity subdomain 'api.example.com' for the Supabase project 'my-app-staging'.`
- `Verify if the DNS records for 'custom.example.com' are correctly pointing to my Supabase instance.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your infrastructure orchestrator, interpreting natural language requests into precise API operations.
- Use a model capable of structured JSON output for reliable API interaction.
- Instruct the agent to prioritize error handling and status verification.
- Maintain a clear context of the project ID and domain requirements in the system prompt.

### 2) Composio Toolset Node
- Provide your Supabase API Key and Organization ID within the Composio connection settings.
- Ensure the connection scope includes read/write permissions for project settings and domain management.

### 3) Tool Availability
- **Domain Provisioning**: Create and assign custom hostnames.
- **Status Checker**: Retrieve current DNS and domain verification states.
- **Project Lister**: Query available projects to ensure correct targeting.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automate security and configuration audits for your cloud infrastructure.
- [Zone Provisioning Agent](../zone-provisioning-agent-by-cloudflare/README.md) - Manage and provision DNS zones and networking configurations at scale.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform operational workflows and task management.
