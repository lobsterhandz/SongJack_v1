# utils.py - Utility functions for sorting, searching, and algorithms

# Task 1: Binary Search for Songs

def binary_search_songs(songs, target_title):
    """
    Perform binary search on a sorted list of songs by title.
    :param songs: List of Song objects sorted by title
    :param target_title: Title of the song to search for
    :return: The Song object if found, else None
    """
    low, high = 0, len(songs) - 1
    while low <= high:
        mid = (low + high) // 2
        if songs[mid].title == target_title:
            return songs[mid]
        elif songs[mid].title < target_title:
            low = mid + 1
        else:
            high = mid - 1
    return None


# Task 2: Quicksort for Songs

def quicksort_songs(songs, key):
    """
    Sort songs based on a specified key (title, artist, genre).
    :param songs: List of Song objects
    :param key: Attribute to sort by (title, artist, genre)
    :return: Sorted list of songs
    """
    if len(songs) <= 1:
        return songs
    pivot = songs[0]
    less = [song for song in songs[1:] if getattr(song, key) <= getattr(pivot, key)]
    greater = [song for song in songs[1:] if getattr(song, key) > getattr(pivot, key)]
    return quicksort_songs(less, key) + [pivot] + quicksort_songs(greater, key)


# Task 3: Example Usage and Testing
if __name__ == "__main__":
    from app.models import Song

    # Example Songs
    song1 = Song("Song A", "Artist 1", "Pop", 210, "songs/song1.mp3")
    song2 = Song("Song B", "Artist 2", "Rock", 180, "songs/song2.mp3")
    song3 = Song("Song C", "Artist 3", "Jazz", 200, "songs/song3.mp3")

    songs = [song1, song2, song3]

    # Sort songs by title
    sorted_songs = quicksort_songs(songs, 'title')
    print("Sorted by title:", [song.title for song in sorted_songs])

    # Binary search for a song
    result = binary_search_songs(sorted_songs, "Song B")
    print("Found song:", result)
