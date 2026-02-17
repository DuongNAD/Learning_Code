import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    data = pd.read_csv(filepath_or_buffer='city_population.csv',header=0)

    # TAST 1: In ra 10 thành phố có dân số lớn nhất & 10 thành phố có dân số nhỏ nhất
    df_sorted = data.sort_values(by=['Population'], ascending=False)
    print("======================== 10 Thành phố có dân số lớn nhất ========================")
    print(df_sorted.head(10))
    print("\n")
    print("======================== 10 Thành phố có dân số nhỏ nhất ========================")
    print(df_sorted.tail(10).sort_values(by=['Population'], ascending=True))
    print("\n")

    # TAST 2: In ra các quốc gia có tối thiểu 3 thành phố
    print("======================== Các quốc gia có 3 thành phố trở lên ========================")
    country_counts = data['Country'].value_counts()
    target_countries = country_counts[country_counts >= 3]
    print(target_countries.index.tolist())
    print("\n")

    # TASK 3: In ra top 5 quốc gia có nhiều thành phố xuất hiện nhất
    print("======================== Top 5 quốc gia có nhiều thành phố xuất hiện nhất ========================")
    top5_countries = country_counts.head(5)
    print(top5_countries.index.tolist())
    print("\n")

    # TASK 4: In ra các thành phố có dân số & diện tích đều nằm trong top 20
    print("======================== Các thành phố có dân số & diện tích đều trong top 20 ========================")
    top20_pop_cities = data.nlargest(20, 'Population')['City']
    top20_area_cities = data.nlargest(20, 'Area_KM2')['City']

    df_top20_pop_area = data[data['City'].isin(top20_pop_cities) & data['City'].isin(top20_area_cities) ]
    top20_cities = sorted(list(set(df_top20_pop_area['City'])))
    print(top20_cities)
    print("\n")

    # TASK 5: Thống kê mật độ dân số theo quốc gia
    print("======================== Thống kê mật độ dân số theo quốc gia ========================")
    country_stats = data.groupby('Country')[['Population', 'Area_KM2']].sum()
    country_stats['Density_KM2'] = country_stats['Population'] / country_stats['Area_KM2']
    sountry_stats_result = country_stats.sort_values(by=['Density_KM2'], ascending=False)
    print(sountry_stats_result)
    print("\n")

    #TASK 6: Thống kê các thành phố có dân số lớn nhất của từng quốc gia (Chỉ tính những quốc gia có 2 thành phố trở lên)
    print("======================== Thống kê các thành phố có dân số lớn nhất của từng quốc gia ========================")
    valid_country = country_counts[country_counts >= 2].index
    more_than_2_countries = data[data['Country'].isin(valid_country)]

    stats_max_pop_countries = more_than_2_countries.sort_values(by=['Population'], ascending=False).groupby('Country').head(1)
    print(stats_max_pop_countries)
    print("\n")

