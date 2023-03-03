from splotify.plots import audiofeatures
from splotify import spotifyapi
import pandas as pd


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


def test_add_features():
    sp = spotify_auth()
    data = [
        [
            "Reincarnation Apple",
            "PinocchioP",
            "Reincarnation Apple",
            "spotify:track:1O8mA7lbLISvEGUiNFwQnV",
        ],
        [
            "God-ish",
            "PinocchioP",
            "God-ish",
            "spotify:track:206UWNKXURTnN4zf9vmXUV"
        ],
        [
            "Magical Girl and Chocolate",
            "PinocchioP",
            "Magical Girl and Chocolate",
            "spotify:track:12shJ1oIZnCG5ZZD8HjQVi",
        ],
        [
            "Non-breath oblige",
            "PinocchioP",
            "Non-breath oblige",
            "spotify:track:5LAec0974S9ZJ4WmNbgRyv",
        ],
    ]
    df = pd.DataFrame(data, columns=["name", "artist", "album", "uri"])

    afp = audiofeatures.AudioFeaturesPlot(sp, df, ["loudness", "danceability"])

    df["loudness"] = [-4.500, -7.125, -7.107, -4.996]
    df["danceability"] = [0.662, 0.652, 0.646, 0.606]

    assert afp.get_df().equals(df)

    afp.add_features(["duration_ms"])
    df["duration_ms"] = [219083, 203760, 187600, 208991]

    assert afp.get_df().equals(df)


def test_select_features():
    sp = spotify_auth()
    data = [
        [
            "No Surprises",
            "Radiohead",
            "OK Computer",
            "spotify:track:10nyNJ6zNy2YVYLrcwLccB",
        ],
        ["Creep", "Radiohead", "Pablo Honey",
            "spotify:track:70LcF31zb1H0PyJoS1Sx1r"],
        [
            "High and Dry",
            "Radiohead",
            "The Bends",
            "spotify:track:2a1iMaoWQ5MnvLFBDv4qkf",
        ],
        [
            "Karma Police",
            "Radiohead",
            "OK Computer",
            "spotify:track:63OQupATfueTdZMWTxW03A",
        ],
    ]
    df = pd.DataFrame(data, columns=["name", "artist", "album", "uri"])

    afp = audiofeatures.AudioFeaturesPlot(
        sp, df, ["loudness", "danceability", "duration_ms", "energy", "tempo"]
    )

    afp.select_features(["duration_ms", "energy", "tempo"])

    assert afp.get_features() == ["duration_ms", "energy", "tempo"]
