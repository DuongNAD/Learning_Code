import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())
print(df['Outcome'].value_counts())
print(df['Outcome'].value_counts(normalize=True))

df.hist(figsize=(12, 8), bins=20)
plt.tight_layout()
plt.show()

