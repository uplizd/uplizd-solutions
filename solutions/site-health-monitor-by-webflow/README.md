# Site Health Monitor (Uplizd) - Proactive Webflow performance and integrity management

## Summary
The Site Health Monitor by Webflow is an automated AI workflow designed to ensure your digital presence remains error-free and optimized. By leveraging the Composio Toolset to interface directly with Webflow, this solution identifies broken links, monitors collection item status, and flags publishing discrepancies, providing a single source of truth for your site's operational health and reducing manual QA overhead.

---

## Demo
![Site Health Monitor dashboard showing real-time Webflow collection status and error logs](image.png)
**Alt text (SEO-ready):** Site Health Monitor dashboard showing real-time Webflow collection status, error logs, and automated uptime tracking for Uplizd AI workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/be97868f-972e-51dc-a50b-c2ab863bd95a)

---

## Category
**Primary category:** Operations
**Secondary tags:** webflow, site monitoring, data hygiene, web scrapers, automation, composio, ai workflow, performance tracking.
This solution bridges the gap between raw Webflow site data and proactive maintenance, ensuring your web assets remain performant and compliant.

---

## Who is this for?
This solution is designed for teams managing complex web environments who need to maintain high uptime and data accuracy.

- **Web Developers**
    - Automate routine site audits to identify broken links and missing assets before they impact users.
- **Content Managers**
    - Ensure collection items are correctly published and synced without manual verification.
- **SEO Specialists**
    - Detect crawlability issues and metadata gaps that could negatively affect search engine rankings.
- **Operations Managers**
    - Maintain a consistent, error-free site experience across multiple Webflow projects through automated reporting.

---

## Features
- **Automated Site Audits**
    - Schedule recurring scans of your Webflow collections to detect publishing errors and broken references.
- **Real-time Status Alerts**
    - Receive immediate notifications when critical site elements or collection items fail to render correctly.
- **Composio-Powered Webflow Integration**
    - Utilize the Composio Toolset to securely read and update Webflow site data via official APIs.
- **Data Hygiene Reporting**
    - Generate clean, actionable summaries of site health that highlight specific collections requiring attention.
- **Intelligent Error Triage**
    - Use AI-driven analysis to categorize issues by severity, allowing teams to prioritize high-impact fixes.

---

## Use Cases
**Proactive Maintenance**
- Automatically scan for 404 errors across all published pages on a daily basis.
- Identify and flag unpublished collection items that are referenced in live site navigation.

**Content Quality Assurance**
- Verify that all images and media assets in your CMS have valid alt text and optimized file paths.
- Audit collection fields for missing or malformed data that could break front-end design components.

**Performance & SEO Optimization**
- Track the loading status of dynamic pages to ensure high-traffic content remains accessible.
- Monitor metadata consistency across large-scale Webflow projects to maintain search engine visibility.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Workflow" to add the Site Health Monitor template to your Uplizd workspace.
3. Connect your Webflow account via the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or scheduled audit request.
- **Agent**: Processes site data and interprets health metrics based on your instructions.
- **Composio Toolset**: Executes API calls to fetch Webflow site structure and collection data.
- **Chat Output**: Delivers the final health report or error summary to your preferred channel.

### 3) Run the Flow
Use the Playground to test your monitoring capabilities:
- `Scan my primary site for broken links and report any 404s.`
- `Check the status of all items in the 'Blog Posts' collection.`
- `Generate a summary report of all unpublished items currently referenced on the homepage.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as your automated site auditor.
- Instruct the agent to prioritize critical errors over minor formatting warnings.
- Define specific collection names that require high-frequency monitoring.
- Set the tone for reporting (e.g., "concise technical summary" vs. "detailed developer log").

### 2) Composio Toolset Node
- Provide your Webflow API key within the Composio connection settings.
- Ensure the connection scope includes read/write access to your specific Site IDs.

### 3) Tool Availability
- `webflow_get_sites`: Retrieve site structure and configuration.
- `webflow_get_collection_items`: Fetch data from specific CMS collections.
- `webflow_get_published_status`: Verify the live status of pages and items.

---

## Related Solutions
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Track and report on account usage metrics.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Monitor the operational status of your internal team workflows.
- [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensure your web assets meet accessibility standards.
