# Location Data Enricher (Uplizd) - Automate geographic data enrichment and business intelligence

## Summary
The Location Data Enricher (Uplizd) is an intelligent AI workflow that automates the process of appending precise geographic coordinates, regional business details, and location-based metadata to your existing customer records. By leveraging the Yandex Geocoder and search APIs, this solution eliminates manual data entry, ensures a single source of truth for location-based operations, and significantly improves the hygiene of your CRM data pipeline.

---

## Demo
![Location Data Enricher workflow interface showing Yandex API integration and data mapping](image.png)
**Alt text (SEO-ready):** Location Data Enricher workflow in Uplizd, showing automated geographic data enrichment, Yandex API integration, and CRM data pipeline synchronization.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/c0ee38a0-f683-5066-836f-56a002e1aefd)

---

## Category
- **Primary category:** Data integration
- **Secondary tags:** yandex, geocoding, data enrichment, crm, data hygiene, api automation, location services, composio
- This solution bridges the gap between raw address strings and actionable location intelligence, streamlining your data enrichment workflows.

---

## Who is this for?
This solution is designed for data-driven teams looking to standardize location information across their enterprise applications.

- **Data Operations Manager**
    - Automates the bulk cleaning and standardization of address fields across disparate databases.
- **Sales Operations Lead**
    - Ensures sales territories are accurately mapped by enriching lead data with precise geographic coordinates.
- **Logistics Coordinator**
    - Validates shipping and service locations in real-time to optimize delivery routes and operational efficiency.
- **Marketing Analyst**
    - Enables hyper-local segmentation by appending regional business data to customer profiles.

---

## Features
- **Automated Geocoding**
    - Converts unstructured address strings into precise latitude and longitude coordinates using the Yandex Geocoder API.
- **Business Intelligence Enrichment**
    - Automatically appends relevant business metadata, such as district, postal codes, and regional identifiers, to customer records.
- **Composio Toolset Integration**
    - Leverages the Composio framework to securely manage API connections and authentication with Yandex services.
- **Real-time Data Sync**
    - Processes location updates instantly, ensuring that your CRM remains the single source of truth for geographic data.
- **Error Handling & Validation**
    - Identifies and flags incomplete or ambiguous address entries for manual review, maintaining high data hygiene standards.

---

## Use Cases
**Territory Management**
- Automatically assign new leads to the correct sales representative based on enriched regional data.
- Update existing account records with current district information to reflect organizational changes.

**Logistics & Operations**
- Validate customer delivery addresses against official geographic databases to reduce shipping errors.
- Calculate distance-based service fees by retrieving accurate location coordinates for client sites.

**Marketing & Analytics**
- Segment customer lists by specific geographic regions to run targeted local marketing campaigns.
- Visualize customer density and market penetration using enriched location data in your BI dashboard.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge above to navigate to the solution page.
2. Select "Import Flow" to add the Location Data Enricher template to your workspace.
3. Connect your Yandex API credentials via the Composio Toolset node.
4. Ensure nodes are correctly mapped: **Chat Input → Agent → Composio Toolset → Chat Output**.

### 2) Setup the Nodes
- **Chat Input**: Receives the raw address or business name string from your CRM or user input.
- **Agent**: Processes the input, determines the necessary geocoding parameters, and instructs the toolset.
- **Composio Toolset**: Executes the Yandex API calls to retrieve and format the requested location data.
- **Chat Output**: Returns the enriched location details or confirmation of the data update.

### 3) Run the Flow
Use the Uplizd Playground to test the enrichment capabilities:
- `Enrich the address: "123 Business St, Moscow" with full geographic details.`
- `Find location coordinates for "Central Business District, St. Petersburg" and update the CRM.`
- `Validate and append regional metadata for the following list of client addresses: [List].`

---

## Configuration
### 1) Language Model (Agent Node)
The agent acts as the orchestrator between user intent and the Yandex API.
- Use a model capable of structured data output (e.g., GPT-4o or Claude 3.5).
- Instruct the agent to prioritize accuracy and handle ambiguous address inputs gracefully.
- Configure the system prompt to output JSON-formatted location data for seamless CRM integration.

### 2) Composio Toolset Node
- Provide your valid Yandex API key within the Composio configuration panel.
- Set the connection scope to allow read/write access to geocoding and search endpoints.

### 3) Tool Availability
- **Geocoding API**: For converting text addresses to coordinates.
- **Search API**: For retrieving business-specific location metadata.
- **Data Formatter**: For standardizing API responses into your required schema.

---

## Related Solutions
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enhance account records with firmographic and contact data.
- [CRM Data Sync Agent](../crm-data-sync-agent/README.md) — Maintain data consistency across multiple CRM platforms.
- [CRM Data Hygiene Manager](../crm-data-hygiene-manager/README.md) — Clean and deduplicate your CRM database automatically.
