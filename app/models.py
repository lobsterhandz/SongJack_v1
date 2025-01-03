# models.py - Defines Song and Playlist classes

# Task 1: Define Song Class
class Song:
    def __init__(self, title, artist, genre, duration, file_path):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration  # Duration in seconds
        self.file_path = file_path

    def __repr__(self):
        return f"{self.title} by {self.artist} ({self.genre}) - {self.duration}s"


# Task 2: Define Playlist Class
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def get_songs(self):
        return self.songs

    def sort_by_title(self):
        self.songs.sort(key=lambda song: song.title)

    def sort_by_artist(self):
        self.songs.sort(key=lambda song: song.artist)

    def sort_by_genre(self):
        self.songs.sort(key=lambda song: song.genre)

    def __repr__(self):
        return f"Playlist: {self.name} ({len(self.songs)} songs)"


# Example Usage (Temporary test code, remove before deployment):
if __name__ == "__main__":
    # Create Songs
    song1 = Song("Song A", "Artist 1", "Pop", 210, "songs/song1.mp3")
    song2 = Song("Song B", "Artist 2", "Rock", 180, "songs/song2.mp3")
    song3 = Song("Song C", "Artist 1", "Pop", 200, "songs/song3.mp3")

    # Create Playlist
    playlist = Playlist("My Playlist")
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)

    # Test Sorting
    print("Original Playlist:", playlist.get_songs())
    playlist.sort_by_title()
    print("Sorted by Title:", playlist.get_songs())
    playlist.sort_by_artist()
    print("Sorted by Artist:", playlist.get_songs())
    playlist.sort_by_genre()
    print("Sorted by Genre:", playlist.get_songs())
