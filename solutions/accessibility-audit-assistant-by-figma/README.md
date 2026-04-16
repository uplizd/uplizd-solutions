# Accessibility Audit Assistant (Uplizd) - Automated design accessibility compliance and remediation

## Summary
The Accessibility Audit Assistant by Uplizd streamlines the design-to-development workflow by automatically scanning Figma files for WCAG compliance gaps. This AI-powered workflow empowers design teams to identify color contrast issues, missing alt text, and touch-target violations in real-time, ensuring that digital products are inclusive, accessible, and ready for handoff without manual audit fatigue.

---

## Demo
![Accessibility Audit Assistant dashboard showing automated Figma layer analysis and compliance reporting](image.png)
**Alt text (SEO-ready):** Accessibility Audit Assistant by Uplizd, automated Figma design audit, WCAG compliance checker, AI-powered design workflow, and accessibility remediation tool.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/128b087e-e848-58c9-8303-666f660f37c7)

---

## Category
- **Primary category:** Design Operations
- **Secondary tags:** figma, accessibility, wcag, design systems, compliance, ui-ux, composio, ai workflow
- This solution bridges the gap between creative design and technical accessibility standards through automated inspection and reporting.

---

## Who is this for?
This solution is designed for product teams striving to build inclusive digital experiences efficiently.

- **Product Designers**
    - Automate the identification of accessibility violations during the design phase to reduce rework.
- **Design Systems Managers**
    - Ensure all components in the library adhere to strict accessibility guidelines before they are used in production.
- **Accessibility Specialists**
    - Scale audit capabilities across large-scale design files without manual layer-by-layer inspection.
- **Frontend Developers**
    - Receive clean, compliant design specs that minimize accessibility-related bugs during the implementation phase.

---

## Features
- **Automated WCAG Scanning**
  Instantly scan Figma frames for common accessibility failures like insufficient color contrast ratios.
- **Contextual Remediation Advice**
  Receive AI-generated suggestions on how to adjust hex codes or layer properties to meet compliance standards.
- **Layer-Specific Reporting**
  Map accessibility issues directly to specific Figma layers, making it easy for designers to locate and fix errors.
- **Composio Toolset Integration**
  Leverage the Composio Toolset to bridge the Figma API with the Uplizd agent for real-time design file interaction.
- **Compliance Documentation**
  Generate automated audit logs that track accessibility improvements over the lifecycle of a design project.

---

## Use Cases
**Design System Governance**
- Automatically validate new UI components against accessibility standards before they are published to the team library.
- Track compliance drift in existing design systems as new features are added to the product roadmap.

**Pre-Handoff Quality Assurance**
- Run a comprehensive audit on high-fidelity prototypes to catch touch-target and font-size issues before developer handoff.
- Generate a summary report of pending accessibility fixes to be addressed during the final design polish phase.

**Inclusive Product Iteration**
- Audit existing legacy designs to identify high-impact accessibility improvements for the next sprint.
- Monitor the accessibility health of user flows to ensure consistent compliance across all product screens.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Accessibility Audit Assistant template from the solution library.
3. Connect your Figma account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the Figma file URL and specific frame IDs to audit.
- **Agent**: Analyzes design metadata and compares it against accessibility rules.
- **Composio Toolset**: Executes API calls to fetch layer data and properties from Figma.
- **Chat Output**: Delivers a structured report of identified issues and actionable remediation steps.

### 3) Run the Flow
Use the Playground to test your audit workflow with these prompts:
- `Scan the design file at [URL] for any color contrast violations.`
- `Identify all elements in the 'Login' frame that fail WCAG 2.1 touch target requirements.`
- `Generate a summary report of all accessibility issues found in the current design project.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an accessibility expert, interpreting design data to provide actionable feedback.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Set the system instruction to prioritize WCAG 2.1/2.2 standards.
- Ensure the agent is instructed to output findings in a clear, prioritized list format.

### 2) Composio Toolset Node
- Provide your Figma API key within the Composio Toolset node.
- Ensure the connection scope includes read access to design files and layer metadata.

### 3) Tool Availability
- **Figma Layer Inspector**: Retrieves properties like fill, stroke, and dimensions.
- **Accessibility Validator**: Compares extracted properties against standard compliance thresholds.
- **Report Generator**: Formats raw audit data into human-readable summaries.

---

## Related Solutions
- [../crm-data-quality-agent/README.md](../crm-data-quality-agent/README.md) - Maintain high data standards across your CRM and design databases.
- [../crm-system-health-monitor/README.md](../crm-system-health-monitor/README.md) - Monitor the overall health and performance of your integrated business systems.
- [../AIWorkflowDebuggerByOpenai/README.md](../ai-workflow-debugger-by-openai/README.md) - Debug and optimize your AI-driven design and development workflows.
