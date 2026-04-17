# Content Quality Guardian (Uplizd) - Automated content consistency and brand compliance

## Summary
The Content Quality Guardian is an intelligent Uplizd AI workflow designed to automate the review, editing, and optimization of digital content. By leveraging the TextRazor API, this solution ensures that all drafted material meets your organization's specific brand voice, grammatical standards, and SEO requirements before publication, significantly reducing manual editing time and improving content velocity.

---

## Demo
![Content Quality Guardian workflow interface showing TextRazor analysis nodes and content refinement pipeline](image.png)
**Alt text (SEO-ready):** Content Quality Guardian Uplizd workflow, automated content editing, TextRazor AI integration, and brand compliance pipeline.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/4e247257-269e-591b-9334-3191e1bc04dc)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** content strategy, brand compliance, text analysis, seo, automation, composio, ai workflow, quality assurance.
This solution bridges the gap between creative drafting and editorial excellence by providing real-time, AI-driven feedback on content quality.

---

## Who is this for?
This solution is designed for teams that need to maintain high editorial standards across large volumes of content.

* **Content Managers**
    * Ensures all published articles adhere to brand guidelines and tone-of-voice requirements automatically.
* **SEO Specialists**
    * Validates that content contains necessary keyword density and structural elements to rank effectively.
* **Technical Writers**
    * Maintains consistency in terminology and clarity across complex documentation sets.
* **Marketing Operations Leads**
    * Reduces the bottleneck of manual review cycles by providing an automated first-pass quality gate.

---

## Features
- **Automated Tone Analysis**
    Detects inconsistencies in writing style and suggests adjustments to match your defined brand persona.
- **SEO Optimization Engine**
    Analyzes text against search intent and keyword targets to ensure maximum visibility for every piece of content.
- **Grammar and Clarity Guardrails**
    Identifies complex sentences, passive voice, and grammatical errors to improve readability scores.
- **Composio-Powered Integration**
    Seamlessly connects with your CMS or document storage platforms to pull drafts and push refined content.
- **Real-time Compliance Checks**
    Flags non-compliant terminology or prohibited phrases before content reaches the staging environment.

---

## Use Cases
**Content Production Pipeline**
* Automatically scan new blog drafts for brand voice alignment before they reach the editor's queue.
* Flag high-priority articles that require manual human review based on automated sentiment analysis scores.

**SEO & Performance Tuning**
* Audit existing landing page copy to ensure keyword density matches current search engine optimization targets.
* Generate meta-description and title tag recommendations based on the primary content body.

**Documentation & Knowledge Base**
* Standardize terminology across technical help articles to ensure a consistent user experience.
* Identify and simplify overly complex jargon in support documentation to improve customer self-service rates.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Content Quality Guardian template from the solution library.
3. Connect your TextRazor API credentials within the integration settings.
4. Ensure nodes are correctly linked from **Chat Input** to **Agent** to **Composio Toolset** to **Chat Output**.

### 2) Setup the Nodes
* **Chat Input:** Receives the raw text draft or document URL for analysis.
* **Agent:** Processes the text against your brand guidelines and SEO requirements.
* **Composio Toolset:** Executes the TextRazor analysis and retrieves necessary content metadata.
* **Chat Output:** Returns the refined content, suggested edits, and a quality score report.

### 3) Run the Flow
Use the Playground to test your content:
* `Analyze this blog post draft for brand tone consistency and suggest improvements.`
* `Check this article for SEO optimization and provide a list of missing keywords.`
* `Review the following text for clarity and identify any overly complex sentences.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as your automated editor.
* Use a high-reasoning model (e.g., GPT-4o or Claude 3.5) for nuanced tone analysis.
* Provide a system prompt defining your specific brand voice and prohibited vocabulary.
* Set the temperature to 0.2 to ensure consistent, objective editorial feedback.

### 2) Composio Toolset Node
* Provide your TextRazor API key to enable deep linguistic analysis.
* Define the connection scope to include read/write access to your CMS or document repository.

### 3) Tool Availability
* **TextRazor Analysis:** For entity extraction, sentiment analysis, and structural breakdown.
* **CMS Connector:** For fetching drafts and pushing final polished versions.
* **SEO Audit Tool:** For keyword density and meta-data generation.

---

## Related Solutions
* [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) — Refine academic papers and formal research documentation.
* [Accessibility Compliance Monitor](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Ensure digital content meets accessibility standards.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track the efficiency and status of your automated content pipelines.
