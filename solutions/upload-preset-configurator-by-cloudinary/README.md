# Upload Preset Configurator (Uplizd) - Automate media asset standardization and Cloudinary configuration

## Summary
The Upload Preset Configurator is an intelligent Uplizd AI workflow designed to streamline media asset management by automating the configuration of Cloudinary upload presets. By centralizing preset logic, marketing and development teams can ensure consistent image transformation, metadata tagging, and security settings across their digital infrastructure, ultimately reducing manual configuration errors and accelerating media pipeline velocity.

---

## Demo
![Upload Preset Configurator workflow interface showing Cloudinary integration nodes and preset configuration parameters](image.png)
**Alt text (SEO-ready):** Upload Preset Configurator (Uplizd) - Automated media asset standardization, Cloudinary preset management, and AI-driven workflow integration.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/aa1cce26-3ab3-5444-86ff-50eadcfa1d90)

---

## Category
**Primary category:** Marketing operations
**Secondary tags:** cloud-storage, cloudinary, media-management, asset-optimization, automation, workflow-orchestration, composio, digital-asset-management

This solution bridges the gap between creative asset requirements and technical storage configurations, serving as a single source of truth for media upload standards.

---

## Who is this for?
This solution is designed for teams managing high-volume media assets who need to maintain strict quality and compliance standards.

*   **Marketing Operations Manager**
    *   Ensures consistent branding and image transformation rules across all uploaded marketing assets.
*   **Web Developer**
    *   Automates the deployment of secure, optimized upload presets to prevent storage bloat and security vulnerabilities.
*   **Content Strategist**
    *   Maintains organized media libraries by enforcing metadata tagging and categorization at the point of upload.
*   **Digital Asset Manager**
    *   Reduces manual overhead by programmatically updating preset configurations as business requirements evolve.

---

## Features
- **Intelligent Preset Mapping**
    Automatically maps business requirements to Cloudinary upload preset parameters for consistent asset handling.
- **Real-time Configuration Sync**
    Utilizes the Composio Toolset to push updates directly to Cloudinary, ensuring changes are reflected immediately.
- **Automated Validation**
    Validates preset settings against organizational compliance rules before applying changes to the production environment.
- **Dynamic Metadata Tagging**
    Injects context-aware tags into media assets during the upload process to improve searchability and organization.
- **Error Handling & Logging**
    Provides detailed feedback on configuration failures, allowing for rapid remediation of preset deployment issues.

---

## Use Cases
**Media Pipeline Standardization**
*   Enforcing uniform image compression and format conversion settings for all user-generated content.
*   Standardizing watermarking and branding overlays across global marketing campaign assets.

**Compliance and Security**
*   Automatically applying restricted access policies to sensitive media folders via upload preset permissions.
*   Ensuring all uploaded assets are scanned for PII or prohibited content based on preset security filters.

**Operational Efficiency**
*   Bulk-updating upload presets across multiple Cloudinary cloud names to support new regional requirements.
*   Streamlining the onboarding of new developers by providing a pre-configured, automated preset setup process.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Upload Preset Configurator template from the solution library.
3. Connect your Cloudinary account via the Composio integration portal.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
*   **Chat Input**: Receives the desired preset configuration parameters or update requests.
*   **Agent**: Interprets the intent and translates natural language requests into specific Cloudinary API calls.
*   **Composio Toolset**: Executes the authenticated API requests to manage Cloudinary upload presets.
*   **Chat Output**: Confirms the successful application or modification of the upload preset.

### 3) Run the Flow
Use the Playground to test your configurations with these example prompts:
* `Create a new upload preset named 'web_optimized' with auto-format and 80% quality settings.`
* `Update the 'marketing_assets' preset to include a watermark overlay and auto-tagging.`
* `List all current upload presets and identify any that are missing the mandatory security headers.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator for your media configuration logic.
* Use a model capable of structured JSON output to ensure API compatibility.
* Instruct the agent to prioritize security and naming conventions defined in your organization's style guide.
* Enable tool-calling capabilities to allow the agent to query existing presets before proposing changes.

### 2) Composio Toolset Node
* Provide your Cloudinary API Key and Secret within the Composio connection settings.
* Ensure the connection scope includes `admin` permissions to allow for preset creation and modification.

### 3) Tool Availability
* **Preset Management**: Create, Read, Update, and Delete (CRUD) operations for upload presets.
* **Transformation Builder**: Tools to define complex image transformation strings.
* **Metadata Manager**: Capabilities to inject and update asset tags and context data.

---

## Related Solutions
* [Account Setup Agent by Salesforce](../account-setup-agent-by-salesforce/README.md) - Automate CRM account provisioning and configuration.
* [Accessibility Compliance Monitor by Alttext AI](../accessibility-compliance-monitor-by-alttext-ai/README.md) - Ensure media assets meet accessibility standards.
* [Workflow Automation Agent by JobNimbus](../workflow-automation-agent-by-jobnimbus/README.md) - Orchestrate complex business process automations.
