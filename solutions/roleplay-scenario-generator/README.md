
# Roleplay Scenario Generator (Chatfai) - Immersive Character Interaction

## Summary
An Uplizd AI workflow designed for creative writers, educators, and trainers to generate complex, dynamic roleplay scenarios. By integrating with character-based AI systems, it creates immersive environments where users can interact with personas that maintain consistent personalities, memories, and emotional depth—perfect for narrative prototyping or soft-skills training.

---

## Demo

![Uplizd Roleplay Scenario Generator flow creating dynamic dialogue and character interactions](../image.png)

**Alt text:** Uplizd Roleplay Scenario Generator integrating Chatfai toolsets to automate character creation and immersive scenario branching.

---
## 🚀 Run on Uplizd

[![Run on Uplizd](https://img.shields.io/badge/RUN%20ON%20UPLIZD-blue?style=for-the-badge&logo=lightning)](https://uplizd.ai/solutions/6ef551d8-4da4-5df8-b2fd-aac8c0163fae/)

---
## Who is this for?
This workflow is built for narrative designers and trainers looking to scale realistic human-AI interactions:

- **Creative Writers & Narrative Designers**
    - Quickly prototype character dialogue and story branches for novels, scripts, or games.

- **Sales & Customer Support Trainers**
    - Generate realistic "difficult customer" simulations for staff to practice de-escalation and negotiation.

- **Game Developers**
    - Create dynamic quest-giving and world-building dialogue that adapts to player choice.

- **Community Managers**
    - Build engaging, personality-driven bots for community platforms that provide more than just static responses.

---

## Features

- **Personality-Driven Scenarios**  
  Uses `CHATFAI_CREATE_CHARACTER` and `CHATFAI_LIST_CHARACTERS` to build scenarios around specific behaviors, traits, and backstories.

- **Dynamic Memory Management**  
  Maintains context and past interactions via `CHATFAI_GET_CHARACTER_CONVERSATION` to ensure continuity across long-form sessions.

- **Multi-Persona Orchestration**  
  Engineered to coordinate interactions between multiple AI characters within a single narrative scene.

- **Scenario Branching Logic**  
  Automatically generates multiple path options and outcomes based on user inputs or character motivations.

- **Emotional Tone Adaptation**  
  Intelligently adjusts character responses based on the perceived sentiment and urgency of the user's interaction.

- **Narrative Guardrails**  
  Ensures characters stay "in character" and adhere to the established rules of the fictional or professional setting.

---

## Use Cases

- **Soft-Skills & Corporate Training**
  - "Roleplay as a skeptical enterprise lead who is concerned about data privacy during a sales pitch."
  - "Simulate a performance review between a manager and an underperforming employee to practice feedback delivery."

- **Narrative Prototyping**
  - "Generate an interactive scene between a wise mentor and a reckless apprentice in a high-fantasy setting."
  - "Prototype a detective noir investigation where characters hide clues based on their trustworthiness."

- **Conflict Resolution Practice**
  - "Simulate a tenant-landlord dispute to help local mediators practice de-escalation techniques in a controlled environment."

---
## Quick Start

### 1) Import the Flow into Uplizd
1. Click the **Run on Uplizd** CTA button above.
2. On Uplizd, click **Try out**.
3. Create a new workspace or open an existing workspace.
4. Ensure all nodes are connected correctly:
   - **Chat Input**
   - **Chatfai - CHATFAI_LIST_CHARACTERS**
   - **Chatfai - CHATFAI_CREATE_CHARACTER**
   - **Chatfai - CHATFAI_GET_CHARACTER_CONVERSATION**
   - **Agent**
   - **Chat Output**

### 2) Setup the Nodes
Verify the workflow structure:

- **Chat Input** → receives the scenario prompt, character names, or training objective.
- **Agent** → coordinates the narrative flow (Scenario Setup -> Character Selection -> Memory Retrieval -> Dialogue Generation -> Sentiment Check).
- **Chatfai Toolset** → Provides the specialized infrastructure for persona management and conversation memory.
- **Chat Output** → presents the character's response and any system-generated narrative cues.

### 3) Run the Flow
1. Click **Playground** to open Chat Interface.
2. Enter a request such as:
   - `"Start a roleplay session with a landlord. I am a tenant complaining about a broken heater."`
   - `"Generate a dialogue scene where a merchant tries to sell a cursed item to a wary traveler."`
   - `"Setup a training scenario for a Junior Sales rep dealing with a price-sensitive prospect."`

---

## Configuration

### 1) Language Model (Agent Node)
The **Agent** node is pre-configured to prioritize narrative consistency and character depth.

Recommended instruction pattern:
- Never break character unless explicitly asked for a meta-commentary.
- Maintain a consistent tone and vocabulary appropriate for the character's background.
- Focus on emotional intelligence and realistic human reactions.

### 2) Chatfai Toolset Nodes
Requires your **Composio API Key** and a connection to your **Chatfai** account where your character presets are stored.

### 3) Tool Availability
The agent can call tools for:
- Discovering existing character personas
- Creating new characters on the fly
- Retrieving and updating conversation history

---

## Related Solutions

* **[Business Proposal Generator](../business-proposal-generator/README.md)**  
  Transform client briefs and raw project data into professional business proposals.

* **[Invoice Processing Agent](../invoice-processing-agent/README.md)**  
  Automate the extraction and routing of invoice data from emails and PDFs.

* **[Compliance Document Processor](../compliance-document-processor/README.md)**  
  Automate multilingual compliance document processing and entity matching.

* **[Meeting Room Coordinator](../meeting-room-coordinator/README.md)**  
  Automate office scheduling and resolve meeting room conflicts directly through Slack.
