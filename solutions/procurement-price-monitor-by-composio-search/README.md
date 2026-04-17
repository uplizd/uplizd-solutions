# Procurement Price Monitor (Uplizd) - Automated supplier research and real-time price comparison

## Summary
The Procurement Price Monitor is an intelligent Uplizd workflow that automates supplier research and price benchmarking across multiple digital marketplaces. By leveraging the Composio Toolset to interface with live search and data extraction APIs, this solution enables procurement teams to maintain a single source of truth for market pricing, significantly reducing manual research time and ensuring competitive vendor selection.

---

## Demo
![Procurement Price Monitor workflow showing automated search, data extraction, and price comparison nodes](image.png)
**Alt text (SEO-ready):** Uplizd procurement price monitor workflow using Composio search tools for automated supplier research and competitive price analysis.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAQAAAAEBAQAAAP//AwA+0wEBAAAAEElEQVR42mNgGAWjYBSMglEwAAAEBAQAAA==)](https://uplizd.ai/solutions/67d13322-227d-5652-bf8e-369994a8d40b)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** procurement, price comparison, web scraping, supply chain, market intelligence, composio, ai workflow, data extraction
- This solution streamlines procurement operations by automating the collection and analysis of vendor pricing data from external web sources.

---

## Who is this for?
This workflow is designed for professionals responsible for cost management and vendor relations who need to stay ahead of market fluctuations.

- **Procurement Manager**
    - Automates the tedious process of manual price benchmarking across multiple supplier portals.
- **Supply Chain Analyst**
    - Provides real-time visibility into market price trends to optimize inventory purchasing cycles.
- **Operations Lead**
    - Ensures data hygiene by centralizing disparate pricing information into a structured, actionable format.
- **Finance Controller**
    - Validates vendor quotes against real-time market data to prevent overspending and improve margin control.

---

## Features
- **Automated Market Research**
    - Uses advanced search agents to scan multiple supplier platforms simultaneously for specific product pricing.
- **Real-Time Data Extraction**
    - Leverages the Composio Toolset to parse complex web data into clean, structured JSON formats.
- **Dynamic Price Benchmarking**
    - Automatically compares extracted prices against internal cost targets or historical baseline data.
- **Intelligent Alerting**
    - Triggers notifications when price drops or spikes are detected for critical procurement items.
- **Unified Reporting**
    - Aggregates findings into a single, easy-to-read output for rapid decision-making by stakeholders.

---

## Use Cases
**Supplier Price Benchmarking**
- Comparing unit costs for raw materials across three or more primary vendors.
- Identifying seasonal price fluctuations for high-volume inventory items.

**Vendor Negotiation Support**
- Generating data-backed reports to leverage lower competitor pricing during contract renewals.
- Validating vendor quotes against current market averages to ensure competitive procurement.

**Market Intelligence Gathering**
- Tracking the availability and pricing of new product releases from key industry competitors.
- Monitoring price changes in real-time to adjust internal procurement budgets dynamically.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution in the Uplizd builder.
2. Review the pre-configured workflow structure in the canvas.
3. Connect your required API credentials within the Composio Toolset node settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the product name or SKU to be researched.
- **Agent**: Processes the request and determines the necessary search parameters.
- **Composio Toolset**: Executes the web search and data extraction queries.
- **Chat Output**: Returns the summarized pricing report to the user.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Find the current market price for 500 units of industrial-grade steel bolts.`
- `Compare the pricing for 'Model X' laptop across major electronics suppliers.`
- `Search for the lowest available price for bulk office stationery and summarize the top three vendors.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the procurement research lead, synthesizing search results into actionable insights.
- Instruct the agent to prioritize verified vendor sources.
- Set the output format to prioritize price-per-unit comparisons.
- Configure the agent to highlight the most cost-effective procurement options.

### 2) Composio Toolset Node
- Provide your API key for the search and scraping integrations.
- Define the connection scope to include specific supplier domains or general search engines.

### 3) Tool Availability
- **Search Engine API**: For broad market discovery.
- **Web Scraper Tool**: For extracting specific pricing tables from vendor sites.
- **Data Parser**: For converting unstructured HTML data into clean, comparable metrics.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Automates deep-dive research on potential vendor accounts.
- [Account Reconciliation Helper](../account-reconciliation-helper-by-quickbooks/README.md) — Streamlines financial data matching and invoice verification.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Orchestrates complex multi-step procurement and operations tasks.
