import pytest
from splotify.plots import audiofeatures
from splotify import spotifyapi
import pandas as pd


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


@pytest.fixture
def track_data():
    data = [
        [
            "Reincarnation Apple",
            "PinocchioP",
            "Reincarnation Apple",
            "spotify:track:1O8mA7lbLISvEGUiNFwQnV",
        ],
        ["God-ish", "PinocchioP", "God-ish", "spotify:track:206UWNKXURTnN4zf9vmXUV"],
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
    return pd.DataFrame(data, columns=["name", "artist", "album", "uri"])


def test_add_features(track_data):
    sp = spotify_auth()

    afp = audiofeatures.AudioFeaturesPlot(sp, track_data, ["loudness", "danceability"])

    track_data["loudness"] = [-4.500, -7.125, -7.107, -4.996]
    track_data["danceability"] = [0.662, 0.652, 0.646, 0.606]

    assert afp.get_df().equals(track_data)

    afp.add_features(["duration_ms"])
    track_data["duration_ms"] = [219083, 203760, 187600, 208991]

    assert afp.get_df().equals(track_data)


def test_select_features(track_data):
    sp = spotify_auth()
    afp = audiofeatures.AudioFeaturesPlot(
        sp, track_data, ["loudness", "danceability", "duration_ms", "energy", "tempo"]
    )

    afp.select_features(["duration_ms", "energy", "tempo"])

    assert afp.get_features() == ["duration_ms", "energy", "tempo"]
