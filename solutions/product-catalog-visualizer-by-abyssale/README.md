# Product Catalog Visualizer (Uplizd) - Automated visual asset generation and catalog management

## Summary
The Product Catalog Visualizer (Uplizd) is an intelligent automation workflow designed to streamline the creation of high-quality product visuals and structured catalogs. By integrating AI-driven image generation with your existing product database, this solution eliminates manual design bottlenecks, ensuring your marketing assets are always synchronized with your inventory for improved pipeline velocity and brand consistency.

---

## Demo
![Product Catalog Visualizer workflow interface showing automated image generation and catalog sync](image.png)

**Alt text (SEO-ready):** Product Catalog Visualizer (Uplizd) workflow showing automated image generation, product data integration, and catalog management via Composio toolset.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-0acdc623--2db5--54eb--a7ba--312ced9f2b4c-blue)](https://uplizd.ai/solutions/0acdc623-2db5-54eb-a7ba-312ced9f2b4c)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** product catalog, visual assets, ai generation, abyssale, automation, ecommerce, content operations, composio
- This solution bridges the gap between raw product data and visual marketing collateral, enabling automated content pipelines for modern e-commerce teams.

---

## Who is this for?
This workflow is built for teams looking to scale their visual content production without increasing headcount.

- **E-commerce Manager**
    - Automates the generation of product imagery for new inventory drops, reducing time-to-market.
- **Marketing Designer**
    - Offloads repetitive template-based visual tasks to the AI, allowing focus on high-level creative strategy.
- **Catalog Specialist**
    - Maintains a single source of truth by syncing product specifications directly with generated visual assets.
- **Operations Lead**
    - Improves pipeline velocity by ensuring all sales channels receive updated product visuals simultaneously.

---

## Features
- **Automated Visual Generation**
    - Leverages AI to transform raw product data into professional-grade visual assets using dynamic templates.
- **Real-time Catalog Sync**
    - Ensures that any change in product attributes or pricing is immediately reflected in the visual catalog.
- **Composio Toolset Integration**
    - Seamlessly connects your product database with design APIs to execute complex visual workflows.
- **Template-Driven Consistency**
    - Maintains strict brand guidelines by applying consistent design rules across all generated product imagery.
- **Bulk Processing Engine**
    - Handles large-scale catalog updates efficiently, processing hundreds of product items in a single automated run.

---

## Use Cases
**New Product Launches**
- Automatically generate social media assets and website banners for upcoming product releases.
- Sync new product specifications with generated visuals to ensure immediate availability across all sales channels.

**Seasonal Catalog Updates**
- Update existing product visuals to reflect seasonal themes or promotional discounts in bulk.
- Refresh catalog imagery for entire product categories based on inventory availability and current trends.

**Multi-Channel Asset Distribution**
- Create platform-specific visual formats for different marketplaces and social media outlets.
- Standardize visual quality across various regional catalogs to maintain a cohesive global brand identity.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Product Catalog Visualizer template from the marketplace.
3. Connect your preferred product database and design API (e.g., Abyssale) via the Composio Toolset.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives product IDs or catalog update requests from the user.
- **Agent**: Interprets the request, fetches product data, and instructs the design tool.
- **Composio Toolset**: Executes the API calls to generate visuals and update the catalog.
- **Chat Output**: Confirms successful generation and provides links to the new visual assets.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Generate a new product catalog visual for product ID 5502 using the 'Spring-Sale' template.`
- `Update all visuals for the 'Electronics' category with the latest pricing and feature specs.`
- `Create a promotional banner for the new arrivals collection and sync it to the main catalog.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between your data and the design engine.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5).
- Provide clear instructions on mapping product attributes to design template variables.
- Ensure the agent is configured to handle error states if an image generation fails.

### 2) Composio Toolset Node
- Provide your API keys for the design platform (e.g., Abyssale) and your product database.
- Set the connection scope to allow read/write access to your product catalog and asset storage.

### 3) Tool Availability
- **Product Data Fetcher**: Retrieves real-time product details.
- **Visual Generation Engine**: Applies data to design templates.
- **Asset Storage Manager**: Saves and organizes generated files.

---

## Related Solutions
- [ab-test-visual-documenter-by-apiflash](../ab-test-visual-documenter-by-apiflash/README.md) - Automates the visual documentation of A/B test variants.
- [account-setup-agent-by-salesforce](../account-setup-agent-by-salesforce/README.md) - Streamlines the onboarding and setup of new accounts in your CRM.
- [whats-app-lead-nurturing-agent-by-spoki](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Automates lead engagement and nurturing via WhatsApp.
