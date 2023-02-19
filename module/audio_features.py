from __init__ import sp
import plotly.express as px
import pandas as pd
from tqdm import tqdm

# Generate plots to view the audio features of tracks


class AudioFeaturesPlot:
    def __init__(self, tracks, feature1, feature2=None, feature3=None, dims=2):
        self.f1 = feature1
        self.f2 = feature2
        self.f3 = feature3
        self.dims = dims
        self.df = self.add_data(tracks, dims)

    def add_data(self, tracks, dims):
        data = []

        for track in tqdm(tracks, desc='Preparing to graph'):
            track_data = []
            track_data.append(track['name'])
            track_data.append(track['artists'][0]['name'])
            track_data.append(track['album']['name'])
            track_data.append(track['uri'])

            audio_features = sp.audio_features(track['uri'])[0]

            track_data.append(audio_features[self.f1])
            if dims > 1:
                track_data.append(audio_features[self.f2])
            if dims > 2:
                track_data.append(audio_features[self.f3])
            data.append(track_data)

        if dims == 1:
            df = pd.DataFrame(
                data, columns=['name', 'artist', 'album', 'uri', self.f1])
        elif dims == 2:
            df = pd.DataFrame(
                data, columns=['name', 'artist', 'album', 'uri', self.f1, self.f2])
        elif dims == 3:
            df = pd.DataFrame(
                data, columns=['name', 'artist', 'album', 'uri', self.f1, self.f2, self.f3])
        return df

    def add_features(self, features):
        data = []
        for uri in tqdm(self.df['uri'].values, desc='Adding features'):
            track_data = []
            audio_features = sp.audio_features(uri)[0]
            for feature in features:
                track_data.append(audio_features[feature])
            data.append(track_data)
        fs = pd.DataFrame(data, columns=features)
        self.df = pd.concat([self.df, fs], axis=1)

    def select_features(self, features):
        if len(features) > 0:
            self.f1 = features[0]
        elif len(features) > 1:
            self.f2 = features[1]
        elif len(features) > 2:
            self.f3 = features[2]

    def scatter_plot_2d(self, color=None):
        fig = px.scatter(self.df, x=self.f1, y=self.f2, color=color,
                         custom_data=['name', 'artist', 'album'])

        fig.update_traces(
            hovertemplate="<br>".join([
                "name: %{customdata[0]}",
                "artist: %{customdata[1]}",
                "album: %{customdata[2]}",
            ])
        )
        fig.show()

    def scatter_plot_3d(self, color=None):
        fig = px.scatter_3d(self.df, x=self.f1, y=self.f2, z=self.f3,
                            color=color, custom_data=['name', 'artist', 'album'])

        fig.update_traces(
            hovertemplate="<br>".join([
                "name: %{customdata[0]}",
                "artist: %{customdata[1]}",
                "album: %{customdata[2]}",
            ])
        )
        fig.show()

    def histogram(self, feature, color=None):
        fig = px.histogram(self.df, x=feature, color=color)
        fig.show()

    # def scatter_plot_2d_average(type='album'):
