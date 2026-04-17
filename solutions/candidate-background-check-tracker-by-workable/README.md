# Candidate Background Check Tracker (Uplizd) - Automate recruitment compliance and verification

## Summary
The Candidate Background Check Tracker is an intelligent Uplizd AI workflow designed to automate the monitoring, status updates, and compliance tracking of candidate background checks within Workable. By integrating directly with your recruiting stack, this solution eliminates manual status checking, reduces time-to-hire, and ensures a consistent, audit-ready record of all candidate vetting activities.

---

## Demo
![Uplizd AI workflow for tracking candidate background check status in Workable](../image.png)
**Alt text (SEO-ready):** Uplizd AI workflow for tracking candidate background check status in Workable, featuring automated status updates, recruitment compliance monitoring, and Composio tool integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f3010e4b-e50d-5fae-bb60-64a18ca0b08c)

---

## Category
- **Primary category:** Recruiting operations
- **Secondary tags:** `recruiting`, `workable`, `background-check`, `compliance`, `hiring`, `automation`, `composio`, `ai-workflow`
- This solution bridges the gap between candidate screening platforms and your ATS to maintain seamless data hygiene during the hiring process.

---

## Who is this for?
This solution is built for talent acquisition teams and operations managers who need to maintain high velocity without sacrificing compliance.

- **Recruiting Manager**
    - Automates the oversight of pending background checks across the entire candidate pipeline.
- **HR Compliance Officer**
    - Ensures every candidate file contains verified background documentation before the offer stage.
- **Talent Acquisition Specialist**
    - Reduces manual data entry by syncing background check statuses directly into Workable.
- **Operations Coordinator**
    - Provides real-time alerts on stalled background checks to prevent hiring bottlenecks.

---

## Features
- **Automated Status Syncing**
    - Automatically pulls background check results from external providers and updates the corresponding candidate profile in Workable.
- **Compliance Alerting**
    - Triggers real-time notifications when a background check requires manual intervention or fails to meet company standards.
- **Unified Dashboarding**
    - Aggregates background check progress into a single view, allowing teams to track multiple candidates simultaneously.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely authenticate and communicate with Workable and third-party verification APIs.
- **Audit-Ready Logging**
    - Maintains a detailed history of all status changes and verification timestamps for internal and external audits.

---

## Use Cases
**Pipeline Velocity**
- Automatically move candidates to the "Ready for Offer" stage once a background check is marked as "Clear."
- Notify hiring managers instantly when a background check is initiated, ensuring transparency in the hiring timeline.

**Data Hygiene & Compliance**
- Flag candidate profiles that have missing background check documentation to ensure 100% compliance before onboarding.
- Standardize status naming conventions across the recruiting team to prevent duplicate or confusing data entries.

**Exception Management**
- Escalate "Flagged" or "Needs Review" background checks to the HR team via Slack or email immediately upon detection.
- Archive outdated background check requests for candidates who have withdrawn from the hiring process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Workflow" to add the Candidate Background Check Tracker to your Uplizd workspace.
3. Connect your Workable account and any relevant background check provider via the Composio Toolset.
4. Ensure nodes are correctly mapped: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives commands to check status or trigger a new verification request.
- **Agent**: Interprets recruitment intent and manages the logic for status updates.
- **Composio Toolset**: Executes API calls to Workable to fetch or update candidate records.
- **Chat Output**: Returns the current status of the background check or confirmation of the update.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Check the background status for candidate John Doe in the Engineering pipeline.`
- `Update the background check status for all candidates in the 'Pending' stage.`
- `List all candidates who have been waiting for a background check for more than 5 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a recruitment operations assistant.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Instruction: "You are a recruitment operations assistant. Your goal is to verify background check statuses and update Workable records accurately."
- Instruction: "Always confirm the candidate's email or ID before performing an update to ensure data integrity."

### 2) Composio Toolset Node
- Provide your Workable API key and ensure the connection scope includes read/write access to candidate profiles.
- Configure the toolset to handle rate limits if processing large batches of candidates.

### 3) Tool Availability
- `workable_get_candidate`: Fetches current profile details.
- `workable_update_candidate_field`: Updates custom fields related to background check status.
- `background_check_provider_api`: Retrieves verification results.

---

## Related Solutions
- [Account Setup Agent (Salesforce)](../account-setup-agent-by-salesforce/README.md) - Automate CRM account creation and field population.
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline the transition from candidate to employee.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Manage new user access and permissions systematically.
