# Adaptive Learning Curriculum Builder (Uplizd) - Personalized AI-Driven Education Paths

## Summary
The Adaptive Learning Curriculum Builder is an intelligent Uplizd workflow that automates the creation of customized educational paths by leveraging real-time content curation. Designed for educators, corporate trainers, and lifelong learners, this solution transforms static syllabi into dynamic, data-backed learning experiences, ensuring high engagement and improved knowledge retention through automated content discovery and sequencing.

---

## Demo
![Adaptive Learning Curriculum Builder workflow screenshot showing Chat Input, Agent node with Perplexity AI, and Composio Toolset output](image.png)
**Alt text (SEO-ready):** Adaptive Learning Curriculum Builder workflow on Uplizd, featuring AI-driven content curation, automated syllabus generation, and Perplexity AI integration for personalized education paths.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/6fe970f3-e9f3-5f15-b4e7-1243961beaf8)

---

## Category
- **Primary category:** Education Technology
- **Secondary tags:** ai, curriculum, personalization, perplexity, learning management, content curation, edtech, workflow automation
- This solution bridges the gap between static instructional design and dynamic, AI-powered content delivery for modern learning environments.

---

## Who is this for?
This solution is designed for professionals managing complex knowledge transfer and skill development programs.

- **Instructional Designers**
    - Automate the research and assembly of diverse learning materials to reduce manual curriculum development time.
- **Corporate Trainers**
    - Deliver personalized onboarding and upskilling paths that adapt to individual employee knowledge gaps.
- **Academic Program Managers**
    - Ensure course materials remain current by integrating real-time web research into existing academic frameworks.
- **EdTech Product Managers**
    - Prototype and deploy adaptive learning features that leverage external search intelligence to enhance user outcomes.

---

## Features
- **Dynamic Content Curation**
    - Automatically fetches the most relevant and up-to-date educational resources using Perplexity AI search capabilities.
- **Personalized Path Generation**
    - Tailors learning modules based on user-defined skill levels, goals, and preferred learning formats.
- **Real-time Knowledge Synthesis**
    - Aggregates information from disparate sources into a cohesive, structured curriculum document.
- **Composio-Powered Integration**
    - Seamlessly connects the agent to external search tools and document management systems for streamlined workflow execution.
- **Adaptive Feedback Loop**
    - Adjusts the curriculum structure based on the agent's iterative analysis of search results and user requirements.

---

## Use Cases
**Corporate Upskilling**
- Generate custom training modules for new software rollouts based on specific team roles.
- Create rapid-response learning paths for compliance updates using the latest industry documentation.

**Academic Research Support**
- Build comprehensive reading lists and study guides for specialized research topics in real-time.
- Synthesize complex academic papers into simplified summaries for introductory course modules.

**Personalized Skill Development**
- Design a multi-week learning roadmap for mastering new programming languages or technical frameworks.
- Curate daily learning micro-lessons based on a user's evolving interest in emerging market trends.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Adaptive Learning Curriculum Builder template from the solution library.
3. Connect your preferred LLM provider and API credentials for the search tools.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts the user's learning goal, target skill level, and time constraints.
- **Agent**: Processes the request and orchestrates the research strategy using Perplexity AI.
- **Composio Toolset**: Executes real-time web searches and retrieves high-quality educational content.
- **Chat Output**: Delivers the structured, personalized curriculum directly to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Create a 4-week curriculum for a beginner learning Python for data science.`
- `Build a summary and reading list for the latest advancements in generative AI for healthcare.`
- `Design a personalized study plan for a mid-level manager transitioning into a product leadership role.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the instructional architect, synthesizing research into actionable learning paths.
- Set the system prompt to prioritize pedagogical structure and clarity.
- Use a high-context window model (e.g., GPT-4o or Claude 3.5) to ensure complex curricula remain coherent.
- Configure temperature settings between 0.3 and 0.5 for a balance of creativity and factual accuracy.

### 2) Composio Toolset Node
- Provide your Perplexity API key to enable high-fidelity web research.
- Set the connection scope to allow the agent to perform broad searches across academic and technical domains.

### 3) Tool Availability
- **Search Engine Access**: For retrieving the latest articles, documentation, and tutorials.
- **Data Summarization**: For distilling long-form content into digestible curriculum modules.
- **Formatting Tools**: For organizing output into structured Markdown tables and lists.

---

## Related Solutions
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) — Monitor and analyze the reach of academic publications.
- [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) — Enhance the quality and clarity of scholarly writing.
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) — Automate the creation and organization of collaborative workshop materials.
