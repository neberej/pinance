
from setuptools import setup

from distutils.core import setup
setup(
  name = 'pinance',
  packages = ['pinance'],
  version = '0.1',
  description = 'A collection of python modules to get finance data (stock quotes, news and options)',
  author = 'NT (neberej)',
  author_email = 'mail@vguh.com',
  url = 'https://github.com/neberej/pinance',
  download_url = 'https://github.com/neberej/pinance/archive/0.1.tar.gz',
  keywords = ['stock', 'options', 'finance', 'trade', 'market-data', 'python', 'yahoo-finance-api', 'google-finance'],
  classifiers = [

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Intended Audience :: Financial and Insurance Industry',
    'Topic :: Office/Business :: Financial :: Investment',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Operating System :: OS Independent',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
  ],
  install_requires=['demjson', 'simplejson', 'pytz', 'datetime', 're', 'urllib', 'random', 'Request', 'json', 'urlopen']
)

