# Employee Finance Onboarding Bot (Uplizd) - Automated Financial Provisioning for New Hires

## Summary
The Employee Finance Onboarding Bot automates the complex task of provisioning financial tools and corporate cards for new hires. By integrating directly with platforms like Brex, this Uplizd AI workflow eliminates manual data entry, reduces onboarding bottlenecks, and ensures new employees have immediate access to necessary financial resources, creating a seamless and compliant "Day 1" experience.

---

## Demo
![Employee Finance Onboarding Bot workflow diagram showing automated card provisioning and financial tool setup](image.png)
**Alt text (SEO-ready):** Employee Finance Onboarding Bot workflow for automated corporate card provisioning, financial tool setup, and new hire onboarding using Uplizd and Composio.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMJFR0W+7/35QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lQTHHxK04AAAAiSURBVEjHY2AYBaNgFIyCUjAKRsEoGAWjYBSMglEwChgBAAAGAAH5314AAAAASUVORK5CYII=)](https://uplizd.ai/solutions/32fb58a1-a7d3-58f0-a25a-262777945bb3)

---

## Category
**Primary category:** Finance operations
**Secondary tags:** brex, onboarding, fintech, automation, employee management, expense management, composio, ai workflow

This solution streamlines financial operations by connecting HR onboarding triggers to corporate spend management platforms.

---

## Who is this for?
This workflow is designed for teams managing rapid headcount growth and complex financial access requirements.

* **People Operations Manager**
    * Automates the repetitive task of setting up employee financial profiles, saving hours of manual data entry per hire.
* **Finance Controller**
    * Ensures strict adherence to spending limits and policy compliance by automating card issuance based on predefined roles.
* **IT Systems Administrator**
    * Reduces ticket volume related to access requests by providing automated, role-based provisioning on day one.
* **New Employee**
    * Receives immediate, frictionless access to corporate financial tools, allowing them to focus on their role rather than administrative blockers.

---

## Features
- **Automated Card Provisioning**
    Instantly trigger corporate card creation and limit assignment in Brex based on HR system data.
- **Role-Based Access Control**
    Dynamically assign financial tool permissions based on the employee's department and seniority level.
- **Real-Time Sync**
    Ensures that employee status changes in the HRIS are immediately reflected in financial management platforms.
- **Compliance Guardrails**
    Automatically applies company spending policies to new accounts, preventing unauthorized or out-of-policy expenditures.
- **Audit-Ready Logging**
    Maintains a detailed trail of all provisioning actions, simplifying internal audits and financial reporting.

---

## Use Cases
**New Hire Financial Setup**
* Automatically generate a corporate card for a new hire upon their start date.
* Assign specific spending limits to a new employee based on their department's budget.

**Departmental Access Management**
* Provision access to expense reporting software for new members of the Sales team.
* Revoke or adjust financial tool access when an employee transitions between departments.

**Policy Enforcement & Compliance**
* Flag new hire profiles that lack required documentation before issuing financial credentials.
* Sync employee metadata to ensure that all corporate cards are correctly categorized for tax and accounting purposes.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your workspace and click "Import Flow" to initialize the workflow.
3. Authenticate your Brex and HRIS connections within the Composio Toolset node.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the new hire's details (name, email, role, department).
* **Agent**: Processes the request and determines the appropriate financial provisioning logic.
* **Composio Toolset**: Executes API calls to Brex to create cards and set limits.
* **Chat Output**: Confirms successful provisioning or alerts the admin to missing information.

### 3) Run the Flow
Use the Uplizd Playground to test the workflow with these prompts:
* `Provision a new corporate card for John Doe in the Marketing department with a $500 monthly limit.`
* `Check the status of financial tool access for the latest batch of new hires.`
* `Update the spending limit for Jane Smith to $1000 and notify her via email.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestration layer between HR data and financial APIs.
* Use a model capable of structured JSON output for reliable API parameter mapping.
* Instruction: "You are a financial operations assistant. Extract employee details, map them to the correct department budget, and call the appropriate Brex tool."
* Instruction: "Always verify the employee's role before assigning spending limits to ensure policy compliance."

### 2) Composio Toolset Node
* Provide your Brex API key and ensure the connection scope includes `cards.write` and `users.read` permissions.
* Configure the toolset to handle authentication via OAuth2 or API Key headers as required by your Brex integration.

### 3) Tool Availability
* **Brex Card API**: For creating, updating, and managing corporate cards.
* **Brex User API**: For fetching user details and assigning permissions.
* **HRIS Connector**: For retrieving new hire metadata and department mappings.

---

## Related Solutions
* [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) — Automates the reconciliation of corporate expenses and ledger entries.
* [../account-health-compliance-monitor-by-brevo/README.md](../account-health-compliance-monitor-by-brevo/README.md) — Monitors and maintains compliance across various account management systems.
* [../workflow-automation-agent-by-jobnimbus/README.md](../workflow-automation-agent-by-jobnimbus/README.md) — General-purpose workflow automation for managing operational tasks and data syncs.
