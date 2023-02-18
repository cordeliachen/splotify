from __init__ import sp
import plotly.express as px
import pandas as pd
from tqdm import tqdm


def graph_track_audio_features(tracks, feature1, feature2=None, feature3=None, plot='histogram', dims=1):
    data = []
    for track in tqdm(tracks, desc='Graphing'):
        song_data = []
        song_data.append(track['name'])
        song_data.append(track['artists'][0]['name'])
        song_data.append(track['album']['name'])
        track_id = track['uri']

        audio_features = sp.audio_features(track_id)[0]

        song_data.append(audio_features[feature1])
        if dims > 1:
            song_data.append(audio_features[feature2])
        if dims > 2:
            song_data.append(audio_features[feature3])
        data.append(song_data)

    if plot == 'histogram':
        print("lol")
    elif plot == 'scatterplot':
        if dims == 2:
            df = pd.DataFrame(
                data, columns=['name', 'artist', 'album', feature1, feature2])
            fig = px.scatter(df, x=feature1, y=feature2, color='artist',
                             custom_data=['name', 'artist', 'album'])
        elif dims == 3:
            df = pd.DataFrame(
                data, columns=['name', 'artist', 'album', feature1, feature2, feature3])
            fig = px.scatter_3d(df, x=feature1, y=feature2, z=feature3, custom_data=[
                                'name', 'artist', 'album'])
        fig.update_traces(
            hovertemplate="<br>".join([
                "name: %{customdata[0]}",
                "artist: %{customdata[1]}",
                "album: %{customdata[2]}",
            ])
        )
    fig.show()


# def graph_artist_audio_features(input, feature1, feature2=None, feature3=None, plot='histogram', dims=1):
