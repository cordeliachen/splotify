import spotipy
from spotipy.oauth2 import SpotifyOAuth
import plotly.express as px
import pandas as pd


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def fetch_data(type='user', id=0, limit=20):
    # if type == 'artist':
    #     return sp.
    # else:
    return sp.current_user_saved_tracks(limit)


def graph_audio_features(input, feature1, feature2=None, feature3=None, plot='histogram', dims=1):
    data = []
    for item in enumerate(input['items']):
        song_data = []
        song_data.append(item[1]['track']['name'])
        song_data.append(item[1]['track']['artists'][0]['name'])
        song_data.append(item[1]['track']['album']['name'])
        track_id = item[1]['track']['uri']
        song_data.append(sp.audio_features(track_id)[0][feature1])
        if dims > 1:
            song_data.append(sp.audio_features(track_id)[0][feature2])
        if dims > 2:
            song_data.append(sp.audio_features(track_id)[0][feature3])
        data.append(song_data)

    if plot == 'histogram':
        print("lol")
    elif plot == 'scatterplot':
        if dims == 2:
            df = pd.DataFrame(
                data, columns=['name', 'artist', 'album', feature1, feature2])
            fig = px.scatter(df, x=feature1, y=feature2,
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


results = fetch_data(limit=50)


# graph_audio_features(results, feature1='energy',
#                      feature2='loudness', plot='scatterplot', dims=2)

graph_audio_features(results, feature1='energy',
                     feature2='loudness', feature3='danceability', plot='scatterplot', dims=3)
