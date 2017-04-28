
"""

Python module for getting stock data
@module: pinance
@author: neberej (https://github.com/neberej)
@version: 1.00

"""


# Dependencies
from datetime import datetime, timedelta
from urllib.request import urlopen
from urllib.parse import urlencode
from simplejson import loads
import pytz


# Create a YQL query
def make_query(symbol):
  query = 'select * from yahoo.finance.quotes where symbol = "{symbol}"'.format(symbol=symbol)
  req = urlopen('https://query.yahooapis.com/v1/public/yql?' + urlencode({
      'q': query,
      'format': 'json',
      'env': 'store://datatables.org/alltableswithkeys'
  }))
  return loads(req.read())


def make_request(symbol):
  response = make_query(symbol)
  try:
    _, results = response['query']['results'].popitem()
    if (results["Name"]):
      return results
    return []
    
  except (KeyError, StopIteration, AttributeError):
    try:
      return []
    except KeyError:
      return []
    else:
      return []


def get_quotes(symbol):
  response = make_request(symbol)
  if response:
    return response
  return []