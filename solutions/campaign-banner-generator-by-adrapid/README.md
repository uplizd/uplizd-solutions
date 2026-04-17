# Campaign Banner Generator (Uplizd) - Automated visual asset creation for marketing campaigns

## Summary
The Campaign Banner Generator is an intelligent Uplizd workflow that transforms simple text-based marketing briefs into high-quality visual campaign banners. By leveraging the AdRapid integration, this solution eliminates manual design bottlenecks, ensuring marketing teams can maintain pipeline velocity and brand consistency across all digital channels without needing dedicated graphic design resources for every iteration.

---

## Demo
![Campaign Banner Generator workflow showing text input to AdRapid banner output](../image.png)
**Alt text (SEO-ready):** Campaign Banner Generator by AdRapid for Uplizd, automating marketing asset creation and visual design workflows.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/742ee7e3-5486-58ed-9079-9abc27ee2143)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** adrapid, creative automation, banner generation, marketing assets, content workflow, design automation, composio, ai workflow
- This solution streamlines the creative production process by connecting marketing intent directly to automated visual generation tools.

---

## Who is this for?
This solution is designed for marketing professionals and creative teams looking to scale their visual output.

- **Digital Marketer**
  - Accelerate campaign launch timelines by generating variations of ad assets instantly.
- **Content Strategist**
  - Ensure visual brand alignment across multiple platforms without manual design oversight.
- **Social Media Manager**
  - Rapidly produce platform-specific banner sizes for high-frequency social media updates.
- **Growth Hacker**
  - Enable high-volume A/B testing of visual creatives to optimize click-through rates.

---

## Features
- **Automated Design Generation**
  - Convert text-based campaign briefs into professional-grade banners using the AdRapid engine.
- **Dynamic Template Mapping**
  - Map specific marketing variables to design templates to ensure consistent brand identity.
- **Multi-Platform Scaling**
  - Generate multiple banner dimensions and formats from a single source of truth.
- **Composio-Powered Integration**
  - Seamlessly connect your marketing workflow to design APIs for real-time asset delivery.
- **Rapid Iteration Cycles**
  - Update campaign messaging and regenerate visual assets in seconds, not hours.

---

## Use Cases
**Campaign Launch Acceleration**
- Generate a full suite of display banners for a new product launch based on a single marketing brief.
- Create localized banner variations for international markets by dynamically updating text layers.

**Social Media Ad Optimization**
- Produce platform-specific assets (e.g., LinkedIn, Facebook, Instagram) from one core campaign concept.
- Refresh ad creative daily by feeding new performance data into the banner generation pipeline.

**Brand Consistency Management**
- Enforce strict brand guidelines by using pre-approved templates for all automated banner outputs.
- Maintain a unified visual language across all digital touchpoints by automating the design process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Campaign Banner Generator solution.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your AdRapid API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the campaign brief, target audience, and desired dimensions.
- **Agent**: Interprets the creative brief and maps requirements to the design template.
- **Composio Toolset**: Executes the API calls to AdRapid to render the visual assets.
- **Chat Output**: Returns the final banner image URLs or download links to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Create a 1200x628 banner for our Q4 software sale targeting CTOs, use a professional blue theme.`
- `Generate a set of Instagram story banners for the upcoming summer webinar series.`
- `Design a display ad for our new whitepaper, focusing on the headline "Scale Your Infrastructure".`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative director, translating natural language into design parameters.
- Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5).
- Instruct the agent to extract dimensions, color palettes, and copy from the user input.
- Maintain a strict mapping between user-defined campaign goals and template IDs.

### 2) Composio Toolset Node
- Provide your AdRapid API key in the connection settings.
- Ensure the scope allows for "Create Asset" and "Render Template" permissions.

### 3) Tool Availability
- **Template Retrieval**: Fetch available design templates and their required parameters.
- **Asset Generation**: Trigger the rendering engine with mapped text and image inputs.
- **Status Monitoring**: Verify the completion of render jobs before returning the final URL.

---

## Related Solutions
- [../ab-test-optimizer-by-mixpanel/README.md](../ab-test-optimizer-by-mixpanel/README.md) - Optimize your campaign performance using data-driven insights.
- [../you-tube-content-distribution-agent-by-youtube/README.md](../you-tube-content-distribution-agent-by-youtube/README.md) - Automate the distribution of your video content and associated assets.
- [../accessibility-compliance-generator-by-aivoov/README.md](../accessibility-compliance-generator-by-aivoov/README.md) - Ensure your generated banners meet accessibility standards.
