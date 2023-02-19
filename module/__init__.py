import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
