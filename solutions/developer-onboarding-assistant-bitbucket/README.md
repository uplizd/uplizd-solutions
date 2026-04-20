# Developer Onboarding Assistant (Bitbucket) - Automate Repos & Task Setup

## Summary
The Developer Onboarding Assistant is an Uplizd AI workflow designed to streamline technical onboarding by automating the provisioning of sandbox environments and task tracking. By integrating directly with Bitbucket, it ensures new hires receive standardized repository access and clear onboarding objectives, significantly reducing manual setup time and improving team velocity.

---

## Demo

![Uplizd Developer Onboarding Assistant flow creating repositories and onboarding issues](image.png)

**Alt text (SEO-ready):** Uplizd Developer Onboarding Assistant workflow automating Bitbucket repository creation, issue tracking, and developer setup tasks.

---

## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/RUN%20ON%20UPLIZD-blue?style=for-the-badge&logo=lightning)](https://uplizd.ai/solutions/04a90240-322f-5349-ad8b-65d0750c7c97/)

---

## Category

**Primary category:** Developer Operations
**Secondary tags:** bitbucket, onboarding, automation, devops, repository management, workflow, composio, ai agent

This solution bridges the gap between HR onboarding and technical infrastructure setup, providing a single source of truth for new hire provisioning.

---

## Who is this for?

This workflow is built for engineering teams who want to standardize and accelerate the developer onboarding experience:

- **Engineering Managers**
    - Automate the repetitive tasks of repository creation and issue tracking, allowing more time for team mentorship.
- **DevOps Engineers**
    - Standardize the way personal sandboxes are provisioned and ensure consistent workspace permissions across the team.
- **Human Resources**
    - Partner with engineering to provide a professional, automated technical setup on day one for every new hire.
- **Startup Founders**
    - Scale your team quickly by automating the infrastructure setup for every new developer, ensuring immediate productivity.

---

## Features

- **Automated Repository Provisioning**
  Instantly creates private sandbox repositories for new members with standard settings and project configurations.

- **Standardized Project Templating**
  Ensures every new repository starts with the necessary guidelines, coding standards, and project structures.

- **Onboarding Task Automation**
  Automatically generates critical onboarding issues to guide the new hire through setup, review standards, and practice exercises.

- **Access & Permission Verification**
  Continuously verifies that the new member has correctly synced with the workspace and has the required repository permissions.

- **Bitbucket Integration via Composio**
  Seamlessly connects with your Bitbucket workspace to manage repositories, issues, and member data in real-time.

---

## Use Cases

**Kickstart New Hire Onboarding**
- Trigger a full setup workflow as soon as a new developer joins the team.
- Provision `{username}-sandbox` repositories automatically to keep the main workspace clean.

**Standardize Practice Environments**
- Create isolated environments for interns or junior developers to learn the team's tech stack.
- Ensure every developer starts with the same project templates and baseline issues.

**Workspace Access Auditing**
- Use the agent to verify if recent hires have the correct permissions across all repositories.
- Generate setup confirmation summaries for management to ensure compliance and readiness.

---

## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out** to load the template.
3. Create a new workspace or select an existing one.
4. Ensure nodes are connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input** → Receives developer details and onboarding requests.
- **Agent** → Coordinates the onboarding logic and tool execution.
- **Composio Toolset** → Provides the Bitbucket API actions for repository and issue management.
- **Chat Output** → Summarizes the completed onboarding setup for the user.

### 3) Run the Flow
1. Click **Playground** to open the Chat Interface.
2. Enter a request such as:
   - `"Set up onboarding for new developer John Doe (johndoe@example.com, username: jdoe)"`
   - `"Verify if the new member has been correctly added to the workspace"`
   - `"Create a sandbox repo and onboarding issues for our new intern"`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is pre-configured with a workflow designed to handle Bitbucket lifecycle events.
- Maintain a professional and welcoming tone for the new hire.
- Ensure repository naming follows team standards.
- Log and report any API failures for manual follow-up.

### 2) Composio Toolset Node
Requires your **Composio API Key** and a synchronized connection to your **Bitbucket** account.

### 3) Tool Availability
- Repository discovery and creation
- Issue creation and management
- Workspace member listing
- User profile verification

---

## Related Solutions

* **[CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md)**  
  Continuous maintenance to ensure your CRM stays clean, organized, and free of data rot.
* **[CRM Data Sync Manager](../crm-data-sync-manager/README.md)**  
  Orchestrate and monitor data flows across your entire enterprise tech stack.
* **[Deal Pipeline Manager](../deal-pipeline-manager/README.md)**  
  Automatically update deal progress and create follow-up tasks for your sales team.
