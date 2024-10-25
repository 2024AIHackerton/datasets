import pandas as pd

tm1 = "20140101"
tm2 = "20141231"

filename = f"./data/column_filtered/weather_data_{tm1}_{tm2}_filtered.csv"
num_filtered_filename = f'./data/number_filtered/weather_data_{tm1}_{tm2}_num_filtered.csv'

df = pd.read_csv(filename)

df['RN_DAY'] = df['RN_DAY'].replace(-9, 0)

df.to_csv(num_filtered_filename)