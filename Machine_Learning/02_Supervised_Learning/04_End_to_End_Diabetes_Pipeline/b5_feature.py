from b4_split import X_train, X_test
from sklearn.preprocessing import StandardScaler, MinMaxScaler

MinMax_scaler = MinMaxScaler()
Standard_scaler = StandardScaler()

MinMax_scaler.fit(X_train)
X_train_minmax = MinMax_scaler.transform(X_train)
X_test_minmax = MinMax_scaler.transform(X_test)

Standard_scaler.fit(X_train)
X_train_standard = Standard_scaler.transform(X_train)
X_test_standard = Standard_scaler.transform(X_test)

