# database.py - Simulated database for storing playlists and songs

from app.models import Song, Playlist

# Task 1: Initialize Storage
songs_db = []  # List to store Song objects
playlists_db = {}  # Dictionary to store Playlist objects by name

# Task 2: Add Song to Database
def add_song_to_db(song):
    """
    Add a song to the database.
    :param song: Song object
    """
    songs_db.append(song)

# Task 3: Get Song by Title
def get_song_by_title(title):
    """
    Retrieve a song by its title.
    :param title: Title of the song
    :return: Song object or None
    """
    for song in songs_db:
        if song.title == title:
            return song
    return None

# Task 4: Add Playlist to Database
def add_playlist_to_db(playlist):
    """
    Add a playlist to the database.
    :param playlist: Playlist object
    """
    playlists_db[playlist.name] = playlist

# Task 5: Get Playlist by Name
def get_playlist_by_name(name):
    """
    Retrieve a playlist by its name.
    :param name: Name of the playlist
    :return: Playlist object or None
    """
    return playlists_db.get(name)

# Task 6: Example Usage
if __name__ == "__main__":
    # Create songs
    song1 = Song("Song A", "Artist 1", "Pop", 210, "songs/song1.mp3")
    song2 = Song("Song B", "Artist 2", "Rock", 180, "songs/song2.mp3")

    # Add songs to database
    add_song_to_db(song1)
    add_song_to_db(song2)

    # Test song retrieval
    print("Get Song A:", get_song_by_title("Song A"))

    # Create and add playlist
    playlist = Playlist("My Playlist")
    playlist.add_song(song1)
    playlist.add_song(song2)
    add_playlist_to_db(playlist)

    # Test playlist retrieval
    print("Get Playlist:", get_playlist_by_name("My Playlist"))
