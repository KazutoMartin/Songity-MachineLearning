import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
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

df = df.drop(columns=['type', 'id', 'uri', 'track_href','analysis_url', 'song_name','Unnamed: 0','title', 'duration_ms','time_signature'])
# df = df.drop(['type'])


df['genre'] = df['genre'].replace(['Dark Trap', 'Rap', 'Pop', 'Hiphop', 'Trap Metal', 'RnB', 'techno', 'trance', 'hardstyle', 'Underground Rap', 'dnb', 'psytrance', 'Emo', 'trap', 'techhouse'],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

# loudness can have some negative data
df["loudness"] = df["loudness"] + df["loudness"].min()

df["key"] = (df["key"] / df["key"].max())
df["tempo"] = (df["tempo"] / df["tempo"].max())
df["loudness"] = (df["loudness"] / df["loudness"].max())





df = df.sample(frac=1)
# df_random.to_csv('now.csv')

knn = KNeighborsClassifier(n_neighbors=61)

X = df.drop(columns=['genre'])
y = df['genre']


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)



# cross_validate
cv_scores = cross_val_score(knn, X, y, cv=10)

cv_scores_mean = np.mean(cv_scores)
print(cv_scores , "\n\n""mean =" ,"{:.2f}".format(cv_scores_mean))
