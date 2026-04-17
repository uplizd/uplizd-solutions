# Marketing Campaign Link Auditor (Uplizd) - Automated link validation and performance tracking

## Summary
The Marketing Campaign Link Auditor is an intelligent Uplizd workflow that automates the verification of campaign URLs and tracks their engagement metrics via Cutt.ly. By proactively auditing link health and monitoring click-through performance, marketing teams ensure high-quality traffic delivery, prevent broken user experiences, and maintain a single source of truth for campaign asset performance.

---

## Demo
![Marketing Campaign Link Auditor workflow dashboard showing automated URL validation and Cutt.ly performance metrics](image.png)
**Alt text (SEO-ready):** Marketing Campaign Link Auditor Uplizd workflow, automated URL validation, Cutt.ly link tracking, marketing campaign performance monitoring, and link health audit.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/bbc10789-ceb3-5fe9-83f1-e61219c7e607)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** marketing, link tracking, cutt.ly, campaign management, url validation, data hygiene, automation, composio
This solution streamlines marketing operations by integrating link auditing and performance analytics into a unified, automated pipeline.

---

## Who is this for?
This solution is designed for marketing professionals who need to maintain link integrity and track campaign effectiveness at scale.

* **Digital Marketing Manager**
    * Ensures all campaign traffic is directed to active, functional landing pages to maximize conversion rates.
* **Affiliate Marketer**
    * Monitors link performance and click-through rates across multiple channels to optimize ROI.
* **Marketing Operations Specialist**
    * Automates the audit process for thousands of links, reducing manual QA time and preventing broken user journeys.
* **Content Strategist**
    * Gains real-time visibility into which campaign assets are driving the most engagement via Cutt.ly analytics.

---

## Features
- **Automated Link Verification**
    Real-time scanning of campaign URLs to identify broken links or 404 errors before they impact your audience.
- **Cutt.ly Integration**
    Seamless connection with the Cutt.ly API to programmatically generate, manage, and audit shortened links.
- **Performance Analytics**
    Aggregates click-through data and engagement metrics directly into your workflow for instant reporting.
- **Proactive Alerting**
    Configurable notifications that alert the team immediately when a high-traffic link fails or shows anomalous behavior.
- **Composio Toolset Orchestration**
    Leverages the Composio Toolset to bridge the gap between your marketing dashboard and external link management tools.

---

## Use Cases
**Campaign Quality Assurance**
* Automatically audit all URLs in a new email blast or social media campaign before launch.
* Identify and replace expired or redirected links that no longer point to the intended landing page.

**Performance Monitoring**
* Track daily click-through rates for active affiliate campaigns to identify top-performing content.
* Generate automated weekly reports on link usage and traffic distribution across different marketing channels.

**Link Lifecycle Management**
* Bulk-audit legacy campaign links to ensure historical content remains accessible and functional.
* Standardize link naming and tracking parameters across the organization to maintain data hygiene.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Marketing Campaign Link Auditor template from the solution library.
3. Authenticate your Cutt.ly account within the Composio Toolset node.
4. Ensure nodes are correctly connected: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives the list of campaign URLs or campaign IDs to be audited.
* **Agent**: Processes the input, triggers link health checks, and interprets performance data.
* **Composio Toolset**: Executes API calls to Cutt.ly to validate links and fetch metrics.
* **Chat Output**: Returns a summary report of link status and performance insights.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
* `Audit all links in the current Q3 Summer Campaign and report any broken URLs.`
* `Fetch the latest click performance metrics for my top 5 affiliate links.`
* `Check the status of all campaign links and provide a summary of any that are currently inactive.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine for your marketing data.
* **Instruction Pattern:**
    * "You are a marketing link auditor; verify URL reachability and report errors immediately."
    * "Analyze Cutt.ly performance data to identify high-performing vs. under-performing assets."
    * "Maintain a professional tone when reporting link health status to the marketing team."

### 2) Composio Toolset Node
* **API Key:** Provide your Cutt.ly API key in the node configuration.
* **Connection Scope:** Ensure the toolset has read/write access to your link management dashboard.

### 3) Tool Availability
* **Link Validator:** Checks HTTP status codes for all provided URLs.
* **Cutt.ly Analytics:** Fetches click counts, referral sources, and geographic data.
* **Link Manager:** Allows for the creation, updating, and deletion of shortened links.

---

## Related Solutions
* [Affiliate Link Performance Tracker](../affiliate-link-performance-tracker-by-cutt-ly/README.md) - Track and optimize affiliate link engagement.
* [Abuse Report Manager](../abuse-report-manager-by-abuselpdb/README.md) - Manage and respond to link abuse reports.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational status of your automated workflows.
