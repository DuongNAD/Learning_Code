from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from b4_split import y_train, y_test
from b5_feature import X_train_standard, X_test_standard

# --- Tune Decision Tree ---
grid_dt = GridSearchCV(
    DecisionTreeClassifier(),
    {"max_depth": [3, 5, 10, 15, None], "min_samples_split": [2, 5, 10], "min_samples_leaf": [1, 2, 5]},
    cv=5, scoring="accuracy"
)
grid_dt.fit(X_train_standard, y_train)
print("Decision Tree best:", grid_dt.best_params_, grid_dt.best_score_)

# --- Tune Random Forest ---
grid_rf = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {"n_estimators": [50, 100, 200], "max_depth": [3, 5, 10, None], "min_samples_split": [2, 5, 10]},
    cv=5, scoring="accuracy"
)
grid_rf.fit(X_train_standard, y_train)
print("Random Forest best:", grid_rf.best_params_, grid_rf.best_score_)

# --- Tune KNN ---
grid_knn = GridSearchCV(
    KNeighborsClassifier(),
    {"n_neighbors": [3, 5, 7, 9, 11], "weights": ["uniform", "distance"]},
    cv=5, scoring="accuracy"
)
grid_knn.fit(X_train_standard, y_train)
print("KNN best:", grid_knn.best_params_, grid_knn.best_score_)
