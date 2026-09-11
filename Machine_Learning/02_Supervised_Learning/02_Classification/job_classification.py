"""
02_Classification: Job Career Level NLP Classification
=====================================================
Multi-class text classification pipeline handling extreme class imbalance:
- Regex feature extraction for job locations
- Multi-channel TF-IDF Vectorization across title, description, and industry
- One-Hot Encoding for categorical features (location, function)
- Class-weight balancing with RandomForest to handle imbalanced career levels
- Optional SMOTEN oversampling when `imblearn` is installed
"""

import os
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(CURRENT_DIR, "final_project.csv")
ODS_PATH = os.path.join(CURRENT_DIR, "final_project.ods")

# Dynamic data file resolution
if os.path.exists(CSV_PATH):
    print(f"Loading pre-parsed CSV data: {CSV_PATH}")
    data = pd.read_csv(CSV_PATH, dtype=str)
elif os.path.exists(ODS_PATH):
    print(f"Loading ODS data: {ODS_PATH}")
    data = pd.read_excel(ODS_PATH, dtype=str)
else:
    fallback = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/job_classification/final_project.csv")
    if os.path.exists(fallback):
        print(f"Loading from dataset store: {fallback}")
        data = pd.read_csv(fallback, dtype=str)
    else:
        raise FileNotFoundError("Could not locate final_project dataset.")


def filter_location(location):
    """Trích xuất mã tiểu bang 2 chữ cái (ví dụ ', CA' -> 'CA') nếu có."""
    if not isinstance(location, str):
        return "UNKNOWN"
    result = re.findall(r"\,\s([A-Z]{2})$", location)
    if len(result) == 0:
        return location
    return result[0]


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

print("\n=== PHÂN BỐ CÁC LỚP NGHỀ NGHIỆP TRONG TẬP TRAIN ===")
print(y_train.value_counts())

# Thử nghiệm oversampling bằng SMOTEN nếu có imblearn
has_imblearn = False
try:
    from imblearn.over_sampling import SMOTEN
    has_imblearn = True
    print("\n[SMOTEN] Phát hiện thư viện imblearn, áp dụng SMOTEN oversampling...")
    # Chỉ resample các lớp có ít nhất 2 mẫu
    valid_classes = y_train.value_counts()
    strategy = {}
    for cls_name, cnt in valid_classes.items():
        if cnt >= 2 and cnt < 500:
            strategy[cls_name] = 500
    if strategy:
        sampler = SMOTEN(sampling_strategy=strategy, k_neighbors=1, random_state=0)
        x_train_resampled, y_train_resampled = sampler.fit_resample(x_train, y_train)
        x_train, y_train = x_train_resampled, y_train_resampled
        print("Phân bố sau SMOTEN:")
        print(y_train.value_counts())
except ImportError:
    print("\n[Lưu ý] 'imblearn' không cài đặt -> Áp dụng phương pháp Scikit-Learn Native: class_weight='balanced'")

# Xây dựng ColumnTransformer xử lý đa nguồn văn bản & biến định danh
preprocessor = ColumnTransformer(transformers=[
    ("tit", TfidfVectorizer(max_features=1000), "title"),
    ("loc", OneHotEncoder(handle_unknown="ignore"), ["location"]),
    ("desc", TfidfVectorizer(max_features=3000, stop_words="english", ngram_range=(1, 2)), "description"),
    ("func", OneHotEncoder(handle_unknown="ignore"), ["function"]),
    ("ind", TfidfVectorizer(max_features=500), "industry")
])

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=50,
        class_weight="balanced",
        random_state=1009,
        n_jobs=-1
    )),
])

print("\nĐang huấn luyện mô hình phân loại đa lớp...")
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

print("\n=== MA TRẬN NHẦM LẪN (CONFUSION MATRIX) ===")
print(confusion_matrix(y_test, y_predict))

print("\n=== BÁO CÁO PHÂN LOẠI (CLASSIFICATION REPORT) ===")
print(classification_report(y_test, y_predict, zero_division=0))
