# Portfolio Website Code Generator (Uplizd) - Automate resume-to-portfolio web development

## Summary
The Portfolio Website Code Generator is an intelligent Uplizd workflow that bridges the gap between static career documents and professional web presence. By parsing PDF or TXT resumes into structured JSON and mapping them to responsive HTML templates, this solution enables developers, designers, and job seekers to automate the creation of high-quality portfolio sites, ensuring consistent data hygiene and rapid deployment of professional profiles.

---

## Demo
![Portfolio Website Code Generator workflow interface showing resume parsing and HTML output](image.png)
**Alt text (SEO-ready):** Uplizd Portfolio Website Code Generator workflow, automated resume-to-HTML conversion, JSON data structuring, and web development automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8266fed4-eed1-5b29-b35d-0d0c1c186a2a)

---

## Category
**Primary category:** Web Development Automation
**Secondary tags:** resume parsing, json, html generation, portfolio builder, web development, automation, ai workflow, composio

This solution streamlines the transition from raw career documentation to a live web presence by automating the extraction and formatting of professional data.

---

## Who is this for?
This solution is designed for professionals looking to maintain a modern web presence without manual coding effort.

- **Software Developers**
    - Automate the generation of personal portfolio sites directly from updated resume files.
- **Graphic Designers**
    - Quickly convert text-based experience summaries into structured, web-ready HTML layouts.
- **Career Coaches**
    - Provide clients with a scalable tool to instantly generate professional landing pages from existing documents.
- **Technical Recruiters**
    - Standardize candidate portfolio formats by automating the ingestion of diverse resume file types.

---

## Features
- **Intelligent Resume Parsing**
    - Uses advanced extraction logic to convert unstructured PDF or TXT resume data into clean, machine-readable JSON.
- **Automated HTML Generation**
    - Maps extracted professional experience, skills, and education directly into responsive, pre-defined HTML templates.
- **Structured Data Mapping**
    - Ensures consistency across portfolio fields, maintaining high data hygiene for web-ready content.
- **Composio Toolset Integration**
    - Leverages secure tool connectors to handle file processing and code output generation in real-time.
- **Rapid Deployment Workflow**
    - Reduces the time-to-market for personal websites from hours of manual coding to seconds of automated processing.

---

## Use Cases
**Personal Branding**
- Convert a legacy PDF resume into a modern, responsive single-page portfolio site.
- Update portfolio content dynamically by simply uploading a new version of your TXT resume.

**Agency Portfolio Management**
- Standardize the presentation of team member profiles across an agency's main website.
- Batch process multiple employee resumes to generate consistent team-page HTML code.

**Developer Productivity**
- Automate the creation of boilerplate portfolio code, allowing for quick customization of CSS and layout styles.
- Sync resume updates with website content to ensure professional credentials remain current.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button to open the template in your workspace.
2. Connect your preferred LLM provider to the Agent node.
3. Configure the Composio Toolset node with your API credentials.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw resume file (PDF/TXT) and user styling preferences.
- **Agent**: Analyzes the document, extracts key professional data, and maps it to the JSON schema.
- **Composio Toolset**: Executes file parsing and triggers the HTML generation script.
- **Chat Output**: Delivers the final, ready-to-deploy HTML code block.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Generate a portfolio website HTML for the attached resume, using a minimalist dark-mode theme.`
- `Extract my work history from this PDF and format it into a structured JSON object for my portfolio.`
- `Create a responsive HTML portfolio template based on the provided text resume, including a contact section.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the data extraction and transformation engine.
- Use a model with high reasoning capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions for JSON schema adherence.
- Ensure the agent is instructed to prioritize accuracy in extracting dates and job titles.

### 2) Composio Toolset Node
- Provide your **Composio API Key** to enable file-handling capabilities.
- Set the connection scope to allow read access to document storage and write access for code generation.

### 3) Tool Availability
- **File Parser**: Extracts text from PDF and TXT formats.
- **JSON Formatter**: Structures raw data into clean, key-value pairs.
- **HTML Generator**: Maps JSON data into responsive web templates.

---

## Related Solutions
- [Accessibility Audit Assistant](../accessibility-audit-assistant-by-figma/README.md) - Automate design compliance checks.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline business process automation.
- [Workspace Setup Optimizer](../workspace-setup-optimizer-by-clockify/README.md) - Optimize productivity and environment settings.
