from requests import Request, Session
import json
import pprint
import sys

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

coin = int(input("Enter coin ID: "))

sys.stdout = open('prices.xml', 'w')

parameters = {
    'id':coin,
    'convert':'USD'
}

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY': #here goes your coinmarketcap key
}

session = Session()

session.headers.update(headers)

response = session.get(url, params = parameters)

#pprint.pprint((json.loads(response.text)))

price = (json.loads(response.text)['data'][str(coin)]['quote']['USD']['price'])
#price = (json.loads(response.text))
#print("$currency_name: " + parameters['slug'] + " - " + str(price))
pprint.pprint(price)
sys.stdout.close()
