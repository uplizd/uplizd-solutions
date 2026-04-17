# Content Performance Analyzer (Uplizd) - Optimize digital content strategy with AI-driven insights

## Summary
The Content Performance Analyzer by Agility CMS is an intelligent Uplizd workflow designed to audit, categorize, and evaluate digital content assets. By leveraging the Composio Toolset to interface with your CMS, this solution provides actionable insights into content structure and performance, helping marketing teams maintain high-quality digital experiences and improve pipeline velocity through data-driven content hygiene.

---

## Demo
![Content Performance Analyzer workflow diagram showing CMS data ingestion, AI analysis, and performance reporting](image.png)
**Alt text (SEO-ready):** Content Performance Analyzer Uplizd workflow for Agility CMS, featuring AI-driven content auditing, digital experience optimization, and automated performance reporting.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue)](https://uplizd.ai/solutions/content-performance-analyzer-by-agility-cms)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** content management, agility cms, content audit, performance analytics, digital experience, ai workflow, composio, content hygiene

This solution bridges the gap between raw CMS data and strategic content planning by automating the analysis of digital assets.

---

## Who is this for?
This workflow is designed for teams managing complex digital ecosystems who need to scale content quality without manual overhead.

- **Content Strategist**
    - Identifies underperforming content clusters to prioritize for refresh or archival.
- **Marketing Operations Manager**
    - Ensures consistent content metadata and taxonomy across the Agility CMS instance.
- **SEO Specialist**
    - Detects content decay and optimization opportunities based on automated performance signals.
- **Digital Product Manager**
    - Monitors the health of digital experiences to ensure high-value pages meet engagement benchmarks.

---

## Features
- **Automated Content Auditing**
    - Scans CMS entries to identify outdated, duplicate, or low-performing content assets.
- **AI-Driven Taxonomy Mapping**
    - Automatically categorizes content based on topic, intent, and performance metrics.
- **Real-time Performance Insights**
    - Integrates with analytics data to provide immediate feedback on content engagement.
- **Composio-Powered CMS Integration**
    - Seamlessly connects to Agility CMS to fetch, update, and manage content entries via secure API calls.
- **Actionable Optimization Reports**
    - Generates clear, prioritized lists of content requiring updates or structural improvements.

---

## Use Cases
**Content Lifecycle Management**
- Automatically flag content older than 12 months that lacks updated SEO metadata.
- Identify "orphan" pages that have high traffic but no internal links to high-conversion assets.

**Performance Optimization**
- Analyze engagement metrics for blog posts to recommend content expansion or consolidation.
- Detect discrepancies between published content and current brand messaging guidelines.

**Data Hygiene & Governance**
- Standardize content tags and categories across large-scale CMS repositories.
- Audit media asset usage to identify unused or redundant files taking up storage.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Content Performance Analyzer template from the marketplace.
3. Authenticate your Agility CMS connection via the Composio integration portal.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's request for a specific content audit or performance report.
- **Agent**: Processes the request, interprets content data, and formulates optimization strategies.
- **Composio Toolset**: Executes API queries to Agility CMS to fetch content data and perform updates.
- **Chat Output**: Delivers the final audit report and recommended actions back to the user.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Analyze all blog posts published in Q1 and identify those with engagement rates below 2%.`
- `Audit the 'Product' content category for missing meta-descriptions and suggest improvements.`
- `List all content assets that haven't been updated in over 18 months and categorize them by topic.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a content strategist and data analyst.
- Use a model with strong reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruction: "You are a content performance expert. Analyze CMS data, identify trends, and provide actionable, data-backed recommendations."
- Ensure the agent is configured to output structured JSON for reporting.

### 2) Composio Toolset Node
- Provide your Agility CMS API key and organization ID within the Composio connection settings.
- Ensure the scope includes read/write access to content entries and media libraries.

### 3) Tool Availability
- `cms_fetch_entries`: Retrieves content data based on filters.
- `cms_update_metadata`: Updates tags and SEO fields on existing entries.
- `analytics_fetch_metrics`: Pulls performance data for specific content IDs.
- `cms_list_categories`: Retrieves current taxonomy structures for audit comparison.

---

## Related Solutions
- [../account-intelligence-reporter-by-leadfeeder/README.md](Account Intelligence Reporter) - Aggregates account data for targeted marketing outreach.
- [../ab-test-optimizer-by-mixpanel/README.md](A/B Test Optimizer) - Uses performance data to refine digital experimentation strategies.
- [../crm-data-hygiene-manager/README.md](CRM Data Hygiene Manager) - Maintains clean data records to support marketing and sales alignment.
