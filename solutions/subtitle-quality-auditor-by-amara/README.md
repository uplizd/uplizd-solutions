# Subtitle Quality Auditor (Uplizd) - Automated precision for video accessibility and compliance

## Summary
The Subtitle Quality Auditor (Uplizd) is an intelligent AI workflow designed to automate the verification, correction, and compliance monitoring of subtitle files across large video libraries. By leveraging the Amara API via the Composio Toolset, this solution ensures that content creators, accessibility teams, and media managers maintain high-fidelity captions, reducing manual review time and ensuring adherence to global accessibility standards.

---

## Demo
![Subtitle Quality Auditor workflow interface showing automated Amara subtitle verification and error reporting](image.png)
**Alt text (SEO-ready):** Subtitle Quality Auditor (Uplizd) workflow interface showing automated Amara subtitle verification, error reporting, and accessibility compliance monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/d84db9e7-fafd-5ce5-833c-9dbc9083670d)

---

## Category
**Primary category:** Content Operations
**Secondary tags:** accessibility, subtitle, amara, video, compliance, quality assurance, automation, composio

This solution streamlines media accessibility workflows by integrating automated audit capabilities directly into your video management pipeline.

---

## Who is this for?
This solution is designed for media professionals and accessibility advocates who need to maintain high standards for video content.

*   **Accessibility Manager**
    *   Ensures all video assets meet WCAG and regional compliance standards automatically.
*   **Content Operations Lead**
    *   Reduces the manual overhead of auditing thousands of subtitle files across global libraries.
*   **Video Editor**
    *   Receives instant feedback on timing, sync, and formatting errors before final publication.
*   **Localization Specialist**
    *   Validates that translated subtitles maintain linguistic accuracy and appropriate character limits.

---

## Features
- **Automated Quality Audits**
  Real-time scanning of subtitle files to detect timing inconsistencies, sync errors, and formatting issues.
- **Amara Integration**
  Seamless connection to the Amara platform to fetch, analyze, and update subtitle metadata and content.
- **Compliance Reporting**
  Generates structured reports identifying non-compliant assets that require immediate human intervention.
- **Intelligent Error Correction**
  Uses the Agent node to suggest fixes for common captioning errors like overlapping text or excessive character counts.
- **Pipeline Velocity**
  Accelerates the post-production cycle by automating the QA bottleneck in the video delivery workflow.

---

## Use Cases
**Accessibility Compliance**
*   Automating the audit of video libraries to ensure captions meet strict regulatory requirements.
*   Flagging missing or corrupted subtitle tracks for immediate remediation by the production team.

**Quality Assurance Automation**
*   Validating subtitle timing against video timestamps to ensure perfect synchronization.
*   Identifying and correcting formatting inconsistencies across multi-language subtitle files.

**Content Lifecycle Management**
*   Monitoring subtitle health for legacy content during library migrations or platform updates.
*   Streamlining the feedback loop between automated audit results and manual editing tasks in Amara.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution in the builder.
2. Connect your Amara account via the Composio Toolset configuration.
3. Review the pre-configured workflow logic in the canvas.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the video ID or subtitle file reference to be audited.
*   **Agent**: Analyzes the subtitle data based on defined quality and compliance instructions.
*   **Composio Toolset**: Executes API calls to Amara to retrieve and validate subtitle content.
*   **Chat Output**: Returns a detailed audit report or confirmation of successful validation.

### 3) Run the Flow
Use the Playground to test your audit logic with these prompts:
* `Audit the subtitle quality for video ID 12345 and list any timing errors.`
* `Check if the subtitles for the latest training video meet accessibility compliance standards.`
* `Identify all subtitle files in the current project that exceed the character-per-second limit.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your subtitle data.
*   Use a model with strong reasoning capabilities (e.g., GPT-4o) to interpret complex timing and linguistic rules.
*   Provide clear instructions on the specific accessibility standards (e.g., WCAG) to be enforced.
*   Configure the agent to output results in a structured JSON format for easier integration with downstream systems.

### 2) Composio Toolset Node
*   **API Key**: Provide your Amara API credentials within the Composio configuration.
*   **Connection Scope**: Ensure the connection has read/write access to the specific video projects you intend to audit.

### 3) Tool Availability
*   `amara_get_subtitles`: Fetches raw subtitle data for analysis.
*   `amara_update_metadata`: Allows the agent to flag or update subtitle status based on audit findings.
*   `amara_list_videos`: Enables the agent to scan library-wide content for bulk auditing.

---

## Related Solutions
* [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Monitor and report on digital accessibility compliance across web assets.
* [Accessibility Audit Assistant](../accessibility-audit-assistant-by-figma/README.md) — Automate design-level accessibility checks within Figma environments.
* [Accessibility Compliance Generator](../accessibility-compliance-generator-by-aivoov/README.md) — Generate compliant accessibility assets and documentation for media.
