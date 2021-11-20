import cbpro
import time
from data import sandbox_key,sandbox_pass,sandbox_secret,btc_id,usd_id
api_url = "https://api-public.sandbox.pro.coinbase.com"

client = cbpro.AuthenticatedClient(sandbox_key,sandbox_secret,sandbox_pass, api_url = api_url)
ticker_id = 'BTC-USD'


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
    latest_buy_price = latest_price('buy')
    latest_sell_price = latest_price('sell')
    size = get_size()
    funds = get_funds()
    sell_change = (current_price - latest_buy_price)/latest_buy_price 
    buy_change = (latest_sell_price - current_price)/latest_sell_price
    if sell_change > 0.03 and size > 0.000021: 
        response = client.place_market_order(ticker_id, side ='sell', size = size)
        print(response)
        print("Sold at a profit")
    elif buy_change  > 0.03 and funds > 10:
        response = client.place_market_order(ticker_id, side ='buy', funds = funds)
        print(response)
        print("Bought at lower cost")
    else:
        print('Passing')
    time.sleep(10)
