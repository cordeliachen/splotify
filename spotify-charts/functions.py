import spotipy
from spotipy.oauth2 import SpotifyOAuth
import matplotlib.pyplot as plt
import numpy as np

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def fetch_data(type='user', id=0, limit=20):
    # if type == 'artist':
    #     return sp.
    # else:
    return sp.current_user_saved_tracks(limit)


def graph_audio_features(data, feature1, feature2=None, feature3=None, plot='histogram', dims=1):
    x = []
    y = []
    z = []
    for item in enumerate(data['items']):
        track_id = item[1]['track']['uri']
        x.append(sp.audio_features(track_id)[0][feature1])
        if dims > 1:
            y.append(sp.audio_features(track_id)[0][feature2])
        if dims > 2:
            z.append(sp.audio_features(track_id)[0][feature3])

    if plot == 'histogram':
        plt.hist(np.array(x))
    elif plot == 'scatterplot':
        if dims == 2:
            plt.scatter(x, y)
            plt.xlabel(feature1)
            plt.ylabel(feature2)
        elif dims == 3:
            _, ax = plt.subplots(subplot_kw={"projection": "3d"})
            ax.scatter(x, y, z)
            ax.set_xlabel(feature1)
            ax.set_ylabel(feature2)
            ax.set_zlabel(feature3)
    plt.show()
    # if dims < 1 or dims > 3:
    #     raise Exception("Invalid dimensions. The supported number of dimensions are: 1, 2, 3")
    # else:
    #     raise Exception("Invalid plot type. The supported plot types are: 'histogram', 'scatterplot'")


results = fetch_data(50)


graph_audio_features(results, feature1='energy',
                     feature2='loudness', plot='scatterplot', dims=2)

# graph_audio_features(results, feature1='energy',
#                      feature2='loudness', feature3='danceability', plot='scatterplot', dims=3)
