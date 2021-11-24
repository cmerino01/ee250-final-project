import requests
import json

# Animechan API: https://p.nomics.com/cryptocurrency-bitcoin-api

NOMICS_API_KEY = '0b67fd069815f50e931582968ec927530c81f1d9'

def crypto_init():
    params = {
        'key': NOMICS_API_KEY,
        'ids':'BTC'

    }

    response = requests.get('https://api.nomics.com/v1/currencies/ticker',params)

    if response.status_code == 200: # Status: OK
        data = response.json()

        # TODO: Extract the anime from the data.
        temp = data
        print(temp)
        return 1

    else:
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return None


BITCOIN_APP = {
    'name': 'BTC',
    'init': crypto_init
}


if __name__ == '__main__':
    crypto_init()
