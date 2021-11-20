import cbpro
import time
from data import sandbox_key,sandbox_pass,sandbox_secret
api_url = "https://api-public.sandbox.pro.coinbase.com"

client = cbpro.AuthenticatedClient(sandbox_key,sandbox_secret,sandbox_pass, api_url = api_url)
ticker_id = 'BTC-USD'
btc_id = '20dbdb66-882f-451e-96ab-bb57a838f4cf'
usd_id = '71a6eee3-1327-4e92-8c4a-05f51e1aa9f4'

def get_size():
    #global btc_account
    btc_account = client.get_account(btc_id)
    return float(btc_account['available'])

def get_funds():
    #global usd_account
    usd_account = client.get_account(usd_id)
    return float(usd_account['available'])

def get_price():
    return float(client.get_product_ticker(ticker_id)['price'])

def get_btc_history():
    global btc_history
    btc_history = list(client.get_account_history(btc_id))

def latest_price(type):
    transactions = list(client.get_fills(product_id=ticker_id))[::-1]
    for i in transactions:
        if i['side'] == type:
            return float(i['price'])


while True:
    current_price = get_price()
    buy_price = latest_price('buy')
    sell_price = latest_price('sell')
    if (current_price - buy_price)/buy_price > 0.03:
        client.place_market_order(ticker_id, side ='sell', size = get_size())
        print("Sold at a profit")
    elif (sell_price - current_price)/current_price > 0.03:
        client.place_market_order(ticker_id, side ='buy', funds = get_funds())
        print("Bought at lower cost")
    else:
        print('Passing')
    time.sleep(30)
