# Rnb : https://open.spotify.com/playlist/7k2tDlptu3OHDMBVbO94zf?si=7788e5a682004beb
# psytrance : https://open.spotify.com/playlist/5PpLEyVEGJWhybBaZoGRQ3?si=211eae7f639a4ee6
# Techno : https://open.spotify.com/playlist/7mwPa6HjqoiUrsk3C2Hitk?si=8e4fe4f8079d4f8b
#          https://open.spotify.com/playlist/2MSE9BQC2U1i3U4NNltxOw?si=2d6a1a729a824cbb
# Emo: https://open.spotify.com/playlist/4M5jDOpPSmPPCQEMPCkgO5?si=8495de4493a24635
#      https://open.spotify.com/playlist/0shS8aqWu8BLP8YEdwveGr?si=1c25a638e6964fe5
# Hardstyle : https://open.spotify.com/playlist/5lpA197Jsrugj8INDnNyp4?si=a7a60f27a3dd45cd
#             https://open.spotify.com/playlist/1PZIEAy8yEcD3Z41wAJ74i?si=428feb85432d4020
#             https://open.spotify.com/playlist/3bGSAHGYFEDxyEj7uXe0qq?si=09a86398a59849a5
# Rap : https://open.spotify.com/playlist/1i12RnXAQIoH4m4zlKyN8u?si=ecaf2999582342ca
#       https://open.spotify.com/playlist/0mSf78pnq5xVU6kOtdv6dx?si=a537a4ddc846435f
#       https://open.spotify.com/playlist/4nZo2X8iHrwhYBYdKvysgI?si=9711b7b547594a49
# Hiphop : https://open.spotify.com/playlist/0ppKLqk6Jy0hNpoLQY5NvQ?si=d2436f2a83ba4cab
# Pop : https://open.spotify.com/playlist/2UZk7JjJnbTut1w8fqs3JL?si=e7fdd2e8757b4dc1
#       https://open.spotify.com/playlist/0locryv72BXQL47gTcFJch?si=3b3d8406b21e422c
# Rock : https://open.spotify.com/playlist/4aQsjBuSIy3yUs8w6I2OQr?si=6db38de920cb4a92
# Trap : https://open.spotify.com/playlist/6ggB3innVuQK2tKwFhg1to?si=7e4de93b8d1a4472
#        https://open.spotify.com/playlist/6CK91P2zdiStnuKF8xIZx7?si=fa5d60f59e624de5
# Dark Trap : https://open.spotify.com/playlist/1eBUubNHdBrDv7jLHmwJIv?si=7394ee061d194d3b
#             https://open.spotify.com/playlist/2Gx2R8QEplxaUOoSAWNfP0?si=cc4b60022cee4125
#             https://open.spotify.com/playlist/3vOMMPed4hbEG9AOaLtu7l?si=5376981bc2ce4ec2
# Underground Rap : https://open.spotify.com/playlist/1eBUubNHdBrDv7jLHmwJIv?si=7394ee061d194d3b
# Trap Metal : https://open.spotify.com/playlist/2NX8c9bZdRrMUgcdHW4Aj6?si=ad2e64544bc14c2c
#              https://open.spotify.com/playlist/3vOMMPed4hbEG9AOaLtu7l?si=5376981bc2ce4ec2
# dnb : https://open.spotify.com/playlist/2PwL4MlktpfWc8Fxtlb8yT?si=8ad2ce77d6304263
#       https://open.spotify.com/playlist/2S2GM0uc71Qdt9rx3kgqS9?si=cce9341024654f35
# Technohouse : https://open.spotify.com/playlist/0xFeowCNlsHchPwK5GGphN?si=3876a75991634b25
#               https://open.spotify.com/playlist/6R9WV3HTMGbGgaeLw9uB6V?si=7362962909e94d6a

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
playlists = {
    'Rnb': ['https://open.spotify.com/playlist/7k2tDlptu3OHDMBVbO94zf?si=7788e5a682004beb'],
    'psytrance' : ['https://open.spotify.com/playlist/5PpLEyVEGJWhybBaZoGRQ3?si=211eae7f639a4ee6'],
    'Techno' : [
        'https://open.spotify.com/playlist/7mwPa6HjqoiUrsk3C2Hitk?si=8e4fe4f8079d4f8b',
        'https://open.spotify.com/playlist/2MSE9BQC2U1i3U4NNltxOw?si=2d6a1a729a824cbb'
        ],
    'Emo' : [
        'https://open.spotify.com/playlist/4M5jDOpPSmPPCQEMPCkgO5?si=8495de4493a24635',
        'https://open.spotify.com/playlist/0shS8aqWu8BLP8YEdwveGr?si=1c25a638e6964fe5'
        ],
    'Hardstyle' : [
        'https://open.spotify.com/playlist/5lpA197Jsrugj8INDnNyp4?si=a7a60f27a3dd45cd',
        'https://open.spotify.com/playlist/1PZIEAy8yEcD3Z41wAJ74i?si=428feb85432d4020',
        'https://open.spotify.com/playlist/3bGSAHGYFEDxyEj7uXe0qq?si=09a86398a59849a5'
        ],
    'Rap' : [
        'https://open.spotify.com/playlist/1i12RnXAQIoH4m4zlKyN8u?si=ecaf2999582342ca',
        'https://open.spotify.com/playlist/0mSf78pnq5xVU6kOtdv6dx?si=a537a4ddc846435f',
        'https://open.spotify.com/playlist/4nZo2X8iHrwhYBYdKvysgI?si=9711b7b547594a49',
        ],
    'Hiphop' : ['https://open.spotify.com/playlist/0ppKLqk6Jy0hNpoLQY5NvQ?si=d2436f2a83ba4cab'],
    'Pop' : [
        'https://open.spotify.com/playlist/2UZk7JjJnbTut1w8fqs3JL?si=e7fdd2e8757b4dc1',
        'https://open.spotify.com/playlist/0locryv72BXQL47gTcFJch?si=3b3d8406b21e422c'
        ],
    'Rock' : ['https://open.spotify.com/playlist/4aQsjBuSIy3yUs8w6I2OQr?si=6db38de920cb4a92'],
    'Trap' : [
        'https://open.spotify.com/playlist/6ggB3innVuQK2tKwFhg1to?si=7e4de93b8d1a4472',
        'https://open.spotify.com/playlist/6CK91P2zdiStnuKF8xIZx7?si=fa5d60f59e624de5'
        ],
    'Dark Trap' : [
        'https://open.spotify.com/playlist/1eBUubNHdBrDv7jLHmwJIv?si=7394ee061d194d3b',
        'https://open.spotify.com/playlist/2Gx2R8QEplxaUOoSAWNfP0?si=cc4b60022cee4125',
        'https://open.spotify.com/playlist/3vOMMPed4hbEG9AOaLtu7l?si=5376981bc2ce4ec2'
        ],
    'Underground Rap' : ['https://open.spotify.com/playlist/1eBUubNHdBrDv7jLHmwJIv?si=7394ee061d194d3b'],
    'Trap Metal' : [
            'https://open.spotify.com/playlist/2NX8c9bZdRrMUgcdHW4Aj6?si=ad2e64544bc14c2c',
            'https://open.spotify.com/playlist/3vOMMPed4hbEG9AOaLtu7l?si=5376981bc2ce4ec2'
                    ],
    
    'dnb' : ['https://open.spotify.com/playlist/2PwL4MlktpfWc8Fxtlb8yT?si=8ad2ce77d6304263',
            'https://open.spotify.com/playlist/2S2GM0uc71Qdt9rx3kgqS9?si=cce9341024654f35'],
    
    'Technohouse' : ['https://open.spotify.com/playlist/0xFeowCNlsHchPwK5GGphN?si=3876a75991634b25',
                    'https://open.spotify.com/playlist/6R9WV3HTMGbGgaeLw9uB6V?si=7362962909e94d6a']

    
    
}

