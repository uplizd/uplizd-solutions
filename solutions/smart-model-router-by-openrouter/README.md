# Smart Model Router (Uplizd) - Optimize AI performance and cost by routing tasks to the best-fit model

## Summary
The Smart Model Router is an intelligent Uplizd workflow that dynamically evaluates incoming prompts to determine the most cost-effective and performant AI model for the task. By analyzing complexity and intent, the workflow routes requests between high-capability models for complex reasoning and lightweight models for simple queries, ensuring optimal pipeline velocity and reduced operational expenditure.

---

## Demo
![Smart Model Router workflow diagram showing prompt analysis and dynamic routing to OpenRouter models](image.png)
**Alt text (SEO-ready):** Smart Model Router workflow in Uplizd, demonstrating dynamic AI model selection, OpenRouter integration, and automated task routing.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-51e1762e--5999--5a3d--833d--024e9c3c52ac-blue)](https://uplizd.ai/solutions/51e1762e-5999-5a3d-833d-024e9c3c52ac)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** ai workflow, openrouter, model routing, cost optimization, llm, automation, composio, prompt engineering
- This solution enables teams to standardize AI infrastructure by programmatically selecting the best model for every specific user request.

---

## Who is this for?
This workflow is designed for technical teams looking to scale their AI operations while maintaining strict control over performance and API costs.

- **AI Engineers**
    - Automate model selection logic to prevent over-spending on simple tasks.
- **Product Managers**
    - Ensure consistent user experience by matching model capability to feature requirements.
- **Operations Leads**
    - Monitor and optimize total token consumption across multiple LLM providers.
- **DevOps Engineers**
    - Implement a centralized routing layer that simplifies model updates and provider switching.

---

## Features
- **Dynamic Complexity Analysis**
    - Automatically evaluates the intent and depth of user prompts to categorize task difficulty.
- **OpenRouter Integration**
    - Seamlessly connects to the OpenRouter API to access a unified interface for hundreds of LLM endpoints.
- **Cost-Optimized Routing**
    - Routes routine queries to high-speed, low-cost models while reserving premium models for complex reasoning.
- **Real-Time Latency Management**
    - Reduces overall system response time by avoiding unnecessary calls to heavy, high-latency models.
- **Centralized Routing Logic**
    - Allows for rapid updates to routing rules without needing to modify the underlying application code.

---

## Use Cases
**Cost Management**
- Route simple status checks or greeting prompts to low-cost models to save on token usage.
- Implement monthly budget caps by forcing all non-critical traffic through smaller, efficient models.

**Performance Optimization**
- Direct complex coding or data analysis tasks to high-parameter models to ensure accuracy.
- Bypass heavy models for simple summarization tasks to improve end-user perceived latency.

**Model A/B Testing**
- Split traffic between different model versions to compare performance metrics in a production environment.
- Gradually roll out new model releases by routing a percentage of traffic to the latest versions.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Smart Model Router template file provided in this repository.
3. Connect your OpenRouter API credentials within the environment settings.
4. Ensure nodes are correctly linked from the Chat Input to the Agent and finally to the Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's prompt and passes it to the routing agent.
- **Agent**: Analyzes the prompt complexity and selects the optimal model endpoint.
- **Composio Toolset**: Executes the routing request via the OpenRouter API.
- **Chat Output**: Returns the generated response from the selected model to the user.

### 3) Run the Flow
Use the Uplizd Playground to test the routing logic with these prompts:
- `Summarize this short email in one sentence.`
- `Write a complex Python script to scrape a website and handle pagination.`
- `What is the capital of France?`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making brain of the router.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for the Agent to ensure accurate routing decisions.
- Instruction: "Analyze the user prompt for complexity. If the task is simple, route to a fast model. If complex, route to a high-reasoning model."
- Ensure the agent has access to the tool definitions required to trigger the OpenRouter API.

### 2) Composio Toolset Node
- Provide your OpenRouter API key in the Composio configuration.
- Set the connection scope to allow the agent to perform model inference calls.

### 3) Tool Availability
- **Model Inference**: Capability to send prompts to specific OpenRouter endpoints.
- **Complexity Classifier**: Logic to determine if a prompt requires high-reasoning capabilities.
- **Fallback Handler**: Mechanism to retry requests if a specific model endpoint is unavailable.

---

## Related Solutions
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline cross-platform task execution.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive intelligence gathering for sales accounts.
- [Adaptive Learning Curriculum Builder](../adaptive-learning-curriculum-builder-by-perplexityai/README.md) - Create personalized learning paths using AI.
