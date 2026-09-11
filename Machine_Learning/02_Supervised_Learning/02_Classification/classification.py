import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pickle
from lazypredict.Supervised import LazyClassifier
# from ydata_profiling import ProfileReport

data = pd.read_csv("diabetes.csv")
# profile = ProfileReport(data, title="Diabetes Report")
# profile.to_file("diabetes_report.html")
target = "Outcome"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=1009
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# clf = LazyClassifier(verbose=0,ignore_warnings=True, custom_metric=None)
# models, predictions = clf.fit(x_train, x_test, y_train, y_test)
params = {
    "n_estimators": [100, 500, 1000],
    "criterion": ["gini", "entropy", "log_loss"],
    # "max_depth": [None, 2, 5, 10]
}

model = GridSearchCV(
    RandomForestClassifier(random_state=100),
    param_grid=params,
    cv=6,
    scoring="f1",
    verbose=2,
    n_jobs=6
)

model.fit(x_train, y_train)
print(model.best_score_)
print(model.best_params_)

with open('model.pkl', 'wb') as file:
    pickle.dump([model, scaler], file)

y_predict = model.predict(x_test)
# for i,j in zip(y_predict, y_test):
#     print("Prediction: {}. Actual value: {}".format(i,j))
print(classification_report(y_test, y_predict))
# print(confusion_matrix(y_test, y_predict))
