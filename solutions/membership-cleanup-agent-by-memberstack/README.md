# Membership Cleanup Agent (Uplizd) - Automate member lifecycle and data hygiene

## Summary
The Membership Cleanup Agent is an intelligent workflow designed to automate the identification, verification, and removal of inactive or non-compliant user accounts within Memberstack. By leveraging the Composio Toolset, this agent streamlines administrative overhead, ensures data hygiene, and maintains platform security by programmatically auditing membership status and executing cleanup tasks based on predefined inactivity thresholds.

---

## Demo
![Membership Cleanup Agent workflow diagram showing Chat Input, Agent, Memberstack Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Uplizd Membership Cleanup Agent workflow for Memberstack, automating user account management and data hygiene via AI-driven Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/52e07b92-22b9-5742-b3a6-5440429e4e67)

---

## Category
**Primary category:** Operations
**Secondary tags:** memberstack, data hygiene, user management, automation, account cleanup, composio, ai workflow, crm
This solution bridges the gap between manual administrative tasks and automated platform maintenance to ensure your membership database remains accurate and optimized.

---

## Who is this for?
This solution is designed for operations teams and community managers who need to maintain a clean, active user base without manual intervention.

*   **Community Manager**
    *   Automates the removal of spam or inactive accounts to maintain high-quality member engagement metrics.
*   **Operations Lead**
    *   Ensures compliance with data retention policies by programmatically auditing and cleaning up stale user records.
*   **Platform Administrator**
    *   Reduces manual workload by triggering bulk cleanup tasks based on last-login timestamps or custom membership fields.
*   **Growth Marketer**
    *   Maintains accurate audience lists by ensuring only active, verified members are included in marketing segments.

---

## Features
- **Automated Inactivity Detection**
    Analyzes member metadata to identify accounts that have not logged in within a specified timeframe.
- **Bulk Cleanup Execution**
    Safely processes large volumes of account deletions or status updates using the Memberstack API via Composio.
- **Customizable Cleanup Rules**
    Allows users to define specific criteria for "inactive" status, such as last login date, email verification status, or custom field values.
- **Audit Logging**
    Generates a summary report of all actions taken, providing transparency and a record of cleaned accounts.
- **Real-time Integration**
    Connects directly to your Memberstack environment to ensure that changes are reflected immediately across your platform.

---

## Use Cases
**Lifecycle Management**
*   Automatically archive accounts that have been inactive for more than 90 days.
*   Flag members with unverified email addresses for follow-up or automated removal.

**Data Hygiene & Compliance**
*   Perform bulk cleanup of test or duplicate accounts created during development phases.
*   Ensure GDPR compliance by programmatically purging data for users who have requested account deletion.

**Engagement Optimization**
*   Identify and remove "ghost" members to improve the accuracy of community engagement analytics.
*   Sync membership status updates with external CRM tools to keep cross-platform data consistent.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" link above to open the solution template.
2. Select your preferred workspace and project to import the workflow.
3. Connect your Memberstack API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives your natural language request to initiate a cleanup task.
*   **Agent**: Processes the cleanup logic using LLM instructions to interpret inactivity criteria.
*   **Composio Toolset**: Executes secure API calls to Memberstack to fetch and modify user data.
*   **Chat Output**: Returns a confirmation summary of the cleanup operation performed.

### 3) Run the Flow
Use the Playground to trigger the agent with prompts such as:
* `Find all members who haven't logged in for 6 months and flag them for review.`
* `Delete all accounts with the status 'unverified' created before January 1st.`
* `Generate a report of all inactive members and remove those without active subscriptions.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the decision-making engine for your cleanup logic.
*   Define the inactivity threshold clearly in the system prompt.
*   Instruct the agent to prioritize safety by listing accounts before executing bulk deletions.
*   Ensure the agent is configured to handle API rate limits by processing records in batches.

### 2) Composio Toolset Node
*   **API Key**: Provide your Memberstack API key to authorize the agent.
*   **Connection Scope**: Ensure the connection has read/write permissions for the Memberstack Members API.

### 3) Tool Availability
*   `memberstack_list_members`: Retrieve member data for analysis.
*   `memberstack_delete_member`: Execute removal of identified inactive accounts.
*   `memberstack_update_member`: Modify member metadata or status fields.

---

## Related Solutions
* [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) - Automate new user provisioning and account configuration.
* [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Streamline the administrative onboarding process for new platform users.
* [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain clean and accurate records across your CRM ecosystem.
