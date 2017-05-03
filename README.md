pinance
=========

A collection of python modules to get finance data (stock quotes, options data and news)


## Modules list

* yfinance - Gets stock data from Yahoo API
* yfinance2 - Gets options data from Yahoo Finance API
* gfinance - Gets stock data from Google Finance
* gfinance.py - Gets news from Google Finance Page


## Installation


* From repo

```
$ git clone git://github.com/neberej/pinance.git
$ cd pinance
$ python setup.py install
```

* From PyPI with pip:

```
$ pip install pinance
```


## Usage


**Initialize**
```python
from pinance import Pinance

symbol = "AMD"
stock = Pinance(symbol)
```

**Get stock data**
```python
stock.get_quotes()
print(stock.quotes_data)
```

```javascript
// Output
{
    'exchangeTimezoneShortName': 'EDT',
    'Symbol': 'AMD',
    'LastTradeTime': '4:00pm',
    'YearHigh': '15.55',
    'DividendShare': '0.00',
    'Currency': 'USD',
    'bidSize': 7,
    'ChangePercent': '+0.21',
    'askSize': 1,
    'preMarketChangePercent': 1.0279027,
    'OneyrTargetPrice': '12.20',
    'Yield': '',
    'PriceSales': '2.95',
    'Volume': '31327634',
    'DaysHigh': '13.70',
    'messageBoardId': 'finmb_168864',
    'EPSEstimateNextQuarter': '-0.01',
    'ExtHrsLastTradeWithCurrency': '13.76',
    'fullExchangeName': 'NasdaqCM',
    'sharesOutstanding': 941398976,
    'ChangeFromYearLow': '10.17',
    'DaysLow': '13.37',
    'currency': 'USD',
    'regularMarketPreviousClose': 13.41,
    'fiftyTwoWeekLow': 3.45,
    'PEGRatio': '-1.67',
    'priceHint': 2,
    'TwoHundreddayMovingAverage': '11.02',
    'PriceEPSEstimateNextYear': '46.97',
    'marketCap': 12831267840,
    'gmtOffSetMilliseconds': -14400000,
    'LastTradePrice': '13.62',
    'YearLow': '3.45',
    'PreviousClosePrice': '13.41',
    'averageDailyVolume10Day': 35123562,
    'Name': 'Advanced Micro Devices, Inc.',
    'AverageDailyVolume': '69189000',
    'bid': 13.7,
    'fiftyTwoWeekLowChange': 10.18,
    'Change': '+0.21',
    'epsForward': 0.29,
    'ChangeFromYearHigh': '-1.93',
    'ChangeinPercent': '+1.57%',
    'quoteType': 'EQUITY',
    'quoteSourceName': 'Nasdaq Real Time Price',
    'ExtHrsChange': '+0.14',
    'marketState': 'PRE',
    'ShortRatio': '1.51',
    'regularMarketChangePercent': 1.6405687,
    'Bid': '13.67',
    'ExtHrsChangePercent': '1.03',
    'LastTradeDateTimeLong': 'Apr 27, 4:00PM EDT',
    'twoHundredDayAverageChangePercent': 0.23722452,
    'YearRange': '3.45 - 15.55',
    'ExtHrsLastTradeDateTimeLong': 'Apr 28, 5:21AM EDT',
    'exchangeTimezoneName': 'America/New_York',
    'LastTradeDateTime': '2017-04-27T16:00:01Z',
    'FiftydayMovingAverage': '13.59',
    'preMarketPrice': 13.76,
    'PercentChangeFromFiftydayMovingAverage': '+0.23%',
    'PercentChange': '+1.57%',
    'StockSymbol': 'AMD',
    'longName': 'Advanced Micro Devices,Inc.',
    'earningsTimestampStart': 1484704800,
    'sourceInterval': 15,
    'fiftyDayAverageChange': 0.040857315,
    'regularMarketOpen': 13.43,
    'Open': '13.43',
    'epsTrailingTwelveMonths': -0.6,
    'LastTradeWithTime': '4:00pm - <b>13.62</b>',
    'twoHundredDayAverage': 11.016594,
    'Change_PercentChange': '+0.21 - +1.57%',
    'PreviousClose': '13.41',
    'market': 'us_market',
    'regularMarketPrice': 13.63,
    'EPSEstimateCurrentYear': '0.08',
    'LastTradeSize': '1',
    'ExtHrsLastTradePrice': '13.76',
    'averageDailyVolume3Month': 69188977,
    'Ask': '13.74',
    'EBITDA': '-249.00M',
    'preMarketTime': 1493371275,
    'ask': 13.73,
    'PercebtChangeFromYearHigh': '-12.41%',
    'fiftyTwoWeekLowChangePercent': 2.9507246,
    'BookValue': '0.44',
    'symbol': 'AMD',
    'fiftyDayAverageChangePercent': 0.0030066145,
    'DividendYield': '0.00',
    'PriceBook': '30.13',
    'ChangeFromTwoHundreddayMovingAverage': '2.60',
    'DaysRange': '13.37 - 13.70',
    'regularMarketDayHigh': 13.7,
    'fiftyTwoWeekHighChange': -1.9200001,
    'PercentChangeFromYearLow': '+294.78%',
    'Dividend': '',
    'fiftyTwoWeekHighChangePercent': -0.123472676,
    'ChangeFromFiftydayMovingAverage': '0.03',
    'fiftyTwoWeekHigh': 15.55,
    'EPSEstimateNextYear': '0.29',
    'Index': 'NASDAQ',
    'preMarketChange': 0.14000034,
    'LastTradePriceOnly': '13.62',
    'regularMarketTime': 1493323200,
    'forwardPE': 47.0,
    'EarningsShare': '-0.60',
    'regularMarketVolume': 30351473,
    'bookValue': 0.445,
    'LastTradeDate': '4/27/2017',
    'fiftyDayAverage': 13.589143,
    'exchange': 'NCM',
    'ID': '327',
    'regularMarketChange': 0.22000027,
    'LastTradeWithCurrency': '13.62',
    'shortName': 'Advanced Micro Devices,Inc.',
    'MarketCapitalization': '12.81B',
    'twoHundredDayAverageChange': 2.6134062,
    'earningsTimestamp': 1493668800,
    'regularMarketDayLow': 13.37,
    'PercentChangeFromTwoHundreddayMovingAverage': '+23.63%',
    'earningsTimestampEnd': 1485223200,
    'PriceEPSEstimateCurrentYear': '170.25',
    'StockExchange': 'NCM',
    'priceToBook': 30.629213
}
```

