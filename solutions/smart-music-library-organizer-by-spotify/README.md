# Smart Music Library Organizer (Uplizd) - Intelligent Spotify library curation and automated playlist management

## Summary
The Smart Music Library Organizer is an automated AI workflow designed to streamline your Spotify music collection by intelligently categorizing tracks, cleaning up metadata, and maintaining organized playlists. By leveraging the Composio Toolset to interface with the Spotify API, this solution eliminates manual library maintenance, ensuring your music discovery remains discoverable and perfectly sorted based on genre, mood, or tempo.

---

## Demo
![Smart Music Library Organizer workflow dashboard showing Spotify integration and categorization nodes](image.png)
**Alt text (SEO-ready):** Smart Music Library Organizer Uplizd workflow, Spotify library automation, AI-powered music playlist management, and Composio integration.

---

## 🚀 Run on Uplizd
[![](https://img.shields.io/badge/Run_on-Uplizd-blue?logo=uplizd)](https://uplizd.ai/solutions/9899095d-9bd0-5dd2-9975-3fd886ba8c1b)

---

## Category
- **Primary category:** Media operations
- **Secondary tags:** spotify, music library, automation, playlist management, data hygiene, ai workflow, composio, media organization
- This solution bridges the gap between raw music discovery and structured library management through automated AI-driven categorization.

---

## Who is this for?
This solution is designed for power users and music enthusiasts who need to maintain order in their digital audio collections.

- **Music Enthusiasts**
    - Automatically sort thousands of saved tracks into genre-specific playlists without manual effort.
- **Content Creators**
    - Quickly curate background music libraries for video projects based on mood or tempo metadata.
- **Playlist Curators**
    - Maintain high-quality, clean playlists by identifying and removing duplicate or low-engagement tracks.
- **Data-Driven Listeners**
    - Gain deeper insights into listening habits by normalizing track metadata and library tags.

---

## Features
- **Intelligent Genre Tagging**
    - Automatically analyzes track audio features to assign accurate genre and mood tags for better searchability.
- **Automated Playlist Cleanup**
    - Scans existing playlists to identify and remove dead links, duplicates, or tracks that no longer fit the theme.
- **Real-time Spotify Sync**
    - Uses the Composio Toolset to ensure your library changes are reflected instantly across all your Spotify-connected devices.
- **Smart Metadata Normalization**
    - Standardizes artist names, album titles, and release years to maintain a pristine and searchable library structure.
- **Mood-Based Sorting**
    - Groups tracks into dynamic playlists based on energy, valence, and tempo metrics provided by the Spotify API.

---

## Use Cases
**Library Maintenance**
- Automatically move unsorted "Liked Songs" into structured folders based on release date or genre.
- Identify and archive tracks that haven't been played in over 12 months to declutter your main library.

**Playlist Curation**
- Generate "Focus" or "Workout" playlists by filtering tracks with specific BPM ranges and energy levels.
- Sync your local music discovery folders with public Spotify playlists to keep your collection updated.

**Metadata Hygiene**
- Fix inconsistent artist naming conventions (e.g., "The Beatles" vs "Beatles, The") across your entire saved library.
- Flag tracks with missing metadata or incomplete album information for manual review.

---

## Quick Start
### 1) Import the Flow into Uplizd
1. Click the "Run on Uplizd" badge to open the solution template.
2. Select your preferred workspace and project destination.
3. Authenticate your Spotify account via the Composio connection prompt.
4. Ensure nodes are correctly connected: Chat Input → Agent → Composio Toolset → Chat Output.

### 2) Setup the Nodes
- **Chat Input**: Receives your natural language command (e.g., "Sort my library by genre").
- **Agent**: Interprets the intent and orchestrates the necessary Spotify API calls.
- **Composio Toolset**: Executes the specific Spotify actions like `get_playlist`, `add_to_playlist`, or `remove_tracks`.
- **Chat Output**: Returns a summary of the actions taken and the current status of your library.

### 3) Run the Flow
Open the Playground and try these prompts:
- `Sort my 'Liked Songs' into playlists based on their primary genre.`
- `Find all duplicate tracks in my 'Workout' playlist and remove them.`
- `Create a new playlist called 'Chill Vibes' and add all tracks with a tempo under 90 BPM.`

---

## Configuration
### 1) Language Model (Agent Node)
The Agent requires a clear instruction set to handle music data effectively.
- Prioritize accuracy when matching track metadata to genre categories.
- Always confirm with the user before performing bulk delete operations.
- Ensure the agent maintains a consistent naming convention for all newly created playlists.

### 2) Composio Toolset Node
- **API Key**: Ensure your Spotify developer credentials are linked within the Composio dashboard.
- **Connection Scope**: Grant `playlist-modify-private`, `playlist-read-private`, and `user-library-read` permissions for full functionality.

### 3) Tool Availability
- `spotify_get_user_saved_tracks`: Fetches your library data for analysis.
- `spotify_create_playlist`: Generates new containers for your organized music.
- `spotify_add_tracks_to_playlist`: Populates playlists based on agent logic.
- `spotify_remove_tracks_from_playlist`: Cleans up unwanted or duplicate content.

---

## Related Solutions
- [../workout-music-optimizer-by-spotify/README.md](../workout-music-optimizer-by-spotify/README.md) - Optimize your exercise playlists with high-energy track selection.
- [../you-tube-content-performance-optimizer-by-youtube/README.md](../you-tube-content-performance-optimizer-by-youtube/README.md) - Manage and optimize media content performance metrics.
- [../account-reconciliation-helper-by-quickbooks/README.md](../account-reconciliation-helper-by-quickbooks/README.md) - Automate data matching and reconciliation tasks for financial records.
