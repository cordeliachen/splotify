from __init__ import sp
from tqdm import tqdm

# Data stores the all the tracks you want to view in tqdm(a single plot


class Data:
    def __init__(self):
        self.data = []
        pass

    def add_track(self, id):
        result = sp.track(id)
        self.data.append(result)
        return result

    def add_tracks(self, ids):
        result = []
        for id in tqdm(ids, desc='Adding tracks'):
            result.append(self.add_track(id))
        return result

    def add_album(self, id):
        result = []
        tracks = sp.album(id)['tracks']['items']
        for track in tqdm(tracks, desc='Adding album'):
            self.add_track(track['uri'])
            result.append(track)
        return result

    def add_albums(self, ids):
        for id in tqdm(ids, desc='Adding albums'):
            self.add_album(id)

    def add_playlist(self, id):
        result = []
        tracks = sp.playlist(id)['tracks']['items']
        for track in tqdm(tracks, desc='Adding playlist'):
            self.add_track(track['track']['uri'])
            result.append(track)
        return result

    def add_playlists(self, ids):
        for id in tqdm(ids, desc='Adding playlists'):
            self.add_playlist(id)

    def get_data(self):
        return self.data
