# Brand Compliance Monitor (Uplizd) - Automated brand asset verification and governance

## Summary
The Brand Compliance Monitor is an automated AI workflow designed to ensure consistent brand asset usage across all marketing and public-facing materials. By leveraging the Brandfetch integration, this solution scans digital assets in real-time, identifying unauthorized logo usage, outdated color palettes, or incorrect typography, thereby protecting brand equity and maintaining visual identity standards across distributed teams.

---

## Demo
![Brand Compliance Monitor dashboard showing automated asset verification and compliance alerts](image.png)
**Alt text (SEO-ready):** Brand Compliance Monitor dashboard showing automated asset verification, brand identity audit, and compliance alerts using Uplizd and Brandfetch.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/491bd1c8-a9a7-5843-92ea-8ae71671bb09)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** brand compliance, brandfetch, asset management, marketing automation, visual identity, quality assurance, composio, ai workflow
- This solution streamlines the enforcement of brand guidelines by automating the detection of non-compliant assets across your marketing ecosystem.

---

## Who is this for?
This solution is designed for teams responsible for maintaining a unified brand presence across diverse digital channels.

- **Brand Manager**
    - Ensures all public-facing assets adhere to the latest style guides and visual standards.
- **Marketing Operations Lead**
    - Automates the audit process to reduce manual asset review time and operational bottlenecks.
- **Creative Director**
    - Maintains oversight of brand integrity without needing to manually inspect every campaign output.
- **Legal/Compliance Officer**
    - Verifies that all assets utilize licensed logos and approved typography to prevent copyright issues.

---

## Features
- **Automated Asset Scanning**
    - Real-time detection of brand assets using the Brandfetch API to ensure current logo and color usage.
- **Compliance Scoring**
    - Assigns a health score to marketing materials based on the accuracy of applied brand elements.
- **Cross-Platform Integration**
    - Seamlessly connects with your existing design and marketing stacks via the Composio Toolset.
- **Instant Alerting**
    - Triggers notifications when non-compliant assets are detected in active campaigns or drafts.
- **Historical Audit Logs**
    - Maintains a searchable record of all compliance checks for reporting and future brand strategy refinement.

---

## Use Cases
**Marketing Campaign Audits**
- Automatically verify that all social media ad creative uses the current fiscal year's logo version.
- Scan email marketing templates to ensure hex codes match the approved primary brand palette.

**Digital Asset Management**
- Audit landing page assets to identify and flag outdated or low-resolution brand imagery.
- Monitor partner-facing portals to ensure external collaborators are using the correct brand guidelines.

**Brand Governance**
- Identify unauthorized use of secondary brand marks in internal presentations or public documents.
- Generate automated reports on brand consistency across different regional marketing departments.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Brand Compliance Monitor template from the solution library.
3. Connect your Brandfetch API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the URL or file path of the asset to be audited.
- **Agent**: Analyzes the input against the provided brand guidelines and identifies discrepancies.
- **Composio Toolset**: Executes the Brandfetch API calls to fetch current brand standards for comparison.
- **Chat Output**: Returns a detailed compliance report with specific feedback on required corrections.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Check the brand compliance of the logo used on this landing page: [URL]`
- `Verify if the colors in this design file match our current brand palette.`
- `List any non-compliant assets found in the latest marketing campaign folder.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a brand governance expert, focusing on visual accuracy and policy enforcement.
- Instruction: "You are a brand compliance expert; compare provided assets against the official Brandfetch guidelines."
- Instruction: "Flag any deviations in logo, color, or typography as 'Non-Compliant' and provide the correct asset link."
- Instruction: "Maintain a professional tone and provide actionable feedback for the creative team."

### 2) Composio Toolset Node
- Requires a valid Brandfetch API key to access your organization's verified asset repository.
- Connection scope should be set to 'Read-Only' for asset metadata and 'Full' for style guide retrieval.

### 3) Tool Availability
- **Asset Fetcher**: Retrieves current logo, color, and font data.
- **Compliance Validator**: Compares input data against retrieved brand standards.
- **Reporting Engine**: Formats the audit results into a readable summary for the user.

---

## Related Solutions
- [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) - Monitor account health and compliance metrics.
- [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensure digital content meets accessibility standards.
- [Work Hours Compliance Monitor](../work-hours-compliance-monitor-by-timely/README.md) - Track and report on work hour compliance.
