
"""

Python module for getting stock data
@module: pinance
@author: neberej (https://github.com/neberej)
@version: 1.00

"""

# Dependencies
import demjson
import json
import sys
import re
import urllib
from urllib.request import Request, urlopen

# Human readable texts
mapping = {
  u'id'     : u'ID',
  u't'      : u'StockSymbol',
  u'e'      : u'Index',
  u'l'      : u'LastTradePrice',
  u'l_cur'  : u'LastTradeWithCurrency',
  u'ltt'    : u'LastTradeTime',
  u'lt_dts' : u'LastTradeDateTime',
  u'lt'     : u'LastTradeDateTimeLong',
  u'div'    : u'Dividend',
  u'yld'    : u'Yield',
  u's'      : u'LastTradeSize',
  u'c'      : u'Change',
  u'c'      : u'ChangePercent',
  u'el'     : u'ExtHrsLastTradePrice',
  u'el_cur' : u'ExtHrsLastTradeWithCurrency',
  u'elt'    : u'ExtHrsLastTradeDateTimeLong',
  u'ec'     : u'ExtHrsChange',
  u'ecp'    : u'ExtHrsChangePercent',
  u'pcls_fix': u'PreviousClosePrice'
}

# Replace keys on response using mapping object
def replaceKeys(quotes):
  global mapping
  quotesWithReadableKey = []
  for q in quotes:
    qReadableKey = {}
    for k in mapping:
      if k in q:
        qReadableKey[mapping[k]] = q[k]
      quotesWithReadableKey.append(qReadableKey)
  return quotesWithReadableKey


# Make request to google finance
def makeQuotesRequest(symbol):
  url = 'https://finance.google.com/finance/info?client=ig&q=' \
      + symbol
  try:
    req = Request(url)
    resp = urlopen(req)
    content = resp.read().decode('ascii', 'ignore').strip()
    content = json.loads(content[3:])
    return replaceKeys(content);
  except urllib.error.URLError as e:
    return []
  except urllib.error.HTTPError as e:
    return []


def get_quotes(symbol):
  response = makeQuotesRequest(symbol)
  if response:
    return response[0]
  return []
