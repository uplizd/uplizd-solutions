# AI Agent Starter Kit: Weather & Web Scraping (Uplizd) - Build your first autonomous agent workflow

## Summary
The AI Agent Starter Kit provides a foundational framework for developers to build and deploy autonomous agents that combine real-time weather data retrieval with live web scraping capabilities. By leveraging the Uplizd orchestration engine and the Composio Toolset, this solution enables users to create intelligent workflows that fetch external information and process it into actionable insights, serving as the perfect entry point for mastering AI-driven automation and pipeline velocity.

---

## Demo
![AI Agent Starter Kit workflow showing Chat Input connected to an Agent node with Weather and Web Scraping tools](image.png)
**Alt text (SEO-ready):** Uplizd AI Agent Starter Kit workflow demonstrating weather API integration and web scraping automation for intelligent data retrieval.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9309fda7-d958-5718-b9df-fb337c69c886)

---

## Category
- **Primary category:** AI Development
- **Secondary tags:** ai agent, web scraping, weather api, automation, composio, starter kit, workflow builder, data extraction
- This solution serves as a foundational template for developers looking to integrate external data sources into their custom AI-driven automation workflows.

---

## Who is this for?
This starter kit is designed for builders and technical professionals looking to accelerate their AI implementation journey:

- **Junior Developers**
    - Gain hands-on experience connecting LLMs to real-world data sources through standardized toolsets.
- **Automation Engineers**
    - Rapidly prototype data-fetching workflows that combine multiple external APIs into a single agentic process.
- **Product Managers**
    - Validate the feasibility of AI-driven feature sets by building functional proof-of-concepts in minutes.
- **Technical Founders**
    - Reduce time-to-market for internal tools by leveraging pre-configured agentic patterns for web research.

---

## Features
- **Weather Integration**
    - Seamlessly pull real-time meteorological data to inform agent decision-making processes.
- **Web Scraping Capabilities**
    - Extract structured content from live websites to feed context-aware responses into your agent.
- **Composio Toolset Connectivity**
    - Utilize pre-built tool connectors to manage authentication and data flow between the agent and external services.
- **Modular Workflow Design**
    - Easily swap or extend nodes to customize the agent's logic for specific business requirements.
- **Real-time Execution**
    - Experience low-latency processing as the agent orchestrates tool calls and generates human-like responses.

---

## Use Cases
**Market Research Automation**
- Automatically scrape industry news sites to gather competitive intelligence for weekly reports.
- Combine local weather data with retail traffic trends to predict store performance.

**Personalized Assistant Development**
- Build a daily briefing agent that summarizes weather forecasts and relevant web-scraped articles.
- Create travel planning bots that fetch destination weather and attraction details in real-time.

**Data Enrichment Pipelines**
- Scrape contact information from company websites to enrich CRM profiles automatically.
- Integrate weather-based triggers into logistics workflows to update delivery schedules dynamically.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Starter Kit template using the provided JSON configuration.
3. Authenticate your required API keys within the Composio Toolset settings.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's natural language query.
- **Agent**: Processes the intent and determines which tools to invoke.
- **Composio Toolset**: Executes the specific weather or scraping functions requested.
- **Chat Output**: Delivers the synthesized information back to the user.

### 3) Run the Flow
Open the Playground and try these prompts:
- `What is the weather in San Francisco today and how does it compare to New York?`
- `Scrape the latest headlines from the tech news section of the provided URL.`
- `Find the current temperature in London and summarize the top three news stories from a major news site.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent node acts as the brain of the operation, interpreting user intent and managing tool execution.
- Set the system prompt to define the agent's persona as a "Research Assistant."
- Enable "Tool Calling" mode to allow the agent to interact with the Composio Toolset.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for optimal tool selection accuracy.

### 2) Composio Toolset Node
- Input your unique Composio API key to authorize the agent's access to external tools.
- Define the connection scope to include only the specific weather and scraping tools required for your workflow.

### 3) Tool Availability
- **Weather API**: Real-time temperature, humidity, and forecast data.
- **Web Scraper**: HTML parsing, text extraction, and metadata retrieval.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research on target accounts.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamline complex business processes with agentic logic.
- [YouTube Insight Agent](../youtube-insight-agent-by/README.md) - Extract and analyze data from video content.
