from splotify import data
from splotify.plots import audiofeatures
from splotify import helpers
from unittest.mock import patch


@patch("splotify.spotifyapi.SpotifyApi")
def test_integration(
    mock_sp,
    raw_search_data,
    raw_album_data,
    raw_track_data,
    raw_af_data,
    loudness_data,
    danceability_data,
):
    mock_sp.seach.return_value = raw_search_data[1]
    mock_sp.album.side_effect = raw_album_data
    mock_sp.track.sife_effect = raw_track_data
    mock_sp.audio_features.side_effect = raw_af_data

    d = data.Data(mock_sp)

    id1 = "spotify:album:7iLuHJkrb9KHPkMgddYigh"
    id2 = helpers.search_id(mock_sp, "OK Computer", limit=1, type="album")[1][2]

    d.add_albums([id1, id2])

    afp = audiofeatures.AudioFeaturesPlot(
        mock_sp, d.get_df(), ["loudness", "danceability"]
    )

    df = d.get_df()

    df["loudness"] = loudness_data
    df["danceability"] = danceability_data

    assert afp.get_df().equals(df)
