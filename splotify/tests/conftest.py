import pytest
import pandas as pd


@pytest.fixture
def track_data():
    data = [
        [
            "As Good As New",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:71or1G6CbfIttRDnBnTTAL",
        ],
        ["Voulez-Vous", "ABBA", "Voulez-Vous", "spotify:track:17OqI90oTFZ3J8PVu6j07V"],
        [
            "I Have A Dream",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:1PtJclc46wTk367PlsU6Uj",
        ],
        ["Angeleyes", "ABBA", "Voulez-Vous", "spotify:track:7rWgGyRK7RAqAAXy4bLft9"],
        [
            "The King Has Lost His Crown",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:4IKF9BDHZALfCXYXdS0koQ",
        ],
        [
            "Does Your Mother Know",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:2HPB3px8MJZRMfu1L65Z41",
        ],
        [
            "If It Wasn't For The Nights",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:3R47KOuGuGvmoeQqbODPa3",
        ],
        ["Chiquitita", "ABBA", "Voulez-Vous", "spotify:track:762B4bOcXF7I2Y8UlKTyTy"],
        [
            "Lovers (Live A Little Longer)",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:0mb5Q9w5GJKU7HClkEzHpy",
        ],
        [
            "Kisses Of Fire",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:4zoWdR02nRwK8NWqpCM151",
        ],
        [
            "Summer Night City",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:35iCSlFxyiawRBUOtQAkeT",
        ],
        [
            "Lovelight - Original Version",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:2TyQF1DcQ8k2cLjiweqQyG",
        ],
        [
            "Gimme! Gimme! Gimme! (A Man After Midnight)",
            "ABBA",
            "Voulez-Vous",
            "spotify:track:3vkQ5DAB1qQMYO4Mr9zJN6",
        ],
        ["Airbag", "Radiohead", "OK Computer", "spotify:track:7c378mlmubSu7NGkLFa4sN"],
        [
            "Paranoid Android",
            "Radiohead",
            "OK Computer",
            "spotify:track:6LgJvl0Xdtc73RJ1mmpotq",
        ],
        [
            "Subterranean Homesick Alien",
            "Radiohead",
            "OK Computer",
            "spotify:track:2CVV8PtUYYsux8XOzWkCP0",
        ],
        [
            "Exit Music (For A Film)",
            "Radiohead",
            "OK Computer",
            "spotify:track:0z1o5L7HJx562xZSATcIpY",
        ],
        [
            "Let Down",
            "Radiohead",
            "OK Computer",
            "spotify:track:2fuYa3Lx06QQJAm0MjztKr",
        ],
        [
            "Karma Police",
            "Radiohead",
            "OK Computer",
            "spotify:track:63OQupATfueTdZMWTxW03A",
        ],
        [
            "Fitter Happier",
            "Radiohead",
            "OK Computer",
            "spotify:track:6wnmRxEbwUK7WLyUtiRuT7",
        ],
        [
            "Electioneering",
            "Radiohead",
            "OK Computer",
            "spotify:track:0gTRROuntlrPQ64W3J2Etv",
        ],
        [
            "Climbing Up the Walls",
            "Radiohead",
            "OK Computer",
            "spotify:track:2PDQReEXBViVwkrbQ34vd7",
        ],
        [
            "No Surprises",
            "Radiohead",
            "OK Computer",
            "spotify:track:10nyNJ6zNy2YVYLrcwLccB",
        ],
        ["Lucky", "Radiohead", "OK Computer", "spotify:track:14xj58ZexBaEaHARb11Cqs"],
        [
            "The Tourist",
            "Radiohead",
            "OK Computer",
            "spotify:track:1UuaWKypSkIHxFZD03zw4m",
        ],
    ]
    return pd.DataFrame(data, columns=["name", "artist", "album", "uri"])


@pytest.fixture
def loudness_data():
    return [
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


@pytest.fixture
def danceability_data():
    return [
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


@pytest.fixture
def energy_data():
    return [
        0.783,
        0.774,
        0.374,
        0.922,
        0.557,
        0.865,
        0.88,
        0.554,
        0.732,
        0.754,
        0.858,
        0.723,
        0.491,
        0.872,
        0.848,
        0.595,
        0.276,
        0.676,
        0.501,
        0.391,
        0.888,
        0.656,
        0.393,
        0.4,
        0.295,
    ]
