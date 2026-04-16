# AI Talent Matching Engine (Uplizd) - Automated candidate-to-job profile alignment

## Summary
The AI Talent Matching Engine (Uplizd) leverages intelligent agent workflows to bridge the gap between candidate resumes and open job descriptions. By automating the extraction of skills, experience, and qualifications, this solution enables HR teams and recruiters to drastically reduce time-to-hire, ensure high-quality candidate pipelines, and maintain a single source of truth for talent acquisition data.

---

## Demo
![AI Talent Matching Engine workflow diagram showing candidate data ingestion, skill extraction, and Workday profile matching](image.png)
**Alt text (SEO-ready):** AI Talent Matching Engine by Uplizd, automated candidate screening, Workday integration, recruitment workflow, talent acquisition automation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://uplizd.ai/assets/run-on-uplizd.svg)](https://uplizd.ai/solutions/d513aca8-a4b4-5903-866f-b9a586d027a9)

---

## Category
- **Primary category:** HR Operations
- **Secondary tags:** recruitment, talent acquisition, workday, candidate matching, ai workflow, hiring automation, composio, skill parsing
- This solution streamlines the talent acquisition lifecycle by integrating AI-driven analysis with core HR platforms to optimize hiring velocity.

---

## Who is this for?
This solution is designed for talent acquisition teams and HR professionals looking to modernize their hiring pipeline.

- **Technical Recruiter**
    - Automates the initial screening of high-volume technical applications to identify top-tier talent faster.
- **HR Operations Manager**
    - Ensures data consistency and hygiene across the candidate database by standardizing skill tagging.
- **Hiring Manager**
    - Receives curated shortlists of candidates who meet specific role requirements, reducing manual review time.
- **Talent Acquisition Lead**
    - Gains actionable insights into candidate pipeline health and skill gaps within the current applicant pool.

---

## Features
- **Intelligent Skill Extraction**
    - Automatically parses resumes to identify core competencies, years of experience, and certifications.
- **Workday Integration**
    - Seamlessly syncs matched candidate profiles directly into Workday using the Composio Toolset.
- **Real-time Scoring**
    - Ranks candidates based on the alignment between their profile and the specific job description requirements.
- **Automated Communication**
    - Triggers personalized follow-up emails or status updates to candidates based on their matching score.
- **Pipeline Hygiene**
    - Cleans and organizes candidate data to prevent duplicate entries and ensure accurate reporting.

---

## Use Cases
**Candidate Screening & Shortlisting**
- Automatically filter incoming applications against mandatory job requirements.
- Generate a ranked shortlist of the top 5 candidates for every new job opening.

**Data Enrichment & Sync**
- Update candidate profiles in Workday with parsed skill sets and experience tags.
- Sync candidate status changes across multiple platforms to keep the recruitment funnel accurate.

**Talent Pipeline Optimization**
- Identify "silver medalist" candidates from past applications for new, relevant roles.
- Monitor incoming candidate quality to adjust sourcing strategies in real-time.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Import Workflow."
2. Paste the solution JSON or connect via the Uplizd marketplace link.
3. Configure your API credentials for Workday and your LLM provider.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the candidate resume and job description text.
- **Agent**: Analyzes the input, performs skill mapping, and determines the match score.
- **Composio Toolset**: Executes the API calls to update candidate records in Workday.
- **Chat Output**: Returns the final match analysis and confirmation of the profile update.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Match the resume provided in the attachment against the Senior Software Engineer job description.`
- `Extract all technical skills from this candidate and update their profile in Workday.`
- `Score this candidate based on their experience with Python and Cloud Infrastructure.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized technical recruiter.
- Use a high-reasoning model (e.g., GPT-4o or Claude 3.5 Sonnet) for accurate skill parsing.
- Provide clear instructions on the scoring rubric (e.g., "Weight 5+ years of experience as 50% of the score").
- Ensure the agent outputs structured data (JSON) for seamless integration with downstream tools.

### 2) Composio Toolset Node
- Connect your Workday API key within the Composio dashboard.
- Set the connection scope to allow "Read/Write" access to candidate and job objects.

### 3) Tool Availability
- **Workday Search**: Locate existing candidate profiles.
- **Workday Update**: Modify candidate metadata and skill tags.
- **Email/Notification Service**: Send automated updates to the recruiting team.

---

## Related Solutions
- [Workforce Onboarding Automator](../workforce-onboarding-automator-by-connecteam/README.md) - Streamlines the employee transition process post-hiring.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enriches professional contact data for better outreach.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - General purpose automation for managing complex business processes.
