# CMS Content Auditor (Uplizd) - Automated quality, structure, and compliance monitoring for headless CMS

## Summary
The CMS Content Auditor is an intelligent Uplizd workflow designed to streamline content governance by automatically scanning, validating, and reporting on assets within your headless CMS. By leveraging the Composio Toolset, this solution ensures brand consistency, SEO optimization, and structural integrity, significantly reducing manual QA time and improving pipeline velocity for content teams.

---

## Demo
![CMS Content Auditor workflow dashboard showing automated content scanning and compliance reporting](../image.png)
**Alt text (SEO-ready):** CMS Content Auditor Uplizd workflow for automated content quality, SEO compliance, and headless CMS data hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/61373690-669e-5b00-9240-85d69edfcd52)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** cms, content strategy, data hygiene, seo, compliance, composio, ai workflow, content audit
- This solution bridges the gap between raw CMS data and high-quality content standards through automated, AI-driven oversight.

---

## Who is this for?
This solution is designed for teams managing high-volume content operations who need to maintain strict quality standards across digital properties.

- **Content Managers**
    - Automate the identification of stale or non-compliant content across large-scale documentation and marketing sites.
- **SEO Specialists**
    - Ensure all published content meets metadata, keyword density, and structural requirements for search engine indexing.
- **Compliance Officers**
    - Enforce brand voice and legal disclaimer requirements across all dynamic CMS entries.
- **Technical Writers**
    - Maintain consistent formatting and structural integrity within complex headless CMS schemas.

---

## Features
- **Automated Content Scanning**
    - Real-time crawling of CMS entries to identify structural inconsistencies and missing metadata fields.
- **SEO Compliance Engine**
    - Automatically validates meta-tags, alt-text, and keyword usage against current best practices.
- **Brand Voice Validation**
    - Uses advanced LLM analysis to ensure content tone aligns with defined corporate brand guidelines.
- **Integration-Ready Workflow**
    - Seamlessly connects to your headless CMS via the Composio Toolset for direct read/write operations.
- **Customizable Audit Reports**
    - Generates actionable summaries of content health, highlighting specific entries that require human intervention.

---

## Use Cases
**Content Quality Assurance**
- Automatically flag articles missing required H1-H3 headers or structural elements.
- Identify and report on broken internal links or outdated references within CMS content blocks.

**SEO & Discovery Optimization**
- Scan all new content entries for missing meta-descriptions or non-optimized title tags.
- Audit image assets for missing descriptive alt-text to improve accessibility and search ranking.

**Brand & Compliance Governance**
- Flag content that deviates from the approved brand voice or tone guidelines.
- Monitor for the presence of mandatory legal disclaimers or required product attribution links.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the CMS Content Auditor template from the solution library.
3. Connect your headless CMS credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger or manual request to initiate a content audit.
- **Agent**: Processes the CMS data against defined quality and compliance rules.
- **Composio Toolset**: Executes API calls to fetch, validate, and update content entries.
- **Chat Output**: Delivers the final audit report and recommendations to the user.

### 3) Run the Flow
Use the Playground to test your audit logic with these prompts:
- `Audit the 'Blog' folder for any entries missing meta-descriptions.`
- `Scan all recent content for brand voice compliance and list items needing revision.`
- `Check the 'Product' category for missing alt-text on images and generate a summary report.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the primary auditor, applying logic to CMS content.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate content analysis.
- Provide a clear system prompt defining your specific brand voice and SEO requirements.
- Configure the agent to output results in a structured format (JSON or Markdown tables) for better readability.

### 2) Composio Toolset Node
- Provide your headless CMS API key within the Composio connection settings.
- Ensure the connection scope includes read/write permissions for the specific content types you intend to audit.

### 3) Tool Availability
- **CMS Fetcher**: Retrieves content bodies, metadata, and asset lists.
- **Content Validator**: Compares retrieved data against defined schema and SEO rules.
- **Report Generator**: Formats audit findings into a concise summary for the end-user.

---

## Related Solutions
- [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Automated monitoring for WCAG compliance and accessibility standards.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracking and reporting on user engagement and content interaction metrics.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitoring the operational status and efficiency of automated business processes.
