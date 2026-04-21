# Training Course Creator (Uplizd) - Automated slide deck generation from training materials

## Summary
The Training Course Creator (Uplizd) is an AI-powered workflow that transforms raw training documentation, PDFs, and text-based outlines into structured, professional slide presentations. By leveraging the Composio Toolset to interface with Google Slides, this solution eliminates manual formatting time, ensuring that educational content is consistently organized, visually aligned, and ready for delivery, ultimately increasing instructional design velocity.

---

## Demo
![Training Course Creator workflow interface showing document ingestion and Google Slides generation](image.png)
**Alt text (SEO-ready):** Training Course Creator Uplizd workflow, automated Google Slides generation, AI-powered instructional design, document-to-presentation automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3ab64cda-8a49-53c0-849b-9bbb9363c65d)

---

## Category
**Primary category:** Operations
**Secondary tags:** google slides, training, automation, content creation, instructional design, ai workflow, composio, productivity
This solution streamlines the creation of educational materials by bridging the gap between raw knowledge bases and visual presentation software.

---

## Who is this for?
This solution is designed for professionals who need to convert dense information into digestible visual formats efficiently.

- **Instructional Designers**
    - Rapidly prototype slide decks from existing curriculum documentation.
- **Corporate Trainers**
    - Standardize onboarding materials across multiple departments without manual design work.
- **HR Managers**
    - Automate the creation of company policy and compliance training presentations.
- **Subject Matter Experts**
    - Focus on content quality while the AI handles the structural layout and slide generation.

---

## Features
- **Automated Slide Structuring**
    - Automatically parses text input to create logical slide hierarchies, including title slides, bulleted lists, and summary sections.
- **Google Slides Integration**
    - Utilizes the Composio Toolset to directly push generated content into your Google Drive, creating editable presentation files.
- **Intelligent Content Summarization**
    - Condenses long-form training manuals into concise, high-impact bullet points suitable for presentation slides.
- **Real-time Formatting**
    - Applies consistent formatting rules to ensure that every slide maintains a professional look and feel.
- **Workflow Customization**
    - Allows users to define specific tone, audience, and slide count constraints to tailor the output to specific training needs.

---

## Use Cases
**Corporate Onboarding**
- Converting employee handbooks into interactive "Welcome to the Team" slide decks.
- Generating department-specific training modules from existing internal wikis.

**Compliance Training**
- Transforming dense legal or safety documentation into simplified, easy-to-follow training presentations.
- Updating annual compliance slides automatically when source policy documents are revised.

**Educational Content Development**
- Turning academic research papers into summarized lecture slides for classroom use.
- Creating quick-start guides and workshop decks from technical documentation.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select the "Import Flow" option.
2. Upload the provided solution file to initialize the workflow nodes.
3. Authenticate your Google Slides connection via the Composio Toolset.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts your raw training text, PDF content, or curriculum outline.
- **Agent**: Processes the input, summarizes key points, and structures the slide content.
- **Composio Toolset**: Executes the API calls to create and populate the Google Slides deck.
- **Chat Output**: Confirms the successful creation of the slide deck with a direct link to the file.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Create a 10-slide training deck from this text about our new cybersecurity protocols.`
- `Generate a slide presentation for a workshop on effective communication based on these notes.`
- `Summarize the attached PDF into a 5-slide onboarding deck for new sales hires.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the instructional designer, ensuring content is concise and well-structured.
- Use a high-reasoning model to ensure logical flow between slides.
- Instruct the agent to prioritize bullet points over long paragraphs.
- Ensure the agent maintains a professional and educational tone throughout the deck.

### 2) Composio Toolset Node
- Provide your Google API credentials within the Composio dashboard.
- Ensure the connection scope includes `slides.readonly` and `slides.app.create` permissions.

### 3) Tool Availability
- `google-slides-create-presentation`: Initializes a new slide deck.
- `google-slides-add-slide`: Appends new slides to the presentation.
- `google-slides-insert-text`: Populates slide placeholders with generated content.

---

## Related Solutions
- [Workshop Template Curator](../workshop-template-curator-by-miro/README.md) - Automates the selection and setup of collaborative workshop templates.
- [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) - Manages the end-to-end process of employee onboarding and document distribution.
- [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) - Refines technical and academic content for professional presentation.
