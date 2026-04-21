# Tech Talent Scout (Uplizd) - Automated Hacker News talent sourcing and engagement

## Summary
The Tech Talent Scout (Uplizd) workflow automates the discovery and evaluation of high-quality engineering talent by monitoring Hacker News activity. By leveraging AI to analyze technical discussions and contributions, this solution enables recruiters and hiring managers to identify passive candidates who demonstrate expertise in specific technologies, significantly reducing sourcing time and increasing the quality of outreach.

---

## Demo
![Tech Talent Scout workflow dashboard showing Hacker News integration and candidate filtering](image.png)
**Alt text (SEO-ready):** Tech Talent Scout workflow on Uplizd, demonstrating automated Hacker News candidate sourcing, technical profile analysis, and recruitment pipeline integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c3351e0f-11b4-542e-8096-535203225614)

---

## Category
**Primary category:** Recruiting
**Secondary tags:** talent acquisition, hacker news, sourcing, engineering recruitment, ai workflow, composio, passive candidates, tech hiring.
This solution bridges the gap between public technical discourse on Hacker News and professional talent pipelines, streamlining the identification of top-tier engineering talent.

---

## Who is this for?
This solution is designed for talent acquisition teams and technical leaders who need to find high-signal candidates in a crowded market.

* **Technical Recruiter**
    * Quickly identify candidates who demonstrate deep knowledge in niche programming languages or frameworks.
* **Engineering Manager**
    * Source candidates who contribute meaningfully to technical discussions, ensuring a high cultural and technical fit.
* **Head of Talent**
    * Build a proactive sourcing engine that identifies talent before they hit the open job market.
* **Startup Founder**
    * Efficiently discover early-stage engineers who are passionate about specific tech stacks and community-driven development.

---

## Features
- **Real-time HN Monitoring**
  Continuously scans Hacker News threads for specific keywords, technologies, or project mentions to find active contributors.
- **AI-Powered Profile Analysis**
  Uses the Agent node to evaluate the quality, tone, and technical depth of user comments and submissions.
- **Composio Toolset Integration**
  Seamlessly connects with recruitment CRMs and communication platforms to log identified candidates for follow-up.
- **Automated Outreach Drafting**
  Generates personalized engagement messages based on the specific technical contributions discovered in the candidate's history.
- **Candidate Scoring Engine**
  Ranks prospects based on technical relevance and engagement frequency, ensuring recruiters focus on the most promising leads.

---

## Use Cases
**Proactive Technical Sourcing**
* Identify engineers discussing specific architectural patterns or languages like Rust or Go in real-time.
* Filter candidates based on the complexity and community reception of their technical contributions.

**Engineering Pipeline Enrichment**
* Automatically push qualified candidate profiles from Hacker News directly into your ATS or CRM.
* Create a database of "passive" candidates who are not currently applying but demonstrate high technical proficiency.

**Personalized Candidate Engagement**
* Draft tailored outreach emails that reference specific technical insights shared by the candidate on Hacker News.
* Maintain a consistent follow-up cadence by tracking engagement status within the Uplizd workflow.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import" to load the pre-configured workflow into your Uplizd workspace.
3. Connect your required API credentials for the Hacker News API and your target CRM.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Define the target technology or keyword (e.g., "Distributed Systems").
* **Agent**: Processes search results and evaluates candidate technical depth.
* **Composio Toolset**: Executes actions to fetch HN data and update your CRM.
* **Chat Output**: Displays the list of identified candidates and suggested outreach templates.

### 3) Run the Flow
Open the Playground and test with these prompts:
* `Find engineers discussing React performance optimization in the last 48 hours.`
* `Analyze the last 10 comments from [Username] and summarize their technical expertise.`
* `Identify top contributors in the 'Who is hiring' thread interested in backend engineering.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the primary filter for technical relevance and sentiment analysis.
* **Instruction Pattern:** Focus on identifying technical depth rather than just keyword frequency.
* **Instruction Pattern:** Prioritize candidates who provide constructive, high-quality technical feedback.
* **Instruction Pattern:** Maintain a professional and encouraging tone for all generated outreach drafts.

### 2) Composio Toolset Node
Requires an active connection to the Hacker News API and your chosen CRM (e.g., Greenhouse, Lever, or Salesforce) via the Composio platform to enable data synchronization.

### 3) Tool Availability
* **HN Search Tool**: Queries Hacker News threads and comments for specific technical keywords.
* **Profile Scraper**: Extracts user history and comment metadata for analysis.
* **CRM Connector**: Performs write operations to save candidate profiles and engagement notes.

---

## Related Solutions
* [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich candidate profiles with verified contact information.
* [Account Research Agent](../account-research-agent-by-onepage/README.md) — Deep-dive research into company technical stacks and hiring needs.
* [Workforce Onboarding Automator](../workforce-onboarding-automator/README.md) — Streamline the transition from candidate identification to new hire setup.
