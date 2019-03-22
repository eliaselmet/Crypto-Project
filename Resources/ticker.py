import poloniex
from datetime import datetime

# TODO: put your API key and secret in a file, separate them with commas.
# Put it in the same directory and call it key.txt.
f = file('key.txt', 'r')
pair = f.read().split(',')

key = pair[0]
secret = pair[1]

p = poloniex.poloniex(key, secret)

# make request to poloniex tick data API.
# ret is a dictionary containing various pieces of data for different symbols.
ret = p.returnTicker()

for item in ret:
	# this only looks at BTC_* or USDT_BTC. You can change these or just take out the if statement.
    if item.startswith('BTC') or item.startswith('USDT_BTC'):
		theDict = ret[item]
		
		currencyPairData = {'timestamp': datetime.now(), 'symbol': item, 'last': theDict['last'], 'quoteVolume': theDict['quoteVolume'],
                       'high24hr': theDict['high24hr'], 'highestBid': theDict['highestBid'], 'percentChange': theDict['percentChange'],
					   'low24hr': theDict['low24hr'], 'lowestAsk': theDict['lowestAsk'], 'baseVolume': theDict['baseVolume']}
		
		# this is one data point. so you can do whatever you want with it at that point.
		# store it in a database, write it to a csv file, use it to do calculations, whatever...
		print currencyPairData