auth_manager = SpotifyClientCredentials(client_id="d14a44a773b64759b4ec6df4438207e0", client_secret="8d75260500d44106a9de3f7e8d836bc1")
sp = spotipy.Spotify(auth_manager=auth_manager)
count = 0

for key in playlists:
    print(f'key:{key}')
    for playlist in playlists[key]:
        offset = 0
        total = 10**5
        while offset < total:
            pl = sp.playlist_items(playlist, additional_types=['track'],limit=100, offset=offset)
            total = pl['total']
            # print(pl['total'])
            # print(json.dumps(pl['items'], indent=2))
            for track in pl['items']:
                try:
                    # print(track['track']['name'])
                    count += 1
                except TypeError:
                    continue
            offset += len(pl['items'])
            
print(count)
            
            
        # print('total', total)
        # print(count)
        
# print(sp.audio_features(sp.playlist('https://open.spotify.com/playlist/7mwPa6HjqoiUrsk3C2Hitk?si=8e4fe4f8079d4f8b')['tracks']['items'][0]['track']['href']))
# # print(jsonsp.playlist('https://open.spotify.com/playlist/5yjBElkbHDzxznSn99eSI4?si=7232f4ea571148f9'))
# print(json.dumps(sp.playlist('https://open.spotify.com/playlist/7mwPa6HjqoiUrsk3C2Hitk?si=8e4fe4f8079d4f8b')['tracks']['items'][0]['track']['popularity'], indent = 2))
