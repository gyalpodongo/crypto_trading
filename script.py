from coinbase.wallet.client import Client
from time import sleep
from data import api_key, api_secret

#Some coinbase guidance https://developers.coinbase.com/docs/wallet/guides/buy-sell

def percentage_change(a : float,b: float) -> float:
    """
    Takes two floats and returns their percentage change
    """
    return (a-b)/a * 100

#setting our client to link our account to our code
client = Client(api_key,api_secret)
#payment_method = client.get_payment_methods()[0] #Gets main form of payment from your coinbase account

#Following lines get inputs from the user such as the currency they use, the limit order and the amount spent
currency_code= str(input("What currency are you using? (Please enter in 3 character valid format e.g. USD): "))

user_limit_order = float(input(f"Enter a price for your bitcoin limit order in {currency_code}: "))

user_amount_spent = float(input(f"Enter how much you want to spend in {currency_code} :"))

start_price = client.get_spot_price(currency = currency_code)

while True:
    #Reset current values and finds percentage changes
    buy_price = client.get_buy_price(currency = currency_code)
    percentage_gainloss = percentage_change(start_price.amount, buy_price.amount)
    