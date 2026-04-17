# Location-Based Fraud Detector (Uplizd) - Real-time identity and geolocation risk mitigation

## Summary
The Location-Based Fraud Detector is an automated Uplizd AI workflow designed to protect platforms from fraudulent activity by cross-referencing user-provided location data against IP geolocation and identity signals. By leveraging the Composio Toolset to integrate with real-time data providers, this solution enables security teams and operations managers to identify anomalies, prevent unauthorized access, and maintain platform integrity with high pipeline velocity.

---

## Demo
![Location-Based Fraud Detector workflow showing input validation, geolocation lookup, and risk scoring nodes](image.png)
**Alt text (SEO-ready):** Location-Based Fraud Detector workflow in Uplizd, showing IP geolocation lookup, identity verification, and automated risk scoring via Composio integrations.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/741dd5cb-2adc-59a1-89c1-e8fea31746fa)

---

## Category
**Primary category:** Data integration
**Secondary tags:** fraud detection, geolocation, identity verification, security, risk management, data hygiene, composio, ai workflow
This solution bridges the gap between user input and global security databases to ensure automated, real-time fraud prevention.

---

## Who is this for?
This workflow is designed for teams managing high-volume user interactions where security and data accuracy are paramount.

*   **Security Operations Manager**
    *   Automates the detection of high-risk login attempts and suspicious location patterns.
*   **Compliance Officer**
    *   Ensures platform usage adheres to regional data residency and access policies.
*   **Fraud Analyst**
    *   Reduces manual review time by surfacing high-confidence risk scores for flagged accounts.
*   **Platform Engineer**
    *   Integrates robust identity verification checks directly into existing user onboarding pipelines.

---

## Features
- **Real-time IP Geolocation**
    Automatically maps incoming user IP addresses to physical coordinates to detect discrepancies.
- **Identity Signal Cross-Referencing**
    Connects with external data providers via Composio to validate user contact information against known risk databases.
- **Automated Risk Scoring**
    Assigns a dynamic risk score to every transaction or login attempt based on configurable security thresholds.
- **Instant Alerting**
    Triggers immediate notifications or account freezes when high-risk location anomalies are detected.
- **Seamless API Integration**
    Utilizes the Composio Toolset to maintain stable, authenticated connections with global fraud detection and geolocation services.

---

## Use Cases
**Account Security & Authentication**
*   Flagging login attempts originating from countries outside of a user's established geographic profile.
*   Blocking access for known malicious IP ranges and VPN exit nodes identified in real-time.

**Onboarding & KYC Compliance**
*   Verifying that the physical address provided during signup matches the geolocation of the user's device.
*   Automating the screening of new accounts against global watchlists to prevent synthetic identity fraud.

**Transaction Integrity**
*   Validating the proximity of a user's location to the billing address associated with a payment method.
*   Identifying velocity attacks where multiple accounts are accessed from a single suspicious location.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Workflow."
2. Import the Location-Based Fraud Detector template from the solution library.
3. Connect your preferred security and geolocation API keys within the integration settings.
4. Ensure nodes are correctly wired: **Chat Input** → **Agent** → **Composio Toolset** → **Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives user metadata, including IP address and reported location.
*   **Agent**: Processes the input, evaluates risk logic, and determines if a tool call is required.
*   **Composio Toolset**: Executes the specific API queries to fetch geolocation and identity verification data.
*   **Chat Output**: Returns the final risk assessment and recommended action to the user or system dashboard.

### 3) Run the Flow
Open the Playground and test the flow with the following prompts:
*   `"Check if the IP 192.168.1.1 matches the user's reported location in New York."`
*   `"Analyze the risk score for user ID 8842 based on their recent login geolocation."`
*   `"Identify any potential fraud indicators for a signup originating from a high-risk region."`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the analytical engine, interpreting raw data and applying security rules.
*   Prioritize accuracy and strict adherence to defined risk thresholds.
*   Maintain a neutral, objective tone when reporting risk scores.
*   Ensure the agent is instructed to request manual review for "medium-risk" flags.

### 2) Composio Toolset Node
*   **API Key**: Configure the connection with your specific geolocation and security provider keys.
*   **Connection Scope**: Limit the agent's access to read-only security data to maintain system integrity.

### 3) Tool Availability
*   **IP Geolocation API**: Provides latitude, longitude, and ISP data.
*   **Identity Verification Service**: Checks against global fraud databases.
*   **Risk Scoring Engine**: Calculates the probability of fraudulent activity based on input signals.

---

## Related Solutions
*   [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich user profiles with verified contact and identity data.
*   [Account Verification Assistant](../account-verification-assistant-by-twocaptcha/README.md) - Automate the verification of user credentials and CAPTCHA challenges.
*   [Admin User Access Auditor](../admin-user-access-auditor-by-storeganise/README.md) - Monitor and audit user access levels to ensure platform security.
