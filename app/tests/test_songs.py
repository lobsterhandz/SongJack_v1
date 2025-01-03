import unittest
from app.models import Song

class TestSong(unittest.TestCase):
    # Task 1: Setup Test Environment
    def setUp(self):
        self.song = Song("Song A", "Artist 1", "Pop", 210, "songs/song1.mp3")

    # Task 2: Test Song Initialization
    def test_song_initialization(self):
        self.assertEqual(self.song.title, "Song A")
        self.assertEqual(self.song.artist, "Artist 1")
        self.assertEqual(self.song.genre, "Pop")
        self.assertEqual(self.song.duration, 210)
        self.assertEqual(self.song.file_path, "songs/song1.mp3")

    # Task 3: Test Song Representation
    def test_song_repr(self):
        self.assertEqual(repr(self.song), "Song A by Artist 1 (Pop) - 210s")

if __name__ == "__main__":
    unittest.main()
