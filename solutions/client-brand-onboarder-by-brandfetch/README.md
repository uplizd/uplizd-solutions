# Client Brand Onboarder (Uplizd) - Automated asset collection and brand identity synchronization

## Summary
The Client Brand Onboarder by Brandfetch automates the collection, validation, and organization of client brand assets, ensuring your creative and marketing teams have a single source of truth for logos, colors, and typography from the moment a project begins. By leveraging the Brandfetch API, this Uplizd workflow eliminates manual file hunting, reduces onboarding friction, and maintains brand hygiene across all client-facing deliverables.

---

## Demo
![Uplizd workflow diagram showing the Client Brand Onboarder process from Chat Input to Brandfetch asset retrieval and final output](../image.png)
**Alt text (SEO-ready):** Uplizd Client Brand Onboarder workflow using Brandfetch integration for automated asset collection and brand identity synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/1515700c-355e-5dd3-aa73-7196115c6ad1)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** brandfetch, asset management, client onboarding, brand identity, automation, workflow, data integration, creative operations
- This solution streamlines the creative onboarding process by bridging the gap between client input and centralized brand asset repositories.

---

## Who is this for?
This solution is designed for teams that need to standardize their creative intake process and ensure brand consistency across every project.

- **Account Managers**
    - Reduce time spent chasing clients for high-resolution logos and brand guidelines.
- **Creative Directors**
    - Ensure all designers have immediate access to the correct, approved brand assets.
- **Marketing Operations Managers**
    - Maintain a clean, organized database of client brand identities for scalable project delivery.
- **Onboarding Specialists**
    - Automate the initial setup phase of new client accounts to accelerate time-to-value.

---

## Features
- **Automated Asset Retrieval**
    - Instantly fetch logos, color palettes, and fonts directly from the Brandfetch database using only a company domain.
- **Real-time Brand Validation**
    - Verify that the retrieved assets meet your team's quality and format requirements before project kickoff.
- **Centralized Asset Sync**
    - Automatically push validated brand assets into your project management or storage tools via the Composio Toolset.
- **Intelligent Error Handling**
    - Receive proactive alerts if a brand profile is incomplete or if assets are missing, allowing for immediate client follow-up.
- **Standardized Onboarding Pipeline**
    - Create a repeatable, scalable workflow that ensures every new client engagement starts with a consistent data foundation.

---

## Use Cases
**New Client Kickoff**
- Automatically pull brand identity assets the moment a new client record is created in your CRM.
- Generate a summary report of the client's brand presence to share with the internal creative team.

**Creative Project Preparation**
- Populate design project folders with the correct brand assets before the first design sprint begins.
- Update existing project documentation with the latest brand guidelines retrieved directly from the client's domain.

**Brand Audit & Hygiene**
- Periodically verify that the brand assets on file for long-term clients are still current and accurate.
- Identify and flag clients with outdated or missing brand identity components in your internal database.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your preferred workspace to import the workflow.
3. Connect your Brandfetch API key and any required storage integrations in the settings.
4. Ensure nodes are properly linked and the workflow is enabled in your environment.

### 2) Setup the Nodes
- **Chat Input**: Receives the client domain or company name to trigger the lookup.
- **Agent**: Processes the input and orchestrates the Brandfetch API calls to extract relevant brand data.
- **Composio Toolset**: Executes the secure connection to retrieve assets and sync them to your destination.
- **Chat Output**: Delivers a confirmation message with a summary of the retrieved brand assets and their storage location.

### 3) Run the Flow
Use the Playground to test your workflow with these prompts:
- `Fetch brand assets for apple.com and save them to the new project folder.`
- `Retrieve the primary color palette and logo for google.com.`
- `Check if microsoft.com has updated their brand assets and notify the design team.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the central intelligence for interpreting brand requests and managing API interactions.
- Use a model capable of structured data extraction (e.g., GPT-4o or Claude 3.5 Sonnet).
- Instruct the agent to prioritize high-resolution asset retrieval.
- Configure the agent to format output clearly for non-technical stakeholders.

### 2) Composio Toolset Node
- Provide your Brandfetch API key to enable secure access to the brand database.
- Define the scope to include read-only access for asset retrieval and write access for your designated storage platform.

### 3) Tool Availability
- **Brandfetch API**: For querying company domains and retrieving identity assets.
- **File Storage Connectors**: For saving assets to platforms like Google Drive, Dropbox, or internal project management tools.
- **Notification Tools**: For alerting team members once the onboarding process is complete.

---

## Related Solutions
- [Account Research Agent](../account-research-agent-by-onepage/README.md) - Automate deep-dive research into new client accounts.
- [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) - Streamline the technical onboarding of new accounts in your CRM.
- [Workflow Automation Agent](../workflow-automation-agent-by-jobnimbus/README.md) - Extend your onboarding process with end-to-end task automation.
