# Meeting Compliance Monitor (Uplizd) - Automated regulatory oversight for meeting transcripts

## Summary
The Meeting Compliance Monitor is an intelligent Uplizd workflow that automatically scans meeting transcripts for sensitive data, regulatory violations, and non-compliant language. By leveraging the Composio Toolset to interface with communication platforms like Fireflies, this solution provides legal and operations teams with a single source of truth for corporate governance, ensuring pipeline hygiene and mitigating risk through real-time automated auditing.

---

## Demo
![Meeting Compliance Monitor dashboard showing transcript analysis and flagged compliance violations](image.png)
**Alt text (SEO-ready):** Meeting Compliance Monitor dashboard displaying automated transcript analysis, regulatory flagging, and Uplizd workflow compliance auditing for enterprise meetings.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/facb9b38-2f69-562c-a619-8abb2c81e446)

---

## Category
**Primary category:** Legal Operations
**Secondary tags:** compliance, meeting analytics, fireflies, data governance, risk management, ai workflow, composio, transcript analysis.
This solution bridges the gap between raw meeting data and regulatory adherence by automating the identification of sensitive information.

---

## Who is this for?
This solution is designed for teams responsible for maintaining strict communication standards and mitigating corporate liability.

- **Legal Counsel**
    - Automates the review of thousands of meeting hours to ensure adherence to industry-specific regulatory frameworks.
- **Compliance Officer**
    - Receives instant alerts when sensitive topics or prohibited language are detected in recorded sessions.
- **Operations Manager**
    - Standardizes internal meeting hygiene by identifying recurring non-compliant communication patterns.
- **Sales Enablement Lead**
    - Ensures that client-facing representatives remain within the bounds of approved messaging and disclosure requirements.

---

## Features
- **Automated Transcript Scanning**
    - Real-time ingestion of meeting transcripts via Fireflies to identify keywords and phrases that trigger compliance flags.
- **Intelligent Risk Scoring**
    - Assigns a severity level to flagged interactions, allowing teams to prioritize manual review for high-risk discussions.
- **Composio-Powered Integration**
    - Seamlessly connects to your existing communication stack to pull data and push compliance reports into your CRM or internal tools.
- **Customizable Compliance Rules**
    - Define specific prohibited topics, sensitive data patterns, or required disclosures that the AI agent must monitor.
- **Audit-Ready Reporting**
    - Generates structured summaries of compliance checks, providing a clear trail for internal audits and regulatory inquiries.

---

## Use Cases
**Regulatory Data Protection**
- Automatically flag meetings where PII (Personally Identifiable Information) is discussed without proper consent protocols.
- Identify instances where mandatory legal disclaimers were omitted during client-facing calls.

**Corporate Policy Enforcement**
- Monitor for unauthorized promises or guarantees made by sales staff during discovery or negotiation calls.
- Detect the usage of non-approved terminology or outdated product positioning in recorded team syncs.

**Risk Mitigation & Training**
- Extract snippets of non-compliant interactions to use as real-world examples for internal sales training modules.
- Maintain a searchable database of flagged meetings to quickly respond to internal or external compliance audits.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and select the Meeting Compliance Monitor.
2. Click "Import" to add the workflow template to your workspace.
3. Connect your Fireflies account via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the meeting ID or transcript trigger.
- **Agent**: Analyzes the text against the provided compliance rulebook.
- **Composio Toolset**: Fetches transcript data and executes compliance logging actions.
- **Chat Output**: Returns the summary report and any identified violations.

### 3) Run the Flow
Use the Playground to test your compliance logic with the following prompts:
- `Scan the latest meeting from Fireflies and report any mentions of unapproved pricing discounts.`
- `Review the transcript for meeting ID 98765 and flag any PII leaks.`
- `Generate a compliance summary for all meetings held in the last 24 hours.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a specialized compliance auditor.
- **Instruction Pattern:**
    - Act as a senior legal compliance officer with expertise in industry-specific communication regulations.
    - Analyze transcripts strictly against the provided list of prohibited topics and mandatory disclosures.
    - Output findings in a structured format, including the timestamp, the specific violation, and a recommended action.

### 2) Composio Toolset Node
- Provide your API key for Fireflies and any secondary CRM integration keys.
- Set the connection scope to "Read-Only" for transcripts to ensure data integrity.

### 3) Tool Availability
- **Transcript Retrieval**: Accesses raw meeting text from Fireflies.
- **Data Logging**: Writes compliance reports to your internal database or Slack/Email.
- **Alerting**: Triggers notifications for high-severity violations.

---

## Related Solutions
- [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automates the organization and tracking of meeting follow-ups.
- [Account Health Usage Monitor](../account-health-usage-monitor-by-jotform/README.md) — Tracks customer engagement metrics to ensure account stability.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitors team communication and process efficiency.
