import requests
import time
import random

# Task 1: Configuration
BASE_URL = "https://musicbrainz.org/ws/2/"
HEADERS = {
    "User-Agent": "SongJack/1.0 (contact@example.com)"
}

# Task 2: Retry Logic with Rate Limiting

def fetch_with_retry(endpoint, params):
    """
    Fetch data with retry logic to handle rate limits.
    :param endpoint: API endpoint (e.g., 'artist/' or 'recording/')
    :param params: Query parameters
    :return: JSON response or error message
    """
    attempts = 0
    while attempts < 5:  # Retry up to 5 times
        response = requests.get(BASE_URL + endpoint, headers=HEADERS, params=params)
        if response.status_code == 200:
            return response.json()  # Success
        elif response.status_code == 503:  # Rate limited
            wait_time = random.uniform(1, 3)  # Random delay between 1-3 seconds
            print(f"Rate limit hit. Retrying in {wait_time:.2f} seconds...")
            time.sleep(wait_time)  # Wait before retrying
        else:
            response.raise_for_status()
        attempts += 1
    raise Exception("Failed after multiple attempts.")


# Task 3: Search Artist

def search_artist(artist_name):
    """
    Search for an artist by name using MusicBrainz API.
    :param artist_name: Name of the artist to search
    :return: JSON response containing artist details
    """
    params = {
        'query': artist_name,
        'fmt': 'json'
    }
    return fetch_with_retry("artist/", params)


# Task 4: Search Recording

def search_recording(recording_title):
    """
    Search for a recording by title using MusicBrainz API.
    :param recording_title: Title of the recording to search
    :return: JSON response containing recording details
    """
    params = {
        'query': recording_title,
        'fmt': 'json'
    }
    return fetch_with_retry("recording/", params)


# Task 5: Example Usage
if __name__ == "__main__":
    artist_name = input("Enter artist name: ")
    try:
        artist_results = search_artist(artist_name)
        print("Artist Search Results:", artist_results)
    except Exception as e:
        print("Error fetching artist details:", e)

    recording_title = input("Enter recording title: ")
    try:
        recording_results = search_recording(recording_title)
        print("Recording Search Results:", recording_results)
    except Exception as e:
        print("Error fetching recording details:", e)
