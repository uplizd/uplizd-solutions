# Benefits Enrollment Advisor (Uplizd) - Automated HR benefits guidance and enrollment assistance

## Summary
The Benefits Enrollment Advisor is an intelligent Uplizd workflow designed to streamline the employee benefits selection process. By integrating directly with HR platforms like BambooHR, this AI-driven solution provides personalized plan recommendations, answers complex policy questions, and assists employees with enrollment tasks, ensuring a frictionless experience that reduces HR administrative overhead and improves employee satisfaction.

---

## Demo
![Benefits Enrollment Advisor workflow interface showing AI-driven plan recommendations and BambooHR integration](../image.png)
**Alt text (SEO-ready):** Benefits Enrollment Advisor Uplizd workflow for HR automation, personalized benefits recommendations, and BambooHR integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/247aeb49-0262-5eda-923c-910f11ed110b)

---

## Category
- **Primary category:** HR Operations
- **Secondary tags:** hr, bamboohr, benefits, employee experience, automation, ai workflow, composio, enrollment
- This solution bridges the gap between complex HR policy documentation and employee-facing support through automated data retrieval and guidance.

---

## Who is this for?
This solution is designed for organizations looking to modernize their HR service delivery and empower employees with self-service tools.

- **HR Managers**
    - Automate routine benefits inquiries to focus on high-value employee relations and strategy.
- **Benefits Administrators**
    - Ensure consistent, policy-compliant guidance is provided to every employee during open enrollment.
- **Employees**
    - Receive instant, personalized answers regarding coverage options without waiting for HR availability.
- **Operations Leads**
    - Reduce the volume of repetitive support tickets and streamline the data entry process for new enrollments.

---

## Features
- **Personalized Plan Matching**
    - Uses AI to analyze employee profiles and suggest the most relevant benefit packages based on individual needs.
- **HR Platform Integration**
    - Leverages the Composio Toolset to securely query and update employee records directly within BambooHR.
- **Real-Time Policy Q&A**
    - Provides instant, accurate responses to benefits-related questions by referencing your organization's specific policy documents.
- **Guided Enrollment Assistance**
    - Walks users through the enrollment steps, ensuring all required fields are completed accurately to prevent processing delays.
- **Automated Status Notifications**
    - Triggers updates and confirmations as employees progress through their enrollment journey, keeping all stakeholders informed.

---

## Use Cases
**Open Enrollment Support**
- Providing 24/7 assistance to employees comparing health, dental, and vision plan options.
- Automating the collection of beneficiary information and dependent details during the annual enrollment window.

**New Hire Onboarding**
- Guiding new employees through their initial benefits selection process during their first week.
- Answering common questions about waiting periods, eligibility, and coverage start dates.

**Benefits Policy Clarification**
- Interpreting complex HR policy language into simple, actionable summaries for employees.
- Resolving common inquiries regarding "Life Event" changes and how they impact current coverage.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Benefits Enrollment Advisor template from the solution library.
3. Connect your BambooHR API credentials within the integration settings.
4. Ensure nodes are properly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives employee questions or enrollment requests.
*   **Agent**: Processes natural language queries and determines the necessary HR actions.
*   **Composio Toolset**: Executes secure API calls to fetch or update data in BambooHR.
*   **Chat Output**: Delivers personalized recommendations and enrollment confirmation to the user.

### 3) Run the Flow
Test the workflow in the Uplizd Playground using these example prompts:
- `What are the key differences between the Gold and Silver health plans?`
- `I just got married, how do I update my benefits coverage?`
- `Can you help me enroll in the company dental plan?`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an empathetic and knowledgeable HR assistant.
- **Recommended instruction pattern:**
    - Act as a professional HR Benefits Advisor.
    - Only provide information based on the provided policy documents and BambooHR data.
    - If a request requires manual HR approval, clearly inform the user of the next steps.

### 2) Composio Toolset Node
- Requires a valid BambooHR API key with read/write permissions for employee benefits and profile modules.
- Ensure the connection scope is limited to the specific HR modules required for enrollment.

### 3) Tool Availability
- `bamboohr_get_employee_details`: Retrieve current plan information.
- `bamboohr_update_benefits`: Submit enrollment changes.
- `policy_search_tool`: Query internal benefits documentation.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamline new hire documentation and system access.
- [Admin User Onboarding Assistant](../admin-user-onboarding-assistant-by-storeganise/README.md) - Automate administrative account setup and permissions.
- [Work Hours Compliance Monitor](../work-hours-compliance-monitor-by-timely/README.md) - Track and report on employee time-tracking compliance.
