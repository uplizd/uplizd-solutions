# Customer Journey Mapping Agent (Uplizd) - Automate visual customer experience mapping from research data

## Summary
The Customer Journey Mapping Agent by Mural streamlines the creation and maintenance of visual customer experience maps by synthesizing raw research data into actionable insights. By leveraging the Composio Toolset to interface with Mural and research repositories, this workflow eliminates manual documentation bottlenecks, ensuring that product and design teams maintain a single source of truth for user touchpoints and pain points.

---

## Demo
![Customer Journey Mapping Agent interface showing automated Mural board population from research data](image.png)
**Alt text (SEO-ready):** Customer Journey Mapping Agent by Mural, Uplizd AI workflow for automated UX research visualization and customer experience mapping.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6bfa0e92-77da-56ca-977b-f070526dc2c7)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** customer journey, ux research, mural, design ops, ai workflow, composio, data visualization, user experience
- This solution bridges the gap between raw qualitative research and visual strategy, enabling teams to automate the documentation of complex user journeys.

---

## Who is this for?
This agent is designed for teams that need to turn scattered user feedback into structured visual strategies.

- **UX Researchers**
    - Rapidly translate interview transcripts into structured journey map stages and emotional trend lines.
- **Product Managers**
    - Maintain up-to-date visual representations of user friction points to prioritize the product roadmap.
- **Design Leads**
    - Automate the population of Mural templates to ensure design consistency across multiple product workstreams.
- **Customer Success Managers**
    - Visualize the end-to-end customer lifecycle to identify churn risks and opportunities for proactive engagement.

---

## Features
- **Automated Mural Population**
    - Instantly generate sticky notes, connectors, and journey stages in Mural based on processed research inputs.
- **Research Synthesis Engine**
    - Utilize advanced LLM reasoning to extract key user sentiments and behavioral patterns from unstructured text.
- **Dynamic Template Mapping**
    - Map research findings directly into existing Mural frameworks, ensuring your data fits your team's preferred visual structure.
- **Real-time Sync**
    - Ensure your journey maps reflect the latest user feedback by triggering updates directly from your research repository.
- **Cross-Platform Integration**
    - Seamlessly connect research data sources with the Composio Toolset to execute complex mapping workflows without manual copy-pasting.

---

## Use Cases
**UX Research Documentation**
- Automatically populate journey maps after completing a batch of user interviews.
- Categorize user pain points by stage (Awareness, Consideration, Decision) within Mural.

**Product Strategy Alignment**
- Visualize the impact of new feature releases on the overall customer journey.
- Identify and highlight stalled user segments that require immediate product intervention.

**Design Operations Efficiency**
- Standardize the format of journey maps across different product teams using pre-defined Mural templates.
- Reduce the time spent on manual documentation, allowing designers to focus on high-level strategy.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to access the solution template.
2. Select your workspace and project destination.
3. Authenticate your Mural account within the Composio connection manager.
4. Ensure nodes are correctly mapped: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives raw research data or interview summaries.
- **Agent**: Analyzes the input to identify journey stages and user sentiments.
- **Composio Toolset**: Executes API calls to create and organize elements within your Mural board.
- **Chat Output**: Confirms successful board updates and provides a summary of the mapped data.

### 3) Run the Flow
Use the Playground to test the agent with your research data:
- `Map the following research notes into a 5-stage journey map in Mural: [Insert Notes]`
- `Update the existing 'Q3 User Journey' board with these new pain points from our recent survey.`
- `Create a new journey map for the 'Onboarding' flow based on the attached user feedback summary.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a research analyst and visual strategist.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate sentiment extraction.
- Instruct the agent to strictly follow the JSON schema required by the Mural API.
- Define clear persona instructions to ensure the tone of the journey map remains professional and objective.

### 2) Composio Toolset Node
- Provide your Mural API key and ensure the connection scope includes `board:write` and `content:create` permissions.
- Verify that the agent has access to your specific workspace ID.

### 3) Tool Availability
- **Mural API**: For creating boards, adding sticky notes, and drawing connectors.
- **Data Parser**: For cleaning and structuring raw research text.
- **Sentiment Analyzer**: For mapping user feedback to emotional states on the journey map.

---

## Related Solutions
- [Workshop Facilitator Agent](../workshop-facilitator-agent-by-mural/README.md) - Automate the setup and management of collaborative workshops in Mural.
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Manage and deploy standardized workshop templates across your organization.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Gather and synthesize account intelligence to inform your customer journey strategy.
