from unittest.mock import patch
from splotify import helpers


@patch("splotify.spotifyapi.SpotifyApi")
def test_search_id(mock_sp, raw_search_data):
    mock_sp.search.side_effect = raw_search_data

    result = helpers.search_id(mock_sp, "No Surprises")
    assert len(result) == 11
    assert result[0] == ["Name", "Album", "Artists", "URI"]
    assert len(result[1]) == 4
    assert result[1] == [
        "No Surprises",
        "OK Computer",
        ["Radiohead"],
        "spotify:track:10nyNJ6zNy2YVYLrcwLccB",
    ]

    result = helpers.search_id(mock_sp, "OK Computer", limit=23, type="album")
    assert len(result) == 24
    assert result[0] == ["Name", "Artists", "URI"]
    assert len(result[1]) == 3
    assert result[1] == [
        "OK Computer",
        ["Radiohead"],
        "spotify:album:6dVIqQ8qmQ5GBnJ9shOYGE",
    ]

    result = helpers.search_id(mock_sp, "Radiohead", limit=15, type="artist")
    assert len(result) == 16
    assert result[0] == ["Name", "URI"]
    assert len(result[1]) == 2
    assert result[1] == ["Radiohead", "spotify:artist:4Z8W4fKeB5YxbusRsdQVPb"]

    result = helpers.search_id(mock_sp, "Radiohead", limit=3, type="playlist")
    assert len(result) == 4
    assert result[0] == ["Name", "Owner", "URI"]
    assert len(result[1]) == 3
    assert result[1] == [
        "This Is Radiohead",
        "Spotify",
        "spotify:playlist:37i9dQZF1DZ06evO2VxlyE",
    ]


# @patch("splotify.spotifyapi.SpotifyApi")
# def test_my_id(mock_sp, raw_my_data):
#     mock_sp.current_user_playlists =

#     result = helpers.my_uri(mock_sp)

#     assert len(result) == 11
#     assert result[0] == ["Name", "URI"]
#     assert len(result[1]) == 2
