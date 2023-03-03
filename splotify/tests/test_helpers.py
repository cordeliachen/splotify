from splotify import spotifyapi
from splotify import helpers


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


def test_search_uri():
    sp = spotify_auth()

    result = helpers.search_uri(sp, "No Surprises")
    assert len(result) == 11
    assert result[0] == ["Name", "Album", "Artists", "URI"]
    assert len(result[1]) == 4
    assert result[1] == [
        "No Surprises",
        "OK Computer",
        ["Radiohead"],
        "spotify:track:10nyNJ6zNy2YVYLrcwLccB",
    ]

    result = helpers.search_uri(sp, "OK Computer", limit=23, type="album")
    assert len(result) == 24
    assert result[0] == ["Name", "Artists", "URI"]
    assert len(result[1]) == 3
    assert result[1] == [
        "OK Computer",
        ["Radiohead"],
        "spotify:album:6dVIqQ8qmQ5GBnJ9shOYGE",
    ]

    result = helpers.search_uri(sp, "Radiohead", limit=15, type="artist")
    assert len(result) == 16
    assert result[0] == ["Name", "URI"]
    assert len(result[1]) == 2
    assert result[1] == ["Radiohead", "spotify:artist:4Z8W4fKeB5YxbusRsdQVPb"]

    result = helpers.search_uri(sp, "Radiohead", limit=3, type="playlist")
    assert len(result) == 4
    assert result[0] == ["Name", "Owner", "URI"]
    assert len(result[1]) == 3
    assert result[1] == [
        "This Is Radiohead",
        "Spotify",
        "spotify:playlist:37i9dQZF1DZ06evO2VxlyE",
    ]


def test_my_uri():
    sp = spotify_auth()

    result = helpers.my_uri(sp)

    assert len(result) == 11
    assert result[0] == ["Name", "URI"]
    assert len(result[1]) == 2
