# Prototype Flow Analyzer (Uplizd) - Automate Figma design documentation and user flow analysis

## Summary
The Prototype Flow Analyzer (Uplizd) streamlines the design-to-documentation pipeline by automatically parsing Figma prototypes into structured user flow reports. By leveraging the Composio Toolset to interface with Figma’s API, this workflow eliminates manual mapping, ensuring design teams maintain a single source of truth for complex user journeys while accelerating hand-off velocity.

---

## Demo
![Prototype Flow Analyzer dashboard showing automated mapping of Figma frames to user journey steps](image.png)
**Alt text (SEO-ready):** Prototype Flow Analyzer (Uplizd) dashboard showing automated mapping of Figma frames to user journey steps, design documentation, and Figma API integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c4805ac8-3328-5e61-96bc-e63f16b9bc3c)

---

## Category
**Primary category:** Design Operations
**Secondary tags:** figma, design-ops, user-flow, documentation, automation, composio, ai-workflow, prototyping
This solution bridges the gap between visual design prototypes and technical documentation through intelligent API-driven analysis.

---

## Who is this for?
This solution is designed for product teams looking to eliminate manual documentation overhead and improve design-to-development hand-off.

*   **Product Designers**
    *   Automate the creation of flow charts and documentation directly from Figma frames.
*   **UX Researchers**
    *   Analyze user journey paths and prototype interactions without manual mapping.
*   **Engineering Leads**
    *   Ensure technical requirements align perfectly with the latest design prototypes.
*   **Design Ops Managers**
    *   Standardize documentation formats across multiple design files and project teams.

---

## Features
- **Automated Flow Mapping**
  Extracts frame connections and transitions directly from Figma to visualize user paths.
- **Real-time Sync**
  Updates documentation automatically when changes are pushed to the Figma prototype.
- **Structured Reporting**
  Generates clean, readable summaries of prototype interactions for stakeholder review.
- **Composio-Powered Integration**
  Utilizes the Composio Toolset to securely authenticate and fetch design metadata from Figma.
- **Cross-Platform Compatibility**
  Exports analysis results into formats compatible with common project management and documentation tools.

---

## Use Cases
**Design Documentation**
*   Automatically generate comprehensive user flow diagrams from complex Figma prototypes.
*   Maintain living documentation that reflects the current state of the design system.

**Hand-off Optimization**
*   Provide developers with clear, annotated journey maps to reduce implementation ambiguity.
*   Highlight interaction logic and edge-case transitions during the design-to-dev hand-off phase.

**UX Auditing**
*   Identify disconnected nodes or broken user paths within a prototype before user testing.
*   Analyze the complexity of user journeys to optimize navigation and reduce friction.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the Uplizd builder.
2. Connect your Figma account via the Composio Toolset configuration.
3. Select the target Figma file URL and frame range for analysis.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the Figma file URL and specific analysis parameters.
*   **Agent**: Processes design metadata to interpret user journey logic and flow transitions.
*   **Composio Toolset**: Executes secure API calls to fetch frame data and interaction properties from Figma.
*   **Chat Output**: Delivers the structured flow report or documentation summary to the user.

### 3) Run the Flow
Use the Playground to test your analysis:
* `Analyze the user flow for the 'Checkout' prototype and identify any missing transition states.`
* `Generate a documentation summary for the latest 'Onboarding' flow in Figma.`
* `Map the navigation path from the home screen to the settings menu in the provided prototype.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a design documentation specialist.
*   Focus on identifying logical transitions between frames.
*   Prioritize clarity in describing user actions and system responses.
*   Maintain consistency with standard UX terminology in all generated reports.

### 2) Composio Toolset Node
Requires a valid Figma API token configured within the Composio dashboard to allow the agent to read file structures, frames, and prototype connections.

### 3) Tool Availability
*   `figma_get_file`: Retrieve the structure of the design file.
*   `figma_get_file_nodes`: Access specific frame data and interaction properties.
*   `figma_get_comments`: Optional inclusion of design feedback in the flow analysis.

---

## Related Solutions
*   [Accessibility Audit Assistant (Figma)](../accessibility-audit-assistant-by-figma/README.md) — Automate accessibility compliance checks for design files.
*   [Workshop Template Curator (Miro)](../workshop-template-curator-by-miro/README.md) — Manage and deploy standardized workshop templates.
*   [Account Research Assistant (ZoomInfo)](../account-research-assistant-by-zoominfo/README.md) — Enrich account data for sales and product alignment.
