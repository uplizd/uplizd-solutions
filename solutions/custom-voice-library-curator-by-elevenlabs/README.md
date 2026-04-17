# Custom Voice Library Curator (Uplizd) - Streamline AI voice asset management for brand consistency

## Summary
The Custom Voice Library Curator is an automated Uplizd workflow designed to organize, tag, and maintain a centralized repository of synthetic voice assets. By leveraging the ElevenLabs API, this solution enables creative teams and brand managers to ensure consistent audio output across all customer touchpoints, reducing manual asset tracking and ensuring high-fidelity voice compliance.

---

## Demo
![Custom Voice Library Curator workflow showing ElevenLabs integration and voice tagging](image.png)
**Alt text (SEO-ready):** Custom Voice Library Curator dashboard in Uplizd, showing automated ElevenLabs voice asset management, AI voice tagging, and brand consistency workflow.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH6AMKFRQ5P6o/8QAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABCSURBVEjHY2AYBaNgFIyCUUAKwP///z8GAAkgA0YFwP///z8GAAkgA0YFwP///z8GAAkgA0YFwP///z8GAAkgA0YFwAAJAAy2+5b7AAAAAElFTkSuQmCC)](https://uplizd.ai/solutions/d5c1350c-43bd-5a1d-947c-cb861f641a0b)

---

## Category
- **Primary category:** Marketing operations
- **Secondary tags:** elevenlabs, voice-ai, brand-consistency, asset-management, audio-production, composio, ai-workflow, content-automation
- This solution bridges the gap between creative audio production and automated marketing operations by centralizing voice asset control.

---

## Who is this for?
This solution is designed for teams managing high-volume audio content who need to maintain strict brand standards across diverse media channels.

- **Brand Manager**
    - Ensures all synthetic audio assets adhere to established brand voice guidelines and tone-of-voice requirements.
- **Content Producer**
    - Rapidly retrieves approved voice clones for video, podcast, and social media production without searching through disparate folders.
- **Creative Director**
    - Audits the quality and variety of the voice library to ensure the brand remains competitive and distinct.
- **Marketing Operations Lead**
    - Automates the ingestion and categorization of new voice assets, ensuring the library remains organized and accessible to the entire team.

---

## Features
- **Centralized Voice Registry**
    - Maintains a single source of truth for all custom voice clones, complete with metadata and usage rights.
- **Automated Tagging System**
    - Uses AI to automatically categorize voices based on gender, accent, age, and intended use-case (e.g., "Professional," "Casual," "Narrative").
- **ElevenLabs Integration**
    - Direct connection to the ElevenLabs platform via the Composio Toolset to fetch, update, and manage voice IDs in real-time.
- **Brand Compliance Monitoring**
    - Flags voice assets that are nearing expiration or do not meet current quality benchmarks for production.
- **Seamless Asset Retrieval**
    - Provides instant access to voice IDs for developers and creators, accelerating the production pipeline for new audio content.

---

## Use Cases
**Voice Asset Organization**
- Automatically sync new voice clones from ElevenLabs into the master library with descriptive metadata.
- Batch update voice tags when brand guidelines evolve to ensure all assets remain searchable.

**Production Workflow Acceleration**
- Quickly query the library for the "best voice for a 30-second product explainer" to speed up creative iteration.
- Integrate voice selection directly into video editing workflows to reduce time-to-market for new content.

**Brand Governance**
- Audit the library to identify and remove outdated or unauthorized voice clones that no longer fit the brand identity.
- Maintain a history of voice usage to ensure compliance with licensing and usage agreements.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd Solutions gallery.
2. Select the "Custom Voice Library Curator" and click "Import Flow."
3. Connect your ElevenLabs API key within the Composio integration settings.
4. Ensure nodes are correctly linked: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives user queries regarding voice library searches or asset updates.
- **Agent**: Processes natural language requests to identify the correct voice or management action.
- **Composio Toolset**: Executes ElevenLabs API calls to fetch, list, or modify voice data.
- **Chat Output**: Returns the requested voice details or confirms the successful update of the library.

### 3) Run the Flow
Use the Playground to test your voice management capabilities:
- `List all available voices in the library tagged as 'Professional'.`
- `Find the voice ID for the 'Brand-Narrator-V2' clone.`
- `Update the metadata for the latest voice clone to include the tag 'Marketing-Campaign-2024'.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the intelligent interface between your team and the ElevenLabs voice library.
- Use a model with strong instruction-following capabilities (e.g., GPT-4o or Claude 3.5 Sonnet).
- Provide clear instructions on how to parse voice metadata and handle API errors.
- Ensure the agent is configured to prioritize "Brand-Approved" assets during search results.

### 2) Composio Toolset Node
- Requires a valid ElevenLabs API key configured within the Composio dashboard.
- Ensure the connection scope includes `voice:read` and `voice:write` permissions to allow for full library management.

### 3) Tool Availability
- `list_voices`: Retrieves all available voice clones from the ElevenLabs account.
- `get_voice_details`: Fetches specific metadata for a given voice ID.
- `edit_voice_metadata`: Updates tags and descriptions for existing voice assets.

---

## Related Solutions
- [247-customer-support-voice-agent-by-bolna](../247-customer-support-voice-agent-by-bolna/README.md) - Deploy voice-based support automation.
- [247-customer-support-voice-assistant-by-synthflow-ai](../247-customer-support-voice-assistant-by-synthflow-ai/README.md) - Manage voice-driven customer interactions.
- [you-tube-content-performance-optimizer-by-youtube](../you-tube-content-performance-optimizer-by-youtube/README.md) - Optimize video content distribution and performance.
