# Website Visual Monitor (Uplizd) - Automated visual change detection and site integrity alerting

## Summary
The Website Visual Monitor (Uplizd) is an automated AI workflow designed to track, capture, and analyze visual changes across web properties. By leveraging the ApiFlash integration, this solution provides teams with a single source of truth for site integrity, ensuring that design regressions, unauthorized content changes, or layout shifts are identified in real-time. It streamlines quality assurance pipelines and maintains brand hygiene without manual oversight.

---

## Demo
![Website Visual Monitor dashboard showing automated screenshot comparisons and change detection alerts](image.png)
**Alt text (SEO-ready):** Website Visual Monitor dashboard by Uplizd showing automated screenshot comparisons, visual change detection, and web integrity alerts using ApiFlash.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d5318a6d-3c14-5bdc-9b1c-f6c709544d6b)

---

## Category
**Primary category:** Engineering
**Secondary tags:** web monitoring, visual regression, apiflash, quality assurance, automation, site integrity, composio, ai workflow.
This solution bridges the gap between manual web testing and automated visual monitoring by providing continuous, AI-driven oversight of your digital assets.

---

## Who is this for?
This workflow is designed for technical and creative teams responsible for maintaining high-quality web experiences.

*   **QA Engineers**
    *   Automate visual regression testing to catch layout bugs before they reach production.
*   **Frontend Developers**
    *   Receive instant notifications when CSS changes or component updates cause unexpected visual shifts.
*   **Marketing Operations Managers**
    *   Ensure brand consistency across landing pages by monitoring for unauthorized content modifications.
*   **Site Reliability Engineers (SRE)**
    *   Detect site outages or broken UI elements immediately through scheduled visual snapshots.

---

## Features
- **Automated Visual Snapshots**
  Capture high-fidelity screenshots of any URL at scheduled intervals using the ApiFlash integration.
- **Change Detection Logic**
  Utilize AI to compare current snapshots against historical baselines to identify pixel-perfect or structural deviations.
- **Real-time Alerting**
  Trigger immediate notifications via the Chat Output node when significant visual anomalies are detected.
- **Composio-Powered Orchestration**
  Seamlessly connect your web monitoring tools with your existing communication channels for streamlined reporting.
- **Historical Baseline Management**
  Maintain a searchable archive of site states to audit changes over time and verify resolution of reported issues.

---

## Use Cases
**Visual Regression Testing**
*   Automatically verify that new code deployments do not break existing UI components.
*   Compare staging environments against production to ensure parity before a major release.

**Brand & Compliance Monitoring**
*   Monitor landing pages for unauthorized content changes or broken marketing assets.
*   Ensure legal disclaimers and compliance banners remain visible and correctly placed on all pages.

**Site Integrity & Uptime**
*   Detect "white screen" errors or broken layout elements that standard uptime monitors might miss.
*   Track third-party script failures that impact the visual rendering of your website.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Website Visual Monitor template from the solution library.
3. Authenticate your ApiFlash and notification service credentials within the Composio Toolset.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
*   **Chat Input**: Receives the target URL and monitoring frequency parameters.
*   **Agent**: Processes the request and triggers the visual capture and comparison logic.
*   **Composio Toolset**: Executes the ApiFlash API calls to render the site and retrieve the visual data.
*   **Chat Output**: Delivers the final report, including links to snapshots and summaries of detected changes.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
*   `"Monitor https://example.com every hour and alert me if the hero section layout changes."`
*   `"Take a snapshot of the pricing page and compare it to the baseline from yesterday."`
*   `"Check for visual regressions on the homepage and report any discrepancies to the dev team."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for visual analysis and decision-making.
*   Use a model with strong vision capabilities to interpret screenshot comparisons.
*   Instruction: "Analyze the provided visual data, compare it against the stored baseline, and summarize any detected changes."
*   Instruction: "If a change is detected, categorize it as a minor layout shift or a critical visual error."

### 2) Composio Toolset Node
*   **API Key**: Provide your ApiFlash API key to enable high-quality screenshot generation.
*   **Connection Scope**: Ensure the agent has permission to access the web-capture toolset and your preferred notification channel (e.g., Slack or Email).

### 3) Tool Availability
*   **ApiFlash Capture**: High-speed rendering of web pages into image formats.
*   **Comparison Engine**: Logic to overlay and diff images to highlight specific pixel changes.
*   **Notification Dispatcher**: Automated messaging for alerting stakeholders of detected anomalies.

---

## Related Solutions
*   [AB Test Visual Documenter](../ab-test-visual-documenter-by-apiflash/README.md) — Capture and document visual variations for A/B testing campaigns.
*   [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Ensure your web assets meet accessibility standards through automated auditing.
*   [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Track user engagement and account health metrics for your web applications.
