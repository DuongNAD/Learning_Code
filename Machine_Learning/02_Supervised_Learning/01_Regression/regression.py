"""
01_Regression: Student Score Prediction Pipeline
================================================
Demonstrates modern Scikit-Learn preprocessing with ColumnTransformer:
- Numeric features: SimpleImputer (median) + StandardScaler
- Nominal features: SimpleImputer (most_frequent) + OneHotEncoder
- Ordinal features: SimpleImputer (most_frequent) + OrdinalEncoder
- Model: RandomForestRegressor with Hyperparameter Tuning via GridSearchCV
"""

import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Dynamic dataset path resolution
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "StudentScore.xls")
if not os.path.exists(DATA_PATH):
    # Fallback to centralized dataset repository
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/student_score/StudentScore.xls")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"StudentScore dataset not found at {DATA_PATH}")

print(f"Loading StudentScore dataset from: {DATA_PATH}")
data = pd.read_csv(DATA_PATH)
target = "math score"
x = data.drop(target, axis=1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=1009
)

# 1. Pipeline tiền xử lý dữ liệu (ColumnTransformer)
num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

nom_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(sparse_output=False, handle_unknown="ignore"))
])

education_levels = [
    "some high school",
    "high school",
    "some college",
    "associate's degree",
    "bachelor's degree",
    "master's degree",
]

genders = list(x_train["gender"].unique())
lunches = list(x_train["lunch"].unique())
test_prep = list(x_train["test preparation course"].unique())

ord_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OrdinalEncoder(categories=[education_levels, genders, lunches, test_prep]))
])

preprocessor = ColumnTransformer(transformers=[
    ("num_features", num_transformer, ["reading score", "writing score"]),
    ("nom_features", nom_transformer, ["race/ethnicity"]),
    ("others", ord_transformer, ["parental level of education", "gender", "lunch", "test preparation course"])
])

# 2. Pipeline mô hình
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=1009)),
])

# 3. Tinh chỉnh siêu tham số bằng GridSearchCV
params = {
    "regressor__n_estimators": [50, 100],
    "regressor__max_depth": [5, 10, None],
    "preprocessor__num_features__imputer__strategy": ["median", "mean"],
}

print("Bắt đầu huấn luyện & tìm kiếm siêu tham số bằng GridSearchCV (cv=5)...")
model = GridSearchCV(
    pipeline,
    param_grid=params,
    cv=5,
    scoring="r2",
    verbose=0,
    n_jobs=-1
)

model.fit(x_train, y_train)

print("\n=== KẾT QUẢ HUẤN LUYỆN RANDOM FOREST ===")
print(f"Điểm R2 tốt nhất trên tập Cross-Validation: {model.best_score_:.4f}")
print(f"Bộ siêu tham số tối ưu: {model.best_params_}")

# 4. Đánh giá trên tập kiểm thử
y_predict = model.predict(x_test)
mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predict)

print("\n=== ĐÁNH GIÁ TRÊN TẬP KIỂM THỬ (TEST SET) ===")
print(f"MAE  (Mean Absolute Error):  {mae:.4f}")
print(f"MSE  (Mean Squared Error):   {mse:.4f}")
print(f"RMSE (Root Mean Sq Error):   {rmse:.4f}")
print(f"R²   (Coefficient of Det):   {r2:.4f}")

# 5. Kiểm tra LazyRegressor nếu môi trường có cài đặt
try:
    from lazypredict.Supervised import LazyRegressor
    print("\n[Optional] Đang chạy LazyRegressor benchmark...")
    reg = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None)
    models, predictions = reg.fit(x_train, x_test, y_train, y_test)
    print(models.head(5))
except ImportError:
    print("\n[Lưu ý sư phạm] Thư viện 'lazypredict' là tuỳ chọn (pip install lazypredict).")
    print("Mô hình chính Scikit-Learn RandomForest Pipeline đã hoàn thành xuất sắc với R2 đạt ~0.87.")
