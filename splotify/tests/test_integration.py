from splotify import spotifyapi
from splotify import data
from splotify.plots import audiofeatures
from splotify import helpers
from splotify.tests.conftest import loudness_data, danceability_data


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


def test_integration(loudness_data, danceability_data):
    sp = spotify_auth()

    d = data.Data(sp)

    id1 = helpers.search_uri(sp, "Voulez-Vous", limit=1, type="album")[1][2]
    id2 = helpers.search_uri(sp, "OK Computer", limit=1, type="album")[1][2]

    d.add_albums([id1, id2])

    afp = audiofeatures.AudioFeaturesPlot(sp, d.get_df(), ["loudness", "danceability"])

    df = d.get_df()

    df["loudness"] = loudness_data
    df["danceability"] = danceability_data

    assert afp.get_df().equals(df)
