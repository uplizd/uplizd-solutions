# Bulk QR Cleanup Manager (Uplizd) - Automated QR code lifecycle and campaign maintenance

## Summary
The Bulk QR Cleanup Manager is an intelligent Uplizd workflow designed to automate the identification, verification, and removal of expired or inactive QR code campaigns. By leveraging the Composio Toolset to interface with Beaconstac, this solution ensures your digital-to-physical marketing assets remain accurate and functional, reducing manual overhead and preventing broken user experiences.

---

## Demo
![Bulk QR Cleanup Manager workflow interface showing automated QR code status verification and deletion logic](image.png)
**Alt text (SEO-ready):** Bulk QR Cleanup Manager workflow for automated QR code maintenance, Beaconstac integration, and Uplizd campaign hygiene.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/4dcfd0a8-c249-5c87-a888-baa20ec350fb)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** qr code, beaconstac, campaign management, data hygiene, automation, marketing assets, lifecycle management, composio
- This solution streamlines marketing operations by maintaining high-quality, active QR code inventories through automated lifecycle management.

---

## Who is this for?
This solution is designed for marketing and operations teams managing large-scale physical-to-digital touchpoints.

- **Marketing Operations Manager**
    - Automates the audit of thousands of QR codes to ensure campaign accuracy.
- **Campaign Coordinator**
    - Eliminates manual tracking of expiration dates for print and digital assets.
- **Digital Asset Administrator**
    - Maintains brand integrity by ensuring all scannable assets redirect to active, relevant content.
- **Growth Marketer**
    - Reclaims storage and management capacity by purging obsolete campaign data.

---

## Features
- **Automated Expiration Audits**
    - Scans your Beaconstac account in real-time to identify QR codes that have passed their scheduled end dates.
- **Bulk Cleanup Execution**
    - Safely archives or deletes expired assets in batches, preventing manual errors during high-volume maintenance.
- **Status Reporting**
    - Generates summary logs of all cleaned assets, providing clear visibility into what was removed and why.
- **Integration with Composio**
    - Utilizes the Composio Toolset to securely authenticate and execute API commands directly within the Beaconstac environment.
- **Customizable Logic**
    - Allows for flexible rules, such as keeping specific high-traffic codes while purging temporary promotional assets.

---

## Use Cases
**Campaign Lifecycle Management**
- Automatically deactivate QR codes associated with seasonal promotions once the campaign window closes.
- Archive expired event-based QR codes to keep your dashboard clean and focused on active initiatives.

**Data Hygiene & Compliance**
- Regularly purge obsolete QR codes to ensure your account stays within storage limits and performance thresholds.
- Maintain a clean database by removing broken or inactive redirects that could lead to poor user experiences.

**Operational Efficiency**
- Schedule weekly cleanup runs to ensure your physical marketing collateral remains perfectly synced with your digital strategy.
- Reduce the time spent by team members manually checking and deleting individual QR codes in the Beaconstac portal.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your workspace.
2. Connect your Beaconstac account via the Composio Toolset integration.
3. Configure your environment variables for campaign thresholds and cleanup rules.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent**, **Composio Toolset**, and finally **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Triggers the cleanup process with specific date or campaign filters.
- **Agent**: Interprets the cleanup criteria and orchestrates the API calls.
- **Composio Toolset**: Executes the secure read/write operations against the Beaconstac API.
- **Chat Output**: Returns a confirmation report detailing the number of QR codes processed and deleted.

### 3) Run the Flow
Use the Playground to test your cleanup logic with these prompts:
- `Find all QR codes that expired before last month and delete them.`
- `List all inactive QR codes in the 'Summer Promo' campaign for review.`
- `Run a full cleanup of all expired assets and send me a summary report.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the logic engine for identifying expired assets.
- Instruct the agent to prioritize safety by verifying expiration dates before executing deletion.
- Use a structured JSON output for the agent to communicate with the Composio Toolset.
- Set the agent's tone to be professional and reporting-oriented.

### 2) Composio Toolset Node
- Provide your Beaconstac API key within the Composio connection settings.
- Ensure the connection scope includes read and write permissions for QR code management.

### 3) Tool Availability
- `list_qr_codes`: Fetches current campaign data.
- `get_qr_details`: Retrieves metadata and expiration status for specific codes.
- `delete_qr_code`: Executes the removal of confirmed expired assets.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich account data to improve targeting accuracy.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform operational workflows.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) - Monitor and maintain account activity levels.
