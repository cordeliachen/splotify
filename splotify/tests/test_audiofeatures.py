from unittest.mock import patch
from splotify.plots import audiofeatures


@patch("splotify.spotifyapi.SpotifyApi")
def test_add_features(
    mock_sp, raw_af_data, track_data, loudness_data, danceability_data, energy_data
):
    mock_sp.audio_features.side_effect = raw_af_data

    afp = audiofeatures.AudioFeaturesPlot(
        mock_sp, track_data, ["loudness", "danceability"]
    )

    track_data["loudness"] = loudness_data
    track_data["danceability"] = danceability_data

    assert afp.get_df().equals(track_data)

    mock_sp.audio_features.side_effect = raw_af_data

    afp.add_features(["energy"])
    track_data["energy"] = energy_data

    print(afp.get_df())
    print(track_data)

    assert afp.get_df().equals(track_data)


@patch("splotify.spotifyapi.SpotifyApi")
def test_select_features(mock_sp, raw_af_data, track_data):
    mock_sp.audio_features.side_effect = raw_af_data
    afp = audiofeatures.AudioFeaturesPlot(
        mock_sp,
        track_data,
        ["loudness", "danceability", "duration_ms", "energy", "tempo"],
    )

    afp.select_features(["duration_ms", "energy", "tempo"])

    assert afp.get_features() == ["duration_ms", "energy", "tempo"]


@patch("splotify.spotifyapi.SpotifyApi")
def test_scatter_plot_2d(mock_sp, raw_af_data, track_data):
    mock_sp.audio_features.side_effect = raw_af_data
    afp = audiofeatures.AudioFeaturesPlot(
        mock_sp, track_data, ["loudness", "danceability"]
    )

    fig = afp.scatter_plot_2d(color="album")

    assert fig is not None


@patch("splotify.spotifyapi.SpotifyApi")
def test_scatter_plot_3d(mock_sp, raw_af_data, track_data):
    mock_sp.audio_features.side_effect = raw_af_data
    afp = audiofeatures.AudioFeaturesPlot(
        mock_sp, track_data, ["loudness", "danceability", "energy"]
    )
    fig = afp.scatter_plot_3d(color="album")
    assert fig is not None


@patch("splotify.spotifyapi.SpotifyApi")
def test_histogram(mock_sp, raw_af_data, track_data):
    mock_sp.audio_features.side_effect = raw_af_data
    afp = audiofeatures.AudioFeaturesPlot(
        mock_sp, track_data, ["loudness", "danceability", "energy"]
    )
    fig = afp.histogram(feature="danceability", color="artist")
    assert fig is not None
