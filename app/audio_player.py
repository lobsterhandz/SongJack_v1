import pygame
import os

# Task 1: Initialize Audio Player
class AudioPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.current_track = None

    # Task 2: Play Song
    def play_song(self, filename):
        filepath = os.path.join(self.music_folder, filename)
        if os.path.exists(filepath):
            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()
            self.current_track = filename
            print(f"Playing: {filename}")
        else:
            print(f"File {filename} not found!")

    # Task 3: Stop Song
    def stop_song(self):
        pygame.mixer.music.stop()
        self.current_track = None
        print("Music stopped.")

    # Task 4: Pause Song
    def pause_song(self):
        pygame.mixer.music.pause()
        print("Music paused.")

    # Task 5: Resume Song
    def resume_song(self):
        pygame.mixer.music.unpause()
        print("Music resumed.")

    # Task 6: Check if Song is Playing
    def is_playing(self):
        return pygame.mixer.music.get_busy()

# Task 7: Example Usage
if __name__ == "__main__":
    music_folder = "songs"  # Change to your music folder path
    player = AudioPlayer(music_folder)

    # Test functions
    player.play_song("song1.mp3")
    input("Press Enter to pause...")
    player.pause_song()

    input("Press Enter to resume...")
    player.resume_song()

    input("Press Enter to stop...")
    player.stop_song()

    print("Is playing:", player.is_playing())
