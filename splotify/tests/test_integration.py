from splotify import spotifyapi
from splotify import data
from splotify.plots import audiofeatures


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


def test_integration():
    sp = spotify_auth()
    d = data.Data(sp)

    d.add_album("spotify:album:5gqdC7ZnKbTJqypdYHr1Kt")
    d.add_albums(
        [
            "spotify:album:5MEXGTej0dxa5MbXZCJJyk",
            "spotify:album:1zXLavJ8fGLSqPfCc8Z4yG",
            "spotify:album:6bL5NBdI1WHI7xRQc4NNVw",
        ]
    )

    afp = audiofeatures.AudioFeaturesPlot(
        sp, d.create_df(), ["loudness", "danceability"]
    )

    df = d.create_df()

    df["loudness"] = [-4.500, -7.125, -7.107, -4.996]
    df["danceability"] = [0.662, 0.652, 0.646, 0.606]

    assert afp.get_df().equals(df)
