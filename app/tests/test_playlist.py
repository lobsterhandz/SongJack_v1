import unittest
from app.models import Playlist, Song

class TestPlaylist(unittest.TestCase):
    # Task 1: Setup Test Environment
    def setUp(self):
        self.playlist = Playlist("Test Playlist")
        self.song1 = Song("Song A", "Artist 1", "Pop", 210, "songs/song1.mp3")
        self.song2 = Song("Song B", "Artist 2", "Rock", 180, "songs/song2.mp3")
        self.song3 = Song("Song C", "Artist 3", "Jazz", 200, "songs/song3.mp3")

    # Task 2: Test Adding Songs
    def test_add_song(self):
        self.playlist.add_song(self.song1)
        self.assertIn(self.song1, self.playlist.get_songs())

    # Task 3: Test Removing Songs
    def test_remove_song(self):
        self.playlist.add_song(self.song1)
        self.playlist.remove_song(self.song1)
        self.assertNotIn(self.song1, self.playlist.get_songs())

    # Task 4: Test Sorting by Title
    def test_sort_by_title(self):
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song1)
        self.playlist.sort_by_title()
        self.assertEqual(self.playlist.get_songs()[0], self.song1)

    # Task 5: Test Sorting by Artist
    def test_sort_by_artist(self):
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song1)
        self.playlist.sort_by_artist()
        self.assertEqual(self.playlist.get_songs()[0], self.song1)

    # Task 6: Test Sorting by Genre
    def test_sort_by_genre(self):
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song1)
        self.playlist.sort_by_genre()
        self.assertEqual(self.playlist.get_songs()[0], self.song1)

    # Task 7: Test Playlist Representation
    def test_playlist_repr(self):
        self.playlist.add_song(self.song1)
        self.assertEqual(repr(self.playlist), "Playlist: Test Playlist (1 songs)")

if __name__ == "__main__":
    unittest.main()
