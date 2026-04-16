# Basic Prompting (Uplizd) - Streamlined AI interaction and task execution

## Summary
The Basic Prompting solution provides a foundational AI workflow designed to bridge the gap between user intent and intelligent execution. By leveraging the Uplizd engine, this solution enables users to interact with advanced language models to process queries, generate content, and execute tasks via the Composio Toolset, serving as a single source of truth for rapid AI-driven automation and pipeline velocity.

---

## Demo
![Basic Prompting workflow interface showing Chat Input, Agent node, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Basic Prompting workflow interface in Uplizd, demonstrating AI agent task execution, Composio tool integration, and automated chat output.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/cbb036fa-2721-5d52-bc19-21edd5e6dfef)

---

## Category
- **Primary category:** AI Automation
- **Secondary tags:** ai workflow, prompting, composio, automation, productivity, task management, generative ai
- This solution acts as the core framework for deploying modular AI agents that require flexible, prompt-based instruction to perform complex business operations.

---

## Who is this for?
This solution is designed for professionals looking to standardize their AI interactions and automate repetitive cognitive tasks.

- **Operations Managers**
    - Streamline daily administrative workflows by automating routine prompt-based data processing.
- **Product Developers**
    - Rapidly prototype AI-driven features using the Composio Toolset to test integration capabilities.
- **Sales Representatives**
    - Generate personalized outreach and follow-up content with consistent brand voice and logic.
- **Data Analysts**
    - Quickly interpret unstructured datasets by applying standardized prompts to extract actionable insights.

---

## Features
- **Dynamic Prompt Engineering**
    - Utilize advanced LLM instructions to ensure consistent, high-quality outputs across diverse business scenarios.
- **Composio Toolset Integration**
    - Seamlessly connect the agent to external APIs and tools to execute real-time actions based on user prompts.
- **Modular Workflow Design**
    - Easily scale or modify the agent’s logic by adjusting the node-based architecture within the Uplizd builder.
- **Real-Time Execution**
    - Experience low-latency processing that allows for immediate feedback and iterative task refinement.
- **Context-Aware Responses**
    - Maintain conversation history and state to provide relevant, accurate answers tailored to specific user requirements.

---

## Use Cases
**Content Generation**
- Drafting professional emails or internal memos based on brief bullet-point inputs.
- Creating structured summaries from long-form meeting transcripts or documentation.

**Task Automation**
- Triggering external API actions through natural language commands to update CRM records.
- Automating the retrieval of information from third-party services to support decision-making.

**Data Processing**
- Extracting key entities and sentiment from customer feedback logs for reporting.
- Formatting raw data into clean, actionable tables or lists for team review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Basic Prompting template from the solution library.
3. Configure your API credentials for the chosen LLM and Composio.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's natural language request or task description.
- **Agent**: Processes the input using the configured LLM and system instructions.
- **Composio Toolset**: Executes external functions or API calls requested by the agent.
- **Chat Output**: Delivers the final response or confirmation of task completion to the user.

### 3) Run the Flow
Open the Playground and test the flow with these prompts:
- `Summarize the key action items from the following meeting notes: [Paste Text]`
- `Draft a follow-up email to a lead who hasn't responded in 3 days, maintaining a professional tone.`
- `Search for the latest account status in the CRM and provide a summary of recent activity.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node serves as the brain of the operation.
- Set the system prompt to define the agent's persona and primary objectives.
- Enable "Tool Use" to allow the agent to interface with the Composio Toolset.
- Adjust the temperature setting (0.2–0.7) based on whether you require strict factual accuracy or creative generation.

### 2) Composio Toolset Node
- Input your unique Composio API key to authenticate the connection.
- Define the scope of tools available to the agent to ensure secure and controlled access to your integrated platforms.

### 3) Tool Availability
- **CRM Connectors**: Access and update records in platforms like Salesforce or HubSpot.
- **Communication Tools**: Send emails, Slack messages, or WhatsApp notifications.
- **Data Utilities**: Perform search, extraction, and formatting operations on external data sources.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into prospect accounts.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Manage complex multi-step business process automations.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) - Synchronize data across platforms with conflict resolution.
