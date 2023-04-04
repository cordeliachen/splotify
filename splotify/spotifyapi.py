"""`SpotifyApi` class.

This module contains the `SpotifyApi` class that interacts with the Spotify Web
API to fetch your Spotify data.

"""

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyApi:
    """Object to fetch Spotify data.

    Interacts with the Spotify Web API to fetch your Spotify data. When
    initialized for the first time, you will need to paste in the URI you were
    directed to. This `SpotifyAPI` object is passed into various functions that
    need to access Spotify data.

    Args:
        client_id (str): SPOTIPY_CLIENT_ID from Spotify developer app you
            created.
        client_secret (str): SPOTIPY_CLIENT_SECRET from Spotify developer app
            you created.
        redirect_uri (str): SPOTIPY_REDIRECT_URI from Spotify developer app you
            created.

    """

    def __init__(self, client_id, client_secret, redirect_uri):
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

        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(scope=scope, open_browser=False)
        )

    def search(self, query, limit, type):
        return self.sp.search(q=query, limit=limit, type=type)

    def current_user_playlists(self):
        return self.sp.current_user_playlists()

    def track(self, id):
        return self.sp.track(id)

    def album(self, id):
        return self.sp.album(id)

    def playlist(self, id):
        return self.sp.playlist(id)

    def audio_features(self, id):
        return self.sp.audio_features(id)
