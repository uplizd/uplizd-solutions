# Space Education Curator (Uplizd) - Automated STEM content discovery and curriculum alignment

## Summary
The Space Education Curator is an intelligent Uplizd workflow designed to automate the discovery, filtering, and organization of astronomical data and educational resources from NASA. By leveraging real-time API integration, this solution empowers educators and researchers to maintain a high-velocity pipeline of verified space science content, ensuring that curriculum materials remain accurate, engaging, and aligned with current scientific discoveries.

---

## Demo
![Space Education Curator workflow interface showing NASA API integration and automated content filtering](image.png)
**Alt text (SEO-ready):** Space Education Curator Uplizd workflow for automated NASA data retrieval, STEM content filtering, and educational resource organization via Composio.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/540186b0-0b96-5ab1-9c7d-326661ffbd26)

---

## Category
- **Primary category:** Education technology
- **Secondary tags:** nasa, stem, content curation, data integration, composio, ai workflow, research automation, curriculum development
- This solution bridges the gap between raw astronomical data streams and structured educational content, providing a streamlined pipeline for academic resource management.

---

## Who is this for?
This solution is designed for professionals and institutions dedicated to advancing space science literacy through automated data management.

- **STEM Educators**
    - Automate the collection of daily space facts and imagery to keep classroom materials current.
- **Science Curriculum Developers**
    - Rapidly source verified astronomical data to build structured, accurate lesson modules.
- **Academic Researchers**
    - Monitor new NASA data releases and filter relevant findings for ongoing study projects.
- **Educational Content Managers**
    - Maintain a consistent, high-quality stream of space-themed media for digital learning platforms.

---

## Features
- **Automated NASA Data Retrieval**
    - Seamlessly fetches real-time data and imagery from NASA’s public APIs using the Composio Toolset.
- **Intelligent Content Filtering**
    - Uses AI-driven logic to categorize space content by difficulty level, topic, and educational relevance.
- **Structured Resource Mapping**
    - Automatically formats retrieved data into standardized templates suitable for LMS or digital publication.
- **Real-time Sync & Updates**
    - Ensures that educational databases are updated as soon as new astronomical discoveries are published.
- **Customizable Prompt Engineering**
    - Allows users to define specific scientific focus areas, ensuring the agent retrieves only the most pertinent information.

---

## Use Cases
**Curriculum Enrichment**
- Automatically pull "Image of the Day" data to populate daily classroom warm-up activities.
- Generate summary reports of recent Mars rover findings for high school science modules.

**Research Monitoring**
- Track specific celestial events or mission milestones to provide timely updates to research teams.
- Filter raw telemetry data into simplified summaries for undergraduate-level study guides.

**Digital Content Production**
- Curate a weekly digest of space news for educational newsletters or social media channels.
- Organize NASA media assets into categorized folders based on scientific themes like "Exoplanets" or "Solar Physics."

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Solution."
2. Import the `space-education-curator-by-nasa` template from the repository.
3. Configure your environment variables, including your NASA API credentials.
4. Ensure nodes are correctly connected in the builder and verify that the Agent has access to the required Composio Toolset.

### 2) Setup the Nodes
- **Chat Input**: Receives user requests for specific space topics or timeframes.
- **Agent**: Processes the request and determines the necessary API calls to fetch data.
- **Composio Toolset**: Executes the authenticated requests to NASA's endpoints.
- **Chat Output**: Delivers the curated, formatted educational content to the user.

### 3) Run the Flow
Open the Playground and test with these prompts:
- `Find the latest high-resolution images from the James Webb Space Telescope and summarize their scientific significance.`
- `Create a 5-day curriculum plan based on recent Mars exploration data.`
- `List the most significant astronomical discoveries published by NASA in the last 48 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary orchestrator for interpreting educational needs and mapping them to data queries.
- **Role:** Scientific Content Analyst.
- **Instruction Pattern:** 
    - Prioritize accuracy by cross-referencing NASA API metadata.
    - Maintain a neutral, educational tone suitable for academic environments.
    - Format output in structured Markdown for easy integration into learning management systems.

### 2) Composio Toolset Node
- **API Key:** Provide your valid NASA API key in the environment configuration.
- **Connection Scope:** Ensure the toolset has read-access to the relevant NASA data endpoints.

### 3) Tool Availability
- **NASA Data Fetcher:** Retrieves raw mission data, imagery, and telemetry.
- **Content Formatter:** Standardizes output into educational summaries.
- **Search & Filter:** Allows the agent to query specific date ranges or scientific categories.

---

## Related Solutions
- [Adaptive Learning Curriculum Builder](../adaptive-learning-curriculum-builder-by-perplexityai/README.md) - AI-driven tools for creating personalized educational pathways.
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) - Monitor and analyze the reach of scientific publications and research.
- [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) - Improve the clarity and accuracy of educational and scientific documentation.
