"""`AudioFeaturesPlot` class.

This module contains the `AudioFeaturesPlot` class that plots the audio
features of your selected tracks.

"""

import plotly.express as px
import pandas as pd
from tqdm import tqdm


class AudioFeaturesPlot:
    """Object to plot the audio features of a group of tracks.

    Supports 2D and 3D scatter plots, histograms, and box plots. The supported
    features are:

    "acousticness",
    "danceability",
    "duration_ms",
    "energy",
    "instrumentalness",
    "key",
    "liveness",
    "loudness",
    "mode",
    "speechiness",
    "tempo",
    "time_signature",
    "valence"

    These features are explained further in the `Spotify Web API documentation
    <https://developer.spotify.com/documentation/web-api/reference/get-audio-features>`_.

    Args:
        sp (splotify.spotifyapi.SpotifyApi): A `SpotifyApi` instance.
        data (splotify.data.Data): A `Data` instance.
        features(:obj:`list` of :obj:`str`): The list of audio features
            that you want to plot. If len(features) > 3, only the first 3
            features in the list will be selected.

    """

    def __init__(self, sp, data, features):
        self.df = data.get_data()
        self.sp = sp
        self.add_features()
        self.select_features(features)

    def add_features(self):
        data = []
        for id in tqdm(self.df["uri"].values, desc="Adding features"):
            audio_features = self.sp.audio_features(id)[0]
            features = [
                "acousticness",
                "danceability",
                "duration_ms",
                "energy",
                "instrumentalness",
                "key",
                "liveness",
                "loudness",
                "mode",
                "speechiness",
                "tempo",
                "time_signature",
                "valence",
            ]
            track_data = [audio_features.get(feature) for feature in features]
            data.append(track_data)
        self.fs = pd.DataFrame(data, columns=features)
        self.df = pd.concat([self.df, self.fs], axis=1)

    def select_features(self, features):
        """Selects the audio features you want to plot.

        Args:
            features(:obj:`list` of :obj:`str`): The list of audio features
                that you want to plot. If len(features) > 3, only the first 3
                features in the list will be selected.

        """
        if len(features) > 0:
            self.f1 = features[0]
        else:
            self.f1 = None

        if len(features) > 1:
            self.f2 = features[1]
        else:
            self.f2 = None

        if len(features) > 2:
            self.f3 = features[2]
        else:
            self.f3 = None

    def get_features(self):
        """Returns the currently selected audio features."""
        return [self.f1, self.f2, self.f3]

    def scatter_plot_2d(self, color=None):
        """Plots the tracks in a 2D scatter plot by the first 2 selected audio
        features.

        Args:
            color (:obj:`str`, optional): What the color of the points on the
                plot represent. Currently only supports 'artist' and 'album'.
                Defaults to 'None'.

        """
        fig = px.scatter(
            self.df,
            x=self.f1,
            y=self.f2,
            color=color,
            custom_data=["name", "artist", "album"],
        )

        fig.update_traces(
            hovertemplate="<br>".join(
                [
                    "name: %{customdata[0]}",
                    "artist: %{customdata[1]}",
                    "album: %{customdata[2]}",
                ]
            )
        )
        fig.show()

        return fig

    def scatter_plot_3d(self, color=None):
        """Plots the tracks in a 3D scatter plot by the first 3 selected audio
        features.

        Args:
            color (:obj:`str`, optional): What the color of the points on the
                plot represent. Currently only supports 'artist' and 'album'.
                Defaults to 'None'.

        """
        fig = px.scatter_3d(
            self.df,
            x=self.f1,
            y=self.f2,
            z=self.f3,
            color=color,
            custom_data=["name", "artist", "album"],
        )

        fig.update_traces(
            hovertemplate="<br>".join(
                [
                    "name: %{customdata[0]}",
                    "artist: %{customdata[1]}",
                    "album: %{customdata[2]}",
                ]
            )
        )
        fig.show()

        return fig

    def scatter_plot_2d_average(self, groupby="album"):
        """Plots the averages of tracks in a 2D scatter plot by the first 2
        selected audio features.

        Groups the tracks based on the `groupby` parameter, computes the
        averages of each audio feature for each group, and plots the averages.

        Args:
            groupby (:obj:`str`): What to group the tracks by. Currently only
                supports 'artist' and 'album'. Defaults to 'album'.

        """
        avg_df = (
            pd.concat([self.df.loc[:, groupby], self.fs], axis=1)
            .groupby(groupby, as_index=False)
            .mean()
        )
        fig = px.scatter(
            avg_df,
            x=self.f1,
            y=self.f2,
            color=groupby,
            custom_data=[groupby],
        )

        fig.update_traces(
            hovertemplate="<br>".join(
                [
                    groupby + ": %{customdata[0]}",
                ]
            )
        )
        fig.show()

        return fig

    def scatter_plot_3d_average(self, groupby="album"):
        """Plots the averages of tracks in a 3D scatter plot by the first 3
        selected audio features.

        Groups the tracks based on the `groupby` parameter, computes the
        averages of each audio feature for each group, and plots the averages.

        Args:
            groupby (:obj:`str`): What to group the tracks by. Currently only
                supports 'artist' and 'album'. Defaults to 'album'.

        """

        avg_df = (
            pd.concat([self.df.loc[:, groupby], self.fs], axis=1)
            .groupby(groupby, as_index=False)
            .mean()
        )

        fig = px.scatter_3d(
            avg_df,
            x=self.f1,
            y=self.f2,
            z=self.f3,
            color=groupby,
            custom_data=[groupby],
        )

        fig.update_traces(
            hovertemplate="<br>".join(
                [
                    groupby + ": %{customdata[0]}",
                ]
            )
        )
        fig.show()

        return fig

    def histogram(self, feature, color=None):
        """Plots the tracks in a histogram by the selected audio feature.

        Args:
            feature (str): The audio feature you want to plot.
            color (:obj:`str`, optional): What the color of the points on the
                plot represent. Currently only supports 'artist' and 'album'.
                Defaults to 'None'.

        """
        fig = px.histogram(self.df, x=feature, color=color)
        fig.show()

        return fig

    def box_plot(self, feature, groupby=None):
        """Plots the tracks in a box plot by the selected audio feature.

        Setting the `groupby` parameter will plot each resulting group as a
        separate box plot.

        Args:
            feature (str): The audio feature you want to plot.
            groupby (:obj:`str`, optional): What to group the tracks by.
                Currently only supports 'artist' and 'album'. Defaults to
                'None'.

        """
        fig = px.box(
            self.df,
            x=groupby,
            y=feature,
            color=groupby,
            points="all",
            custom_data=["name", "artist", "album"],
        )

        fig.update_traces(
            hovertemplate="<br>".join(
                [
                    "name: %{customdata[0]}",
                    "artist: %{customdata[1]}",
                    "album: %{customdata[2]}",
                ]
            )
        )
        fig.show()

        return fig
