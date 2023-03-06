from splotify import data
import pandas as pd
from unittest.mock import patch


@patch("splotify.spotifyapi.SpotifyApi")
def test_add_tracks(mock_sp, raw_track_data, track_data):
    mock_sp.track.side_effect = raw_track_data
    d = data.Data(mock_sp)

    d.add_track("spotify:track:71or1G6CbfIttRDnBnTTAL")
    d.add_tracks(
        [
            "spotify:track:17OqI90oTFZ3J8PVu6j07V",
            "spotify:track:1PtJclc46wTk367PlsU6Uj",
            "spotify:track:7rWgGyRK7RAqAAXy4bLft9",
            "spotify:track:4IKF9BDHZALfCXYXdS0koQ",
            "spotify:track:2HPB3px8MJZRMfu1L65Z41",
            "spotify:track:3R47KOuGuGvmoeQqbODPa3",
            "spotify:track:762B4bOcXF7I2Y8UlKTyTy",
            "spotify:track:0mb5Q9w5GJKU7HClkEzHpy",
            "spotify:track:4zoWdR02nRwK8NWqpCM151",
            "spotify:track:35iCSlFxyiawRBUOtQAkeT",
            "spotify:track:2TyQF1DcQ8k2cLjiweqQyG",
            "spotify:track:3vkQ5DAB1qQMYO4Mr9zJN6",
            "spotify:track:7c378mlmubSu7NGkLFa4sN",
            "spotify:track:6LgJvl0Xdtc73RJ1mmpotq",
            "spotify:track:2CVV8PtUYYsux8XOzWkCP0",
            "spotify:track:0z1o5L7HJx562xZSATcIpY",
            "spotify:track:2fuYa3Lx06QQJAm0MjztKr",
            "spotify:track:63OQupATfueTdZMWTxW03A",
            "spotify:track:6wnmRxEbwUK7WLyUtiRuT7",
            "spotify:track:0gTRROuntlrPQ64W3J2Etv",
            "spotify:track:2PDQReEXBViVwkrbQ34vd7",
            "spotify:track:10nyNJ6zNy2YVYLrcwLccB",
            "spotify:track:14xj58ZexBaEaHARb11Cqs",
            "spotify:track:1UuaWKypSkIHxFZD03zw4m",
        ]
    )
    result = d.get_df()

    expected = pd.DataFrame(track_data, columns=["name", "artist", "album", "uri"])

    assert result.equals(expected)


@patch("splotify.spotifyapi.SpotifyApi")
def test_add_albums(mock_sp, raw_album_data, raw_track_data, track_data):
    mock_sp.album.side_effect = raw_album_data
    mock_sp.track.side_effect = raw_track_data
    d = data.Data(mock_sp)

    d.add_albums(
        ["spotify:album:7iLuHJkrb9KHPkMgddYigh", "spotify:album:6dVIqQ8qmQ5GBnJ9shOYGE"]
    )
    result = d.get_df()

    expected = pd.DataFrame(track_data, columns=["name", "artist", "album", "uri"])

    assert result.equals(expected)
