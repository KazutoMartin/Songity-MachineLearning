import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder,StandardScaler



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
df = df.drop(columns=['type', 'id', 'uri', 'track_href','analysis_url', 'song_name','Unnamed: 0','title','time_signature',
                      'mode', 'key'])

df['genre_encoded'] = LabelEncoder().fit_transform(df['genre'])
le = LabelEncoder()
le.fit(df['genre'])
le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
print(le_name_mapping)


X = df.drop(columns=['genre', 'genre_encoded'])
y = df['genre_encoded']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

std = StandardScaler().fit(X_train[['tempo']])
X_train['tempo'] = std.transform(X_train[['tempo']])
X_test['tempo'] = std.transform(X_test[['tempo']])

std = StandardScaler().fit(X_train[['duration_ms']])
X_train['duration_ms'] = std.transform(X_train[['duration_ms']])
X_test['duration_ms'] = std.transform(X_test[['duration_ms']])





# df = df.sample(frac=1)
# df_random.to_csv('now.csv')




from xgboost import XGBClassifier
xgb = XGBClassifier(n_jobs = -1)
params = {
    'learning_rate':[0.01,0.03,0.05,0.1,0.15,0.2],
    'n_estimators':[100,200,350,500,1000,2000],
    'max_depth':[2,3,5,8,10],
    'colsample_bytree':[0.1,0.3,0.5,1],
    'colsample_bylevel':[0.1,0.3,0.5,1],
    'reg_alpha' : [0.001,0.01,0.1,1,10],
    'reg_lambda' : [0.001,0.01,0.1,1,10],
    'subsample':[0.1,0.3,0.5,1]
    }
# clf = RandomizedSearchCV(xgb, params, cv=5, scoring='f1_micro', n_jobs=-1, verbose=10)
# clf.fit(X_train, y_train)
# print(clf.best_estimator_)
# print(clf.best_params_)
clf = XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=0.5, gamma=0, gpu_id=-1,
              importance_type='gain', interaction_constraints='',
              learning_rate=0.15, max_delta_step=0, max_depth=2,
              min_child_weight=1, monotone_constraints='()',
              n_estimators=500, n_jobs=-1, num_parallel_tree=1,
              objective='multi:softprob', random_state=0, reg_alpha=1,
              reg_lambda=0.001, scale_pos_weight=None, subsample=1,
              tree_method='exact', validate_parameters=1, verbosity=None)
clf.fit(X_train,y_train)
clf.save_model('my_model.json')
y_train_pred = clf.predict(X_train)
y_pred = clf.predict(X_test)

# Train Confusion Matrix
# plot_confusion_matrix(y_train,y_train_pred, 'Train Confusion Matrix')
# Test Confusion Matrix
# plot_confusion_matrix(y_test,y_pred, 'Test Confusion Matrix')
print('Train F1 Score is {0}'.format(f1_score(y_train,y_train_pred,average='micro')))
print('Test F1 Score is {0}'.format(f1_score(y_test,y_pred,average='micro')))