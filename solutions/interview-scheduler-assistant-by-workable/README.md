# Interview Scheduler Assistant (Uplizd) - Automate candidate scheduling and interview coordination

## Summary
The Interview Scheduler Assistant streamlines the recruitment lifecycle by automating the coordination of interview slots between hiring teams and candidates. By integrating directly with Workable and your calendar infrastructure, this Uplizd AI workflow eliminates manual back-and-forth communication, reduces scheduling friction, and ensures a seamless candidate experience from initial screening to final interview.

---

## Demo
![Interview Scheduler Assistant workflow showing candidate data processing and calendar synchronization](image.png)
**Alt text (SEO-ready):** Interview Scheduler Assistant workflow for Uplizd, automating candidate interview scheduling, Workable integration, and calendar management.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhL7dExDQAgEAMw+B+9Bw8QkSgqC/yJpG0tM8/7CgAAgJ+11gIAAPyv1loLAADwX1trLQAAv9daCwAA8F9rLQAA/P8A1JkH/c25s+gAAAAASUVORK5CYII=)](https://uplizd.ai/solutions/3a5c33f0-8a74-5955-8899-5b55ff1cd6d8)

---

## Category
**Primary category:** Recruiting operations
**Secondary tags:** `workable`, `scheduling`, `recruitment`, `candidate experience`, `hr automation`, `composio`, `calendar sync`, `ai workflow`

This solution optimizes talent acquisition workflows by bridging the gap between applicant tracking systems and real-time calendar availability.

---

## Who is this for?
This assistant is designed for HR and recruitment teams looking to scale their hiring velocity without increasing administrative overhead.

*   **Recruitment Coordinator**
    *   Automates the tedious task of aligning candidate availability with interviewer schedules.
*   **Hiring Manager**
    *   Receives instant calendar invites for qualified candidates without manual coordination.
*   **Talent Acquisition Lead**
    *   Reduces time-to-hire metrics by eliminating scheduling bottlenecks in the pipeline.
*   **HR Operations Specialist**
    *   Ensures consistent scheduling hygiene and data accuracy across the Workable platform.

---

## Features
- **Automated Availability Matching**
    Cross-references interviewer calendar blocks with candidate preferences to propose optimal meeting times.
- **Workable Integration**
    Directly pulls candidate details and interview requirements from Workable to trigger scheduling workflows.
- **Real-time Calendar Sync**
    Uses the Composio Toolset to push confirmed interview slots directly into Google or Outlook calendars.
- **Candidate Communication Loop**
    Generates personalized, professional interview invitations and confirmation emails automatically.
- **Scheduling Conflict Resolution**
    Proactively identifies and flags scheduling overlaps, suggesting alternative slots to maintain pipeline momentum.

---

## Use Cases
**High-Volume Hiring**
*   Batch scheduling for initial screening calls across multiple open roles.
*   Automated rescheduling for candidates who need to adjust their interview time.

**Executive Search Coordination**
*   Managing complex, multi-stage interview panels involving multiple stakeholders.
*   Syncing high-priority interview slots with executive calendars to prevent double-booking.

**Candidate Experience Optimization**
*   Sending automated calendar links to candidates to allow self-selection of interview times.
*   Providing instant confirmation and meeting details to reduce candidate drop-off rates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your Workable and Calendar accounts via the integration settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the candidate's profile and interview request details.
*   **Agent**: Interprets the scheduling requirements and determines the best time slots.
*   **Composio Toolset**: Executes the API calls to Workable and your calendar provider.
*   **Chat Output**: Confirms the scheduled interview details to the recruiter and candidate.

### 3) Run the Flow
Use the Playground to test your scheduling logic with these prompts:
* `Schedule a 30-minute screening call for candidate John Doe with the engineering team for next Tuesday.`
* `Check availability for the hiring manager and propose three time slots for the final interview round.`
* `Reschedule the interview for Jane Smith to Thursday afternoon and update the Workable status.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the scheduling coordinator, ensuring all constraints are met.
*   Prioritize interviewer availability over candidate preferences when conflicts arise.
*   Maintain a professional, welcoming tone in all candidate-facing communications.
*   Always verify the candidate's current stage in Workable before proposing a meeting.

### 2) Composio Toolset Node
Requires an active API key with permissions for Workable and your primary Calendar service (Google/Outlook). Ensure the connection scope includes read/write access for events and candidate records.

### 3) Tool Availability
*   **Workable API**: Retrieve candidate data, update interview status, and log notes.
*   **Calendar API**: Query free/busy status, create events, and send calendar invites.
*   **Notification Service**: Trigger email alerts for interview confirmations.

---

## Related Solutions
* [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Streamlines new account creation and data entry.
* [Workforce Onboarding Automator by Connecteam](../workforce-onboarding-automator-by-connecteam/README.md) - Automates the transition from candidate to employee.
* [Workflow Automation Agent by Jobnimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Manages end-to-end business process automation.
