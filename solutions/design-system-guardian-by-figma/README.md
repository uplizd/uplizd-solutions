# Design System Guardian (Uplizd) - Automated Figma consistency and compliance monitoring

## Summary
The Design System Guardian is an intelligent Uplizd workflow that continuously monitors Figma files to ensure adherence to established design tokens, component libraries, and style guides. By automating the detection of design drift and non-compliant elements, this solution helps design teams maintain a single source of truth, significantly reducing manual QA time and ensuring high-fidelity output across all product design assets.

---

## Demo
![Design System Guardian workflow dashboard showing Figma component audit results](image.png)
**Alt text (SEO-ready):** Design System Guardian Uplizd workflow dashboard showing Figma component audit results, design system compliance, and automated design token synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3c6b0828-ac16-5b63-8c1c-12de7ab211a0)

---

## Category
- **Primary category:** Design Operations
- **Secondary tags:** figma, design system, ui ux, design tokens, compliance, automation, composio, workflow
- This solution bridges the gap between design intent and implementation by automating the audit of design assets against your organization's core design system.

---

## Who is this for?
This solution is designed for product design teams and engineering leads who need to scale their design operations without sacrificing quality.

- **Design Systems Manager**
    - Ensures that every team member is utilizing the most current, approved component versions.
- **Product Designer**
    - Receives real-time feedback on non-compliant layers, allowing for instant correction during the design phase.
- **Engineering Lead**
    - Reduces friction during handoff by ensuring design files are structured correctly and follow naming conventions.
- **Design Ops Specialist**
    - Automates the tedious process of auditing large-scale design projects for brand and accessibility compliance.

---

## Features
- **Automated Component Auditing**
    - Scans Figma files to identify instances of detached components or outdated library versions.
- **Design Token Validation**
    - Cross-references color, typography, and spacing values against your centralized design token repository.
- **Real-time Compliance Reporting**
    - Generates instant reports on design drift, highlighting specific frames or layers that deviate from the system.
- **Composio-Powered Figma Integration**
    - Leverages the Composio Toolset to securely interact with the Figma API for deep file inspection and metadata retrieval.
- **Automated Notification Triggers**
    - Alerts designers via Slack or email when critical design system violations are detected in active projects.

---

## Use Cases
**Design System Maintenance**
- Automatically flag instances where local styles are used instead of global design tokens.
- Identify unused components within a file to help keep the design system lean and performant.

**Quality Assurance & Handoff**
- Run a pre-handoff audit to ensure all layers are correctly named and organized for developer consumption.
- Verify that accessibility contrast ratios meet brand standards before a design is marked as "Ready for Dev."

**Design Team Onboarding**
- Provide automated feedback to new designers on their use of the design system library.
- Track common patterns of non-compliance to identify areas where the design system documentation needs improvement.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Design System Guardian solution.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your Figma account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the Figma file URL or project ID to be audited.
- **Agent**: Processes the design requirements and compares them against the retrieved Figma data.
- **Composio Toolset**: Executes API calls to fetch layer data, styles, and component metadata from Figma.
- **Chat Output**: Delivers a structured summary of compliance issues and recommended fixes.

### 3) Run the Flow
Use the Playground to test your design system monitoring:
- `Audit this Figma file [URL] for any detached components.`
- `Check if all typography in [Project Name] matches the design system tokens.`
- `Generate a report of all non-compliant color styles in the current design file.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the design auditor, interpreting Figma's JSON structure to find discrepancies.
- Focus on identifying deviations from the provided design system documentation.
- Prioritize actionable feedback that tells the designer exactly which layer needs adjustment.
- Maintain a professional, constructive tone when reporting design system violations.

### 2) Composio Toolset Node
- Provide your Figma API key within the Composio configuration panel.
- Ensure the connection scope includes read access to your organization's design files and library assets.

### 3) Tool Availability
- **Figma File Inspector**: Fetches structural data of the design file.
- **Style Validator**: Compares local styles against global library tokens.
- **Component Tracker**: Maps instances to their source library definitions.

---

## Related Solutions
- [Accessibility Audit Assistant by Figma](../accessibility-audit-assistant-by-figma/README.md) - Automated accessibility compliance checking for design files.
- [Account Research Agent by OnePage](../account-research-agent-by-onepage/README.md) - Streamlined research and data gathering for account management.
- [Workflow Health Monitor by DailyBot](../workflow-health-monitor-by-dailybot/README.md) - Tracking and reporting on the operational efficiency of automated workflows.
