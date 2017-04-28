
"""

Python module for getting stock data
@module: pinance
@author: neberej (https://github.com/neberej)
@version: 1.00

"""

import urllib.request, urllib.error, urllib.parse
import time
from random import randrange
from datetime import datetime
from datetime import date
from datetime import timedelta
import json

# Create URL (select query1 or query2 randomly)
def create_url(ticker, expiry):
  srv = randrange(1, 3, 1)
  if expiry:
    return 'https://query{}.finance.yahoo.com/v7/finance/options/{}?&date={}'.format(srv, ticker, expiry)
  else:
    return 'https://query{}.finance.yahoo.com/v7/finance/options/{}'.format(srv, ticker)

# Make request to yahoo finance
def make_request(ticker, expiry):
  if expiry:
    url = create_url(ticker, expiry)
  else:
    url = create_url(ticker, None)

  try:
    response = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
  except urllib.error.URLError as e:
    if hasattr(e, 'reason'):
      return []
    elif hasattr(e, 'code'):
      return []
  return response


def extract_options_data(response, type, strike):
  #print(response['optionChain']['result'][0]['options'][0])
  if type == 'C':
    calls = response['optionChain']['result'][0]['options'][0]['calls']
    for call in calls:
      if call['strike'] == round(strike, 1):
        return call

  elif type == 'P':
    puts = response['optionChain']['result'][0]['options'][0]['puts']
    for put in puts:
      if put['strike'] == round(strike, 1):
        return put

  return []

def get_options(ticker, a, b, c):
  response = make_request(ticker, a)
  try:
    options_data = extract_options_data(response, b, c)  #options is options
    return options_data
  except:
    return []

