from flask import Flask, request, jsonify
from app.models import Song, Playlist

app = Flask(__name__)

# Temporary storage for songs and playlists
songs = []
playlists = {}

# Task 1: CRUD Operations for Songs
@app.route('/song', methods=['POST'])
def create_song():
    data = request.get_json()
    song = Song(
        data['title'],
        data['artist'],
        data['genre'],
        data['duration'],
        data['file_path']
    )
    songs.append(song)
    return jsonify({'message': 'Song created successfully', 'song': repr(song)}), 201

@app.route('/song/<title>', methods=['GET'])
def get_song(title):
    for song in songs:
        if song.title == title:
            return jsonify({'song': repr(song)}), 200
    return jsonify({'error': 'Song not found'}), 404

@app.route('/song/<title>', methods=['DELETE'])
def delete_song(title):
    global songs
    songs = [song for song in songs if song.title != title]
    return jsonify({'message': 'Song deleted successfully'}), 200

# Task 2: CRUD Operations for Playlists
@app.route('/playlist', methods=['POST'])
def create_playlist():
    data = request.get_json()
    name = data['name']
    playlists[name] = Playlist(name)
    return jsonify({'message': f'Playlist "{name}" created successfully'}), 201

@app.route('/playlist/<name>', methods=['GET'])
def get_playlist(name):
    playlist = playlists.get(name)
    if playlist:
        return jsonify({'playlist': repr(playlist), 'songs': [repr(song) for song in playlist.get_songs()]}), 200
    return jsonify({'error': 'Playlist not found'}), 404

@app.route('/playlist/<name>', methods=['DELETE'])
def delete_playlist(name):
    if name in playlists:
        del playlists[name]
        return jsonify({'message': 'Playlist deleted successfully'}), 200
    return jsonify({'error': 'Playlist not found'}), 404

# Task 3: Add/Remove Songs in Playlist
@app.route('/playlist/<name>/add', methods=['POST'])
def add_song_to_playlist(name):
    data = request.get_json()
    song_title = data['title']
    playlist = playlists.get(name)
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404

    for song in songs:
        if song.title == song_title:
            playlist.add_song(song)
            return jsonify({'message': 'Song added to playlist successfully'}), 200
    return jsonify({'error': 'Song not found'}), 404

@app.route('/playlist/<name>/remove', methods=['POST'])
def remove_song_from_playlist(name):
    data = request.get_json()
    song_title = data['title']
    playlist = playlists.get(name)
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404

    for song in playlist.get_songs():
        if song.title == song_title:
            playlist.remove_song(song)
            return jsonify({'message': 'Song removed from playlist successfully'}), 200
    return jsonify({'error': 'Song not found in playlist'}), 404

# Task 4: Sort Songs in Playlist
@app.route('/playlist/<name>/sort/<criteria>', methods=['POST'])
def sort_playlist(name, criteria):
    playlist = playlists.get(name)
    if not playlist:
        return jsonify({'error': 'Playlist not found'}), 404

    if criteria == 'title':
        playlist.sort_by_title()
    elif criteria == 'artist':
        playlist.sort_by_artist()
    elif criteria == 'genre':
        playlist.sort_by_genre()
    else:
        return jsonify({'error': 'Invalid sorting criteria'}), 400

    return jsonify({'message': f'Playlist sorted by {criteria}'}), 200

# Task 5: Run App
if __name__ == '__main__':
    app.run(debug=True)
