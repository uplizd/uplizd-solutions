# Course Cleanup Optimizer (Uplizd) - Intelligent archiving and lifecycle management for educational content

## Summary
The Course Cleanup Optimizer is an automated Uplizd AI workflow designed to streamline the maintenance of educational platforms like D2L Brightspace. By identifying outdated, unused, or redundant courses and assessments, this solution helps administrators maintain a clean, high-performance learning environment, reducing storage bloat and improving navigation velocity for instructors and students alike.

---

## Demo
![Course Cleanup Optimizer workflow dashboard showing automated course archiving and data hygiene status](image.png)
**Alt text (SEO-ready):** Course Cleanup Optimizer Uplizd workflow for D2L Brightspace, automated course archiving, data hygiene, and educational content management.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/a31d9ff5-a2f0-5b94-9f8c-d0a45e1a1923)

---

## Category
- **Primary category:** Operations
- **Secondary tags:** lms, d2l brightspace, data hygiene, course management, automation, archiving, workflow, ai agent
- This solution bridges the gap between static course catalogs and dynamic content management by automating the identification and archival of stale learning assets.

---

## Who is this for?
This solution is designed for educational administrators and IT teams managing large-scale learning environments.

- **LMS Administrator**
  - Automates the identification of inactive courses to reclaim storage and reduce clutter.
- **Instructional Designer**
  - Ensures that only current, relevant course versions are accessible to students and faculty.
- **Academic Operations Manager**
  - Maintains compliance and data hygiene standards across the institution's digital learning infrastructure.
- **IT Support Specialist**
  - Reduces manual ticket volume related to course navigation issues caused by outdated content.

---

## Features
- **Automated Audit Engine**
  - Scans D2L Brightspace environments to flag courses based on last-access dates and enrollment activity.
- **Intelligent Archival Logic**
  - Safely moves identified stale courses to an archive state without permanent data loss.
- **Customizable Thresholds**
  - Allows administrators to define specific time windows for what constitutes an "outdated" course.
- **Composio-Powered Integration**
  - Leverages the Composio Toolset to securely execute API calls directly within the D2L Brightspace ecosystem.
- **Reporting & Notification**
  - Generates summary logs of all cleanup actions, providing transparency for stakeholders.

---

## Use Cases
**Course Lifecycle Management**
- Automatically archive courses that have had zero student activity for more than 18 months.
- Flag duplicate or draft assessments that were never published to a live course section.

**Storage Optimization**
- Identify large, unused media files associated with legacy courses to free up institutional storage.
- Batch-process the cleanup of sandbox or test courses created during semester setup.

**Compliance & Data Hygiene**
- Ensure that outdated curriculum materials are removed to prevent student confusion and maintain institutional standards.
- Maintain a clean course directory to improve search performance and navigation for end-users.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to open the solution template.
2. Select your workspace and import the workflow configuration.
3. Connect your D2L Brightspace credentials via the Composio Toolset node.
4. Ensure nodes are correctly linked: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the trigger command or manual audit request.
- **Agent**: Processes instructions to evaluate course metadata against defined criteria.
- **Composio Toolset**: Executes the specific D2L Brightspace API actions for auditing and archiving.
- **Chat Output**: Returns a summary report of all courses processed and actions taken.

### 3) Run the Flow
Use the Playground to test your cleanup logic:
- `Audit all courses inactive for more than 2 years and generate a report.`
- `Archive the course with ID 12345 and notify the department head.`
- `List all courses created before 2022 that have no student enrollments.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the decision-making engine for content lifecycle management.
- Use a model capable of structured data reasoning (e.g., GPT-4o).
- Instruct the agent to prioritize safety by verifying course status before archival.
- Configure the system prompt to output logs in a consistent, readable format.

### 2) Composio Toolset Node
- Provide your D2L Brightspace API key and ensure the connection scope includes read/write access to course management endpoints.
- Verify that the Composio environment is active and authenticated.

### 3) Tool Availability
- **Course List API**: Fetching active and inactive course catalogs.
- **Course Update API**: Modifying course status and archival flags.
- **Logging Utility**: Recording audit results for administrative review.

---

## Related Solutions
- [Academic Impact Tracker](../academic-impact-tracker-by-semanticscholar/README.md) - Monitor and analyze the reach of academic research.
- [Academic Writing Precision Assistant](../academic-writing-precision-assistant-by-dictionary-api/README.md) - Enhance the quality and accuracy of educational content.
- [Workflow Health Monitor](../workflow-health-monitor-by-dailybot/README.md) - Track the operational efficiency of your automated processes.
