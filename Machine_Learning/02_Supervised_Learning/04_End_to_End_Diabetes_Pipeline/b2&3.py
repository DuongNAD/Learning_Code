import pandas as pd

df = pd.read_csv('diabetes.csv')

def remove_outliers(df, column_name):
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df[column_name] >= Q1 - 1.5*IQR) & (df[column_name] <= Q3 + 1.5*IQR)]
    return df

df = df[(df['Glucose'] > 0) & (df['BloodPressure'] > 0) & (df['SkinThickness'] > 0) & (df['Insulin'] > 0) & (df['BMI'] > 0)]

df = remove_outliers(df, 'Glucose')
df = remove_outliers(df, 'BloodPressure')
df = remove_outliers(df, 'SkinThickness')
df = remove_outliers(df, 'Insulin')
df = remove_outliers(df, 'BMI')

df.to_csv('diabetes_cleaned.csv', index=False)

