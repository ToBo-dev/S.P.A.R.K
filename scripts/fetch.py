import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import json
from download import *

CLIENT_ID = '14b9c55513d344b48226972ef7e7b628'
CLIENT_SECRET = '16880cd68c6a4323a863999ac7d691ee'


# Authenticate with Spotify
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_playlist_tracks(playlist_url):
    # Extract playlist ID from URL
    playlist_id = playlist_url.split('/')[-1].split('?')[0]
    
    # Get playlist tracks
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    # Extract artist names and song titles
    playlist_data = []
    for item in tracks:
        track = item['track']
        if track is not None:  # Check if the track is not None
            song_title = track['name']
            album = track['album']['name']
            artist_names = track['artists'][0]['name']  # Get the main artist's name
            playlist_data.append({'artist': artist_names, 'song': song_title, 'album': album})  # JSON object
    
    return playlist_data


if __name__ == "__main__":
    playlist_url = input("Enter the Spotify playlist URL: ")
    playlist_data = get_playlist_tracks(playlist_url)

    asyncio.run(downloadFiles(playlist_data))