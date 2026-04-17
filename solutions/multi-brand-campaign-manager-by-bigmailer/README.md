# Multi-Brand Campaign Manager (Uplizd) - Streamline cross-brand email marketing and campaign orchestration

## Summary
The Multi-Brand Campaign Manager is an intelligent Uplizd workflow designed to centralize and automate transactional email orchestration across diverse brand portfolios. By leveraging the Composio Toolset to interface with BigMailer, this solution eliminates manual cross-platform toggling, ensuring consistent messaging, optimized delivery schedules, and unified campaign hygiene for marketing teams managing multiple distinct brand identities.

---

## Demo
![Multi-Brand Campaign Manager dashboard showing automated email scheduling and brand-specific analytics](image.png)
**Alt text (SEO-ready):** Multi-Brand Campaign Manager Uplizd workflow dashboard showing automated email scheduling, BigMailer integration, and cross-brand campaign analytics.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/dde2cd31-f8e4-519e-b5e3-3671be5af15a)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** email marketing, bigmailer, multi-brand, campaign management, automation, marketing ops, data sync, composio
- This solution provides a scalable framework for marketing teams to synchronize and execute email campaigns across multiple brands from a single automated interface.

---

## Who is this for?
This workflow is built for marketing professionals and operations teams who need to maintain brand consistency while scaling email output.

- **Marketing Manager**
    - Orchestrates complex campaign schedules across multiple brand domains without manual intervention.
- **Email Marketing Specialist**
    - Ensures high deliverability and consistent template usage across diverse customer segments.
- **Operations Lead**
    - Reduces operational overhead by automating the synchronization of campaign data between BigMailer and internal databases.
- **Brand Strategist**
    - Monitors cross-brand performance metrics to refine messaging and audience engagement strategies.

---

## Features
- **Cross-Brand Orchestration**
    - Seamlessly toggle between different brand accounts within BigMailer to deploy targeted campaigns.
- **Automated Campaign Scheduling**
    - Trigger email dispatches based on real-time data inputs or predefined time-based triggers.
- **Unified Analytics Sync**
    - Aggregate open rates, click-throughs, and bounce data into a centralized reporting view.
- **Dynamic Template Management**
    - Utilize AI to inject brand-specific variables and content blocks into standardized email templates.
- **Composio-Powered Integration**
    - Leverage the Composio Toolset for secure, authenticated API communication with BigMailer endpoints.

---

## Use Cases
**Multi-Brand Campaign Scaling**
- Deploy seasonal promotional blasts across five distinct brand identities simultaneously.
- Automate the distribution of brand-specific newsletters based on user subscription preferences.

**Transactional Email Hygiene**
- Automatically pause campaigns for specific brands if bounce rates exceed defined thresholds.
- Sync customer suppression lists across all brand accounts to ensure compliance and list health.

**Performance Reporting**
- Generate weekly cross-brand performance summaries to identify top-performing email content.
- Trigger automated alerts when a specific campaign underperforms against historical benchmarks.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Multi-Brand Campaign Manager.
2. Click "Import" to add the workflow to your workspace.
3. Connect your BigMailer API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives campaign parameters, brand selection, and content instructions.
- **Agent**: Processes instructions and determines the appropriate BigMailer API actions.
- **Composio Toolset**: Executes the requested email operations (send, schedule, or fetch analytics).
- **Chat Output**: Returns the status of the campaign execution or the requested performance data.

### 3) Run the Flow
Use the Playground to test your campaign automation:
- `Deploy the 'Summer Sale' template to the 'Brand A' subscriber list.`
- `Fetch the last 7 days of campaign performance data for 'Brand B'.`
- `Pause all active campaigns for 'Brand C' due to list maintenance.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central orchestrator for your email operations.
- **Instruction Pattern:**
    - Always verify the target brand ID before executing any API call.
    - Prioritize error handling for failed dispatches by logging the specific brand and campaign ID.
    - Maintain a professional, data-driven tone when reporting campaign analytics to the user.

### 2) Composio Toolset Node
- **API Key:** Provide your BigMailer API key to enable secure access to your account.
- **Connection Scope:** Ensure the toolset has read/write permissions for campaigns, templates, and reporting endpoints.

### 3) Tool Availability
- **Campaign Management:** Create, update, and trigger email dispatches.
- **Template Access:** Retrieve and validate brand-specific email templates.
- **Analytics Retrieval:** Query campaign performance metrics and subscriber engagement data.

---

## Related Solutions
- [Abandoned Cart Recovery Agent](../abandoned-cart-recovery-agent-by-klaviyo/README.md) — Automate recovery sequences for lost sales.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Gather and report on account-level engagement data.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — General purpose automation for complex business processes.
