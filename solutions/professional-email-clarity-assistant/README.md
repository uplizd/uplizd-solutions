
# Professional Email Clarity Assistant (Uplizd) - Refine Business Communication

## Summary
An intelligent Uplizd AI workflow designed to help professionals elevate their business communication. It analyzes email drafts for ambiguity, validates word choices using real-time dictionary data, and provides polished, high-clarity alternatives.

---

## Demo

![Professional Email Clarity Assistant flow refining an email draft](../image.png)

**Alt text:** Uplizd Professional Email Clarity Assistant workflow featuring a structured agent that analyzes, validates, and polishes email drafts using a real-time dictionary tool.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/8ddddfe3-73dc-4e33-a8f4-b1f25f39ce4e)

---
## Who is this for?
This workflow is ideal for anyone whose professional success depends on clear, unambiguous written communication:

- **Executives & Managers**
    - Ensure your directives and announcements are precise and professional.

- **Client-Facing Teams**
    - Avoid miscommunication with clients by using contextually appropriate terminology.

- **Non-Native English Speakers**
    - Gain confidence in choosing the most accurate words for professional business settings.

- **HR & Internal Communications**
    - Craft sensitive internal messages that are clear, empathetic, and professional.

---

## Features

- **Semantic Ambiguity Analysis**  
  Identifies words or phrases that might be interpreted differently in a professional context.

- **Dictionary-Backed Validation**  
  Integrates directly with the Dictionary API to verify the precise meaning and context of flagged words.

- **Contextual Professional Suggestions**  
  Recommends alternatives that match the intended professional tone and specific industry audience.

- **Clarity Scoring (1-10)**  
  Provides a metrics-driven comparison between the original draft and the improved version.

- **Automated Polishing & Final Versioning**  
  Generates a complete, ready-to-send email that incorporates all improvements while maintaining the original intent.

---

## Use Cases

- **Clarifying Technical Reports**
  - Simplify complex jargon for non-technical stakeholders without losing critical meaning.

- **Softening Sensitive Requests**
  - Adjust word choices to turn a potentially blunt request into a collaborative, professional prompt.

- **Standardizing Corporate Tone**
  - Ensure all team communication adheres to a consistent level of professional clarity.

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all **4 nodes** are connected correctly:
   - **Chat Input**
   - **Agent**
   - **DictionaryApi: GET_WORD_DEFINITION**
   - **Chat Output**

### 2) Setup the Nodes
Verify the workflow configuration:

- **Chat Input** → receives your draft email text.
- **Agent** → handles the 5-step analysis (Analyze, Validate, Suggest, Score, Polish).
- **DictionaryApi** → provides the tool for the agent to look up precise definitions.
- **Chat Output** → presents the improved email and clarity report.

### 3) Run the Flow
1. Click **Playground** to open Chat Interface.
2. Paste your email draft and ask for a review:
   - *"Please review this email for a new project proposal."*
   - *"Is this word choice too aggressive for a manager?"*
   - *"Make this draft more concise and professional."*

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is pre-configured with a specific "Professional Email Clarity Assistant" system prompt.

Recommended settings:
- **Model**: GPT-4o-mini or Claude-3.5-Sonnet for best semantic analysis.
- **System Prompt**: Ensure the instructions include the Analyze-Validate-Suggest-Score-Polish workflow.

### 2) Dictionary Connection
Requires your **Composio API Key** to connect to the Dictionary API tool. This allows the agent to fetch real-time definitions to validate its suggestions.

### 3) Tool Availability
The agent leverages the following action via Composio:
- **DICTIONARY_API_GET_WORD_DEFINITION_V2**: Used by the agent to verify semantics before suggesting alternatives.

---

## Related Solutions

* **[Event Registration Email Checker](../event-registration-email-checker/readme.md)**  
  Verify and clean your recipient lists before sending out your professionally refined emails.

* **[Event Attendee Manager](../event-attendee-manager/README.md)**  
  Manage attendee segments and automate the delivery of your professional email content.

* **[Research Insight Synthesizer](../research-insight-synthesizer/README.md)**  
  Communicate complex research findings clearly and professionally using our clarity assistant.

* **[Language Translation Agent](../language-translation-agent/README.md)**  
  Translate your professional emails across multiple languages while maintaining tone.
