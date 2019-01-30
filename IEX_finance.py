'''
pip install iexfinance

'''

import datetime

from iexfinance.stocks import get_historical_data


start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2019, 1, 1)

df = get_historical_data('TSLA', start, end, output_format='pandas')
