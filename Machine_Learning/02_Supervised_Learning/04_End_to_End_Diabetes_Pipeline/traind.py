from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from b4_split import y_train, y_test
from b5_feature import X_train_standard, X_test_standard

models = {
    "Logistic Regression": LogisticRegression(),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(),
}

for name, model in models.items():
    model.fit(X_train_standard, y_train)
    score = model.score(X_test_standard, y_test)
    print(f"{name}: {score:.4f}")
