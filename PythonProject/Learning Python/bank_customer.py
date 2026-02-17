import pandas as pd
from pandas import set_option

df = pd.read_csv("Bank Customer Churn Prediction.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# TASK 1: Tìm ra top 20 người có credit_score (Điểm tín dụng) cao nhất
df_sorted_credit_score = df.sort_values(by='credit_score',ascending=False)
print(df_sorted_credit_score.head(20))
print("\n")

# TASK 2: Tìm top 10 người 35 - 50 tuổi có balance (số dư) lớn nhất
df_filtered_old = df.query("30 <= age <= 50")
result = df_filtered_old.sort_values(by='balance',ascending=False).head(10)
print(result)
print("\n")

# TASK 3: Tìm quốc gia có credit_score (điểm tín dụng) cao nhất
country_dict = {}
country_sum_credit_score = {}

countries = df['country'].unique()
for country in countries:
    people_country = df[df['country'] == country]
    country_dict[country] = people_country
    country_sum_credit_score[country] = None

for key, value in country_dict.items():
    total_credit_score = int(value['credit_score'].sum())
    country_sum_credit_score[key] = total_credit_score

highest_name = max(country_sum_credit_score, key=country_sum_credit_score.get)
highest_credit_score = country_sum_credit_score[highest_name]
print(country_sum_credit_score)
print(highest_name,":",highest_credit_score)


