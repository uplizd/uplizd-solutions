# Email Campaign Link Manager (Uplizd) - Automate URL shortening and tracking for marketing campaigns

## Summary
The Email Campaign Link Manager (Uplizd) streamlines marketing operations by automatically shortening, standardizing, and tracking campaign URLs via TinyURL. This workflow eliminates manual link management, ensures consistent tracking parameters across email platforms, and provides a single source of truth for campaign performance metrics, ultimately increasing pipeline velocity and link hygiene.

---

## Demo
![Email Campaign Link Manager workflow showing URL input, TinyURL processing, and output generation](image.png)
**Alt text (SEO-ready):** Email Campaign Link Manager workflow using Uplizd, TinyURL, and Composio for automated marketing link shortening and campaign tracking.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-Launch_Solution-blue)](https://uplizd.ai/solutions/0e12a27b-d69b-5e32-9a54-f4c0e68ebcad)

---

## Category
**Marketing operations**
- `marketing`, `email`, `tinyurl`, `link management`, `automation`, `composio`, `ai workflow`, `campaign tracking`

This solution bridges the gap between marketing content creation and link distribution, ensuring every campaign asset is tracked accurately.

---

## Who is this for?
This solution is designed for marketing teams and operations professionals who need to maintain clean, trackable links at scale.

- **Email Marketer**
    - Ensures all campaign links are shortened and formatted correctly before hitting the send button.
- **Marketing Ops Manager**
    - Maintains data hygiene by standardizing URL structures across diverse email platforms.
- **Growth Specialist**
    - Gains visibility into campaign performance through consistent, trackable link metrics.
- **Content Strategist**
    - Automates the tedious process of manual link generation, allowing more time for high-level campaign planning.

---

## Features
- **Automated URL Shortening**
    - Instantly converts long, messy URLs into clean, professional links using the TinyURL API.
- **Standardized Tracking Parameters**
    - Automatically appends UTM parameters to ensure every click is attributed to the correct campaign source.
- **Real-time Link Validation**
    - Checks link integrity before deployment to prevent broken redirects in live email campaigns.
- **Composio-Powered Integration**
    - Leverages the Composio Toolset to securely connect the Uplizd agent with your TinyURL account.
- **Bulk Processing Capability**
    - Handles multiple links simultaneously, significantly reducing the time required for large-scale email blasts.

---

## Use Cases
**Campaign Launch Preparation**
- Automatically generate shortened links for all CTA buttons in a new product announcement email.
- Validate and shorten landing page URLs to ensure they meet platform character limits.

**Performance Tracking & Analytics**
- Standardize link naming conventions to ensure clean data ingestion into your CRM or analytics dashboard.
- Create unique, trackable links for different segments of an email list to measure A/B test performance.

**Content Distribution Hygiene**
- Replace long, unreadable URLs in newsletters with branded, shortened alternatives.
- Maintain a centralized log of all campaign links generated for audit and historical reporting.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Email Campaign Link Manager JSON configuration.
3. Connect your TinyURL API credentials within the Composio integration settings.
4. Ensure nodes are correctly mapped: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw long URL and campaign metadata from the user.
- **Agent**: Processes the request, applies UTM logic, and instructs the toolset.
- **Composio Toolset**: Executes the API call to TinyURL to generate the shortened link.
- **Chat Output**: Returns the finalized, shortened, and tracked URL to the user.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Shorten this URL for my Q3 newsletter campaign: https://example.com/landing-page?source=email`
- `Generate a TinyURL for this link and add UTM parameters for a LinkedIn outreach campaign.`
- `Process these 3 links for the upcoming product launch email and return the shortened versions.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator for link formatting and tool selection.
- Use a model capable of structured data handling (e.g., GPT-4o or Claude 3.5).
- **Instruction Pattern:**
    - "Always prioritize the addition of UTM parameters before shortening."
    - "If a link is already shortened, return an error message to the user."
    - "Maintain a professional tone when confirming the generated links."

### 2) Composio Toolset Node
- Provide your **TinyURL API Key** in the integration settings.
- Ensure the connection scope allows for link creation and retrieval.

### 3) Tool Availability
- `tinyurl_shorten`: Primary tool for link conversion.
- `tinyurl_get_stats`: Optional tool for retrieving click-through data on generated links.
- `url_validator`: Utility for checking link reachability.

---

## Related Solutions
- [../affiliate-link-performance-tracker-by-cutt-ly/README.md](../affiliate-link-performance-tracker-by-cutt-ly/README.md) - Track affiliate link performance and click metrics.
- [../abandoned-cart-recovery-agent-by-klaviyo/README.md](../abandoned-cart-recovery-agent-by-klaviyo/README.md) - Automate recovery emails for abandoned shopping carts.
- [../whats-app-lead-nurturing-agent-by-spoki/README.md](../whats-app-lead-nurturing-agent-by-spoki/README.md) - Nurture leads through automated messaging workflows.
