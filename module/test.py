import data
import audio_features
import category
from helpers import search_uri, my_uri


# search_uri("radiohead", type='playlist')

# search_uri("deco27", type='playlist')
# my_uri(50)

input = data.Data()

input.add_playlist('spotify:playlist:65pRMS3u6EF1ljvDTHTe6B')
# input.add_playlist('spotify:playlist:37i9dQZF1DZ06evO4liOn9')
# input.add_album('spotify:album:0JwHz5SSvpYWuuCNbtYZoV')

results = input.create_df()

m = category.CategoryPlot(results)

m.pie_chart(type='artist')

# afp = audio_features.AudioFeaturesPlot(
#     results, ['energy', 'loudness'], dims=1)


# afp.histogram('loudness', color='artist')
