# HR Onboarding Orchestrator (Uplizd) - Automated employee provisioning and lifecycle management

## Summary
The HR Onboarding Orchestrator automates the complex, multi-system provisioning process required when bringing new talent into an organization. By integrating HRIS platforms with IT identity management and communication tools, this Uplizd AI workflow eliminates manual data entry, ensures consistent access rights, and reduces the time-to-productivity for new hires, serving as a single source of truth for the entire onboarding lifecycle.

---

## Demo
![HR Onboarding Orchestrator dashboard showing automated provisioning steps across HRIS and IT systems](image.png)
**Alt text (SEO-ready):** HR Onboarding Orchestrator Uplizd workflow, automated employee provisioning, HRIS to IT system synchronization, and AI-driven onboarding pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8d9b32f9-b727-54b5-8d3f-8b5723cb4852)

---

## Category
- **Primary category:** HR Operations
- **Secondary tags:** hr, onboarding, provisioning, identity management, automation, employee lifecycle, nango, composio
- This solution bridges the gap between human resources and IT infrastructure to ensure seamless, compliant, and rapid employee onboarding.

---

## Who is this for?
This solution is designed for teams managing high-growth hiring or complex cross-departmental provisioning workflows.

- **HR Operations Manager**
    - Automates repetitive data entry tasks to focus on the human element of the employee experience.
- **IT Systems Administrator**
    - Ensures consistent, error-free provisioning of user accounts and permissions across all corporate software.
- **People Operations Lead**
    - Maintains a standardized onboarding timeline that improves new hire satisfaction and retention.
- **Security Compliance Officer**
    - Enforces strict access control policies by automating the de-provisioning and role-based access assignment processes.

---

## Features
- **Automated Provisioning**
  Triggers account creation in IT systems immediately upon status updates in the HRIS platform.
- **Cross-Platform Synchronization**
  Uses Nango and Composio to maintain data integrity between disparate HR and IT toolsets.
- **Role-Based Access Control**
  Automatically assigns the correct software permissions based on the new hire's department and seniority level.
- **Real-Time Status Tracking**
  Provides instant visibility into the onboarding progress, flagging any stalled tasks for immediate manual intervention.
- **Compliance-Ready Audit Logs**
  Generates detailed records of every provisioning action, ensuring all access changes are documented for security audits.

---

## Use Cases
**New Hire Provisioning**
- Automatically create email, Slack, and Jira accounts when a candidate is marked as "Hired" in the HRIS.
- Send personalized welcome messages and access instructions to the new hire's personal email.

**Departmental Access Management**
- Assign specific software licenses (e.g., Adobe Creative Cloud, Salesforce) based on the employee's assigned department.
- Update team distribution lists and Slack channels based on the employee's role and location.

**Lifecycle Maintenance**
- Trigger offboarding workflows automatically when an employee's status changes to "Terminated" or "Resigned."
- Revoke access to sensitive internal databases and cloud environments to maintain organizational security.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the `hr-onboarding-orchestrator-by-nango` template file.
3. Connect your HRIS and IT tool integrations via the Composio dashboard.
4. Ensure nodes are correctly mapped to your specific API endpoints and environment variables.

### 2) Setup the Nodes
- **Chat Input**: Receives the new hire's details and onboarding requirements.
- **Agent**: Processes the data and determines the necessary provisioning steps based on the hire's role.
- **Composio Toolset**: Executes the API calls to create accounts and assign permissions across connected platforms.
- **Chat Output**: Confirms successful provisioning or alerts the admin to any configuration errors.

### 3) Run the Flow
Use the Playground to test your onboarding logic with these example prompts:
- `Provision a new hire for the Engineering department with standard developer access.`
- `Onboard John Doe as a Marketing Manager and assign him to the relevant Slack channels.`
- `Check the status of the onboarding workflow for the new Sales hire starting next Monday.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer, interpreting HR data and triggering the correct tool sequences.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on mapping HRIS fields to IT provisioning requirements.
- Define strict error-handling protocols for failed API requests.

### 2) Composio Toolset Node
- Authenticate with your Nango/Composio API key to enable secure connections to your HRIS and IT software.
- Ensure the connection scope includes read access to HRIS data and write access to IT identity management tools.

### 3) Tool Availability
- **HRIS Connector**: Fetching new hire metadata and role definitions.
- **Identity Provider (IdP) Tool**: Creating user accounts and managing group memberships.
- **Communication Toolset**: Sending automated welcome notifications and team alerts.

---

## Related Solutions
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamlined administrative account setup and access management.
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Comprehensive workforce management and onboarding orchestration.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automated CRM account provisioning and configuration for new sales personnel.