**Get news**
```python
stock.get_news()
print(stock.news_data)
```

```javascript
// Output
[
   {
       'u': 'http://finance.yahoo.com/news/apos-store-advanced-micro-amd-160504758.html',
       'usg': 'AFQjCNGb8DQIPU1jyPO3XYBZfHGFIr6vjQ',
       'sru': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=http://finance.yahoo.com/news/apos-store-advanced-micro-amd-160504758.html&cid=52779472218229&ei=VxADWbHUMteVjAGT_47gBg&usg=AFQjCNHxIwMyNNqm6vg5UtfKr_35t_7UsQ',
       's': 'Yahoo Finance',
       'tt': '1493311950',
       'sp': 'Advanced Micro Devices Inc. AMD set to report first-quarter 2017 results on May 1. Notably,the company has a mixed record of earnings surprises in the trailing four quarters, with an average positive surprise of 35.76%.',
       'd': '16 hours ago',
       't': 'What&#39;s in Store for Advanced Micro (AMD) in Q1 Earnings?'
    },
    {
       'u': 'https://www.benzinga.com/analyst-ratings/analyst-color/17/04/9350958/advanced-micro-devices-traders-mind-the-goldman-gap',
       'usg': 'AFQjCNEJsNOrL2CRCAMS9aCjE-EAvRC10g',
       'sru': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://www.benzinga.com/analyst-ratings/analyst-color/17/04/9350958/advanced-micro-devices-traders-mind-the-goldman-gap&cid=52779472218229&ei=VxADWbHUMteVjAGT_47gBg&usg=AFQjCNEgwk3mxSb9k7IDLs9Id2UijOE9Gg',
       's': 'Benzinga',
       'tt': '1493234415',
       'sp': 'Advanced Micro Devices, Inc. (NASDAQ: AMD) shares have been drifting mostly sideways since Goldman Sachs issued a Sell rating and $11 price target for the stock back on April 6. Prior to the Goldman Sell rating, AMD had been one of the hottest stocks ...',
       'd': 'Apr 26, 2017',
       't': 'Advanced Micro Devices Traders Mind The &#39;Goldman Gap&#39;'
    },
    {
       'u': 'https://stocknewsjournal.com/2017/04/27/the-case-for-and-against-advanced-micro-devices-inc-amd-2/',
       'usg': 'AFQjCNFPkplQM5t3EGxze-eloSzvSX2RNQ',
       'sru': 'http://news.google.com/news/url?sa=T&ct2=us&fd=S&url=https://stocknewsjournal.com/2017/04/27/the-case-for-and-against-advanced-micro-devices-inc-amd-2/&cid=52779472218229&ei=VxADWbHUMteVjAGT_47gBg&usg=AFQjCNGFvUBOkIPPK6tOID5yNw-IIV42oQ',
       's': 'StockNewsJournal',
       'tt': '1493319375',
       'sp': 'Advanced Micro Devices, Inc. (AMD) is an interesting player in the Technology space, with a focus on Semiconductor - Broad Line.',
       'd': '14 hours ago',
       't': 'The Case for and Against Advanced Micro Devices, Inc. (AMD)'
  }
]
```

**Get options data**
```python
stock.get_options('2017-05-05', 'P', 10)
print(stock.options_data)
```

```javascript
// Output
{
    'openInterest': 0,
    'contractSize': 'REGULAR',
    'change': 0.0,
    'lastTradeDate': 1493323145,
    'impliedVolatility': 0.2500075,
    'strike': 15.0,
    'bid': 0.0,
    'inTheMoney': False,
    'lastPrice': 0.28,
    'percentChange': 0.0,
    'contractSymbol': 'AMD170505C00015000',
    'expiration': 1493942400,
    'volume': 1106,
    'ask': 0.0,
    'currency': 'USD'
}
```
