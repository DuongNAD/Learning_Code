import pandas as pd

from sklearn.model_selection import train_test_split


df = pd.read_csv("diabetes_cleaned.csv")
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("Train shape: ", X_train.shape)
print("Test shape: ", X_test.shape)

