import unittest
import os
from app.audio_player import AudioPlayer

class TestAudioPlayer(unittest.TestCase):
    # Task 1: Setup Test Environment
    def setUp(self):
        self.music_folder = "test_songs"
        os.makedirs(self.music_folder, exist_ok=True)
        self.test_file = os.path.join(self.music_folder, "test_song.mp3")
        # Create a dummy file to simulate an audio track
        with open(self.test_file, "wb") as f:
            f.write(b"\x00" * 1024)
        self.player = AudioPlayer(self.music_folder)

    # Task 2: Test Play Song
    def test_play_song(self):
        self.player.play_song("test_song.mp3")
        self.assertEqual(self.player.current_track, "test_song.mp3")

    # Task 3: Test Pause Song
    def test_pause_song(self):
        self.player.play_song("test_song.mp3")
        self.player.pause_song()
        self.assertFalse(self.player.is_playing())

    # Task 4: Test Resume Song
    def test_resume_song(self):
        self.player.play_song("test_song.mp3")
        self.player.pause_song()
        self.player.resume_song()
        self.assertTrue(self.player.is_playing())

    # Task 5: Test Stop Song
    def test_stop_song(self):
        self.player.play_song("test_song.mp3")
        self.player.stop_song()
        self.assertIsNone(self.player.current_track)

    # Task 6: Cleanup Test Environment
    def tearDown(self):
        self.player.stop_song()
        os.remove(self.test_file)
        os.rmdir(self.music_folder)

if __name__ == "__main__":
    unittest.main()
