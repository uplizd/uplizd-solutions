# Signup Email Guardian (Uplizd) - Real-time email validation for secure user registration

## Summary
The Signup Email Guardian is an automated Uplizd workflow designed to validate user email addresses at the point of registration. By integrating real-time verification, this solution prevents fake account creation, reduces bounce rates, and ensures that your CRM or database remains populated with high-quality, deliverable contact information.

---

## Demo
![Signup Email Guardian workflow showing email input validation and Emailable integration](image.png)
**Alt text (SEO-ready):** Signup Email Guardian workflow by Uplizd, demonstrating real-time email validation, Emailable integration, and automated user registration security.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/7629ebc2-12c7-5b32-8502-8aa8a25d5d3e)

---

## Category
- **Primary category:** Data hygiene
- **Secondary tags:** email validation, emailable, user registration, data quality, security, lead management, composio, ai workflow
- This solution ensures your user acquisition pipeline remains clean by filtering out invalid or malicious email addresses before they enter your system.

---

## Who is this for?
This solution is designed for teams managing high-volume user signups who need to maintain data integrity and communication deliverability.

- **Growth Marketers**
    - Ensure marketing automation tools are only sending emails to verified, high-intent users.
- **Product Managers**
    - Reduce friction and fraud during the onboarding process by validating user identities instantly.
- **Sales Operations**
    - Maintain a pristine CRM database by preventing junk data from entering the lead pipeline.
- **Security Engineers**
    - Mitigate the risk of bot-driven account creation and spam by enforcing strict email verification protocols.

---

## Features
- **Real-time Verification**
    - Instantly check the validity of email addresses via the Emailable API as soon as a user submits a form.
- **Automated Filtering**
    - Automatically flag or block registrations associated with disposable, invalid, or high-risk email domains.
- **Composio-Powered Integration**
    - Seamlessly bridge the gap between your registration interface and the Emailable toolset using the Composio workflow engine.
- **Data Hygiene Reporting**
    - Log verification results to maintain a clear audit trail of accepted and rejected registration attempts.
- **Configurable Thresholds**
    - Adjust sensitivity settings to balance between strict security and user conversion requirements.

---

## Use Cases
**Registration Security**
- Automatically block temporary or "burner" email addresses from creating trial accounts.
- Prevent bot-driven signups by verifying the deliverability of the provided email address in real-time.

**Lead Quality Management**
- Ensure that only high-quality, reachable leads are passed to your downstream CRM or email marketing platform.
- Reduce bounce rates by filtering out mistyped or non-existent email addresses before they reach your sales team.

**Operational Efficiency**
- Automate the cleanup of your user database by identifying and removing decayed or invalid email entries.
- Streamline the onboarding experience by providing instant feedback to users if their email address appears invalid.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the solution template.
2. Connect your Emailable API credentials within the Composio integration settings.
3. Map your registration form input field to the Chat Input node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the email address submitted by the user during the registration process.
- **Agent**: Analyzes the input and triggers the verification process using the connected toolset.
- **Composio Toolset**: Executes the Emailable API call to validate the email's deliverability and status.
- **Chat Output**: Returns the validation status (Valid/Invalid) to the system to approve or reject the registration.

### 3) Run the Flow
Use the Playground to test the flow with these example prompts:
- `Validate the email address: test-user@example.com`
- `Check if the following email is deliverable: user-123@disposable-domain.com`
- `Verify the status of the email: contact@valid-business.com`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the decision-making layer that interprets the Emailable response.
- Use a model capable of structured output (e.g., GPT-4o or Claude 3.5).
- Instruction: "Analyze the API response from Emailable; if the email is 'deliverable', return 'Approved', otherwise return 'Rejected'."
- Ensure the agent is configured to handle API errors gracefully by defaulting to a 'Manual Review' status.

### 2) Composio Toolset Node
- Provide your Emailable API Key in the Composio dashboard.
- Set the connection scope to allow read-only access to email verification endpoints.

### 3) Tool Availability
- **Emailable Verify**: Endpoint to check syntax, domain health, and mailbox existence.
- **Emailable Batch**: Optional capability for bulk cleaning of existing user databases.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) - Enrich user profiles with firmographic data.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) - Maintain overall CRM data health and formatting.
- [Account Verification Assistant](../account-verification-assistant-by-twocaptcha/README.md) - Solve CAPTCHAs and verify user authenticity during signup.
