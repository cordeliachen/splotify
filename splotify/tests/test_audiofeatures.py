from splotify import spotifyapi


from splotify.plots import audiofeatures


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


def test_add_features(track_data, loudness_data, danceability_data, energy_data):
    sp = spotify_auth()

    afp = audiofeatures.AudioFeaturesPlot(sp, track_data, ["loudness", "danceability"])

    track_data["loudness"] = loudness_data
    track_data["danceability"] = danceability_data

    assert afp.get_df().equals(track_data)

    afp.add_features(["energy"])
    track_data["energy"] = energy_data

    assert afp.get_df().equals(track_data)


def test_select_features(track_data):
    sp = spotify_auth()
    afp = audiofeatures.AudioFeaturesPlot(
        sp, track_data, ["loudness", "danceability", "duration_ms", "energy", "tempo"]
    )

    afp.select_features(["duration_ms", "energy", "tempo"])

    assert afp.get_features() == ["duration_ms", "energy", "tempo"]


def test_scatter_plot_2d(track_data):
    sp = spotify_auth()
    afp = audiofeatures.AudioFeaturesPlot(sp, track_data, ["loudness", "danceability"])

    fig = afp.scatter_plot_2d(color="album")

    assert fig is not None


def test_scatter_plot_3d(track_data):
    sp = spotify_auth()
    afp = audiofeatures.AudioFeaturesPlot(
        sp, track_data, ["loudness", "danceability", "energy"]
    )

    fig = afp.scatter_plot_3d(color="album")

    assert fig is not None


def test_histogram(track_data):
    sp = spotify_auth()
    afp = audiofeatures.AudioFeaturesPlot(
        sp, track_data, ["loudness", "danceability", "energy"]
    )

    fig = afp.histogram(feature="danceability", color="artist")

    assert fig is not None
