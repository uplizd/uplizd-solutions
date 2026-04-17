# Client Training Coordinator (Uplizd) - Automate client onboarding and learning progress tracking

## Summary
The Client Training Coordinator is an intelligent Uplizd workflow designed to bridge the gap between client management and educational delivery. By integrating with Coassemble, this solution automates the assignment of training modules, tracks learner progress in real-time, and triggers personalized follow-ups, ensuring high engagement and consistent onboarding outcomes for customer success teams.

---

## Demo
![Client Training Coordinator workflow interface showing Coassemble integration nodes and automated progress tracking logic](../image.png)
**Alt text (SEO-ready):** Client Training Coordinator Uplizd workflow, Coassemble integration, automated learner progress tracking, and customer onboarding automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7009b85a-37e1-5489-a3dc-49546ed3e68e)

---

## Category
**Primary category:** Operations  
**Secondary tags:** `coassemble`, `learning management`, `lms`, `client onboarding`, `customer success`, `automation`, `composio`, `ai workflow`

This solution streamlines the delivery of educational content by automating manual administrative tasks within your Learning Management System.

---

## Who is this for?
This solution is designed for teams managing high-volume client education and onboarding programs.

- **Customer Success Manager**
    - Automate training module assignments based on client lifecycle stages to ensure timely product adoption.
- **Learning & Development Lead**
    - Monitor aggregate learner progress and identify knowledge gaps through automated reporting and alerts.
- **Onboarding Specialist**
    - Eliminate manual data entry between your CRM and Coassemble by syncing user enrollment status automatically.
- **Client Support Representative**
    - Proactively assist clients who have stalled in their training path by triggering personalized check-in emails.

---

## Features
- **Automated Enrollment Triggers**
    - Instantly enroll clients in specific Coassemble courses based on triggers from your CRM or project management tools.
- **Real-time Progress Syncing**
    - Maintain a single source of truth by syncing completion data from Coassemble back to your central database.
- **Intelligent Follow-up Logic**
    - Deploy AI-driven reminders to learners who have not accessed their training modules within a specified timeframe.
- **Customized Learning Paths**
    - Dynamically assign training modules based on user roles, industry, or specific product feature sets.
- **Performance Analytics Reporting**
    - Generate automated summaries of training engagement metrics to help leadership assess the effectiveness of onboarding.

---

## Use Cases
**Client Onboarding Optimization**
- Automatically trigger a "Welcome to the Platform" training sequence the moment a new account is marked as 'Closed-Won'.
- Assign specialized technical training modules based on the specific product tier purchased by the client.

**Learner Engagement & Retention**
- Send personalized nudges via email or Slack to users who have completed 50% of their curriculum but have been inactive for 7 days.
- Celebrate milestone achievements by triggering automated congratulatory messages upon the completion of certification courses.

**Data-Driven Success Management**
- Aggregate training completion data to provide Customer Success Managers with a 'Health Score' based on product proficiency.
- Identify common drop-off points in training modules to inform future content updates and curriculum improvements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace to import the pre-configured workflow.
3. Connect your Coassemble and CRM accounts via the Composio Toolset.
4. Ensure nodes are correctly mapped and all API credentials are authenticated in the settings panel.

### 2) Setup the Nodes
- **Chat Input**: Receives commands or triggers regarding client status updates.
- **Agent**: Processes enrollment logic and evaluates learner progress against defined milestones.
- **Composio Toolset**: Executes API calls to Coassemble to fetch course data and update user statuses.
- **Chat Output**: Returns confirmation of enrollment, progress summaries, or alerts regarding stalled learners.

### 3) Run the Flow
Use the Playground to test your workflow with these example prompts:
- `Check the training progress for client 'Acme Corp' and list any incomplete modules.`
- `Enroll all new users from the 'Enterprise' segment into the 'Advanced Admin' training track.`
- `Send a reminder to all clients who haven't logged into their Coassemble portal in the last 14 days.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for your training operations.
- **Role:** Customer Success Automation Assistant.
- **Instruction Pattern:**
    - Always verify the client's current onboarding stage before suggesting new training assignments.
    - Prioritize data accuracy when syncing completion status between Coassemble and the CRM.
    - Maintain a helpful and encouraging tone when drafting automated follow-up communications.

### 2) Composio Toolset Node
- **API Key:** Provide your Coassemble API key to enable secure access to your learning environment.
- **Connection Scope:** Ensure the token has read/write permissions for user management and course enrollment modules.

### 3) Tool Availability
- **User Management:** Create, update, and retrieve learner profiles.
- **Course Enrollment:** Assign and track progress for specific learning modules.
- **Analytics Fetcher:** Retrieve completion percentages and last-access timestamps.
- **Notification Dispatcher:** Trigger automated emails or Slack alerts based on learner activity.

---

## Related Solutions
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automate initial account configurations and user provisioning.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform task management and project workflows.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track usage metrics to proactively manage account health and retention.
