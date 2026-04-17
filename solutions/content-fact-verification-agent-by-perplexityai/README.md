# Content Fact Verification Agent (Uplizd) - Automated accuracy and source validation for high-trust content

## Summary
The Content Fact Verification Agent is an automated AI workflow designed to streamline the editorial process by cross-referencing claims against authoritative web sources. By leveraging the Perplexity AI search engine via the Composio Toolset, this solution acts as a real-time research assistant, ensuring that marketing copy, academic drafts, and corporate communications maintain a single source of truth, reducing manual fact-checking time and mitigating the risk of misinformation.

---

## Demo
![Content Fact Verification Agent workflow interface showing input, search, and verification nodes](image.png)
**Alt text (SEO-ready):** Content Fact Verification Agent workflow in Uplizd, demonstrating automated AI fact-checking, source validation, and Perplexity AI integration for content accuracy.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/802a46f1-b960-5021-afe2-524f2b78ab35)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** content, fact-checking, research, ai workflow, perplexityai, verification, editorial, composio

This solution bridges the gap between draft creation and publication by automating the verification of factual claims using real-time web intelligence.

---

## Who is this for?
This agent is designed for teams that prioritize accuracy and brand authority in their written output.

*   **Content Marketers**
    *   Ensures all blog posts and whitepapers are backed by verifiable data before hitting the CMS.
*   **Editorial Managers**
    *   Reduces the time spent on manual fact-checking cycles, allowing for faster content velocity.
*   **Corporate Communications Specialists**
    *   Protects brand reputation by validating claims in press releases and public statements.
*   **Academic Researchers**
    *   Provides a rapid secondary verification layer for citations and statistical claims in draft reports.

---

## Features
- **Real-time Web Search**
  Utilizes the Perplexity AI engine to fetch the most current information available on the web.
- **Automated Claim Extraction**
  The agent intelligently parses input text to identify specific factual assertions requiring validation.
- **Source Citation Mapping**
  Automatically links verified claims to their original authoritative URLs for easy review and audit.
- **Confidence Scoring**
  Provides a qualitative assessment of the verification results to help users decide if further manual review is needed.
- **Seamless Composio Integration**
  Connects directly to the Perplexity API via the Composio Toolset for secure, authenticated research queries.

---

## Use Cases
**Editorial Quality Assurance**
*   Verifying statistical claims in long-form marketing reports against current industry data.
*   Checking historical dates and company milestones mentioned in brand storytelling content.

**Corporate Compliance & Risk**
*   Validating external product claims in marketing collateral to ensure they align with technical specifications.
*   Cross-referencing press release statements against official regulatory filings or news reports.

**Academic & Technical Writing**
*   Confirming the accuracy of scientific or technical terminology used in draft documentation.
*   Ensuring that cited studies or research papers are correctly attributed to their primary sources.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to add the workflow to your workspace.
3. Configure your API credentials within the Composio connection settings.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw text content or specific claims to be verified.
*   **Agent**: Processes the text, extracts claims, and formulates research queries.
*   **Composio Toolset**: Executes the Perplexity AI search to retrieve factual data.
*   **Chat Output**: Returns the verified report, including source links and accuracy assessments.

### 3) Run the Flow
Open the Playground and test with these prompts:
* `Verify the following claim: "The global cloud computing market is expected to reach $1.2 trillion by 2027."`
* `Check this paragraph for factual accuracy and provide sources for all data points: [Paste your text here]`
* `Is the statement "Company X launched their flagship product in 2019" factually correct?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent requires a model capable of high-reasoning to distinguish between claims and context.
*   Set the system prompt to prioritize factual accuracy and source citation.
*   Configure the temperature to 0.2 to minimize creative hallucination.
*   Ensure the model has access to the full context of the user's input.

### 2) Composio Toolset Node
*   **API Key**: Provide your Perplexity API key within the Composio dashboard.
*   **Connection Scope**: Ensure the toolset is authorized to perform web searches and retrieve search results.

### 3) Tool Availability
*   **Search Capability**: Allows the agent to query the Perplexity API for real-time web data.
*   **Source Retrieval**: Enables the agent to extract and format URLs for citation.
*   **Data Parsing**: Allows the agent to break down complex paragraphs into individual verifiable statements.

---

## Related Solutions
* [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) - Monitor research citations and academic influence.
* [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) - Improve vocabulary and technical accuracy in writing.
* [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Gather and verify business intelligence on prospect accounts.
