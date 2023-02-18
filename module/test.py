import data
import graph
from helpers import search_uri


search_uri("radiohead", type='playlist')

search_uri("deco27", type='playlist')

input = data.Data()

input.add_playlist('spotify:playlist:37i9dQZF1DZ06evO2VxlyE')
input.add_playlist('spotify:playlist:37i9dQZF1DZ06evO4liOn9')

results = input.get_data()

graph.graph_track_audio_features(results, feature1='energy',
                                 feature2='loudness', plot='scatterplot', dims=2)
