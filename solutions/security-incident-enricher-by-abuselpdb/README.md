# Security Incident Enricher (Uplizd) - Automated threat context and attribution for security incidents

## Summary
The Security Incident Enricher is an intelligent Uplizd workflow that automatically gathers threat intelligence and attribution data for incoming security alerts. By integrating real-time security data sources, this solution reduces manual investigation time, eliminates context-switching, and provides security teams with a single source of truth for rapid incident response and triage.

---

## Demo
![Security Incident Enricher workflow diagram showing automated threat intelligence lookup and incident attribution](image.png)
**Alt text (SEO-ready):** Security Incident Enricher workflow in Uplizd for automated threat intelligence lookup, incident attribution, and security alert enrichment using Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run%20on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/3d173f69-876a-5d7c-9f6d-7410c6fac7bc)

---

## Category
**Primary category:** Security Operations
**Secondary tags:** security, threat intelligence, incident response, abuselpdb, automation, data enrichment, composio, ai workflow

This solution streamlines security operations by automating the enrichment of raw incident data with actionable threat intelligence.

---

## Who is this for?
This solution is designed for security professionals who need to accelerate incident triage and minimize the time spent on manual research.

*   **Security Analyst**
    *   Reduces time-to-resolution by automatically pulling threat context for every incoming alert.
*   **SOC Manager**
    *   Ensures consistent incident documentation and improved hygiene across the security operations center.
*   **Incident Responder**
    *   Provides immediate attribution data, allowing for faster decision-making during active security events.
*   **DevSecOps Engineer**
    *   Integrates automated enrichment pipelines into existing security workflows to maintain high pipeline velocity.

---

## Features
- **Automated Threat Lookup**
    Leverages the Composio Toolset to query threat intelligence databases like AbuseIPDB in real-time.
- **Contextual Incident Enrichment**
    Automatically maps raw IP or domain data to known threat actors and historical incident patterns.
- **Standardized Reporting**
    Formats complex security data into clear, actionable summaries for immediate team review.
- **Seamless Integrations**
    Connects directly with security tooling to trigger enrichment workflows the moment an alert is ingested.
- **Real-time Triage**
    Reduces the manual burden on analysts by filtering noise and highlighting high-confidence threats.

---

## Use Cases
**Threat Intelligence Gathering**
*   Automatically query IP addresses against global blacklists upon incident ingestion.
*   Attach historical abuse reports to new tickets to identify recurring attack patterns.

**Incident Response Acceleration**
*   Summarize threat actor profiles to help responders understand the scope of an attack.
*   Update security incident fields with attribution data to prioritize critical threats.

**Security Operations Hygiene**
*   Ensure every security alert contains verified attribution data before reaching an analyst.
*   Maintain a clean, searchable database of enriched incident logs for post-mortem analysis.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Authenticate your security tool connectors within the Uplizd dashboard.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the raw security alert or incident ID.
*   **Agent**: Analyzes the input and determines the necessary threat intelligence queries.
*   **Composio Toolset**: Executes the API calls to security databases to fetch enrichment data.
*   **Chat Output**: Delivers the enriched incident report back to the user or ticketing system.

### 3) Run the Flow
Use the Playground to test the workflow with the following prompts:
* `Enrich incident ID 99284 with current threat intelligence.`
* `Check the reputation of IP 192.168.1.1 and provide an attribution summary.`
* `Analyze the latest security alert and append threat actor details to the incident record.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the security analyst, interpreting raw data and synthesizing threat reports.
* Use a model with strong reasoning capabilities for accurate threat attribution.
* Instruct the agent to prioritize high-confidence data sources.
* Ensure the output is formatted for immediate consumption by security teams.

### 2) Composio Toolset Node
* Provide your API keys for the relevant security intelligence platforms.
* Set the connection scope to allow read-only access to threat databases.

### 3) Tool Availability
* **AbuseIPDB**: For real-time IP reputation and abuse reporting.
* **Security API Connectors**: For fetching incident metadata and updating ticket fields.
* **Data Formatting Tools**: For converting raw JSON threat data into human-readable summaries.

---

## Related Solutions
* [Abuse Report Manager](../abuse-report-manager-by-abuselpdb/README.md) - Streamline the management and reporting of abuse incidents.
* [Account Audit Agent](../account-audit-agent-by-cloudflare/README.md) - Automate security audits and account access monitoring.
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track and maintain the operational health of your automated workflows.
