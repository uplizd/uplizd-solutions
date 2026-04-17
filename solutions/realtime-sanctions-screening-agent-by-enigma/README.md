# Real-time Sanctions Screening Agent (Uplizd) - Automated global watchlist compliance and risk monitoring

## Summary
The Real-time Sanctions Screening Agent is an automated Uplizd workflow designed to continuously monitor customer databases against global sanctions lists and watchlists. By leveraging the Enigma API via the Composio Toolset, this solution ensures your organization maintains regulatory compliance, reduces manual screening overhead, and mitigates financial crime risk through proactive, real-time data verification.

---

## Demo
![Real-time Sanctions Screening Agent workflow interface showing automated watchlist checks and risk scoring](image.png)
**Alt text (SEO-ready):** Real-time Sanctions Screening Agent workflow in Uplizd, showing automated global watchlist integration, risk scoring, and compliance monitoring.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/56009dc1-ad7b-5e05-b8c0-618b89b8814c)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** compliance, risk management, sanctions screening, data verification, enigma, ai workflow, automated monitoring, regulatory reporting
- This solution streamlines the complex process of cross-referencing customer data against global sanctions databases to ensure continuous regulatory adherence.

---

## Who is this for?
This agent is built for teams responsible for maintaining high-integrity customer data and meeting stringent financial regulations.

- **Compliance Officer**
    - Automates the audit trail for watchlist checks to ensure consistent regulatory reporting.
- **Risk Manager**
    - Identifies high-risk entities in real-time to prevent exposure to sanctioned individuals or organizations.
- **Operations Lead**
    - Eliminates manual data entry and batch processing delays by integrating screening directly into the customer onboarding pipeline.
- **Data Analyst**
    - Maintains clean, verified customer records by flagging discrepancies between internal data and global watchlists.

---

## Features
- **Automated Watchlist Integration**
    - Seamlessly connects to Enigma’s global sanctions and watchlist databases to perform instant entity verification.
- **Real-time Risk Scoring**
    - Automatically calculates risk profiles based on screening results, allowing for immediate escalation of high-risk matches.
- **Continuous Monitoring**
    - Runs recurring checks on existing customer records to detect changes in sanctions status as global lists are updated.
- **Compliance Audit Logging**
    - Generates structured, timestamped logs of all screening activities, simplifying the preparation for regulatory audits.
- **Intelligent Triage**
    - Uses AI to filter out false positives, ensuring that compliance teams only focus on legitimate matches requiring human intervention.

---

## Use Cases
**Customer Onboarding**
- Automatically screen new applicants against global watchlists during the sign-up process.
- Flag high-risk entities for manual review before account activation.

**Ongoing Compliance Monitoring**
- Periodically re-screen the entire customer base to ensure no new sanctions have been applied to existing clients.
- Trigger automated alerts to the compliance team when a status change is detected.

**Risk Mitigation**
- Integrate screening results into internal CRM systems to prevent transactions with sanctioned entities.
- Maintain a centralized, up-to-date repository of screening outcomes for internal risk assessment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Real-time Sanctions Screening Agent template from the solution library.
3. Connect your Enigma API credentials within the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives customer entity details (name, jurisdiction, ID).
- **Agent**: Analyzes input and orchestrates the screening request via the Enigma toolset.
- **Composio Toolset**: Executes the API call to fetch real-time sanctions data.
- **Chat Output**: Returns the screening status, risk score, and recommended next steps.

### 3) Run the Flow
Use the Playground to test the agent with the following prompts:
- `Screen the entity 'Global Logistics Corp' located in Singapore for sanctions.`
- `Check the current sanctions status for 'John Doe' with ID 88291.`
- `Run a batch screening for the latest customer list and report any high-risk matches.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a compliance assistant, interpreting screening results and providing actionable summaries.
- **Recommended instruction pattern:**
    - "You are a compliance assistant. Analyze the Enigma API output for sanctions matches."
    - "If a match is found, provide the risk score and suggest whether to escalate or ignore."
    - "Maintain a professional, objective tone suitable for regulatory documentation."

### 2) Composio Toolset Node
- **API Key**: Ensure your Enigma API key is active and has permissions for watchlist screening.
- **Connection Scope**: Configure the toolset to allow read-only access to global sanctions databases.

### 3) Tool Availability
- **Entity Search**: Query global databases for specific names or identifiers.
- **Sanctions Matcher**: Compare entity details against updated global watchlists.
- **Risk Assessment Engine**: Analyze match confidence and provide a risk rating.

---

## Related Solutions
- [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) — Automate security and compliance audits for your cloud infrastructure.
- [Account Verification Assistant](../account-verification-assistant-by-twocaptcha/README.md) — Streamline user identity verification and CAPTCHA resolution.
- [Workplace Risk Early Warning System](../workplace-risk-early-warning-system-by-faceup/README.md) — Proactively identify and manage organizational risk factors.
