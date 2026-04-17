# Compliance Recording Controller (Uplizd) - Automated regulatory meeting management

## Summary
The Compliance Recording Controller is an intelligent Uplizd workflow designed to automate the governance of meeting recordings. By leveraging the Recall.ai integration, this solution monitors, tags, and manages recording lifecycles based on content sensitivity, ensuring organizations maintain strict regulatory compliance while reducing manual administrative overhead in legal and operational workflows.

---

## Demo
![Compliance Recording Controller workflow showing automated meeting analysis and storage routing](image.png)
**Alt text (SEO-ready):** Compliance Recording Controller workflow in Uplizd, automating meeting recording management, regulatory compliance, and Recall.ai integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAG5JREFUSEtjYBgFo2AUjIJRMApGATkBAAEAAAE=)](https://uplizd.ai/solutions/eb131665-3055-526c-8ebe-b005c05bc788)

---

## Category
- **Primary category:** Legal & Compliance
- **Secondary tags:** compliance, recall.ai, meeting management, data governance, legal ops, automation, workflow, security
- This solution bridges the gap between automated meeting capture and regulatory data retention policies.

---

## Who is this for?
This solution is designed for teams managing sensitive communications and high-stakes meeting data.

- **Compliance Officer**
    - Ensures all recorded meetings adhere to industry-specific data retention and privacy regulations.
- **Legal Counsel**
    - Automates the identification and secure archiving of privileged or sensitive meeting discussions.
- **IT Operations Manager**
    - Reduces storage costs and security risks by automating the deletion or archival of non-compliant recordings.
- **Sales Operations Lead**
    - Maintains clean, compliant records of client interactions without requiring manual intervention from account executives.

---

## Features
- **Automated Sensitivity Tagging**
    - Automatically analyzes meeting transcripts to categorize recordings based on sensitive content or regulatory keywords.
- **Recall.ai Integration**
    - Seamlessly connects with the Recall.ai platform to trigger recording actions, status updates, and metadata retrieval.
- **Policy-Driven Lifecycle Management**
    - Executes custom retention policies, such as auto-deleting non-compliant files or moving sensitive data to secure storage.
- **Real-time Compliance Monitoring**
    - Provides immediate feedback and logging on recording status, ensuring no meeting slips through the compliance net.
- **Unified Dashboard Control**
    - Centralizes recording oversight within the Uplizd builder, allowing for rapid adjustments to compliance logic.

---

## Use Cases
**Regulatory Data Retention**
- Automatically purge recordings that exceed the mandatory 30-day storage window for financial services.
- Flag and move recordings containing PII (Personally Identifiable Information) to an encrypted, restricted-access vault.

**Legal Discovery Preparation**
- Index meeting recordings by project or client name to streamline the e-discovery process during audits.
- Generate automated summaries of sensitive meetings for legal review, reducing the time spent listening to raw audio.

**Operational Hygiene**
- Identify and delete "empty" or "no-show" meeting recordings to optimize cloud storage utilization.
- Categorize internal vs. external meetings to apply different retention and visibility permissions automatically.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd solution library and select the **Compliance Recording Controller**.
2. Click **"Import"** to initialize the workflow in your workspace.
3. Connect your Recall.ai API credentials within the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives meeting metadata and trigger events from your recording platform.
- **Agent**: Processes meeting transcripts and evaluates them against your defined compliance logic.
- **Composio Toolset**: Executes commands via Recall.ai to update, delete, or move recordings.
- **Chat Output**: Confirms the action taken and logs the compliance status for the audit trail.

### 3) Run the Flow
Use the Playground to test your compliance logic with these prompts:
- `Check the recording status for meeting ID 98765 and apply the standard 30-day retention policy.`
- `Scan the transcript for meeting 12345 for sensitive financial terms and move to the secure compliance vault.`
- `Identify all recordings from last week that contain no participants and trigger an auto-delete.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the compliance engine, interpreting transcript data and mapping it to your specific organizational policies.
- **Instruction Pattern:**
    - "Analyze the provided transcript for specific keywords related to sensitive financial or legal data."
    - "Determine the appropriate retention action based on the meeting type and participant list."
    - "Output a structured summary of the action taken for the final audit log."

### 2) Composio Toolset Node
- Requires a valid **Recall.ai API Key** to interface with your recording infrastructure.
- Ensure the connection scope includes `read:recordings` and `write:recordings` permissions.

### 3) Tool Availability
- **Recall.ai List Recordings**: Fetch metadata for recent sessions.
- **Recall.ai Update Recording**: Modify storage or access tags.
- **Recall.ai Delete Recording**: Execute secure removal for expired data.
- **Recall.ai Get Transcript**: Retrieve text for sensitivity analysis.

---

## Related Solutions
- [../account-health-compliance-monitor-by-brevo/README.md](../account-health-compliance-monitor-by-brevo/README.md) — Monitors account health metrics to ensure regulatory and usage compliance.
- [../accessibility-compliance-monitor-by-alttext-ai/README.md](../accessibility-compliance-monitor-by-alttext-ai/README.md) — Automates accessibility auditing to maintain web compliance standards.
- [../work-hours-compliance-monitor-by-timely/README.md](../work-hours-compliance-monitor-by-timely/README.md) — Tracks work hours to ensure adherence to labor regulations and internal policies.
