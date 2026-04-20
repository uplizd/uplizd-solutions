# Website Content Auditor (Uplizd) - Automated compliance, accuracy, and brand consistency monitoring

## Summary
The Website Content Auditor is an intelligent Uplizd workflow designed to automate the scanning and verification of web pages against predefined brand guidelines, compliance standards, and factual accuracy benchmarks. By leveraging the Composio Toolset to navigate and extract live site data, this solution eliminates manual content review cycles, ensuring your digital presence remains polished, compliant, and optimized for search engines without the overhead of human intervention.

---

## Demo
![Website Content Auditor workflow dashboard showing automated page scanning and compliance reporting](image.png)
**Alt text (SEO-ready):** Website Content Auditor Uplizd workflow showing automated page scanning, compliance reporting, and brand consistency analysis using Composio tools.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/f13c72c3-f159-5466-b683-796db5ab1874)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content audit, brand compliance, web scraping, seo, data hygiene, composio, ai workflow, quality assurance
- This solution bridges the gap between raw web content and enterprise-grade quality standards through automated, AI-driven oversight.

---

## Who is this for?
This solution is designed for teams managing complex digital footprints who need to maintain high standards of content integrity.

- **Content Managers**
    - Automate the identification of broken links, outdated messaging, or non-compliant copy across hundreds of landing pages.
- **SEO Specialists**
    - Ensure all meta tags, headers, and content structures align with current search engine optimization best practices.
- **Compliance Officers**
    - Verify that legal disclaimers, privacy policies, and accessibility statements are present and accurate on every page.
- **Brand Strategists**
    - Monitor brand voice consistency and ensure that product terminology remains uniform across the entire domain.

---

## Features
- **Automated Page Crawling**
    - Uses the Composio browser toolset to programmatically navigate and extract text from live website URLs.
- **Compliance Rule Engine**
    - Validates site content against custom-defined checklists for legal, accessibility, and brand-specific requirements.
- **Real-time Error Reporting**
    - Generates structured summaries of discrepancies, highlighting specific pages and elements that require immediate attention.
- **Multi-Platform Integration**
    - Seamlessly connects with existing CRM and project management tools to log audit findings as actionable tasks.
- **Intelligent Content Analysis**
    - Employs LLM-powered reasoning to detect nuanced tone shifts or factual inaccuracies that traditional regex scanners miss.

---

## Use Cases
**Brand Integrity Monitoring**
- Automatically flag pages where outdated product pricing or deprecated service names are detected.
- Ensure all promotional banners adhere to current seasonal brand guidelines and color palettes.

**SEO & Technical Health**
- Identify missing or duplicate meta descriptions and H1 tags across large-scale documentation sites.
- Monitor page load performance and content structure to ensure alignment with core web vitals.

**Regulatory Compliance**
- Verify the presence and accuracy of mandatory GDPR or CCPA notices on all footer-linked pages.
- Audit accessibility compliance by checking for missing alt text on images and proper semantic HTML structure.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Upload the provided solution JSON file or paste the workflow configuration.
3. Connect your required API credentials for the browser and content management tools.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the target URL or domain list for the audit.
- **Agent**: Analyzes the extracted content against your specific compliance and brand guidelines.
- **Composio Toolset**: Executes browser-based navigation and data retrieval tasks.
- **Chat Output**: Delivers a comprehensive audit report detailing findings and suggested fixes.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Audit https://example.com for any broken links and check if the privacy policy link is active.`
- `Scan the homepage for brand consistency and report any instances where the product is referred to by an old name.`
- `Perform a compliance check on the pricing page to ensure all legal disclaimers are present and visible.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, processing raw HTML text into actionable insights.
- **Instruction Pattern:** 
    - Act as a senior web auditor focused on brand compliance and SEO accuracy.
    - Extract specific content blocks and compare them against the provided "Golden Rule" reference document.
    - Prioritize findings by severity, distinguishing between critical compliance errors and minor stylistic suggestions.

### 2) Composio Toolset Node
- **API Key:** Provide your valid Composio API key to enable browser automation capabilities.
- **Connection Scope:** Ensure the toolset has permission to access the target domains and perform read-only extraction.

### 3) Tool Availability
- **Browser Navigation:** Ability to visit URLs and render dynamic content.
- **Data Extraction:** Capability to parse DOM elements, text, and metadata.
- **Reporting Interface:** Integration with external notification channels to export audit results.

---

## Related Solutions
- [../accessibility-compliance-monitor-by-alttext-ai/README.md](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Automated monitoring for web accessibility standards.
- [../account-health-compliance-monitor-by-brevo/README.md](../account-health-compliance-monitor-by-brevo/README.md) - Ensuring account-level compliance and data health.
- [../ab-test-performance-analyzer-by-microsoft-clarity/README.md](../ab-test-performance-analyzer-by-microsoft-clarity/README.md) - Analyzing web performance and user behavior metrics.
