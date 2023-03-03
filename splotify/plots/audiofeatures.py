import plotly.express as px
import pandas as pd
from tqdm import tqdm

# Generate plots to view the audio features of tracks


class AudioFeaturesPlot:
    def __init__(self, sp, tracks, features, dims=2):
        self.dims = dims
        self.df = tracks
        self.sp = sp
        self.add_features(features)
        self.select_features(features)

    def add_features(self, features):
        data = []
        for uri in tqdm(self.df["uri"].values, desc="Adding features"):
            track_data = []
            audio_features = self.sp.audio_features(uri)[0]
            for feature in features:
                track_data.append(audio_features[feature])
            data.append(track_data)
        fs = pd.DataFrame(data, columns=features)
        self.df = pd.concat([self.df, fs], axis=1)

    def select_features(self, features):
        if len(features) > 0:
            self.f1 = features[0]
            print(len(features))
        if len(features) > 1:
            self.f2 = features[1]
        if len(features) > 2:
            self.f3 = features[2]

    def get_df(self):
        return self.df

    def get_features(self):
        return [self.f1, self.f2, self.f3]

    def scatter_plot_2d(self, color=None):
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

    def histogram(self, feature, color=None):
        fig = px.histogram(self.df, x=feature, color=color)
        fig.show()

        return fig

    # def box_plot()

    # def scatter_plot_2d_average(type='album'):
