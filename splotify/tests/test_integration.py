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

    id1 = helpers.search_uri(sp, "Reincarnation Apple")[1][3]
    id2 = helpers.search_uri(sp, "God-ish")[1][3]
    id3 = helpers.search_uri(sp, "Magical Girl and Chocolate")[1][3]
    id4 = helpers.search_uri(sp, "Non-breath oblige")[1][3]

    d = data.Data(sp)

    d.add_track(id1)
    d.add_tracks([id2, id3, id4])

    afp = audiofeatures.AudioFeaturesPlot(
        sp, d.create_df(), ["loudness", "danceability"]
    )

    df = d.create_df()

    df["loudness"] = [-4.500, -7.125, -7.107, -4.996]
    df["danceability"] = [0.662, 0.652, 0.646, 0.606]

    assert afp.get_df().equals(df)
