"""`Data` class.

This module contains the `Data` class that stores the tracks you want to plot.

"""

from tqdm import tqdm
import pandas as pd


class Data:
    """Object to store the tracks you want to plot.

    Add all the tracks you want to view together in a single plot to a `Data`
    instance.

    Args:
        sp (splotify.spotifyapi.SpotifyApi): A `SpotifyApi` instance.

    """

    def __init__(self, sp):
        self.data = []
        self.sp = sp

    def add_track(self, id):
        """Adds a single track to a `Data` instance.

        Args:
            id (str): The URI of the track you want to add. Supports Spotify
                URIs, Spotify URLs, and Spotify IDs.

        """
        result = self.sp.track(id)
        self.data.append(result)
        return result

    def add_tracks(self, ids):
        """Adds multiple tracks to a `Data` instance.

        Args:
            ids (:obj:`list` of :obj:`str`): The URIs of the tracks you want to
                add. Supports Spotify URIs, Spotify URLs, and Spotify IDs.

        """
        result = []
        for id in tqdm(ids, desc="Adding tracks"):
            result.append(self.add_track(id))
        return result

    def add_album(self, id):
        """Adds all the tracks on a single album to a `Data` instance.

        Args:
            id (str): The URI of the album you want to add. Supports Spotify
                URIs, Spotify URLs, and Spotify IDs.

        """
        result = []
        tracks = self.sp.album(id)["tracks"]["items"]
        for track in tqdm(tracks, desc="Adding album"):
            self.add_track(track["uri"])
            result.append(track)
        return result

    def add_albums(self, ids):
        """Adds all the tracks on multiple albums to a `Data` instance.

        Args:
            ids (:obj:`list` of :obj:`str`): The URIs of the albums you want to
                add. Supports Spotify URIs, Spotify URLs, and Spotify IDs.

        """
        for id in tqdm(ids, desc="Adding albums"):
            self.add_album(id)

    def add_playlist(self, id):
        """Adds the tracks on a single playlist to a `Data` instance.

        Only adds the most recently added 100 songs of a playlist.

        Args:
            id (str): The URI of the playlist you want to add. Supports Spotify
                URIs, Spotify URLs, and Spotify IDs.

        """
        result = []
        tracks = self.sp.playlist(id)["tracks"]["items"]
        for track in tqdm(tracks, desc="Adding playlist"):
            self.add_track(track["track"]["uri"])
            result.append(track)
        return result

    def add_playlists(self, ids):
        """Adds the tracks on multiple playlists to a `Data` instance.

        Only adds the most recently added 100 songs of a playlist.

        Args:
            ids (:obj:`list` of :obj:`str`): The URIs of the playlists you want
                to add. Supports Spotify URIs, Spotify URLs, and Spotify IDs.

        """
        for id in tqdm(ids, desc="Adding playlists"):
            self.add_playlist(id)

    def get_data(self):
        """Returns all the tracks in a `Data` instance as a Pandas Dataframe

        The returned Dataframe should be passed in while initializing the plot
        classes, not the Data object itself.

        Returns:
            A Pandas Dataframe containing the track data added to the `Data`
            instance with the columns ["name", "artist", "album", "uri"].

        """
        data = []

        for track in tqdm(self.data, desc="Creating DataFrame"):
            track_data = []
            track_data.append(track["name"])
            track_data.append(track["artists"][0]["name"])
            track_data.append(track["album"]["name"])
            track_data.append(track["uri"])
            data.append(track_data)

        return pd.DataFrame(data, columns=["name", "artist", "album", "uri"])
