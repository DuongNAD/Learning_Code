import pandas as pd
import re
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_selection import SelectKBest, chi2, SelectPercentile
from imblearn.over_sampling import RandomOverSampler, SMOTEN


def filter_location(location):
    # if location[-4:-2] == ", " and location[-2:].isupper():
    #     return location[-2:]
    # else:
    #     return location
    result = re.findall(pattern="\,\s[A-Z]{2}$", string=location)
    if len(result) == 0:
        return location
    else:
        return location[0][-2:]


import os
if os.path.exists("final_project.csv"):
    data = pd.read_csv("final_project.csv", dtype=str)
else:
    data = pd.read_excel("final_project.ods", dtype=str)
data = data.dropna(axis=0)
data["location"] = data["location"].apply(filter_location)
target = "career_level"

x = data.drop(target, axis=1)
y = data[target]
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=1009,
    stratify=y
)
print(y_train.value_counts())
print("-----------------")
sampler = SMOTEN(
    sampling_strategy={
        "managing_director_small_medium_company": 500,
        "specialist": 500,
        "director_business_unit_leader": 500,
        "bereichsleiter": 1000
    },
    k_neighbors=2,
    random_state=0
)
x_train, y_train = sampler.fit_resample(x_train, y_train)
print(y_train.value_counts())
exit(0)

preprocessor = ColumnTransformer(transformers=[
    ("tit", TfidfVectorizer(), "title"),
    ("loc", OneHotEncoder(handle_unknown="ignore"), ["location"]),
    ("desc", TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.99, stop_words="english"), "description"),
    ("func", OneHotEncoder(handle_unknown="ignore"), ["function"]),
    ("ind", TfidfVectorizer(), "industry")
])

# unigram+bigram: (6458, 848501)
# unigram+bigram+min_df+max_df: (6458, 7954)

# output = preprocessor.fit_transform(x_train)
# print(output.shape)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    # ("feature_selector", SelectKBest(chi2, k=500)),
    ("feature_selector", SelectPercentile(chi2, percentile=8)),
    ("regressor", RandomForestClassifier(random_state=1009)),
])

model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict))
#                                         precision    recall  f1-score   support
#
#                         bereichsleiter       0.56      0.14      0.23       192
#          director_business_unit_leader       1.00      0.07      0.13        14
#                    manager_team_leader       0.65      0.73      0.69       534
# managing_director_small_medium_company       0.00      0.00      0.00         1
#   senior_specialist_or_project_manager       0.84      0.93      0.88       868
#                             specialist       0.00      0.00      0.00         6
#
#                               accuracy                           0.76      1615
#                              macro avg       0.51      0.31      0.32      1615
#                           weighted avg       0.75      0.76      0.73      1615
