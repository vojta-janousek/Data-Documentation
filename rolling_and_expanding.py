'''

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('walmart_stock.csv', index_col='Date', parse_dates=True)

# Rolling mean cancels the data 'noise'. The higher the window, the lower the noise.
df['Open'].plot()
df.rolling(window=7).mean()['Close'].plot(figsize=(16,6))

#
df['Close 30 day MA'] = df['Close'].rolling(window=30).mean()
df[['Close 30 day MA', 'Close']].plot(figsize=(16,6))

# Expanding takes into account all previous values. Each point is a mean
# of all points before it.
df['Close'].expanding().mean().plot(figsize=(16,6))

# Bollinger Bands indicate current volatility.
df['Close: 20 Day Mean'] = df['Close'].rolling(20).mean()

# Upper band = 20MA + 2*std(20)
df['Upper'] = df['Close: 20 Day Mean'] + 2*(df['Close'].rolling(20).std())
# Lower band = 20MA - 2*std(20)
df['Lower'] = df['Close: 20 Day Mean'] - 2*(df['Close'].rolling(20).std())

df[['Close', 'Close: 20 Day Mean', 'Upper', 'Lower']].tail(200).plot(figsize=(16,6))
