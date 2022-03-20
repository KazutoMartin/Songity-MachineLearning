import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split



# {'Dark Trap', 1
# 'Rap', 2
# 'Pop',3
# 'Hiphop', 4
# 'Trap Metal',5
# 'RnB', 6
# 'techno', 7
# 'trance', 8
# 'hardstyle', 9 
# 'Underground Rap', 10
# 'dnb',11
# 'psytrance',12
# 'Emo',13
# 'trap',14
# 'techhouse'15
# }

df = pd.read_csv("Data/genres_v2.csv")

# print(df.head())
df = df.drop(columns=['type', 'id', 'uri', 'track_href','analysis_url', 'song_name','Unnamed: 0','title', 'duration_ms','time_signature',
                      'mode'])


df['genre'] = df['genre'].replace(['Dark Trap', 'Rap', 'Pop', 'Hiphop', 'Trap Metal', 'RnB', 'techno', 'trance', 'hardstyle', 'Underground Rap', 'dnb', 'psytrance', 'Emo', 'trap', 'techhouse'],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


df["key"] = (df["key"] / df["key"].max())
df["tempo"] = (df["tempo"] / df["tempo"].max())
df["loudness"] = (df["loudness"] / df["loudness"].min())





df = df.sample(frac=1)
# df_random.to_csv('now.csv')


X = df.drop(columns=['genre'])
y = df['genre']



# alg = KNeighborsClassifier(n_neighbors=20)
# alg = DecisionTreeClassifier()
alg = RandomForestClassifier()

# cross_validate
cv_scores = cross_val_score(alg, X, y, cv=10)

cv_scores_mean = np.mean(cv_scores)
print(cv_scores , "\n\n""mean =" ,"{:.2f}".format(cv_scores_mean))