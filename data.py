import pandas as pd
import matplotlib.pyplot as plt

acousticness_rate = 0
danceability_rate = 0
energy_rate = 0
instrumentalness_rate = 0
liveness_rate = 0
loudness_rate = 0
speechiness_rate = 0
tempo_rate = 0
valence_rate = 0
popularity_rate = 0


df = pd.read_csv('Data/SpotifyAudioFeaturesApril2019.csv')
for row in df:
    print(row)
# print(df.head())
# for index, row in df.iterrows():
#     print(row['popularity'], row['valence'])