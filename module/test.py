import data
import audio_features
from helpers import search_uri


# search_uri("radiohead", type='playlist')

# search_uri("deco27", type='playlist')

input = data.Data()

input.add_playlist('spotify:playlist:37i9dQZF1DZ06evO2VxlyE')
input.add_playlist('spotify:playlist:37i9dQZF1DZ06evO4liOn9')
# input.add_album('spotify:album:0JwHz5SSvpYWuuCNbtYZoV')

results = input.get_data()

afp = audio_features.AudioFeaturesPlot(
    results, feature1='energy', feature2='loudness', dims=2)

afp.histogram('energy', color='artist')
