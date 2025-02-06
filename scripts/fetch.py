import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

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
        print(track)
        if track is not None:  # Check if the track is not None
            song_title = track['name']
            artist_names = ", ".join([artist['name'] for artist in track['artists']])  # Join artists with a comma
            playlist_data.append([artist_names, song_title])  # Artist first, then title
    
    return playlist_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')  # Fixed delimiter as '-'
        # Write header
        writer.writerow(['Artists', 'Song Title'])  # Header updated to match order
        # Write data
        writer.writerows(data)

if __name__ == "__main__":
    playlist_url = input("Enter the Spotify playlist URL: ")
    playlist_data = get_playlist_tracks(playlist_url)
    
    # Save to CSV with fixed delimiter '-'
    save_to_csv(playlist_data, 'playlist_data.csv')
    print("Playlist data saved to 'playlist_data.csv'")