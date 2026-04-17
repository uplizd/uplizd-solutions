# Hybrid Search RAG (Uplizd) - Intelligent Information Retrieval with Vector and Keyword Synergy

## Summary
The Hybrid Search RAG (Retrieval-Augmented Generation) solution leverages Uplizd to combine the semantic depth of vector embeddings with the precision of keyword-based search. By integrating advanced retrieval techniques, this workflow ensures that AI agents provide highly accurate, context-aware responses, significantly reducing hallucinations and improving information retrieval velocity for enterprise knowledge bases.

---

## Demo
![Hybrid Search RAG workflow diagram showing vector and keyword retrieval integration](image.png)
**Alt text (SEO-ready):** Hybrid Search RAG workflow diagram showing vector and keyword retrieval integration within the Uplizd AI platform for enhanced data accuracy.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,...)](https://uplizd.ai/solutions/e15ec3d1-7250-5c28-beef-57137b64e983)

---

## Category
- **Primary category:** Data Integration
- **Secondary tags:** rag, hybrid search, vector database, semantic search, information retrieval, ai workflow, composio, knowledge management
- This solution bridges the gap between unstructured data and precise query results by unifying vector-based semantic understanding with traditional keyword indexing.

---

## Who is this for?
This solution is designed for technical teams and knowledge managers who need to extract precise insights from vast, complex datasets.

- **Knowledge Manager**
    - Ensures that internal documentation and wikis are searchable with high recall and precision.
- **AI Engineer**
    - Implements robust RAG pipelines that minimize model hallucinations through hybrid retrieval.
- **Data Architect**
    - Optimizes database query performance by balancing semantic similarity and exact keyword matching.
- **Operations Lead**
    - Accelerates team access to critical business information, reducing time spent on manual research.

---

## Features
- **Dual-Engine Retrieval**
    - Combines vector embeddings for semantic intent and BM25/keyword search for exact terminology matching.
- **Context-Aware Synthesis**
    - Uses the Agent node to synthesize retrieved documents into concise, human-readable answers.
- **Composio Toolset Integration**
    - Seamlessly connects to vector databases and search APIs to execute complex retrieval queries in real-time.
- **Hallucination Mitigation**
    - Grounds AI responses in verified retrieved chunks, ensuring high-fidelity output based on source data.
- **Scalable Indexing**
    - Supports dynamic updates to knowledge bases, ensuring the agent always has access to the latest information.

---

## Use Cases
**Enterprise Knowledge Base**
- Querying internal technical documentation for specific error codes or configuration settings.
- Retrieving policy documents based on natural language questions from HR or legal teams.

**Customer Support Automation**
- Finding exact product manual references based on vague customer descriptions.
- Matching support tickets to historical resolution logs using both intent and specific product keywords.

**Research and Development**
- Identifying relevant patent or research paper excerpts using a mix of thematic and technical terminology.
- Summarizing findings from large document repositories based on complex, multi-faceted user queries.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Hybrid Search RAG template from the solution library.
3. Configure your API keys for the vector database and LLM providers.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the user's natural language query.
- **Agent**: Processes the query and determines the optimal retrieval strategy.
- **Composio Toolset**: Executes the hybrid search across vector and keyword indices.
- **Chat Output**: Delivers the synthesized, grounded answer to the user.

### 3) Run the Flow
Use the Playground to test the retrieval logic:
- `Find the technical specifications for the X-200 model using keyword and semantic search.`
- `What are the company policies regarding remote work for the engineering department?`
- `Retrieve all documentation related to API authentication errors from the last quarter.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for retrieval and synthesis.
- Set the system prompt to prioritize source-based answering.
- Configure the temperature to a low setting (e.g., 0.2) for maximum factual accuracy.
- Enable tool-calling capabilities to allow the agent to trigger search functions.

### 2) Composio Toolset Node
- Provide the necessary API keys for your vector database (e.g., Pinecone, Weaviate).
- Define the scope to include both semantic search and keyword search tool definitions.

### 3) Tool Availability
- **Vector Search Tool**: Performs similarity matching on document embeddings.
- **Keyword Search Tool**: Performs exact match indexing for specific terms and IDs.
- **Synthesis Tool**: Formats retrieved data into a coherent narrative.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automates gathering deep intelligence on target accounts.
- [Account Intelligence Reporter](../account-intelligence-reporter-by-leadfeeder/README.md) - Generates comprehensive reports on account activity and intent.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Streamlines complex operational workflows across platforms.
