# Pitch Deck Generator (Uplizd) - Automated Investor Presentation Creation

## Summary
The Pitch Deck Generator (Uplizd) is an AI-driven workflow designed to transform raw startup data and business concepts into professional, structured investor presentations. By leveraging the Composio Toolset to interface with Google Slides, this solution automates the slide creation process, ensuring consistent branding, logical flow, and high-quality content, ultimately saving founders hours of manual design and formatting time.

---

## Demo
![Pitch Deck Generator workflow interface showing data input to Google Slides automation](image.png)
**Alt text (SEO-ready):** Pitch Deck Generator Uplizd workflow, automated investor presentation creation, Google Slides integration, AI-powered startup deck builder, Composio workflow automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/ff8bd172-93e3-5004-8abd-0efdcb269a5e)

---

## Category
- **Primary category:** Sales automation
- **Secondary tags:** google slides, pitch deck, startup, investor relations, presentation, automation, composio, ai workflow
- This solution bridges the gap between raw business intelligence and visual storytelling for fundraising operations.

---

## Who is this for?
This solution is designed for professionals who need to produce high-impact visual narratives without the overhead of manual design.

- **Startup Founders**
    - Rapidly iterate on pitch decks to match different investor profiles or market feedback.
- **Investment Analysts**
    - Automate the creation of standardized portfolio company summaries and performance reports.
- **Marketing Managers**
    - Maintain visual brand consistency across all external-facing slide decks and company presentations.
- **Sales Operations Leads**
    - Generate customized sales collateral and pitch materials at scale for diverse client segments.

---

## Features
- **Automated Slide Generation**
  Instantly populate Google Slides templates with structured data, ensuring professional layout and design.
- **Dynamic Content Mapping**
  Intelligently map business metrics, market analysis, and team bios directly from your input into designated slide placeholders.
- **Composio Toolset Integration**
  Seamlessly connects to your Google Workspace, enabling secure and real-time interaction with your presentation files.
- **Investor-Ready Formatting**
  Applies professional formatting rules to ensure your deck meets industry standards for clarity and impact.
- **Version Control & Iteration**
  Quickly regenerate or update specific slides based on new data inputs without rebuilding the entire deck.

---

## Use Cases
**Fundraising Preparation**
- Generate a comprehensive 10-slide pitch deck from a raw business plan document.
- Create customized versions of a pitch deck tailored to specific venture capital firms.

**Corporate Reporting**
- Automate the creation of monthly board meeting slide decks using live performance metrics.
- Generate standardized quarterly business review (QBR) presentations for stakeholders.

**Sales Enablement**
- Build personalized pitch decks for high-value prospects based on CRM account data.
- Rapidly produce competitive analysis slides for sales teams to use in client meetings.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution in the Uplizd builder.
2. Connect your Google account via the Composio Toolset node to grant slide editing permissions.
3. Configure your input parameters, such as the target Google Slides template ID and the data source.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives your startup data, pitch narrative, or specific slide requirements.
- **Agent**: Processes the input and instructs the toolset on how to structure the slide content.
- **Composio Toolset**: Executes the API calls to Google Slides to insert text, images, and charts.
- **Chat Output**: Confirms the successful creation of the presentation and provides a link to the file.

### 3) Run the Flow
Use the Playground to test your deck generation:
- `Generate a 10-slide pitch deck for a SaaS startup focused on AI-driven CRM automation.`
- `Create a summary slide for our Q3 performance based on the provided growth metrics.`
- `Update the 'Market Opportunity' slide in the existing deck with the latest industry report data.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the creative director and structural architect for your presentation.
- **Instruction Pattern:**
    - Analyze the input data to identify key value propositions and market differentiators.
    - Map content to the specific slide structure defined in your Google Slides template.
    - Maintain a professional, persuasive tone suitable for investor audiences.

### 2) Composio Toolset Node
- **API Key:** Ensure your Google Workspace API key is configured within the Composio dashboard.
- **Connection Scope:** Grant `slides.readonly` and `slides.appends` permissions to allow the agent to read templates and write new content.

### 3) Tool Availability
- **Google Slides API**: For creating, reading, and updating presentation slides.
- **Google Drive API**: For managing file permissions and locating template files.
- **Text Processing Utility**: For summarizing long-form business data into concise bullet points.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) — Gather deep account intelligence to inform your pitch deck content.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) — Extract actionable insights from lead data to strengthen your market analysis slides.
- [Account Relationship Builder](../account-relationship-builder-by-dynamics365/README.md) — Manage and track investor relationships alongside your fundraising materials.
