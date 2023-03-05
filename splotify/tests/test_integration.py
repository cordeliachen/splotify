from splotify import spotifyapi
from splotify import data
from splotify.plots import audiofeatures
from splotify import helpers


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


def test_integration():
    sp = spotify_auth()

    d = data.Data(sp)

    id1 = helpers.search_uri(sp, "Voulez-Vous", limit=1, type="album")[1][2]
    id2 = helpers.search_uri(sp, "OK Computer", limit=1, type="album")[1][2]

    d.add_albums([id1, id2])

    afp = audiofeatures.AudioFeaturesPlot(sp, d.get_df(), ["loudness", "danceability"])

    df = d.get_df()

    df["loudness"] = [
        -5.697,
        -6.931,
        -12.049,
        -6.091,
        -8.236,
        -5.68,
        -4.692,
        -8.108,
        -6.371,
        -6.963,
        -5.66,
        -5.938,
        -9.655,
        -7.313,
        -6.501,
        -8.919,
        -11.357,
        -9.017,
        -9.129,
        -14.99,
        -5.491,
        -7.475,
        -10.654,
        -9.813,
        -8.57,
    ]
    df["danceability"] = [
        0.846,
        0.708,
        0.549,
        0.719,
        0.717,
        0.728,
        0.7,
        0.5,
        0.519,
        0.589,
        0.476,
        0.56,
        0.749,
        0.305,
        0.251,
        0.312,
        0.293,
        0.351,
        0.36,
        0.432,
        0.201,
        0.243,
        0.255,
        0.213,
        0.241,
    ]

    assert afp.get_df().equals(df)
