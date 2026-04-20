# User Data Cleanup Agent (Uplizd) - Automated Canny user data hygiene and compliance

## Summary
The User Data Cleanup Agent is an automated workflow designed to maintain data integrity and privacy compliance within your Canny workspace. By leveraging the Composio Toolset, this Uplizd solution identifies stale, duplicate, or non-compliant user records and executes cleanup actions, ensuring your product feedback pipeline remains accurate, performant, and aligned with data retention policies.

---

## Demo
![User Data Cleanup Agent workflow dashboard showing automated Canny record processing and data validation steps](image.png)
**Alt text (SEO-ready):** User Data Cleanup Agent workflow for Canny, featuring automated data hygiene, record deduplication, and privacy compliance monitoring via Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/909d5d58-53f8-5541-8ec1-a5b15c8cb4ea)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** canny, user data, compliance, automation, data cleanup, crm, composio, ai workflow
- This solution streamlines the maintenance of user feedback platforms by automating the identification and removal of redundant or outdated records.

---

## Who is this for?
This solution is designed for teams managing high-volume feedback channels who need to maintain strict data standards without manual intervention.

- **Product Operations Manager**
    - Automates the removal of inactive user accounts to keep feedback metrics focused on active customers.
- **Data Privacy Officer**
    - Ensures compliance with GDPR and CCPA by automating the deletion or anonymization of requested user data.
- **Customer Success Lead**
    - Maintains a clean feedback environment, ensuring support teams interact with current and relevant user profiles.
- **Systems Administrator**
    - Reduces technical debt by syncing and purging redundant user records across integrated feedback and CRM systems.

---

## Features
- **Automated Record Auditing**
    - Scans Canny user databases in real-time to flag accounts that meet specific inactivity or duplication criteria.
- **Compliance-Aware Deletion**
    - Executes secure data removal protocols, ensuring that user deletion requests are processed accurately and logged for audit trails.
- **Intelligent Deduplication**
    - Merges or removes duplicate user entries based on email or unique identifiers to prevent fragmented feedback history.
- **Customizable Retention Rules**
    - Allows users to define specific time-based triggers for data cleanup, such as purging accounts inactive for over 12 months.
- **Composio-Powered Integration**
    - Utilizes the Composio Toolset to securely interface with Canny APIs, providing reliable, authenticated data manipulation.

---

## Use Cases
**Data Privacy & Compliance**
- Automatically process "Right to be Forgotten" requests by locating and purging all associated user feedback records.
- Enforce data retention policies by identifying and archiving user data that exceeds defined organizational storage limits.

**Feedback Pipeline Hygiene**
- Identify and merge duplicate user profiles created by cross-platform sign-ins to consolidate feedback history.
- Remove test or spam accounts that clutter product feedback boards and skew user sentiment analysis.

**Operational Efficiency**
- Schedule recurring cleanup tasks to prevent database bloat and maintain optimal performance in your Canny environment.
- Automatically flag and notify administrators of suspicious user activity or anomalous data patterns for manual review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and project destination.
3. Authenticate your Canny account via the Composio connection prompt.
4. Ensure nodes are correctly mapped and the API credentials are active in the configuration panel.

### 2) Setup the Nodes
- **Chat Input**: Receives manual triggers or scheduled cleanup commands from the user.
- **Agent**: Analyzes the Canny database against defined cleanup criteria and determines the necessary actions.
- **Composio Toolset**: Executes the API calls to fetch, merge, or delete user records within Canny.
- **Chat Output**: Returns a summary report of all processed, deleted, or merged user records to the user.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Identify and list all users inactive for more than 365 days.`
- `Find and merge duplicate user profiles associated with the same email domain.`
- `Run a full compliance audit and purge all records flagged for deletion.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making layer for your data hygiene strategy.
- Set the system prompt to prioritize data safety and strict adherence to the provided cleanup rules.
- Enable "Tool Use" mode to allow the agent to invoke the Composio Toolset.
- Configure the temperature to 0.0 to ensure deterministic, consistent data processing results.

### 2) Composio Toolset Node
- Provide your Canny API key within the Composio connection settings.
- Ensure the connection scope includes read/write permissions for user and feedback objects.

### 3) Tool Availability
- `canny_list_users`: Fetch user records for audit.
- `canny_delete_user`: Execute secure record removal.
- `canny_merge_users`: Consolidate duplicate profiles.
- `canny_get_user_details`: Retrieve specific metadata for compliance verification.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research on customer accounts.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Comprehensive data cleaning for enterprise CRM systems.
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Manages and purges stale action items across workflows.
