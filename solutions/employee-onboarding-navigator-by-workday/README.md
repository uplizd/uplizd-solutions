# Employee Onboarding Navigator (Uplizd) - Streamline new hire setup in Workday

## Summary
The Employee Onboarding Navigator is an intelligent Uplizd AI workflow designed to automate and simplify the new hire experience within Workday. By acting as a personalized guide, the agent assists employees in completing mandatory profile setup, training modules, and documentation tasks, significantly reducing HR administrative overhead and accelerating time-to-productivity for new team members.

---

## Demo
![Employee Onboarding Navigator workflow showing Chat Input, Agent, Workday Composio Toolset, and Chat Output nodes](image.png)

**Alt text (SEO-ready):** Employee Onboarding Navigator Uplizd workflow for Workday automation, HR onboarding assistance, and automated employee task management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/7113a2a5-353f-50c0-ac95-25b78d7b7da7)

---

## Category
**Primary category:** HR Operations  
**Secondary tags:** onboarding, workday, employee experience, hr automation, workflow, composio, ai agent, task management.  
This solution bridges the gap between complex HR systems and new hire requirements to ensure a seamless, automated onboarding journey.

---

## Who is this for?
The Employee Onboarding Navigator is designed to support organizations looking to modernize their HR workflows and improve new hire engagement.

- **HR Managers**
    - Automate routine onboarding inquiries and reduce manual support tickets.
- **New Hires**
    - Receive real-time, personalized guidance through complex Workday setup processes.
- **IT Administrators**
    - Ensure consistent provisioning and compliance across all new employee accounts.
- **Operations Leads**
    - Gain visibility into onboarding bottlenecks and track completion rates of essential tasks.

---

## Features
- **Personalized Onboarding Paths**
    - Tailors guidance based on the employee's role, department, and specific Workday requirements.
- **Workday Integration**
    - Leverages the Composio Toolset to securely interact with Workday APIs for real-time task updates.
- **Proactive Task Reminders**
    - Automatically identifies incomplete profile fields or pending training and nudges the user to complete them.
- **Compliance Monitoring**
    - Ensures all mandatory documentation is signed and uploaded, maintaining audit-ready employee records.
- **Natural Language Interface**
    - Allows employees to ask questions about their onboarding status in plain language, reducing the need for manual HR intervention.

---

## Use Cases
**New Hire Setup**
- Guiding employees through the initial Workday profile configuration and emergency contact entry.
- Automating the enrollment process for mandatory company benefits and payroll information.

**Training & Compliance**
- Tracking completion status of mandatory security and compliance training modules within Workday.
- Sending automated reminders for pending document signatures or policy acknowledgments.

**HR Support Automation**
- Answering common onboarding FAQs regarding company equipment, office access, and team structure.
- Escalating complex HR queries to human agents only when the AI cannot resolve the request.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Employee Onboarding Navigator JSON configuration.
3. Connect your Workday API credentials via the Composio Toolset.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the new hire's questions or status update requests.
- **Agent**: Processes intent and queries Workday for relevant employee data.
- **Composio Toolset**: Executes secure API calls to retrieve or update Workday records.
- **Chat Output**: Delivers clear, actionable instructions back to the employee.

### 3) Run the Flow
Open the Playground and test the following prompts:
- `What tasks do I need to complete in Workday for my first week?`
- `I have finished my benefits enrollment, can you verify if it's submitted?`
- `How do I update my emergency contact information in the system?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the HR assistant, maintaining a helpful and professional tone.
- Instruction: "You are an HR Onboarding Assistant. Use the provided Workday tools to look up employee tasks."
- Instruction: "Always verify the employee's identity before accessing sensitive profile data."
- Instruction: "Provide step-by-step instructions for any Workday task the user needs to complete."

### 2) Composio Toolset Node
- Requires a valid Workday API key with permissions for employee profile and task management.
- Ensure the connection scope is limited to the necessary HR modules to maintain data security.

### 3) Tool Availability
- **Workday Profile Reader**: Fetches current employee status and pending task lists.
- **Workday Task Updater**: Marks specific onboarding milestones as complete.
- **Notification Service**: Triggers alerts for missing documentation or approaching deadlines.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline general workforce onboarding and task management.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Automate account provisioning and configuration workflows.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Manage administrative access and user setup processes.
