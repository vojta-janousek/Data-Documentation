'''

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime


my_year = 2017
my_month = 2
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

my_date = datetime(my_year, my_month, my_day)
my_date_time = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)
my_date_time.day # -> 2

# Using DateTime as an index
first_two = [datetime(2016, 1, 1), datetime(2016, 1, 2)]
dt_ind = pd.DatetimeIndex(first_two)
df = pd.DataFrame(data=np.random.randn(2,2), index=dt_ind, columns=['A', 'B'])

df_wall = pd.read_csv('walmart_stock.csv')

# df_wall.info() -> Date is a non-null object (string)
# Convert Date to DateTime format
df_wall['Date'] = pd.to_datetime(df_wall['Date'])
df_wall.set_index('Date', inplace=True)
# Alternatively
df_wall_alter = pd.read_csv('walmart_stock.csv', index_col='Date', parse_dates=True)

# Annual resampling
df_wall.resample(rule='A').mean()

# Custom functions can be used
df_wall.resample('Q').apply(lambda entry: entry[0])
#
df_wall['Close'].resample('A').mean().plot(kind='bar')

# Shift index by 1
df.shift(periods=1)
# Shift index to the end of month day
df.tshift(freq='M')
