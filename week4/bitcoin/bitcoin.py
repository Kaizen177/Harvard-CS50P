
import requests
import sys




try:
    n=float(sys.argv[1])
except ValueError :
    sys.exit('Command-line argument is not a number')

except TypeError :
    sys.exit('Missing command-line argument')
else:
    infos=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    price=infos['bpi']['USD']['rate'].replace(',','')
    x=n*float(price)
    formatted_value = "${:,.4f}".format(x)
    print(formatted_value)
