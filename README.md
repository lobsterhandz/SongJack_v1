# SongJack - Interactive Playlist Management System

**SongJack** is a fun and interactive music application that combines powerful algorithms and metadata integration to provide an exceptional music experience. It supports local audio playback, playlist management, and seamless integration with the MusicBrainz API for metadata retrieval.

SongJack_v1 is currently designed as a RESTful API backend, meaning you interact with it primarily through API endpoints rather than a graphical interface—at least for now!

---

## Features
1. **Playlist Management** - Create, update, and delete playlists easily.
2. **Song Management** - Add, remove, and sort songs by title, artist, and genre.
3. **Audio Playback** - Play, pause, resume, and stop songs stored locally in MP3/WAV format.
4. **Metadata Integration** - Fetch song and artist details using the MusicBrainz API.
5. **Advanced Search and Sort** - Leverage algorithms like quicksort and binary search for optimized performance.
6. **Interactive API** - Manage all features via RESTful API endpoints built with Flask.

---

## File Structure
```
SongJack/
├── app/
│   ├── __init__.py            # Initializes Flask app
│   ├── models.py              # Defines Song and Playlist classes
│   ├── routes.py              # Flask routes for API endpoints
│   ├── audio_player.py        # Handles local audio playback
│   ├── utils.py               # Sorting, searching, and algorithms
│   ├── musicbrainz_api.py     # MusicBrainz API integration
│   ├── database.py            # Simulated database
│   └── tests/                 # Unit tests for endpoints and features
│       ├── test_songs.py
│       ├── test_playlists.py
│       ├── test_audio_player.py
│       └── test_utils.py
├── songs/                     # Folder for storing local audio files
├── static/                    # Static assets (optional)
├── templates/                 # HTML templates (optional)
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
├── config.py                  # Configuration settings
└── run.py                     # Main entry point for Flask app
```

---

## Installation
1. **Clone the Repository**
```
git clone https://github.com/yourusername/SongJack.git
cd SongJack
```

2. **Create a Virtual Environment**
```
python3 -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Run the Application**
```
python run.py
```

---

## API Endpoints
### Song Endpoints
- **POST /song** - Add a new song.
- **GET /song/<title>** - Retrieve song details.
- **DELETE /song/<title>** - Delete a song.

### Playlist Endpoints
- **POST /playlist** - Create a new playlist.
- **GET /playlist/<name>** - Retrieve playlist details.
- **DELETE /playlist/<name>** - Delete a playlist.

### Additional Endpoints
- **POST /playlist/<name>/add** - Add a song to a playlist.
- **POST /playlist/<name>/remove** - Remove a song from a playlist.
- **POST /playlist/<name>/sort/<criteria>** - Sort a playlist by title, artist, or genre.
- **POST /play** - Play a song.
- **POST /pause** - Pause playback.
- **POST /resume** - Resume playback.
- **POST /stop** - Stop playback.

---

## Testing
Run unit tests for different modules:
```
python -m unittest discover -s app/tests
```

---

## Dependencies
- Flask
- pygame
- requests
- unittest

---

## Future Enhancements
1. Add support for online streaming.
2. Implement lyrics synchronization.
3. Enhance the UI with React or Vue.js for a modern interface.
4. Optimize performance with database integration.
5. Replace Flask's development server with a production-ready server like Gunicorn or uWSGI.
6. Remove `if __name__ == '__main__': app.run(debug=True)` blocks from scripts when preparing for deployment and rely on `run.py` for launching the app.

---

## License
This project is licensed under the MIT License.

---

## Author
**Jose Murillo** - [GitHub Profile](https://github.com/Lobsterhandz)

