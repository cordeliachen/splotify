from splotify import spotifyapi
from splotify import data
import pandas as pd


def spotify_auth():
    return spotifyapi.get_sp(
        "234645624be5451eb959f0af3d9e00ac",
        "a1425a973e8d4574a0dfbd3c9e20438f",
        "https://localhost:8888/callback",
    )


def test_add_tracks():
    sp = spotify_auth()
    d = data.Data(sp)

    d.add_track("spotify:track:10nyNJ6zNy2YVYLrcwLccB")
    d.add_tracks(
        [
            "spotify:track:70LcF31zb1H0PyJoS1Sx1r",
            "spotify:track:2a1iMaoWQ5MnvLFBDv4qkf",
            "spotify:track:63OQupATfueTdZMWTxW03A",
        ]
    )
    result = d.create_df()

    expected_data = [
        [
            "No Surprises",
            "Radiohead",
            "OK Computer",
            "spotify:track:10nyNJ6zNy2YVYLrcwLccB",
        ],
        ["Creep", "Radiohead", "Pablo Honey", "spotify:track:70LcF31zb1H0PyJoS1Sx1r"],
        [
            "High and Dry",
            "Radiohead",
            "The Bends",
            "spotify:track:2a1iMaoWQ5MnvLFBDv4qkf",
        ],
        [
            "Karma Police",
            "Radiohead",
            "OK Computer",
            "spotify:track:63OQupATfueTdZMWTxW03A",
        ],
    ]
    expected = pd.DataFrame(expected_data, columns=["name", "artist", "album", "uri"])

    assert result.equals(expected)


def test_add_albums():
    sp = spotify_auth()
    d = data.Data(sp)

    d.add_album("spotify:album:5gqdC7ZnKbTJqypdYHr1Kt")
    d.add_albums(
        [
            "spotify:album:5MEXGTej0dxa5MbXZCJJyk",
            "spotify:album:1zXLavJ8fGLSqPfCc8Z4yG",
            "spotify:album:6bL5NBdI1WHI7xRQc4NNVw",
        ]
    )
    result = d.create_df()
    print(result)
    expected_data = [
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
    expected = pd.DataFrame(expected_data, columns=["name", "artist", "album", "uri"])

    assert result.equals(expected)
