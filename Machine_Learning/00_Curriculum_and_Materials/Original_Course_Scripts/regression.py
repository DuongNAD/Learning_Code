import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from lazypredict.Supervised import LazyRegressor
# from data_profiling import ProfileReport

data = pd.read_csv("StudentScore.xls")
# profile = ProfileReport(data, title="Student Report")
# profile.to_file("student_report.html")
target = "math score"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=1009
)

num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

nom_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(sparse_output=False))
])

education_levels = [
    "some high school",
    "high school",
    "some college",
    "associate's degree",
    "bachelor's degree",
    "master's degree",
]

genders = x_train["gender"].unique()
lunches = x_train["lunch"].unique()
test_prep = x_train["test preparation course"].unique()

ord_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[education_levels, genders, lunches, test_prep]))
])

preprocessor = ColumnTransformer(transformers=[
    ("num_features", num_transformer, ["reading score", "writing score"]),
    ("nom_features", nom_transformer, ["race/ethnicity"]),
    ("others", ord_transformer, ["parental level of education", "gender", "lunch", "test preparation course"])
])

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=1009)),
])

params = {
    "regressor__n_estimators": [20, 50, 100],
    "regressor__criterion": ["squared_error", "absolute_error", "friedman_mse"],
    "preprocessor__num_features__imputer__strategy": ["median", "mean"],
}

model = GridSearchCV(
    pipeline,
    param_grid=params,
    cv=6,
    scoring="r2",
    verbose=1,
    n_jobs=6
)

# model.fit(x_train, y_train)
# print(model.best_score_)
# print(model.best_params_)
# y_predict = model.predict(x_test)
# print("MAE: {}".format(mean_absolute_error(y_test, y_predict)))
# print("MSE: {}".format(mean_squared_error(y_test, y_predict)))
# print("R2: {}".format(r2_score(y_test, y_predict)))
reg = LazyRegressor(verbose=0,ignore_warnings=False, custom_metric=None )
models,predictions = reg.fit(x_train, x_test, y_train, y_test)

