
import sys
sys.path.append('../pinance/engine')

import gfinance
import gfinancenews
import yfinance
import yfinance2
from datetime import datetime, timedelta

millnames = ['','T','M','B','T']


# Human readable numbers
def millify(n):
  n = float(n)
  millidx = max(0,min(len(millnames)-1,
                      int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
  return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])


# Check if dictionary
def isValid(item):
  if(type(item) is dict):
    return True
  return False


# Combine data from all three sources and remove all keys which has 'None' as values
def combine_objects(a, b, c):
  data = {}
  if isValid(a):
    data.update(a)
  if isValid(b):
    data.update(b)
  if isValid(c):
    data.update(c)
  res = {k:v for k,v in data.items() if v is not None}
  return res
  
# Convert date/time to unix time for options
def totimestamp(inputdate, epoch=datetime(1970,1,1)):
  dt = datetime.strptime(inputdate, '%Y-%m-%d')
  td = dt - epoch
  timestamp = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6 # td.total_seconds()
  return int(timestamp)


# Extract expiry, call/put and strike price (allows to enter them on any order)
def options_params(a, b, c):
  expiry = totimestamp(a)
  return expiry, b, c


class Base(object):


  def __init__(self, symbol):
    self.symbol = symbol


  def __request_quotes__(self):
    gfinance_data = gfinance.get_quotes(self.symbol)
    yfinance_data = yfinance.get_quotes(self.symbol)
    yfinance2_data = yfinance2.get_quotes(self.symbol)
    return combine_objects(gfinance_data, yfinance_data, yfinance2_data)

  def __request_news__(self):
    gfinance_news = gfinancenews.get_news(self.symbol)
    return gfinance_news

  def __request_options__(self, a, b, c):
    yfinance2_options = yfinance2.get_options(self.symbol, a, b, c)
    return yfinance2_options

  def __getQuotes__(self):
    self.quotes_data = self.__request_quotes__()

  def __getNews__(self):
    self.news_data = self.__request_news__()

  def __getOptions__(self, a, b, c):
    expiry, type, strike = options_params(a, b, c)
    self.options_data = self.__request_options__(expiry, type, strike)


class Pinance(Base):

  def __init__(self, symbol):
    super(Pinance, self).__init__(symbol)
    self.symbol = symbol

  def get_quotes(self):
    self.__getQuotes__()

  def get_news(self):
    self.__getNews__()

  def get_options(self, a, b, c):
    self.__getOptions__(a, b, c)

  def quotes_data(self):
    return self.quotes_data

  def news_data(self):
    return self.news_data

  def options_data(self):
    return self.options_data
