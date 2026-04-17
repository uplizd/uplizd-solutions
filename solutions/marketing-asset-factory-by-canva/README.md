# Marketing Asset Factory (Uplizd) - Automate branded campaign visual production

## Summary
The Marketing Asset Factory is an intelligent Uplizd workflow that streamlines the creation of high-quality, branded marketing collateral. By integrating generative AI with design platforms like Canva, this solution enables marketing teams to transform campaign briefs into production-ready assets instantly, ensuring brand consistency, accelerating time-to-market, and eliminating manual design bottlenecks.

---

## Demo
![Marketing Asset Factory workflow diagram showing AI-driven design generation](image.png)
**Alt text (SEO-ready):** Marketing Asset Factory workflow diagram showing AI-driven design generation with Uplizd, Canva integration, and automated campaign asset creation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/marketing-asset-factory-by-canva)

---

## Category
**Marketing operations**
**Tags:** marketing, canva, generative ai, brand consistency, content automation, design workflow, composio, campaign management.
This solution bridges the gap between creative strategy and production by automating repetitive design tasks within the marketing lifecycle.

---

## Who is this for?
This solution is designed for marketing teams looking to scale content production without sacrificing brand integrity.

* **Content Manager**
  * Automates the generation of social media graphics and ad banners from standardized templates.
* **Brand Designer**
  * Ensures all AI-generated assets adhere to pre-defined brand guidelines and color palettes.
* **Campaign Coordinator**
  * Reduces the turnaround time for multi-channel campaign asset delivery.
* **Social Media Specialist**
  * Rapidly produces platform-specific variations of visual content to maintain high engagement.

---

## Features
- **Template-Driven Generation**
  Automatically populates pre-designed Canva templates with campaign-specific text and imagery.
- **Brand Identity Enforcement**
  Uses AI to ensure all generated assets maintain consistent fonts, logos, and color schemes.
- **Multi-Platform Resizing**
  Instantly generates optimized variations of a single design for Instagram, LinkedIn, and Twitter.
- **Composio-Powered Integration**
  Leverages the Composio Toolset to securely communicate with the Canva API for real-time asset creation.
- **Automated Review Workflow**
  Routes generated assets to a staging folder for final human approval before deployment.

---

## Use Cases
**Campaign Launch Acceleration**
* Generating a full suite of display ads from a single campaign brief.
* Creating localized versions of marketing collateral for different regional markets.

**Social Media Content Scaling**
* Transforming blog post summaries into engaging carousel graphics.
* Automating the production of daily promotional banners for seasonal sales.

**Brand Hygiene Maintenance**
* Updating outdated visual assets across all active marketing campaigns.
* Ensuring all team-generated content uses the latest approved brand assets from Canva.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution in your workspace.
2. Select your preferred project folder to initialize the workflow.
3. Authenticate your Canva account via the Composio connection prompt.
4. Ensure nodes are correctly mapped and all API credentials are saved in the environment settings.

### 2) Setup the Nodes
* **Chat Input**: Receives the campaign brief, target platform, and design dimensions.
* **Agent**: Interprets the brief and selects the appropriate Canva template ID.
* **Composio Toolset**: Executes the API calls to Canva to generate and export the visual asset.
* **Chat Output**: Returns the final asset link or confirmation of successful generation.

### 3) Run the Flow
Use the Playground to test your asset generation:
* `Create a 1080x1080 Instagram post for our Summer Sale campaign using the 'Minimalist' template.`
* `Generate a LinkedIn banner for the upcoming product webinar based on the provided event details.`
* `Create 3 variations of a promotional graphic for the 'New Arrivals' collection using the brand color palette.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a creative director that maps natural language requests to design parameters.
* Use a model capable of structured JSON output for template mapping.
* Instruction: "Analyze the user request to identify the campaign theme and required dimensions."
* Instruction: "Map the request to the correct Canva template ID from the available toolset."

### 2) Composio Toolset Node
* Requires a valid Canva API key with `design:write` and `asset:read` scopes.
* Ensure the toolset is configured to access your team’s shared folder for template retrieval.

### 3) Tool Availability
* `canva_create_design`: Generates new designs from templates.
* `canva_get_templates`: Retrieves available brand-approved templates.
* `canva_export_design`: Exports final assets to your preferred storage location.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich lead data to inform personalized marketing campaigns.
* [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) - Analyze video metrics to refine visual content strategy.
* [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensure all marketing assets meet accessibility standards automatically.
