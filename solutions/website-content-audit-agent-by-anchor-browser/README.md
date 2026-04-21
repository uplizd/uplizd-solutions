# Website Content Audit Agent (Uplizd) - Automated SEO and Content Performance Analysis

## Summary
The Website Content Audit Agent is an intelligent Uplizd workflow designed to automate the scanning, analysis, and reporting of website content health. By leveraging the Composio Toolset to interface with web crawling and SEO analysis tools, this agent identifies broken links, missing meta tags, and content optimization opportunities, providing marketing teams with a single source of truth to improve search rankings and site hygiene.

---

## Demo
![Website Content Audit Agent dashboard showing SEO health scores and broken link reports](image.png)
**Alt text (SEO-ready):** Website Content Audit Agent dashboard showing SEO health scores, broken link reports, and content optimization metrics within the Uplizd workflow platform.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c225f9a9-328d-5447-a957-6c99b6baea1f)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** seo, content audit, web analytics, site hygiene, digital marketing, composio, ai workflow, content optimization
- This solution streamlines technical SEO and content maintenance by automating repetitive site-wide audits.

---

## Who is this for?
This agent is built for teams managing high-volume web content who need to maintain peak SEO performance without manual intervention.

- **SEO Specialist**
    - Automates the identification of technical debt, such as broken links and missing meta descriptions, across thousands of pages.
- **Content Manager**
    - Ensures content quality and consistency by flagging outdated information and underperforming pages for review.
- **Web Developer**
    - Receives prioritized lists of site errors, allowing for faster debugging and improved site architecture.
- **Marketing Operations Lead**
    - Gains visibility into site health metrics to report on content ROI and search visibility improvements over time.

---

## Features
- **Automated Site Crawling**
    - Uses the Composio Toolset to systematically traverse site maps and identify page-level issues.
- **SEO Health Scoring**
    - Calculates real-time health scores based on meta-tag completeness, keyword density, and link integrity.
- **Broken Link Detection**
    - Automatically flags 404 errors and redirect chains that negatively impact user experience and crawl budget.
- **Content Gap Analysis**
    - Compares existing page content against target keywords to suggest optimization improvements.
- **Actionable Reporting**
    - Generates summarized reports that categorize issues by severity, enabling rapid remediation workflows.

---

## Use Cases
**Technical SEO Maintenance**
- Automatically scan for missing H1 tags, duplicate meta descriptions, and non-optimized image alt text.
- Identify and report broken internal and external links to prevent crawl budget waste.

**Content Strategy Optimization**
- Audit landing pages for keyword relevance to ensure alignment with current search intent.
- Track content decay by identifying pages that have not been updated or audited in over six months.

**Site Migration & Launch Prep**
- Verify that all redirects are configured correctly before pushing major site updates live.
- Perform a comprehensive pre-launch audit to ensure no critical SEO elements are missing from new page templates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions library and select the **Website Content Audit Agent**.
2. Click "Import" to add the workflow to your workspace.
3. Connect your required API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, then to **Composio Toolset**, and finally to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target domain URL and audit parameters from the user.
- **Agent**: Processes the request, orchestrates the audit logic, and interprets tool outputs.
- **Composio Toolset**: Executes web requests and SEO data retrieval tasks.
- **Chat Output**: Delivers the structured audit report and actionable recommendations.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Audit the SEO health of https://example.com and list all broken links.`
- `Analyze the homepage for missing meta descriptions and suggest improvements.`
- `Perform a full site audit and prioritize pages that need content updates based on SEO best practices.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as an SEO consultant, prioritizing technical accuracy and actionable insights.
- Instruct the agent to categorize findings by "Critical," "Warning," and "Info."
- Ensure the agent provides specific URLs for every identified issue.
- Maintain a professional, data-driven tone in all generated reports.

### 2) Composio Toolset Node
- Provide your API key for the relevant web crawling or SEO analysis integration.
- Set the connection scope to allow read-only access to site metadata and link structures.

### 3) Tool Availability
- **Web Crawler**: For traversing site pages and extracting HTML content.
- **SEO Analyzer**: For checking meta tags, headers, and keyword density.
- **Link Validator**: For verifying the status of internal and external URLs.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automated infrastructure and account configuration auditing.
- [Accessibility Audit Assistant](../accessibility-audit-assistant-by-figma/README.md) - Automated design and content accessibility compliance checks.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Real-time monitoring and reporting for automated business processes.
