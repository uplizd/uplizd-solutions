# Meeting Compliance & Privacy Monitor (Uplizd) - Automated meeting data governance and privacy enforcement

## Summary
The Meeting Compliance & Privacy Monitor is an intelligent Uplizd workflow designed to automate the oversight of sensitive meeting data, ensuring organizational adherence to privacy regulations. By leveraging the Composio Toolset to interface with platforms like Gong, this solution provides a single source of truth for compliance officers and legal teams, significantly reducing the risk of data exposure and improving pipeline hygiene through automated policy enforcement.

---

## Demo
![Meeting Compliance & Privacy Monitor workflow dashboard showing automated data privacy alerts and Gong integration status](image.png)
**Alt text (SEO-ready):** Meeting Compliance & Privacy Monitor (Uplizd) workflow dashboard showing automated data privacy alerts and Gong integration status for enterprise compliance.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABCSURBVEhLY2AYBaNgFIyCUUAKGAAABAAAV4J7+gAAAABJRU5ErkJggg==)](https://uplizd.ai/solutions/0dac6603-8183-56fd-ac8d-1473037520da)

---

## Category
**Primary category:** Legal & Compliance
**Secondary tags:** privacy, compliance, gong, data governance, meeting security, risk management, composio, ai workflow
This solution bridges the gap between raw meeting data and regulatory requirements by automating privacy audits and access controls.

---

## Who is this for?
This solution is built for teams responsible for maintaining strict data governance across customer-facing communications.

* **Compliance Officer**
    * Ensures all recorded meetings meet internal privacy standards and regulatory requirements.
* **Legal Counsel**
    * Automates the identification of sensitive information that requires redaction or restricted access.
* **Sales Operations Manager**
    * Maintains clean, compliant data pipelines within Gong to avoid downstream legal bottlenecks.
* **IT Security Analyst**
    * Monitors access logs and permission settings to prevent unauthorized data exposure.

---

## Features
- **Automated Privacy Audits**
  Scans meeting metadata and transcripts in real-time to flag potential compliance violations.
- **Gong Integration**
  Utilizes the Composio Toolset to securely interface with Gong, ensuring seamless data retrieval and policy application.
- **Risk Scoring Engine**
  Assigns a risk level to each meeting based on content sensitivity and participant access levels.
- **Proactive Alerting**
  Triggers immediate notifications to stakeholders when a non-compliant meeting is detected.
- **Access Control Enforcement**
  Automatically updates sharing permissions or archives meetings that fail to meet privacy criteria.

---

## Use Cases
**Regulatory Compliance**
* Automatically flagging meetings that contain PII (Personally Identifiable Information) for immediate legal review.
* Generating audit-ready reports of all compliance actions taken on recorded meeting assets.

**Data Hygiene**
* Identifying and purging or restricting access to outdated meeting recordings that exceed retention policies.
* Standardizing metadata tagging across all sales calls to ensure consistent data classification.

**Risk Mitigation**
* Detecting unauthorized external sharing of sensitive internal strategy or product roadmap discussions.
* Restricting access to high-stakes negotiation calls to authorized personnel only.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd marketplace and locate the Meeting Compliance & Privacy Monitor.
2. Click "Import" to add the workflow to your workspace.
3. Connect your Gong account via the Composio Toolset configuration.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives manual triggers or scheduled audit requests.
* **Agent**: Processes compliance logic and evaluates meeting data against privacy rules.
* **Composio Toolset**: Executes secure API calls to Gong to fetch and update meeting permissions.
* **Chat Output**: Returns a summary of compliance actions taken or alerts for manual intervention.

### 3) Run the Flow
Use the Playground to test your compliance monitoring:
* `Check all meetings from the last 24 hours for PII violations.`
* `Restrict access to all meetings tagged as 'Internal Strategy' to the legal team.`
* `Generate a compliance report for all calls involving the 'Enterprise' segment.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the compliance engine, interpreting privacy policies and executing tool calls.
* **Instruction Pattern:**
    * "You are a compliance assistant; prioritize data privacy and regulatory adherence."
    * "Always verify the sensitivity level before modifying access permissions."
    * "Provide clear, actionable summaries for every compliance flag identified."

### 2) Composio Toolset Node
* **API Key:** Provide your Gong API credentials within the Composio dashboard.
* **Connection Scope:** Ensure the agent has 'Read' and 'Write' access to meeting metadata and permission settings.

### 3) Tool Availability
* **Gong Search:** Locate meetings based on date, participant, or keyword.
* **Gong Metadata Update:** Modify tags and classification labels.
* **Permission Manager:** Update access lists and sharing settings for specific recordings.

---

## Related Solutions
* [Account Health Compliance Monitor](../account-health-compliance-monitor-by-brevo/README.md) — Monitor account health and compliance metrics.
* [Action Item Cleanup Agent](../action-item-cleanup-agent-by-rootly/README.md) — Automate the cleanup of stale action items and tasks.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Track and optimize the health of your automated workflows.
