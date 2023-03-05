import spotifyapi

sp = spotifyapi.get_sp(
    "234645624be5451eb959f0af3d9e00ac",
    "a1425a973e8d4574a0dfbd3c9e20438f",
    "https://localhost:8888/callback",
)

print("token acquired")
