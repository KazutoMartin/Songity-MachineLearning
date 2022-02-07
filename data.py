import pandas as pd


###################################################
################ Initial Values ###################
###################################################
rates = {
    'acousticness' : 0.5,
    'danceability' : 0.75,
    'energy' : 0.75,
    'instrumentalness' : 0.8,
    'liveness' : 0.8,
    'loudness' : 0.8,
    'speechiness' : 0.6,
    'tempo' : 0.5,
    'valence' : 0.5,
    'popularity' : 0.9,
}

###################################################

def get_sigma(**args):
    sigma = 0
    for inp in args:
        sigma += args[inp] * rates[inp]
    print(sigma)
    return sigma
        



df = pd.read_csv('Data/SpotifyAudioFeaturesApril2019.csv')
for row in df:
    print(row)
sigmas = []
# print(df.head())
for index, row in df.iterrows():
    sigmas.append(get_sigma(
        acousticness=row['acousticness'], 
        danceability=row['danceability'],
        energy=row['energy'],
        instrumentalness=row['instrumentalness'],
        liveness=row['liveness'],
        loudness=row['loudness'],
        speechiness=row['speechiness'],
        tempo=row['tempo'],
        valence=row['valence'],
        popularity=row['popularity'],
        ))
    
print('min:', min(sigmas))
print('max:', max(sigmas))

    