import matplotlib.pyplot as plt
import pandas as pd


sales_data = 'sales_data.csv'

df = pd.read_csv(sales_data, sep=',', index_col=['purchase-date'],
                   usecols=['purchase-date', 'quantity'],
                   parse_dates=True, encoding="utf8")
# print(df)


df = df.set_index([df.index.hour, df.index.weekday, df.index])
df.index.names = ['hour', 'weekday', 'day']
# print(df)

# weekday
df_weekday = df.sum(level='weekday')
df_weekday = df_weekday.sort_index(axis=0)
plt.figure()
df_weekday.plot()
plt.savefig("image_weekday.png")
# print(df_weekday)

# hour
df_hour = df.sum(level='hour')
df_hour = df_hour.sort_index(axis=0)
plt.figure()
df_hour.plot()
plt.savefig("image_hour.png")
# print(df_hour)

