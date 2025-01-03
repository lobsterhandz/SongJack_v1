import unittest
from app.models import Song
from app.utils import binary_search_songs, quicksort_songs

class TestUtils(unittest.TestCase):
    # Task 1: Setup Test Environment
    def setUp(self):
        self.song1 = Song("Song A", "Artist 1", "Pop", 210, "songs/song1.mp3")
        self.song2 = Song("Song B", "Artist 2", "Rock", 180, "songs/song2.mp3")
        self.song3 = Song("Song C", "Artist 3", "Jazz", 200, "songs/song3.mp3")
        self.songs = [self.song3, self.song1, self.song2]  # Unsorted list

    # Task 2: Test Quicksort
    def test_quicksort_by_title(self):
        sorted_songs = quicksort_songs(self.songs, 'title')
        self.assertEqual([song.title for song in sorted_songs], ["Song A", "Song B", "Song C"])

    def test_quicksort_by_artist(self):
        sorted_songs = quicksort_songs(self.songs, 'artist')
        self.assertEqual([song.artist for song in sorted_songs], ["Artist 1", "Artist 2", "Artist 3"])

    def test_quicksort_by_genre(self):
        sorted_songs = quicksort_songs(self.songs, 'genre')
        self.assertEqual([song.genre for song in sorted_songs], ["Jazz", "Pop", "Rock"])

    # Task 3: Test Binary Search
    def test_binary_search_found(self):
        sorted_songs = quicksort_songs(self.songs, 'title')
        result = binary_search_songs(sorted_songs, "Song B")
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Song B")

    def test_binary_search_not_found(self):
        sorted_songs = quicksort_songs(self.songs, 'title')
        result = binary_search_songs(sorted_songs, "Song Z")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
