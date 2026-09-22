from itertools import groupby

import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    data = pd.read_csv("customer_data.csv", header=0)

    # TASK 1: Thống kê số lượng khách hàng theo học vấn
    count_customers = data['educational_level'].value_counts()
    print(count_customers.to_string())
    print("\n")

    # TASK 2: In ra 20 khác hàng có thu nhập cá nhân cao nhất
    sorted_customers_annual_income = data.sort_values(by=['annual_income'], ascending=False)
    top20_annual_income_highest = sorted_customers_annual_income.head(20)
    print(top20_annual_income_highest.to_string())
    print("\n")

    # TASK 3: In ra những khách hàng sinh sau năm 1960 và thu nhập cá nhân trên $50,000/năm
    value_task3 = data.query('year_of_birth > 1960 and annual_income > 50000')
    print(value_task3.to_string())
    print("\n")

    # TASK 4: Kết hợp điều kiện task 2 và task 3
    value_task4 = data.query('year_of_birth > 1960 and annual_income > 50000').nlargest(20, 'annual_income')
    print("\n")

    # TASK 5: In ra những khách hàng có tình trạng hôn nhân là đã kết hôn hoặc đã ly hôn
    value_task5 = data[data['marital_status'].isin(['Married', 'Divorced'])]
    print(value_task5.to_string())
    print("\n")

    # TASK 6: Tính thu nhập trung bình theo trình độ học vấn
    value_task6 = data.groupby('educational_level')['annual_income'].mean()
    print(value_task6.to_string())
    print("\n")

    # TASK 7: Tính thu nhập trung bình theo trình độ học vấn + tình trạng hôn nhân
    value_task7 = data.groupby(['educational_level' ,'marital_status'])['annual_income'].mean()
    print(value_task7.to_string())
    print("\n")

    # TASK 8: