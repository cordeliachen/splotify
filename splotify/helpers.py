"""URI search functions.

This module contains functions to help get the Spotify URIs of tracks, albums,
artists, and playlists.

"""

from tabulate import tabulate


def search_id(sp, query, limit=10, type="track"):
    """Returns and prints the URIs of public Spotify data.

    Returns and prints the URIs of Spotify data that is not user-specific such
    as tracks, albums, artists, and public playlists.

    Args:
        sp (splotify.spotifyapi.SpotifyApi): A `SpotifyApi` instance.
        query (str): The query you want to search for.
        limit (:obj:`int`, optional): The number of results you want to view.
            Defaults to 10.
        type (:obj:`str`, optional): The type of URI you want to search up.
            Currently only supports 'track', 'album', 'artist', and 'playlist'.
            Defaults to 'track'.

    Returns:
        A nested list. The first list is the names of the columns, and the
        remaining lists are the search results.

    """
    results = sp.search(query, limit, type)
    if type == "track":
        table = [["Name", "Album", "Artists", "URI"]]
        for i in range(limit):
            song = results["tracks"]["items"][i]
            table.append(
                [
                    song["name"],
                    song["album"]["name"],
                    [x["name"] for x in song["artists"]],
                    song["uri"],
                ]
            )
        print(tabulate(table, headers="firstrow"))
    elif type == "album":
        table = [["Name", "Artists", "URI"]]
        for i in range(limit):
            album = results["albums"]["items"][i]
            table.append(
                [album["name"], [x["name"] for x in album["artists"]], album["uri"]]
            )
        print(tabulate(table, headers="firstrow"))
    elif type == "artist":
        table = [["Name", "URI"]]
        for i in range(limit):
            artist = results["artists"]["items"][i]
            table.append([artist["name"], artist["uri"]])
        print(tabulate(table, headers="firstrow"))
    elif type == "playlist":
        table = [["Name", "Owner", "URI"]]
        for i in range(limit):
            playlist = results["playlists"]["items"][i]
            table.append(
                [playlist["name"], playlist["owner"]["display_name"], playlist["uri"]]
            )
        print(tabulate(table, headers="firstrow"))
    # else:

    return table


def my_id(sp, limit=10, type="playlist"):
    """Returns and prints the URIs of your personal Spotify playlists.

    Args:
        sp (splotify.spotifyapi.SpotifyApi): A `SpotifyApi` instance.
        limit (:obj:`int`, optional): The number of results you want to view.
            Defaults to 10.
        type (str, optional): The type of URI you want to search up. Defaults
            to 'playlist'. Currently only supports 'playlist'.

    Returns:
        A nested list. The first list is the names of the columns, and the
        remaining lists are the search results.

    """
    if type == "playlist":
        results = sp.current_user_playlists()
        table = [["Name", "URI"]]
        for i in range(limit):
            playlist = results["items"][i]
            table.append([playlist["name"], playlist["uri"]])
        print(tabulate(table, headers="firstrow"))
    return table
