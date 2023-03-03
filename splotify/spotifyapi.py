import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_sp(client_id, client_secret, redirect_uri):
    os.environ["SPOTIPY_CLIENT_ID"] = client_id
    os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
    os.environ["SPOTIPY_REDIRECT_URI"] = redirect_uri

    scope = """playlist-read-collaborative
        playlist-read-private
        playlist-modify-private
        playlist-modify-public
        user-follow-read
        user-follow-modify
        user-library-modify
        user-library-read
        user-modify-playback-state
        user-read-currently-playing
        user-read-playback-state
        user-read-playback-position
        user-read-private
        user-read-recently-played"""

    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
