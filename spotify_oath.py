import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

auth_manager = SpotifyClientCredentials(client_id="d14a44a773b64759b4ec6df4438207e0", client_secret="8d75260500d44106a9de3f7e8d836bc1")
sp = spotipy.Spotify(auth_manager=auth_manager)
# print(json.dumps(sp.audio_analysis("https://open.spotify.com/track/6SRsiMl7w1USE4mFqrOhHC?si=93a79271912a40e6"), indent = 4))
print('...')
f = open('sample.txt', 'w')
f.write(str(json.dumps(sp.audio_features("https://open.spotify.com/track/0nkzd3yNniB767zSDDdLZ3?si=610c67560cf147a5"), indent=4)))
f.close()
print('done')
