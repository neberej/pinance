
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


# Make request to google finance
def makeRequest(symbol):
  url = 'http://www.google.com/finance/company_news?output=json&q=' \
        + symbol + '&start=0&num=1000'
  try:
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()

    content_json = demjson.decode(content)
    clusters = content_json['clusters']
    if clusters[0]:
      return clusters[0]["a"]
    return []
  except urllib.error.URLError as e:
    return []
  except urllib.error.HTTPError as e:
    return []


def get_news(symbol):
  response = makeRequest(symbol)
  if response:
    return response
  return []
