# Directory User Cleanup Agent (Uplizd) - Automate user lifecycle management and directory hygiene

## Summary
The Directory User Cleanup Agent is an intelligent workflow designed to maintain pristine directory data by identifying and removing inactive, duplicate, or unauthorized user accounts. By leveraging the Composio Toolset to interface with your directory services, this agent ensures your organizational data remains accurate, secure, and compliant, reducing manual administrative overhead and mitigating security risks associated with stale user access.

---

## Demo
![Directory User Cleanup Agent dashboard showing automated user identification and deletion workflow](image.png)
**Alt text (SEO-ready):** Directory User Cleanup Agent dashboard showing automated user identification and deletion workflow, Uplizd AI automation, directory management, and user data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/46e080ef-b00d-57f1-ac9e-590f343e6f59)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** directory management, user lifecycle, data hygiene, automation, identity security, composio, ai workflow
- This solution streamlines identity governance by automating the identification and cleanup of stale user accounts within your directory infrastructure.

---

## Who is this for?
This agent is designed for IT and Operations teams tasked with maintaining secure and organized user directories.

- **IT Administrators**
    - Automate the offboarding process to ensure immediate access revocation for terminated employees.
- **Security Officers**
    - Reduce the attack surface by identifying and purging dormant accounts that pose potential security vulnerabilities.
- **Operations Managers**
    - Maintain accurate directory counts to optimize software licensing costs and resource allocation.
- **HR Systems Specialists**
    - Ensure directory data integrity by reconciling active employee lists with current directory entries.

---

## Features
- **Automated Inactivity Detection**
    - Scans directory logs to flag user accounts that have not authenticated within a defined threshold period.
- **Duplicate Account Identification**
    - Uses intelligent matching algorithms to detect and consolidate redundant user profiles sharing identical identifiers.
- **Secure Deletion Workflows**
    - Executes controlled removal of stale accounts with built-in confirmation steps to prevent accidental data loss.
- **Compliance Reporting**
    - Generates audit-ready logs detailing every cleanup action taken, ensuring full transparency for security audits.
- **Composio-Powered Integration**
    - Seamlessly connects with directory services via the Composio Toolset for real-time, API-driven management.

---

## Use Cases
**Lifecycle Management**
- Automatically flag and disable accounts for users who have not logged in for over 90 days.
- Sync offboarding status from HR systems to trigger immediate directory cleanup.

**Data Hygiene**
- Identify and merge duplicate user entries created by legacy system migrations.
- Standardize user naming conventions by detecting and flagging accounts that deviate from corporate policy.

**Security & Compliance**
- Audit directory access to ensure only active, authorized personnel maintain system permissions.
- Maintain a clean directory environment to pass periodic security and data privacy compliance checks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Directory User Cleanup Agent template from the solution library.
3. Connect your directory service provider via the Composio Toolset integration.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled cleanup commands.
- **Agent**: Processes directory data and applies cleanup logic based on your defined rules.
- **Composio Toolset**: Executes the API calls to query, flag, and remove directory users.
- **Chat Output**: Provides a summary report of all actions performed during the cleanup cycle.

### 3) Run the Flow
Use the Playground to test your cleanup logic:
- `Identify all users inactive for more than 180 days and list them for review.`
- `Find and report duplicate accounts based on email address.`
- `Run a full cleanup cycle for all accounts marked as 'terminated' in the directory.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision engine for your directory hygiene strategy.
- Focus on identifying anomalies in user activity patterns.
- Prioritize safety by requiring confirmation for deletion tasks.
- Maintain a neutral, professional tone in all audit reports.

### 2) Composio Toolset Node
- Provide your API credentials for the target directory service.
- Ensure the connection scope includes read/write permissions for user management endpoints.

### 3) Tool Availability
- **User Querying**: Capability to fetch user metadata and last-login timestamps.
- **Account Modification**: Ability to disable or update user status flags.
- **Deletion Protocols**: Secure execution of account removal based on verified criteria.

---

## Related Solutions
- [../admin-user-access-auditor-by-storeganise/README.md](../admin-user-access-auditor-by-storeganise/README.md) — Monitor and audit administrative user access levels.
- [../admin-user-onboarding-assistant-by-storeganise/README.md](../admin-user-onboarding-assistant-by-storeganise/README.md) — Automate the provisioning and onboarding of new directory users.
- [../account-audit-agent-by-cloudflare/README.md](../account-audit-agent-by-cloudflare/README.md) — Perform comprehensive security audits on organizational accounts.
