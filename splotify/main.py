import spotifyapi

# import helpers
import data

# import pandas as pd
# import plots.audiofeatures as audiofeatures

sp = spotifyapi.get_sp(
    "234645624be5451eb959f0af3d9e00ac",
    "a1425a973e8d4574a0dfbd3c9e20438f",
    "https://localhost:8888/callback",
)

d = data.Data(sp)

d.add_track("spotify:track:10nyNJ6zNy2YVYLrcwLccB")
d.add_tracks(
    [
        "spotify:track:70LcF31zb1H0PyJoS1Sx1r",
        "spotify:track:2a1iMaoWQ5MnvLFBDv4qkf",
        "spotify:track:63OQupATfueTdZMWTxW03A",
    ]
)
print(d.create_df())
