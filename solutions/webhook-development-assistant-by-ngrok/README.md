# Webhook Development Assistant (Uplizd) - Accelerate local webhook testing and tunnel management

## Summary
The Webhook Development Assistant is an AI-powered workflow designed to streamline the testing and debugging of webhooks by automating tunnel creation and payload inspection. By integrating directly with development tools like ngrok, this solution enables developers to expose local environments securely, capture incoming requests in real-time, and validate integration logic without manual configuration overhead.

---

## Demo
![Webhook Development Assistant workflow showing tunnel initialization and request inspection](image.png)
**Alt text (SEO-ready):** Webhook Development Assistant (Uplizd) workflow for automated tunnel management, ngrok integration, and real-time webhook payload inspection.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/b82f15a4-ca69-53e8-821e-7e2cd1ea7ef3)

---

## Category
**Primary category:** Development Operations  
**Secondary tags:** webhook, ngrok, api testing, devops, automation, tunnel, local development, composio  
This solution bridges the gap between local development environments and external service webhooks, ensuring seamless integration testing.

---

## Who is this for?
This assistant is built for engineering teams and developers who need to iterate rapidly on webhook-driven applications.

* **Backend Developer**
    * Reduces the time spent manually configuring tunnels and restarting local servers during integration testing.
* **API Integration Engineer**
    * Provides a reliable way to inspect and replay incoming webhook payloads to verify data handling logic.
* **DevOps Engineer**
    * Standardizes the local development environment setup, ensuring consistent tunnel security and access.
* **Full-Stack Developer**
    * Simplifies the end-to-end testing process for webhooks, allowing for faster feedback loops during feature development.

---

## Features
- **Automated Tunnel Provisioning**
  Uses the Composio Toolset to trigger ngrok tunnels instantly, exposing local ports to the internet with a single command.
- **Real-time Payload Inspection**
  Captures and logs incoming webhook requests directly into the chat interface for immediate analysis and debugging.
- **Dynamic Port Mapping**
  Automatically detects active local development ports and maps them to secure public URLs.
- **Webhook Replay Capability**
  Allows developers to re-trigger captured payloads to test changes to application logic without waiting for the source service.
- **Secure Access Control**
  Implements automated tunnel lifecycle management, ensuring tunnels are closed immediately after testing sessions conclude.

---

## Use Cases
**Local Development Testing**
* Exposing a local Node.js or Python server to test Stripe or Shopify webhook events.
* Validating signature verification logic by replaying captured payloads against local endpoints.

**API Integration Debugging**
* Troubleshooting malformed webhook payloads by inspecting raw headers and body content in the chat interface.
* Testing edge-case scenarios by manually injecting mock data into the local development pipeline.

**Workflow Automation**
* Integrating tunnel status updates into team Slack channels for shared visibility during collaborative debugging.
* Automating the cleanup of stale tunnels to maintain a clean and secure development environment.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" button above to open the template.
2. Select your workspace and project destination.
3. Configure your environment variables, including your ngrok API key.
4. Ensure nodes are correctly connected: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
* **Chat Input**: Receives your command to start a tunnel or inspect a specific webhook event.
* **Agent**: Processes natural language requests to determine which tunnel action or inspection tool to execute.
* **Composio Toolset**: Executes the specific ngrok or network commands required to manage your local environment.
* **Chat Output**: Returns the public tunnel URL or the parsed details of the captured webhook payload.

### 3) Run the Flow
Use the Playground to test the assistant with these prompts:
* `Start a new tunnel for local port 3000 and give me the public URL.`
* `List all active tunnels and their current status.`
* `Inspect the last received webhook payload and show me the JSON body.`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as a DevOps orchestrator, translating developer intent into network commands.
* Use a model capable of structured output (e.g., GPT-4o or Claude 3.5 Sonnet).
* Ensure the system prompt emphasizes tool-use accuracy for network operations.
* Maintain a concise, technical tone for all output responses.

### 2) Composio Toolset Node
* Provide a valid ngrok API key within the Composio configuration.
* Set the connection scope to include `ngrok` and `network-utils` to ensure the agent has full control over tunnel lifecycle management.

### 3) Tool Availability
* **ngrok_start_tunnel**: Creates a secure tunnel to a specified local port.
* **ngrok_list_tunnels**: Retrieves a list of currently active tunnels.
* **ngrok_close_tunnel**: Terminates a specific tunnel session.
* **webhook_inspector**: Parses and formats raw webhook request data for readability.

---

## Related Solutions
* [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) — Monitor the operational status of your automated development pipelines.
* [Account Setup Agent](../account-setup-agent-by-salesforce/README.md) — Automate the provisioning and configuration of CRM-integrated development accounts.
* [Action Item Prioritizer](../action-item-prioritizer-by-rootly/README.md) — Manage and prioritize debugging tasks identified during webhook integration testing.
