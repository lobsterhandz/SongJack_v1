# config.py - Configuration Settings

# Task 1: Flask Configuration
UPLOAD_FOLDER = 'songs/'  # Folder to store uploaded songs
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit file uploads to 16 MB

# Task 2: MusicBrainz API Configuration
MUSICBRAINZ_BASE_URL = "https://musicbrainz.org/ws/2/"
MUSICBRAINZ_HEADERS = {
    "User-Agent": "SongJack/1.0 (contact@example.com)"
}

# Task 3: Debug Mode
DEBUG = True  # Set to False in production

# Task 4: Example Environment Variables (Optional for Future Enhancements)
# SECRET_KEY = "your_secret_key_here"
# DATABASE_URL = "sqlite:///songjack.db"
