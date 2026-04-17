# Content Audit Agent (Uplizd) - Automated Contentful space optimization and hygiene

## Summary
The Content Audit Agent is an intelligent workflow designed to streamline content management by automatically scanning, auditing, and optimizing entries within Contentful spaces. By leveraging AI-driven analysis, this solution helps marketing and content teams maintain high-quality digital assets, ensure metadata consistency, and improve overall content performance through automated cleanup and reporting.

---

## Demo
![Content Audit Agent workflow interface showing Contentful integration and AI analysis nodes](image.png)
**Alt text (SEO-ready):** Content Audit Agent (Uplizd) workflow for Contentful content optimization, automated data hygiene, and marketing operations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1e7109d7-854e-56c7-be09-7a5d7f06cb1e)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** contentful, content audit, data hygiene, marketing, automation, composio, ai workflow, content strategy
- This solution bridges the gap between raw content storage and strategic performance by automating the audit lifecycle for enterprise CMS platforms.

---

## Who is this for?
This solution is designed for teams managing large-scale digital content libraries who need to maintain consistency and quality at scale.

- **Content Manager**
  - Ensures brand guidelines and metadata standards are applied consistently across all published entries.
- **SEO Specialist**
  - Identifies missing meta-descriptions, alt tags, and keyword-optimized content to boost search visibility.
- **Marketing Operations Lead**
  - Reduces technical debt by automating the identification of stale, duplicate, or incomplete content assets.
- **Digital Producer**
  - Accelerates the quality assurance process by flagging broken links or missing assets before they reach production.

---

## Features
- **Automated Content Scanning**
  - Performs real-time audits of Contentful spaces to identify missing fields, broken references, and outdated content.
- **AI-Powered Quality Scoring**
  - Evaluates content against predefined quality benchmarks to provide actionable insights for editors.
- **Bulk Metadata Correction**
  - Uses the Composio Toolset to programmatically update missing SEO tags, alt text, and categories across multiple entries.
- **Stale Content Identification**
  - Automatically flags content that hasn't been updated within a specific timeframe, helping teams prioritize refresh cycles.
- **Seamless CMS Integration**
  - Connects directly to Contentful via secure API tokens to ensure data integrity and real-time synchronization.

---

## Use Cases
**Content Quality Assurance**
- Automatically audit new entries for compliance with brand voice and mandatory field requirements.
- Identify and report on orphaned assets or broken media links within the Contentful media library.

**SEO and Performance Optimization**
- Scan existing blog posts and landing pages for missing H1 tags, meta descriptions, and image alt text.
- Suggest content improvements based on current SEO best practices to increase organic search traffic.

**Lifecycle and Maintenance**
- Flag outdated product documentation or marketing collateral that requires a scheduled review or archival.
- Generate weekly reports on content health metrics to inform the editorial calendar and resource allocation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Content Audit Agent template from the solution gallery.
3. Connect your Contentful API credentials within the integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the audit command or content scope from the user.
*   **Agent**: Processes the audit request and determines which content fields require inspection.
*   **Composio Toolset**: Executes read/write operations against the Contentful API.
*   **Chat Output**: Delivers the final audit report and summary of actions taken.

### 3) Run the Flow
Open the Playground and test the agent with these prompts:
- `Audit all blog posts created in the last 30 days for missing meta descriptions.`
- `Find all entries in the 'Product' content type that have empty 'Alt Text' fields.`
- `Generate a report of all stale content that hasn't been updated in over 6 months.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting audit rules and CMS data.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a content auditor. Analyze the provided Contentful entries, identify missing metadata, and suggest improvements."
- Maintain a professional, objective tone for all generated audit reports.

### 2) Composio Toolset Node
- Provide your Contentful API Key and Space ID to authorize the connection.
- Ensure the connection scope includes read/write access to the target Contentful environment.

### 3) Tool Availability
- **Contentful Read**: Fetch entry data, schema definitions, and media assets.
- **Contentful Write**: Update entry fields, publish changes, and manage metadata.
- **Data Processor**: Format audit results into structured JSON or human-readable summaries.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates gathering and organizing account intelligence.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Tracks and reports on the operational status of automated workflows.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Aggregates and reports on account-level data for sales and marketing teams.
