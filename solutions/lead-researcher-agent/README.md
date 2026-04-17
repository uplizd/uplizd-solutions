# Lead Researcher Agent (Uplizd) - Automated prospect intelligence for high-context outreach

## Summary
The Lead Researcher Agent is an Uplizd workflow that turns a handful of identifiers—company name, domain, role, or territory—into a structured research brief. It aggregates public signals, firmographic context, and recent events so sellers and marketers can personalize outreach without spending hours in tabs and spreadsheets.

---

## Demo
![Lead Researcher Agent workflow showing AI-driven prospect research and brief generation](image.png)
**Alt text (SEO-ready):** Uplizd Lead Researcher Agent workflow for automated B2B lead research, qualification context, and outreach-ready intelligence briefs.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/marketplace/lead-researcher-agent)

---

## Category
**Sales automation**
- **Secondary tags:** `lead research`, `prospect intelligence`, `b2b sales`, `outreach`, `qualification`, `composio`, `ai workflow`, `sales enablement`
This solution compresses manual desk research into a repeatable agent flow so every lead gets consistent depth and sourcing discipline.

---

## Who is this for?
Built for teams that need fast, defensible context before the first meaningful touch.

- **Sales Development Representative**
    - Produces concise briefs for outbound sequences with hooks tied to recent company or role-level signals.
- **Account Executive**
    - Prepares for discovery by mapping stakeholders, priorities, and likely objections from structured research output.
- **Revenue Operations**
    - Standardizes what “good research” looks like across pods and reduces rework from shallow personalization.
- **Founder-Led Sales**
    - Keeps research lightweight while still sounding specific and credible on early-stage calls.

---

## Features
- **Structured Research Briefs**
    - Outputs sections such as company overview, recent signals, persona angles, and suggested talk tracks.
- **Signal-Oriented Synthesis**
    - Prioritizes timely triggers—hiring, product launches, funding, leadership changes—when available from connected tools.
- **Source-Aware Responses**
    - Instructs the agent to attribute claims and avoid inventing facts when data is missing.
- **Composio-Ready Tooling**
    - Connects your approved data providers through the Composio toolset so the agent pulls live context instead of stale guesses.
- **Repeatable Prompting**
    - Encodes your team’s research checklist into the agent system instructions for consistent quality.

---

## Use Cases
**Outbound personalization**
- Draft opener lines grounded in verified company context rather than generic templates.

**Territory and account planning**
- Batch-generate “why now” notes for accounts entering a new segment or region.

**Inbound follow-up**
- Enrich inbound leads with firmographic and timing context before routing to sales.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Open the Uplizd marketplace and import the Lead Researcher Agent template into your workspace.
2. Connect the integrations your organization allows (for example, company and news lookup tools) in the Composio toolset configuration.
3. Verify the graph runs from **Chat Input** through **Agent** and **Composio Toolset** to **Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Accepts lead identifiers (domain, company name, persona, region) and optional research goals.
- **Agent**: Plans the research steps, calls tools, and writes the final brief in your preferred format.
- **Composio Toolset**: Executes provider-backed lookups you enable for this workspace.
- **Chat Output**: Returns the brief with clear headings and citations where the tools supplied evidence.

### 3) Run the Flow
Try prompts like:
- `Research [company.com] for a VP Marketing outbound sequence; include 3 hooks and 2 risks to avoid.`
- `Summarize what changed at [Company] in the last 90 days that matters for a [Product] sale.`
- `Build a stakeholder map for [Company] focused on data infrastructure buyers.`

---

## Configuration
### 1) Language Model (Agent Node)
- Prefer a model with strong reasoning and long-context support for multi-source synthesis.
- Set system instructions to enforce citations, date awareness, and a professional sales tone.
- Define the output schema (headings, bullets, max length) to match your CRM or sequencing tool.

### 2) Composio Toolset Node
- Enable only the connectors approved by your security and data governance policies.
- Use read-only scopes where possible and rotate keys on a regular cadence.

### 3) Quality Safeguards
- Add explicit rules: if a tool returns nothing, the agent should say so instead of fabricating detail.
- Log or store briefs according to your retention policy and regional privacy requirements.

---

## Related Solutions
- [Account Research Assistant](../account-research-assistant-by-zoominfo/README.md) - Deep B2B account intelligence and sales preparation.
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Focused account-level research workflows.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrichment-led account context for outreach.
