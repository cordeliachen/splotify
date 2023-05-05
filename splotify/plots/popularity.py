# TODO: call Data.get_data() during __init__.

"""`PopularityPlot` class.

This module contains the `PopularityPlot` class that plots the popularity of your
selected tracks.

"""

import plotly.express as px
import pandas as pd
from tqdm import tqdm


class PopularityPlot:
    """Object to plot the popularity of a group of tracks.

    Supports bar charts. Based on Spotify's `popularity` variable for `tracks
    <https://developer.spotify.com/documentation/web-api/reference/get-track>`_
    and `albums
    <https://developer.spotify.com/documentation/web-api/reference/get-an-album>`_.

    Args:
        sp (splotify.spotifyapi.SpotifyApi): A `SpotifyApi` instance.
        data (splotify.data.Data): A `Data` instance.

    """

    def __init__(self, sp, data):
        self.df = data.get_data()
        self.sp = sp

    def track_bar_chart(self):
        """Plots the popularity of tracks in a bar chart."""

        data = []
        for id in tqdm(self.df["uri"].values, desc="Adding track popularity"):
            popularity = self.sp.track(id)["popularity"]
            data.append(popularity)
        track_df = pd.concat(
            [self.df["name"], pd.DataFrame(data, columns=["popularity"])], axis=1
        )

        track_df.drop_duplicates()

        fig = px.bar(track_df, x="name", y="popularity")
        fig.show()
        return fig

    def album_bar_chart(self):
        """Plots the popularity of albums present in a group of tracks in a bar
        chart."""

        data = []
        for id in tqdm(self.df["uri"].values, desc="Adding album popularity"):
            popularity = self.sp.album(self.sp.track(id)["album"]["uri"])["popularity"]
            data.append(popularity)
        album_df = pd.concat(
            [self.df["album"], pd.DataFrame(data, columns=["popularity"])], axis=1
        )

        album_df.drop_duplicates()

        fig = px.bar(album_df, x="album", y="popularity")
        fig.show()
        return fig
