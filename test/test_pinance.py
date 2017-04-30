

import sys
sys.path.append('../pinance')
from pytz import timezone
from datetime import datetime, timedelta
from __init__ import Pinance 

symbol = "AMD"


stock = Pinance(symbol)

# Stock
stock.get_quotes()
print(stock.quotes_data)

# News
stock.get_news()
print(stock.news_data)

# Option
stock.get_options('2017-05-05', 'P', 10)
print(stock.options_data)
