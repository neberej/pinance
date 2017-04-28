pinance
=========

A collection of python modules to get finance data (stock quotes, news and options)

## Installation

* From PyPI with pip

```
pip install pinance
```

* From repo

```
$ git clone git://github.com/neberej/pinance.git
```

## Modules list

* yfinance
* yfinance2
* gfinance
* gfinance.py


## Usage

```
// Initialize
symbol = "AMD"
stock = Pinance(symbol)

# Get stock data
stock.get_quotes()
print(stock.quotes_data)

# Get news
stock.get_news()
print(stock.news_data)

#Get Option data
stock.get_options('2017-04-14', 'P', 10)
print(stock.options_data)
```