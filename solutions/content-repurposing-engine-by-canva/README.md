# Content Repurposing Engine (Uplizd) - Automate multi-format content distribution

## Summary
The Content Repurposing Engine is an intelligent Uplizd workflow that automatically transforms long-form content into diverse visual formats, enabling marketing teams to scale their reach across channels. By leveraging the Composio Toolset to interface with Canva, this solution eliminates manual design bottlenecks, ensures brand consistency, and maximizes content ROI through automated asset generation.

---

## Demo
![Content Repurposing Engine workflow diagram showing input processing, Canva design generation, and multi-channel output](image.png)
**Alt text (SEO-ready):** Content Repurposing Engine by Uplizd, automated marketing workflow, Canva design integration, AI content distribution, and social media asset generation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/9c6ccf6b-88bf-550c-be37-743176dfdb44)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** content marketing, canva, automation, social media, ai workflow, composio, brand consistency, asset generation
- This solution streamlines the creative pipeline by bridging the gap between raw text content and high-quality visual assets for cross-platform distribution.

---

## Who is this for?
This engine is designed for marketing professionals and creative teams looking to maximize their content output without increasing headcount.

- **Content Marketers**
    - Repurpose blog posts and whitepapers into social media graphics and slide decks in minutes.
- **Social Media Managers**
    - Maintain a consistent posting schedule by automating the creation of platform-specific visual assets.
- **Brand Designers**
    - Focus on high-level creative direction while the AI handles repetitive layout and formatting tasks.
- **Growth Hackers**
    - Increase pipeline velocity by rapidly testing different visual formats across multiple acquisition channels.

---

## Features
- **Automated Design Synthesis**
    - Uses AI to interpret text input and map it to pre-defined Canva templates for instant visual generation.
- **Multi-Format Transformation**
    - Converts single source content into various sizes and styles including Instagram posts, LinkedIn banners, and presentation slides.
- **Composio-Powered Integration**
    - Seamlessly connects your Uplizd workflow to Canva’s API, ensuring secure and real-time asset creation.
- **Brand Asset Management**
    - Applies your specific brand guidelines, fonts, and color palettes automatically to every generated asset.
- **Real-Time Workflow Feedback**
    - Provides instant status updates and preview links for generated designs directly within your chat interface.

---

## Use Cases
**Social Media Scaling**
- Convert a long-form industry report into a 5-slide carousel for LinkedIn.
- Generate platform-optimized image assets from a single promotional blog post.

**Internal Communications**
- Transform meeting notes or project updates into professional-looking summary infographics.
- Automate the creation of announcement graphics for internal company newsletters.

**Campaign Rapid Prototyping**
- Create multiple visual variations of a campaign message to test audience engagement.
- Rapidly generate localized assets for global marketing campaigns using dynamic text injection.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Content Repurposing Engine template file provided in this repository.
3. Connect your Canva account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw text or URL of the content to be repurposed.
- **Agent**: Analyzes the content and extracts key insights for visual representation.
- **Composio Toolset**: Executes the API calls to Canva to generate the visual assets.
- **Chat Output**: Delivers the final design links and confirmation to the user.

### 3) Run the Flow
Open the Playground and try these prompts:
- `Repurpose this blog post into an Instagram carousel: [Insert URL]`
- `Create a LinkedIn banner based on these key takeaways: [Insert Text]`
- `Generate a slide deck summary for this whitepaper: [Insert URL]`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the creative director, summarizing content and mapping it to design parameters.
- Instruction: "You are an expert content strategist. Extract the core message and format it for the requested visual template."
- Instruction: "Ensure all generated text fits within the design constraints of the selected Canva template."
- Instruction: "Maintain a professional and engaging tone consistent with the brand guidelines provided."

### 2) Composio Toolset Node
- Requires a valid Canva API key and appropriate connection scopes for design creation.
- Configure the toolset to allow the agent to read template IDs and write new designs to your workspace.

### 3) Tool Availability
- **Canva Create Design**: Allows the agent to initiate new design projects.
- **Canva Template Fetcher**: Enables the agent to list and select available brand templates.
- **Asset Previewer**: Provides the agent with the ability to generate and return shareable design links.

---

## Related Solutions
- [YouTube Content Distribution Agent](../you-tube-content-distribution-agent-by-youtube/README.md) — Automate the syndication of video content across social channels.
- [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Ensure all repurposed visual assets meet accessibility standards.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) — Manage complex multi-step marketing workflows beyond content creation.
