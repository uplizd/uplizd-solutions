# User Lifecycle Manager (Uplizd) - Automate student and faculty account provisioning

## Summary
The User Lifecycle Manager by D2L Brightspace is an automated AI workflow designed to streamline the onboarding, maintenance, and offboarding of academic users. By synchronizing identity data with learning management systems, this solution ensures data hygiene, reduces manual administrative overhead for IT teams, and maintains a single source of truth for student and faculty access throughout the academic lifecycle.

---

## Demo
![User Lifecycle Manager workflow showing automated account provisioning and status updates in D2L Brightspace](image.png)
**Alt text (SEO-ready):** User Lifecycle Manager (Uplizd) workflow for automated student and faculty account provisioning, identity management, and D2L Brightspace integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d160a433-2642-5297-9799-65d3c1405e17)

---

## Category
**Primary category:** Operations
**Secondary tags:** education, d2l, brightspace, user management, provisioning, identity, automation, composio, ai workflow.
This solution bridges the gap between institutional identity providers and learning management systems to ensure seamless access control.

---

## Who is this for?
This solution is designed for educational administrators and IT operations teams managing large-scale user environments.

*   **IT System Administrator**
    *   Automates repetitive account creation and deactivation tasks to reduce manual ticket volume.
*   **Registrar Office Manager**
    *   Ensures student access to course materials is synchronized with enrollment status in real-time.
*   **Academic Technology Lead**
    *   Maintains strict compliance and data hygiene across institutional learning platforms.
*   **Faculty Operations Coordinator**
    *   Facilitates immediate system access for new staff and instructors during onboarding windows.

---

## Features
- **Automated Provisioning**
    Real-time creation of user accounts based on enrollment triggers, reducing the time from registration to system access.
- **Lifecycle Synchronization**
    Automatically updates user roles and permissions in D2L Brightspace as students move through academic terms.
- **Identity Data Hygiene**
    Cleans and standardizes user profile information to prevent duplicate accounts and ensure accurate reporting.
- **Secure Offboarding**
    Triggers automated account suspension or archival upon graduation or contract termination to maintain system security.
- **Composio-Powered Integration**
    Leverages the Composio Toolset to bridge D2L Brightspace APIs with external identity management systems for seamless data flow.

---

## Use Cases
**New Semester Onboarding**
*   Bulk provisioning of student accounts based on course registration data.
*   Automatic assignment of faculty to specific course shells based on department rosters.

**Mid-Term Status Changes**
*   Updating user permissions when a student changes their major or academic standing.
*   Syncing leave-of-absence status to temporarily restrict platform access while preserving data.

**End-of-Cycle Offboarding**
*   Archiving user activity logs and disabling access for graduated students.
*   Revoking system credentials for departing faculty members to ensure data privacy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the User Lifecycle Manager template from the solution library.
3. Connect your D2L Brightspace API credentials within the integration settings.
4. Ensure nodes are correctly mapped to your specific institutional domain and user schema.

### 2) Setup the Nodes
*   **Chat Input**: Receives triggers from your identity provider or manual administrative requests.
*   **Agent**: Processes the user lifecycle logic and determines the necessary provisioning action.
*   **Composio Toolset**: Executes the specific API calls to D2L Brightspace for user creation, update, or deletion.
*   **Chat Output**: Confirms the successful execution of the lifecycle event or flags errors for manual review.

### 3) Run the Flow
Use the Playground to test your lifecycle triggers:
*   `Provision new student account for user ID 98765 in the Fall 2024 semester.`
*   `Update faculty permissions for instructor John Doe to reflect department change to Science.`
*   `Deactivate user account for student ID 12345 due to graduation.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer for identity logic.
*   Instruction: "You are an identity management assistant. Verify user status against the provided enrollment data before executing any D2L Brightspace API calls."
*   Instruction: "Prioritize security by ensuring that account deactivations are processed immediately upon receipt of termination signals."
*   Instruction: "Log all provisioning actions with a timestamp and user ID for audit compliance."

### 2) Composio Toolset Node
*   **API Key**: Provide your D2L Brightspace API key and secret.
*   **Connection Scope**: Ensure the connection has read/write permissions for the User and Course management endpoints.

### 3) Tool Availability
*   `d2l_create_user`: Creates new user profiles.
*   `d2l_update_user_role`: Modifies access levels and permissions.
*   `d2l_deactivate_user`: Suspends account access.
*   `d2l_get_user_status`: Retrieves current account state for verification.

---

## Related Solutions
*   [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - Streamlines employee onboarding and access management.
*   [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automates account configuration and setup tasks.
*   [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Simplifies the onboarding process for administrative user roles.
