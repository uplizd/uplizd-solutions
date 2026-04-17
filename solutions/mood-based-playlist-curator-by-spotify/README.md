# Mood-Based Playlist Curator (Uplizd) - Automated AI-driven music curation for any mood

## Summary
The Mood-Based Playlist Curator is an intelligent Uplizd workflow that bridges the gap between human sentiment and digital music libraries. By leveraging the Composio Toolset to interface with Spotify, this solution analyzes user-provided mood descriptions or activity contexts to generate, update, and organize personalized music playlists in real-time. It provides a seamless way for music enthusiasts and content creators to maintain a dynamic, high-quality audio experience without manual track selection.

---

## Demo
![Mood-Based Playlist Curator workflow showing Chat Input, Agent, Composio Toolset, and Chat Output nodes](image.png)
**Alt text (SEO-ready):** Mood-Based Playlist Curator workflow diagram showing Uplizd AI agent integrating with Spotify via Composio Toolset for automated music playlist generation.

---

## 🚀 Run on Uplizd
[![Run on Uplizd](https://img.shields.io/badge/Run_on_Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/ee4f6db3-bd81-5c19-97bb-d6554f4b0d5e)

---

## Category
- **Primary category:** Media & Entertainment
- **Secondary tags:** spotify, music, automation, ai workflow, playlist, personalization, composio, user experience
- This solution streamlines digital music management by automating the curation process based on real-time user input.

---

## Who is this for?
This workflow is designed for individuals and professionals looking to optimize their listening experience through intelligent automation.

- **Music Enthusiasts**
    - Effortlessly generate thematic playlists for specific moods or events without spending hours searching for tracks.
- **Content Creators**
    - Quickly curate background music tracks that match the tone and pacing of their video or audio projects.
- **Fitness Instructors**
    - Automatically update workout playlists to match the intensity levels of different training sessions.
- **Event Planners**
    - Create custom, mood-appropriate music sets for gatherings, ensuring the atmosphere aligns perfectly with the event theme.

---

## Features
- **Natural Language Processing**
    - Interprets subjective mood descriptions or activity prompts to identify appropriate musical genres, tempos, and artists.
- **Spotify Integration**
    - Utilizes the Composio Toolset to authenticate and perform direct read/write operations on your personal Spotify library.
- **Dynamic Playlist Generation**
    - Automatically creates new playlists or appends tracks to existing ones based on the agent's intelligent analysis.
- **Real-time Synchronization**
    - Ensures that your music library stays updated instantly as your mood or activity requirements change throughout the day.
- **Context-Aware Curation**
    - Refines track selection by considering historical listening data and current user-defined constraints.

---

## Use Cases
**Personalized Listening**
- Generate a "Focus" playlist for deep work sessions by specifying a preference for lo-fi beats or instrumental tracks.
- Create an "Energy Boost" collection for morning routines by filtering for high-BPM songs from your saved library.

**Event & Activity Planning**
- Curate a "Dinner Party" playlist that transitions from upbeat jazz to mellow acoustic tracks based on the time of evening.
- Build a "Post-Workout Cool Down" list that automatically selects tracks with lower energy profiles after a high-intensity session.

**Content & Professional Use**
- Generate mood-specific background tracks for video editing projects to ensure the audio matches the visual narrative.
- Organize weekly "Discovery" playlists by asking the agent to find new releases that match your favorite genres.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Navigate to the Uplizd dashboard and select "Create New Flow."
2. Import the Mood-Based Playlist Curator JSON template provided in this repository.
3. Connect your Spotify account via the Composio integration settings.
4. Ensure nodes are correctly linked: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives your mood, activity, or genre-based request.
- **Agent**: Processes the natural language input and determines the necessary Spotify API calls.
- **Composio Toolset**: Executes the search, creation, and track-adding commands on your Spotify account.
- **Chat Output**: Confirms the playlist creation and provides a direct link to your new music collection.

### 3) Run the Flow
Open the Playground and test the workflow with these prompts:
- `Create a high-energy playlist for a 30-minute HIIT workout.`
- `Make a relaxing acoustic playlist for reading on a rainy afternoon.`
- `Add some upbeat 80s pop tracks to my "Friday Night" playlist.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent acts as the orchestrator between your intent and the Spotify API.
- **Recommended instruction pattern:**
    - Act as a professional music curator with deep knowledge of genres and mood-based audio profiles.
    - Always verify the user's intent before modifying existing playlists to prevent accidental deletions.
    - Use the Composio Toolset to search for tracks that match the requested mood descriptors.

### 2) Composio Toolset Node
- **API Key**: Ensure your Spotify developer credentials are saved within the Composio connection settings.
- **Connection Scope**: Grant the necessary permissions for playlist modification and library access.

### 3) Tool Availability
- `spotify_search_tracks`: Find songs based on mood, genre, or artist.
- `spotify_create_playlist`: Initialize a new playlist container.
- `spotify_add_tracks_to_playlist`: Populate the playlist with curated selections.
- `spotify_get_user_playlists`: Retrieve existing lists for updates or appending.

---

## Related Solutions
- [Workout Music Optimizer (Spotify)](../workout-music-optimizer-by-spotify/README.md) — Automate the creation of high-energy music sets for fitness routines.
- [YouTube Content Performance Optimizer](../you-tube-content-performance-optimizer-by-youtube/README.md) — Analyze and improve the reach of your video content.
- [Account Intelligence Gatherer](../account-intelligence-gatherer-by-dropcontact/README.md) — Enrich your CRM data with external account insights.
