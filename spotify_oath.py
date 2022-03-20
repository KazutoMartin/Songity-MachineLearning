import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

auth_manager = SpotifyClientCredentials(client_id="d14a44a773b64759b4ec6df4438207e0", client_secret="8d75260500d44106a9de3f7e8d836bc1")
sp = spotipy.Spotify(auth_manager=auth_manager)
# print(json.dumps(sp.audio_analysis("https://open.spotify.com/track/6SRsiMl7w1USE4mFqrOhHC?si=93a79271912a40e6"), indent = 4))
print('...')

# print(sp.audio_features('https://open.spotify.com/track/31fMJwgrgNdk1IbWZEchX2?si=8aca4dc13f7542c0'))
f = open('sample.txt', 'w')
f.write(str(json.dumps(sp.audio_features("https://open.spotify.com/track/7H0ya83CMmgFcOhw0UB6ow?si=a17be5a722e84fc4"), indent=4)))
f.close()
# print('done')
# print(json.dumps(sp.artist(artist_id="6qqNVTkY8uBg9cP3Jd7DAH?si=jJuOLAzSSrG_WNgVn4R08w"), indent=2))
