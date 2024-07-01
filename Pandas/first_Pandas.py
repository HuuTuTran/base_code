import pandas as pd
df = pd.read_csv("world_data.csv")
# df = pd.read_csv("world_data.csv", index_col='Country Name', parse_dates=True)

# print(df)
 
# df.tail()
# df.head()
# print(df.head())
# print(df.describe())
# print(df['Country Name'])
country_name = pd.Series(df['Country Name'])
country_code = pd.Series(df['Country Code'])
population = pd.Series(df[' Population, total '])
gdp = pd.Series(df['GDP, PPP (current international $)'])
internet_users = pd.Series(df['Internet users (per 100 people)'])
life_expectancy = pd.Series(df['2014 Life expectancy at birth, total (years)'])
literacy_rate = pd.Series(df['Literacy rate, adult female (% of females ages 15 and above)'])
exports = pd.Series(df['Exports of goods and services (% of GDP)'])

literacy_rate_sorted = literacy_rate.sort_values(ascending=True)

# print(literacy_rate_sorted)
combination = pd.merge(pd.DataFrame({'key': literacy_rate_sorted.index, 's1_values': literacy_rate_sorted.values}), 
              pd.DataFrame({'key': country_name.index, 's2_values': country_name.values}), 
              on='key')

# print(combination)

# lst = [1,2,3,4]
# print(pd.Series(lst).mean())
# combination = pd.concat([])
# import pandas as pd

# create two sample Series
# s1 = pd.Series(['a1', 'a2', 'a3'])
# s2 = pd.Series(['a', 'b', 'c'])

# # combine the two Series into a DataFrame
# df = pd.concat([s1, s2], axis=1)

# print(df)

# sp_prices = [('A', 68.06),
#  ('FB', 51.4),
#  ('AAP', 109.93),
#  ('AAPL', 159.54),
#  ('ABBV', 113.62),
#  ('NFLX', 94.22),
#  ('ABT', 58.67),
#  ('ACN', 155.15),
#  ('AMZN', 192.34),
#  ('GOOGL', 85.35)]

# faang_tickers = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOGL']


# print([ [j[1] for j in sp_prices if j[0]==i ][0]  for i in  faang_tickers ])
# no_exam = [(student_ids[attendences.index(i)],names[attendences.index(i)])  for i in attendences if i != 'Present' ]
