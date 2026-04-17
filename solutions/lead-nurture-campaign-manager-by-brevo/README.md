# Lead Nurture Campaign Manager (Uplizd) - Automated personalized email sequences for lead conversion

## Summary
The Lead Nurture Campaign Manager (Uplizd) is an intelligent automation workflow designed to streamline lead engagement by orchestrating personalized email sequences. By leveraging the Composio Toolset to integrate with Brevo, this solution enables marketing and sales teams to maintain consistent communication, improve lead velocity, and ensure no prospect falls through the cracks, ultimately driving higher conversion rates through automated, data-driven outreach.

---

## Demo
![Lead Nurture Campaign Manager workflow showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Lead Nurture Campaign Manager Uplizd workflow for automated email sequences using Brevo and Composio Toolset integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bf167d06-fd1c-5e32-904c-bdcae5afb33d)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** lead nurturing, email marketing, brevo, sales automation, drip campaigns, conversion, composio, ai workflow
- This solution bridges the gap between raw lead data and active engagement by automating the delivery of tailored content through your preferred email marketing platform.

---

## Who is this for?
This solution is designed for professionals focused on maximizing lead value and operational efficiency.

- **Marketing Manager**
    - Automate multi-stage nurture tracks to ensure consistent brand messaging without manual intervention.
- **Sales Development Representative (SDR)**
    - Focus on high-intent leads while the system handles the initial warming and follow-up sequences.
- **RevOps Specialist**
    - Standardize lead communication protocols across the organization to improve pipeline hygiene and data accuracy.
- **Growth Marketer**
    - Rapidly deploy and test new email campaign variations to optimize conversion rates across different lead segments.

---

## Features
- **Automated Sequence Orchestration**
    - Dynamically trigger and manage multi-step email nurture flows based on real-time lead status updates.
- **Personalized Content Injection**
    - Utilize AI-driven logic to customize email subject lines and body copy based on lead profile attributes.
- **Brevo Integration**
    - Seamlessly sync lead data and campaign triggers with Brevo via the Composio Toolset for reliable delivery.
- **Real-time Lead Sync**
    - Maintain a single source of truth by updating lead engagement status across your CRM and marketing platforms.
- **Intelligent Campaign Monitoring**
    - Track engagement signals and automatically adjust follow-up cadences to match lead responsiveness.

---

## Use Cases
**Lead Lifecycle Management**
- Automatically enroll new leads into a 5-day welcome sequence upon form submission.
- Update lead status in the CRM based on email open and click-through activity.

**Personalized Outreach**
- Generate custom email content based on industry-specific pain points identified in the lead profile.
- Tailor follow-up timing based on the lead's timezone and previous interaction history.

**Operational Efficiency**
- Clean up inactive lead lists by triggering re-engagement campaigns for stale contacts.
- Standardize email formatting and compliance checks across all automated marketing communications.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and project to initialize the workflow.
3. Authenticate your Brevo account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives lead data and campaign parameters.
- **Agent**: Processes lead intent and drafts personalized email content.
- **Composio Toolset**: Executes API calls to Brevo to send emails and update contact lists.
- **Chat Output**: Confirms successful campaign initiation or logs errors for review.

### 3) Run the Flow
Use the Playground to test your nurture sequences with these prompts:
- `Enroll the new lead from the 'Q3 Webinar' list into the standard nurture sequence.`
- `Draft and send a personalized follow-up email to the lead with ID 98765 based on their recent interest in our enterprise plan.`
- `Check the status of the current nurture campaign for the 'Tech-Startups' segment and report any delivery failures.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the brain of the operation, interpreting lead data and generating context-aware communication.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5) for optimal content generation.
- Ensure the system prompt includes clear instructions on brand voice and email compliance.
- Set temperature to 0.7 to balance creativity with professional tone.

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable secure communication with external services.
- Ensure the connection scope includes `brevo:send_email` and `brevo:update_contact` permissions.

### 3) Tool Availability
- **Brevo API**: For sending emails, managing contact lists, and tracking campaign metrics.
- **CRM Connector**: For fetching lead attributes and updating lifecycle stages.
- **Data Formatter**: For cleaning and normalizing lead information before campaign entry.

---

## Related Solutions
- [../account-health-compliance-monitor-by-brevo/README.md](../account-health-compliance-monitor-by-brevo/README.md) - Monitor and maintain account health compliance using Brevo data.
- [../whats-app-lead-nurturing-agent-by-spoki/README.md](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Manage lead nurturing sequences via WhatsApp for multi-channel engagement.
- [../crm-data-sync-agent/README.md](../crm-data-sync-agent/README.md) - Synchronize lead and contact data across multiple platforms to ensure data integrity.
