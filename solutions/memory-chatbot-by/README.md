# Memory Chatbot (Uplizd) - Intelligent context-aware conversational AI

## Summary
The Memory Chatbot is an advanced Uplizd workflow designed to transform standard AI interactions into persistent, context-aware conversations. By leveraging integrated memory storage, this solution allows the agent to recall previous user inputs and session history, ensuring a seamless, personalized experience that maintains continuity across long-running interactions.

---

## Demo
![Memory Chatbot workflow interface showing context retrieval and persistent conversation history](image.png)
**Alt text (SEO-ready):** Memory Chatbot (Uplizd) workflow interface showing context retrieval, persistent conversation history, and AI memory integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/12bc6566-15e7-58de-bda4-1fd2725893f7)

---

## Category
**Primary category:** AI Workflow Automation
**Secondary tags:** memory, chatbot, context-aware, conversational ai, state management, composio, persistent chat, user experience.
This solution bridges the gap between stateless LLM requests and stateful, human-like dialogue management.

---

## Who is this for?
This solution is designed for professionals who need to maintain continuity in AI-driven interactions without losing track of previous user data.

*   **Customer Support Leads**
    *   Maintain historical context of user issues to provide faster, more accurate resolutions without asking customers to repeat themselves.
*   **Personal Productivity Coaches**
    *   Track long-term user goals and progress notes across multiple sessions to provide highly tailored coaching advice.
*   **Sales Development Representatives**
    *   Recall specific prospect preferences and past objections discussed in previous meetings to refine follow-up strategies.
*   **Technical Product Managers**
    *   Manage complex project requirements and feature requests by keeping a persistent log of stakeholder feedback throughout the development lifecycle.

---

## Features
- **Persistent Session Memory**
    Automatically stores and retrieves conversation history, allowing the agent to reference past interactions as if they occurred moments ago.
- **Contextual Awareness**
    Enables the LLM to understand the "why" and "how" behind user requests by analyzing the full thread of previous messages.
- **Composio Toolset Integration**
    Seamlessly connects the agent to external databases and memory stores to ensure data is retrieved and updated in real-time.
- **Dynamic Response Personalization**
    Uses stored user preferences to tailor tone, style, and content, resulting in a more human-like and engaging user experience.
- **Scalable State Management**
    Handles complex, multi-turn dialogues efficiently, ensuring the agent remains focused even during extended, information-heavy sessions.

---

## Use Cases
**Customer Relationship Management**
*   Summarizing past support tickets to identify recurring pain points for a specific client.
*   Updating user profiles based on new information provided during a live chat session.

**Personalized Coaching & Mentorship**
*   Tracking a user's learning milestones over several weeks to suggest relevant resources.
*   Referencing past goals to provide encouragement and accountability in daily check-ins.

**Project & Task Coordination**
*   Maintaining a running list of action items discussed during brainstorming sessions.
*   Recalling specific constraints or requirements mentioned by stakeholders in earlier project phases.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Memory Chatbot template from the solution library.
3. Configure your environment variables for the LLM and memory storage provider.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the user's message and current session ID.
*   **Agent**: Processes the input, queries the memory store, and generates a context-aware response.
*   **Composio Toolset**: Executes the retrieval and storage operations to maintain conversation state.
*   **Chat Output**: Delivers the final, memory-enriched response back to the user.

### 3) Run the Flow
Open the Playground and test the agent's memory capabilities:
*   `"My name is Alex and I prefer a professional tone in all our communications."`
*   `"What is my name and how should you be talking to me?"`
*   `"Based on our previous chat, can you summarize the project requirements we discussed?"`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence, managing the flow of information between the user and the memory store.
*   **Instruction Pattern**: Always check the memory store before answering factual questions about the user.
*   **Instruction Pattern**: Summarize and store key user preferences explicitly identified during the conversation.
*   **Instruction Pattern**: Maintain a neutral, helpful tone while prioritizing the accuracy of retrieved historical data.

### 2) Composio Toolset Node
Requires a valid API key and connection scope to your chosen memory storage service (e.g., Pinecone, Redis, or a CRM-based storage). Ensure the agent has read/write permissions for the specific session index.

### 3) Tool Availability
*   **Memory Retrieval**: Fetch relevant past messages based on semantic similarity.
*   **Memory Update**: Append new information and user preferences to the session log.
*   **Session Management**: Initialize or clear conversation contexts as required by the user.

---

## Related Solutions
*   [247 Customer Support Assistant](../247-customer-support-assistant-by-ai-ml-api/README.md) — Automate support inquiries with 24/7 availability.
*   [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Keep your customer data synchronized across multiple platforms.
*   [Deal Pipeline Manager](../deal-pipeline-manager/README.md) — Track and optimize your sales pipeline stages effectively.
